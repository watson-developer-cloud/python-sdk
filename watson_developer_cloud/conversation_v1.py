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
The IBM Watson&trade; Conversation service combines machine learning, natural language understanding, and integrated dialog tools to create conversation flows between your apps and your users.
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService

class ConversationV1(WatsonDeveloperCloudService):
    """Client for the Conversation service."""

    default_url = 'https://gateway.watsonplatform.net/conversation/api'
    latest_version = '2017-02-03'

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
        :param workspace_id: The workspace ID.
        :param text: The text of a user input example.
        """
        params = {'version': self.version}
        data = {}
        data['text'] = text
        return self.request(method='POST',
                            url='/v1/workspaces/{0}/counterexamples'.format(workspace_id),
                            params=params,
                            json=data,
                            accept_json=True)

    def delete_counterexample(self, workspace_id, text):
        """
        Delete counterexample.
        :param workspace_id: The workspace ID.
        :param text: The text of a user input counterexample (for example, `What are you wearing?`).
        """
        params = {'version': self.version}
        return self.request(method='DELETE',
                            url='/v1/workspaces/{0}/counterexamples/{1}'.format(workspace_id, text),
                            params=params,
                            accept_json=True)

    def get_counterexample(self, workspace_id, text):
        """
        Get counterexample.
        :param workspace_id: The workspace ID.
        :param text: The text of a user input counterexample (for example, `What are you wearing?`).
        """
        params = {'version': self.version}
        return self.request(method='GET',
                            url='/v1/workspaces/{0}/counterexamples/{1}'.format(workspace_id, text),
                            params=params,
                            accept_json=True)

    def list_counterexamples(self, workspace_id, page_limit=None, include_count=None, sort=None, cursor=None):
        """
        List counterexamples.
        :param workspace_id: The workspace ID.
        :param page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param include_count: Whether to include information about the number of records returned.
        :param sort: The sort order that determines the behavior of the pagination cursor.
        :param cursor: A token identifying the last value from the previous page of results.
        """
        params = {'version': self.version}
        params['page_limit'] = page_limit
        params['include_count'] = include_count
        params['sort'] = sort
        params['cursor'] = cursor
        return self.request(method='GET',
                            url='/v1/workspaces/{0}/counterexamples'.format(workspace_id),
                            params=params,
                            accept_json=True)

    def update_counterexample(self, workspace_id, text, body):
        """
        Update counterexample.
        :param workspace_id: The workspace ID.
        :param text: The text of a user input counterexample (for example, `What are you wearing?`).
        :param body: An UpdateExample object defining the new text for the counterexample.
        """
        params = {'version': self.version}
        data = {}
        return self.request(method='POST',
                            url='/v1/workspaces/{0}/counterexamples/{1}'.format(workspace_id, text),
                            params=params,
                            json=data,
                            accept_json=True)

    #########################
    # examples
    #########################

    def create_example(self, workspace_id, intent, text):
        """
        Create user input example.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of a user input example.
        """
        params = {'version': self.version}
        data = {}
        data['text'] = text
        return self.request(method='POST',
                            url='/v1/workspaces/{0}/intents/{1}/examples'.format(workspace_id, intent),
                            params=params,
                            json=data,
                            accept_json=True)

    def delete_example(self, workspace_id, intent, text):
        """
        Delete user input example.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of the user input example.
        """
        params = {'version': self.version}
        return self.request(method='DELETE',
                            url='/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(workspace_id, intent, text),
                            params=params,
                            accept_json=True)

    def get_example(self, workspace_id, intent, text):
        """
        Get user input example.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of the user input example.
        """
        params = {'version': self.version}
        return self.request(method='GET',
                            url='/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(workspace_id, intent, text),
                            params=params,
                            accept_json=True)

    def list_examples(self, workspace_id, intent, page_limit=None, include_count=None, sort=None, cursor=None):
        """
        List user input examples.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param include_count: Whether to include information about the number of records returned.
        :param sort: The sort order that determines the behavior of the pagination cursor.
        :param cursor: A token identifying the last value from the previous page of results.
        """
        params = {'version': self.version}
        params['page_limit'] = page_limit
        params['include_count'] = include_count
        params['sort'] = sort
        params['cursor'] = cursor
        return self.request(method='GET',
                            url='/v1/workspaces/{0}/intents/{1}/examples'.format(workspace_id, intent),
                            params=params,
                            accept_json=True)

    def update_example(self, workspace_id, intent, text, body):
        """
        Update user input example.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param text: The text of the user input example.
        :param body: An UpdateExample object defining the new text for the user input example.
        """
        params = {'version': self.version}
        data = {}
        return self.request(method='POST',
                            url='/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(workspace_id, intent, text),
                            params=params,
                            json=data,
                            accept_json=True)

    #########################
    # intents
    #########################

    def create_intent(self, workspace_id, intent, description=None, examples=None):
        """
        Create intent.
        :param workspace_id: The workspace ID.
        :param intent: The name of the intent.
        :param description: The description of the intent.
        :param examples: An array of user input examples.
        """
        params = {'version': self.version}
        data = {}
        data['intent'] = intent
        data['description'] = description
        data['examples'] = examples
        return self.request(method='POST',
                            url='/v1/workspaces/{0}/intents'.format(workspace_id),
                            params=params,
                            json=data,
                            accept_json=True)

    def delete_intent(self, workspace_id, intent):
        """
        Delete intent.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        """
        params = {'version': self.version}
        return self.request(method='DELETE',
                            url='/v1/workspaces/{0}/intents/{1}'.format(workspace_id, intent),
                            params=params,
                            accept_json=True)

    def get_intent(self, workspace_id, intent, export=None):
        """
        Get intent.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        """
        params = {'version': self.version}
        params['export'] = export
        return self.request(method='GET',
                            url='/v1/workspaces/{0}/intents/{1}'.format(workspace_id, intent),
                            params=params,
                            accept_json=True)

    def list_intents(self, workspace_id, export=None, page_limit=None, include_count=None, sort=None, cursor=None):
        """
        List intents.
        :param workspace_id: The workspace ID.
        :param export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        :param page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param include_count: Whether to include information about the number of records returned.
        :param sort: The sort order that determines the behavior of the pagination cursor.
        :param cursor: A token identifying the last value from the previous page of results.
        """
        params = {'version': self.version}
        params['export'] = export
        params['page_limit'] = page_limit
        params['include_count'] = include_count
        params['sort'] = sort
        params['cursor'] = cursor
        return self.request(method='GET',
                            url='/v1/workspaces/{0}/intents'.format(workspace_id),
                            params=params,
                            accept_json=True)

    def update_intent(self, workspace_id, intent, body):
        """
        Update intent.
        :param workspace_id: The workspace ID.
        :param intent: The intent name (for example, `pizza_order`).
        :param body: An UpdateIntent object defining the updated content of the intent.
        """
        params = {'version': self.version}
        data = {}
        return self.request(method='POST',
                            url='/v1/workspaces/{0}/intents/{1}'.format(workspace_id, intent),
                            params=params,
                            json=data,
                            accept_json=True)

    #########################
    # message
    #########################

    def message(self, workspace_id, message_input, alternate_intents=None, context=None, entities=None, intents=None, output=None):
        """
        Get a response to a user's input.
        :param workspace_id: Unique identifier of the workspace.
        :param message_input: An input object that includes the input text.
        :param alternate_intents: Whether to return more than one intent. Set to `true` to return all matching intents.
        :param context: State information for the conversation. Include the context object from the previous response when you send multiple requests for the same conversation.
        :param entities: Include the entities from the previous response when they do not need to change and to prevent Watson from trying to identify them.
        :param intents: An array of name-confidence pairs for the user input. Include the intents from the previous response when they do not need to change and to prevent Watson from trying to identify them.
        :param output: System output. Include the output from the request when you have several requests within the same Dialog turn to pass back in the intermediate information.
        """
        params = {'version': self.version}
        data = {}
        data['message_input'] = message_input
        data['alternate_intents'] = alternate_intents
        data['context'] = context
        data['entities'] = entities
        data['intents'] = intents
        data['output'] = output
        return self.request(method='POST',
                            url='/v1/workspaces/{0}/message'.format(workspace_id),
                            params=params,
                            json=data,
                            accept_json=True)

    #########################
    # workspaces
    #########################

    def create_workspace(self, name=None, description=None, language=None, metadata=None, intents=None, entities=None, dialog_nodes=None, counterexamples=None):
        """
        Create workspace.
        :param name: The name of the workspace.
        :param description: The description of the workspace.
        :param language: The language of the workspace.
        :param metadata: Any metadata that is required by the workspace.
        :param intents: An array of CreateIntent objects defining the intents for the workspace.
        :param entities: An array of CreateEntity objects defining the entities for the workspace.
        :param dialog_nodes: An array of CreateDialogNode objects defining the nodes in the workspace dialog.
        :param counterexamples: An array of CreateExample objects defining input examples that have been marked as irrelevant input.
        """
        params = {'version': self.version}
        data = {}
        data['name'] = name
        data['description'] = description
        data['language'] = language
        data['metadata'] = metadata
        data['intents'] = intents
        data['entities'] = entities
        data['dialog_nodes'] = dialog_nodes
        data['counterexamples'] = counterexamples
        return self.request(method='POST',
                            url='/v1/workspaces',
                            params=params,
                            json=data,
                            accept_json=True)

    def delete_workspace(self, workspace_id):
        """
        Delete workspace.
        :param workspace_id: The workspace ID.
        """
        params = {'version': self.version}
        return self.request(method='DELETE',
                            url='/v1/workspaces/{0}'.format(workspace_id),
                            params=params,
                            accept_json=True)

    def get_workspace(self, workspace_id, export=None):
        """
        Get information about a workspace.
        :param workspace_id: The workspace ID.
        :param export: Whether to include all element content in the returned data. If export=`false`, the returned data includes only information about the element itself. If export=`true`, all content, including subelements, is included. The default value is `false`.
        """
        params = {'version': self.version}
        params['export'] = export
        return self.request(method='GET',
                            url='/v1/workspaces/{0}'.format(workspace_id),
                            params=params,
                            accept_json=True)

    def list_workspaces(self, page_limit=None, include_count=None, sort=None, cursor=None):
        """
        List workspaces.
        :param page_limit: The number of records to return in each page of results. The default page limit is 100.
        :param include_count: Whether to include information about the number of records returned.
        :param sort: The sort order that determines the behavior of the pagination cursor.
        :param cursor: A token identifying the last value from the previous page of results.
        """
        params = {'version': self.version}
        params['page_limit'] = page_limit
        params['include_count'] = include_count
        params['sort'] = sort
        params['cursor'] = cursor
        return self.request(method='GET',
                            url='/v1/workspaces',
                            params=params,
                            accept_json=True)

    def update_workspace(self, workspace_id, name=None, description=None, language=None, metadata=None, intents=None, entities=None, dialog_nodes=None, counterexamples=None):
        """
        Update workspace.
        :param workspace_id: The workspace ID.
        :param name: The name of the workspace.
        :param description: The description of the workspace.
        :param language: The language of the workspace.
        :param metadata: Any metadata that is required by the workspace.
        :param intents: An array of CreateIntent objects defining the intents for the workspace.
        :param entities: An array of CreateEntity objects defining the entities for the workspace.
        :param dialog_nodes: An array of CreateDialogNode objects defining the nodes in the workspace dialog.
        :param counterexamples: An array of CreateExample objects defining input examples that have been marked as irrelevant input.
        """
        params = {'version': self.version}
        data = {}
        data['name'] = name
        data['description'] = description
        data['language'] = language
        data['metadata'] = metadata
        data['intents'] = intents
        data['entities'] = entities
        data['dialog_nodes'] = dialog_nodes
        data['counterexamples'] = counterexamples
        return self.request(method='POST',
                            url='/v1/workspaces/{0}'.format(workspace_id),
                            params=params,
                            json=data,
                            accept_json=True)

