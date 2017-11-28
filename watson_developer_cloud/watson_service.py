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
import json as json_import
import platform
import os
import requests
import sys
from requests.structures import CaseInsensitiveDict
import dateutil.parser as date_parser

try:
    from http.cookiejar import CookieJar  # Python 3
except ImportError:
    from cookielib import CookieJar  # Python 2
from .version import __version__


# Uncomment this to enable http debugging
# try:
#    import http.client as http_client
# except ImportError:
#    # Python 2
#    import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1


def load_from_vcap_services(service_name):
    vcap_services = os.getenv("VCAP_SERVICES")
    if vcap_services is not None:
        services = json_import.loads(vcap_services)
        if service_name in services:
            return services[service_name][0]["credentials"]
    else:
        return None


class WatsonException(Exception):
    """
    Custom exception class for Watson Services.
    """
    pass


class WatsonApiException(WatsonException):
    """
    Custom exception class for errors returned from Watson APIs.

    :param int code: The HTTP status code returned.
    :param str message: A message describing the error.
    :param dict info: A dictionary of additional information about the error.
    """
    def __init__(self, code, message, info=None):
        # Call the base class constructor with the parameters it needs
        super(WatsonApiException, self).__init__(message)
        self.message = message
        self.code = code
        self.info = info

    def __str__(self):
        return 'Error: ' + self.message + ', Code: ' + str(self.code)


class WatsonInvalidArgument(WatsonException):
    pass

def datetime_to_string(datetime):
    """
    Serializes a datetime to a string.
    :param datetime: datetime value
    :return: string. containing iso8601 format date string
    """
    return datetime.isoformat().replace('+00:00', 'Z')


def string_to_datetime(string):
    """
    Deserializes string to datetime.
    :param string: string containing datetime in iso8601 format
    :return: datetime.
    """
    return date_parser.parse(string)


def _cleanup_param_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def _cleanup_param_values(dictionary):
    if isinstance(dictionary, dict):
        return dict(
            [(k, _cleanup_param_value(v)) for k, v in dictionary.items()])
    return dictionary


def _remove_null_values(dictionary):
    if isinstance(dictionary, dict):
        return dict([(k, v) for k, v in dictionary.items() if v is not None])
    return dictionary


def _convert_boolean_value(value):
    if isinstance(value, bool):
        return 1 if value else 0
    return value


def _convert_boolean_values(dictionary):
    if isinstance(dictionary, dict):
        return dict(
            [(k, _convert_boolean_value(v)) for k, v in dictionary.items()])
    return dictionary


class WatsonService(object):
    def __init__(self, vcap_services_name, url, username=None, password=None,
                 use_vcap_services=True, api_key=None,
                 x_watson_learning_opt_out=False):
        """
        Loads credentials from the VCAP_SERVICES environment variable if
        available, preferring credentials explicitly
        set in the request.
        If VCAP_SERVICES is not found (or use_vcap_services is set to False),
        username and password credentials must
        be specified.
        """

        self.url = url
        self.jar = None
        self.api_key = None
        self.username = None
        self.password = None
        self.default_headers = None

        user_agent_string = 'watson-apis-python-sdk-' + __version__ # SDK version
        user_agent_string += ' ' + platform.system() # OS
        user_agent_string += ' ' + platform.release() # OS version
        user_agent_string += ' ' + platform.python_version() # Python version
        self.user_agent_header = {'user-agent': user_agent_string}

        if x_watson_learning_opt_out:
            self.default_headers = {'x-watson-learning-opt-out': 'true'}

        if api_key is not None:
            if username is not None or password is not None:
                raise ValueError(
                    'Cannot set api_key and username and password together')
            self.set_api_key(api_key)
        else:
            self.set_username_and_password(username, password)

        if use_vcap_services and not self.username and not self.api_key:
            self.vcap_service_credentials = load_from_vcap_services(
                vcap_services_name)
            if self.vcap_service_credentials is not None and isinstance(
                    self.vcap_service_credentials, dict):
                self.url = self.vcap_service_credentials['url']
                if 'username' in self.vcap_service_credentials:
                    self.username = self.vcap_service_credentials['username']
                if 'password' in self.vcap_service_credentials:
                    self.password = self.vcap_service_credentials['password']
                if 'apikey' in self.vcap_service_credentials:
                    self.api_key = self.vcap_service_credentials['apikey']
                if 'api_key' in self.vcap_service_credentials:
                    self.api_key = self.vcap_service_credentials['api_key']

        if (self.username is None or self.password is None)\
                and self.api_key is None:
            raise ValueError(
                'You must specify your username and password service '
                'credentials (Note: these are different from your Bluemix id)')

    def set_username_and_password(self, username=None, password=None):
        if username == 'YOUR SERVICE USERNAME':
            username = None
        if password == 'YOUR SERVICE PASSWORD':
            password = None

        self.username = username
        self.password = password
        self.jar = CookieJar()

    def set_api_key(self, api_key):
        if api_key == 'YOUR API KEY':
            api_key = None

        self.api_key = api_key
        self.jar = CookieJar()

    def set_url(self, url):
        self.url = url

    def set_default_headers(self, headers):
        """
        Set http headers to be sent in every request.
        :param headers: A dictionary of header names and values
        """
        if isinstance(headers, dict):
            self.default_headers = headers
        else:
            raise TypeError("headers parameter must be a dictionary")

    # Could make this compute the label_id based on the variable name of the
    # dictionary passed in (using **kwargs), but
    # this might be confusing to understand.
    @staticmethod
    def unpack_id(dictionary, label_id):
        if isinstance(dictionary, dict) and label_id in dictionary:
            return dictionary[label_id]
        return dictionary

    @staticmethod
    def _convert_model(val):
        if hasattr(val, "_to_dict"):
            return val._to_dict()
        return val

    @staticmethod
    def _convert_list(val):
        if isinstance(val, list):
            return ",".join(val)
        return val

    @staticmethod
    def _encode_path_vars(*args):
        return (requests.utils.quote(x, safe='') for x in args)

    @staticmethod
    def _get_error_message(response):
        """
        Gets the error message from a JSON response.
        :return: the error message
        :rtype: string
        """
        error_message = 'Unknown error'
        try:
            error_json = response.json()
            if 'error' in error_json:
                if isinstance(error_json['error'], dict) and 'description' in \
                        error_json['error']:
                    error_message = error_json['error']['description']
                else:
                    error_message = error_json['error']
            elif 'error_message' in error_json:
                error_message = error_json['error_message']
            elif 'msg' in error_json:
                error_message = error_json['msg']
            elif 'statusInfo' in error_json:
                error_message = error_json['statusInfo']
            return error_message
        except:
            return response.text or error_message


    @staticmethod
    def _get_error_info(response):
        """
        Gets the error info (if any) from a JSON response.
        :return: A `dict` containing additional information about the error.
        :rtype: dict
        """
        info_keys = ['code_description', 'description', 'errors', 'help',
                     'sub_code', 'warnings']
        error_info = {}
        try:
            error_json = response.json()
            error_info = {k:v for k, v in error_json.items() if k in info_keys}
        except:
            pass
        return error_info if any(error_info) else None


    def _alchemy_html_request(self, method_name=None, url=None, html=None,
                              text=None, params=None, method='POST',
                              method_url=None):
        if params is None:
            params = {}
        params['outputMode'] = 'json'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        params = _convert_boolean_values(params)
        url_encoded_params = {}

        if method.upper() == 'POST':
            url_encoded_params = params
            params = {}

        url_encoded_params['html'] = html
        url_encoded_params['text'] = text

        if method_url is None:
            if url:
                params['url'] = url
                method_url = '/url/URL' + method_name
            elif html:
                method_url = '/html/HTML' + method_name
            elif text:
                method_url = '/text/Text' + method_name
            else:
                raise WatsonInvalidArgument(
                    'url, html or text must be specified')

        return self.request(method=method, url=method_url, params=params,
                            data=url_encoded_params, headers=headers,
                            accept_json=True)

    def _alchemy_image_request(self, method_name, image_file=None,
                               image_url=None, params=None):
        if params is None:
            params = {}
        params['outputMode'] = 'json'
        params = _convert_boolean_values(params)
        headers = {}
        image_contents = None

        if image_file:
            params['imagePostMode'] = 'raw'
            image_contents = image_file.read()
            # headers['content-length'] = sys.getsizeof(image_contents)
            url = '/image/Image' + method_name
        elif image_url:
            params['imagePostMode'] = 'not-raw'
            params['url'] = image_url
            url = '/url/URL' + method_name
        else:
            raise WatsonInvalidArgument(
                'image_file or image_url must be specified')

        return self.request(method='POST', url=url, params=params,
                            data=image_contents, headers=headers,
                            accept_json=True)

    def request(self, method, url, accept_json=False, headers=None,
                params=None, json=None, data=None, files=None, **kwargs):
        full_url = self.url + url

        input_headers = _remove_null_values(headers) if headers else {}

        headers = CaseInsensitiveDict(self.user_agent_header)
        if self.default_headers is not None:
            headers.update(self.default_headers)
        if accept_json:
            headers['accept'] = 'application/json'
        headers.update(input_headers)

        # Remove keys with None values
        params = _remove_null_values(params)
        params = _cleanup_param_values(params)
        json = _remove_null_values(json)
        data = _remove_null_values(data)
        files = _remove_null_values(files)

        if sys.version_info >= (3, 0) and isinstance(data, str):
            data = data.encode('utf-8')

        # Support versions of requests older than 2.4.2 without the json input
        if not data and json is not None:
            data = json_import.dumps(json)
            headers.update({'content-type': 'application/json'})

        auth = None
        if self.username and self.password:
            auth = (self.username, self.password)
        if self.api_key is not None:
            if params is None:
                params = {}
            if full_url.startswith(
                    'https://gateway-a.watsonplatform.net/calls'):
                params['apikey'] = self.api_key
            else:
                params['api_key'] = self.api_key

        response = requests.request(method=method, url=full_url,
                                    cookies=self.jar, auth=auth,
                                    headers=headers,
                                    params=params, data=data, files=files,
                                    **kwargs)

        if 200 <= response.status_code <= 299:
            if response.status_code == 204:
                return None
            if accept_json:
                response_json = response.json()
                if 'status' in response_json and response_json['status'] \
                        == 'ERROR':
                    status_code = 400
                    error_message = 'Unknown error'

                    if 'statusInfo' in response_json:
                        error_message = response_json['statusInfo']
                    if error_message == 'invalid-api-key':
                        status_code = 401
                    raise WatsonApiException(status_code, error_message)
                return response_json
            return response
        else:
            if response.status_code == 401:
                error_message = 'Unauthorized: Access is denied due to ' \
                                'invalid credentials '
            else:
                error_message = self._get_error_message(response)
            error_info = self._get_error_info(response)
            raise WatsonApiException(response.status_code, error_message,
                                     error_info)
