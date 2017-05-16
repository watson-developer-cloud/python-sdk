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
The IBM Watson Conversation service combines machine learning, natural
language understanding, and integrated dialog tools to create conversation
flows between your apps and your users.
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService

class ConversationV1(WatsonDeveloperCloudService):
    """Client for the Conversation service."""

    default_url = 'https://gateway.watsonplatform.net/conversation/api'
    latest_version = '2017-04-21'

    def __init__(self, version, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'conversation', url,
                                             **kwargs)
        self.version = version

    #########################
    # counterexamples
    #########################

    def create_counterexample(self, workspace_id, text):
        """
        Create counterexample.

        Add a new counterexample to a workspace. Counterexamples are
        examples that have been marked as irrelevant input.

        :param workspace_id: The workspace ID.
        :param text: The text of a user input example.
        """
        params = {'version': self.version}
        data = {'text': text}
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/counterexamples'.format(workspace_id),
            params=params,
            json=data,
            accept_json=True)

    def delete_counterexample(self, workspace_id, text):
        """
        Delete counterexample.

        Delete a counterexample from a workspace. Counterexamples are
        examples that have been marked as irrelevant input.

        :param workspace_id: The workspace ID.
        :param text: The text of a user input counterexample (for example,
            `What are you wearing?`).
        """
        params = {'version': self.version}
        return self.request(
            method='DELETE',
            url='/v1/workspaces/{0}/counterexamples/{1}'.format(
                workspace_id, text),
            params=params,
            accept_json=True)

    def get_counterexample(self, workspace_id, text):
        """
        Get counterexample.

        Get information about a counterexample. Counterexamples are
        examples that have been marked as irrelevant input.

        :param workspace_id: The workspace ID.
        :param text: The text of a user input counterexample (for example,
            `What are you wearing?`).
        """
        params = {'version': self.version}
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/counterexamples/{1}'.format(
                workspace_id, text),
            params=params,
            accept_json=True)

    def list_counterexamples(self,
                             workspace_id,
                             page_limit=None,
                             include_count=None,
                             sort=None,
                             cursor=None):
        """
        List counterexamples.

        List the counterexamples for a workspace. Counterexamples are
        examples that have been marked as irrelevant input.

        :param workspace_id: The workspace ID.
        :param page_limit: The number of records to return in each page of
            results. The default page limit is 100.
        :param include_count: Whether to include information about the number
            of records returned.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param cursor: A token identifying the last value from the previous
            page of results.
        """
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/counterexamples'.format(workspace_id),
            params=params,
            accept_json=True)

    def update_counterexample(self, workspace_id, text, new_text=None):
        """
        Update counterexample.

        Update the text of a counterexample. Counterexamples are
        examples that have been marked as irrelevant input.

        :param workspace_id: The workspace ID.
        :param text: The text of a user input counterexample (for example,
            `What are you wearing?`).
        :param new_text: The new text of a user input counterexample.
        """
        params = {'version': self.version}
        data = {'text': new_text}
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/counterexamples/{1}'.format(
                workspace_id, text),
            params=params,
            json=data,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param description: The description of the entity.
        :param metadata: Any metadata related to the value.
        :param values: An array of entity values.
        :param fuzzy_match: Whether to use fuzzy matching for the entity.
        """
        params = {'version': self.version}
        data = {
            'entity': entity,
            'description': description,
            'metadata': metadata,
            'values': values,
            'fuzzy_match': fuzzy_match
        }
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/entities'.format(workspace_id),
            params=params,
            json=data,
            accept_json=True)

    def delete_entity(self, workspace_id, entity):
        """
        Delete entity.

        Delete an entity from a workspace.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        """
        params = {'version': self.version}
        return self.request(
            method='DELETE',
            url='/v1/workspaces/{0}/entities/{1}'.format(workspace_id, entity),
            params=params,
            accept_json=True)

    def get_entity(self, workspace_id, entity, export=None):
        """
        Get entity.

        Get information about an entity, optionally
        including all entity content.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param export: Whether to include all element content in the
            returned data. If export=`false`, the returned data includes
            only information about the element itself. If export=`true`,
            all content, including subelements, is included. The default
            value is `false`.
        """
        params = {'version': self.version, 'export': export}
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/entities/{1}'.format(workspace_id, entity),
            params=params,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param export: Whether to include all element content in the
            returned data. If export=`false`, the returned data includes
            only information about the element itself. If export=`true`,
            all content, including subelements, is included. The default
            value is `false`.
        :param page_limit: The number of records to return in each page of
            results. The default page limit is 100.
        :param include_count: Whether to include information about the number
            of records returned.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param cursor: A token identifying the last value from the previous
            page of results.
        """
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/entities'.format(workspace_id),
            params=params,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param new_entity: The new name of the entity.
        :param new_description: The new description of the entity.
        :param new_metadata: Any new metadata related to the entity.
        :param new_fuzzy_match: Whether to use fuzzy matching for the entity.
        :param new_values: A new array of entity values.
        """
        params = {'version': self.version}
        data = {
            'entity': new_entity,
            'description': new_description,
            'metadata': new_metadata,
            'fuzzy_match': new_fuzzy_match,
            'values': new_values
        }
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/entities/{1}'.format(workspace_id, entity),
            params=params,
            json=data,
            accept_json=True)

    #########################
    # examples
    #########################

    def create_example(self, workspace_id, intent, text):
        """
        Create user input example.

        Add a new user input example to an intent.

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of a user input example.
        """
        params = {'version': self.version}
        data = {'text': text}
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/intents/{1}/examples'.format(
                workspace_id, intent),
            params=params,
            json=data,
            accept_json=True)

    def delete_example(self, workspace_id, intent, text):
        """
        Delete user input example.

        Delete a user input example from an intent.

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of the user input example.
        """
        params = {'version': self.version}
        return self.request(
            method='DELETE',
            url='/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
                workspace_id, intent, text),
            params=params,
            accept_json=True)

    def get_example(self, workspace_id, intent, text):
        """
        Get user input example.

        Get information about a user input example.

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of the user input example.
        """
        params = {'version': self.version}
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
                workspace_id, intent, text),
            params=params,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param page_limit: The number of records to return in each page of
            results. The default page limit is 100.
        :param include_count: Whether to include information about the number
            of records returned.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param cursor: A token identifying the last value from the previous
            page of results.
        """
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/intents/{1}/examples'.format(
                workspace_id, intent),
            params=params,
            accept_json=True)

    def update_example(self, workspace_id, intent, text, new_text=None):
        """
        Update user input example.

        Update the text of a user input example.

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of the user input example.
        :param new_text: The text of the user input example.
        """
        params = {'version': self.version}
        data = {'text': new_text}
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
                workspace_id, intent, text),
            params=params,
            json=data,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param intent: The name of the intent.
        :param description: The description of the intent.
        :param examples: An array of user input examples.
        """
        params = {'version': self.version}
        data = {
            'intent': intent,
            'description': description,
            'examples': examples
        }
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/intents'.format(workspace_id),
            params=params,
            json=data,
            accept_json=True)

    def delete_intent(self, workspace_id, intent):
        """
        Delete intent.

        Delete an intent from a workspace.

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        """
        params = {'version': self.version}
        return self.request(
            method='DELETE',
            url='/v1/workspaces/{0}/intents/{1}'.format(workspace_id, intent),
            params=params,
            accept_json=True)

    def get_intent(self, workspace_id, intent, export=None):
        """
        Get intent.

        Get information about an intent, optionally
        including all intent content.

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param export: Whether to include all element content in the
            returned data. If export=`false`, the returned data includes
            only information about the element itself. If export=`true`,
            all content, including subelements, is included. The default
            value is `false`.
        """
        params = {'version': self.version, 'export': export}
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/intents/{1}'.format(workspace_id, intent),
            params=params,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param export: Whether to include all element content in the
            returned data. If export=`false`, the returned data includes
            only information about the element itself. If export=`true`,
            all content, including subelements, is included. The default
            value is `false`.
        :param page_limit: The number of records to return in each page of
            results. The default page limit is 100.
        :param include_count: Whether to include information about the
            number of records returned.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param cursor: A token identifying the last value from the previous
            page of results.
        """
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/intents'.format(workspace_id),
            params=params,
            accept_json=True)

    def update_intent(self,
                      workspace_id,
                      intent,
                      new_intent=None,
                      new_description=None,
                      new_examples=None):
        """
        Update intent.

        Update an existing intent with new or modified data. You must provide data defining the content of the updated intent.

        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param new_intent: The new intent name.
        :param new_description: The description of the intent.
        :param new_examples: An array of new user input examples.
        """
        params = {'version': self.version}
        data = {
            'intent': new_intent,
            'description': new_description,
            'examples': new_examples
        }
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/intents/{1}'.format(workspace_id, intent),
            params=params,
            json=data,
            accept_json=True)

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
        List log events.

        List log events associated with the given workspace.

        :param workspace_id: The workspace ID.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param filter: A cacheable parameter that limits the results to
            those matching the specified filter.
        :param page_limit: The number of records to return in each page
            of results. The default page limit is 100.
        :param cursor: A token identifying the last value from the
            previous page of results.
        """
        params = {
            'version': self.version,
            'sort': sort,
            'filter': filter,
            'page_limit': page_limit,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/logs'.format(workspace_id),
            params=params,
            accept_json=True)

    #########################
    # message
    #########################

    def message(self,
                workspace_id,
                message_input,
                alternate_intents=None,
                context=None,
                entities=None,
                intents=None,
                output=None):
        """
        Get a response to a user's input.

        Send a user's message and receive a response.

        :param workspace_id: Unique identifier of the workspace.
        :param message_input: An input object that includes the input text.
        :param alternate_intents: Whether to return more than one intent.
            Set to `true` to return all matching intents.
        :param context: State information for the conversation. Continue a
            conversation by including the context object from the previous
            response.
        :param entities: Include the entities from the previous response when
            they do not need to change and to prevent Watson from trying to
            identify them.
        :param intents: An array of name-confidence pairs for the user input.
            Include the intents from the previous response when they do not
            need to change and to prevent Watson from trying to identify them.
        :param output: System output. Include the output from the request
            when you have several requests within the same Dialog turn to
            pass back in the intermediate information.
        """
        params = {'version': self.version}
        data = {
            'input': message_input,
            'alternate_intents': alternate_intents,
            'context': context,
            'entities': entities,
            'intents': intents,
            'output': output
        }
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/message'.format(workspace_id),
            params=params,
            json=data,
            accept_json=True)

    #########################
    # synonyms
    #########################

    def create_synonym(self, workspace_id, entity, value, synonym):
        """
        Add entity value synonym.

        Add a new synonym to an entity value.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param synonym: The text of the synonym.
        """
        params = {'version': self.version}
        data = {'synonym': synonym}
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
                workspace_id, entity, value),
            params=params,
            json=data,
            accept_json=True)

    def delete_synonym(self, workspace_id, entity, value, synonym):
        """
        Delete entity value synonym.

        Delete a synonym for an entity value.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param synonym: The text of the synonym.
        """
        params = {'version': self.version}
        return self.request(
            method='DELETE',
            url=
            '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
                workspace_id, entity, value, synonym),
            params=params,
            accept_json=True)

    def get_synonym(self, workspace_id, entity, value, synonym):
        """
        Get entity value synonym.

        Get information about a synonym for an entity value.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param synonym: The text of the synonym.
        """
        params = {'version': self.version}
        return self.request(
            method='GET',
            url=
            '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
                workspace_id, entity, value, synonym),
            params=params,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param page_limit: The number of records to return in each page
            of results. The default page limit is 100.
        :param include_count: Whether to include information about the
            number of records returned.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param cursor: A token identifying the last value from the
            previous page of results.
        """
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
                workspace_id, entity, value),
            params=params,
            accept_json=True)

    def update_synonym(self,
                       workspace_id,
                       entity,
                       value,
                       synonym,
                       new_synonym=None):
        """
        Update entity value synonym.

        Update the information about a synonym for an entity value.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param synonym: The text of the synonym.
        :param new_synonym: The text of the synonym.
        """
        params = {'version': self.version}
        data = {'synonym': new_synonym}
        return self.request(
            method='POST',
            url=
            '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
                workspace_id, entity, value, synonym),
            params=params,
            json=data,
            accept_json=True)

    #########################
    # values
    #########################

    def create_value(self,
                     workspace_id,
                     entity,
                     value,
                     metadata=None,
                     synonyms=None):
        """
        Add entity value.

        Create a new value for an entity.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param metadata: Any metadata related to the entity value.
        :param synonyms: Any array of synonyms for the entity value.
        """
        params = {'version': self.version}
        data = {'value': value, 'metadata': metadata, 'synonyms': synonyms}
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/entities/{1}/values'.format(
                workspace_id, entity),
            params=params,
            json=data,
            accept_json=True)

    def delete_value(self, workspace_id, entity, value):
        """
        Delete entity value.

        Delete a value for an entity.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        """
        params = {'version': self.version}
        return self.request(
            method='DELETE',
            url='/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
                workspace_id, entity, value),
            params=params,
            accept_json=True)

    def get_value(self, workspace_id, entity, value, export=None):
        """
        Get entity value.

        Get information about an entity value.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param export: Whether to include all element content in the
            returned data. If export=`false`, the returned data includes
            only information about the element itself. If export=`true`,
            all content, including subelements, is included. The default
            value is `false`.
        """
        params = {'version': self.version, 'export': export}
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
                workspace_id, entity, value),
            params=params,
            accept_json=True)

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

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param export: Whether to include all element content in the
            returned data. If export=`false`, the returned data includes
            only information about the element itself. If export=`true`,
            all content, including subelements, is included. The default
            value is `false`.
        :param page_limit: The number of records to return in each page
            of results. The default page limit is 100.
        :param include_count: Whether to include information about the
            number of records returned.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param cursor: A token identifying the last value from the
            previous page of results.
        """
        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}/entities/{1}/values'.format(
                workspace_id, entity),
            params=params,
            accept_json=True)

    def update_value(self,
                     workspace_id,
                     entity,
                     value,
                     new_value=None,
                     new_metadata=None,
                     new_synonyms=None):
        """
        Update entity value.

        Update the content of a value for an entity.

        :param workspace_id: The workspace ID.
        :param entity: The name of the entity.
        :param value: The text of the entity value.
        :param new_value: The text of the entity value.
        :param new_metadata: Any metadata related to the entity value.
        :param new_synonyms: An array of synonyms for the entity value.
        """
        params = {'version': self.version}
        data = {
            'value': new_value,
            'metadata': new_metadata,
            'synonyms': new_synonyms
        }
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
                workspace_id, entity, value),
            params=params,
            json=data,
            accept_json=True)

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
                         metadata=None):
        """
        Create workspace.

        Create a workspace based on component objects. You must provide
        workspace components defining the content of the new workspace.

        :param name: The name of the workspace.
        :param description: The description of the workspace.
        :param language: The language of the workspace.
        :param intents: An array of CreateIntent objects defining the
            intents for the workspace.
        :param entities: An array of CreateEntity objects defining the
            entities for the workspace.
        :param dialog_nodes: An array of CreateDialogNode objects defining
            the nodes in the workspace dialog.
        :param counterexamples: An array of CreateExample objects defining
            input examples that have been marked as irrelevant input.
        :param metadata: Any metadata related to the workspace.
        """
        params = {'version': self.version}
        data = {
            'name': name,
            'description': description,
            'language': language,
            'intents': intents,
            'entities': entities,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata
        }
        return self.request(
            method='POST',
            url='/v1/workspaces',
            params=params,
            json=data,
            accept_json=True)

    def delete_workspace(self, workspace_id):
        """
        Delete workspace.

        Delete a workspace from the service instance.

        :param workspace_id: The workspace ID.
        """
        params = {'version': self.version}
        return self.request(
            method='DELETE',
            url='/v1/workspaces/{0}'.format(workspace_id),
            params=params,
            accept_json=True)

    def get_workspace(self, workspace_id, export=None):
        """
        Get information about a workspace.

        Get information about a workspace, optionally including all workspace content.

        :param workspace_id: The workspace ID.
        :param export: Whether to include all element content in the
            returned data. If export=`false`, the returned data includes
            only information about the element itself. If export=`true`,
            all content, including subelements, is included. The default
            value is `false`.
        """
        params = {'version': self.version, 'export': export}
        return self.request(
            method='GET',
            url='/v1/workspaces/{0}'.format(workspace_id),
            params=params,
            accept_json=True)

    def list_workspaces(self,
                        page_limit=None,
                        include_count=None,
                        sort=None,
                        cursor=None):
        """
        List workspaces.

        List the workspaces associated with a Conversation service instance.

        :param page_limit: The number of records to return in each page of
            results. The default page limit is 100.
        :param include_count: Whether to include information about the number
            of records returned.
        :param sort: Sorts the response according to the value of the
            specified property, in ascending or descending order.
        :param cursor: A token identifying the last value from the previous
            page of results.
        """
        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor
        }
        return self.request(
            method='GET',
            url='/v1/workspaces',
            params=params,
            accept_json=True)

    def update_workspace(self,
                         workspace_id,
                         name=None,
                         description=None,
                         language=None,
                         intents=None,
                         entities=None,
                         dialog_nodes=None,
                         counterexamples=None,
                         metadata=None):
        """
        Update workspace.

        Update an existing workspace with new or modified data.
        You must provide component objects defining the content
        of the updated workspace.

        :param workspace_id: The workspace ID.
        :param name: The name of the workspace.
        :param description: The description of the workspace.
        :param language: The language of the workspace.
        :param intents: An array of CreateIntent objects defining the
            intents for the workspace.
        :param entities: An array of CreateEntity objects defining the
            entities for the workspace.
        :param dialog_nodes: An array of CreateDialogNode objects defining
            the nodes in the workspace dialog.
        :param counterexamples: An array of CreateExample objects defining
            input examples that have been marked as irrelevant input.
        :param metadata: Any metadata related to the workspace.
        """
        params = {'version': self.version}
        data = {
            'name': name,
            'description': description,
            'language': language,
            'intents': intents,
            'entities': entities,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata
        }
        return self.request(
            method='POST',
            url='/v1/workspaces/{0}'.format(workspace_id),
            params=params,
            json=data,
            accept_json=True)
