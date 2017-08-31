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
The v1 Discovery Service
(http://www.ibm.com/watson/developercloud/doc/discovery/)
"""
import json
import mimetypes

from .watson_developer_cloud_service import WatsonDeveloperCloudService

default_url = 'https://gateway.watsonplatform.net/discovery/api'
latest_version = '2016-11-07'


class DiscoveryV1(WatsonDeveloperCloudService):
    """Client for Discovery service"""

    def __init__(self, version, url=default_url, username=None, password=None,
                 use_vcap_services=True):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        :param version: specifies the specific version-date of the service to
        use
        """

        WatsonDeveloperCloudService.__init__(
            self, 'discovery', url, username, password, use_vcap_services)
        self.version = version

    def get_environments(self):
        """
        Retrieves information about the environments associated with the user
        """
        return self.request(method='GET', url='/v1/environments',
                            params={"version": self.version}, accept_json=True)

    def get_environment(self, environment_id):
        """
        Retrieves information about the specific
        :param environment_id:
        :return:
        """

        return self.request(method='GET',
                            url='/v1/environments/{0}'.format(environment_id),
                            params={"version": self.version}, accept_json=True)

    @staticmethod
    def _valid_name_and_description(name, description):
        if len(name) not in range(0, 255):
            raise ValueError(
                "name must be a string having length between 0 and 255 "
                "characters")
        if len(description) not in range(0, 255):
            raise ValueError(
                "description must be a string having length between 0 and 255 "
                "characters")

    def create_environment(self, name="", description="", size=1):
        """

        :param name: name of the environment (max 255 chars) can be empty
        :param description: description of the environment (max 255 chars)
        can be empty
        :param size: size of the environment (1,2, or 3)
        :return:
        """
        self._valid_name_and_description(name=name, description=description)
        if size not in range(0, 4):
            raise ValueError("Size can be 0, 1, 2, or 3")

        body = json.dumps({"name": name,
                           "description": description,
                           "size": size})
        return self.request(method='POST',
                            url='/v1/environments',
                            params={"version": self.version},
                            data=body,
                            headers={'content-type': 'application/json'},
                            accept_json=True)

    def update_environment(self, environment_id, name="", description=""):
        """

        :param environment_id: guid of the environment to modify
        :param name: update the name of the environment
        :param description: update the description of the environment
        :return:
        """
        self._valid_name_and_description(name=name, description=description)
        body = json.dumps({"name": name, "description": description})
        return self.request(method='PUT',
                            url='/v1/environments/{0}'.format(environment_id),
                            params={"version": self.version},
                            data=body,
                            headers={'content-type': 'application/json'},
                            accept_json=True)

    def delete_environment(self, environment_id):
        """
        Deletes the specified environment.
        :param environment_id: guid of environment to delete
        :return:
        """
        url_string = '/v1/environments/{0}'.format(environment_id)
        return self.request(method='DELETE', url=url_string,
                            params={"version": self.version},
                            accept_json=True)

    def list_configurations(self, environment_id):

        format_string = '/v1/environments/{0}/configurations'
        url_string = format_string.format(environment_id)
        return self.request(method='GET', url=url_string,
                            params={'version': self.version},
                            accept_json=True)

    def get_configuration(self, environment_id, configuration_id):

        format_string = '/v1/environments/{0}/configurations/{1}'
        url_string = format_string.format(environment_id, configuration_id)
        return self.request(method='GET', url=url_string,
                            params={'version': self.version},
                            accept_json=True)

    def create_configuration(self, environment_id, config_data):

        format_string = '/v1/environments/{0}/configurations'
        url_string = format_string.format(environment_id)
        return self.request(method='POST', url=url_string,
                            params={'version': self.version},
                            data=json.dumps(config_data),
                            headers={'content-type': 'application/json'},
                            accept_json=True)

    def delete_configuration(self, environment_id, configuration_id):

        format_string = '/v1/environments/{0}/configurations/{1}'
        url_string = format_string.format(environment_id, configuration_id)
        return self.request(method='DELETE', url=url_string,
                            params={'version': self.version},
                            accept_json=True)

    def update_configuration(self,
                             environment_id,
                             configuration_id,
                             config_data):

        format_string = '/v1/environments/{0}/configurations/{1}'
        url_string = format_string.format(environment_id, configuration_id)
        return self.request(method='PUT', url=url_string,
                            params={'version': self.version},
                            data=json.dumps(config_data),
                            headers={'content-type': 'application/json'},
                            accept_json=True)

    def list_collections(self, environment_id):
        """
        Retrieves information about the collections within a given environment
        :param environment_id: this is the guid of a valid environment
        :return: json results of the collections in an environment
        """
        url_string = '/v1/environments/{0}/collections'.format(
            environment_id)
        return self.request(method='GET', url=url_string,
                            params={"version": self.version},
                            accept_json=True)

    def get_collection(self, environment_id, collection_id):
        """
        Retrieves information about a sepcific collection in an environment
        :param environment_id: the guid of a valid environment
        :param collection_id: the guid of a valid collection
        :return: json results of the collection information
        """
        return self.request(method='GET',
                            url='/v1/environments/{0}/collections/{1}'.format(
                                environment_id, collection_id),
                            params={"version": self.version},
                            accept_json=True)

    def create_collection(self,
                          environment_id,
                          name,
                          description="",
                          configuration_id=None):
        data_dict = {'configuration_id': configuration_id,
                     'name': name,
                     'description': description}
        url_string = '/v1/environments/{0}/collections'.format(
            environment_id)
        return self.request(method='POST',
                            url=url_string,
                            json=data_dict,
                            params={'version': self.version},
                            accept_json=True)

    def list_collection_fields(self, environment_id, collection_id):
        url_string = '/v1/environments/{0}/collections/{1}/fields'.format(
            environment_id, collection_id)

        return self.request(method='GET',
                            url=url_string,
                            params={'version': self.version},
                            accept_json=True)

    def delete_collection(self, environment_id, collection_id):

        url_string = '/v1/environments/{0}/collections/{1}'.format(
            environment_id, collection_id)

        return self.request(method='DELETE',
                            url=url_string,
                            params={'version': self.version},
                            accept_json=True)

    def add_document(self,
                     environment_id,
                     collection_id,
                     file_info=None,
                     file_data=None,
                     mime_type=None,
                     metadata=None):
        url_string = '/v1/environments/{0}/collections/{1}/documents'.format(
            environment_id, collection_id)

        params = {'version': self.version}

        if metadata is None:
            metadata = {}

        file_tuple = None

        if file_info:
            mime_type = mime_type or 'application/octet-stream'
            file_tuple = (file_info.name, file_info, mime_type)
        elif file_data:
            file_tuple = ('tmpfile', file_data, mime_type or
                          'application/html')

        return self.request(method='POST',
                            url=url_string,
                            params=params,
                            data=metadata,
                            files={'file': file_tuple,
                                   'metadata': (None,
                                                json.dumps(metadata),
                                                'application/json')},
                            accept_json=True)

    def update_document(self,
                        environment_id,
                        collection_id,
                        document_id,
                        file_info=None,
                        file_data=None,
                        mime_type=None,
                        metadata=None):
        url_string = '/v1/environments/{0}/collections/{1}/documents/{2}'. \
            format(environment_id, collection_id, document_id)

        params = {'version': self.version}

        if metadata is None:
            metadata = {}

        file_tuple = None

        if file_info:
            mime_type = mime_type or mimetypes.guess_type(
                file_info.name)[0]
            file_tuple = (file_info.name, file_info, mime_type)
        elif file_data:
            file_tuple = ('tmpfile', file_data, mime_type or
                          'application/html')

        return self.request(method='POST',
                            url=url_string,
                            params=params,
                            data=metadata,
                            files={'file': file_tuple,
                                   'metadata': (None,
                                                json.dumps(metadata),
                                                'application/json')},
                            accept_json=True)

    def test_document(self,
                      environment_id,
                      fileinfo,
                      configuration_id=None,
                      metadata=None):
        url_string = '/v1/environments/{0}/preview'.format(
            environment_id)

        params = {'version': self.version,
                  'configuration_id': configuration_id}

        if metadata is None:
            metadata = {}

        mime_type = mimetypes.guess_type(
            fileinfo.name)[0] or 'application/octet-stream'

        return self.request(method='POST',
                            url=url_string,
                            params=params,
                            data=metadata,
                            files={'file': (fileinfo.name,
                                            fileinfo,
                                            mime_type),
                                   'metadata': (None,
                                                json.dumps(metadata),
                                                'application/json')},
                            accept_json=True)

    def get_document(self,
                     environment_id,
                     collection_id,
                     document_id):
        """
        Get document status
        :param environment_id the guid of the environment
        :param collection_id collection guid
        :param document_id the id of the document
        :return dict of document info, not the contents.
        """
        base_url = '/v1/environments/{0}/collections/{1}/documents/{2}'

        url_string = base_url.format(
            environment_id, collection_id, document_id)

        params = {'version': self.version}

        return self.request(method='GET',
                            url=url_string,
                            params=params,
                            accept_json=True)

    def delete_document(self,
                        environment_id,
                        collection_id,
                        document_id):
        base_url = '/v1/environments/{0}/collections/{1}/documents/{2}'

        url_string = base_url.format(
            environment_id, collection_id, document_id)

        params = {'version': self.version}

        return self.request(method='DELETE',
                            url=url_string,
                            params=params,
                            accept_json=True)

    def query(self, environment_id, collection_id, query_options):
        """
         Performs a query and returns the results.
        :param environment_id: the guid of a valid environment
        :param collection_id: the guid of a valid collection
        :param query_options: this is a hash of query params and their values
        :return:
        """
        query_options["version"] = self.version
        return self.request(
            method='GET',
            url='/v1/environments/{0}/collections/{1}/query'.format(
                environment_id, collection_id),
            params=query_options, accept_json=True)


    def delete_training_data(self, environment_id, collection_id):
        """
        Clears all training data for this collection.
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :return: Code: 204, All training data removed
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data'
        url_string = format_string.format(environment_id, collection_id)
        params = {'version': self.version}

        return self.request(method='DELETE',
                            url=url_string,
                            params=params)


    def list_training_data(self, environment_id, collection_id):
        """
        Lists the training data for this collection
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :return: Training data for this collection found and returned.
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data'
        url_string = format_string.format(environment_id, collection_id)
        params = {'version': self.version}

        return self.request(method='GET',
                            url=url_string,
                            params=params,
                            accept_json=True)


    def add_training_data_query(self,
                                environment_id,
                                collection_id,
                                natural_language_query,
                                query_id=None,
                                filter=None,
                                examples=None):
        """
        Adds a query to the training data for this collection.
        The query can contain a filter and natural language query
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param natural_language_query:
        :param filter:
        :param examples:
        :return: Training data for this collection found and returned.
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data'
        url_string = format_string.format(environment_id, collection_id)
        params = {'version': self.version}
        data = {'natural_language_query': natural_language_query,
                'filter': filter,
                'examples': examples,
                'query_id': query_id}

        return self.request(method='POST',
                            url=url_string,
                            params=params,
                            json=data,
                            accept_json=True)


    def delete_training_data_query(self,
                                   environment_id,
                                   collection_id,
                                   query_id):
        """
        Removes the query and all associated examples from the training data
        set.
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param query_id: the ID of the query used for training
        :return: Code: 204, Query and all example document references
        successfully removed from the training set for this collection
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data/{2}'
        url_string = format_string.format(environment_id,
                                          collection_id,
                                          query_id)
        params = {'version': self.version}

        return self.request(method='DELETE',
                            url=url_string,
                            params=params)


    def get_training_data_query(self,
                                environment_id,
                                collection_id,
                                query_id):
        """
        Shows details for a specific query, including the query string and all
        examples.
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param query_id: the ID of the query used for training
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data/{2}'
        url_string = format_string.format(environment_id,
                                          collection_id,
                                          query_id)
        params = {'version': self.version}

        return self.request(method='GET',
                            url=url_string,
                            params=params,
                            accept_json=True)


    def list_training_data_query_examples(self,
                                          environment_id,
                                          collection_id,
                                          query_id):
        """
        Get all training examples for this query
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param query_id: the ID of the query used for training
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data' + \
            '/{2}/examples'
        url_string = format_string.format(environment_id,
                                          collection_id,
                                          query_id)
        params = {'version': self.version}

        return self.request(method='GET',
                            url=url_string,
                            params=params,
                            accept_json=True)


    def add_training_data_query_example(self,
                                        environment_id,
                                        collection_id,
                                        query_id,
                                        document_id,
                                        relevance,
                                        cross_reference=None):
        """
        Adds a new example to this query
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param query_id: the ID of the query used for training
        :param document_id:
        :param relevance:
        :param cross_reference:
        :return: The example was successfully added to the query.
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data' + \
            '/{2}/examples'
        url_string = format_string.format(environment_id,
                                          collection_id,
                                          query_id)
        params = {'version': self.version}
        data = {'document_id': document_id,
                'relevance': relevance,
                'cross_reference': cross_reference}

        return self.request(method='POST',
                            url=url_string,
                            params=params,
                            json=data,
                            accept_json=True)


    def delete_training_data_query_example(self,
                                           environment_id,
                                           collection_id,
                                           query_id,
                                           example_id):
        """
        Removes the example document with the given ID from the query.
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param query_id: the ID of the query used for training
        :param example_id: the ID of the document as it is indexed
        :return: Code: 204, The example document reference was removed from the
        query
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data' + \
            '/{2}/examples/{3}'
        url_string = format_string.format(environment_id,
                                          collection_id,
                                          query_id,
                                          example_id)
        params = {'version': self.version}

        return self.request(method='DELETE',
                            url=url_string,
                            params=params)


    def get_training_data_query_example(self,
                                        environment_id,
                                        collection_id,
                                        query_id,
                                        example_id):
        """
        Gets the details for this example.
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param query_id: the ID of the query used for training
        :param example_id: the ID of the document as it is indexed
        :return: Details for this example successfully found and returned.
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data' + \
            '/{2}/examples/{3}'
        url_string = format_string.format(environment_id,
                                          collection_id,
                                          query_id,
                                          example_id)
        params = {'version': self.version}

        return self.request(method='GET',
                            url=url_string,
                            params=params,
                            accept_json=True)


    def update_training_data_query_example(self,
                                           environment_id,
                                           collection_id,
                                           query_id,
                                           example_id,
                                           relevance=None,
                                           cross_reference=None):
        """
        Changes the label or cross reference query for this example.
        :param environment_id: the ID of your environment
        :param collection_id: the ID of your collection
        :param query_id: the ID of the query used for training
        :param example_id: the ID of the document as it is indexed
        :param relevance:
        :param cross_reference:
        :return: The label or cross reference query were successfully applied.
        """
        format_string = '/v1/environments/{0}/collections/{1}/training_data' + \
            '/{2}/examples/{3}'
        url_string = format_string.format(environment_id,
                                          collection_id,
                                          query_id,
                                          example_id)
        params = {'version': self.version}
        data = {'document_id': example_id,
                'relevance': relevance,
                'cross_reference': cross_reference}

        return self.request(method='PUT',
                            url=url_string,
                            params=params,
                            json=data,
                            accept_json=True)
