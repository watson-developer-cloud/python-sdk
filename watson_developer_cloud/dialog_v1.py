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
The v1 Dialog service
(https://www.ibm.com/watson/developercloud/dialog.html)
"""
from __future__ import print_function
from .watson_developer_cloud_service import WatsonDeveloperCloudService


class DialogV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/dialog/api'
    dialog_json_format = 'application/wds+json'
    dialog_xml_format = 'application/wds+xml'
    dialog_binary_format = 'application/octet-stream'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'dialog', url, **kwargs)
        print(
            'WARNING: The Dialog service was deprecated, existing instances '
            'of the service will continue to function'
            'until August 9, 2017. See '
            'https://www.ibm.com/watson/developercloud/doc/conversation'
            '/migration.shtml')

    def get_dialogs(self):
        return self.request(method='GET', url='/v1/dialogs', accept_json=True)

    def get_dialog(self, dialog_id, accept='application/wds+json'):
        accept_json = accept == self.dialog_json_format
        headers = {'accept': accept}
        return self.request(method='GET',
                            url='/v1/dialogs/{0}'.format(dialog_id),
                            headers=headers,
                            accept_json=accept_json)

    def create_dialog(self, dialog_file, name):
        return self.request(method='POST', url='/v1/dialogs',
                            files={'file': dialog_file}, accept_json=True,
                            data={'name': name})

    def update_dialog(self, dialog_id, dialog_file):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        return self.request(method='PUT',
                            url='/v1/dialogs/{0}'.format(dialog_id),
                            files={'file': dialog_file},
                            accept_json=True)

    def get_content(self, dialog_id):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        return self.request(method='GET',
                            url='/v1/dialogs/{0}/content'.format(dialog_id),
                            accept_json=True)

    def update_content(self, dialog_id, content):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        return self.request(method='PUT',
                            url='/v1/dialogs/{0}/content'.format(dialog_id),
                            json=content,
                            accept_json=True)

    def conversation(self, dialog_id, dialog_input=None, client_id=None,
                     conversation_id=None):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        data = {'input': dialog_input, 'client_id': client_id,
                'conversation_id': conversation_id}
        return self.request(method='POST',
                            url='/v1/dialogs/{0}/conversation'.format(
                                dialog_id), data=data,
                            accept_json=True)

    @staticmethod
    def _format_date(date):
        if date:
            return date.strftime('%Y-%m-%d %H:%M:%S')

    def get_conversation(self, dialog_id, date_from, date_to):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        params = {'date_from': self._format_date(
            date_from), 'date_to': self._format_date(date_to)}
        return self.request(method='GET',
                            url='/v1/dialogs/{0}/conversation'.format(
                                dialog_id), params=params,
                            accept_json=True)

    def get_profile(self, dialog_id, client_id, name=None):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        client_id = self.unpack_id(client_id, 'client_id')
        params = {'client_id': client_id, 'name': name}
        return self.request(method='GET',
                            url='/v1/dialogs/{0}/profile'.format(dialog_id),
                            params=params,
                            accept_json=True)

    def update_profile(self, dialog_id, name_values, client_id=None):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        client_id = self.unpack_id(client_id, 'client_id')
        if isinstance(name_values, dict):
            name_values = list({'name': item[0], 'value': item[1]} for item in
                               name_values.items())
        params = {
            'client_id': client_id,
            'name_values': name_values
        }
        return self.request(method='PUT',
                            url='/v1/dialogs/{0}/profile'.format(dialog_id),
                            json=params,
                            accept_json=True)

    def delete_dialog(self, dialog_id):
        dialog_id = self.unpack_id(dialog_id, 'dialog_id')
        return self.request(method='DELETE',
                            url='/v1/dialogs/{0}'.format(dialog_id),
                            accept_json=True)
