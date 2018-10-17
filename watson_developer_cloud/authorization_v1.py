# coding: utf-8
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
The v1 Authorization "service" that enables developers to
retrieve a temporary access token
"""

from watson_developer_cloud.watson_service import WatsonService

try:
    import urllib.parse as urlparse  # Python 3
except ImportError:
    import urlparse  # Python 2


class AuthorizationV1(WatsonService):
    """
    Generates tokens, which can be used client-side to avoid exposing the
    service credentials.
    Tokens are valid for 1 hour and are sent using the
    `X-Watson-Authorization-Token` header.
    """
    default_url = "https://stream.watsonplatform.net/authorization/api"

    def __init__(self, url=default_url,
                 username=None, password=None, use_vcap_services=True):
        WatsonService.__init__(
            self, 'authorization', url, username, password, use_vcap_services)

    def get_token(self, url):
        """
        Retrieves a temporary access token
        """
        # A hack to avoid url-encoding the url, since the authorization service
        # doesn't work with correctly encoded urls

        parsed_url = urlparse.urlsplit(url)
        parsed_url = parsed_url._replace(path='/authorization/api')
        self.url = urlparse.urlunsplit(parsed_url)

        response = self.request(method='GET', url='/v1/token?url=' + url)
        return response.result.text
