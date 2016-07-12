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

    default_url = 'https://gateway.watsonplatform.net/conversation-experimental/api'
    latest_version = '2016-07-11'

    def __init__(self, version, url=default_url, username=None, password=None, use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'conversation', url, username, password, use_vcap_services)
        self.version = version

    def message(self, workspace_id, message_input, context=None):
        """
        Retrieves information about a specific classifier.
        :param workspace_id: The workspace to use
        :param message_input: The input, usually containing a text field
        :param context: The optional context object
        """

        params = {'version': self.version}
        data = {'input': message_input,
                'context': context}
        return self.request(method='POST', url='/v1/workspaces/{0}/message'.format(workspace_id), params=params,
                            json=data, accept_json=True)
