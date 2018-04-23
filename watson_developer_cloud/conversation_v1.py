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
The IBM Watson Conversation service combines machine learning, natural language
understanding, and integrated dialog tools to create conversation flows between your apps
and your users.
"""

from __future__ import absolute_import

import json
from .watson_service import datetime_to_string, string_to_datetime
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class ConversationV1(WatsonService):
    """The Conversation V1 service."""

    default_url = 'https://gateway.watsonplatform.net/conversation/api'

    def __init__(self,
                 version,
                 url=default_url,
                 username=None,
                 password=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
        """
        Construct a new client for the Conversation service.

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

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway.watsonplatform.net/conversation/api").
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
            vcap_services_name='conversation',
            url=url,
            username=username,
            password=password,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)
        self.version = version

    #########################
    # Message
    #########################

    def message(self,
                workspace_id,
                input=None,
                alternate_intents=None,
                context=None,
                entities=None,
                intents=None,
                output=None,
                nodes_visited_details=None,
                **kwargs):
        """
        Get response to user input.

        Get a response to a user's input.    There is no rate limit for this operation.

        :param str workspace_id: Unique identifier of the workspace.
        :param InputData input: An input object that includes the input text.
        :param bool alternate_intents: Whether to return more than one intent. Set to `true` to return all matching intents.
        :param Context context: State information for the conversation. Continue a conversation by including the context object from the previous response.
        :param list[RuntimeEntity] entities: Entities to use when evaluating the message. Include entities from the previous response to continue using those entities rather than detecting entities in the new input.
        :param list[RuntimeIntent] intents: Intents to use when evaluating the user input. Include intents from the previous response to continue using those intents rather than trying to recognize intents in the new input.
        :param OutputData output: System output. Include the output from the previous response to maintain intermediate information over multiple requests.
        :param bool nodes_visited_details: Whether to include additional diagnostic information about the dialog nodes that were visited during processing of the message.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `MessageResponse` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if input is not None:
            input = self._convert_model(input, InputData)
        if context is not None:
            context = self._convert_model(context, Context)
        if entities is not None:
            entities = [
                self._convert_model(x, RuntimeEntity) for x in entities
            ]
        if intents is not None:
            intents = [self._convert_model(x, RuntimeIntent) for x in intents]
        if output is not None:
            output = self._convert_model(output, OutputData)
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'nodes_visited_details': nodes_visited_details
        }
        data = {
            'input': input,
            'alternate_intents': alternate_intents,
            'context': context,
            'entities': entities,
            'intents': intents,
            'output': output
        }
        url = '/v1/workspaces/{0}/message'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Workspaces
    #########################

    def create_workspace(self,
                         name=None,
                         description=None,
                         language=None,
                         intents=None,
                         entities=None,
                         dialog_nodes=None,
                         counterexamples=None,
                         metadata=None,
                         learning_opt_out=None,
                         **kwargs):
        """
        Create workspace.

        Create a workspace based on component objects. You must provide workspace
        components defining the content of the new workspace.    This operation is limited
        to 30 requests per 30 minutes. For more information, see **Rate limiting**.

        :param str name: The name of the workspace. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 64 characters.
        :param str description: The description of the workspace. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param str language: The language of the workspace.
        :param list[CreateIntent] intents: An array of objects defining the intents for the workspace.
        :param list[CreateEntity] entities: An array of objects defining the entities for the workspace.
        :param list[CreateDialogNode] dialog_nodes: An array of objects defining the nodes in the workspace dialog.
        :param list[CreateCounterexample] counterexamples: An array of objects defining input examples that have been marked as irrelevant input.
        :param object metadata: Any metadata related to the workspace.
        :param bool learning_opt_out: Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Workspace` response.
        :rtype: dict
        """
        if intents is not None:
            intents = [self._convert_model(x, CreateIntent) for x in intents]
        if entities is not None:
            entities = [self._convert_model(x, CreateEntity) for x in entities]
        if dialog_nodes is not None:
            dialog_nodes = [
                self._convert_model(x, CreateDialogNode) for x in dialog_nodes
            ]
        if counterexamples is not None:
            counterexamples = [
                self._convert_model(x, CreateCounterexample)
                for x in counterexamples
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'name': name,
            'description': description,
            'language': language,
            'intents': intents,
            'entities': entities,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out
        }
        url = '/v1/workspaces'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_workspace(self, workspace_id, **kwargs):
        """
        Delete workspace.

        Delete a workspace from the service instance.    This operation is limited to 30
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/workspaces/{0}'.format(
            *self._encode_path_vars(workspace_id))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_workspace(self,
                      workspace_id,
                      export=None,
                      include_audit=None,
                      **kwargs):
        """
        Get information about a workspace.

        Get information about a workspace, optionally including all workspace content.
        With **export**=`false`, this operation is limited to 6000 requests per 5 minutes.
        With **export**=`true`, the limit is 20 requests per 30 minutes. For more
        information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: Whether to include all element content in the returned data. If **export**=`false`, the returned data includes only information about the element itself. If **export**=`true`, all content, including subelements, is included.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `WorkspaceExport` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_workspaces(self,
                        page_limit=None,
                        include_count=None,
                        sort=None,
                        cursor=None,
                        include_audit=None,
                        **kwargs):
        """
        List workspaces.

        List the workspaces associated with a Conversation service instance.    This
        operation is limited to 500 requests per 30 minutes. For more information, see
        **Rate limiting**.

        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `WorkspaceCollection` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_workspace(self,
                         workspace_id,
                         name=None,
                         description=None,
                         language=None,
                         intents=None,
                         entities=None,
                         dialog_nodes=None,
                         counterexamples=None,
                         metadata=None,
                         learning_opt_out=None,
                         append=None,
                         **kwargs):
        """
        Update workspace.

        Update an existing workspace with new or modified data. You must provide component
        objects defining the content of the updated workspace.    This operation is
        limited to 30 request per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str name: The name of the workspace. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 64 characters.
        :param str description: The description of the workspace. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param str language: The language of the workspace.
        :param list[CreateIntent] intents: An array of objects defining the intents for the workspace.
        :param list[CreateEntity] entities: An array of objects defining the entities for the workspace.
        :param list[CreateDialogNode] dialog_nodes: An array of objects defining the nodes in the workspace dialog.
        :param list[CreateCounterexample] counterexamples: An array of objects defining input examples that have been marked as irrelevant input.
        :param object metadata: Any metadata related to the workspace.
        :param bool learning_opt_out: Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
        :param bool append: Whether the new data is to be appended to the existing data in the workspace. If **append**=`false`, elements included in the new data completely replace the corresponding existing elements, including all subelements. For example, if the new data includes **entities** and **append**=`false`, all existing entities in the workspace are discarded and replaced with the new entities.    If **append**=`true`, existing elements are preserved, and the new elements are added. If any elements in the new data collide with existing elements, the update request fails.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Workspace` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intents is not None:
            intents = [self._convert_model(x, CreateIntent) for x in intents]
        if entities is not None:
            entities = [self._convert_model(x, CreateEntity) for x in entities]
        if dialog_nodes is not None:
            dialog_nodes = [
                self._convert_model(x, CreateDialogNode) for x in dialog_nodes
            ]
        if counterexamples is not None:
            counterexamples = [
                self._convert_model(x, CreateCounterexample)
                for x in counterexamples
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version, 'append': append}
        data = {
            'name': name,
            'description': description,
            'language': language,
            'intents': intents,
            'entities': entities,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out
        }
        url = '/v1/workspaces/{0}'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Intents
    #########################

    def create_intent(self,
                      workspace_id,
                      intent,
                      description=None,
                      examples=None,
                      **kwargs):
        """
        Create intent.

        Create a new intent.    This operation is limited to 2000 requests per 30 minutes.
        For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The name of the intent. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, hyphen, and dot characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 128 characters.
        :param str description: The description of the intent. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param list[CreateExample] examples: An array of user input examples for the intent.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Intent` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if examples is not None:
            examples = [
                self._convert_model(x, CreateExample) for x in examples
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'intent': intent,
            'description': description,
            'examples': examples
        }
        url = '/v1/workspaces/{0}/intents'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_intent(self, workspace_id, intent, **kwargs):
        """
        Delete intent.

        Delete an intent from a workspace.    This operation is limited to 2000 requests
        per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/intents/{1}'.format(*self._encode_path_vars(
            workspace_id, intent))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_intent(self,
                   workspace_id,
                   intent,
                   export=None,
                   include_audit=None,
                   **kwargs):
        """
        Get intent.

        Get information about an intent, optionally including all intent content.    With
        **export**=`false`, this operation is limited to 6000 requests per 5 minutes. With
        **export**=`true`, the limit is 400 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param bool export: Whether to include all element content in the returned data. If **export**=`false`, the returned data includes only information about the element itself. If **export**=`true`, all content, including subelements, is included.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `IntentExport` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/intents/{1}'.format(*self._encode_path_vars(
            workspace_id, intent))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_intents(self,
                     workspace_id,
                     export=None,
                     page_limit=None,
                     include_count=None,
                     sort=None,
                     cursor=None,
                     include_audit=None,
                     **kwargs):
        """
        List intents.

        List the intents for a workspace.    With **export**=`false`, this operation is
        limited to 2000 requests per 30 minutes. With **export**=`true`, the limit is 400
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: Whether to include all element content in the returned data. If **export**=`false`, the returned data includes only information about the element itself. If **export**=`true`, all content, including subelements, is included.
        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `IntentCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/intents'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_intent(self,
                      workspace_id,
                      intent,
                      new_intent=None,
                      new_description=None,
                      new_examples=None,
                      **kwargs):
        """
        Update intent.

        Update an existing intent with new or modified data. You must provide component
        objects defining the content of the updated intent.    This operation is limited
        to 2000 requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str new_intent: The name of the intent. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, hyphen, and dot characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 128 characters.
        :param str new_description: The description of the intent.
        :param list[CreateExample] new_examples: An array of user input examples for the intent.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Intent` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if new_examples is not None:
            new_examples = [
                self._convert_model(x, CreateExample) for x in new_examples
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'intent': new_intent,
            'description': new_description,
            'examples': new_examples
        }
        url = '/v1/workspaces/{0}/intents/{1}'.format(*self._encode_path_vars(
            workspace_id, intent))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Examples
    #########################

    def create_example(self, workspace_id, intent, text, **kwargs):
        """
        Create user input example.

        Add a new user input example to an intent.    This operation is limited to 1000
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of a user input example. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 1024 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Example` response.
        :rtype: dict
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
        params = {'version': self.version}
        data = {'text': text}
        url = '/v1/workspaces/{0}/intents/{1}/examples'.format(
            *self._encode_path_vars(workspace_id, intent))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_example(self, workspace_id, intent, text, **kwargs):
        """
        Delete user input example.

        Delete a user input example from an intent.    This operation is limited to 1000
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_example(self,
                    workspace_id,
                    intent,
                    text,
                    include_audit=None,
                    **kwargs):
        """
        Get user input example.

        Get information about a user input example.    This operation is limited to 6000
        requests per 5 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Example` response.
        :rtype: dict
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
        params = {'version': self.version, 'include_audit': include_audit}
        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_examples(self,
                      workspace_id,
                      intent,
                      page_limit=None,
                      include_count=None,
                      sort=None,
                      cursor=None,
                      include_audit=None,
                      **kwargs):
        """
        List user input examples.

        List the user input examples for an intent.    This operation is limited to 2500
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ExampleCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/intents/{1}/examples'.format(
            *self._encode_path_vars(workspace_id, intent))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_example(self,
                       workspace_id,
                       intent,
                       text,
                       new_text=None,
                       **kwargs):
        """
        Update user input example.

        Update the text of a user input example.    This operation is limited to 1000
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param str new_text: The text of the user input example. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 1024 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Example` response.
        :rtype: dict
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
        params = {'version': self.version}
        data = {'text': new_text}
        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Counterexamples
    #########################

    def create_counterexample(self, workspace_id, text, **kwargs):
        """
        Create counterexample.

        Add a new counterexample to a workspace. Counterexamples are examples that have
        been marked as irrelevant input.    This operation is limited to 1000 requests per
        30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input marked as irrelevant input. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters  - It cannot consist of only whitespace characters  - It must be no longer than 1024 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Counterexample` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'text': text}
        url = '/v1/workspaces/{0}/counterexamples'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_counterexample(self, workspace_id, text, **kwargs):
        """
        Delete counterexample.

        Delete a counterexample from a workspace. Counterexamples are examples that have
        been marked as irrelevant input.    This operation is limited to 1000 requests per
        30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example, `What are you wearing?`).
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_counterexample(self,
                           workspace_id,
                           text,
                           include_audit=None,
                           **kwargs):
        """
        Get counterexample.

        Get information about a counterexample. Counterexamples are examples that have
        been marked as irrelevant input.    This operation is limited to 6000 requests per
        5 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example, `What are you wearing?`).
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Counterexample` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version, 'include_audit': include_audit}
        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_counterexamples(self,
                             workspace_id,
                             page_limit=None,
                             include_count=None,
                             sort=None,
                             cursor=None,
                             include_audit=None,
                             **kwargs):
        """
        List counterexamples.

        List the counterexamples for a workspace. Counterexamples are examples that have
        been marked as irrelevant input.    This operation is limited to 2500 requests per
        30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `CounterexampleCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/counterexamples'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_counterexample(self,
                              workspace_id,
                              text,
                              new_text=None,
                              **kwargs):
        """
        Update counterexample.

        Update the text of a counterexample. Counterexamples are examples that have been
        marked as irrelevant input.    This operation is limited to 1000 requests per 30
        minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example, `What are you wearing?`).
        :param str new_text: The text of a user input counterexample.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Counterexample` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'text': new_text}
        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Entities
    #########################

    def create_entity(self,
                      workspace_id,
                      entity,
                      description=None,
                      metadata=None,
                      values=None,
                      fuzzy_match=None,
                      **kwargs):
        """
        Create entity.

        Create a new entity.    This operation is limited to 1000 requests per 30 minutes.
        For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, and hyphen characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 64 characters.
        :param str description: The description of the entity. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param object metadata: Any metadata related to the value.
        :param list[CreateValue] values: An array of objects describing the entity values.
        :param bool fuzzy_match: Whether to use fuzzy matching for the entity.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Entity` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if values is not None:
            values = [self._convert_model(x, CreateValue) for x in values]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'entity': entity,
            'description': description,
            'metadata': metadata,
            'values': values,
            'fuzzy_match': fuzzy_match
        }
        url = '/v1/workspaces/{0}/entities'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_entity(self, workspace_id, entity, **kwargs):
        """
        Delete entity.

        Delete an entity from a workspace.    This operation is limited to 1000 requests
        per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/entities/{1}'.format(*self._encode_path_vars(
            workspace_id, entity))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_entity(self,
                   workspace_id,
                   entity,
                   export=None,
                   include_audit=None,
                   **kwargs):
        """
        Get entity.

        Get information about an entity, optionally including all entity content.    With
        **export**=`false`, this operation is limited to 6000 requests per 5 minutes. With
        **export**=`true`, the limit is 200 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param bool export: Whether to include all element content in the returned data. If **export**=`false`, the returned data includes only information about the element itself. If **export**=`true`, all content, including subelements, is included.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `EntityExport` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/entities/{1}'.format(*self._encode_path_vars(
            workspace_id, entity))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_entities(self,
                      workspace_id,
                      export=None,
                      page_limit=None,
                      include_count=None,
                      sort=None,
                      cursor=None,
                      include_audit=None,
                      **kwargs):
        """
        List entities.

        List the entities for a workspace.    With **export**=`false`, this operation is
        limited to 1000 requests per 30 minutes. With **export**=`true`, the limit is 200
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: Whether to include all element content in the returned data. If **export**=`false`, the returned data includes only information about the element itself. If **export**=`true`, all content, including subelements, is included.
        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `EntityCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/entities'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_entity(self,
                      workspace_id,
                      entity,
                      new_entity=None,
                      new_description=None,
                      new_metadata=None,
                      new_fuzzy_match=None,
                      new_values=None,
                      **kwargs):
        """
        Update entity.

        Update an existing entity with new or modified data. You must provide component
        objects defining the content of the updated entity.    This operation is limited
        to 1000 requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str new_entity: The name of the entity. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, and hyphen characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 64 characters.
        :param str new_description: The description of the entity. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param object new_metadata: Any metadata related to the entity.
        :param bool new_fuzzy_match: Whether to use fuzzy matching for the entity.
        :param list[CreateValue] new_values: An array of entity values.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Entity` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if new_values is not None:
            new_values = [
                self._convert_model(x, CreateValue) for x in new_values
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'entity': new_entity,
            'description': new_description,
            'metadata': new_metadata,
            'fuzzy_match': new_fuzzy_match,
            'values': new_values
        }
        url = '/v1/workspaces/{0}/entities/{1}'.format(*self._encode_path_vars(
            workspace_id, entity))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Values
    #########################

    def create_value(self,
                     workspace_id,
                     entity,
                     value,
                     metadata=None,
                     synonyms=None,
                     patterns=None,
                     value_type=None,
                     **kwargs):
        """
        Add entity value.

        Create a new value for an entity.    This operation is limited to 1000 requests
        per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param object metadata: Any metadata related to the entity value.
        :param list[str] synonyms: An array containing any synonyms for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A synonym must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param list[str] patterns: An array of patterns for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A pattern is a regular expression no longer than 128 characters. For more information about how to specify a pattern, see the [documentation](https://console.bluemix.net/docs/services/conversation/entities.html#creating-entities).
        :param str value_type: Specifies the type of value.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Value` response.
        :rtype: dict
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
        params = {'version': self.version}
        data = {
            'value': value,
            'metadata': metadata,
            'synonyms': synonyms,
            'patterns': patterns,
            'type': value_type
        }
        url = '/v1/workspaces/{0}/entities/{1}/values'.format(
            *self._encode_path_vars(workspace_id, entity))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_value(self, workspace_id, entity, value, **kwargs):
        """
        Delete entity value.

        Delete a value from an entity.    This operation is limited to 1000 requests per
        30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_value(self,
                  workspace_id,
                  entity,
                  value,
                  export=None,
                  include_audit=None,
                  **kwargs):
        """
        Get entity value.

        Get information about an entity value.    This operation is limited to 6000
        requests per 5 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param bool export: Whether to include all element content in the returned data. If **export**=`false`, the returned data includes only information about the element itself. If **export**=`true`, all content, including subelements, is included.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ValueExport` response.
        :rtype: dict
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
        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_values(self,
                    workspace_id,
                    entity,
                    export=None,
                    page_limit=None,
                    include_count=None,
                    sort=None,
                    cursor=None,
                    include_audit=None,
                    **kwargs):
        """
        List entity values.

        List the values for an entity.    This operation is limited to 2500 requests per
        30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param bool export: Whether to include all element content in the returned data. If **export**=`false`, the returned data includes only information about the element itself. If **export**=`true`, all content, including subelements, is included.
        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ValueCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/entities/{1}/values'.format(
            *self._encode_path_vars(workspace_id, entity))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_value(self,
                     workspace_id,
                     entity,
                     value,
                     new_value=None,
                     new_metadata=None,
                     new_type=None,
                     new_synonyms=None,
                     new_patterns=None,
                     **kwargs):
        """
        Update entity value.

        Update an existing entity value with new or modified data. You must provide
        component objects defining the content of the updated entity value.    This
        operation is limited to 1000 requests per 30 minutes. For more information, see
        **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str new_value: The text of the entity value. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param object new_metadata: Any metadata related to the entity value.
        :param str new_type: Specifies the type of value.
        :param list[str] new_synonyms: An array of synonyms for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A synonym must conform to the following resrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param list[str] new_patterns: An array of patterns for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A pattern is a regular expression no longer than 128 characters. For more information about how to specify a pattern, see the [documentation](https://console.bluemix.net/docs/services/conversation/entities.html#creating-entities).
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Value` response.
        :rtype: dict
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
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Synonyms
    #########################

    def create_synonym(self, workspace_id, entity, value, synonym, **kwargs):
        """
        Add entity value synonym.

        Add a new synonym to an entity value.    This operation is limited to 1000
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Synonym` response.
        :rtype: dict
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
        params = {'version': self.version}
        data = {'synonym': synonym}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_synonym(self, workspace_id, entity, value, synonym, **kwargs):
        """
        Delete entity value synonym.

        Delete a synonym from an entity value.    This operation is limited to 1000
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_synonym(self,
                    workspace_id,
                    entity,
                    value,
                    synonym,
                    include_audit=None,
                    **kwargs):
        """
        Get entity value synonym.

        Get information about a synonym of an entity value.    This operation is limited
        to 6000 requests per 5 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Synonym` response.
        :rtype: dict
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
        params = {'version': self.version, 'include_audit': include_audit}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_synonyms(self,
                      workspace_id,
                      entity,
                      value,
                      page_limit=None,
                      include_count=None,
                      sort=None,
                      cursor=None,
                      include_audit=None,
                      **kwargs):
        """
        List entity value synonyms.

        List the synonyms for an entity value.    This operation is limited to 2500
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `SynonymCollection` response.
        :rtype: dict
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
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_synonym(self,
                       workspace_id,
                       entity,
                       value,
                       synonym,
                       new_synonym=None,
                       **kwargs):
        """
        Update entity value synonym.

        Update an existing entity value synonym with new text.    This operation is
        limited to 1000 requests per 30 minutes. For more information, see **Rate
        limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param str new_synonym: The text of the synonym. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Synonym` response.
        :rtype: dict
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
        params = {'version': self.version}
        data = {'synonym': new_synonym}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Dialog nodes
    #########################

    def create_dialog_node(self,
                           workspace_id,
                           dialog_node,
                           description=None,
                           conditions=None,
                           parent=None,
                           previous_sibling=None,
                           output=None,
                           context=None,
                           metadata=None,
                           next_step=None,
                           actions=None,
                           title=None,
                           node_type=None,
                           event_name=None,
                           variable=None,
                           digress_in=None,
                           digress_out=None,
                           digress_out_slots=None,
                           **kwargs):
        """
        Create dialog node.

        Create a new dialog node.    This operation is limited to 500 requests per 30
        minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 1024 characters.
        :param str description: The description of the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param str conditions: The condition that will trigger the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 2048 characters.
        :param str parent: The ID of the parent dialog node.
        :param str previous_sibling: The ID of the previous dialog node.
        :param object output: The output of the dialog node. For more information about how to specify dialog node output, see the [documentation](https://console.bluemix.net/docs/services/conversation/dialog-overview.html#complex).
        :param object context: The context for the dialog node.
        :param object metadata: The metadata for the dialog node.
        :param DialogNodeNextStep next_step: The next step to be executed in dialog processing.
        :param list[DialogNodeAction] actions: An array of objects describing any actions to be invoked by the dialog node.
        :param str title: The alias used to identify the dialog node. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 64 characters.
        :param str node_type: How the dialog node is processed.
        :param str event_name: How an `event_handler` node is processed.
        :param str variable: The location in the dialog context where output is stored.
        :param str digress_in: Whether this top-level dialog node can be digressed into.
        :param str digress_out: Whether this dialog node can be returned to after a digression.
        :param str digress_out_slots: Whether the user can digress to top-level nodes while filling out slots.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DialogNode` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        if next_step is not None:
            next_step = self._convert_model(next_step, DialogNodeNextStep)
        if actions is not None:
            actions = [
                self._convert_model(x, DialogNodeAction) for x in actions
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
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
            'actions': actions,
            'title': title,
            'type': node_type,
            'event_name': event_name,
            'variable': variable,
            'digress_in': digress_in,
            'digress_out': digress_out,
            'digress_out_slots': digress_out_slots
        }
        url = '/v1/workspaces/{0}/dialog_nodes'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_dialog_node(self, workspace_id, dialog_node, **kwargs):
        """
        Delete dialog node.

        Delete a dialog node from a workspace.    This operation is limited to 500
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_dialog_node(self,
                        workspace_id,
                        dialog_node,
                        include_audit=None,
                        **kwargs):
        """
        Get dialog node.

        Get information about a dialog node.    This operation is limited to 6000 requests
        per 5 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DialogNode` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version, 'include_audit': include_audit}
        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_dialog_nodes(self,
                          workspace_id,
                          page_limit=None,
                          include_count=None,
                          sort=None,
                          cursor=None,
                          include_audit=None,
                          **kwargs):
        """
        List dialog nodes.

        List the dialog nodes for a workspace.    This operation is limited to 2500
        requests per 30 minutes. For more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param int page_limit: The number of records to return in each page of results.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str cursor: A token identifying the page of results to retrieve.
        :param bool include_audit: Whether to include the audit properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DialogNodeCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }
        url = '/v1/workspaces/{0}/dialog_nodes'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_dialog_node(self,
                           workspace_id,
                           dialog_node,
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
                           **kwargs):
        """
        Update dialog node.

        Update an existing dialog node with new or modified data.    This operation is
        limited to 500 requests per 30 minutes. For more information, see **Rate
        limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :param str new_dialog_node: The dialog node ID. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 1024 characters.
        :param str new_description: The description of the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param str new_conditions: The condition that will trigger the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 2048 characters.
        :param str new_parent: The ID of the parent dialog node.
        :param str new_previous_sibling: The ID of the previous sibling dialog node.
        :param object new_output: The output of the dialog node. For more information about how to specify dialog node output, see the [documentation](https://console.bluemix.net/docs/services/conversation/dialog-overview.html#complex).
        :param object new_context: The context for the dialog node.
        :param object new_metadata: The metadata for the dialog node.
        :param DialogNodeNextStep new_next_step: The next step to be executed in dialog processing.
        :param str new_title: The alias used to identify the dialog node. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 64 characters.
        :param str new_type: How the dialog node is processed.
        :param str new_event_name: How an `event_handler` node is processed.
        :param str new_variable: The location in the dialog context where output is stored.
        :param list[DialogNodeAction] new_actions: An array of objects describing any actions to be invoked by the dialog node.
        :param str new_digress_in: Whether this top-level dialog node can be digressed into.
        :param str new_digress_out: Whether this dialog node can be returned to after a digression.
        :param str new_digress_out_slots: Whether the user can digress to top-level nodes while filling out slots.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DialogNode` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        if new_next_step is not None:
            new_next_step = self._convert_model(new_next_step,
                                                DialogNodeNextStep)
        if new_actions is not None:
            new_actions = [
                self._convert_model(x, DialogNodeAction) for x in new_actions
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
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
            'digress_out_slots': new_digress_out_slots
        }
        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Logs
    #########################

    def list_all_logs(self,
                      filter,
                      sort=None,
                      page_limit=None,
                      cursor=None,
                      **kwargs):
        """
        List log events in all workspaces.

        List the events from the logs of all workspaces in the service instance.    If
        **cursor** is not specified, this operation is limited to 40 requests per 30
        minutes. If **cursor** is specified, the limit is 120 requests per minute. For
        more information, see **Rate limiting**.

        :param str filter: A cacheable parameter that limits the results to those matching the specified filter. You must specify a filter query that includes a value for `language`, as well as a value for `workspace_id` or `request.context.metadata.deployment`. For more information, see the [documentation](https://console.bluemix.net/docs/services/conversation/filter-reference.html#filter-query-syntax).
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param int page_limit: The number of records to return in each page of results.
        :param str cursor: A token identifying the page of results to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `LogCollection` response.
        :rtype: dict
        """
        if filter is None:
            raise ValueError('filter must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'filter': filter,
            'sort': sort,
            'page_limit': page_limit,
            'cursor': cursor
        }
        url = '/v1/logs'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_logs(self,
                  workspace_id,
                  sort=None,
                  filter=None,
                  page_limit=None,
                  cursor=None,
                  **kwargs):
        """
        List log events in a workspace.

        List the events from the log of a specific workspace.    If **cursor** is not
        specified, this operation is limited to 40 requests per 30 minutes. If **cursor**
        is specified, the limit is 120 requests per minute. For more information, see
        **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str sort: The attribute by which returned results will be sorted. To reverse the sort order, prefix the value with a minus sign (`-`). Supported values are `name`, `updated`, and `workspace_id`.
        :param str filter: A cacheable parameter that limits the results to those matching the specified filter. For more information, see the [documentation](https://console.bluemix.net/docs/services/conversation/filter-reference.html#filter-query-syntax).
        :param int page_limit: The number of records to return in each page of results.
        :param str cursor: A token identifying the page of results to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `LogCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'sort': sort,
            'filter': filter,
            'page_limit': page_limit,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/logs'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class CaptureGroup(object):
    """
    CaptureGroup.

    :attr str group: A recognized capture group for the entity.
    :attr list[int] location: (optional) Zero-based character offsets that indicate where the entity value begins and ends in the input text.
    """

    def __init__(self, group, location=None):
        """
        Initialize a CaptureGroup object.

        :param str group: A recognized capture group for the entity.
        :param list[int] location: (optional) Zero-based character offsets that indicate where the entity value begins and ends in the input text.
        """
        self.group = group
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
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


class Context(object):
    """
    State information for the conversation. To maintain state, include the context from
    the previous response.

    :attr str conversation_id: (optional) The unique identifier of the conversation.
    :attr SystemResponse system: (optional) For internal use only.
    """

    def __init__(self, conversation_id=None, system=None, **kwargs):
        """
        Initialize a Context object.

        :param str conversation_id: (optional) The unique identifier of the conversation.
        :param SystemResponse system: (optional) For internal use only.
        :param **kwargs: (optional) Any additional properties.
        """
        self.conversation_id = conversation_id
        self.system = system
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
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'conversation_id', 'system'}
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


class Counterexample(object):
    """
    Counterexample.

    :attr str text: The text of the counterexample.
    :attr datetime created: (optional) The timestamp for creation of the counterexample.
    :attr datetime updated: (optional) The timestamp for the last update to the counterexample.
    """

    def __init__(self, text, created=None, updated=None):
        """
        Initialize a Counterexample object.

        :param str text: The text of the counterexample.
        :param datetime created: (optional) The timestamp for creation of the counterexample.
        :param datetime updated: (optional) The timestamp for the last update to the counterexample.
        """
        self.text = text
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Counterexample object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in Counterexample JSON'
            )
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


class CounterexampleCollection(object):
    """
    CounterexampleCollection.

    :attr list[Counterexample] counterexamples: An array of objects describing the examples marked as irrelevant input.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, counterexamples, pagination):
        """
        Initialize a CounterexampleCollection object.

        :param list[Counterexample] counterexamples: An array of objects describing the examples marked as irrelevant input.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.counterexamples = counterexamples
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CounterexampleCollection object from a json dictionary."""
        args = {}
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


class CreateCounterexample(object):
    """
    CreateCounterexample.

    :attr str text: The text of a user input marked as irrelevant input. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters  - It cannot consist of only whitespace characters  - It must be no longer than 1024 characters.
    """

    def __init__(self, text):
        """
        Initialize a CreateCounterexample object.

        :param str text: The text of a user input marked as irrelevant input. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters  - It cannot consist of only whitespace characters  - It must be no longer than 1024 characters.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateCounterexample object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in CreateCounterexample JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this CreateCounterexample object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateDialogNode(object):
    """
    CreateDialogNode.

    :attr str dialog_node: The dialog node ID. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 1024 characters.
    :attr str description: (optional) The description of the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
    :attr str conditions: (optional) The condition that will trigger the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 2048 characters.
    :attr str parent: (optional) The ID of the parent dialog node.
    :attr str previous_sibling: (optional) The ID of the previous dialog node.
    :attr object output: (optional) The output of the dialog node. For more information about how to specify dialog node output, see the [documentation](https://console.bluemix.net/docs/services/conversation/dialog-overview.html#complex).
    :attr object context: (optional) The context for the dialog node.
    :attr object metadata: (optional) The metadata for the dialog node.
    :attr DialogNodeNextStep next_step: (optional) The next step to be executed in dialog processing.
    :attr list[DialogNodeAction] actions: (optional) An array of objects describing any actions to be invoked by the dialog node.
    :attr str title: (optional) The alias used to identify the dialog node. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 64 characters.
    :attr str node_type: (optional) How the dialog node is processed.
    :attr str event_name: (optional) How an `event_handler` node is processed.
    :attr str variable: (optional) The location in the dialog context where output is stored.
    :attr str digress_in: (optional) Whether this top-level dialog node can be digressed into.
    :attr str digress_out: (optional) Whether this dialog node can be returned to after a digression.
    :attr str digress_out_slots: (optional) Whether the user can digress to top-level nodes while filling out slots.
    """

    def __init__(self,
                 dialog_node,
                 description=None,
                 conditions=None,
                 parent=None,
                 previous_sibling=None,
                 output=None,
                 context=None,
                 metadata=None,
                 next_step=None,
                 actions=None,
                 title=None,
                 node_type=None,
                 event_name=None,
                 variable=None,
                 digress_in=None,
                 digress_out=None,
                 digress_out_slots=None):
        """
        Initialize a CreateDialogNode object.

        :param str dialog_node: The dialog node ID. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 1024 characters.
        :param str description: (optional) The description of the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param str conditions: (optional) The condition that will trigger the dialog node. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 2048 characters.
        :param str parent: (optional) The ID of the parent dialog node.
        :param str previous_sibling: (optional) The ID of the previous dialog node.
        :param object output: (optional) The output of the dialog node. For more information about how to specify dialog node output, see the [documentation](https://console.bluemix.net/docs/services/conversation/dialog-overview.html#complex).
        :param object context: (optional) The context for the dialog node.
        :param object metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep next_step: (optional) The next step to be executed in dialog processing.
        :param list[DialogNodeAction] actions: (optional) An array of objects describing any actions to be invoked by the dialog node.
        :param str title: (optional) The alias used to identify the dialog node. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot characters.  - It must be no longer than 64 characters.
        :param str node_type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where output is stored.
        :param str digress_in: (optional) Whether this top-level dialog node can be digressed into.
        :param str digress_out: (optional) Whether this dialog node can be returned to after a digression.
        :param str digress_out_slots: (optional) Whether the user can digress to top-level nodes while filling out slots.
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
        self.actions = actions
        self.title = title
        self.node_type = node_type
        self.event_name = event_name
        self.variable = variable
        self.digress_in = digress_in
        self.digress_out = digress_out
        self.digress_out_slots = digress_out_slots

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateDialogNode object from a json dictionary."""
        args = {}
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        else:
            raise ValueError(
                'Required property \'dialog_node\' not present in CreateDialogNode JSON'
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
            args['output'] = _dict.get('output')
        if 'context' in _dict:
            args['context'] = _dict.get('context')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'next_step' in _dict:
            args['next_step'] = DialogNodeNextStep._from_dict(
                _dict.get('next_step'))
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction._from_dict(x) for x in (_dict.get('actions'))
            ]
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'type' in _dict or 'node_type' in _dict:
            args['node_type'] = _dict.get('type') or _dict.get('node_type')
        if 'event_name' in _dict:
            args['event_name'] = _dict.get('event_name')
        if 'variable' in _dict:
            args['variable'] = _dict.get('variable')
        if 'digress_in' in _dict:
            args['digress_in'] = _dict.get('digress_in')
        if 'digress_out' in _dict:
            args['digress_out'] = _dict.get('digress_out')
        if 'digress_out_slots' in _dict:
            args['digress_out_slots'] = _dict.get('digress_out_slots')
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
            _dict['output'] = self.output
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'next_step') and self.next_step is not None:
            _dict['next_step'] = self.next_step._to_dict()
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = [x._to_dict() for x in self.actions]
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'node_type') and self.node_type is not None:
            _dict['type'] = self.node_type
        if hasattr(self, 'event_name') and self.event_name is not None:
            _dict['event_name'] = self.event_name
        if hasattr(self, 'variable') and self.variable is not None:
            _dict['variable'] = self.variable
        if hasattr(self, 'digress_in') and self.digress_in is not None:
            _dict['digress_in'] = self.digress_in
        if hasattr(self, 'digress_out') and self.digress_out is not None:
            _dict['digress_out'] = self.digress_out
        if hasattr(self,
                   'digress_out_slots') and self.digress_out_slots is not None:
            _dict['digress_out_slots'] = self.digress_out_slots
        return _dict

    def __str__(self):
        """Return a `str` version of this CreateDialogNode object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateEntity(object):
    """
    CreateEntity.

    :attr str entity: The name of the entity. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, and hyphen characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 64 characters.
    :attr str description: (optional) The description of the entity. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
    :attr object metadata: (optional) Any metadata related to the value.
    :attr list[CreateValue] values: (optional) An array of objects describing the entity values.
    :attr bool fuzzy_match: (optional) Whether to use fuzzy matching for the entity.
    """

    def __init__(self,
                 entity,
                 description=None,
                 metadata=None,
                 values=None,
                 fuzzy_match=None):
        """
        Initialize a CreateEntity object.

        :param str entity: The name of the entity. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, and hyphen characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 64 characters.
        :param str description: (optional) The description of the entity. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param object metadata: (optional) Any metadata related to the value.
        :param list[CreateValue] values: (optional) An array of objects describing the entity values.
        :param bool fuzzy_match: (optional) Whether to use fuzzy matching for the entity.
        """
        self.entity = entity
        self.description = description
        self.metadata = metadata
        self.values = values
        self.fuzzy_match = fuzzy_match

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateEntity object from a json dictionary."""
        args = {}
        if 'entity' in _dict:
            args['entity'] = _dict.get('entity')
        else:
            raise ValueError(
                'Required property \'entity\' not present in CreateEntity JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'values' in _dict:
            args['values'] = [
                CreateValue._from_dict(x) for x in (_dict.get('values'))
            ]
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict.get('fuzzy_match')
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
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [x._to_dict() for x in self.values]
        if hasattr(self, 'fuzzy_match') and self.fuzzy_match is not None:
            _dict['fuzzy_match'] = self.fuzzy_match
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


class CreateExample(object):
    """
    CreateExample.

    :attr str text: The text of a user input example. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 1024 characters.
    """

    def __init__(self, text):
        """
        Initialize a CreateExample object.

        :param str text: The text of a user input example. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 1024 characters.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateExample object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in CreateExample JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this CreateExample object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateIntent(object):
    """
    CreateIntent.

    :attr str intent: The name of the intent. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, hyphen, and dot characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 128 characters.
    :attr str description: (optional) The description of the intent. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
    :attr list[CreateExample] examples: (optional) An array of user input examples for the intent.
    """

    def __init__(self, intent, description=None, examples=None):
        """
        Initialize a CreateIntent object.

        :param str intent: The name of the intent. This string must conform to the following restrictions:  - It can contain only Unicode alphanumeric, underscore, hyphen, and dot characters.  - It cannot begin with the reserved prefix `sys-`.  - It must be no longer than 128 characters.
        :param str description: (optional) The description of the intent. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 128 characters.
        :param list[CreateExample] examples: (optional) An array of user input examples for the intent.
        """
        self.intent = intent
        self.description = description
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateIntent object from a json dictionary."""
        args = {}
        if 'intent' in _dict:
            args['intent'] = _dict.get('intent')
        else:
            raise ValueError(
                'Required property \'intent\' not present in CreateIntent JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'examples' in _dict:
            args['examples'] = [
                CreateExample._from_dict(x) for x in (_dict.get('examples'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
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


class CreateValue(object):
    """
    CreateValue.

    :attr str value: The text of the entity value. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
    :attr object metadata: (optional) Any metadata related to the entity value.
    :attr list[str] synonyms: (optional) An array containing any synonyms for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A synonym must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
    :attr list[str] patterns: (optional) An array of patterns for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A pattern is a regular expression no longer than 128 characters. For more information about how to specify a pattern, see the [documentation](https://console.bluemix.net/docs/services/conversation/entities.html#creating-entities).
    :attr str value_type: (optional) Specifies the type of value.
    """

    def __init__(self,
                 value,
                 metadata=None,
                 synonyms=None,
                 patterns=None,
                 value_type=None):
        """
        Initialize a CreateValue object.

        :param str value: The text of the entity value. This string must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param object metadata: (optional) Any metadata related to the entity value.
        :param list[str] synonyms: (optional) An array containing any synonyms for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A synonym must conform to the following restrictions:  - It cannot contain carriage return, newline, or tab characters.  - It cannot consist of only whitespace characters.  - It must be no longer than 64 characters.
        :param list[str] patterns: (optional) An array of patterns for the entity value. You can provide either synonyms or patterns (as indicated by **type**), but not both. A pattern is a regular expression no longer than 128 characters. For more information about how to specify a pattern, see the [documentation](https://console.bluemix.net/docs/services/conversation/entities.html#creating-entities).
        :param str value_type: (optional) Specifies the type of value.
        """
        self.value = value
        self.metadata = metadata
        self.synonyms = synonyms
        self.patterns = patterns
        self.value_type = value_type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateValue object from a json dictionary."""
        args = {}
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError(
                'Required property \'value\' not present in CreateValue JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'synonyms' in _dict:
            args['synonyms'] = _dict.get('synonyms')
        if 'patterns' in _dict:
            args['patterns'] = _dict.get('patterns')
        if 'type' in _dict or 'value_type' in _dict:
            args['value_type'] = _dict.get('type') or _dict.get('value_type')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'synonyms') and self.synonyms is not None:
            _dict['synonyms'] = self.synonyms
        if hasattr(self, 'patterns') and self.patterns is not None:
            _dict['patterns'] = self.patterns
        if hasattr(self, 'value_type') and self.value_type is not None:
            _dict['type'] = self.value_type
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


class DialogNode(object):
    """
    DialogNode.

    :attr str dialog_node_id: The dialog node ID.
    :attr str description: (optional) The description of the dialog node.
    :attr str conditions: (optional) The condition that triggers the dialog node.
    :attr str parent: (optional) The ID of the parent dialog node. This property is not returned if the dialog node has no parent.
    :attr str previous_sibling: (optional) The ID of the previous sibling dialog node. This property is not returned if the dialog node has no previous sibling.
    :attr object output: (optional) The output of the dialog node.
    :attr object context: (optional) The context (if defined) for the dialog node.
    :attr object metadata: (optional) Any metadata for the dialog node.
    :attr DialogNodeNextStep next_step: (optional) The next step to execute following this dialog node.
    :attr datetime created: (optional) The timestamp for creation of the dialog node.
    :attr datetime updated: (optional) The timestamp for the most recent update to the dialog node.
    :attr list[DialogNodeAction] actions: (optional) The actions for the dialog node.
    :attr str title: (optional) The alias used to identify the dialog node.
    :attr str node_type: (optional) How the dialog node is processed.
    :attr str event_name: (optional) How an `event_handler` node is processed.
    :attr str variable: (optional) The location in the dialog context where output is stored.
    :attr str digress_in: (optional) Whether this top-level dialog node can be digressed into.
    :attr str digress_out: (optional) Whether this dialog node can be returned to after a digression.
    :attr str digress_out_slots: (optional) Whether the user can digress to top-level nodes while filling out slots.
    """

    def __init__(self,
                 dialog_node_id,
                 description=None,
                 conditions=None,
                 parent=None,
                 previous_sibling=None,
                 output=None,
                 context=None,
                 metadata=None,
                 next_step=None,
                 created=None,
                 updated=None,
                 actions=None,
                 title=None,
                 node_type=None,
                 event_name=None,
                 variable=None,
                 digress_in=None,
                 digress_out=None,
                 digress_out_slots=None):
        """
        Initialize a DialogNode object.

        :param str dialog_node_id: The dialog node ID.
        :param str description: (optional) The description of the dialog node.
        :param str conditions: (optional) The condition that triggers the dialog node.
        :param str parent: (optional) The ID of the parent dialog node. This property is not returned if the dialog node has no parent.
        :param str previous_sibling: (optional) The ID of the previous sibling dialog node. This property is not returned if the dialog node has no previous sibling.
        :param object output: (optional) The output of the dialog node.
        :param object context: (optional) The context (if defined) for the dialog node.
        :param object metadata: (optional) Any metadata for the dialog node.
        :param DialogNodeNextStep next_step: (optional) The next step to execute following this dialog node.
        :param datetime created: (optional) The timestamp for creation of the dialog node.
        :param datetime updated: (optional) The timestamp for the most recent update to the dialog node.
        :param list[DialogNodeAction] actions: (optional) The actions for the dialog node.
        :param str title: (optional) The alias used to identify the dialog node.
        :param str node_type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where output is stored.
        :param str digress_in: (optional) Whether this top-level dialog node can be digressed into.
        :param str digress_out: (optional) Whether this dialog node can be returned to after a digression.
        :param str digress_out_slots: (optional) Whether the user can digress to top-level nodes while filling out slots.
        """
        self.dialog_node_id = dialog_node_id
        self.description = description
        self.conditions = conditions
        self.parent = parent
        self.previous_sibling = previous_sibling
        self.output = output
        self.context = context
        self.metadata = metadata
        self.next_step = next_step
        self.created = created
        self.updated = updated
        self.actions = actions
        self.title = title
        self.node_type = node_type
        self.event_name = event_name
        self.variable = variable
        self.digress_in = digress_in
        self.digress_out = digress_out
        self.digress_out_slots = digress_out_slots

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNode object from a json dictionary."""
        args = {}
        if 'dialog_node' in _dict or 'dialog_node_id' in _dict:
            args['dialog_node_id'] = _dict.get('dialog_node') or _dict.get(
                'dialog_node_id')
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
            args['output'] = _dict.get('output')
        if 'context' in _dict:
            args['context'] = _dict.get('context')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'next_step' in _dict:
            args['next_step'] = DialogNodeNextStep._from_dict(
                _dict.get('next_step'))
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction._from_dict(x) for x in (_dict.get('actions'))
            ]
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'type' in _dict or 'node_type' in _dict:
            args['node_type'] = _dict.get('type') or _dict.get('node_type')
        if 'event_name' in _dict:
            args['event_name'] = _dict.get('event_name')
        if 'variable' in _dict:
            args['variable'] = _dict.get('variable')
        if 'digress_in' in _dict:
            args['digress_in'] = _dict.get('digress_in')
        if 'digress_out' in _dict:
            args['digress_out'] = _dict.get('digress_out')
        if 'digress_out_slots' in _dict:
            args['digress_out_slots'] = _dict.get('digress_out_slots')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dialog_node_id') and self.dialog_node_id is not None:
            _dict['dialog_node'] = self.dialog_node_id
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
            _dict['output'] = self.output
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'next_step') and self.next_step is not None:
            _dict['next_step'] = self.next_step._to_dict()
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = [x._to_dict() for x in self.actions]
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'node_type') and self.node_type is not None:
            _dict['type'] = self.node_type
        if hasattr(self, 'event_name') and self.event_name is not None:
            _dict['event_name'] = self.event_name
        if hasattr(self, 'variable') and self.variable is not None:
            _dict['variable'] = self.variable
        if hasattr(self, 'digress_in') and self.digress_in is not None:
            _dict['digress_in'] = self.digress_in
        if hasattr(self, 'digress_out') and self.digress_out is not None:
            _dict['digress_out'] = self.digress_out
        if hasattr(self,
                   'digress_out_slots') and self.digress_out_slots is not None:
            _dict['digress_out_slots'] = self.digress_out_slots
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


class DialogNodeAction(object):
    """
    DialogNodeAction.

    :attr str name: The name of the action.
    :attr str action_type: (optional) The type of action to invoke.
    :attr object parameters: (optional) A map of key/value pairs to be provided to the action.
    :attr str result_variable: The location in the dialog context where the result of the action is stored.
    :attr str credentials: (optional) The name of the context variable that the client application will use to pass in credentials for the action.
    """

    def __init__(self,
                 name,
                 result_variable,
                 action_type=None,
                 parameters=None,
                 credentials=None):
        """
        Initialize a DialogNodeAction object.

        :param str name: The name of the action.
        :param str result_variable: The location in the dialog context where the result of the action is stored.
        :param str action_type: (optional) The type of action to invoke.
        :param object parameters: (optional) A map of key/value pairs to be provided to the action.
        :param str credentials: (optional) The name of the context variable that the client application will use to pass in credentials for the action.
        """
        self.name = name
        self.action_type = action_type
        self.parameters = parameters
        self.result_variable = result_variable
        self.credentials = credentials

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeAction object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in DialogNodeAction JSON'
            )
        if 'type' in _dict or 'action_type' in _dict:
            args['action_type'] = _dict.get('type') or _dict.get('action_type')
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
        if hasattr(self, 'action_type') and self.action_type is not None:
            _dict['type'] = self.action_type
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


class DialogNodeCollection(object):
    """
    An array of dialog nodes.

    :attr list[DialogNode] dialog_nodes: An array of objects describing the dialog nodes defined for the workspace.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, dialog_nodes, pagination):
        """
        Initialize a DialogNodeCollection object.

        :param list[DialogNode] dialog_nodes: An array of objects describing the dialog nodes defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.dialog_nodes = dialog_nodes
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeCollection object from a json dictionary."""
        args = {}
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


class DialogNodeNextStep(object):
    """
    The next step to execute following this dialog node.

    :attr str behavior: What happens after the dialog node completes. The valid values depend on the node type:  - The following values are valid for any node:    - `get_user_input`    - `skip_user_input`    - `jump_to`  - If the node is of type `event_handler` and its parent node is of type `slot` or `frame`, additional values are also valid:    - if **event_name**=`filled` and the type of the parent node is `slot`:      - `reprompt`      - `skip_all_slots`  - if **event_name**=`nomatch` and the type of the parent node is `slot`:      - `reprompt`      - `skip_slot`      - `skip_all_slots`  - if **event_name**=`generic` and the type of the parent node is `frame`:      - `reprompt`      - `skip_slot`      - `skip_all_slots`        If you specify `jump_to`, then you must also specify a value for the `dialog_node` property.
    :attr str dialog_node: (optional) The ID of the dialog node to process next. This parameter is required if **behavior**=`jump_to`.
    :attr str selector: (optional) Which part of the dialog node to process next.
    """

    def __init__(self, behavior, dialog_node=None, selector=None):
        """
        Initialize a DialogNodeNextStep object.

        :param str behavior: What happens after the dialog node completes. The valid values depend on the node type:  - The following values are valid for any node:    - `get_user_input`    - `skip_user_input`    - `jump_to`  - If the node is of type `event_handler` and its parent node is of type `slot` or `frame`, additional values are also valid:    - if **event_name**=`filled` and the type of the parent node is `slot`:      - `reprompt`      - `skip_all_slots`  - if **event_name**=`nomatch` and the type of the parent node is `slot`:      - `reprompt`      - `skip_slot`      - `skip_all_slots`  - if **event_name**=`generic` and the type of the parent node is `frame`:      - `reprompt`      - `skip_slot`      - `skip_all_slots`        If you specify `jump_to`, then you must also specify a value for the `dialog_node` property.
        :param str dialog_node: (optional) The ID of the dialog node to process next. This parameter is required if **behavior**=`jump_to`.
        :param str selector: (optional) Which part of the dialog node to process next.
        """
        self.behavior = behavior
        self.dialog_node = dialog_node
        self.selector = selector

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeNextStep object from a json dictionary."""
        args = {}
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


class DialogNodeVisitedDetails(object):
    """
    DialogNodeVisitedDetails.

    :attr str dialog_node: (optional) A dialog node that was triggered during processing of the input message.
    :attr str title: (optional) The title of the dialog node.
    :attr str conditions: (optional) The conditions that trigger the dialog node.
    """

    def __init__(self, dialog_node=None, title=None, conditions=None):
        """
        Initialize a DialogNodeVisitedDetails object.

        :param str dialog_node: (optional) A dialog node that was triggered during processing of the input message.
        :param str title: (optional) The title of the dialog node.
        :param str conditions: (optional) The conditions that trigger the dialog node.
        """
        self.dialog_node = dialog_node
        self.title = title
        self.conditions = conditions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeVisitedDetails object from a json dictionary."""
        args = {}
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


class Entity(object):
    """
    Entity.

    :attr str entity_name: The name of the entity.
    :attr datetime created: (optional) The timestamp for creation of the entity.
    :attr datetime updated: (optional) The timestamp for the last update to the entity.
    :attr str description: (optional) The description of the entity.
    :attr object metadata: (optional) Any metadata related to the entity.
    :attr bool fuzzy_match: (optional) Whether fuzzy matching is used for the entity.
    """

    def __init__(self,
                 entity_name,
                 created=None,
                 updated=None,
                 description=None,
                 metadata=None,
                 fuzzy_match=None):
        """
        Initialize a Entity object.

        :param str entity_name: The name of the entity.
        :param datetime created: (optional) The timestamp for creation of the entity.
        :param datetime updated: (optional) The timestamp for the last update to the entity.
        :param str description: (optional) The description of the entity.
        :param object metadata: (optional) Any metadata related to the entity.
        :param bool fuzzy_match: (optional) Whether fuzzy matching is used for the entity.
        """
        self.entity_name = entity_name
        self.created = created
        self.updated = updated
        self.description = description
        self.metadata = metadata
        self.fuzzy_match = fuzzy_match

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Entity object from a json dictionary."""
        args = {}
        if 'entity' in _dict or 'entity_name' in _dict:
            args['entity_name'] = _dict.get('entity') or _dict.get(
                'entity_name')
        else:
            raise ValueError(
                'Required property \'entity\' not present in Entity JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict.get('fuzzy_match')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity_name') and self.entity_name is not None:
            _dict['entity'] = self.entity_name
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'fuzzy_match') and self.fuzzy_match is not None:
            _dict['fuzzy_match'] = self.fuzzy_match
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


class EntityCollection(object):
    """
    An array of entities.

    :attr list[EntityExport] entities: An array of objects describing the entities defined for the workspace.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, entities, pagination):
        """
        Initialize a EntityCollection object.

        :param list[EntityExport] entities: An array of objects describing the entities defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.entities = entities
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityCollection object from a json dictionary."""
        args = {}
        if 'entities' in _dict:
            args['entities'] = [
                EntityExport._from_dict(x) for x in (_dict.get('entities'))
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


class EntityExport(object):
    """
    EntityExport.

    :attr str entity_name: The name of the entity.
    :attr datetime created: (optional) The timestamp for creation of the entity.
    :attr datetime updated: (optional) The timestamp for the last update to the entity.
    :attr str description: (optional) The description of the entity.
    :attr object metadata: (optional) Any metadata related to the entity.
    :attr bool fuzzy_match: (optional) Whether fuzzy matching is used for the entity.
    :attr list[ValueExport] values: (optional) An array objects describing the entity values.
    """

    def __init__(self,
                 entity_name,
                 created=None,
                 updated=None,
                 description=None,
                 metadata=None,
                 fuzzy_match=None,
                 values=None):
        """
        Initialize a EntityExport object.

        :param str entity_name: The name of the entity.
        :param datetime created: (optional) The timestamp for creation of the entity.
        :param datetime updated: (optional) The timestamp for the last update to the entity.
        :param str description: (optional) The description of the entity.
        :param object metadata: (optional) Any metadata related to the entity.
        :param bool fuzzy_match: (optional) Whether fuzzy matching is used for the entity.
        :param list[ValueExport] values: (optional) An array objects describing the entity values.
        """
        self.entity_name = entity_name
        self.created = created
        self.updated = updated
        self.description = description
        self.metadata = metadata
        self.fuzzy_match = fuzzy_match
        self.values = values

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityExport object from a json dictionary."""
        args = {}
        if 'entity' in _dict or 'entity_name' in _dict:
            args['entity_name'] = _dict.get('entity') or _dict.get(
                'entity_name')
        else:
            raise ValueError(
                'Required property \'entity\' not present in EntityExport JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict.get('fuzzy_match')
        if 'values' in _dict:
            args['values'] = [
                ValueExport._from_dict(x) for x in (_dict.get('values'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity_name') and self.entity_name is not None:
            _dict['entity'] = self.entity_name
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'fuzzy_match') and self.fuzzy_match is not None:
            _dict['fuzzy_match'] = self.fuzzy_match
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [x._to_dict() for x in self.values]
        return _dict

    def __str__(self):
        """Return a `str` version of this EntityExport object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Example(object):
    """
    Example.

    :attr str example_text: The text of the user input example.
    :attr datetime created: (optional) The timestamp for creation of the example.
    :attr datetime updated: (optional) The timestamp for the last update to the example.
    """

    def __init__(self, example_text, created=None, updated=None):
        """
        Initialize a Example object.

        :param str example_text: The text of the user input example.
        :param datetime created: (optional) The timestamp for creation of the example.
        :param datetime updated: (optional) The timestamp for the last update to the example.
        """
        self.example_text = example_text
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Example object from a json dictionary."""
        args = {}
        if 'text' in _dict or 'example_text' in _dict:
            args['example_text'] = _dict.get('text') or _dict.get(
                'example_text')
        else:
            raise ValueError(
                'Required property \'text\' not present in Example JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'example_text') and self.example_text is not None:
            _dict['text'] = self.example_text
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


class ExampleCollection(object):
    """
    ExampleCollection.

    :attr list[Example] examples: An array of objects describing the examples defined for the intent.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, examples, pagination):
        """
        Initialize a ExampleCollection object.

        :param list[Example] examples: An array of objects describing the examples defined for the intent.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.examples = examples
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExampleCollection object from a json dictionary."""
        args = {}
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


class InputData(object):
    """
    The user input.

    :attr str text: The text of the user input. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 2048 characters.
    """

    def __init__(self, text):
        """
        Initialize a InputData object.

        :param str text: The text of the user input. This string cannot contain carriage return, newline, or tab characters, and it must be no longer than 2048 characters.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InputData object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in InputData JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this InputData object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Intent(object):
    """
    Intent.

    :attr str intent_name: The name of the intent.
    :attr datetime created: (optional) The timestamp for creation of the intent.
    :attr datetime updated: (optional) The timestamp for the last update to the intent.
    :attr str description: (optional) The description of the intent.
    """

    def __init__(self,
                 intent_name,
                 created=None,
                 updated=None,
                 description=None):
        """
        Initialize a Intent object.

        :param str intent_name: The name of the intent.
        :param datetime created: (optional) The timestamp for creation of the intent.
        :param datetime updated: (optional) The timestamp for the last update to the intent.
        :param str description: (optional) The description of the intent.
        """
        self.intent_name = intent_name
        self.created = created
        self.updated = updated
        self.description = description

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Intent object from a json dictionary."""
        args = {}
        if 'intent' in _dict or 'intent_name' in _dict:
            args['intent_name'] = _dict.get('intent') or _dict.get(
                'intent_name')
        else:
            raise ValueError(
                'Required property \'intent\' not present in Intent JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent_name') and self.intent_name is not None:
            _dict['intent'] = self.intent_name
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
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


class IntentCollection(object):
    """
    IntentCollection.

    :attr list[IntentExport] intents: An array of objects describing the intents defined for the workspace.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, intents, pagination):
        """
        Initialize a IntentCollection object.

        :param list[IntentExport] intents: An array of objects describing the intents defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.intents = intents
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IntentCollection object from a json dictionary."""
        args = {}
        if 'intents' in _dict:
            args['intents'] = [
                IntentExport._from_dict(x) for x in (_dict.get('intents'))
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


class IntentExport(object):
    """
    IntentExport.

    :attr str intent_name: The name of the intent.
    :attr datetime created: (optional) The timestamp for creation of the intent.
    :attr datetime updated: (optional) The timestamp for the last update to the intent.
    :attr str description: (optional) The description of the intent.
    :attr list[Example] examples: (optional) An array of objects describing the user input examples for the intent.
    """

    def __init__(self,
                 intent_name,
                 created=None,
                 updated=None,
                 description=None,
                 examples=None):
        """
        Initialize a IntentExport object.

        :param str intent_name: The name of the intent.
        :param datetime created: (optional) The timestamp for creation of the intent.
        :param datetime updated: (optional) The timestamp for the last update to the intent.
        :param str description: (optional) The description of the intent.
        :param list[Example] examples: (optional) An array of objects describing the user input examples for the intent.
        """
        self.intent_name = intent_name
        self.created = created
        self.updated = updated
        self.description = description
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IntentExport object from a json dictionary."""
        args = {}
        if 'intent' in _dict or 'intent_name' in _dict:
            args['intent_name'] = _dict.get('intent') or _dict.get(
                'intent_name')
        else:
            raise ValueError(
                'Required property \'intent\' not present in IntentExport JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'examples' in _dict:
            args['examples'] = [
                Example._from_dict(x) for x in (_dict.get('examples'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent_name') and self.intent_name is not None:
            _dict['intent'] = self.intent_name
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        return _dict

    def __str__(self):
        """Return a `str` version of this IntentExport object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogCollection(object):
    """
    LogCollection.

    :attr list[LogExport] logs: An array of objects describing log events.
    :attr LogPagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, logs, pagination):
        """
        Initialize a LogCollection object.

        :param list[LogExport] logs: An array of objects describing log events.
        :param LogPagination pagination: The pagination data for the returned objects.
        """
        self.logs = logs
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogCollection object from a json dictionary."""
        args = {}
        if 'logs' in _dict:
            args['logs'] = [
                LogExport._from_dict(x) for x in (_dict.get('logs'))
            ]
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


class LogExport(object):
    """
    LogExport.

    :attr MessageRequest request: A request received by the workspace, including the user input and context.
    :attr MessageResponse response: The response sent by the workspace, including the output text, detected intents and entities, and context.
    :attr str log_id: A unique identifier for the logged event.
    :attr str request_timestamp: The timestamp for receipt of the message.
    :attr str response_timestamp: The timestamp for the system response to the message.
    :attr str workspace_id: The unique identifier of the workspace where the request was made.
    :attr str language: The language of the workspace where the message request was made.
    """

    def __init__(self, request, response, log_id, request_timestamp,
                 response_timestamp, workspace_id, language):
        """
        Initialize a LogExport object.

        :param MessageRequest request: A request received by the workspace, including the user input and context.
        :param MessageResponse response: The response sent by the workspace, including the output text, detected intents and entities, and context.
        :param str log_id: A unique identifier for the logged event.
        :param str request_timestamp: The timestamp for receipt of the message.
        :param str response_timestamp: The timestamp for the system response to the message.
        :param str workspace_id: The unique identifier of the workspace where the request was made.
        :param str language: The language of the workspace where the message request was made.
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
        """Initialize a LogExport object from a json dictionary."""
        args = {}
        if 'request' in _dict:
            args['request'] = MessageRequest._from_dict(_dict.get('request'))
        else:
            raise ValueError(
                'Required property \'request\' not present in LogExport JSON')
        if 'response' in _dict:
            args['response'] = MessageResponse._from_dict(
                _dict.get('response'))
        else:
            raise ValueError(
                'Required property \'response\' not present in LogExport JSON')
        if 'log_id' in _dict:
            args['log_id'] = _dict.get('log_id')
        else:
            raise ValueError(
                'Required property \'log_id\' not present in LogExport JSON')
        if 'request_timestamp' in _dict:
            args['request_timestamp'] = _dict.get('request_timestamp')
        else:
            raise ValueError(
                'Required property \'request_timestamp\' not present in LogExport JSON'
            )
        if 'response_timestamp' in _dict:
            args['response_timestamp'] = _dict.get('response_timestamp')
        else:
            raise ValueError(
                'Required property \'response_timestamp\' not present in LogExport JSON'
            )
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in LogExport JSON'
            )
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in LogExport JSON')
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
        """Return a `str` version of this LogExport object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogMessage(object):
    """
    Log message details.

    :attr str level: The severity of the log message.
    :attr str msg: The text of the log message.
    """

    def __init__(self, level, msg, **kwargs):
        """
        Initialize a LogMessage object.

        :param str level: The severity of the log message.
        :param str msg: The text of the log message.
        :param **kwargs: (optional) Any additional properties.
        """
        self.level = level
        self.msg = msg
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessage object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'level' in _dict:
            args['level'] = _dict.get('level')
            del xtra['level']
        else:
            raise ValueError(
                'Required property \'level\' not present in LogMessage JSON')
        if 'msg' in _dict:
            args['msg'] = _dict.get('msg')
            del xtra['msg']
        else:
            raise ValueError(
                'Required property \'msg\' not present in LogMessage JSON')
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self, 'msg') and self.msg is not None:
            _dict['msg'] = self.msg
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'level', 'msg'}
        if not hasattr(self, '_additionalProperties'):
            super(LogMessage, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(LogMessage, self).__setattr__(name, value)

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


class LogPagination(object):
    """
    The pagination data for the returned objects.

    :attr str next_url: (optional) The URL that will return the next page of results, if any.
    :attr int matched: (optional) Reserved for future use.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(self, next_url=None, matched=None, next_cursor=None):
        """
        Initialize a LogPagination object.

        :param str next_url: (optional) The URL that will return the next page of results, if any.
        :param int matched: (optional) Reserved for future use.
        :param str next_cursor: (optional) A token identifying the next page of results.
        """
        self.next_url = next_url
        self.matched = matched
        self.next_cursor = next_cursor

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogPagination object from a json dictionary."""
        args = {}
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


class MessageInput(object):
    """
    The text of the user input.

    :attr str text: (optional) The user's input.
    """

    def __init__(self, text=None):
        """
        Initialize a MessageInput object.

        :param str text: (optional) The user's input.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInput object from a json dictionary."""
        args = {}
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


class MessageRequest(object):
    """
    A request formatted for the Conversation service.

    :attr InputData input: (optional) An input object that includes the input text.
    :attr bool alternate_intents: (optional) Whether to return more than one intent. Set to `true` to return all matching intents.
    :attr Context context: (optional) State information for the conversation. Continue a conversation by including the context object from the previous response.
    :attr list[RuntimeEntity] entities: (optional) Entities to use when evaluating the message. Include entities from the previous response to continue using those entities rather than detecting entities in the new input.
    :attr list[RuntimeIntent] intents: (optional) Intents to use when evaluating the user input. Include intents from the previous response to continue using those intents rather than trying to recognize intents in the new input.
    :attr OutputData output: (optional) System output. Include the output from the previous response to maintain intermediate information over multiple requests.
    """

    def __init__(self,
                 input=None,
                 alternate_intents=None,
                 context=None,
                 entities=None,
                 intents=None,
                 output=None):
        """
        Initialize a MessageRequest object.

        :param InputData input: (optional) An input object that includes the input text.
        :param bool alternate_intents: (optional) Whether to return more than one intent. Set to `true` to return all matching intents.
        :param Context context: (optional) State information for the conversation. Continue a conversation by including the context object from the previous response.
        :param list[RuntimeEntity] entities: (optional) Entities to use when evaluating the message. Include entities from the previous response to continue using those entities rather than detecting entities in the new input.
        :param list[RuntimeIntent] intents: (optional) Intents to use when evaluating the user input. Include intents from the previous response to continue using those intents rather than trying to recognize intents in the new input.
        :param OutputData output: (optional) System output. Include the output from the previous response to maintain intermediate information over multiple requests.
        """
        self.input = input
        self.alternate_intents = alternate_intents
        self.context = context
        self.entities = entities
        self.intents = intents
        self.output = output

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageRequest object from a json dictionary."""
        args = {}
        if 'input' in _dict:
            args['input'] = InputData._from_dict(_dict.get('input'))
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict.get('alternate_intents')
        if 'context' in _dict:
            args['context'] = Context._from_dict(_dict.get('context'))
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in (_dict.get('intents'))
            ]
        if 'output' in _dict:
            args['output'] = OutputData._from_dict(_dict.get('output'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            _dict['input'] = self.input._to_dict()
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context._to_dict()
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'output') and self.output is not None:
            _dict['output'] = self.output._to_dict()
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


class MessageResponse(object):
    """
    A response from the Conversation service.

    :attr MessageInput input: (optional) The user input from the request.
    :attr list[RuntimeIntent] intents: An array of intents recognized in the user input, sorted in descending order of confidence.
    :attr list[RuntimeEntity] entities: An array of entities identified in the user input.
    :attr bool alternate_intents: (optional) Whether to return more than one intent. A value of `true` indicates that all matching intents are returned.
    :attr Context context: State information for the conversation.
    :attr OutputData output: Output from the dialog, including the response to the user, the nodes that were triggered, and log messages.
    """

    def __init__(self,
                 intents,
                 entities,
                 context,
                 output,
                 input=None,
                 alternate_intents=None,
                 **kwargs):
        """
        Initialize a MessageResponse object.

        :param list[RuntimeIntent] intents: An array of intents recognized in the user input, sorted in descending order of confidence.
        :param list[RuntimeEntity] entities: An array of entities identified in the user input.
        :param Context context: State information for the conversation.
        :param OutputData output: Output from the dialog, including the response to the user, the nodes that were triggered, and log messages.
        :param MessageInput input: (optional) The user input from the request.
        :param bool alternate_intents: (optional) Whether to return more than one intent. A value of `true` indicates that all matching intents are returned.
        :param **kwargs: (optional) Any additional properties.
        """
        self.input = input
        self.intents = intents
        self.entities = entities
        self.alternate_intents = alternate_intents
        self.context = context
        self.output = output
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageResponse object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'input' in _dict:
            args['input'] = MessageInput._from_dict(_dict.get('input'))
            del xtra['input']
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in (_dict.get('intents'))
            ]
            del xtra['intents']
        else:
            raise ValueError(
                'Required property \'intents\' not present in MessageResponse JSON'
            )
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
            del xtra['entities']
        else:
            raise ValueError(
                'Required property \'entities\' not present in MessageResponse JSON'
            )
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict.get('alternate_intents')
            del xtra['alternate_intents']
        if 'context' in _dict:
            args['context'] = Context._from_dict(_dict.get('context'))
            del xtra['context']
        else:
            raise ValueError(
                'Required property \'context\' not present in MessageResponse JSON'
            )
        if 'output' in _dict:
            args['output'] = OutputData._from_dict(_dict.get('output'))
            del xtra['output']
        else:
            raise ValueError(
                'Required property \'output\' not present in MessageResponse JSON'
            )
        args.update(xtra)
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
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {
            'input', 'intents', 'entities', 'alternate_intents', 'context',
            'output'
        }
        if not hasattr(self, '_additionalProperties'):
            super(MessageResponse, self).__setattr__('_additionalProperties',
                                                     set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(MessageResponse, self).__setattr__(name, value)

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


class OutputData(object):
    """
    An output object that includes the response to the user, the nodes that were hit, and
    messages from the log.

    :attr list[LogMessage] log_messages: An array of up to 50 messages logged with the request.
    :attr list[str] text: An array of responses to the user.
    :attr list[str] nodes_visited: (optional) An array of the nodes that were triggered to create the response, in the order in which they were visited. This information is useful for debugging and for tracing the path taken through the node tree.
    :attr list[DialogNodeVisitedDetails] nodes_visited_details: (optional) An array of objects containing detailed diagnostic information about the nodes that were triggered during processing of the input message. Included only if **nodes_visited_details** is set to `true` in the message request.
    """

    def __init__(self,
                 log_messages,
                 text,
                 nodes_visited=None,
                 nodes_visited_details=None,
                 **kwargs):
        """
        Initialize a OutputData object.

        :param list[LogMessage] log_messages: An array of up to 50 messages logged with the request.
        :param list[str] text: An array of responses to the user.
        :param list[str] nodes_visited: (optional) An array of the nodes that were triggered to create the response, in the order in which they were visited. This information is useful for debugging and for tracing the path taken through the node tree.
        :param list[DialogNodeVisitedDetails] nodes_visited_details: (optional) An array of objects containing detailed diagnostic information about the nodes that were triggered during processing of the input message. Included only if **nodes_visited_details** is set to `true` in the message request.
        :param **kwargs: (optional) Any additional properties.
        """
        self.log_messages = log_messages
        self.text = text
        self.nodes_visited = nodes_visited
        self.nodes_visited_details = nodes_visited_details
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OutputData object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
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
        if 'nodes_visited' in _dict:
            args['nodes_visited'] = _dict.get('nodes_visited')
            del xtra['nodes_visited']
        if 'nodes_visited_details' in _dict:
            args['nodes_visited_details'] = [
                DialogNodeVisitedDetails._from_dict(x)
                for x in (_dict.get('nodes_visited_details'))
            ]
            del xtra['nodes_visited_details']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'log_messages') and self.log_messages is not None:
            _dict['log_messages'] = [x._to_dict() for x in self.log_messages]
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'nodes_visited') and self.nodes_visited is not None:
            _dict['nodes_visited'] = self.nodes_visited
        if hasattr(self, 'nodes_visited_details'
                   ) and self.nodes_visited_details is not None:
            _dict['nodes_visited_details'] = [
                x._to_dict() for x in self.nodes_visited_details
            ]
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {
            'log_messages', 'text', 'nodes_visited', 'nodes_visited_details'
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


class Pagination(object):
    """
    The pagination data for the returned objects.

    :attr str refresh_url: The URL that will return the same page of results.
    :attr str next_url: (optional) The URL that will return the next page of results.
    :attr int total: (optional) Reserved for future use.
    :attr int matched: (optional) Reserved for future use.
    :attr str refresh_cursor: (optional) A token identifying the current page of results.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(self,
                 refresh_url,
                 next_url=None,
                 total=None,
                 matched=None,
                 refresh_cursor=None,
                 next_cursor=None):
        """
        Initialize a Pagination object.

        :param str refresh_url: The URL that will return the same page of results.
        :param str next_url: (optional) The URL that will return the next page of results.
        :param int total: (optional) Reserved for future use.
        :param int matched: (optional) Reserved for future use.
        :param str refresh_cursor: (optional) A token identifying the current page of results.
        :param str next_cursor: (optional) A token identifying the next page of results.
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


class RuntimeEntity(object):
    """
    A term from the request that was identified as an entity.

    :attr str entity: An entity detected in the input.
    :attr list[int] location: An array of zero-based character offsets that indicate where the detected entity values begin and end in the input text.
    :attr str value: The term in the input text that was recognized as an entity value.
    :attr float confidence: (optional) A decimal percentage that represents Watson's confidence in the entity.
    :attr object metadata: (optional) Any metadata for the entity.
    :attr list[CaptureGroup] groups: (optional) The recognized capture groups for the entity, as defined by the entity pattern.
    """

    def __init__(self,
                 entity,
                 location,
                 value,
                 confidence=None,
                 metadata=None,
                 groups=None,
                 **kwargs):
        """
        Initialize a RuntimeEntity object.

        :param str entity: An entity detected in the input.
        :param list[int] location: An array of zero-based character offsets that indicate where the detected entity values begin and end in the input text.
        :param str value: The term in the input text that was recognized as an entity value.
        :param float confidence: (optional) A decimal percentage that represents Watson's confidence in the entity.
        :param object metadata: (optional) Any metadata for the entity.
        :param list[CaptureGroup] groups: (optional) The recognized capture groups for the entity, as defined by the entity pattern.
        :param **kwargs: (optional) Any additional properties.
        """
        self.entity = entity
        self.location = location
        self.value = value
        self.confidence = confidence
        self.metadata = metadata
        self.groups = groups
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEntity object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'entity' in _dict:
            args['entity'] = _dict.get('entity')
            del xtra['entity']
        else:
            raise ValueError(
                'Required property \'entity\' not present in RuntimeEntity JSON'
            )
        if 'location' in _dict:
            args['location'] = _dict.get('location')
            del xtra['location']
        else:
            raise ValueError(
                'Required property \'location\' not present in RuntimeEntity JSON'
            )
        if 'value' in _dict:
            args['value'] = _dict.get('value')
            del xtra['value']
        else:
            raise ValueError(
                'Required property \'value\' not present in RuntimeEntity JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
            del xtra['confidence']
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
            del xtra['metadata']
        if 'groups' in _dict:
            args['groups'] = [
                CaptureGroup._from_dict(x) for x in (_dict.get('groups'))
            ]
            del xtra['groups']
        args.update(xtra)
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
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {
            'entity', 'location', 'value', 'confidence', 'metadata', 'groups'
        }
        if not hasattr(self, '_additionalProperties'):
            super(RuntimeEntity, self).__setattr__('_additionalProperties',
                                                   set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(RuntimeEntity, self).__setattr__(name, value)

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


class RuntimeIntent(object):
    """
    An intent identified in the user input.

    :attr str intent: The name of the recognized intent.
    :attr float confidence: A decimal percentage that represents Watson's confidence in the intent.
    """

    def __init__(self, intent, confidence, **kwargs):
        """
        Initialize a RuntimeIntent object.

        :param str intent: The name of the recognized intent.
        :param float confidence: A decimal percentage that represents Watson's confidence in the intent.
        :param **kwargs: (optional) Any additional properties.
        """
        self.intent = intent
        self.confidence = confidence
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeIntent object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'intent' in _dict:
            args['intent'] = _dict.get('intent')
            del xtra['intent']
        else:
            raise ValueError(
                'Required property \'intent\' not present in RuntimeIntent JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
            del xtra['confidence']
        else:
            raise ValueError(
                'Required property \'confidence\' not present in RuntimeIntent JSON'
            )
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'intent', 'confidence'}
        if not hasattr(self, '_additionalProperties'):
            super(RuntimeIntent, self).__setattr__('_additionalProperties',
                                                   set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(RuntimeIntent, self).__setattr__(name, value)

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


class Synonym(object):
    """
    Synonym.

    :attr str synonym_text: The text of the synonym.
    :attr datetime created: (optional) The timestamp for creation of the synonym.
    :attr datetime updated: (optional) The timestamp for the most recent update to the synonym.
    """

    def __init__(self, synonym_text, created=None, updated=None):
        """
        Initialize a Synonym object.

        :param str synonym_text: The text of the synonym.
        :param datetime created: (optional) The timestamp for creation of the synonym.
        :param datetime updated: (optional) The timestamp for the most recent update to the synonym.
        """
        self.synonym_text = synonym_text
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Synonym object from a json dictionary."""
        args = {}
        if 'synonym' in _dict or 'synonym_text' in _dict:
            args['synonym_text'] = _dict.get('synonym') or _dict.get(
                'synonym_text')
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
        if hasattr(self, 'synonym_text') and self.synonym_text is not None:
            _dict['synonym'] = self.synonym_text
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


class SynonymCollection(object):
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


class SystemResponse(object):
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


class Value(object):
    """
    Value.

    :attr str value_text: The text of the entity value.
    :attr object metadata: (optional) Any metadata related to the entity value.
    :attr datetime created: (optional) The timestamp for creation of the entity value.
    :attr datetime updated: (optional) The timestamp for the last update to the entity value.
    :attr list[str] synonyms: (optional) An array containing any synonyms for the entity value.
    :attr list[str] patterns: (optional) An array containing any patterns for the entity value.
    :attr str value_type: Specifies the type of value.
    """

    def __init__(self,
                 value_text,
                 value_type,
                 metadata=None,
                 created=None,
                 updated=None,
                 synonyms=None,
                 patterns=None):
        """
        Initialize a Value object.

        :param str value_text: The text of the entity value.
        :param str value_type: Specifies the type of value.
        :param object metadata: (optional) Any metadata related to the entity value.
        :param datetime created: (optional) The timestamp for creation of the entity value.
        :param datetime updated: (optional) The timestamp for the last update to the entity value.
        :param list[str] synonyms: (optional) An array containing any synonyms for the entity value.
        :param list[str] patterns: (optional) An array containing any patterns for the entity value.
        """
        self.value_text = value_text
        self.metadata = metadata
        self.created = created
        self.updated = updated
        self.synonyms = synonyms
        self.patterns = patterns
        self.value_type = value_type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Value object from a json dictionary."""
        args = {}
        if 'value' in _dict or 'value_text' in _dict:
            args['value_text'] = _dict.get('value') or _dict.get('value_text')
        else:
            raise ValueError(
                'Required property \'value\' not present in Value JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'synonyms' in _dict:
            args['synonyms'] = _dict.get('synonyms')
        if 'patterns' in _dict:
            args['patterns'] = _dict.get('patterns')
        if 'type' in _dict or 'value_type' in _dict:
            args['value_type'] = _dict.get('type') or _dict.get('value_type')
        else:
            raise ValueError(
                'Required property \'type\' not present in Value JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value_text') and self.value_text is not None:
            _dict['value'] = self.value_text
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'synonyms') and self.synonyms is not None:
            _dict['synonyms'] = self.synonyms
        if hasattr(self, 'patterns') and self.patterns is not None:
            _dict['patterns'] = self.patterns
        if hasattr(self, 'value_type') and self.value_type is not None:
            _dict['type'] = self.value_type
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


class ValueCollection(object):
    """
    ValueCollection.

    :attr list[ValueExport] values: An array of entity values.
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, values, pagination):
        """
        Initialize a ValueCollection object.

        :param list[ValueExport] values: An array of entity values.
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.values = values
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValueCollection object from a json dictionary."""
        args = {}
        if 'values' in _dict:
            args['values'] = [
                ValueExport._from_dict(x) for x in (_dict.get('values'))
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


class ValueExport(object):
    """
    ValueExport.

    :attr str value_text: The text of the entity value.
    :attr object metadata: (optional) Any metadata related to the entity value.
    :attr datetime created: (optional) The timestamp for creation of the entity value.
    :attr datetime updated: (optional) The timestamp for the last update to the entity value.
    :attr list[str] synonyms: (optional) An array containing any synonyms for the entity value.
    :attr list[str] patterns: (optional) An array containing any patterns for the entity value.
    :attr str value_type: Specifies the type of value.
    """

    def __init__(self,
                 value_text,
                 value_type,
                 metadata=None,
                 created=None,
                 updated=None,
                 synonyms=None,
                 patterns=None):
        """
        Initialize a ValueExport object.

        :param str value_text: The text of the entity value.
        :param str value_type: Specifies the type of value.
        :param object metadata: (optional) Any metadata related to the entity value.
        :param datetime created: (optional) The timestamp for creation of the entity value.
        :param datetime updated: (optional) The timestamp for the last update to the entity value.
        :param list[str] synonyms: (optional) An array containing any synonyms for the entity value.
        :param list[str] patterns: (optional) An array containing any patterns for the entity value.
        """
        self.value_text = value_text
        self.metadata = metadata
        self.created = created
        self.updated = updated
        self.synonyms = synonyms
        self.patterns = patterns
        self.value_type = value_type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValueExport object from a json dictionary."""
        args = {}
        if 'value' in _dict or 'value_text' in _dict:
            args['value_text'] = _dict.get('value') or _dict.get('value_text')
        else:
            raise ValueError(
                'Required property \'value\' not present in ValueExport JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'synonyms' in _dict:
            args['synonyms'] = _dict.get('synonyms')
        if 'patterns' in _dict:
            args['patterns'] = _dict.get('patterns')
        if 'type' in _dict or 'value_type' in _dict:
            args['value_type'] = _dict.get('type') or _dict.get('value_type')
        else:
            raise ValueError(
                'Required property \'type\' not present in ValueExport JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value_text') and self.value_text is not None:
            _dict['value'] = self.value_text
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'synonyms') and self.synonyms is not None:
            _dict['synonyms'] = self.synonyms
        if hasattr(self, 'patterns') and self.patterns is not None:
            _dict['patterns'] = self.patterns
        if hasattr(self, 'value_type') and self.value_type is not None:
            _dict['type'] = self.value_type
        return _dict

    def __str__(self):
        """Return a `str` version of this ValueExport object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Workspace(object):
    """
    Workspace.

    :attr str name: The name of the workspace.
    :attr str language: The language of the workspace.
    :attr datetime created: (optional) The timestamp for creation of the workspace.
    :attr datetime updated: (optional) The timestamp for the last update to the workspace.
    :attr str workspace_id: The workspace ID.
    :attr str description: (optional) The description of the workspace.
    :attr object metadata: (optional) Any metadata related to the workspace.
    :attr bool learning_opt_out: (optional) Whether training data from the workspace (including artifacts such as intents and entities) can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
    """

    def __init__(self,
                 name,
                 language,
                 workspace_id,
                 created=None,
                 updated=None,
                 description=None,
                 metadata=None,
                 learning_opt_out=None):
        """
        Initialize a Workspace object.

        :param str name: The name of the workspace.
        :param str language: The language of the workspace.
        :param str workspace_id: The workspace ID.
        :param datetime created: (optional) The timestamp for creation of the workspace.
        :param datetime updated: (optional) The timestamp for the last update to the workspace.
        :param str description: (optional) The description of the workspace.
        :param object metadata: (optional) Any metadata related to the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the workspace (including artifacts such as intents and entities) can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
        """
        self.name = name
        self.language = language
        self.created = created
        self.updated = updated
        self.workspace_id = workspace_id
        self.description = description
        self.metadata = metadata
        self.learning_opt_out = learning_opt_out

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Workspace object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Workspace JSON')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in Workspace JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in Workspace JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'learning_opt_out' in _dict:
            args['learning_opt_out'] = _dict.get('learning_opt_out')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self,
                   'learning_opt_out') and self.learning_opt_out is not None:
            _dict['learning_opt_out'] = self.learning_opt_out
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


class WorkspaceCollection(object):
    """
    WorkspaceCollection.

    :attr list[Workspace] workspaces: An array of objects describing the workspaces associated with the service instance.
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, workspaces, pagination):
        """
        Initialize a WorkspaceCollection object.

        :param list[Workspace] workspaces: An array of objects describing the workspaces associated with the service instance.
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.workspaces = workspaces
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceCollection object from a json dictionary."""
        args = {}
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


class WorkspaceExport(object):
    """
    WorkspaceExport.

    :attr str name: The name of the workspace.
    :attr str description: The description of the workspace.
    :attr str language: The language of the workspace.
    :attr object metadata: Any metadata that is required by the workspace.
    :attr datetime created: (optional) The timestamp for creation of the workspace.
    :attr datetime updated: (optional) The timestamp for the last update to the workspace.
    :attr str workspace_id: The workspace ID.
    :attr str status: The current status of the workspace.
    :attr bool learning_opt_out: Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
    :attr list[IntentExport] intents: (optional) An array of intents.
    :attr list[EntityExport] entities: (optional) An array of entities.
    :attr list[Counterexample] counterexamples: (optional) An array of counterexamples.
    :attr list[DialogNode] dialog_nodes: (optional) An array of objects describing the dialog nodes in the workspace.
    """

    def __init__(self,
                 name,
                 description,
                 language,
                 metadata,
                 workspace_id,
                 status,
                 learning_opt_out,
                 created=None,
                 updated=None,
                 intents=None,
                 entities=None,
                 counterexamples=None,
                 dialog_nodes=None):
        """
        Initialize a WorkspaceExport object.

        :param str name: The name of the workspace.
        :param str description: The description of the workspace.
        :param str language: The language of the workspace.
        :param object metadata: Any metadata that is required by the workspace.
        :param str workspace_id: The workspace ID.
        :param str status: The current status of the workspace.
        :param bool learning_opt_out: Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
        :param datetime created: (optional) The timestamp for creation of the workspace.
        :param datetime updated: (optional) The timestamp for the last update to the workspace.
        :param list[IntentExport] intents: (optional) An array of intents.
        :param list[EntityExport] entities: (optional) An array of entities.
        :param list[Counterexample] counterexamples: (optional) An array of counterexamples.
        :param list[DialogNode] dialog_nodes: (optional) An array of objects describing the dialog nodes in the workspace.
        """
        self.name = name
        self.description = description
        self.language = language
        self.metadata = metadata
        self.created = created
        self.updated = updated
        self.workspace_id = workspace_id
        self.status = status
        self.learning_opt_out = learning_opt_out
        self.intents = intents
        self.entities = entities
        self.counterexamples = counterexamples
        self.dialog_nodes = dialog_nodes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceExport object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in WorkspaceExport JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError(
                'Required property \'description\' not present in WorkspaceExport JSON'
            )
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in WorkspaceExport JSON'
            )
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        else:
            raise ValueError(
                'Required property \'metadata\' not present in WorkspaceExport JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in WorkspaceExport JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in WorkspaceExport JSON'
            )
        if 'learning_opt_out' in _dict:
            args['learning_opt_out'] = _dict.get('learning_opt_out')
        else:
            raise ValueError(
                'Required property \'learning_opt_out\' not present in WorkspaceExport JSON'
            )
        if 'intents' in _dict:
            args['intents'] = [
                IntentExport._from_dict(x) for x in (_dict.get('intents'))
            ]
        if 'entities' in _dict:
            args['entities'] = [
                EntityExport._from_dict(x) for x in (_dict.get('entities'))
            ]
        if 'counterexamples' in _dict:
            args['counterexamples'] = [
                Counterexample._from_dict(x)
                for x in (_dict.get('counterexamples'))
            ]
        if 'dialog_nodes' in _dict:
            args['dialog_nodes'] = [
                DialogNode._from_dict(x) for x in (_dict.get('dialog_nodes'))
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self,
                   'learning_opt_out') and self.learning_opt_out is not None:
            _dict['learning_opt_out'] = self.learning_opt_out
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self,
                   'counterexamples') and self.counterexamples is not None:
            _dict['counterexamples'] = [
                x._to_dict() for x in self.counterexamples
            ]
        if hasattr(self, 'dialog_nodes') and self.dialog_nodes is not None:
            _dict['dialog_nodes'] = [x._to_dict() for x in self.dialog_nodes]
        return _dict

    def __str__(self):
        """Return a `str` version of this WorkspaceExport object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other