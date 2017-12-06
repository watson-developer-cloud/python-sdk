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
    VERSION_DATE_2017_05_26 = '2017-05-26'
    VERSION_DATE_2017_04_21 = '2017-04-21'
    VERSION_DATE_2017_02_03 = '2017-02-03'
    VERSION_DATE_2016_09_20 = '2016-09-20'
    VERSION_DATE_2016_07_11 = '2016-07-11'

    def __init__(self, version, url=default_url, username=None, password=None):
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

        """

        WatsonService.__init__(
            self,
            vcap_services_name='conversation',
            url=url,
            username=username,
            password=password,
            use_vcap_services=True)
        self.version = version

    #########################
    # workspaces
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
                         learning_opt_out=None):
        """
        Create workspace.

        Create a workspace based on component objects. You must provide workspace
        components defining the content of the new workspace.

        :param str name: The name of the workspace.
        :param str description: The description of the workspace.
        :param str language: The language of the workspace.
        :param list[CreateIntent] intents: An array of objects defining the intents for the workspace.
        :param list[CreateEntity] entities: An array of objects defining the entities for the workspace.
        :param list[CreateDialogNode] dialog_nodes: An array of objects defining the nodes in the workspace dialog.
        :param list[CreateCounterexample] counterexamples: An array of objects defining input examples that have been marked as irrelevant input.
        :param object metadata: Any metadata related to the workspace.
        :param bool learning_opt_out: Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
        :return: A `dict` containing the `Workspace` response.
        :rtype: dict
        """
        if intents is not None:
            intents = [self._convert_model(x) for x in intents]
        if entities is not None:
            entities = [self._convert_model(x) for x in entities]
        if dialog_nodes is not None:
            dialog_nodes = [self._convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [self._convert_model(x) for x in counterexamples]
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
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_workspace(self, workspace_id):
        """
        Delete workspace.

        Delete a workspace from the service instance.

        :param str workspace_id: The workspace ID.
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}'.format(*self._encode_path_vars(workspace_id))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_workspace(self, workspace_id, export=None):
        """
        Get information about a workspace.

        Get information about a workspace, optionally including all workspace content.

        :param str workspace_id: The workspace ID.
        :param bool export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :return: A `dict` containing the `WorkspaceExport` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        params = {'version': self.version, 'export': export}
        url = '/v1/workspaces/{0}'.format(*self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_workspaces(self,
                        page_limit=None,
                        include_count=None,
                        sort=None,
                        cursor=None):
        """
        List workspaces.

        List the workspaces associated with a Conversation service instance.

        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `WorkspaceCollection` response.
        :rtype: dict
        """
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces'
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
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
                         learning_opt_out=None):
        """
        Update workspace.

        Update an existing workspace with new or modified data. You must provide component
        objects defining the content of the updated workspace.

        :param str workspace_id: The workspace ID.
        :param str name: The name of the workspace.
        :param str description: The description of the workspace.
        :param str language: The language of the workspace.
        :param list[CreateIntent] intents: An array of objects defining the intents for the workspace.
        :param list[CreateEntity] entities: An array of objects defining the entities for the workspace.
        :param list[CreateDialogNode] dialog_nodes: An array of objects defining the nodes in the workspace dialog.
        :param list[CreateCounterexample] counterexamples: An array of objects defining input examples that have been marked as irrelevant input.
        :param object metadata: Any metadata related to the workspace.
        :param bool learning_opt_out: Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
        :return: A `dict` containing the `Workspace` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intents is not None:
            intents = [self._convert_model(x) for x in intents]
        if entities is not None:
            entities = [self._convert_model(x) for x in entities]
        if dialog_nodes is not None:
            dialog_nodes = [self._convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [self._convert_model(x) for x in counterexamples]
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
        url = '/v1/workspaces/{0}'.format(*self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # message
    #########################

    def message(self,
                workspace_id,
                input=None,
                alternate_intents=None,
                context=None,
                entities=None,
                intents=None,
                output=None):
        """
        Get a response to a user's input.

        :param str workspace_id: Unique identifier of the workspace.
        :param JSON input: A JSON object that includes the input text in the field 'text' (for example: {"text": "Hi!"})
        :param bool alternate_intents: Whether to return more than one intent. Set to `true` to return all matching intents.
        :param Context context: State information for the conversation. Continue a conversation by including the context object from the previous response.
        :param list[RuntimeEntity] entities: Include the entities from the previous response when they do not need to change and to prevent Watson from trying to identify them.
        :param list[RuntimeIntent] intents: An array of name-confidence pairs for the user input. Include the intents from the previous response when they do not need to change and to prevent Watson from trying to identify them.
        :param OutputData output: System output. Include the output from the request when you have several requests within the same Dialog turn to pass back in the intermediate information.
        :return: A `dict` containing the `MessageResponse` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if input is not None:
            input = self._convert_model(input)
        if context is not None:
            context = self._convert_model(context)
        if entities is not None:
            entities = [self._convert_model(x) for x in entities]
        if intents is not None:
            intents = [self._convert_model(x) for x in intents]
        if output is not None:
            output = self._convert_model(output)
        params = {'version': self.version}
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
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # intents
    #########################

    def create_intent(self,
                      workspace_id,
                      intent,
                      description=None,
                      examples=None):
        """
        Create intent.

        Create a new intent.

        :param str workspace_id: The workspace ID.
        :param str intent: The name of the intent.
        :param str description: The description of the intent.
        :param list[CreateExample] examples: An array of user input examples.
        :return: A `dict` containing the `Intent` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if examples is not None:
            examples = [self._convert_model(x) for x in examples]
        params = {'version': self.version}
        data = {
            'intent': intent,
            'description': description,
            'examples': examples
        }
        url = '/v1/workspaces/{0}/intents'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_intent(self, workspace_id, intent):
        """
        Delete intent.

        Delete an intent from a workspace.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/intents/{1}'.format(*self._encode_path_vars(
            workspace_id, intent))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_intent(self, workspace_id, intent, export=None):
        """
        Get intent.

        Get information about an intent, optionally including all intent content.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :param bool export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :return: A `dict` containing the `IntentExport` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        params = {'version': self.version, 'export': export}
        url = '/v1/workspaces/{0}/intents/{1}'.format(*self._encode_path_vars(
            workspace_id, intent))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_intents(self,
                     workspace_id,
                     export=None,
                     page_limit=None,
                     include_count=None,
                     sort=None,
                     cursor=None):
        """
        List intents.

        List the intents for a workspace.

        :param str workspace_id: The workspace ID.
        :param bool export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `IntentCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/intents'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def update_intent(self,
                      workspace_id,
                      intent,
                      new_intent=None,
                      new_description=None,
                      new_examples=None):
        """
        Update intent.

        Update an existing intent with new or modified data. You must provide data
        defining the content of the updated intent.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :param str new_intent: The name of the intent.
        :param str new_description: The description of the intent.
        :param list[CreateExample] new_examples: An array of user input examples for the intent.
        :return: A `dict` containing the `Intent` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if new_examples is not None:
            new_examples = [self._convert_model(x) for x in new_examples]
        params = {'version': self.version}
        data = {
            'intent': new_intent,
            'description': new_description,
            'examples': new_examples
        }
        url = '/v1/workspaces/{0}/intents/{1}'.format(*self._encode_path_vars(
            workspace_id, intent))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # examples
    #########################

    def create_example(self, workspace_id, intent, text):
        """
        Create user input example.

        Add a new user input example to an intent.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :param str text: The text of a user input example.
        :return: A `dict` containing the `Example` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        data = {'text': text}
        url = '/v1/workspaces/{0}/intents/{1}/examples'.format(
            *self._encode_path_vars(workspace_id, intent))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_example(self, workspace_id, intent, text):
        """
        Delete user input example.

        Delete a user input example from an intent.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :param str text: The text of the user input example.
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_example(self, workspace_id, intent, text):
        """
        Get user input example.

        Get information about a user input example.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :param str text: The text of the user input example.
        :return: A `dict` containing the `Example` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_examples(self,
                      workspace_id,
                      intent,
                      page_limit=None,
                      include_count=None,
                      sort=None,
                      cursor=None):
        """
        List user input examples.

        List the user input examples for an intent.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `ExampleCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/intents/{1}/examples'.format(
            *self._encode_path_vars(workspace_id, intent))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def update_example(self, workspace_id, intent, text, new_text=None):
        """
        Update user input example.

        Update the text of a user input example.

        :param str workspace_id: The workspace ID.
        :param str intent: The intent name (for example, `pizza_order`).
        :param str text: The text of the user input example.
        :param str new_text: The text of the user input example.
        :return: A `dict` containing the `Example` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        data = {'text': new_text}
        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # entities
    #########################

    def create_entity(self,
                      workspace_id,
                      entity,
                      description=None,
                      metadata=None,
                      values=None,
                      fuzzy_match=None):
        """
        Create entity.

        Create a new entity.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str description: The description of the entity.
        :param object metadata: Any metadata related to the value.
        :param list[CreateValue] values: An array of entity values.
        :param bool fuzzy_match: Whether to use fuzzy matching for the entity.
        :return: A `dict` containing the `Entity` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if values is not None:
            values = [self._convert_model(x) for x in values]
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
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_entity(self, workspace_id, entity):
        """
        Delete entity.

        Delete an entity from a workspace.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/entities/{1}'.format(*self._encode_path_vars(
            workspace_id, entity))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_entity(self, workspace_id, entity, export=None):
        """
        Get entity.

        Get information about an entity, optionally including all entity content.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param bool export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :return: A `dict` containing the `EntityExport` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        params = {'version': self.version, 'export': export}
        url = '/v1/workspaces/{0}/entities/{1}'.format(*self._encode_path_vars(
            workspace_id, entity))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_entities(self,
                      workspace_id,
                      export=None,
                      page_limit=None,
                      include_count=None,
                      sort=None,
                      cursor=None):
        """
        List entities.

        List the entities for a workspace.

        :param str workspace_id: The workspace ID.
        :param bool export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `EntityCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/entities'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def update_entity(self,
                      workspace_id,
                      entity,
                      new_entity=None,
                      new_description=None,
                      new_metadata=None,
                      new_fuzzy_match=None,
                      new_values=None):
        """
        Update entity.

        Update an existing entity with new or modified data.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str new_entity: The name of the entity.
        :param str new_description: The description of the entity.
        :param object new_metadata: Any metadata related to the entity.
        :param bool new_fuzzy_match: Whether to use fuzzy matching for the entity.
        :param list[CreateValue] new_values: An array of entity values.
        :return: A `dict` containing the `Entity` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if new_values is not None:
            new_values = [self._convert_model(x) for x in new_values]
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
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # values
    #########################

    def create_value(self,
                     workspace_id,
                     entity,
                     value,
                     metadata=None,
                     synonyms=None,
                     patterns=None,
                     value_type=None):
        """
        Add entity value.

        Create a new value for an entity.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param object metadata: Any metadata related to the entity value.
        :param list[str] synonyms: An array of synonyms for the entity value.
        :param list[str] patterns: An array of patterns for the entity value. A pattern is specified as a regular expression.
        :param str value_type: Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
        :return: A `dict` containing the `Value` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
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
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_value(self, workspace_id, entity, value):
        """
        Delete entity value.

        Delete a value for an entity.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_value(self, workspace_id, entity, value, export=None):
        """
        Get entity value.

        Get information about an entity value.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param bool export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :return: A `dict` containing the `ValueExport` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        params = {'version': self.version, 'export': export}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_values(self,
                    workspace_id,
                    entity,
                    export=None,
                    page_limit=None,
                    include_count=None,
                    sort=None,
                    cursor=None):
        """
        List entity values.

        List the values for an entity.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param bool export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `ValueCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/entities/{1}/values'.format(
            *self._encode_path_vars(workspace_id, entity))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def update_value(self,
                     workspace_id,
                     entity,
                     value,
                     new_value=None,
                     new_metadata=None,
                     new_type=None,
                     new_synonyms=None,
                     new_patterns=None):
        """
        Update entity value.

        Update the content of a value for an entity.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str new_value: The text of the entity value.
        :param object new_metadata: Any metadata related to the entity value.
        :param str new_type: Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
        :param list[str] new_synonyms: An array of synonyms for the entity value.
        :param list[str] new_patterns: An array of patterns for the entity value. A pattern is specified as a regular expression.
        :return: A `dict` containing the `Value` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
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
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # synonyms
    #########################

    def create_synonym(self, workspace_id, entity, value, synonym):
        """
        Add entity value synonym.

        Add a new synonym to an entity value.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
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
        params = {'version': self.version}
        data = {'synonym': synonym}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_synonym(self, workspace_id, entity, value, synonym):
        """
        Delete entity value synonym.

        Delete a synonym for an entity value.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
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
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_synonym(self, workspace_id, entity, value, synonym):
        """
        Get entity value synonym.

        Get information about a synonym for an entity value.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
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
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_synonyms(self,
                      workspace_id,
                      entity,
                      value,
                      page_limit=None,
                      include_count=None,
                      sort=None,
                      cursor=None):
        """
        List entity value synonyms.

        List the synonyms for an entity value.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `SynonymCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def update_synonym(self,
                       workspace_id,
                       entity,
                       value,
                       synonym,
                       new_synonym=None):
        """
        Update entity value synonym.

        Update the information about a synonym for an entity value.

        :param str workspace_id: The workspace ID.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param str new_synonym: The text of the synonym.
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
        params = {'version': self.version}
        data = {'synonym': new_synonym}
        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # dialogNodes
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
                           variable=None):
        """
        Create dialog node.

        Create a dialog node.

        :param str workspace_id: The workspace ID.
        :param str dialog_node: The dialog node ID.
        :param str description: The description of the dialog node.
        :param str conditions: The condition that will trigger the dialog node.
        :param str parent: The ID of the parent dialog node (if any).
        :param str previous_sibling: The previous dialog node.
        :param object output: The output of the dialog node.
        :param object context: The context for the dialog node.
        :param object metadata: The metadata for the dialog node.
        :param DialogNodeNextStep next_step: The next step to execute following this dialog node.
        :param list[DialogNodeAction] actions: The actions for the dialog node.
        :param str title: The alias used to identify the dialog node.
        :param str node_type: How the dialog node is processed.
        :param str event_name: How an `event_handler` node is processed.
        :param str variable: The location in the dialog context where output is stored.
        :return: A `dict` containing the `DialogNode` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        if next_step is not None:
            next_step = self._convert_model(next_step)
        if actions is not None:
            actions = [self._convert_model(x) for x in actions]
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
            'variable': variable
        }
        url = '/v1/workspaces/{0}/dialog_nodes'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_dialog_node(self, workspace_id, dialog_node):
        """
        Delete dialog node.

        Delete a dialog node from the workspace.

        :param str workspace_id: The workspace ID.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_dialog_node(self, workspace_id, dialog_node):
        """
        Get dialog node.

        Get information about a dialog node.

        :param str workspace_id: The workspace ID.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :return: A `dict` containing the `DialogNode` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_dialog_nodes(self,
                          workspace_id,
                          page_limit=None,
                          include_count=None,
                          sort=None,
                          cursor=None):
        """
        List dialog nodes.

        List the dialog nodes in the workspace.

        :param str workspace_id: The workspace ID.
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `DialogNodeCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/dialog_nodes'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def update_dialog_node(self,
                           workspace_id,
                           dialog_node,
                           new_dialog_node,
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
                           new_actions=None):
        """
        Update dialog node.

        Update information for a dialog node.

        :param str workspace_id: The workspace ID.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :param str new_dialog_node: The dialog node ID.
        :param str new_description: The description of the dialog node.
        :param str new_conditions: The condition that will trigger the dialog node.
        :param str new_parent: The ID of the parent dialog node (if any).
        :param str new_previous_sibling: The previous dialog node.
        :param object new_output: The output of the dialog node.
        :param object new_context: The context for the dialog node.
        :param object new_metadata: The metadata for the dialog node.
        :param DialogNodeNextStep new_next_step: The next step to execute following this dialog node.
        :param str new_title: The alias used to identify the dialog node.
        :param str new_type: How the node is processed.
        :param str new_event_name: How an `event_handler` node is processed.
        :param str new_variable: The location in the dialog context where output is stored.
        :param list[DialogNodeAction] new_actions: The actions for the dialog node.
        :return: A `dict` containing the `DialogNode` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        if new_dialog_node is None:
            raise ValueError('new_dialog_node must be provided')
        if new_next_step is not None:
            new_next_step = self._convert_model(new_next_step)
        if new_actions is not None:
            new_actions = [self._convert_model(x) for x in new_actions]
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
            'actions': new_actions
        }
        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    #########################
    # logs
    #########################

    def list_logs(self,
                  workspace_id,
                  sort=None,
                  filter=None,
                  page_limit=None,
                  cursor=None):
        """
        List log events in a workspace.

        List log events in a specific workspace.

        :param str workspace_id: The workspace ID.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str filter: A cacheable parameter that limits the results to those matching the specified filter. For more information, see the [documentation](https://console.bluemix.net/docs/services/conversation/filter-reference.html#filter-query-syntax).
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `LogCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
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
            method='GET', url=url, params=params, accept_json=True)
        return response

    #########################
    # counterexamples
    #########################

    def create_counterexample(self, workspace_id, text):
        """
        Create counterexample.

        Add a new counterexample to a workspace. Counterexamples are examples that have
        been marked as irrelevant input.

        :param str workspace_id: The workspace ID.
        :param str text: The text of a user input marked as irrelevant input.
        :return: A `dict` containing the `Counterexample` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        data = {'text': text}
        url = '/v1/workspaces/{0}/counterexamples'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response

    def delete_counterexample(self, workspace_id, text):
        """
        Delete counterexample.

        Delete a counterexample from a workspace. Counterexamples are examples that have
        been marked as irrelevant input.

        :param str workspace_id: The workspace ID.
        :param str text: The text of a user input counterexample (for example, `What are you wearing?`).
        :rtype: None
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        self.request(method='DELETE', url=url, params=params, accept_json=True)
        return None

    def get_counterexample(self, workspace_id, text):
        """
        Get counterexample.

        Get information about a counterexample. Counterexamples are examples that have
        been marked as irrelevant input.

        :param str workspace_id: The workspace ID.
        :param str text: The text of a user input counterexample (for example, `What are you wearing?`).
        :return: A `dict` containing the `Counterexample` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def list_counterexamples(self,
                             workspace_id,
                             page_limit=None,
                             include_count=None,
                             sort=None,
                             cursor=None):
        """
        List counterexamples.

        List the counterexamples for a workspace. Counterexamples are examples that have
        been marked as irrelevant input.

        :param str workspace_id: The workspace ID.
        :param int page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param bool include_count: Whether to include information about the number of records returned.
        :param str sort: Sorts the response according to the value of the specified property, in ascending or descending order.
        :param str cursor: A token identifying the last value from the previous page of results.
        :return: A `dict` containing the `CounterexampleCollection` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        url = '/v1/workspaces/{0}/counterexamples'.format(
            *self._encode_path_vars(workspace_id))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def update_counterexample(self, workspace_id, text, new_text=None):
        """
        Update counterexample.

        Update the text of a counterexample. Counterexamples are examples that have been
        marked as irrelevant input.

        :param str workspace_id: The workspace ID.
        :param str text: The text of a user input counterexample (for example, `What are you wearing?`).
        :param str new_text: The text of the example to be marked as irrelevant input.
        :return: A `dict` containing the `Counterexample` response.
        :rtype: dict
        """
        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        params = {'version': self.version}
        data = {'text': new_text}
        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        response = self.request(
            method='POST', url=url, params=params, json=data, accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class Context(object):
    """
    Context information for the message. Include the context from the previous response to
    maintain state for the conversation.

    :attr str conversation_id: The unique identifier of the conversation.
    :attr SystemResponse system: For internal use only.
    """

    def __init__(self, conversation_id, system, **kwargs):
        """
        Initialize a Context object.

        :param str conversation_id: The unique identifier of the conversation.
        :param SystemResponse system: For internal use only.
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
            args['conversation_id'] = _dict['conversation_id']
            del xtra['conversation_id']
        else:
            raise ValueError(
                'Required property \'conversation_id\' not present in Context JSON'
            )
        if 'system' in _dict:
            args['system'] = SystemResponse._from_dict(_dict['system'])
            del xtra['system']
        else:
            raise ValueError(
                'Required property \'system\' not present in Context JSON')
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
    :attr datetime created: The timestamp for creation of the counterexample.
    :attr datetime updated: The timestamp for the last update to the counterexample.
    """

    def __init__(self, text, created, updated):
        """
        Initialize a Counterexample object.

        :param str text: The text of the counterexample.
        :param datetime created: The timestamp for creation of the counterexample.
        :param datetime updated: The timestamp for the last update to the counterexample.
        """
        self.text = text
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Counterexample object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in Counterexample JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in Counterexample JSON'
            )
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in Counterexample JSON'
            )
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
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, counterexamples, pagination):
        """
        Initialize a CounterexampleCollection object.

        :param list[Counterexample] counterexamples: An array of objects describing the examples marked as irrelevant input.
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.counterexamples = counterexamples
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CounterexampleCollection object from a json dictionary."""
        args = {}
        if 'counterexamples' in _dict:
            args['counterexamples'] = [
                Counterexample._from_dict(x) for x in _dict['counterexamples']
            ]
        else:
            raise ValueError(
                'Required property \'counterexamples\' not present in CounterexampleCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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

    :attr str text: The text of a user input marked as irrelevant input.
    """

    def __init__(self, text):
        """
        Initialize a CreateCounterexample object.

        :param str text: The text of a user input marked as irrelevant input.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateCounterexample object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict['text']
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

    :attr str dialog_node: The dialog node ID.
    :attr str description: (optional) The description of the dialog node.
    :attr str conditions: (optional) The condition that will trigger the dialog node.
    :attr str parent: (optional) The ID of the parent dialog node (if any).
    :attr str previous_sibling: (optional) The previous dialog node.
    :attr object output: (optional) The output of the dialog node.
    :attr object context: (optional) The context for the dialog node.
    :attr object metadata: (optional) The metadata for the dialog node.
    :attr DialogNodeNextStep next_step: (optional) The next step to execute following this dialog node.
    :attr list[DialogNodeAction] actions: (optional) The actions for the dialog node.
    :attr str title: (optional) The alias used to identify the dialog node.
    :attr str node_type: (optional) How the dialog node is processed.
    :attr str event_name: (optional) How an `event_handler` node is processed.
    :attr str variable: (optional) The location in the dialog context where output is stored.
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
                 variable=None):
        """
        Initialize a CreateDialogNode object.

        :param str dialog_node: The dialog node ID.
        :param str description: (optional) The description of the dialog node.
        :param str conditions: (optional) The condition that will trigger the dialog node.
        :param str parent: (optional) The ID of the parent dialog node (if any).
        :param str previous_sibling: (optional) The previous dialog node.
        :param object output: (optional) The output of the dialog node.
        :param object context: (optional) The context for the dialog node.
        :param object metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep next_step: (optional) The next step to execute following this dialog node.
        :param list[DialogNodeAction] actions: (optional) The actions for the dialog node.
        :param str title: (optional) The alias used to identify the dialog node.
        :param str node_type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where output is stored.
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateDialogNode object from a json dictionary."""
        args = {}
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict['dialog_node']
        else:
            raise ValueError(
                'Required property \'dialog_node\' not present in CreateDialogNode JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'conditions' in _dict:
            args['conditions'] = _dict['conditions']
        if 'parent' in _dict:
            args['parent'] = _dict['parent']
        if 'previous_sibling' in _dict:
            args['previous_sibling'] = _dict['previous_sibling']
        if 'output' in _dict:
            args['output'] = _dict['output']
        if 'context' in _dict:
            args['context'] = _dict['context']
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'next_step' in _dict:
            args['next_step'] = DialogNodeNextStep._from_dict(
                _dict['next_step'])
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction._from_dict(x) for x in _dict['actions']
            ]
        if 'title' in _dict:
            args['title'] = _dict['title']
        if 'type' in _dict:
            args['node_type'] = _dict['type']
        if 'event_name' in _dict:
            args['event_name'] = _dict['event_name']
        if 'variable' in _dict:
            args['variable'] = _dict['variable']
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

    :attr str entity: The name of the entity.
    :attr str description: (optional) The description of the entity.
    :attr object metadata: (optional) Any metadata related to the value.
    :attr list[CreateValue] values: (optional) An array of entity values.
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

        :param str entity: The name of the entity.
        :param str description: (optional) The description of the entity.
        :param object metadata: (optional) Any metadata related to the value.
        :param list[CreateValue] values: (optional) An array of entity values.
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
            args['entity'] = _dict['entity']
        else:
            raise ValueError(
                'Required property \'entity\' not present in CreateEntity JSON')
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'values' in _dict:
            args['values'] = [
                CreateValue._from_dict(x) for x in _dict['values']
            ]
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict['fuzzy_match']
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

    :attr str text: The text of a user input example.
    """

    def __init__(self, text):
        """
        Initialize a CreateExample object.

        :param str text: The text of a user input example.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateExample object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict['text']
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

    :attr str intent: The name of the intent.
    :attr str description: (optional) The description of the intent.
    :attr list[CreateExample] examples: (optional) An array of user input examples.
    """

    def __init__(self, intent, description=None, examples=None):
        """
        Initialize a CreateIntent object.

        :param str intent: The name of the intent.
        :param str description: (optional) The description of the intent.
        :param list[CreateExample] examples: (optional) An array of user input examples.
        """
        self.intent = intent
        self.description = description
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateIntent object from a json dictionary."""
        args = {}
        if 'intent' in _dict:
            args['intent'] = _dict['intent']
        else:
            raise ValueError(
                'Required property \'intent\' not present in CreateIntent JSON')
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'examples' in _dict:
            args['examples'] = [
                CreateExample._from_dict(x) for x in _dict['examples']
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

    :attr str value: The text of the entity value.
    :attr object metadata: (optional) Any metadata related to the entity value.
    :attr list[str] synonyms: (optional) An array of synonyms for the entity value.
    :attr list[str] patterns: (optional) An array of patterns for the entity value. A pattern is specified as a regular expression.
    :attr str value_type: (optional) Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
    """

    def __init__(self,
                 value,
                 metadata=None,
                 synonyms=None,
                 patterns=None,
                 value_type=None):
        """
        Initialize a CreateValue object.

        :param str value: The text of the entity value.
        :param object metadata: (optional) Any metadata related to the entity value.
        :param list[str] synonyms: (optional) An array of synonyms for the entity value.
        :param list[str] patterns: (optional) An array of patterns for the entity value. A pattern is specified as a regular expression.
        :param str value_type: (optional) Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
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
            args['value'] = _dict['value']
        else:
            raise ValueError(
                'Required property \'value\' not present in CreateValue JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'synonyms' in _dict:
            args['synonyms'] = _dict['synonyms']
        if 'patterns' in _dict:
            args['patterns'] = _dict['patterns']
        if 'type' in _dict:
            args['value_type'] = _dict['type']
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
    :attr str description: The description of the dialog node.
    :attr str conditions: The condition that triggers the dialog node.
    :attr str parent: The ID of the parent dialog node.
    :attr str previous_sibling: The ID of the previous sibling dialog node.
    :attr object output: The output of the dialog node.
    :attr object context: The context (if defined) for the dialog node.
    :attr object metadata: The metadata (if any) for the dialog node.
    :attr DialogNodeNextStep next_step: The next step to execute following this dialog node.
    :attr datetime created: The timestamp for creation of the dialog node.
    :attr datetime updated: (optional) The timestamp for the most recent update to the dialog node.
    :attr list[DialogNodeAction] actions: (optional) The actions for the dialog node.
    :attr str title: The alias used to identify the dialog node.
    :attr str node_type: (optional) How the dialog node is processed.
    :attr str event_name: (optional) How an `event_handler` node is processed.
    :attr str variable: (optional) The location in the dialog context where output is stored.
    """

    def __init__(self,
                 dialog_node_id,
                 description,
                 conditions,
                 parent,
                 previous_sibling,
                 output,
                 context,
                 metadata,
                 next_step,
                 created,
                 title,
                 updated=None,
                 actions=None,
                 node_type=None,
                 event_name=None,
                 variable=None):
        """
        Initialize a DialogNode object.

        :param str dialog_node_id: The dialog node ID.
        :param str description: The description of the dialog node.
        :param str conditions: The condition that triggers the dialog node.
        :param str parent: The ID of the parent dialog node.
        :param str previous_sibling: The ID of the previous sibling dialog node.
        :param object output: The output of the dialog node.
        :param object context: The context (if defined) for the dialog node.
        :param object metadata: The metadata (if any) for the dialog node.
        :param DialogNodeNextStep next_step: The next step to execute following this dialog node.
        :param datetime created: The timestamp for creation of the dialog node.
        :param str title: The alias used to identify the dialog node.
        :param datetime updated: (optional) The timestamp for the most recent update to the dialog node.
        :param list[DialogNodeAction] actions: (optional) The actions for the dialog node.
        :param str node_type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where output is stored.
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNode object from a json dictionary."""
        args = {}
        if 'dialog_node' in _dict:
            args['dialog_node_id'] = _dict['dialog_node']
        else:
            raise ValueError(
                'Required property \'dialog_node\' not present in DialogNode JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict['description']
        else:
            raise ValueError(
                'Required property \'description\' not present in DialogNode JSON'
            )
        if 'conditions' in _dict:
            args['conditions'] = _dict['conditions']
        else:
            raise ValueError(
                'Required property \'conditions\' not present in DialogNode JSON'
            )
        if 'parent' in _dict:
            args['parent'] = _dict['parent']
        else:
            raise ValueError(
                'Required property \'parent\' not present in DialogNode JSON')
        if 'previous_sibling' in _dict:
            args['previous_sibling'] = _dict['previous_sibling']
        else:
            raise ValueError(
                'Required property \'previous_sibling\' not present in DialogNode JSON'
            )
        if 'output' in _dict:
            args['output'] = _dict['output']
        else:
            raise ValueError(
                'Required property \'output\' not present in DialogNode JSON')
        if 'context' in _dict:
            args['context'] = _dict['context']
        else:
            raise ValueError(
                'Required property \'context\' not present in DialogNode JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        else:
            raise ValueError(
                'Required property \'metadata\' not present in DialogNode JSON')
        if 'next_step' in _dict:
            args['next_step'] = DialogNodeNextStep._from_dict(
                _dict['next_step'])
        else:
            raise ValueError(
                'Required property \'next_step\' not present in DialogNode JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in DialogNode JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction._from_dict(x) for x in _dict['actions']
            ]
        if 'title' in _dict:
            args['title'] = _dict['title']
        else:
            raise ValueError(
                'Required property \'title\' not present in DialogNode JSON')
        if 'type' in _dict:
            args['node_type'] = _dict['type']
        if 'event_name' in _dict:
            args['event_name'] = _dict['event_name']
        if 'variable' in _dict:
            args['variable'] = _dict['variable']
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
            args['name'] = _dict['name']
        else:
            raise ValueError(
                'Required property \'name\' not present in DialogNodeAction JSON'
            )
        if 'type' in _dict:
            args['action_type'] = _dict['type']
        if 'parameters' in _dict:
            args['parameters'] = _dict['parameters']
        if 'result_variable' in _dict:
            args['result_variable'] = _dict['result_variable']
        else:
            raise ValueError(
                'Required property \'result_variable\' not present in DialogNodeAction JSON'
            )
        if 'credentials' in _dict:
            args['credentials'] = _dict['credentials']
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
    DialogNodeCollection.

    :attr list[DialogNode] dialog_nodes:
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, dialog_nodes, pagination):
        """
        Initialize a DialogNodeCollection object.

        :param list[DialogNode] dialog_nodes:
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.dialog_nodes = dialog_nodes
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeCollection object from a json dictionary."""
        args = {}
        if 'dialog_nodes' in _dict:
            args['dialog_nodes'] = [
                DialogNode._from_dict(x) for x in _dict['dialog_nodes']
            ]
        else:
            raise ValueError(
                'Required property \'dialog_nodes\' not present in DialogNodeCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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

    :attr str behavior: How the `next_step` reference is processed.
    :attr str dialog_node: (optional) The ID of the dialog node to process next.
    :attr str selector: (optional) Which part of the dialog node to process next.
    """

    def __init__(self, behavior, dialog_node=None, selector=None):
        """
        Initialize a DialogNodeNextStep object.

        :param str behavior: How the `next_step` reference is processed.
        :param str dialog_node: (optional) The ID of the dialog node to process next.
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
            args['behavior'] = _dict['behavior']
        else:
            raise ValueError(
                'Required property \'behavior\' not present in DialogNodeNextStep JSON'
            )
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict['dialog_node']
        if 'selector' in _dict:
            args['selector'] = _dict['selector']
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


class Entity(object):
    """
    Entity.

    :attr str entity_name: The name of the entity.
    :attr datetime created: The timestamp for creation of the entity.
    :attr datetime updated: The timestamp for the last update to the entity.
    :attr str description: (optional) The description of the entity.
    :attr object metadata: (optional) Any metadata related to the entity.
    :attr bool fuzzy_match: (optional) Whether fuzzy matching is used for the entity.
    """

    def __init__(self,
                 entity_name,
                 created,
                 updated,
                 description=None,
                 metadata=None,
                 fuzzy_match=None):
        """
        Initialize a Entity object.

        :param str entity_name: The name of the entity.
        :param datetime created: The timestamp for creation of the entity.
        :param datetime updated: The timestamp for the last update to the entity.
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
        if 'entity' in _dict:
            args['entity_name'] = _dict['entity']
        else:
            raise ValueError(
                'Required property \'entity\' not present in Entity JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in Entity JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in Entity JSON')
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict['fuzzy_match']
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

    :attr list[EntityExport] entities: An array of entities.
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, entities, pagination):
        """
        Initialize a EntityCollection object.

        :param list[EntityExport] entities: An array of entities.
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.entities = entities
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityCollection object from a json dictionary."""
        args = {}
        if 'entities' in _dict:
            args['entities'] = [
                EntityExport._from_dict(x) for x in _dict['entities']
            ]
        else:
            raise ValueError(
                'Required property \'entities\' not present in EntityCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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
    :attr datetime created: The timestamp for creation of the entity.
    :attr datetime updated: The timestamp for the last update to the entity.
    :attr str description: (optional) The description of the entity.
    :attr object metadata: (optional) Any metadata related to the entity.
    :attr bool fuzzy_match: (optional) Whether fuzzy matching is used for the entity.
    :attr list[ValueExport] values: (optional) An array of entity values.
    """

    def __init__(self,
                 entity_name,
                 created,
                 updated,
                 description=None,
                 metadata=None,
                 fuzzy_match=None,
                 values=None):
        """
        Initialize a EntityExport object.

        :param str entity_name: The name of the entity.
        :param datetime created: The timestamp for creation of the entity.
        :param datetime updated: The timestamp for the last update to the entity.
        :param str description: (optional) The description of the entity.
        :param object metadata: (optional) Any metadata related to the entity.
        :param bool fuzzy_match: (optional) Whether fuzzy matching is used for the entity.
        :param list[ValueExport] values: (optional) An array of entity values.
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
        if 'entity' in _dict:
            args['entity_name'] = _dict['entity']
        else:
            raise ValueError(
                'Required property \'entity\' not present in EntityExport JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in EntityExport JSON'
            )
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in EntityExport JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict['fuzzy_match']
        if 'values' in _dict:
            args['values'] = [
                ValueExport._from_dict(x) for x in _dict['values']
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

    :attr str example_text: The text of the example.
    :attr datetime created: The timestamp for creation of the example.
    :attr datetime updated: The timestamp for the last update to the example.
    """

    def __init__(self, example_text, created, updated):
        """
        Initialize a Example object.

        :param str example_text: The text of the example.
        :param datetime created: The timestamp for creation of the example.
        :param datetime updated: The timestamp for the last update to the example.
        """
        self.example_text = example_text
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Example object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['example_text'] = _dict['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in Example JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in Example JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in Example JSON')
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

    :attr list[Example] examples: An array of Example objects describing the examples defined for the intent.
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, examples, pagination):
        """
        Initialize a ExampleCollection object.

        :param list[Example] examples: An array of Example objects describing the examples defined for the intent.
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.examples = examples
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExampleCollection object from a json dictionary."""
        args = {}
        if 'examples' in _dict:
            args['examples'] = [
                Example._from_dict(x) for x in _dict['examples']
            ]
        else:
            raise ValueError(
                'Required property \'examples\' not present in ExampleCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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
    An object defining the user input.

    :attr str text: The text of the user input.
    """

    def __init__(self, text):
        """
        Initialize a InputData object.

        :param str text: The text of the user input.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InputData object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict['text']
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
    :attr datetime created: The timestamp for creation of the intent.
    :attr datetime updated: The timestamp for the last update to the intent.
    :attr str description: (optional) The description of the intent.
    """

    def __init__(self, intent_name, created, updated, description=None):
        """
        Initialize a Intent object.

        :param str intent_name: The name of the intent.
        :param datetime created: The timestamp for creation of the intent.
        :param datetime updated: The timestamp for the last update to the intent.
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
        if 'intent' in _dict:
            args['intent_name'] = _dict['intent']
        else:
            raise ValueError(
                'Required property \'intent\' not present in Intent JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in Intent JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in Intent JSON')
        if 'description' in _dict:
            args['description'] = _dict['description']
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

    :attr list[IntentExport] intents: An array of intents.
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, intents, pagination):
        """
        Initialize a IntentCollection object.

        :param list[IntentExport] intents: An array of intents.
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.intents = intents
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IntentCollection object from a json dictionary."""
        args = {}
        if 'intents' in _dict:
            args['intents'] = [
                IntentExport._from_dict(x) for x in _dict['intents']
            ]
        else:
            raise ValueError(
                'Required property \'intents\' not present in IntentCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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
    :attr datetime created: The timestamp for creation of the intent.
    :attr datetime updated: The timestamp for the last update to the intent.
    :attr str description: (optional) The description of the intent.
    :attr list[Example] examples: (optional) An array of user input examples.
    """

    def __init__(self,
                 intent_name,
                 created,
                 updated,
                 description=None,
                 examples=None):
        """
        Initialize a IntentExport object.

        :param str intent_name: The name of the intent.
        :param datetime created: The timestamp for creation of the intent.
        :param datetime updated: The timestamp for the last update to the intent.
        :param str description: (optional) The description of the intent.
        :param list[Example] examples: (optional) An array of user input examples.
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
        if 'intent' in _dict:
            args['intent_name'] = _dict['intent']
        else:
            raise ValueError(
                'Required property \'intent\' not present in IntentExport JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in IntentExport JSON'
            )
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in IntentExport JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'examples' in _dict:
            args['examples'] = [
                Example._from_dict(x) for x in _dict['examples']
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

    :attr list[LogExport] logs: An array of log events.
    :attr LogPagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, logs, pagination):
        """
        Initialize a LogCollection object.

        :param list[LogExport] logs: An array of log events.
        :param LogPagination pagination: An object defining the pagination data for the returned objects.
        """
        self.logs = logs
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogCollection object from a json dictionary."""
        args = {}
        if 'logs' in _dict:
            args['logs'] = [LogExport._from_dict(x) for x in _dict['logs']]
        else:
            raise ValueError(
                'Required property \'logs\' not present in LogCollection JSON')
        if 'pagination' in _dict:
            args['pagination'] = LogPagination._from_dict(_dict['pagination'])
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

    :attr MessageRequest request: A request formatted for the Conversation service.
    :attr MessageResponse response: A response from the Conversation service.
    :attr str log_id: A unique identifier for the logged message.
    :attr str request_timestamp: The timestamp for receipt of the message.
    :attr str response_timestamp: The timestamp for the system response to the message.
    :attr str workspace_id: The workspace ID.
    :attr str language: The language of the workspace where the message request was made.
    """

    def __init__(self, request, response, log_id, request_timestamp,
                 response_timestamp, workspace_id, language):
        """
        Initialize a LogExport object.

        :param MessageRequest request: A request formatted for the Conversation service.
        :param MessageResponse response: A response from the Conversation service.
        :param str log_id: A unique identifier for the logged message.
        :param str request_timestamp: The timestamp for receipt of the message.
        :param str response_timestamp: The timestamp for the system response to the message.
        :param str workspace_id: The workspace ID.
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
            args['request'] = MessageRequest._from_dict(_dict['request'])
        else:
            raise ValueError(
                'Required property \'request\' not present in LogExport JSON')
        if 'response' in _dict:
            args['response'] = MessageResponse._from_dict(_dict['response'])
        else:
            raise ValueError(
                'Required property \'response\' not present in LogExport JSON')
        if 'log_id' in _dict:
            args['log_id'] = _dict['log_id']
        else:
            raise ValueError(
                'Required property \'log_id\' not present in LogExport JSON')
        if 'request_timestamp' in _dict:
            args['request_timestamp'] = _dict['request_timestamp']
        else:
            raise ValueError(
                'Required property \'request_timestamp\' not present in LogExport JSON'
            )
        if 'response_timestamp' in _dict:
            args['response_timestamp'] = _dict['response_timestamp']
        else:
            raise ValueError(
                'Required property \'response_timestamp\' not present in LogExport JSON'
            )
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict['workspace_id']
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in LogExport JSON'
            )
        if 'language' in _dict:
            args['language'] = _dict['language']
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

    :attr str level: The severity of the message.
    :attr str msg: The text of the message.
    """

    def __init__(self, level, msg, **kwargs):
        """
        Initialize a LogMessage object.

        :param str level: The severity of the message.
        :param str msg: The text of the message.
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
            args['level'] = _dict['level']
            del xtra['level']
        else:
            raise ValueError(
                'Required property \'level\' not present in LogMessage JSON')
        if 'msg' in _dict:
            args['msg'] = _dict['msg']
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

    :attr str next_url: (optional) The URL that will return the next page of results.
    :attr int matched: (optional) Reserved for future use.
    """

    def __init__(self, next_url=None, matched=None):
        """
        Initialize a LogPagination object.

        :param str next_url: (optional) The URL that will return the next page of results.
        :param int matched: (optional) Reserved for future use.
        """
        self.next_url = next_url
        self.matched = matched

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogPagination object from a json dictionary."""
        args = {}
        if 'next_url' in _dict:
            args['next_url'] = _dict['next_url']
        if 'matched' in _dict:
            args['matched'] = _dict['matched']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'matched') and self.matched is not None:
            _dict['matched'] = self.matched
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
    An input object that includes the input text.

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
            args['text'] = _dict['text']
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
    :attr list[RuntimeEntity] entities: (optional) Include the entities from the previous response when they do not need to change and to prevent Watson from trying to identify them.
    :attr list[RuntimeIntent] intents: (optional) An array of name-confidence pairs for the user input. Include the intents from the previous response when they do not need to change and to prevent Watson from trying to identify them.
    :attr OutputData output: (optional) System output. Include the output from the request when you have several requests within the same Dialog turn to pass back in the intermediate information.
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
        :param list[RuntimeEntity] entities: (optional) Include the entities from the previous response when they do not need to change and to prevent Watson from trying to identify them.
        :param list[RuntimeIntent] intents: (optional) An array of name-confidence pairs for the user input. Include the intents from the previous response when they do not need to change and to prevent Watson from trying to identify them.
        :param OutputData output: (optional) System output. Include the output from the request when you have several requests within the same Dialog turn to pass back in the intermediate information.
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
            args['input'] = InputData._from_dict(_dict['input'])
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict['alternate_intents']
        if 'context' in _dict:
            args['context'] = Context._from_dict(_dict['context'])
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in _dict['entities']
            ]
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in _dict['intents']
            ]
        if 'output' in _dict:
            args['output'] = OutputData._from_dict(_dict['output'])
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
    :attr bool alternate_intents: (optional) Whether to return more than one intent. `true` indicates that all matching intents are returned.
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
        :param bool alternate_intents: (optional) Whether to return more than one intent. `true` indicates that all matching intents are returned.
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
            args['input'] = MessageInput._from_dict(_dict['input'])
            del xtra['input']
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in _dict['intents']
            ]
            del xtra['intents']
        else:
            raise ValueError(
                'Required property \'intents\' not present in MessageResponse JSON'
            )
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in _dict['entities']
            ]
            del xtra['entities']
        else:
            raise ValueError(
                'Required property \'entities\' not present in MessageResponse JSON'
            )
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict['alternate_intents']
            del xtra['alternate_intents']
        if 'context' in _dict:
            args['context'] = Context._from_dict(_dict['context'])
            del xtra['context']
        else:
            raise ValueError(
                'Required property \'context\' not present in MessageResponse JSON'
            )
        if 'output' in _dict:
            args['output'] = OutputData._from_dict(_dict['output'])
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

    :attr list[LogMessage] log_messages: Up to 50 messages logged with the request.
    :attr list[str] text: An array of responses to the user.
    :attr list[str] nodes_visited: (optional) An array of the nodes that were triggered to create the response.
    """

    def __init__(self, log_messages, text, nodes_visited=None, **kwargs):
        """
        Initialize a OutputData object.

        :param list[LogMessage] log_messages: Up to 50 messages logged with the request.
        :param list[str] text: An array of responses to the user.
        :param list[str] nodes_visited: (optional) An array of the nodes that were triggered to create the response.
        :param **kwargs: (optional) Any additional properties.
        """
        self.log_messages = log_messages
        self.text = text
        self.nodes_visited = nodes_visited
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OutputData object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'log_messages' in _dict:
            args['log_messages'] = [
                LogMessage._from_dict(x) for x in _dict['log_messages']
            ]
            del xtra['log_messages']
        else:
            raise ValueError(
                'Required property \'log_messages\' not present in OutputData JSON'
            )
        if 'text' in _dict:
            args['text'] = _dict['text']
            del xtra['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in OutputData JSON')
        if 'nodes_visited' in _dict:
            args['nodes_visited'] = _dict['nodes_visited']
            del xtra['nodes_visited']
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
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'log_messages', 'text', 'nodes_visited'}
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
    """

    def __init__(self, refresh_url, next_url=None, total=None, matched=None):
        """
        Initialize a Pagination object.

        :param str refresh_url: The URL that will return the same page of results.
        :param str next_url: (optional) The URL that will return the next page of results.
        :param int total: (optional) Reserved for future use.
        :param int matched: (optional) Reserved for future use.
        """
        self.refresh_url = refresh_url
        self.next_url = next_url
        self.total = total
        self.matched = matched

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pagination object from a json dictionary."""
        args = {}
        if 'refresh_url' in _dict:
            args['refresh_url'] = _dict['refresh_url']
        else:
            raise ValueError(
                'Required property \'refresh_url\' not present in Pagination JSON'
            )
        if 'next_url' in _dict:
            args['next_url'] = _dict['next_url']
        if 'total' in _dict:
            args['total'] = _dict['total']
        if 'matched' in _dict:
            args['matched'] = _dict['matched']
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

    :attr str entity: The recognized entity from a term in the input.
    :attr list[int] location: Zero-based character offsets that indicate where the entity value begins and ends in the input text.
    :attr str value: The term in the input text that was recognized.
    :attr float confidence: (optional) A decimal percentage that represents Watson's confidence in the entity.
    :attr object metadata: (optional) The metadata for the entity.
    """

    def __init__(self,
                 entity,
                 location,
                 value,
                 confidence=None,
                 metadata=None,
                 **kwargs):
        """
        Initialize a RuntimeEntity object.

        :param str entity: The recognized entity from a term in the input.
        :param list[int] location: Zero-based character offsets that indicate where the entity value begins and ends in the input text.
        :param str value: The term in the input text that was recognized.
        :param float confidence: (optional) A decimal percentage that represents Watson's confidence in the entity.
        :param object metadata: (optional) The metadata for the entity.
        :param **kwargs: (optional) Any additional properties.
        """
        self.entity = entity
        self.location = location
        self.value = value
        self.confidence = confidence
        self.metadata = metadata
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEntity object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'entity' in _dict:
            args['entity'] = _dict['entity']
            del xtra['entity']
        else:
            raise ValueError(
                'Required property \'entity\' not present in RuntimeEntity JSON'
            )
        if 'location' in _dict:
            args['location'] = _dict['location']
            del xtra['location']
        else:
            raise ValueError(
                'Required property \'location\' not present in RuntimeEntity JSON'
            )
        if 'value' in _dict:
            args['value'] = _dict['value']
            del xtra['value']
        else:
            raise ValueError(
                'Required property \'value\' not present in RuntimeEntity JSON')
        if 'confidence' in _dict:
            args['confidence'] = _dict['confidence']
            del xtra['confidence']
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
            del xtra['metadata']
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
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'entity', 'location', 'value', 'confidence', 'metadata'}
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
            args['intent'] = _dict['intent']
            del xtra['intent']
        else:
            raise ValueError(
                'Required property \'intent\' not present in RuntimeIntent JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict['confidence']
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
    :attr datetime created: The timestamp for creation of the synonym.
    :attr datetime updated: The timestamp for the most recent update to the synonym.
    """

    def __init__(self, synonym_text, created, updated):
        """
        Initialize a Synonym object.

        :param str synonym_text: The text of the synonym.
        :param datetime created: The timestamp for creation of the synonym.
        :param datetime updated: The timestamp for the most recent update to the synonym.
        """
        self.synonym_text = synonym_text
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Synonym object from a json dictionary."""
        args = {}
        if 'synonym' in _dict:
            args['synonym_text'] = _dict['synonym']
        else:
            raise ValueError(
                'Required property \'synonym\' not present in Synonym JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in Synonym JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in Synonym JSON')
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
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, synonyms, pagination):
        """
        Initialize a SynonymCollection object.

        :param list[Synonym] synonyms: An array of synonyms.
        :param Pagination pagination: An object defining the pagination data for the returned objects.
        """
        self.synonyms = synonyms
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SynonymCollection object from a json dictionary."""
        args = {}
        if 'synonyms' in _dict:
            args['synonyms'] = [
                Synonym._from_dict(x) for x in _dict['synonyms']
            ]
        else:
            raise ValueError(
                'Required property \'synonyms\' not present in SynonymCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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
    :attr datetime created: The timestamp for creation of the entity value.
    :attr datetime updated: The timestamp for the last update to the entity value.
    :attr list[str] synonyms: (optional) An array of synonyms for the entity value.
    :attr list[str] patterns: (optional) An array of patterns for the entity value. A pattern is specified as a regular expression.
    :attr str value_type: Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
    """

    def __init__(self,
                 value_text,
                 created,
                 updated,
                 value_type,
                 metadata=None,
                 synonyms=None,
                 patterns=None):
        """
        Initialize a Value object.

        :param str value_text: The text of the entity value.
        :param datetime created: The timestamp for creation of the entity value.
        :param datetime updated: The timestamp for the last update to the entity value.
        :param str value_type: Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
        :param object metadata: (optional) Any metadata related to the entity value.
        :param list[str] synonyms: (optional) An array of synonyms for the entity value.
        :param list[str] patterns: (optional) An array of patterns for the entity value. A pattern is specified as a regular expression.
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
        if 'value' in _dict:
            args['value_text'] = _dict['value']
        else:
            raise ValueError(
                'Required property \'value\' not present in Value JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in Value JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in Value JSON')
        if 'synonyms' in _dict:
            args['synonyms'] = _dict['synonyms']
        if 'patterns' in _dict:
            args['patterns'] = _dict['patterns']
        if 'type' in _dict:
            args['value_type'] = _dict['type']
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
                ValueExport._from_dict(x) for x in _dict['values']
            ]
        else:
            raise ValueError(
                'Required property \'values\' not present in ValueCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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
    :attr datetime created: The timestamp for creation of the entity value.
    :attr datetime updated: The timestamp for the last update to the entity value.
    :attr list[str] synonyms: (optional) An array of synonyms.
    :attr list[str] patterns: (optional) An array of patterns for the entity value. A pattern is specified as a regular expression.
    :attr str value_type: Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
    """

    def __init__(self,
                 value_text,
                 created,
                 updated,
                 value_type,
                 metadata=None,
                 synonyms=None,
                 patterns=None):
        """
        Initialize a ValueExport object.

        :param str value_text: The text of the entity value.
        :param datetime created: The timestamp for creation of the entity value.
        :param datetime updated: The timestamp for the last update to the entity value.
        :param str value_type: Specifies the type of value (`synonyms` or `patterns`). The default value is `synonyms`.
        :param object metadata: (optional) Any metadata related to the entity value.
        :param list[str] synonyms: (optional) An array of synonyms.
        :param list[str] patterns: (optional) An array of patterns for the entity value. A pattern is specified as a regular expression.
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
        if 'value' in _dict:
            args['value_text'] = _dict['value']
        else:
            raise ValueError(
                'Required property \'value\' not present in ValueExport JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in ValueExport JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in ValueExport JSON')
        if 'synonyms' in _dict:
            args['synonyms'] = _dict['synonyms']
        if 'patterns' in _dict:
            args['patterns'] = _dict['patterns']
        if 'type' in _dict:
            args['value_type'] = _dict['type']
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
    :attr datetime created: The timestamp for creation of the workspace.
    :attr datetime updated: The timestamp for the last update to the workspace.
    :attr str workspace_id: The workspace ID.
    :attr str description: (optional) The description of the workspace.
    :attr object metadata: (optional) Any metadata that is required by the workspace.
    :attr bool learning_opt_out: (optional) Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
    """

    def __init__(self,
                 name,
                 language,
                 created,
                 updated,
                 workspace_id,
                 description=None,
                 metadata=None,
                 learning_opt_out=None):
        """
        Initialize a Workspace object.

        :param str name: The name of the workspace.
        :param str language: The language of the workspace.
        :param datetime created: The timestamp for creation of the workspace.
        :param datetime updated: The timestamp for the last update to the workspace.
        :param str workspace_id: The workspace ID.
        :param str description: (optional) The description of the workspace.
        :param object metadata: (optional) Any metadata that is required by the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
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
            args['name'] = _dict['name']
        else:
            raise ValueError(
                'Required property \'name\' not present in Workspace JSON')
        if 'language' in _dict:
            args['language'] = _dict['language']
        else:
            raise ValueError(
                'Required property \'language\' not present in Workspace JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in Workspace JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in Workspace JSON')
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict['workspace_id']
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in Workspace JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict['description']
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        if 'learning_opt_out' in _dict:
            args['learning_opt_out'] = _dict['learning_opt_out']
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

    :attr list[Workspace] workspaces: An array of workspaces.
    :attr Pagination pagination: An object defining the pagination data for the returned objects.
    """

    def __init__(self, workspaces, pagination):
        """
        Initialize a WorkspaceCollection object.

        :param list[Workspace] workspaces: An array of workspaces.
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
                Workspace._from_dict(x) for x in _dict['workspaces']
            ]
        else:
            raise ValueError(
                'Required property \'workspaces\' not present in WorkspaceCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict['pagination'])
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
    :attr datetime created: The timestamp for creation of the workspace.
    :attr datetime updated: The timestamp for the last update to the workspace.
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
                 created,
                 updated,
                 workspace_id,
                 status,
                 learning_opt_out,
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
        :param datetime created: The timestamp for creation of the workspace.
        :param datetime updated: The timestamp for the last update to the workspace.
        :param str workspace_id: The workspace ID.
        :param str status: The current status of the workspace.
        :param bool learning_opt_out: Whether training data from the workspace can be used by IBM for general service improvements. `true` indicates that workspace training data is not to be used.
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
            args['name'] = _dict['name']
        else:
            raise ValueError(
                'Required property \'name\' not present in WorkspaceExport JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict['description']
        else:
            raise ValueError(
                'Required property \'description\' not present in WorkspaceExport JSON'
            )
        if 'language' in _dict:
            args['language'] = _dict['language']
        else:
            raise ValueError(
                'Required property \'language\' not present in WorkspaceExport JSON'
            )
        if 'metadata' in _dict:
            args['metadata'] = _dict['metadata']
        else:
            raise ValueError(
                'Required property \'metadata\' not present in WorkspaceExport JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        else:
            raise ValueError(
                'Required property \'created\' not present in WorkspaceExport JSON'
            )
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict['updated'])
        else:
            raise ValueError(
                'Required property \'updated\' not present in WorkspaceExport JSON'
            )
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict['workspace_id']
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in WorkspaceExport JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict['status']
        else:
            raise ValueError(
                'Required property \'status\' not present in WorkspaceExport JSON'
            )
        if 'learning_opt_out' in _dict:
            args['learning_opt_out'] = _dict['learning_opt_out']
        else:
            raise ValueError(
                'Required property \'learning_opt_out\' not present in WorkspaceExport JSON'
            )
        if 'intents' in _dict:
            args['intents'] = [
                IntentExport._from_dict(x) for x in _dict['intents']
            ]
        if 'entities' in _dict:
            args['entities'] = [
                EntityExport._from_dict(x) for x in _dict['entities']
            ]
        if 'counterexamples' in _dict:
            args['counterexamples'] = [
                Counterexample._from_dict(x) for x in _dict['counterexamples']
            ]
        if 'dialog_nodes' in _dict:
            args['dialog_nodes'] = [
                DialogNode._from_dict(x) for x in _dict['dialog_nodes']
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
