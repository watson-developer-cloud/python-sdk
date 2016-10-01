# Copyright 2016 IBM All Rights Reserved.
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
The Conversation v1 service
(https://www.ibm.com/watson/developercloud/conversation.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class ConversationV1(WatsonDeveloperCloudService):
    """Client for the Conversation service"""

    default_url = 'https://gateway.watsonplatform.net/conversation/api'
    latest_version = '2016-09-20'

    def __init__(self, version, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'conversation', url, **kwargs)
        self.version = version

    def message(self, workspace_id, message_input=None, context=None, entities=None, intents=None, output=None,
                alternate_intents=False):
        """
        Retrieves information about a specific classifier.
        :param workspace_id: The workspace to use
        :param message_input: The input, usually containing a text field
        :param context: The optional context object
        :param entities: The optional entities
        :param intents: The optional intents
        :param alternate_intents: Whether to return more than one intent.
        :param output: The optional output object
        """

        params = {'version': self.version}
        data = {'input': message_input,
                'context': context,
                'entities': entities,
                'intents': intents,
                'alternate_intents': alternate_intents,
                'output': output}
        return self.request(method='POST', url='/v1/workspaces/{0}/message'.format(workspace_id), params=params,
                            json=data, accept_json=True)
