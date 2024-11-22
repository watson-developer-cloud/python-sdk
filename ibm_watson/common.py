# coding: utf-8

# Copyright 2019, 2024 IBM All Rights Reserved.
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

import platform
import json
from .version import __version__
from typing import Iterator

SDK_ANALYTICS_HEADER = 'X-IBMCloud-SDK-Analytics'
USER_AGENT_HEADER = 'User-Agent'
SDK_NAME = 'watson-apis-python-sdk'


def get_system_info():
    return '{0} {1} {2}'.format(
        platform.system(),  # OS
        platform.release(),  # OS version
        platform.python_version())  # Python version


def get_user_agent():
    return user_agent


def get_sdk_analytics(service_name, service_version, operation_id):
    return 'service_name={0};service_version={1};operation_id={2}'.format(
        service_name, service_version, operation_id)


user_agent = '{0}-{1} {2}'.format(SDK_NAME, __version__, get_system_info())


def get_sdk_headers(service_name, service_version, operation_id):
    headers = {}
    headers[SDK_ANALYTICS_HEADER] = get_sdk_analytics(service_name,
                                                      service_version,
                                                      operation_id)
    headers[USER_AGENT_HEADER] = get_user_agent()
    return headers


def parse_sse_stream_data(response) -> Iterator[dict]:
    event_message = None  # Can be used in the future to return the event message to the user
    data_json = None

    for chunk in response.iter_lines():
        decoded_chunk = chunk.decode("utf-8")

        if decoded_chunk.find("event", 0, len("event")) == 0:
            event_message = decoded_chunk[len("event") + 2:]
        elif decoded_chunk.find("data", 0, len("data")) == 0:
            data_json_str = decoded_chunk[len("data") + 2:]
            data_json = json.loads(data_json_str)

        if event_message and data_json is not None:
            yield data_json
            event_message = None
            data_json = None
