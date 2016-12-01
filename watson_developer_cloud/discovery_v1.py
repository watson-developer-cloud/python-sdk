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
"""
The v1 Discovery Service
(http://www.ibm.com/watson/developercloud/doc/discovery/)
"""
import mimetypes
from urllib.parse import urljoin

from .watson_developer_cloud_service import WatsonDeveloperCloudService

default_url = 'https://gateway.watsonplatform.net/discovery-experimental/api'
latest_version = '2016-11-07'

class DiscoveryV1(WatsonDeveloperCloudService):
    """Client for Discovery service"""

    def __init__(self, version, url=default_url, username=None, password=None, use_vcap_services=True):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        :param version: specifies the specific version-date of the service to use
        """

        WatsonDeveloperCloudService.__init__(
            self, 'discovery', url, username, password, use_vcap_services)
        self.version = version

    def get_environments(self):
        """
        Retrieves information about the environments associated with the user
        """
        return self.request(method='GET', url='/v1/environments', params={"version": self.version}, accept_json=True)
        
    
    def create_environment(self):
        pass

    def delete_environment(self,environment_id):
        pass

    def get_collections(self, environment_id):
        """
        Retrieves information about the collections within a given environment
        :param environment_id: this is the guid of a valid environment
        :return: json results of the collections in an environment
        """
        url_string = urljoin('/v1/environments/', environment_id)
        return self.request(method='GET', url=url_string, params={"version": self.version}, accept_json=True)

    def get_collection(self, environment_id, collection_id):
        """
        Retrieves information about a sepcific collection in an environment
        :param environment_id: the guid of a valid environment
        :param collection_id: the guid of a valid collection
        :return: json results of the collection information
        """
        return self.request(method='GET',
                            url='/v1/environments/{0}/collections/{1}'.format(environment_id, collection_id),
                            params={"version": latest_version}, accept_json=True)

    def query(self, environment_id, collection_id, query_options):
        """
         Performs a query and returns the results.
        :param environment_id: the guid of a valid environment
        :param collection_id: the guid of a valid collection
        :param query_options: this is a hash of query params and their values
        :return:
        """
        query_options["version"] = self.version
        return self.request(method='GET',
                            url='/v1/environments/{0}/collections/{1}/query'.format(environment_id, collection_id),
                            params=query_options, accept_json=True)
