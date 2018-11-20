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
import json as json_import
import platform
import os
import requests
import sys
from requests.structures import CaseInsensitiveDict
import dateutil.parser as date_parser
from .iam_token_manager import IAMTokenManager
import warnings

try:
    from http.cookiejar import CookieJar  # Python 3
except ImportError:
    from cookielib import CookieJar  # Python 2
from .version import __version__

BEARER = 'Bearer'
X_WATSON_AUTHORIZATION_TOKEN = 'X-Watson-Authorization-Token'
AUTH_HEADER_DEPRECATION_MESSAGE = 'Authenticating with the X-Watson-Authorization-Token header is deprecated. The token continues to work with Cloud Foundry services, but is not supported for services that use Identity and Access Management (IAM) authentication.'
ICP_PREFIX = 'icp-'
APIKEY = 'apikey'
APIKEY_DEPRECATION_MESSAGE = 'Authenticating with apikey is deprecated. Move to using Identity and Access Management (IAM) authentication.'

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
    :param response httpResponse: response
    """
    def __init__(self, code, message, info=None, httpResponse=None):
        # Call the base class constructor with the parameters it needs
        super(WatsonApiException, self).__init__(message)
        self.message = message
        self.code = code
        self.info = info
        self.httpResponse = httpResponse
        self.transactionId = None
        self.globalTransactionId = None
        if httpResponse is not None:
            self.transactionId = httpResponse.headers.get('X-DP-Watson-Tran-ID')
            self.globalTransactionId = httpResponse.headers.get('X-Global-Transaction-ID')


    def __str__(self):
        msg = 'Error: ' + str(self.message) + ', Code: ' + str(self.code)
        if self.info is not None:
            msg += ' , Information: ' + str(self.info)
        if self.transactionId is not None:
            msg += ' , X-dp-watson-tran-id: ' + str(self.transactionId)
        if self.globalTransactionId is not None:
            msg += ' , X-global-transaction-id: ' + str(self.globalTransactionId)
        return  msg


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


def _cleanup_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value


def _cleanup_values(dictionary):
    if isinstance(dictionary, dict):
        return dict(
            [(k, _cleanup_value(v)) for k, v in dictionary.items()])
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

def get_error_message(response):
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
        elif 'errorMessage' in error_json:
            error_message = error_json['errorMessage']
        elif 'msg' in error_json:
            error_message = error_json['msg']
        elif 'statusInfo' in error_json:
            error_message = error_json['statusInfo']
        return error_message
    except:
        return response.text or error_message

class DetailedResponse(object):
    """
    Custom class for detailed response returned from Watson APIs.

    :param Response response: Either json response or http Response as requested.
    :param dict headers: A dict of response headers
    :param str status_code: HTTP response code
    """
    def __init__(self, response=None, headers=None, status_code=None):
        self.result = response
        self.headers = headers
        self.status_code = status_code

    def get_result(self):
        return self.result

    def get_headers(self):
        return self.headers

    def get_status_code(self):
        return self.status_code

    def _to_dict(self):
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result if isinstance(self.result, dict) else 'HTTP response'
        if hasattr(self, 'headers') and self.headers is not None:
            _dict['headers'] = self.headers
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        return _dict

    def __str__(self):
        return json_import.dumps(self._to_dict(), indent=4, default=lambda o: o.__dict__)

class WatsonService(object):
    def __init__(self, vcap_services_name, url, username=None, password=None,
                 use_vcap_services=True, api_key=None,
                 iam_apikey=None, iam_access_token=None, iam_url=None):
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
        self.http_config = {}
        self.detailed_response = True
        self.iam_apikey = None
        self.iam_access_token = None
        self.iam_url = None
        self.token_manager = None
        self.verify = None # Indicates whether to ignore verifying the SSL certification

        user_agent_string = 'watson-apis-python-sdk-' + __version__ # SDK version
        user_agent_string += ' ' + platform.system() # OS
        user_agent_string += ' ' + platform.release() # OS version
        user_agent_string += ' ' + platform.python_version() # Python version
        self.user_agent_header = {'user-agent': user_agent_string}

        if api_key is not None:
            self.set_api_key(api_key)
        elif username is not None and password is not None:
            if username is APIKEY and not password.startswith(ICP_PREFIX):
                self.set_token_manager(password, iam_access_token, iam_url)
            else:
                self.set_username_and_password(username, password)
        elif iam_access_token is not None or iam_apikey is not None:
            self.set_token_manager(iam_apikey, iam_access_token, iam_url)

        if use_vcap_services and not self.username and not self.api_key:
            self.vcap_service_credentials = load_from_vcap_services(
                vcap_services_name)
            if self.vcap_service_credentials is not None and isinstance(
                    self.vcap_service_credentials, dict):
                self.url = self.vcap_service_credentials['url']
                if 'username' in self.vcap_service_credentials:
                    self.username = self.vcap_service_credentials.get('username')
                if 'password' in self.vcap_service_credentials:
                    self.password = self.vcap_service_credentials.get('password')
                if 'apikey' in self.vcap_service_credentials:
                    self.set_iam_apikey(self.vcap_service_credentials.get('apikey'))
                if 'iam_apikey' in self.vcap_service_credentials:
                    self.set_iam_apikey(self.vcap_service_credentials.get('iam_apikey'))
                if 'iam_access_token' in self.vcap_service_credentials:
                    self.set_iam_access_token(self.vcap_service_credentials.get('iam_access_token'))

        if (self.username is None or self.password is None)\
                and self.api_key is None and self.token_manager is None:
            raise ValueError(
                'You must specify your IAM api key or username and password service '
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
        if api_key is not None:
            warnings.warn(APIKEY_DEPRECATION_MESSAGE)
        if api_key == 'YOUR API KEY':
            api_key = None
        if api_key is not None and api_key.startswith(ICP_PREFIX):
            self.set_username_and_password(APIKEY, api_key)
            return

        self.api_key = api_key

        # This would be called only for Visual recognition
        if self.url is self.default_url:
            self.set_url('https://gateway-a.watsonplatform.net/visual-recognition/api')
        self.jar = CookieJar()

    def set_token_manager(self, iam_apikey=None, iam_access_token=None, iam_url=None):
        if iam_apikey == 'YOUR IAM API KEY':
            return

        self.iam_apikey = iam_apikey
        self.iam_access_token = iam_access_token
        self.iam_url = iam_url
        self.token_manager = IAMTokenManager(iam_apikey, iam_access_token, iam_url)
        self.jar = CookieJar()

    def set_iam_access_token(self, iam_access_token):
        if self.token_manager:
            self.token_manager.set_access_token(iam_access_token)
        else:
            self.token_manager = IAMTokenManager(iam_access_token=iam_access_token)
        self.iam_access_token = iam_access_token
        self.jar = CookieJar()

    def set_iam_apikey(self, iam_apikey):
        if self.token_manager:
            self.token_manager.set_iam_apikey(iam_apikey)
        else:
            self.token_manager = IAMTokenManager(iam_apikey=iam_apikey)
        self.iam_apikey = iam_apikey
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

    def set_http_config(self, http_config):
        """
        Sets the http client config like timeout, proxies, etc.
        """
        if isinstance(http_config, dict):
            self.http_config = http_config
        else:
            raise TypeError("http_config parameter must be a dictionary")

    def disable_SSL_verification(self):
        self.verify = False

    def set_detailed_response(self, detailed_response):
        self.detailed_response = detailed_response

    # Could make this compute the label_id based on the variable name of the
    # dictionary passed in (using **kwargs), but
    # this might be confusing to understand.
    @staticmethod
    def unpack_id(dictionary, label_id):
        if isinstance(dictionary, dict) and label_id in dictionary:
            return dictionary[label_id]
        return dictionary

    @staticmethod
    def _convert_model(val, classname=None):
        if classname is not None and not hasattr(val, "_from_dict"):
            if isinstance(val, str):
                val = json_import.loads(val)
            val = classname._from_dict(dict(val))
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


    def request(self, method, url, accept_json=False, headers=None,
                params=None, json=None, data=None, files=None, **kwargs):
        full_url = self.url + url
        input_headers = _remove_null_values(headers) if headers else {}
        input_headers = _cleanup_values(input_headers)

        headers = CaseInsensitiveDict(self.user_agent_header)
        if self.default_headers is not None:
            headers.update(self.default_headers)
        if accept_json:
            headers['accept'] = 'application/json'
        headers.update(input_headers)

        if X_WATSON_AUTHORIZATION_TOKEN in headers:
            warnings.warn(AUTH_HEADER_DEPRECATION_MESSAGE)

        # Remove keys with None values
        params = _remove_null_values(params)
        params = _cleanup_values(params)
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
        if self.token_manager:
            access_token = self.token_manager.get_token()
            headers['Authorization'] = '{0} {1}'.format(BEARER, access_token)
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

        # Use a one minute timeout when our caller doesn't give a timeout.
        # http://docs.python-requests.org/en/master/user/quickstart/#timeouts
        kwargs = dict({"timeout": 60}, **kwargs)
        kwargs = dict(kwargs, **self.http_config)

        if self.verify is not None:
            kwargs['verify'] = self.verify

        response = requests.request(method=method, url=full_url,
                                    cookies=self.jar, auth=auth,
                                    headers=headers,
                                    params=params, data=data, files=files,
                                    **kwargs)

        if 200 <= response.status_code <= 299:
            if response.status_code == 204 or method == 'HEAD':
                # There is no body content for a HEAD request or a 204 response
                return DetailedResponse(None, response.headers, response.status_code) if self.detailed_response else None
            if accept_json:
                try:
                    response_json = response.json()
                except:
                    # deserialization fails because there is no text
                    return DetailedResponse(None, response.headers, response.status_code) if self.detailed_response else None
                if 'status' in response_json and response_json['status'] \
                        == 'ERROR':
                    status_code = 400
                    error_message = 'Unknown error'

                    if 'statusInfo' in response_json:
                        error_message = response_json['statusInfo']
                    if error_message == 'invalid-api-key':
                        status_code = 401
                    raise WatsonApiException(status_code, error_message, httpResponse=response)
                return DetailedResponse(response_json, response.headers, response.status_code) if self.detailed_response else response_json
            return DetailedResponse(response, response.headers, response.status_code) if self.detailed_response else response
        else:
            if response.status_code == 401:
                error_message = 'Unauthorized: Access is denied due to ' \
                                'invalid credentials '
            else:
                error_message = get_error_message(response)
            error_info = self._get_error_info(response)
            raise WatsonApiException(response.status_code, error_message,
                                     info=error_info, httpResponse=response)
