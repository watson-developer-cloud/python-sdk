# Copyright 2015 IBM All Rights Reserved.
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
import json as json_import
import os
import requests
try:
    from http.cookiejar import CookieJar  # Python 3
except ImportError:
    from cookielib import CookieJar  # Python 2


def load_from_vcap_services(service_name):
    vcap_services = os.getenv("VCAP_SERVICES")
    if vcap_services is not None:
        services = json_import.loads(vcap_services)
        if service_name in services:
            return services[service_name][0]["credentials"]
    else:
        return None


class WatsonException(Exception):
    """Generic exception class."""
    pass


class WatsonInvalidArgument(Exception):
    """A parameter to a function or methods was invalid"""
    pass


def _remove_null_values(dictionary):
    if isinstance(dictionary, dict):
        return {k: v for k, v in dictionary.items() if v is not None}
    return dictionary


class WatsonDeveloperCloudService(object):
    def __init__(self, vcap_services_name, url, username=None, password=None, use_vcap_services=True):
        """
        Loads credentials from the VCAP_SERVICES environment variable if available, preferring credentials explicitly
        set in the request.
        If VCAP_SERVICES is not found (or use_vcap_services is set to False), username and password credentials must
        be specified.
        """

        self.url = url
        self.jar = None
        self.set_username_and_password(username, password)

        if use_vcap_services and not self.username:
            self.vcap_service_credentials = load_from_vcap_services(vcap_services_name)
            if self.vcap_service_credentials is not None:
                self.url = self.vcap_service_credentials['url']
                self.username = self.vcap_service_credentials['username']
                self.password = self.vcap_service_credentials['password']

        if self.username is None or self.password is None:
            raise WatsonException('You must specific your username and password service credentials ' +
                                  '(Note: these are different from your Bluemix id)')

    def set_username_and_password(self, username=None, password=None):
        if username == 'YOUR SERVICE USERNAME':
            username = None

        if password == 'YOUR SERVICE PASSWORD':
            password = None

        self.username = username
        self.password = password
        self.jar = CookieJar()

    def set_url(self, url):
        self.url = url

    # Could make this compute the label_id based on the variable name of the dictionary passed in (using **kwargs), but
    # this might be confusing to understand.
    @staticmethod
    def unpack_id(dictionary, label_id):
        if isinstance(dictionary, dict) and label_id in dictionary:
            return dictionary[label_id]
        return dictionary

    def _get_error_message(self, response):
        '''
        Gets the error message from a JSON response.
        {
            code: 400
            error: 'Bad request'
        }
        '''
        error_message = 'Unknown error'
        try:
            error_json = response.json()
            if 'error' in error_json:
                error_message = error_json['error']
            if 'error_message' in error_json:
                error_message = error_json['error_message']
        except:
            pass
        return error_message

    def request(self, method, url, accept_json=False, headers=None, params=None, json=None, data=None, **kwargs):
        full_url = self.url + url

        if accept_json:
            json_headers = {'accept': 'application/json'}
            if headers:
                json_headers.update(headers)
            headers = json_headers

        # Remove keys with None values
        headers = _remove_null_values(headers)
        params = _remove_null_values(params)
        json = _remove_null_values(json)
        data = _remove_null_values(data)

        response = requests.request(method=method, url=full_url, cookies=self.jar, auth=(self.username, self.password),
                                    headers=headers, params=params, json=json, data=data, **kwargs)

        if 200 <= response.status_code <= 299:
            if accept_json:
                return response.json()
            return response
        else:
            if response.status_code == 401:
                error_message = 'Unauthorized: Access is denied due to invalid credentials'
            else:
                error_message = self._get_error_message(response)

            raise WatsonException('Error: ' + error_message + ', Code: ' + str(response.status_code))
