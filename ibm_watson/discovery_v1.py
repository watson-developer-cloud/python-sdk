# coding: utf-8

# (C) Copyright IBM Corp. 2019, 2020.
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
IBM Watson&trade; Discovery is a cognitive search and content analytics engine that you
can add to applications to identify patterns, trends and actionable insights to drive
better decision-making. Securely unify structured and unstructured data with pre-enriched
content, and use a simplified query language to eliminate the need for manual filtering of
results.
"""

import json
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from .common import get_sdk_headers
from datetime import date
from datetime import datetime
from enum import Enum
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import DetailedResponse
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from os.path import basename
from typing import BinaryIO
from typing import Dict
from typing import List
import sys

##############################################################################
# Service
##############################################################################


class DiscoveryV1(BaseService):
    """The Discovery V1 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/discovery/api'
    DEFAULT_SERVICE_NAME = 'discovery'

    def __init__(
            self,
            version: str,
            authenticator: Authenticator = None,
            service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Discovery service.

        :param str version: The API version date to use with the service, in
               "YYYY-MM-DD" format. Whenever the API is changed in a backwards
               incompatible way, a new minor version of the API is released.
               The service uses the API version for the date you specify, or
               the most recent version before that date. Note that you should
               not programmatically specify the current date at runtime, in
               case the API has been updated since your application's release.
               Instead, specify a version date that is compatible with your
               application, and don't change it until your application is
               ready for a later version.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if not authenticator:
            authenticator = get_authenticator_from_environment(service_name)
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator,
                             disable_ssl_verification=False)
        self.version = version
        self.configure_service(service_name)

    #########################
    # Environments
    #########################

    def create_environment(self,
                           name: str,
                           *,
                           description: str = None,
                           size: str = None,
                           **kwargs) -> 'DetailedResponse':
        """
        Create an environment.

        Creates a new environment for private data. An environment must be created before
        collections can be created.
        **Note**: You can create only one environment for private data per service
        instance. An attempt to create another environment results in an error.

        :param str name: Name that identifies the environment.
        :param str description: (optional) Description of the environment.
        :param str size: (optional) Size of the environment. In the Lite plan the
               default and only accepted value is `LT`, in all other plans the default is
               `S`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_environment')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'name': name, 'description': description, 'size': size}

        url = '/v1/environments'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def list_environments(self,
                          *,
                          name: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        List environments.

        List existing environments for the service instance.

        :param str name: (optional) Show only the environment with the given name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_environments')
        headers.update(sdk_headers)

        params = {'version': self.version, 'name': name}

        url = '/v1/environments'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_environment(self, environment_id: str,
                        **kwargs) -> 'DetailedResponse':
        """
        Get environment info.

        :param str environment_id: The ID of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_environment')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_environment(self,
                           environment_id: str,
                           *,
                           name: str = None,
                           description: str = None,
                           size: str = None,
                           **kwargs) -> 'DetailedResponse':
        """
        Update an environment.

        Updates an environment. The environment's **name** and  **description** parameters
        can be changed. You must specify a **name** for the environment.

        :param str environment_id: The ID of the environment.
        :param str name: (optional) Name that identifies the environment.
        :param str description: (optional) Description of the environment.
        :param str size: (optional) Size that the environment should be increased
               to. Environment size cannot be modified when using a Lite plan. Environment
               size can only increased and not decreased.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_environment')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'name': name, 'description': description, 'size': size}

        url = '/v1/environments/{0}'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_environment(self, environment_id: str,
                           **kwargs) -> 'DetailedResponse':
        """
        Delete environment.

        :param str environment_id: The ID of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_environment')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def list_fields(self, environment_id: str, collection_ids: List[str],
                    **kwargs) -> 'DetailedResponse':
        """
        List fields across collections.

        Gets a list of the unique fields (and their types) stored in the indexes of the
        specified collections.

        :param str environment_id: The ID of the environment.
        :param List[str] collection_ids: A comma-separated list of collection IDs
               to be queried against.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_ids is None:
            raise ValueError('collection_ids must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_fields')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'collection_ids': self._convert_list(collection_ids)
        }

        url = '/v1/environments/{0}/fields'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Configurations
    #########################

    def create_configuration(
            self,
            environment_id: str,
            name: str,
            *,
            description: str = None,
            conversions: 'Conversions' = None,
            enrichments: List['Enrichment'] = None,
            normalizations: List['NormalizationOperation'] = None,
            source: 'Source' = None,
            **kwargs) -> 'DetailedResponse':
        """
        Add configuration.

        Creates a new configuration.
        If the input configuration contains the **configuration_id**, **created**, or
        **updated** properties, then they are ignored and overridden by the system, and an
        error is not returned so that the overridden fields do not need to be removed when
        copying a configuration.
        The configuration can contain unrecognized JSON fields. Any such fields are
        ignored and do not generate an error. This makes it easier to use newer
        configuration files with older versions of the API and the service. It also makes
        it possible for the tooling to add additional metadata and information to the
        configuration.

        :param str environment_id: The ID of the environment.
        :param str name: The name of the configuration.
        :param str description: (optional) The description of the configuration, if
               available.
        :param Conversions conversions: (optional) Document conversion settings.
        :param List[Enrichment] enrichments: (optional) An array of document
               enrichment settings for the configuration.
        :param List[NormalizationOperation] normalizations: (optional) Defines
               operations that can be used to transform the final output JSON into a
               normalized form. Operations are executed in the order that they appear in
               the array.
        :param Source source: (optional) Object containing source parameters for
               the configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if conversions is not None:
            conversions = self._convert_model(conversions)
        if enrichments is not None:
            enrichments = [self._convert_model(x) for x in enrichments]
        if normalizations is not None:
            normalizations = [self._convert_model(x) for x in normalizations]
        if source is not None:
            source = self._convert_model(source)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_configuration')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'name': name,
            'description': description,
            'conversions': conversions,
            'enrichments': enrichments,
            'normalizations': normalizations,
            'source': source
        }

        url = '/v1/environments/{0}/configurations'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def list_configurations(self,
                            environment_id: str,
                            *,
                            name: str = None,
                            **kwargs) -> 'DetailedResponse':
        """
        List configurations.

        Lists existing configurations for the service instance.

        :param str environment_id: The ID of the environment.
        :param str name: (optional) Find configurations with the given name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_configurations')
        headers.update(sdk_headers)

        params = {'version': self.version, 'name': name}

        url = '/v1/environments/{0}/configurations'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_configuration(self, environment_id: str, configuration_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Get configuration details.

        :param str environment_id: The ID of the environment.
        :param str configuration_id: The ID of the configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if configuration_id is None:
            raise ValueError('configuration_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_configuration')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/configurations/{1}'.format(
            *self._encode_path_vars(environment_id, configuration_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_configuration(
            self,
            environment_id: str,
            configuration_id: str,
            name: str,
            *,
            description: str = None,
            conversions: 'Conversions' = None,
            enrichments: List['Enrichment'] = None,
            normalizations: List['NormalizationOperation'] = None,
            source: 'Source' = None,
            **kwargs) -> 'DetailedResponse':
        """
        Update a configuration.

        Replaces an existing configuration.
          * Completely replaces the original configuration.
          * The **configuration_id**, **updated**, and **created** fields are accepted in
        the request, but they are ignored, and an error is not generated. It is also
        acceptable for users to submit an updated configuration with none of the three
        properties.
          * Documents are processed with a snapshot of the configuration as it was at the
        time the document was submitted to be ingested. This means that already submitted
        documents will not see any updates made to the configuration.

        :param str environment_id: The ID of the environment.
        :param str configuration_id: The ID of the configuration.
        :param str name: The name of the configuration.
        :param str description: (optional) The description of the configuration, if
               available.
        :param Conversions conversions: (optional) Document conversion settings.
        :param List[Enrichment] enrichments: (optional) An array of document
               enrichment settings for the configuration.
        :param List[NormalizationOperation] normalizations: (optional) Defines
               operations that can be used to transform the final output JSON into a
               normalized form. Operations are executed in the order that they appear in
               the array.
        :param Source source: (optional) Object containing source parameters for
               the configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if configuration_id is None:
            raise ValueError('configuration_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if conversions is not None:
            conversions = self._convert_model(conversions)
        if enrichments is not None:
            enrichments = [self._convert_model(x) for x in enrichments]
        if normalizations is not None:
            normalizations = [self._convert_model(x) for x in normalizations]
        if source is not None:
            source = self._convert_model(source)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_configuration')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'name': name,
            'description': description,
            'conversions': conversions,
            'enrichments': enrichments,
            'normalizations': normalizations,
            'source': source
        }

        url = '/v1/environments/{0}/configurations/{1}'.format(
            *self._encode_path_vars(environment_id, configuration_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_configuration(self, environment_id: str, configuration_id: str,
                             **kwargs) -> 'DetailedResponse':
        """
        Delete a configuration.

        The deletion is performed unconditionally. A configuration deletion request
        succeeds even if the configuration is referenced by a collection or document
        ingestion. However, documents that have already been submitted for processing
        continue to use the deleted configuration. Documents are always processed with a
        snapshot of the configuration as it existed at the time the document was
        submitted.

        :param str environment_id: The ID of the environment.
        :param str configuration_id: The ID of the configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if configuration_id is None:
            raise ValueError('configuration_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_configuration')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/configurations/{1}'.format(
            *self._encode_path_vars(environment_id, configuration_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Collections
    #########################

    def create_collection(self,
                          environment_id: str,
                          name: str,
                          *,
                          description: str = None,
                          configuration_id: str = None,
                          language: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Create a collection.

        :param str environment_id: The ID of the environment.
        :param str name: The name of the collection to be created.
        :param str description: (optional) A description of the collection.
        :param str configuration_id: (optional) The ID of the configuration in
               which the collection is to be created.
        :param str language: (optional) The language of the documents stored in the
               collection, in the form of an ISO 639-1 language code.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if name is None:
            raise ValueError('name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'name': name,
            'description': description,
            'configuration_id': configuration_id,
            'language': language
        }

        url = '/v1/environments/{0}/collections'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def list_collections(self,
                         environment_id: str,
                         *,
                         name: str = None,
                         **kwargs) -> 'DetailedResponse':
        """
        List collections.

        Lists existing collections for the service instance.

        :param str environment_id: The ID of the environment.
        :param str name: (optional) Find collections with the given name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_collections')
        headers.update(sdk_headers)

        params = {'version': self.version, 'name': name}

        url = '/v1/environments/{0}/collections'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_collection(self, environment_id: str, collection_id: str,
                       **kwargs) -> 'DetailedResponse':
        """
        Get collection details.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_collection(self,
                          environment_id: str,
                          collection_id: str,
                          name: str,
                          *,
                          description: str = None,
                          configuration_id: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Update a collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str name: The name of the collection.
        :param str description: (optional) A description of the collection.
        :param str configuration_id: (optional) The ID of the configuration in
               which the collection is to be updated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if name is None:
            raise ValueError('name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'name': name,
            'description': description,
            'configuration_id': configuration_id
        }

        url = '/v1/environments/{0}/collections/{1}'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_collection(self, environment_id: str, collection_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Delete a collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def list_collection_fields(self, environment_id: str, collection_id: str,
                               **kwargs) -> 'DetailedResponse':
        """
        List collection fields.

        Gets a list of the unique fields (and their types) stored in the index.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_collection_fields')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/fields'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Query modifications
    #########################

    def list_expansions(self, environment_id: str, collection_id: str,
                        **kwargs) -> 'DetailedResponse':
        """
        Get the expansion list.

        Returns the current expansion list for the specified collection. If an expansion
        list is not specified, an object with empty expansion arrays is returned.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_expansions')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/expansions'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def create_expansions(self, environment_id: str, collection_id: str,
                          expansions: List['Expansion'],
                          **kwargs) -> 'DetailedResponse':
        """
        Create or update expansion list.

        Create or replace the Expansion list for this collection. The maximum number of
        expanded terms per collection is `500`. The current expansion list is replaced
        with the uploaded content.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param List[Expansion] expansions: An array of query expansion definitions.
                Each object in the **expansions** array represents a term or set of terms
               that will be expanded into other terms. Each expansion object can be
               configured as bidirectional or unidirectional. Bidirectional means that all
               terms are expanded to all other terms in the object. Unidirectional means
               that a set list of terms can be expanded into a second list of terms.
                To create a bi-directional expansion specify an **expanded_terms** array.
               When found in a query, all items in the **expanded_terms** array are then
               expanded to the other items in the same array.
                To create a uni-directional expansion, specify both an array of
               **input_terms** and an array of **expanded_terms**. When items in the
               **input_terms** array are present in a query, they are expanded using the
               items listed in the **expanded_terms** array.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if expansions is None:
            raise ValueError('expansions must be provided')
        expansions = [self._convert_model(x) for x in expansions]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_expansions')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'expansions': expansions}

        url = '/v1/environments/{0}/collections/{1}/expansions'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_expansions(self, environment_id: str, collection_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Delete the expansion list.

        Remove the expansion information for this collection. The expansion list must be
        deleted to disable query expansion for a collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_expansions')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/expansions'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_tokenization_dictionary_status(self, environment_id: str,
                                           collection_id: str,
                                           **kwargs) -> 'DetailedResponse':
        """
        Get tokenization dictionary status.

        Returns the current status of the tokenization dictionary for the specified
        collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_tokenization_dictionary_status')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/word_lists/tokenization_dictionary'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def create_tokenization_dictionary(
            self,
            environment_id: str,
            collection_id: str,
            *,
            tokenization_rules: List['TokenDictRule'] = None,
            **kwargs) -> 'DetailedResponse':
        """
        Create tokenization dictionary.

        Upload a custom tokenization dictionary to use with the specified collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param List[TokenDictRule] tokenization_rules: (optional) An array of
               tokenization rules. Each rule contains, the original `text` string,
               component `tokens`, any alternate character set `readings`, and which
               `part_of_speech` the text is from.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if tokenization_rules is not None:
            tokenization_rules = [
                self._convert_model(x) for x in tokenization_rules
            ]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_tokenization_dictionary')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'tokenization_rules': tokenization_rules}

        url = '/v1/environments/{0}/collections/{1}/word_lists/tokenization_dictionary'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_tokenization_dictionary(self, environment_id: str,
                                       collection_id: str,
                                       **kwargs) -> 'DetailedResponse':
        """
        Delete tokenization dictionary.

        Delete the tokenization dictionary from the collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_tokenization_dictionary')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/word_lists/tokenization_dictionary'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_stopword_list_status(self, environment_id: str, collection_id: str,
                                 **kwargs) -> 'DetailedResponse':
        """
        Get stopword list status.

        Returns the current status of the stopword list for the specified collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_stopword_list_status')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/word_lists/stopwords'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def create_stopword_list(self,
                             environment_id: str,
                             collection_id: str,
                             stopword_file: BinaryIO,
                             *,
                             stopword_filename: str = None,
                             **kwargs) -> 'DetailedResponse':
        """
        Create stopword list.

        Upload a custom stopword list to use with the specified collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param TextIO stopword_file: The content of the stopword list to ingest.
        :param str stopword_filename: (optional) The filename for stopword_file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if stopword_file is None:
            raise ValueError('stopword_file must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_stopword_list')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        if not stopword_filename and hasattr(stopword_file, 'name'):
            stopword_filename = basename(stopword_file.name)
        if not stopword_filename:
            raise ValueError('stopword_filename must be provided')
        form_data.append(('stopword_file', (stopword_filename, stopword_file,
                                            'application/octet-stream')))

        url = '/v1/environments/{0}/collections/{1}/word_lists/stopwords'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    def delete_stopword_list(self, environment_id: str, collection_id: str,
                             **kwargs) -> 'DetailedResponse':
        """
        Delete a custom stopword list.

        Delete a custom stopword list from the collection. After a custom stopword list is
        deleted, the default list is used for the collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_stopword_list')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/word_lists/stopwords'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Documents
    #########################

    def add_document(self,
                     environment_id: str,
                     collection_id: str,
                     *,
                     file: BinaryIO = None,
                     filename: str = None,
                     file_content_type: str = None,
                     metadata: str = None,
                     **kwargs) -> 'DetailedResponse':
        """
        Add a document.

        Add a document to a collection with optional metadata.
          * The **version** query parameter is still required.
          * Returns immediately after the system has accepted the document for processing.
          * The user must provide document content, metadata, or both. If the request is
        missing both document content and metadata, it is rejected.
          * The user can set the **Content-Type** parameter on the **file** part to
        indicate the media type of the document. If the **Content-Type** parameter is
        missing or is one of the generic media types (for example,
        `application/octet-stream`), then the service attempts to automatically detect the
        document's media type.
          * The following field names are reserved and will be filtered out if present
        after normalization: `id`, `score`, `highlight`, and any field with the prefix of:
        `_`, `+`, or `-`
          * Fields with empty name values after normalization are filtered out before
        indexing.
          * Fields containing the following characters after normalization are filtered
        out before indexing: `#` and `,`
         **Note:** Documents can be added with a specific **document_id** by using the
        **_/v1/environments/{environment_id}/collections/{collection_id}/documents**
        method.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param TextIO file: (optional) The content of the document to ingest. The
               maximum supported file size when adding a file to a collection is 50
               megabytes, the maximum supported file size when testing a configuration is
               1 megabyte. Files larger than the supported size are rejected.
        :param str filename: (optional) The filename for file.
        :param str file_content_type: (optional) The content type of file.
        :param str metadata: (optional) The maximum supported metadata file size is
               1 MB. Metadata parts larger than 1 MB are rejected. Example:  ``` {
                 "Creator": "Johnny Appleseed",
                 "Subject": "Apples"
               } ```.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_document')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        if file:
            if not filename and hasattr(file, 'name'):
                filename = basename(file.name)
            if not filename:
                raise ValueError('filename must be provided')
            form_data.append(('file', (filename, file, file_content_type or
                                       'application/octet-stream')))
        if metadata:
            metadata = str(metadata)
            form_data.append(('metadata', (None, metadata, 'text/plain')))

        url = '/v1/environments/{0}/collections/{1}/documents'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    def get_document_status(self, environment_id: str, collection_id: str,
                            document_id: str, **kwargs) -> 'DetailedResponse':
        """
        Get document details.

        Fetch status details about a submitted document. **Note:** this operation does not
        return the document itself. Instead, it returns only the document's processing
        status and any notices (warnings or errors) that were generated when the document
        was ingested. Use the query API to retrieve the actual document content.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if document_id is None:
            raise ValueError('document_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_document_status')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, document_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_document(self,
                        environment_id: str,
                        collection_id: str,
                        document_id: str,
                        *,
                        file: BinaryIO = None,
                        filename: str = None,
                        file_content_type: str = None,
                        metadata: str = None,
                        **kwargs) -> 'DetailedResponse':
        """
        Update a document.

        Replace an existing document or add a document with a specified **document_id**.
        Starts ingesting a document with optional metadata.
        **Note:** When uploading a new document with this method it automatically replaces
        any document stored with the same **document_id** if it exists.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param TextIO file: (optional) The content of the document to ingest. The
               maximum supported file size when adding a file to a collection is 50
               megabytes, the maximum supported file size when testing a configuration is
               1 megabyte. Files larger than the supported size are rejected.
        :param str filename: (optional) The filename for file.
        :param str file_content_type: (optional) The content type of file.
        :param str metadata: (optional) The maximum supported metadata file size is
               1 MB. Metadata parts larger than 1 MB are rejected. Example:  ``` {
                 "Creator": "Johnny Appleseed",
                 "Subject": "Apples"
               } ```.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if document_id is None:
            raise ValueError('document_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_document')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        if file:
            if not filename and hasattr(file, 'name'):
                filename = basename(file.name)
            if not filename:
                raise ValueError('filename must be provided')
            form_data.append(('file', (filename, file, file_content_type or
                                       'application/octet-stream')))
        if metadata:
            metadata = str(metadata)
            form_data.append(('metadata', (None, metadata, 'text/plain')))

        url = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, document_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    def delete_document(self, environment_id: str, collection_id: str,
                        document_id: str, **kwargs) -> 'DetailedResponse':
        """
        Delete a document.

        If the given document ID is invalid, or if the document is not found, then the a
        success response is returned (HTTP status code `200`) with the status set to
        'deleted'.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if document_id is None:
            raise ValueError('document_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_document')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, document_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Queries
    #########################

    def query(self,
              environment_id: str,
              collection_id: str,
              *,
              filter: str = None,
              query: str = None,
              natural_language_query: str = None,
              passages: bool = None,
              aggregation: str = None,
              count: int = None,
              return_: str = None,
              offset: int = None,
              sort: str = None,
              highlight: bool = None,
              passages_fields: str = None,
              passages_count: int = None,
              passages_characters: int = None,
              deduplicate: bool = None,
              deduplicate_field: str = None,
              similar: bool = None,
              similar_document_ids: str = None,
              similar_fields: str = None,
              bias: str = None,
              spelling_suggestions: bool = None,
              x_watson_logging_opt_out: bool = None,
              **kwargs) -> 'DetailedResponse':
        """
        Query a collection.

        By using this method, you can construct long queries. For details, see the
        [Discovery
        documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-concepts#query-concepts).

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str filter: (optional) A cacheable query that excludes documents
               that don't mention the query content. Filter searches are better for
               metadata-type searches and for assessing the concepts in the data set.
        :param str query: (optional) A query search returns all documents in your
               data set with full enrichments and full text, but with the most relevant
               documents listed first. Use a query search when you want to find the most
               relevant search results.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by utilizing training data and natural language
               understanding.
        :param bool passages: (optional) A passages query that returns the most
               relevant passages from the results.
        :param str aggregation: (optional) An aggregation search that returns an
               exact answer by combining query search with filters. Useful for
               applications to build lists, tables, and time series. For a full list of
               possible aggregations, see the Query reference.
        :param int count: (optional) Number of results to return.
        :param str return_: (optional) A comma-separated list of the portion of the
               document hierarchy to return.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results.
        :param str sort: (optional) A comma-separated list of fields in the
               document to sort on. You can optionally specify a sort direction by
               prefixing the field with `-` for descending or `+` for ascending. Ascending
               is the default sort direction if no prefix is specified. This parameter
               cannot be used in the same query as the **bias** parameter.
        :param bool highlight: (optional) When true, a highlight field is returned
               for each result which contains the fields which match the query with
               `<em></em>` tags around the matching query terms.
        :param str passages_fields: (optional) A comma-separated list of fields
               that passages are drawn from. If this parameter not specified, then all
               top-level fields are included.
        :param int passages_count: (optional) The maximum number of passages to
               return. The search returns fewer passages if the requested total is not
               found. The default is `10`. The maximum is `100`.
        :param int passages_characters: (optional) The approximate number of
               characters that any one passage will have.
        :param bool deduplicate: (optional) When `true`, and used with a Watson
               Discovery News collection, duplicate results (based on the contents of the
               **title** field) are removed. Duplicate comparison is limited to the
               current query only; **offset** is not considered. This parameter is
               currently Beta functionality.
        :param str deduplicate_field: (optional) When specified, duplicate results
               based on the field specified are removed from the returned results.
               Duplicate comparison is limited to the current query only, **offset** is
               not considered. This parameter is currently Beta functionality.
        :param bool similar: (optional) When `true`, results are returned based on
               their similarity to the document IDs specified in the
               **similar.document_ids** parameter.
        :param str similar_document_ids: (optional) A comma-separated list of
               document IDs to find similar documents.
               **Tip:** Include the **natural_language_query** parameter to expand the
               scope of the document similarity search with the natural language query.
               Other query parameters, such as **filter** and **query**, are subsequently
               applied and reduce the scope.
        :param str similar_fields: (optional) A comma-separated list of field names
               that are used as a basis for comparison to identify similar documents. If
               not specified, the entire document is used for comparison.
        :param str bias: (optional) Field which the returned results will be biased
               against. The specified field must be either a **date** or **number**
               format. When a **date** type field is specified returned results are biased
               towards field values closer to the current date. When a **number** type
               field is specified, returned results are biased towards higher field
               values. This parameter cannot be used in the same query as the **sort**
               parameter.
        :param bool spelling_suggestions: (optional) When `true` and the
               **natural_language_query** parameter is used, the **natural_languge_query**
               parameter is spell checked. The most likely correction is retunred in the
               **suggested_query** field of the response (if one exists).
               **Important:** this parameter is only valid when using the Cloud Pak
               version of Discovery.
        :param bool x_watson_logging_opt_out: (optional) If `true`, queries are not
               stored in the Discovery **Logs** endpoint.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {'X-Watson-Logging-Opt-Out': x_watson_logging_opt_out}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='query')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'passages': passages,
            'aggregation': aggregation,
            'count': count,
            'return': return_,
            'offset': offset,
            'sort': sort,
            'highlight': highlight,
            'passages.fields': passages_fields,
            'passages.count': passages_count,
            'passages.characters': passages_characters,
            'deduplicate': deduplicate,
            'deduplicate.field': deduplicate_field,
            'similar': similar,
            'similar.document_ids': similar_document_ids,
            'similar.fields': similar_fields,
            'bias': bias,
            'spelling_suggestions': spelling_suggestions
        }

        url = '/v1/environments/{0}/collections/{1}/query'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def query_notices(self,
                      environment_id: str,
                      collection_id: str,
                      *,
                      filter: str = None,
                      query: str = None,
                      natural_language_query: str = None,
                      passages: bool = None,
                      aggregation: str = None,
                      count: int = None,
                      return_: List[str] = None,
                      offset: int = None,
                      sort: List[str] = None,
                      highlight: bool = None,
                      passages_fields: List[str] = None,
                      passages_count: int = None,
                      passages_characters: int = None,
                      deduplicate_field: str = None,
                      similar: bool = None,
                      similar_document_ids: List[str] = None,
                      similar_fields: List[str] = None,
                      **kwargs) -> 'DetailedResponse':
        """
        Query system notices.

        Queries for notices (errors or warnings) that might have been generated by the
        system. Notices are generated when ingesting documents and performing relevance
        training. See the [Discovery
        documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-concepts#query-concepts)
        for more details on the query language.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str filter: (optional) A cacheable query that excludes documents
               that don't mention the query content. Filter searches are better for
               metadata-type searches and for assessing the concepts in the data set.
        :param str query: (optional) A query search returns all documents in your
               data set with full enrichments and full text, but with the most relevant
               documents listed first.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by utilizing training data and natural language
               understanding.
        :param bool passages: (optional) A passages query that returns the most
               relevant passages from the results.
        :param str aggregation: (optional) An aggregation search that returns an
               exact answer by combining query search with filters. Useful for
               applications to build lists, tables, and time series. For a full list of
               possible aggregations, see the Query reference.
        :param int count: (optional) Number of results to return. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param List[str] return_: (optional) A comma-separated list of the portion
               of the document hierarchy to return.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param List[str] sort: (optional) A comma-separated list of fields in the
               document to sort on. You can optionally specify a sort direction by
               prefixing the field with `-` for descending or `+` for ascending. Ascending
               is the default sort direction if no prefix is specified.
        :param bool highlight: (optional) When true, a highlight field is returned
               for each result which contains the fields which match the query with
               `<em></em>` tags around the matching query terms.
        :param List[str] passages_fields: (optional) A comma-separated list of
               fields that passages are drawn from. If this parameter not specified, then
               all top-level fields are included.
        :param int passages_count: (optional) The maximum number of passages to
               return. The search returns fewer passages if the requested total is not
               found.
        :param int passages_characters: (optional) The approximate number of
               characters that any one passage will have.
        :param str deduplicate_field: (optional) When specified, duplicate results
               based on the field specified are removed from the returned results.
               Duplicate comparison is limited to the current query only, **offset** is
               not considered. This parameter is currently Beta functionality.
        :param bool similar: (optional) When `true`, results are returned based on
               their similarity to the document IDs specified in the
               **similar.document_ids** parameter.
        :param List[str] similar_document_ids: (optional) A comma-separated list of
               document IDs to find similar documents.
               **Tip:** Include the **natural_language_query** parameter to expand the
               scope of the document similarity search with the natural language query.
               Other query parameters, such as **filter** and **query**, are subsequently
               applied and reduce the scope.
        :param List[str] similar_fields: (optional) A comma-separated list of field
               names that are used as a basis for comparison to identify similar
               documents. If not specified, the entire document is used for comparison.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='query_notices')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'passages': passages,
            'aggregation': aggregation,
            'count': count,
            'return': self._convert_list(return_),
            'offset': offset,
            'sort': self._convert_list(sort),
            'highlight': highlight,
            'passages.fields': self._convert_list(passages_fields),
            'passages.count': passages_count,
            'passages.characters': passages_characters,
            'deduplicate.field': deduplicate_field,
            'similar': similar,
            'similar.document_ids': self._convert_list(similar_document_ids),
            'similar.fields': self._convert_list(similar_fields)
        }

        url = '/v1/environments/{0}/collections/{1}/notices'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def federated_query(self,
                        environment_id: str,
                        collection_ids: str,
                        *,
                        filter: str = None,
                        query: str = None,
                        natural_language_query: str = None,
                        passages: bool = None,
                        aggregation: str = None,
                        count: int = None,
                        return_: str = None,
                        offset: int = None,
                        sort: str = None,
                        highlight: bool = None,
                        passages_fields: str = None,
                        passages_count: int = None,
                        passages_characters: int = None,
                        deduplicate: bool = None,
                        deduplicate_field: str = None,
                        similar: bool = None,
                        similar_document_ids: str = None,
                        similar_fields: str = None,
                        bias: str = None,
                        x_watson_logging_opt_out: bool = None,
                        **kwargs) -> 'DetailedResponse':
        """
        Query multiple collections.

        By using this method, you can construct long queries that search multiple
        collection. For details, see the [Discovery
        documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-concepts#query-concepts).

        :param str environment_id: The ID of the environment.
        :param str collection_ids: A comma-separated list of collection IDs to be
               queried against.
        :param str filter: (optional) A cacheable query that excludes documents
               that don't mention the query content. Filter searches are better for
               metadata-type searches and for assessing the concepts in the data set.
        :param str query: (optional) A query search returns all documents in your
               data set with full enrichments and full text, but with the most relevant
               documents listed first. Use a query search when you want to find the most
               relevant search results.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by utilizing training data and natural language
               understanding.
        :param bool passages: (optional) A passages query that returns the most
               relevant passages from the results.
        :param str aggregation: (optional) An aggregation search that returns an
               exact answer by combining query search with filters. Useful for
               applications to build lists, tables, and time series. For a full list of
               possible aggregations, see the Query reference.
        :param int count: (optional) Number of results to return.
        :param str return_: (optional) A comma-separated list of the portion of the
               document hierarchy to return.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results.
        :param str sort: (optional) A comma-separated list of fields in the
               document to sort on. You can optionally specify a sort direction by
               prefixing the field with `-` for descending or `+` for ascending. Ascending
               is the default sort direction if no prefix is specified. This parameter
               cannot be used in the same query as the **bias** parameter.
        :param bool highlight: (optional) When true, a highlight field is returned
               for each result which contains the fields which match the query with
               `<em></em>` tags around the matching query terms.
        :param str passages_fields: (optional) A comma-separated list of fields
               that passages are drawn from. If this parameter not specified, then all
               top-level fields are included.
        :param int passages_count: (optional) The maximum number of passages to
               return. The search returns fewer passages if the requested total is not
               found. The default is `10`. The maximum is `100`.
        :param int passages_characters: (optional) The approximate number of
               characters that any one passage will have.
        :param bool deduplicate: (optional) When `true`, and used with a Watson
               Discovery News collection, duplicate results (based on the contents of the
               **title** field) are removed. Duplicate comparison is limited to the
               current query only; **offset** is not considered. This parameter is
               currently Beta functionality.
        :param str deduplicate_field: (optional) When specified, duplicate results
               based on the field specified are removed from the returned results.
               Duplicate comparison is limited to the current query only, **offset** is
               not considered. This parameter is currently Beta functionality.
        :param bool similar: (optional) When `true`, results are returned based on
               their similarity to the document IDs specified in the
               **similar.document_ids** parameter.
        :param str similar_document_ids: (optional) A comma-separated list of
               document IDs to find similar documents.
               **Tip:** Include the **natural_language_query** parameter to expand the
               scope of the document similarity search with the natural language query.
               Other query parameters, such as **filter** and **query**, are subsequently
               applied and reduce the scope.
        :param str similar_fields: (optional) A comma-separated list of field names
               that are used as a basis for comparison to identify similar documents. If
               not specified, the entire document is used for comparison.
        :param str bias: (optional) Field which the returned results will be biased
               against. The specified field must be either a **date** or **number**
               format. When a **date** type field is specified returned results are biased
               towards field values closer to the current date. When a **number** type
               field is specified, returned results are biased towards higher field
               values. This parameter cannot be used in the same query as the **sort**
               parameter.
        :param bool x_watson_logging_opt_out: (optional) If `true`, queries are not
               stored in the Discovery **Logs** endpoint.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_ids is None:
            raise ValueError('collection_ids must be provided')

        headers = {'X-Watson-Logging-Opt-Out': x_watson_logging_opt_out}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='federated_query')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'collection_ids': collection_ids,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'passages': passages,
            'aggregation': aggregation,
            'count': count,
            'return': return_,
            'offset': offset,
            'sort': sort,
            'highlight': highlight,
            'passages.fields': passages_fields,
            'passages.count': passages_count,
            'passages.characters': passages_characters,
            'deduplicate': deduplicate,
            'deduplicate.field': deduplicate_field,
            'similar': similar,
            'similar.document_ids': similar_document_ids,
            'similar.fields': similar_fields,
            'bias': bias
        }

        url = '/v1/environments/{0}/query'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def federated_query_notices(self,
                                environment_id: str,
                                collection_ids: List[str],
                                *,
                                filter: str = None,
                                query: str = None,
                                natural_language_query: str = None,
                                aggregation: str = None,
                                count: int = None,
                                return_: List[str] = None,
                                offset: int = None,
                                sort: List[str] = None,
                                highlight: bool = None,
                                deduplicate_field: str = None,
                                similar: bool = None,
                                similar_document_ids: List[str] = None,
                                similar_fields: List[str] = None,
                                **kwargs) -> 'DetailedResponse':
        """
        Query multiple collection system notices.

        Queries for notices (errors or warnings) that might have been generated by the
        system. Notices are generated when ingesting documents and performing relevance
        training. See the [Discovery
        documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-concepts#query-concepts)
        for more details on the query language.

        :param str environment_id: The ID of the environment.
        :param List[str] collection_ids: A comma-separated list of collection IDs
               to be queried against.
        :param str filter: (optional) A cacheable query that excludes documents
               that don't mention the query content. Filter searches are better for
               metadata-type searches and for assessing the concepts in the data set.
        :param str query: (optional) A query search returns all documents in your
               data set with full enrichments and full text, but with the most relevant
               documents listed first.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by utilizing training data and natural language
               understanding.
        :param str aggregation: (optional) An aggregation search that returns an
               exact answer by combining query search with filters. Useful for
               applications to build lists, tables, and time series. For a full list of
               possible aggregations, see the Query reference.
        :param int count: (optional) Number of results to return. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param List[str] return_: (optional) A comma-separated list of the portion
               of the document hierarchy to return.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param List[str] sort: (optional) A comma-separated list of fields in the
               document to sort on. You can optionally specify a sort direction by
               prefixing the field with `-` for descending or `+` for ascending. Ascending
               is the default sort direction if no prefix is specified.
        :param bool highlight: (optional) When true, a highlight field is returned
               for each result which contains the fields which match the query with
               `<em></em>` tags around the matching query terms.
        :param str deduplicate_field: (optional) When specified, duplicate results
               based on the field specified are removed from the returned results.
               Duplicate comparison is limited to the current query only, **offset** is
               not considered. This parameter is currently Beta functionality.
        :param bool similar: (optional) When `true`, results are returned based on
               their similarity to the document IDs specified in the
               **similar.document_ids** parameter.
        :param List[str] similar_document_ids: (optional) A comma-separated list of
               document IDs to find similar documents.
               **Tip:** Include the **natural_language_query** parameter to expand the
               scope of the document similarity search with the natural language query.
               Other query parameters, such as **filter** and **query**, are subsequently
               applied and reduce the scope.
        :param List[str] similar_fields: (optional) A comma-separated list of field
               names that are used as a basis for comparison to identify similar
               documents. If not specified, the entire document is used for comparison.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_ids is None:
            raise ValueError('collection_ids must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='federated_query_notices')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'collection_ids': self._convert_list(collection_ids),
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'aggregation': aggregation,
            'count': count,
            'return': self._convert_list(return_),
            'offset': offset,
            'sort': self._convert_list(sort),
            'highlight': highlight,
            'deduplicate.field': deduplicate_field,
            'similar': similar,
            'similar.document_ids': self._convert_list(similar_document_ids),
            'similar.fields': self._convert_list(similar_fields)
        }

        url = '/v1/environments/{0}/notices'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_autocompletion(self,
                           environment_id: str,
                           collection_id: str,
                           prefix: str,
                           *,
                           field: str = None,
                           count: int = None,
                           **kwargs) -> 'DetailedResponse':
        """
        Get Autocomplete Suggestions.

        Returns completion query suggestions for the specified prefix.  /n/n
        **Important:** this method is only valid when using the Cloud Pak version of
        Discovery.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str prefix: The prefix to use for autocompletion. For example, the
               prefix `Ho` could autocomplete to `Hot`, `Housing`, or `How do I upgrade`.
               Possible completions are.
        :param str field: (optional) The field in the result documents that
               autocompletion suggestions are identified from.
        :param int count: (optional) The number of autocompletion suggestions to
               return.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if prefix is None:
            raise ValueError('prefix must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_autocompletion')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'prefix': prefix,
            'field': field,
            'count': count
        }

        url = '/v1/environments/{0}/collections/{1}/autocompletion'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Training data
    #########################

    def list_training_data(self, environment_id: str, collection_id: str,
                           **kwargs) -> 'DetailedResponse':
        """
        List training data.

        Lists the training data for the specified collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_training_data')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/training_data'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def add_training_data(self,
                          environment_id: str,
                          collection_id: str,
                          *,
                          natural_language_query: str = None,
                          filter: str = None,
                          examples: List['TrainingExample'] = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Add query to training data.

        Adds a query to the training data for this collection. The query can contain a
        filter and natural language query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str natural_language_query: (optional) The natural text query for
               the new training query.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        :param List[TrainingExample] examples: (optional) Array of training
               examples.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if examples is not None:
            examples = [self._convert_model(x) for x in examples]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_training_data')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'natural_language_query': natural_language_query,
            'filter': filter,
            'examples': examples
        }

        url = '/v1/environments/{0}/collections/{1}/training_data'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_all_training_data(self, environment_id: str, collection_id: str,
                                 **kwargs) -> 'DetailedResponse':
        """
        Delete all training data.

        Deletes all training data from a collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_all_training_data')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/training_data'.format(
            *self._encode_path_vars(environment_id, collection_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_training_data(self, environment_id: str, collection_id: str,
                          query_id: str, **kwargs) -> 'DetailedResponse':
        """
        Get details about a query.

        Gets details for a specific training data query, including the query string and
        all examples.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_training_data')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/training_data/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def delete_training_data(self, environment_id: str, collection_id: str,
                             query_id: str, **kwargs) -> 'DetailedResponse':
        """
        Delete a training data query.

        Removes the training data query and all associated examples from the training data
        set.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_training_data')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/training_data/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def list_training_examples(self, environment_id: str, collection_id: str,
                               query_id: str, **kwargs) -> 'DetailedResponse':
        """
        List examples for a training data query.

        List all examples for this training data query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_training_examples')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def create_training_example(self,
                                environment_id: str,
                                collection_id: str,
                                query_id: str,
                                *,
                                document_id: str = None,
                                cross_reference: str = None,
                                relevance: int = None,
                                **kwargs) -> 'DetailedResponse':
        """
        Add example to training data query.

        Adds a example to this training data query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str document_id: (optional) The document ID associated with this
               training example.
        :param str cross_reference: (optional) The cross reference associated with
               this training example.
        :param int relevance: (optional) The relevance of the training example.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_training_example')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'document_id': document_id,
            'cross_reference': cross_reference,
            'relevance': relevance
        }

        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_training_example(self, environment_id: str, collection_id: str,
                                query_id: str, example_id: str,
                                **kwargs) -> 'DetailedResponse':
        """
        Delete example for training data query.

        Deletes the example document with the given ID from the training data query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str example_id: The ID of the document as it is indexed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')
        if example_id is None:
            raise ValueError('example_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_training_example')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id,
                                    example_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_training_example(self,
                                environment_id: str,
                                collection_id: str,
                                query_id: str,
                                example_id: str,
                                *,
                                cross_reference: str = None,
                                relevance: int = None,
                                **kwargs) -> 'DetailedResponse':
        """
        Change label or cross reference for example.

        Changes the label or cross reference query for this training data example.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str example_id: The ID of the document as it is indexed.
        :param str cross_reference: (optional) The example to add.
        :param int relevance: (optional) The relevance value for this example.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')
        if example_id is None:
            raise ValueError('example_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_training_example')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'cross_reference': cross_reference, 'relevance': relevance}

        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id,
                                    example_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def get_training_example(self, environment_id: str, collection_id: str,
                             query_id: str, example_id: str,
                             **kwargs) -> 'DetailedResponse':
        """
        Get details for training data example.

        Gets the details for this training example.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str example_id: The ID of the document as it is indexed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')
        if example_id is None:
            raise ValueError('example_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_training_example')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id,
                                    example_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(self, customer_id: str,
                         **kwargs) -> 'DetailedResponse':
        """
        Delete labeled data.

        Deletes all data associated with a specified customer ID. The method has no effect
        if no data is associated with the customer ID.
        You associate a customer ID with data by passing the **X-Watson-Metadata** header
        with a request that passes data. For more information about personal data and
        customer IDs, see [Information
        security](https://cloud.ibm.com/docs/discovery?topic=discovery-information-security#information-security).

        :param str customer_id: The customer ID for which all data is to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customer_id is None:
            raise ValueError('customer_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_user_data')
        headers.update(sdk_headers)

        params = {'version': self.version, 'customer_id': customer_id}

        url = '/v1/user_data'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Events and feedback
    #########################

    def create_event(self, type: str, data: 'EventData',
                     **kwargs) -> 'DetailedResponse':
        """
        Create event.

        The **Events** API can be used to create log entries that are associated with
        specific queries. For example, you can record which documents in the results set
        were "clicked" by a user and when that click occurred.

        :param str type: The event type to be created.
        :param EventData data: Query event data object.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if type is None:
            raise ValueError('type must be provided')
        if data is None:
            raise ValueError('data must be provided')
        data = self._convert_model(data)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_event')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'type': type, 'data': data}

        url = '/v1/events'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def query_log(self,
                  *,
                  filter: str = None,
                  query: str = None,
                  count: int = None,
                  offset: int = None,
                  sort: List[str] = None,
                  **kwargs) -> 'DetailedResponse':
        """
        Search the query and event log.

        Searches the query and event log to find query sessions that match the specified
        criteria. Searching the **logs** endpoint uses the standard Discovery query syntax
        for the parameters that are supported.

        :param str filter: (optional) A cacheable query that excludes documents
               that don't mention the query content. Filter searches are better for
               metadata-type searches and for assessing the concepts in the data set.
        :param str query: (optional) A query search returns all documents in your
               data set with full enrichments and full text, but with the most relevant
               documents listed first.
        :param int count: (optional) Number of results to return. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param List[str] sort: (optional) A comma-separated list of fields in the
               document to sort on. You can optionally specify a sort direction by
               prefixing the field with `-` for descending or `+` for ascending. Ascending
               is the default sort direction if no prefix is specified.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='query_log')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'filter': filter,
            'query': query,
            'count': count,
            'offset': offset,
            'sort': self._convert_list(sort)
        }

        url = '/v1/logs'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_metrics_query(self,
                          *,
                          start_time: datetime = None,
                          end_time: datetime = None,
                          result_type: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Number of queries over time.

        Total number of queries using the **natural_language_query** parameter over a
        specific time window.

        :param datetime start_time: (optional) Metric is computed from data
               recorded after this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param datetime end_time: (optional) Metric is computed from data recorded
               before this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param str result_type: (optional) The type of result to consider when
               calculating the metric.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_metrics_query')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'start_time': start_time,
            'end_time': end_time,
            'result_type': result_type
        }

        url = '/v1/metrics/number_of_queries'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_metrics_query_event(self,
                                *,
                                start_time: datetime = None,
                                end_time: datetime = None,
                                result_type: str = None,
                                **kwargs) -> 'DetailedResponse':
        """
        Number of queries with an event over time.

        Total number of queries using the **natural_language_query** parameter that have a
        corresponding "click" event over a specified time window. This metric requires
        having integrated event tracking in your application using the **Events** API.

        :param datetime start_time: (optional) Metric is computed from data
               recorded after this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param datetime end_time: (optional) Metric is computed from data recorded
               before this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param str result_type: (optional) The type of result to consider when
               calculating the metric.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_metrics_query_event')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'start_time': start_time,
            'end_time': end_time,
            'result_type': result_type
        }

        url = '/v1/metrics/number_of_queries_with_event'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_metrics_query_no_results(self,
                                     *,
                                     start_time: datetime = None,
                                     end_time: datetime = None,
                                     result_type: str = None,
                                     **kwargs) -> 'DetailedResponse':
        """
        Number of queries with no search results over time.

        Total number of queries using the **natural_language_query** parameter that have
        no results returned over a specified time window.

        :param datetime start_time: (optional) Metric is computed from data
               recorded after this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param datetime end_time: (optional) Metric is computed from data recorded
               before this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param str result_type: (optional) The type of result to consider when
               calculating the metric.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_metrics_query_no_results')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'start_time': start_time,
            'end_time': end_time,
            'result_type': result_type
        }

        url = '/v1/metrics/number_of_queries_with_no_search_results'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_metrics_event_rate(self,
                               *,
                               start_time: datetime = None,
                               end_time: datetime = None,
                               result_type: str = None,
                               **kwargs) -> 'DetailedResponse':
        """
        Percentage of queries with an associated event.

        The percentage of queries using the **natural_language_query** parameter that have
        a corresponding "click" event over a specified time window.  This metric requires
        having integrated event tracking in your application using the **Events** API.

        :param datetime start_time: (optional) Metric is computed from data
               recorded after this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param datetime end_time: (optional) Metric is computed from data recorded
               before this timestamp; must be in `YYYY-MM-DDThh:mm:ssZ` format.
        :param str result_type: (optional) The type of result to consider when
               calculating the metric.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_metrics_event_rate')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'start_time': start_time,
            'end_time': end_time,
            'result_type': result_type
        }

        url = '/v1/metrics/event_rate'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_metrics_query_token_event(self,
                                      *,
                                      count: int = None,
                                      **kwargs) -> 'DetailedResponse':
        """
        Most frequent query tokens with an event.

        The most frequent query tokens parsed from the **natural_language_query**
        parameter and their corresponding "click" event rate within the recording period
        (queries and events are stored for 30 days). A query token is an individual word
        or unigram within the query string.

        :param int count: (optional) Number of results to return. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_metrics_query_token_event')
        headers.update(sdk_headers)

        params = {'version': self.version, 'count': count}

        url = '/v1/metrics/top_query_tokens_with_event_rate'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Credentials
    #########################

    def list_credentials(self, environment_id: str,
                         **kwargs) -> 'DetailedResponse':
        """
        List credentials.

        List all the source credentials that have been created for this service instance.
         **Note:**  All credentials are sent over an encrypted connection and encrypted at
        rest.

        :param str environment_id: The ID of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_credentials')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/credentials'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def create_credentials(self,
                           environment_id: str,
                           *,
                           source_type: str = None,
                           credential_details: 'CredentialDetails' = None,
                           status: str = None,
                           **kwargs) -> 'DetailedResponse':
        """
        Create credentials.

        Creates a set of credentials to connect to a remote source. Created credentials
        are used in a configuration to associate a collection with the remote source.
        **Note:** All credentials are sent over an encrypted connection and encrypted at
        rest.

        :param str environment_id: The ID of the environment.
        :param str source_type: (optional) The source that this credentials object
               connects to.
               -  `box` indicates the credentials are used to connect an instance of
               Enterprise Box.
               -  `salesforce` indicates the credentials are used to connect to
               Salesforce.
               -  `sharepoint` indicates the credentials are used to connect to Microsoft
               SharePoint Online.
               -  `web_crawl` indicates the credentials are used to perform a web crawl.
               =  `cloud_object_storage` indicates the credentials are used to connect to
               an IBM Cloud Object Store.
        :param CredentialDetails credential_details: (optional) Object containing
               details of the stored credentials.
               Obtain credentials for your source from the administrator of the source.
        :param str status: (optional) The current status of this set of
               credentials. `connected` indicates that the credentials are available to
               use with the source configuration of a collection. `invalid` refers to the
               credentials (for example, the password provided has expired) and must be
               corrected before they can be used with a collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if credential_details is not None:
            credential_details = self._convert_model(credential_details)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_credentials')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'source_type': source_type,
            'credential_details': credential_details,
            'status': status
        }

        url = '/v1/environments/{0}/credentials'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def get_credentials(self, environment_id: str, credential_id: str,
                        **kwargs) -> 'DetailedResponse':
        """
        View Credentials.

        Returns details about the specified credentials.
         **Note:** Secure credential information such as a password or SSH key is never
        returned and must be obtained from the source system.

        :param str environment_id: The ID of the environment.
        :param str credential_id: The unique identifier for a set of source
               credentials.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if credential_id is None:
            raise ValueError('credential_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_credentials')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/credentials/{1}'.format(
            *self._encode_path_vars(environment_id, credential_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_credentials(self,
                           environment_id: str,
                           credential_id: str,
                           *,
                           source_type: str = None,
                           credential_details: 'CredentialDetails' = None,
                           status: str = None,
                           **kwargs) -> 'DetailedResponse':
        """
        Update credentials.

        Updates an existing set of source credentials.
        **Note:** All credentials are sent over an encrypted connection and encrypted at
        rest.

        :param str environment_id: The ID of the environment.
        :param str credential_id: The unique identifier for a set of source
               credentials.
        :param str source_type: (optional) The source that this credentials object
               connects to.
               -  `box` indicates the credentials are used to connect an instance of
               Enterprise Box.
               -  `salesforce` indicates the credentials are used to connect to
               Salesforce.
               -  `sharepoint` indicates the credentials are used to connect to Microsoft
               SharePoint Online.
               -  `web_crawl` indicates the credentials are used to perform a web crawl.
               =  `cloud_object_storage` indicates the credentials are used to connect to
               an IBM Cloud Object Store.
        :param CredentialDetails credential_details: (optional) Object containing
               details of the stored credentials.
               Obtain credentials for your source from the administrator of the source.
        :param str status: (optional) The current status of this set of
               credentials. `connected` indicates that the credentials are available to
               use with the source configuration of a collection. `invalid` refers to the
               credentials (for example, the password provided has expired) and must be
               corrected before they can be used with a collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if credential_id is None:
            raise ValueError('credential_id must be provided')
        if credential_details is not None:
            credential_details = self._convert_model(credential_details)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_credentials')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'source_type': source_type,
            'credential_details': credential_details,
            'status': status
        }

        url = '/v1/environments/{0}/credentials/{1}'.format(
            *self._encode_path_vars(environment_id, credential_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_credentials(self, environment_id: str, credential_id: str,
                           **kwargs) -> 'DetailedResponse':
        """
        Delete credentials.

        Deletes a set of stored credentials from your Discovery instance.

        :param str environment_id: The ID of the environment.
        :param str credential_id: The unique identifier for a set of source
               credentials.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if credential_id is None:
            raise ValueError('credential_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_credentials')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/credentials/{1}'.format(
            *self._encode_path_vars(environment_id, credential_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # gatewayConfiguration
    #########################

    def list_gateways(self, environment_id: str,
                      **kwargs) -> 'DetailedResponse':
        """
        List Gateways.

        List the currently configured gateways.

        :param str environment_id: The ID of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_gateways')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/gateways'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def create_gateway(self,
                       environment_id: str,
                       *,
                       name: str = None,
                       **kwargs) -> 'DetailedResponse':
        """
        Create Gateway.

        Create a gateway configuration to use with a remotely installed gateway.

        :param str environment_id: The ID of the environment.
        :param str name: (optional) User-defined name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_gateway')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'name': name}

        url = '/v1/environments/{0}/gateways'.format(
            *self._encode_path_vars(environment_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def get_gateway(self, environment_id: str, gateway_id: str,
                    **kwargs) -> 'DetailedResponse':
        """
        List Gateway Details.

        List information about the specified gateway.

        :param str environment_id: The ID of the environment.
        :param str gateway_id: The requested gateway ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if gateway_id is None:
            raise ValueError('gateway_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_gateway')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/gateways/{1}'.format(
            *self._encode_path_vars(environment_id, gateway_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def delete_gateway(self, environment_id: str, gateway_id: str,
                       **kwargs) -> 'DetailedResponse':
        """
        Delete Gateway.

        Delete the specified gateway configuration.

        :param str environment_id: The ID of the environment.
        :param str gateway_id: The requested gateway ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if gateway_id is None:
            raise ValueError('gateway_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_gateway')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/environments/{0}/gateways/{1}'.format(
            *self._encode_path_vars(environment_id, gateway_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class AddDocumentEnums(object):

    class FileContentType(Enum):
        """
        The content type of file.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        APPLICATION_PDF = 'application/pdf'
        TEXT_HTML = 'text/html'
        APPLICATION_XHTML_XML = 'application/xhtml+xml'


class UpdateDocumentEnums(object):

    class FileContentType(Enum):
        """
        The content type of file.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        APPLICATION_PDF = 'application/pdf'
        TEXT_HTML = 'text/html'
        APPLICATION_XHTML_XML = 'application/xhtml+xml'


class GetMetricsQueryEnums(object):

    class ResultType(Enum):
        """
        The type of result to consider when calculating the metric.
        """
        DOCUMENT = 'document'


class GetMetricsQueryEventEnums(object):

    class ResultType(Enum):
        """
        The type of result to consider when calculating the metric.
        """
        DOCUMENT = 'document'


class GetMetricsQueryNoResultsEnums(object):

    class ResultType(Enum):
        """
        The type of result to consider when calculating the metric.
        """
        DOCUMENT = 'document'


class GetMetricsEventRateEnums(object):

    class ResultType(Enum):
        """
        The type of result to consider when calculating the metric.
        """
        DOCUMENT = 'document'


##############################################################################
# Models
##############################################################################


class AggregationResult():
    """
    Aggregation results for the specified query.

    :attr str key: (optional) Key that matched the aggregation type.
    :attr int matching_results: (optional) Number of matching results.
    :attr List[QueryAggregation] aggregations: (optional) Aggregations returned in
          the case of chained aggregations.
    """

    def __init__(self,
                 *,
                 key: str = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None) -> None:
        """
        Initialize a AggregationResult object.

        :param str key: (optional) Key that matched the aggregation type.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned in the case of chained aggregations.
        """
        self.key = key
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AggregationResult':
        """Initialize a AggregationResult object from a json dictionary."""
        args = {}
        valid_keys = ['key', 'matching_results', 'aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AggregationResult: '
                + ', '.join(bad_keys))
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'AggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Collection():
    """
    A collection for storing documents.

    :attr str collection_id: (optional) The unique identifier of the collection.
    :attr str name: (optional) The name of the collection.
    :attr str description: (optional) The description of the collection.
    :attr datetime created: (optional) The creation date of the collection in the
          format yyyy-MM-dd'T'HH:mmcon:ss.SSS'Z'.
    :attr datetime updated: (optional) The timestamp of when the collection was last
          updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str status: (optional) The status of the collection.
    :attr str configuration_id: (optional) The unique identifier of the collection's
          configuration.
    :attr str language: (optional) The language of the documents stored in the
          collection. Permitted values include `en` (English), `de` (German), and `es`
          (Spanish).
    :attr DocumentCounts document_counts: (optional) Object containing collection
          document count information.
    :attr CollectionDiskUsage disk_usage: (optional) Summary of the disk usage
          statistics for this collection.
    :attr TrainingStatus training_status: (optional) Training status details.
    :attr CollectionCrawlStatus crawl_status: (optional) Object containing
          information about the crawl status of this collection.
    :attr SduStatus smart_document_understanding: (optional) Object containing smart
          document understanding information for this collection.
    """

    def __init__(self,
                 *,
                 collection_id: str = None,
                 name: str = None,
                 description: str = None,
                 created: datetime = None,
                 updated: datetime = None,
                 status: str = None,
                 configuration_id: str = None,
                 language: str = None,
                 document_counts: 'DocumentCounts' = None,
                 disk_usage: 'CollectionDiskUsage' = None,
                 training_status: 'TrainingStatus' = None,
                 crawl_status: 'CollectionCrawlStatus' = None,
                 smart_document_understanding: 'SduStatus' = None) -> None:
        """
        Initialize a Collection object.

        :param str collection_id: (optional) The unique identifier of the
               collection.
        :param str name: (optional) The name of the collection.
        :param str description: (optional) The description of the collection.
        :param datetime created: (optional) The creation date of the collection in
               the format yyyy-MM-dd'T'HH:mmcon:ss.SSS'Z'.
        :param datetime updated: (optional) The timestamp of when the collection
               was last updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str status: (optional) The status of the collection.
        :param str configuration_id: (optional) The unique identifier of the
               collection's configuration.
        :param str language: (optional) The language of the documents stored in the
               collection. Permitted values include `en` (English), `de` (German), and
               `es` (Spanish).
        :param DocumentCounts document_counts: (optional) Object containing
               collection document count information.
        :param CollectionDiskUsage disk_usage: (optional) Summary of the disk usage
               statistics for this collection.
        :param TrainingStatus training_status: (optional) Training status details.
        :param CollectionCrawlStatus crawl_status: (optional) Object containing
               information about the crawl status of this collection.
        :param SduStatus smart_document_understanding: (optional) Object containing
               smart document understanding information for this collection.
        """
        self.collection_id = collection_id
        self.name = name
        self.description = description
        self.created = created
        self.updated = updated
        self.status = status
        self.configuration_id = configuration_id
        self.language = language
        self.document_counts = document_counts
        self.disk_usage = disk_usage
        self.training_status = training_status
        self.crawl_status = crawl_status
        self.smart_document_understanding = smart_document_understanding

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Collection':
        """Initialize a Collection object from a json dictionary."""
        args = {}
        valid_keys = [
            'collection_id', 'name', 'description', 'created', 'updated',
            'status', 'configuration_id', 'language', 'document_counts',
            'disk_usage', 'training_status', 'crawl_status',
            'smart_document_understanding'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Collection: '
                + ', '.join(bad_keys))
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'configuration_id' in _dict:
            args['configuration_id'] = _dict.get('configuration_id')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'document_counts' in _dict:
            args['document_counts'] = DocumentCounts._from_dict(
                _dict.get('document_counts'))
        if 'disk_usage' in _dict:
            args['disk_usage'] = CollectionDiskUsage._from_dict(
                _dict.get('disk_usage'))
        if 'training_status' in _dict:
            args['training_status'] = TrainingStatus._from_dict(
                _dict.get('training_status'))
        if 'crawl_status' in _dict:
            args['crawl_status'] = CollectionCrawlStatus._from_dict(
                _dict.get('crawl_status'))
        if 'smart_document_understanding' in _dict:
            args['smart_document_understanding'] = SduStatus._from_dict(
                _dict.get('smart_document_understanding'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Collection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self,
                   'configuration_id') and self.configuration_id is not None:
            _dict['configuration_id'] = self.configuration_id
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self,
                   'document_counts') and self.document_counts is not None:
            _dict['document_counts'] = self.document_counts._to_dict()
        if hasattr(self, 'disk_usage') and self.disk_usage is not None:
            _dict['disk_usage'] = self.disk_usage._to_dict()
        if hasattr(self,
                   'training_status') and self.training_status is not None:
            _dict['training_status'] = self.training_status._to_dict()
        if hasattr(self, 'crawl_status') and self.crawl_status is not None:
            _dict['crawl_status'] = self.crawl_status._to_dict()
        if hasattr(self, 'smart_document_understanding'
                  ) and self.smart_document_understanding is not None:
            _dict[
                'smart_document_understanding'] = self.smart_document_understanding._to_dict(
                )
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Collection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Collection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Collection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        The status of the collection.
        """
        ACTIVE = "active"
        PENDING = "pending"
        MAINTENANCE = "maintenance"


class CollectionCrawlStatus():
    """
    Object containing information about the crawl status of this collection.

    :attr SourceStatus source_crawl: (optional) Object containing source crawl
          status information.
    """

    def __init__(self, *, source_crawl: 'SourceStatus' = None) -> None:
        """
        Initialize a CollectionCrawlStatus object.

        :param SourceStatus source_crawl: (optional) Object containing source crawl
               status information.
        """
        self.source_crawl = source_crawl

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionCrawlStatus':
        """Initialize a CollectionCrawlStatus object from a json dictionary."""
        args = {}
        valid_keys = ['source_crawl']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CollectionCrawlStatus: '
                + ', '.join(bad_keys))
        if 'source_crawl' in _dict:
            args['source_crawl'] = SourceStatus._from_dict(
                _dict.get('source_crawl'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionCrawlStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source_crawl') and self.source_crawl is not None:
            _dict['source_crawl'] = self.source_crawl._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionCrawlStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CollectionCrawlStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionCrawlStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionDiskUsage():
    """
    Summary of the disk usage statistics for this collection.

    :attr int used_bytes: (optional) Number of bytes used by the collection.
    """

    def __init__(self, *, used_bytes: int = None) -> None:
        """
        Initialize a CollectionDiskUsage object.

        :param int used_bytes: (optional) Number of bytes used by the collection.
        """
        self.used_bytes = used_bytes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionDiskUsage':
        """Initialize a CollectionDiskUsage object from a json dictionary."""
        args = {}
        valid_keys = ['used_bytes']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CollectionDiskUsage: '
                + ', '.join(bad_keys))
        if 'used_bytes' in _dict:
            args['used_bytes'] = _dict.get('used_bytes')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionDiskUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'used_bytes') and self.used_bytes is not None:
            _dict['used_bytes'] = self.used_bytes
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionDiskUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CollectionDiskUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionDiskUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionUsage():
    """
    Summary of the collection usage in the environment.

    :attr int available: (optional) Number of active collections in the environment.
    :attr int maximum_allowed: (optional) Total number of collections allowed in the
          environment.
    """

    def __init__(self,
                 *,
                 available: int = None,
                 maximum_allowed: int = None) -> None:
        """
        Initialize a CollectionUsage object.

        :param int available: (optional) Number of active collections in the
               environment.
        :param int maximum_allowed: (optional) Total number of collections allowed
               in the environment.
        """
        self.available = available
        self.maximum_allowed = maximum_allowed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionUsage':
        """Initialize a CollectionUsage object from a json dictionary."""
        args = {}
        valid_keys = ['available', 'maximum_allowed']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CollectionUsage: '
                + ', '.join(bad_keys))
        if 'available' in _dict:
            args['available'] = _dict.get('available')
        if 'maximum_allowed' in _dict:
            args['maximum_allowed'] = _dict.get('maximum_allowed')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'available') and self.available is not None:
            _dict['available'] = self.available
        if hasattr(self,
                   'maximum_allowed') and self.maximum_allowed is not None:
            _dict['maximum_allowed'] = self.maximum_allowed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CollectionUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Completions():
    """
    An object containing an array of autocompletion suggestions.

    :attr List[str] completions: (optional) Array of autcomplete suggestion based on
          the provided prefix.
    """

    def __init__(self, *, completions: List[str] = None) -> None:
        """
        Initialize a Completions object.

        :param List[str] completions: (optional) Array of autcomplete suggestion
               based on the provided prefix.
        """
        self.completions = completions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Completions':
        """Initialize a Completions object from a json dictionary."""
        args = {}
        valid_keys = ['completions']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Completions: '
                + ', '.join(bad_keys))
        if 'completions' in _dict:
            args['completions'] = _dict.get('completions')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Completions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'completions') and self.completions is not None:
            _dict['completions'] = self.completions
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Completions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Completions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Completions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Configuration():
    """
    A custom configuration for the environment.

    :attr str configuration_id: (optional) The unique identifier of the
          configuration.
    :attr str name: The name of the configuration.
    :attr datetime created: (optional) The creation date of the configuration in the
          format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr datetime updated: (optional) The timestamp of when the configuration was
          last updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str description: (optional) The description of the configuration, if
          available.
    :attr Conversions conversions: (optional) Document conversion settings.
    :attr List[Enrichment] enrichments: (optional) An array of document enrichment
          settings for the configuration.
    :attr List[NormalizationOperation] normalizations: (optional) Defines operations
          that can be used to transform the final output JSON into a normalized form.
          Operations are executed in the order that they appear in the array.
    :attr Source source: (optional) Object containing source parameters for the
          configuration.
    """

    def __init__(self,
                 name: str,
                 *,
                 configuration_id: str = None,
                 created: datetime = None,
                 updated: datetime = None,
                 description: str = None,
                 conversions: 'Conversions' = None,
                 enrichments: List['Enrichment'] = None,
                 normalizations: List['NormalizationOperation'] = None,
                 source: 'Source' = None) -> None:
        """
        Initialize a Configuration object.

        :param str name: The name of the configuration.
        :param str configuration_id: (optional) The unique identifier of the
               configuration.
        :param datetime created: (optional) The creation date of the configuration
               in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param datetime updated: (optional) The timestamp of when the configuration
               was last updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str description: (optional) The description of the configuration, if
               available.
        :param Conversions conversions: (optional) Document conversion settings.
        :param List[Enrichment] enrichments: (optional) An array of document
               enrichment settings for the configuration.
        :param List[NormalizationOperation] normalizations: (optional) Defines
               operations that can be used to transform the final output JSON into a
               normalized form. Operations are executed in the order that they appear in
               the array.
        :param Source source: (optional) Object containing source parameters for
               the configuration.
        """
        self.configuration_id = configuration_id
        self.name = name
        self.created = created
        self.updated = updated
        self.description = description
        self.conversions = conversions
        self.enrichments = enrichments
        self.normalizations = normalizations
        self.source = source

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Configuration':
        """Initialize a Configuration object from a json dictionary."""
        args = {}
        valid_keys = [
            'configuration_id', 'name', 'created', 'updated', 'description',
            'conversions', 'enrichments', 'normalizations', 'source'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Configuration: '
                + ', '.join(bad_keys))
        if 'configuration_id' in _dict:
            args['configuration_id'] = _dict.get('configuration_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Configuration JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'conversions' in _dict:
            args['conversions'] = Conversions._from_dict(
                _dict.get('conversions'))
        if 'enrichments' in _dict:
            args['enrichments'] = [
                Enrichment._from_dict(x) for x in (_dict.get('enrichments'))
            ]
        if 'normalizations' in _dict:
            args['normalizations'] = [
                NormalizationOperation._from_dict(x)
                for x in (_dict.get('normalizations'))
            ]
        if 'source' in _dict:
            args['source'] = Source._from_dict(_dict.get('source'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Configuration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'configuration_id') and self.configuration_id is not None:
            _dict['configuration_id'] = self.configuration_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'conversions') and self.conversions is not None:
            _dict['conversions'] = self.conversions._to_dict()
        if hasattr(self, 'enrichments') and self.enrichments is not None:
            _dict['enrichments'] = [x._to_dict() for x in self.enrichments]
        if hasattr(self, 'normalizations') and self.normalizations is not None:
            _dict['normalizations'] = [
                x._to_dict() for x in self.normalizations
            ]
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Configuration object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Configuration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Configuration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Conversions():
    """
    Document conversion settings.

    :attr PdfSettings pdf: (optional) A list of PDF conversion settings.
    :attr WordSettings word: (optional) A list of Word conversion settings.
    :attr HtmlSettings html: (optional) A list of HTML conversion settings.
    :attr SegmentSettings segment: (optional) A list of Document Segmentation
          settings.
    :attr List[NormalizationOperation] json_normalizations: (optional) Defines
          operations that can be used to transform the final output JSON into a normalized
          form. Operations are executed in the order that they appear in the array.
    :attr bool image_text_recognition: (optional) When `true`, automatic text
          extraction from images (this includes images embedded in supported document
          formats, for example PDF, and suppported image formats, for example TIFF) is
          performed on documents uploaded to the collection. This field is supported on
          **Advanced** and higher plans only. **Lite** plans do not support image text
          recognition.
    """

    def __init__(self,
                 *,
                 pdf: 'PdfSettings' = None,
                 word: 'WordSettings' = None,
                 html: 'HtmlSettings' = None,
                 segment: 'SegmentSettings' = None,
                 json_normalizations: List['NormalizationOperation'] = None,
                 image_text_recognition: bool = None) -> None:
        """
        Initialize a Conversions object.

        :param PdfSettings pdf: (optional) A list of PDF conversion settings.
        :param WordSettings word: (optional) A list of Word conversion settings.
        :param HtmlSettings html: (optional) A list of HTML conversion settings.
        :param SegmentSettings segment: (optional) A list of Document Segmentation
               settings.
        :param List[NormalizationOperation] json_normalizations: (optional) Defines
               operations that can be used to transform the final output JSON into a
               normalized form. Operations are executed in the order that they appear in
               the array.
        :param bool image_text_recognition: (optional) When `true`, automatic text
               extraction from images (this includes images embedded in supported document
               formats, for example PDF, and suppported image formats, for example TIFF)
               is performed on documents uploaded to the collection. This field is
               supported on **Advanced** and higher plans only. **Lite** plans do not
               support image text recognition.
        """
        self.pdf = pdf
        self.word = word
        self.html = html
        self.segment = segment
        self.json_normalizations = json_normalizations
        self.image_text_recognition = image_text_recognition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Conversions':
        """Initialize a Conversions object from a json dictionary."""
        args = {}
        valid_keys = [
            'pdf', 'word', 'html', 'segment', 'json_normalizations',
            'image_text_recognition'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Conversions: '
                + ', '.join(bad_keys))
        if 'pdf' in _dict:
            args['pdf'] = PdfSettings._from_dict(_dict.get('pdf'))
        if 'word' in _dict:
            args['word'] = WordSettings._from_dict(_dict.get('word'))
        if 'html' in _dict:
            args['html'] = HtmlSettings._from_dict(_dict.get('html'))
        if 'segment' in _dict:
            args['segment'] = SegmentSettings._from_dict(_dict.get('segment'))
        if 'json_normalizations' in _dict:
            args['json_normalizations'] = [
                NormalizationOperation._from_dict(x)
                for x in (_dict.get('json_normalizations'))
            ]
        if 'image_text_recognition' in _dict:
            args['image_text_recognition'] = _dict.get('image_text_recognition')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Conversions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pdf') and self.pdf is not None:
            _dict['pdf'] = self.pdf._to_dict()
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word._to_dict()
        if hasattr(self, 'html') and self.html is not None:
            _dict['html'] = self.html._to_dict()
        if hasattr(self, 'segment') and self.segment is not None:
            _dict['segment'] = self.segment._to_dict()
        if hasattr(
                self,
                'json_normalizations') and self.json_normalizations is not None:
            _dict['json_normalizations'] = [
                x._to_dict() for x in self.json_normalizations
            ]
        if hasattr(self, 'image_text_recognition'
                  ) and self.image_text_recognition is not None:
            _dict['image_text_recognition'] = self.image_text_recognition
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Conversions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Conversions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Conversions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateEventResponse():
    """
    An object defining the event being created.

    :attr str type: (optional) The event type that was created.
    :attr EventData data: (optional) Query event data object.
    """

    def __init__(self, *, type: str = None, data: 'EventData' = None) -> None:
        """
        Initialize a CreateEventResponse object.

        :param str type: (optional) The event type that was created.
        :param EventData data: (optional) Query event data object.
        """
        self.type = type
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateEventResponse':
        """Initialize a CreateEventResponse object from a json dictionary."""
        args = {}
        valid_keys = ['type', 'data']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CreateEventResponse: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'data' in _dict:
            args['data'] = EventData._from_dict(_dict.get('data'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateEventResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateEventResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CreateEventResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateEventResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        The event type that was created.
        """
        CLICK = "click"


class CredentialDetails():
    """
    Object containing details of the stored credentials.
    Obtain credentials for your source from the administrator of the source.

    :attr str credential_type: (optional) The authentication method for this
          credentials definition. The  **credential_type** specified must be supported by
          the **source_type**. The following combinations are possible:
          -  `"source_type": "box"` - valid `credential_type`s: `oauth2`
          -  `"source_type": "salesforce"` - valid `credential_type`s: `username_password`
          -  `"source_type": "sharepoint"` - valid `credential_type`s: `saml` with
          **source_version** of `online`, or `ntlm_v1` with **source_version** of `2016`
          -  `"source_type": "web_crawl"` - valid `credential_type`s: `noauth` or `basic`
          -  "source_type": "cloud_object_storage"` - valid `credential_type`s:
          `aws4_hmac`.
    :attr str client_id: (optional) The **client_id** of the source that these
          credentials connect to. Only valid, and required, with a **credential_type** of
          `oauth2`.
    :attr str enterprise_id: (optional) The **enterprise_id** of the Box site that
          these credentials connect to. Only valid, and required, with a **source_type**
          of `box`.
    :attr str url: (optional) The **url** of the source that these credentials
          connect to. Only valid, and required, with a **credential_type** of
          `username_password`, `noauth`, and `basic`.
    :attr str username: (optional) The **username** of the source that these
          credentials connect to. Only valid, and required, with a **credential_type** of
          `saml`, `username_password`, `basic`, or `ntlm_v1`.
    :attr str organization_url: (optional) The **organization_url** of the source
          that these credentials connect to. Only valid, and required, with a
          **credential_type** of `saml`.
    :attr str site_collection_path: (optional) The **site_collection.path** of the
          source that these credentials connect to. Only valid, and required, with a
          **source_type** of `sharepoint`.
    :attr str client_secret: (optional) The **client_secret** of the source that
          these credentials connect to. Only valid, and required, with a
          **credential_type** of `oauth2`. This value is never returned and is only used
          when creating or modifying **credentials**.
    :attr str public_key_id: (optional) The **public_key_id** of the source that
          these credentials connect to. Only valid, and required, with a
          **credential_type** of `oauth2`. This value is never returned and is only used
          when creating or modifying **credentials**.
    :attr str private_key: (optional) The **private_key** of the source that these
          credentials connect to. Only valid, and required, with a **credential_type** of
          `oauth2`. This value is never returned and is only used when creating or
          modifying **credentials**.
    :attr str passphrase: (optional) The **passphrase** of the source that these
          credentials connect to. Only valid, and required, with a **credential_type** of
          `oauth2`. This value is never returned and is only used when creating or
          modifying **credentials**.
    :attr str password: (optional) The **password** of the source that these
          credentials connect to. Only valid, and required, with **credential_type**s of
          `saml`, `username_password`, `basic`, or `ntlm_v1`.
          **Note:** When used with a **source_type** of `salesforce`, the password
          consists of the Salesforce password and a valid Salesforce security token
          concatenated. This value is never returned and is only used when creating or
          modifying **credentials**.
    :attr str gateway_id: (optional) The ID of the **gateway** to be connected
          through (when connecting to intranet sites). Only valid with a
          **credential_type** of `noauth`, `basic`, or `ntlm_v1`. Gateways are created
          using the `/v1/environments/{environment_id}/gateways` methods.
    :attr str source_version: (optional) The type of Sharepoint repository to
          connect to. Only valid, and required, with a **source_type** of `sharepoint`.
    :attr str web_application_url: (optional) SharePoint OnPrem WebApplication URL.
          Only valid, and required, with a **source_version** of `2016`. If a port is not
          supplied, the default to port `80` for http and port `443` for https connections
          are used.
    :attr str domain: (optional) The domain used to log in to your OnPrem SharePoint
          account. Only valid, and required, with a **source_version** of `2016`.
    :attr str endpoint: (optional) The endpoint associated with the cloud object
          store that your are connecting to. Only valid, and required, with a
          **credential_type** of `aws4_hmac`.
    :attr str access_key_id: (optional) The access key ID associated with the cloud
          object store. Only valid, and required, with a **credential_type** of
          `aws4_hmac`. This value is never returned and is only used when creating or
          modifying **credentials**. For more infomation, see the [cloud object store
          documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-using-hmac-credentials#using-hmac-credentials).
    :attr str secret_access_key: (optional) The secret access key associated with
          the cloud object store. Only valid, and required, with a **credential_type** of
          `aws4_hmac`. This value is never returned and is only used when creating or
          modifying **credentials**. For more infomation, see the [cloud object store
          documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-using-hmac-credentials#using-hmac-credentials).
    """

    def __init__(self,
                 *,
                 credential_type: str = None,
                 client_id: str = None,
                 enterprise_id: str = None,
                 url: str = None,
                 username: str = None,
                 organization_url: str = None,
                 site_collection_path: str = None,
                 client_secret: str = None,
                 public_key_id: str = None,
                 private_key: str = None,
                 passphrase: str = None,
                 password: str = None,
                 gateway_id: str = None,
                 source_version: str = None,
                 web_application_url: str = None,
                 domain: str = None,
                 endpoint: str = None,
                 access_key_id: str = None,
                 secret_access_key: str = None) -> None:
        """
        Initialize a CredentialDetails object.

        :param str credential_type: (optional) The authentication method for this
               credentials definition. The  **credential_type** specified must be
               supported by the **source_type**. The following combinations are possible:
               -  `"source_type": "box"` - valid `credential_type`s: `oauth2`
               -  `"source_type": "salesforce"` - valid `credential_type`s:
               `username_password`
               -  `"source_type": "sharepoint"` - valid `credential_type`s: `saml` with
               **source_version** of `online`, or `ntlm_v1` with **source_version** of
               `2016`
               -  `"source_type": "web_crawl"` - valid `credential_type`s: `noauth` or
               `basic`
               -  "source_type": "cloud_object_storage"` - valid `credential_type`s:
               `aws4_hmac`.
        :param str client_id: (optional) The **client_id** of the source that these
               credentials connect to. Only valid, and required, with a
               **credential_type** of `oauth2`.
        :param str enterprise_id: (optional) The **enterprise_id** of the Box site
               that these credentials connect to. Only valid, and required, with a
               **source_type** of `box`.
        :param str url: (optional) The **url** of the source that these credentials
               connect to. Only valid, and required, with a **credential_type** of
               `username_password`, `noauth`, and `basic`.
        :param str username: (optional) The **username** of the source that these
               credentials connect to. Only valid, and required, with a
               **credential_type** of `saml`, `username_password`, `basic`, or `ntlm_v1`.
        :param str organization_url: (optional) The **organization_url** of the
               source that these credentials connect to. Only valid, and required, with a
               **credential_type** of `saml`.
        :param str site_collection_path: (optional) The **site_collection.path** of
               the source that these credentials connect to. Only valid, and required,
               with a **source_type** of `sharepoint`.
        :param str client_secret: (optional) The **client_secret** of the source
               that these credentials connect to. Only valid, and required, with a
               **credential_type** of `oauth2`. This value is never returned and is only
               used when creating or modifying **credentials**.
        :param str public_key_id: (optional) The **public_key_id** of the source
               that these credentials connect to. Only valid, and required, with a
               **credential_type** of `oauth2`. This value is never returned and is only
               used when creating or modifying **credentials**.
        :param str private_key: (optional) The **private_key** of the source that
               these credentials connect to. Only valid, and required, with a
               **credential_type** of `oauth2`. This value is never returned and is only
               used when creating or modifying **credentials**.
        :param str passphrase: (optional) The **passphrase** of the source that
               these credentials connect to. Only valid, and required, with a
               **credential_type** of `oauth2`. This value is never returned and is only
               used when creating or modifying **credentials**.
        :param str password: (optional) The **password** of the source that these
               credentials connect to. Only valid, and required, with **credential_type**s
               of `saml`, `username_password`, `basic`, or `ntlm_v1`.
               **Note:** When used with a **source_type** of `salesforce`, the password
               consists of the Salesforce password and a valid Salesforce security token
               concatenated. This value is never returned and is only used when creating
               or modifying **credentials**.
        :param str gateway_id: (optional) The ID of the **gateway** to be connected
               through (when connecting to intranet sites). Only valid with a
               **credential_type** of `noauth`, `basic`, or `ntlm_v1`. Gateways are
               created using the `/v1/environments/{environment_id}/gateways` methods.
        :param str source_version: (optional) The type of Sharepoint repository to
               connect to. Only valid, and required, with a **source_type** of
               `sharepoint`.
        :param str web_application_url: (optional) SharePoint OnPrem WebApplication
               URL. Only valid, and required, with a **source_version** of `2016`. If a
               port is not supplied, the default to port `80` for http and port `443` for
               https connections are used.
        :param str domain: (optional) The domain used to log in to your OnPrem
               SharePoint account. Only valid, and required, with a **source_version** of
               `2016`.
        :param str endpoint: (optional) The endpoint associated with the cloud
               object store that your are connecting to. Only valid, and required, with a
               **credential_type** of `aws4_hmac`.
        :param str access_key_id: (optional) The access key ID associated with the
               cloud object store. Only valid, and required, with a **credential_type** of
               `aws4_hmac`. This value is never returned and is only used when creating or
               modifying **credentials**. For more infomation, see the [cloud object store
               documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-using-hmac-credentials#using-hmac-credentials).
        :param str secret_access_key: (optional) The secret access key associated
               with the cloud object store. Only valid, and required, with a
               **credential_type** of `aws4_hmac`. This value is never returned and is
               only used when creating or modifying **credentials**. For more infomation,
               see the [cloud object store
               documentation](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-using-hmac-credentials#using-hmac-credentials).
        """
        self.credential_type = credential_type
        self.client_id = client_id
        self.enterprise_id = enterprise_id
        self.url = url
        self.username = username
        self.organization_url = organization_url
        self.site_collection_path = site_collection_path
        self.client_secret = client_secret
        self.public_key_id = public_key_id
        self.private_key = private_key
        self.passphrase = passphrase
        self.password = password
        self.gateway_id = gateway_id
        self.source_version = source_version
        self.web_application_url = web_application_url
        self.domain = domain
        self.endpoint = endpoint
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CredentialDetails':
        """Initialize a CredentialDetails object from a json dictionary."""
        args = {}
        valid_keys = [
            'credential_type', 'client_id', 'enterprise_id', 'url', 'username',
            'organization_url', 'site_collection_path', 'site_collection.path',
            'client_secret', 'public_key_id', 'private_key', 'passphrase',
            'password', 'gateway_id', 'source_version', 'web_application_url',
            'domain', 'endpoint', 'access_key_id', 'secret_access_key'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CredentialDetails: '
                + ', '.join(bad_keys))
        if 'credential_type' in _dict:
            args['credential_type'] = _dict.get('credential_type')
        if 'client_id' in _dict:
            args['client_id'] = _dict.get('client_id')
        if 'enterprise_id' in _dict:
            args['enterprise_id'] = _dict.get('enterprise_id')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'organization_url' in _dict:
            args['organization_url'] = _dict.get('organization_url')
        if 'site_collection.path' in _dict:
            args['site_collection_path'] = _dict.get('site_collection.path')
        if 'client_secret' in _dict:
            args['client_secret'] = _dict.get('client_secret')
        if 'public_key_id' in _dict:
            args['public_key_id'] = _dict.get('public_key_id')
        if 'private_key' in _dict:
            args['private_key'] = _dict.get('private_key')
        if 'passphrase' in _dict:
            args['passphrase'] = _dict.get('passphrase')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        if 'gateway_id' in _dict:
            args['gateway_id'] = _dict.get('gateway_id')
        if 'source_version' in _dict:
            args['source_version'] = _dict.get('source_version')
        if 'web_application_url' in _dict:
            args['web_application_url'] = _dict.get('web_application_url')
        if 'domain' in _dict:
            args['domain'] = _dict.get('domain')
        if 'endpoint' in _dict:
            args['endpoint'] = _dict.get('endpoint')
        if 'access_key_id' in _dict:
            args['access_key_id'] = _dict.get('access_key_id')
        if 'secret_access_key' in _dict:
            args['secret_access_key'] = _dict.get('secret_access_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CredentialDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'credential_type') and self.credential_type is not None:
            _dict['credential_type'] = self.credential_type
        if hasattr(self, 'client_id') and self.client_id is not None:
            _dict['client_id'] = self.client_id
        if hasattr(self, 'enterprise_id') and self.enterprise_id is not None:
            _dict['enterprise_id'] = self.enterprise_id
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self,
                   'organization_url') and self.organization_url is not None:
            _dict['organization_url'] = self.organization_url
        if hasattr(self, 'site_collection_path'
                  ) and self.site_collection_path is not None:
            _dict['site_collection.path'] = self.site_collection_path
        if hasattr(self, 'client_secret') and self.client_secret is not None:
            _dict['client_secret'] = self.client_secret
        if hasattr(self, 'public_key_id') and self.public_key_id is not None:
            _dict['public_key_id'] = self.public_key_id
        if hasattr(self, 'private_key') and self.private_key is not None:
            _dict['private_key'] = self.private_key
        if hasattr(self, 'passphrase') and self.passphrase is not None:
            _dict['passphrase'] = self.passphrase
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        if hasattr(self, 'gateway_id') and self.gateway_id is not None:
            _dict['gateway_id'] = self.gateway_id
        if hasattr(self, 'source_version') and self.source_version is not None:
            _dict['source_version'] = self.source_version
        if hasattr(
                self,
                'web_application_url') and self.web_application_url is not None:
            _dict['web_application_url'] = self.web_application_url
        if hasattr(self, 'domain') and self.domain is not None:
            _dict['domain'] = self.domain
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        if hasattr(self, 'access_key_id') and self.access_key_id is not None:
            _dict['access_key_id'] = self.access_key_id
        if hasattr(self,
                   'secret_access_key') and self.secret_access_key is not None:
            _dict['secret_access_key'] = self.secret_access_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CredentialDetails object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CredentialDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CredentialDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CredentialTypeEnum(Enum):
        """
        The authentication method for this credentials definition. The
        **credential_type** specified must be supported by the **source_type**. The
        following combinations are possible:
        -  `"source_type": "box"` - valid `credential_type`s: `oauth2`
        -  `"source_type": "salesforce"` - valid `credential_type`s: `username_password`
        -  `"source_type": "sharepoint"` - valid `credential_type`s: `saml` with
        **source_version** of `online`, or `ntlm_v1` with **source_version** of `2016`
        -  `"source_type": "web_crawl"` - valid `credential_type`s: `noauth` or `basic`
        -  "source_type": "cloud_object_storage"` - valid `credential_type`s: `aws4_hmac`.
        """
        OAUTH2 = "oauth2"
        SAML = "saml"
        USERNAME_PASSWORD = "username_password"
        NOAUTH = "noauth"
        BASIC = "basic"
        NTLM_V1 = "ntlm_v1"
        AWS4_HMAC = "aws4_hmac"

    class SourceVersionEnum(Enum):
        """
        The type of Sharepoint repository to connect to. Only valid, and required, with a
        **source_type** of `sharepoint`.
        """
        ONLINE = "online"


class Credentials():
    """
    Object containing credential information.

    :attr str credential_id: (optional) Unique identifier for this set of
          credentials.
    :attr str source_type: (optional) The source that this credentials object
          connects to.
          -  `box` indicates the credentials are used to connect an instance of Enterprise
          Box.
          -  `salesforce` indicates the credentials are used to connect to Salesforce.
          -  `sharepoint` indicates the credentials are used to connect to Microsoft
          SharePoint Online.
          -  `web_crawl` indicates the credentials are used to perform a web crawl.
          =  `cloud_object_storage` indicates the credentials are used to connect to an
          IBM Cloud Object Store.
    :attr CredentialDetails credential_details: (optional) Object containing details
          of the stored credentials.
          Obtain credentials for your source from the administrator of the source.
    :attr str status: (optional) The current status of this set of credentials.
          `connected` indicates that the credentials are available to use with the source
          configuration of a collection. `invalid` refers to the credentials (for example,
          the password provided has expired) and must be corrected before they can be used
          with a collection.
    """

    def __init__(self,
                 *,
                 credential_id: str = None,
                 source_type: str = None,
                 credential_details: 'CredentialDetails' = None,
                 status: str = None) -> None:
        """
        Initialize a Credentials object.

        :param str credential_id: (optional) Unique identifier for this set of
               credentials.
        :param str source_type: (optional) The source that this credentials object
               connects to.
               -  `box` indicates the credentials are used to connect an instance of
               Enterprise Box.
               -  `salesforce` indicates the credentials are used to connect to
               Salesforce.
               -  `sharepoint` indicates the credentials are used to connect to Microsoft
               SharePoint Online.
               -  `web_crawl` indicates the credentials are used to perform a web crawl.
               =  `cloud_object_storage` indicates the credentials are used to connect to
               an IBM Cloud Object Store.
        :param CredentialDetails credential_details: (optional) Object containing
               details of the stored credentials.
               Obtain credentials for your source from the administrator of the source.
        :param str status: (optional) The current status of this set of
               credentials. `connected` indicates that the credentials are available to
               use with the source configuration of a collection. `invalid` refers to the
               credentials (for example, the password provided has expired) and must be
               corrected before they can be used with a collection.
        """
        self.credential_id = credential_id
        self.source_type = source_type
        self.credential_details = credential_details
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Credentials':
        """Initialize a Credentials object from a json dictionary."""
        args = {}
        valid_keys = [
            'credential_id', 'source_type', 'credential_details', 'status'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Credentials: '
                + ', '.join(bad_keys))
        if 'credential_id' in _dict:
            args['credential_id'] = _dict.get('credential_id')
        if 'source_type' in _dict:
            args['source_type'] = _dict.get('source_type')
        if 'credential_details' in _dict:
            args['credential_details'] = CredentialDetails._from_dict(
                _dict.get('credential_details'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Credentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'credential_id') and self.credential_id is not None:
            _dict['credential_id'] = self.credential_id
        if hasattr(self, 'source_type') and self.source_type is not None:
            _dict['source_type'] = self.source_type
        if hasattr(
                self,
                'credential_details') and self.credential_details is not None:
            _dict['credential_details'] = self.credential_details._to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Credentials object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Credentials') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Credentials') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SourceTypeEnum(Enum):
        """
        The source that this credentials object connects to.
        -  `box` indicates the credentials are used to connect an instance of Enterprise
        Box.
        -  `salesforce` indicates the credentials are used to connect to Salesforce.
        -  `sharepoint` indicates the credentials are used to connect to Microsoft
        SharePoint Online.
        -  `web_crawl` indicates the credentials are used to perform a web crawl.
        =  `cloud_object_storage` indicates the credentials are used to connect to an IBM
        Cloud Object Store.
        """
        BOX = "box"
        SALESFORCE = "salesforce"
        SHAREPOINT = "sharepoint"
        WEB_CRAWL = "web_crawl"
        CLOUD_OBJECT_STORAGE = "cloud_object_storage"

    class StatusEnum(Enum):
        """
        The current status of this set of credentials. `connected` indicates that the
        credentials are available to use with the source configuration of a collection.
        `invalid` refers to the credentials (for example, the password provided has
        expired) and must be corrected before they can be used with a collection.
        """
        CONNECTED = "connected"
        INVALID = "invalid"


class CredentialsList():
    """
    Object containing array of credential definitions.

    :attr List[Credentials] credentials: (optional) An array of credential
          definitions that were created for this instance.
    """

    def __init__(self, *, credentials: List['Credentials'] = None) -> None:
        """
        Initialize a CredentialsList object.

        :param List[Credentials] credentials: (optional) An array of credential
               definitions that were created for this instance.
        """
        self.credentials = credentials

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CredentialsList':
        """Initialize a CredentialsList object from a json dictionary."""
        args = {}
        valid_keys = ['credentials']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CredentialsList: '
                + ', '.join(bad_keys))
        if 'credentials' in _dict:
            args['credentials'] = [
                Credentials._from_dict(x) for x in (_dict.get('credentials'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CredentialsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'credentials') and self.credentials is not None:
            _dict['credentials'] = [x._to_dict() for x in self.credentials]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CredentialsList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CredentialsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CredentialsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteCollectionResponse():
    """
    Response object returned when deleting a colleciton.

    :attr str collection_id: The unique identifier of the collection that is being
          deleted.
    :attr str status: The status of the collection. The status of a successful
          deletion operation is `deleted`.
    """

    def __init__(self, collection_id: str, status: str) -> None:
        """
        Initialize a DeleteCollectionResponse object.

        :param str collection_id: The unique identifier of the collection that is
               being deleted.
        :param str status: The status of the collection. The status of a successful
               deletion operation is `deleted`.
        """
        self.collection_id = collection_id
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteCollectionResponse':
        """Initialize a DeleteCollectionResponse object from a json dictionary."""
        args = {}
        valid_keys = ['collection_id', 'status']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DeleteCollectionResponse: '
                + ', '.join(bad_keys))
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        else:
            raise ValueError(
                'Required property \'collection_id\' not present in DeleteCollectionResponse JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in DeleteCollectionResponse JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteCollectionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteCollectionResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DeleteCollectionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteCollectionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        The status of the collection. The status of a successful deletion operation is
        `deleted`.
        """
        DELETED = "deleted"


class DeleteConfigurationResponse():
    """
    Information returned when a configuration is deleted.

    :attr str configuration_id: The unique identifier for the configuration.
    :attr str status: Status of the configuration. A deleted configuration has the
          status deleted.
    :attr List[Notice] notices: (optional) An array of notice messages, if any.
    """

    def __init__(self,
                 configuration_id: str,
                 status: str,
                 *,
                 notices: List['Notice'] = None) -> None:
        """
        Initialize a DeleteConfigurationResponse object.

        :param str configuration_id: The unique identifier for the configuration.
        :param str status: Status of the configuration. A deleted configuration has
               the status deleted.
        :param List[Notice] notices: (optional) An array of notice messages, if
               any.
        """
        self.configuration_id = configuration_id
        self.status = status
        self.notices = notices

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteConfigurationResponse':
        """Initialize a DeleteConfigurationResponse object from a json dictionary."""
        args = {}
        valid_keys = ['configuration_id', 'status', 'notices']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DeleteConfigurationResponse: '
                + ', '.join(bad_keys))
        if 'configuration_id' in _dict:
            args['configuration_id'] = _dict.get('configuration_id')
        else:
            raise ValueError(
                'Required property \'configuration_id\' not present in DeleteConfigurationResponse JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in DeleteConfigurationResponse JSON'
            )
        if 'notices' in _dict:
            args['notices'] = [
                Notice._from_dict(x) for x in (_dict.get('notices'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteConfigurationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'configuration_id') and self.configuration_id is not None:
            _dict['configuration_id'] = self.configuration_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = [x._to_dict() for x in self.notices]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteConfigurationResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DeleteConfigurationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteConfigurationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Status of the configuration. A deleted configuration has the status deleted.
        """
        DELETED = "deleted"


class DeleteCredentials():
    """
    Object returned after credentials are deleted.

    :attr str credential_id: (optional) The unique identifier of the credentials
          that have been deleted.
    :attr str status: (optional) The status of the deletion request.
    """

    def __init__(self,
                 *,
                 credential_id: str = None,
                 status: str = None) -> None:
        """
        Initialize a DeleteCredentials object.

        :param str credential_id: (optional) The unique identifier of the
               credentials that have been deleted.
        :param str status: (optional) The status of the deletion request.
        """
        self.credential_id = credential_id
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteCredentials':
        """Initialize a DeleteCredentials object from a json dictionary."""
        args = {}
        valid_keys = ['credential_id', 'status']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DeleteCredentials: '
                + ', '.join(bad_keys))
        if 'credential_id' in _dict:
            args['credential_id'] = _dict.get('credential_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteCredentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'credential_id') and self.credential_id is not None:
            _dict['credential_id'] = self.credential_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteCredentials object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DeleteCredentials') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteCredentials') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        The status of the deletion request.
        """
        DELETED = "deleted"


class DeleteDocumentResponse():
    """
    Information returned when a document is deleted.

    :attr str document_id: (optional) The unique identifier of the document.
    :attr str status: (optional) Status of the document. A deleted document has the
          status deleted.
    """

    def __init__(self, *, document_id: str = None, status: str = None) -> None:
        """
        Initialize a DeleteDocumentResponse object.

        :param str document_id: (optional) The unique identifier of the document.
        :param str status: (optional) Status of the document. A deleted document
               has the status deleted.
        """
        self.document_id = document_id
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteDocumentResponse':
        """Initialize a DeleteDocumentResponse object from a json dictionary."""
        args = {}
        valid_keys = ['document_id', 'status']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DeleteDocumentResponse: '
                + ', '.join(bad_keys))
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteDocumentResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteDocumentResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DeleteDocumentResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteDocumentResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Status of the document. A deleted document has the status deleted.
        """
        DELETED = "deleted"


class DeleteEnvironmentResponse():
    """
    Response object returned when deleting an environment.

    :attr str environment_id: The unique identifier for the environment.
    :attr str status: Status of the environment.
    """

    def __init__(self, environment_id: str, status: str) -> None:
        """
        Initialize a DeleteEnvironmentResponse object.

        :param str environment_id: The unique identifier for the environment.
        :param str status: Status of the environment.
        """
        self.environment_id = environment_id
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteEnvironmentResponse':
        """Initialize a DeleteEnvironmentResponse object from a json dictionary."""
        args = {}
        valid_keys = ['environment_id', 'status']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DeleteEnvironmentResponse: '
                + ', '.join(bad_keys))
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        else:
            raise ValueError(
                'Required property \'environment_id\' not present in DeleteEnvironmentResponse JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in DeleteEnvironmentResponse JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteEnvironmentResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteEnvironmentResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DeleteEnvironmentResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteEnvironmentResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Status of the environment.
        """
        DELETED = "deleted"


class DiskUsage():
    """
    Summary of the disk usage statistics for the environment.

    :attr int used_bytes: (optional) Number of bytes within the environment's disk
          capacity that are currently used to store data.
    :attr int maximum_allowed_bytes: (optional) Total number of bytes available in
          the environment's disk capacity.
    """

    def __init__(self,
                 *,
                 used_bytes: int = None,
                 maximum_allowed_bytes: int = None) -> None:
        """
        Initialize a DiskUsage object.

        :param int used_bytes: (optional) Number of bytes within the environment's
               disk capacity that are currently used to store data.
        :param int maximum_allowed_bytes: (optional) Total number of bytes
               available in the environment's disk capacity.
        """
        self.used_bytes = used_bytes
        self.maximum_allowed_bytes = maximum_allowed_bytes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DiskUsage':
        """Initialize a DiskUsage object from a json dictionary."""
        args = {}
        valid_keys = ['used_bytes', 'maximum_allowed_bytes']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DiskUsage: '
                + ', '.join(bad_keys))
        if 'used_bytes' in _dict:
            args['used_bytes'] = _dict.get('used_bytes')
        if 'maximum_allowed_bytes' in _dict:
            args['maximum_allowed_bytes'] = _dict.get('maximum_allowed_bytes')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DiskUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'used_bytes') and self.used_bytes is not None:
            _dict['used_bytes'] = self.used_bytes
        if hasattr(self, 'maximum_allowed_bytes'
                  ) and self.maximum_allowed_bytes is not None:
            _dict['maximum_allowed_bytes'] = self.maximum_allowed_bytes
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DiskUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DiskUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DiskUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentAccepted():
    """
    Information returned after an uploaded document is accepted.

    :attr str document_id: (optional) The unique identifier of the ingested
          document.
    :attr str status: (optional) Status of the document in the ingestion process. A
          status of `processing` is returned for documents that are ingested with a
          *version* date before `2019-01-01`. The `pending` status is returned for all
          others.
    :attr List[Notice] notices: (optional) Array of notices produced by the
          document-ingestion process.
    """

    def __init__(self,
                 *,
                 document_id: str = None,
                 status: str = None,
                 notices: List['Notice'] = None) -> None:
        """
        Initialize a DocumentAccepted object.

        :param str document_id: (optional) The unique identifier of the ingested
               document.
        :param str status: (optional) Status of the document in the ingestion
               process. A status of `processing` is returned for documents that are
               ingested with a *version* date before `2019-01-01`. The `pending` status is
               returned for all others.
        :param List[Notice] notices: (optional) Array of notices produced by the
               document-ingestion process.
        """
        self.document_id = document_id
        self.status = status
        self.notices = notices

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentAccepted':
        """Initialize a DocumentAccepted object from a json dictionary."""
        args = {}
        valid_keys = ['document_id', 'status', 'notices']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentAccepted: '
                + ', '.join(bad_keys))
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'notices' in _dict:
            args['notices'] = [
                Notice._from_dict(x) for x in (_dict.get('notices'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentAccepted object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = [x._to_dict() for x in self.notices]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentAccepted object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocumentAccepted') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentAccepted') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Status of the document in the ingestion process. A status of `processing` is
        returned for documents that are ingested with a *version* date before
        `2019-01-01`. The `pending` status is returned for all others.
        """
        PROCESSING = "processing"
        PENDING = "pending"


class DocumentCounts():
    """
    Object containing collection document count information.

    :attr int available: (optional) The total number of available documents in the
          collection.
    :attr int processing: (optional) The number of documents in the collection that
          are currently being processed.
    :attr int failed: (optional) The number of documents in the collection that
          failed to be ingested.
    :attr int pending: (optional) The number of documents that have been uploaded to
          the collection, but have not yet started processing.
    """

    def __init__(self,
                 *,
                 available: int = None,
                 processing: int = None,
                 failed: int = None,
                 pending: int = None) -> None:
        """
        Initialize a DocumentCounts object.

        :param int available: (optional) The total number of available documents in
               the collection.
        :param int processing: (optional) The number of documents in the collection
               that are currently being processed.
        :param int failed: (optional) The number of documents in the collection
               that failed to be ingested.
        :param int pending: (optional) The number of documents that have been
               uploaded to the collection, but have not yet started processing.
        """
        self.available = available
        self.processing = processing
        self.failed = failed
        self.pending = pending

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentCounts':
        """Initialize a DocumentCounts object from a json dictionary."""
        args = {}
        valid_keys = ['available', 'processing', 'failed', 'pending']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentCounts: '
                + ', '.join(bad_keys))
        if 'available' in _dict:
            args['available'] = _dict.get('available')
        if 'processing' in _dict:
            args['processing'] = _dict.get('processing')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'pending' in _dict:
            args['pending'] = _dict.get('pending')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentCounts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'available') and self.available is not None:
            _dict['available'] = self.available
        if hasattr(self, 'processing') and self.processing is not None:
            _dict['processing'] = self.processing
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'pending') and self.pending is not None:
            _dict['pending'] = self.pending
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentCounts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocumentCounts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentCounts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentStatus():
    """
    Status information about a submitted document.

    :attr str document_id: The unique identifier of the document.
    :attr str configuration_id: (optional) The unique identifier for the
          configuration.
    :attr str status: Status of the document in the ingestion process.
    :attr str status_description: Description of the document status.
    :attr str filename: (optional) Name of the original source file (if available).
    :attr str file_type: (optional) The type of the original source file.
    :attr str sha1: (optional) The SHA-1 hash of the original source file (formatted
          as a hexadecimal string).
    :attr List[Notice] notices: Array of notices produced by the document-ingestion
          process.
    """

    def __init__(self,
                 document_id: str,
                 status: str,
                 status_description: str,
                 notices: List['Notice'],
                 *,
                 configuration_id: str = None,
                 filename: str = None,
                 file_type: str = None,
                 sha1: str = None) -> None:
        """
        Initialize a DocumentStatus object.

        :param str document_id: The unique identifier of the document.
        :param str status: Status of the document in the ingestion process.
        :param str status_description: Description of the document status.
        :param List[Notice] notices: Array of notices produced by the
               document-ingestion process.
        :param str configuration_id: (optional) The unique identifier for the
               configuration.
        :param str filename: (optional) Name of the original source file (if
               available).
        :param str file_type: (optional) The type of the original source file.
        :param str sha1: (optional) The SHA-1 hash of the original source file
               (formatted as a hexadecimal string).
        """
        self.document_id = document_id
        self.configuration_id = configuration_id
        self.status = status
        self.status_description = status_description
        self.filename = filename
        self.file_type = file_type
        self.sha1 = sha1
        self.notices = notices

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentStatus':
        """Initialize a DocumentStatus object from a json dictionary."""
        args = {}
        valid_keys = [
            'document_id', 'configuration_id', 'status', 'status_description',
            'filename', 'file_type', 'sha1', 'notices'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentStatus: '
                + ', '.join(bad_keys))
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        else:
            raise ValueError(
                'Required property \'document_id\' not present in DocumentStatus JSON'
            )
        if 'configuration_id' in _dict:
            args['configuration_id'] = _dict.get('configuration_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in DocumentStatus JSON'
            )
        if 'status_description' in _dict:
            args['status_description'] = _dict.get('status_description')
        else:
            raise ValueError(
                'Required property \'status_description\' not present in DocumentStatus JSON'
            )
        if 'filename' in _dict:
            args['filename'] = _dict.get('filename')
        if 'file_type' in _dict:
            args['file_type'] = _dict.get('file_type')
        if 'sha1' in _dict:
            args['sha1'] = _dict.get('sha1')
        if 'notices' in _dict:
            args['notices'] = [
                Notice._from_dict(x) for x in (_dict.get('notices'))
            ]
        else:
            raise ValueError(
                'Required property \'notices\' not present in DocumentStatus JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self,
                   'configuration_id') and self.configuration_id is not None:
            _dict['configuration_id'] = self.configuration_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(
                self,
                'status_description') and self.status_description is not None:
            _dict['status_description'] = self.status_description
        if hasattr(self, 'filename') and self.filename is not None:
            _dict['filename'] = self.filename
        if hasattr(self, 'file_type') and self.file_type is not None:
            _dict['file_type'] = self.file_type
        if hasattr(self, 'sha1') and self.sha1 is not None:
            _dict['sha1'] = self.sha1
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = [x._to_dict() for x in self.notices]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocumentStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Status of the document in the ingestion process.
        """
        AVAILABLE = "available"
        AVAILABLE_WITH_NOTICES = "available with notices"
        FAILED = "failed"
        PROCESSING = "processing"
        PENDING = "pending"

    class FileTypeEnum(Enum):
        """
        The type of the original source file.
        """
        PDF = "pdf"
        HTML = "html"
        WORD = "word"
        JSON = "json"


class Enrichment():
    """
    Enrichment step to perform on the document. Each enrichment is performed on the
    specified field in the order that they are listed in the configuration.

    :attr str description: (optional) Describes what the enrichment step does.
    :attr str destination_field: Field where enrichments will be stored. This field
          must already exist or be at most 1 level deeper than an existing field. For
          example, if `text` is a top-level field with no sub-fields, `text.foo` is a
          valid destination but `text.foo.bar` is not.
    :attr str source_field: Field to be enriched.
          Arrays can be specified as the **source_field** if the **enrichment** service
          for this enrichment is set to `natural_language_undstanding`.
    :attr bool overwrite: (optional) Indicates that the enrichments will overwrite
          the destination_field field if it already exists.
    :attr str enrichment: Name of the enrichment service to call. Current options
          are `natural_language_understanding` and `elements`.
           When using `natual_language_understanding`, the **options** object must contain
          Natural Language Understanding options.
           When using `elements` the **options** object must contain Element
          Classification options. Additionally, when using the `elements` enrichment the
          configuration specified and files ingested must meet all the criteria specified
          in [the
          documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-element-classification#element-classification).
    :attr bool ignore_downstream_errors: (optional) If true, then most errors
          generated during the enrichment process will be treated as warnings and will not
          cause the document to fail processing.
    :attr EnrichmentOptions options: (optional) Options which are specific to a
          particular enrichment.
    """

    def __init__(self,
                 destination_field: str,
                 source_field: str,
                 enrichment: str,
                 *,
                 description: str = None,
                 overwrite: bool = None,
                 ignore_downstream_errors: bool = None,
                 options: 'EnrichmentOptions' = None) -> None:
        """
        Initialize a Enrichment object.

        :param str destination_field: Field where enrichments will be stored. This
               field must already exist or be at most 1 level deeper than an existing
               field. For example, if `text` is a top-level field with no sub-fields,
               `text.foo` is a valid destination but `text.foo.bar` is not.
        :param str source_field: Field to be enriched.
               Arrays can be specified as the **source_field** if the **enrichment**
               service for this enrichment is set to `natural_language_undstanding`.
        :param str enrichment: Name of the enrichment service to call. Current
               options are `natural_language_understanding` and `elements`.
                When using `natual_language_understanding`, the **options** object must
               contain Natural Language Understanding options.
                When using `elements` the **options** object must contain Element
               Classification options. Additionally, when using the `elements` enrichment
               the configuration specified and files ingested must meet all the criteria
               specified in [the
               documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-element-classification#element-classification).
        :param str description: (optional) Describes what the enrichment step does.
        :param bool overwrite: (optional) Indicates that the enrichments will
               overwrite the destination_field field if it already exists.
        :param bool ignore_downstream_errors: (optional) If true, then most errors
               generated during the enrichment process will be treated as warnings and
               will not cause the document to fail processing.
        :param EnrichmentOptions options: (optional) Options which are specific to
               a particular enrichment.
        """
        self.description = description
        self.destination_field = destination_field
        self.source_field = source_field
        self.overwrite = overwrite
        self.enrichment = enrichment
        self.ignore_downstream_errors = ignore_downstream_errors
        self.options = options

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Enrichment':
        """Initialize a Enrichment object from a json dictionary."""
        args = {}
        valid_keys = [
            'description', 'destination_field', 'source_field', 'overwrite',
            'enrichment', 'ignore_downstream_errors', 'options'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Enrichment: '
                + ', '.join(bad_keys))
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'destination_field' in _dict:
            args['destination_field'] = _dict.get('destination_field')
        else:
            raise ValueError(
                'Required property \'destination_field\' not present in Enrichment JSON'
            )
        if 'source_field' in _dict:
            args['source_field'] = _dict.get('source_field')
        else:
            raise ValueError(
                'Required property \'source_field\' not present in Enrichment JSON'
            )
        if 'overwrite' in _dict:
            args['overwrite'] = _dict.get('overwrite')
        if 'enrichment' in _dict:
            args['enrichment'] = _dict.get('enrichment')
        else:
            raise ValueError(
                'Required property \'enrichment\' not present in Enrichment JSON'
            )
        if 'ignore_downstream_errors' in _dict:
            args['ignore_downstream_errors'] = _dict.get(
                'ignore_downstream_errors')
        if 'options' in _dict:
            args['options'] = EnrichmentOptions._from_dict(_dict.get('options'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Enrichment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self,
                   'destination_field') and self.destination_field is not None:
            _dict['destination_field'] = self.destination_field
        if hasattr(self, 'source_field') and self.source_field is not None:
            _dict['source_field'] = self.source_field
        if hasattr(self, 'overwrite') and self.overwrite is not None:
            _dict['overwrite'] = self.overwrite
        if hasattr(self, 'enrichment') and self.enrichment is not None:
            _dict['enrichment'] = self.enrichment
        if hasattr(self, 'ignore_downstream_errors'
                  ) and self.ignore_downstream_errors is not None:
            _dict['ignore_downstream_errors'] = self.ignore_downstream_errors
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = self.options._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Enrichment object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Enrichment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Enrichment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnrichmentOptions():
    """
    Options which are specific to a particular enrichment.

    :attr NluEnrichmentFeatures features: (optional) Object containing Natural
          Language Understanding features to be used.
    :attr str language: (optional) ISO 639-1 code indicating the language to use for
          the analysis. This code overrides the automatic language detection performed by
          the service. Valid codes are `ar` (Arabic), `en` (English), `fr` (French), `de`
          (German), `it` (Italian), `pt` (Portuguese), `ru` (Russian), `es` (Spanish), and
          `sv` (Swedish). **Note:** Not all features support all languages, automatic
          detection is recommended.
    :attr str model: (optional) *For use with `elements` enrichments only.* The
          element extraction model to use. Models available are: `contract`.
    """

    def __init__(self,
                 *,
                 features: 'NluEnrichmentFeatures' = None,
                 language: str = None,
                 model: str = None) -> None:
        """
        Initialize a EnrichmentOptions object.

        :param NluEnrichmentFeatures features: (optional) Object containing Natural
               Language Understanding features to be used.
        :param str language: (optional) ISO 639-1 code indicating the language to
               use for the analysis. This code overrides the automatic language detection
               performed by the service. Valid codes are `ar` (Arabic), `en` (English),
               `fr` (French), `de` (German), `it` (Italian), `pt` (Portuguese), `ru`
               (Russian), `es` (Spanish), and `sv` (Swedish). **Note:** Not all features
               support all languages, automatic detection is recommended.
        :param str model: (optional) *For use with `elements` enrichments only.*
               The element extraction model to use. Models available are: `contract`.
        """
        self.features = features
        self.language = language
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnrichmentOptions':
        """Initialize a EnrichmentOptions object from a json dictionary."""
        args = {}
        valid_keys = ['features', 'language', 'model']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EnrichmentOptions: '
                + ', '.join(bad_keys))
        if 'features' in _dict:
            args['features'] = NluEnrichmentFeatures._from_dict(
                _dict.get('features'))
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnrichmentOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = self.features._to_dict()
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnrichmentOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EnrichmentOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnrichmentOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LanguageEnum(Enum):
        """
        ISO 639-1 code indicating the language to use for the analysis. This code
        overrides the automatic language detection performed by the service. Valid codes
        are `ar` (Arabic), `en` (English), `fr` (French), `de` (German), `it` (Italian),
        `pt` (Portuguese), `ru` (Russian), `es` (Spanish), and `sv` (Swedish). **Note:**
        Not all features support all languages, automatic detection is recommended.
        """
        AR = "ar"
        EN = "en"
        FR = "fr"
        DE = "de"
        IT = "it"
        PT = "pt"
        RU = "ru"
        ES = "es"
        SV = "sv"


class Environment():
    """
    Details about an environment.

    :attr str environment_id: (optional) Unique identifier for the environment.
    :attr str name: (optional) Name that identifies the environment.
    :attr str description: (optional) Description of the environment.
    :attr datetime created: (optional) Creation date of the environment, in the
          format `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.
    :attr datetime updated: (optional) Date of most recent environment update, in
          the format `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.
    :attr str status: (optional) Current status of the environment. `resizing` is
          displayed when a request to increase the environment size has been made, but is
          still in the process of being completed.
    :attr bool read_only: (optional) If `true`, the environment contains read-only
          collections that are maintained by IBM.
    :attr str size: (optional) Current size of the environment.
    :attr str requested_size: (optional) The new size requested for this
          environment. Only returned when the environment *status* is `resizing`.
          *Note:* Querying and indexing can still be performed during an environment
          upsize.
    :attr IndexCapacity index_capacity: (optional) Details about the resource usage
          and capacity of the environment.
    :attr SearchStatus search_status: (optional) Information about the Continuous
          Relevancy Training for this environment.
    """

    def __init__(self,
                 *,
                 environment_id: str = None,
                 name: str = None,
                 description: str = None,
                 created: datetime = None,
                 updated: datetime = None,
                 status: str = None,
                 read_only: bool = None,
                 size: str = None,
                 requested_size: str = None,
                 index_capacity: 'IndexCapacity' = None,
                 search_status: 'SearchStatus' = None) -> None:
        """
        Initialize a Environment object.

        :param str environment_id: (optional) Unique identifier for the
               environment.
        :param str name: (optional) Name that identifies the environment.
        :param str description: (optional) Description of the environment.
        :param datetime created: (optional) Creation date of the environment, in
               the format `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.
        :param datetime updated: (optional) Date of most recent environment update,
               in the format `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.
        :param str status: (optional) Current status of the environment. `resizing`
               is displayed when a request to increase the environment size has been made,
               but is still in the process of being completed.
        :param bool read_only: (optional) If `true`, the environment contains
               read-only collections that are maintained by IBM.
        :param str size: (optional) Current size of the environment.
        :param str requested_size: (optional) The new size requested for this
               environment. Only returned when the environment *status* is `resizing`.
               *Note:* Querying and indexing can still be performed during an environment
               upsize.
        :param IndexCapacity index_capacity: (optional) Details about the resource
               usage and capacity of the environment.
        :param SearchStatus search_status: (optional) Information about the
               Continuous Relevancy Training for this environment.
        """
        self.environment_id = environment_id
        self.name = name
        self.description = description
        self.created = created
        self.updated = updated
        self.status = status
        self.read_only = read_only
        self.size = size
        self.requested_size = requested_size
        self.index_capacity = index_capacity
        self.search_status = search_status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Environment':
        """Initialize a Environment object from a json dictionary."""
        args = {}
        valid_keys = [
            'environment_id', 'name', 'description', 'created', 'updated',
            'status', 'read_only', 'size', 'requested_size', 'index_capacity',
            'search_status'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Environment: '
                + ', '.join(bad_keys))
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'read_only' in _dict:
            args['read_only'] = _dict.get('read_only')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'requested_size' in _dict:
            args['requested_size'] = _dict.get('requested_size')
        if 'index_capacity' in _dict:
            args['index_capacity'] = IndexCapacity._from_dict(
                _dict.get('index_capacity'))
        if 'search_status' in _dict:
            args['search_status'] = SearchStatus._from_dict(
                _dict.get('search_status'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Environment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'read_only') and self.read_only is not None:
            _dict['read_only'] = self.read_only
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'requested_size') and self.requested_size is not None:
            _dict['requested_size'] = self.requested_size
        if hasattr(self, 'index_capacity') and self.index_capacity is not None:
            _dict['index_capacity'] = self.index_capacity._to_dict()
        if hasattr(self, 'search_status') and self.search_status is not None:
            _dict['search_status'] = self.search_status._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Environment object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Environment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Environment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Current status of the environment. `resizing` is displayed when a request to
        increase the environment size has been made, but is still in the process of being
        completed.
        """
        ACTIVE = "active"
        PENDING = "pending"
        MAINTENANCE = "maintenance"
        RESIZING = "resizing"

    class SizeEnum(Enum):
        """
        Current size of the environment.
        """
        LT = "LT"
        XS = "XS"
        S = "S"
        MS = "MS"
        M = "M"
        ML = "ML"
        L = "L"
        XL = "XL"
        XXL = "XXL"
        XXXL = "XXXL"


class EnvironmentDocuments():
    """
    Summary of the document usage statistics for the environment.

    :attr int available: (optional) Number of documents indexed for the environment.
    :attr int maximum_allowed: (optional) Total number of documents allowed in the
          environment's capacity.
    """

    def __init__(self,
                 *,
                 available: int = None,
                 maximum_allowed: int = None) -> None:
        """
        Initialize a EnvironmentDocuments object.

        :param int available: (optional) Number of documents indexed for the
               environment.
        :param int maximum_allowed: (optional) Total number of documents allowed in
               the environment's capacity.
        """
        self.available = available
        self.maximum_allowed = maximum_allowed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentDocuments':
        """Initialize a EnvironmentDocuments object from a json dictionary."""
        args = {}
        valid_keys = ['available', 'maximum_allowed']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EnvironmentDocuments: '
                + ', '.join(bad_keys))
        if 'available' in _dict:
            args['available'] = _dict.get('available')
        if 'maximum_allowed' in _dict:
            args['maximum_allowed'] = _dict.get('maximum_allowed')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentDocuments object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'available') and self.available is not None:
            _dict['available'] = self.available
        if hasattr(self,
                   'maximum_allowed') and self.maximum_allowed is not None:
            _dict['maximum_allowed'] = self.maximum_allowed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentDocuments object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentDocuments') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentDocuments') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EventData():
    """
    Query event data object.

    :attr str environment_id: The **environment_id** associated with the query that
          the event is associated with.
    :attr str session_token: The session token that was returned as part of the
          query results that this event is associated with.
    :attr datetime client_timestamp: (optional) The optional timestamp for the event
          that was created. If not provided, the time that the event was created in the
          log was used.
    :attr int display_rank: (optional) The rank of the result item which the event
          is associated with.
    :attr str collection_id: The **collection_id** of the document that this event
          is associated with.
    :attr str document_id: The **document_id** of the document that this event is
          associated with.
    :attr str query_id: (optional) The query identifier stored in the log. The query
          and any events associated with that query are stored with the same **query_id**.
    """

    def __init__(self,
                 environment_id: str,
                 session_token: str,
                 collection_id: str,
                 document_id: str,
                 *,
                 client_timestamp: datetime = None,
                 display_rank: int = None,
                 query_id: str = None) -> None:
        """
        Initialize a EventData object.

        :param str environment_id: The **environment_id** associated with the query
               that the event is associated with.
        :param str session_token: The session token that was returned as part of
               the query results that this event is associated with.
        :param str collection_id: The **collection_id** of the document that this
               event is associated with.
        :param str document_id: The **document_id** of the document that this event
               is associated with.
        :param datetime client_timestamp: (optional) The optional timestamp for the
               event that was created. If not provided, the time that the event was
               created in the log was used.
        :param int display_rank: (optional) The rank of the result item which the
               event is associated with.
        :param str query_id: (optional) The query identifier stored in the log. The
               query and any events associated with that query are stored with the same
               **query_id**.
        """
        self.environment_id = environment_id
        self.session_token = session_token
        self.client_timestamp = client_timestamp
        self.display_rank = display_rank
        self.collection_id = collection_id
        self.document_id = document_id
        self.query_id = query_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EventData':
        """Initialize a EventData object from a json dictionary."""
        args = {}
        valid_keys = [
            'environment_id', 'session_token', 'client_timestamp',
            'display_rank', 'collection_id', 'document_id', 'query_id'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EventData: '
                + ', '.join(bad_keys))
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        else:
            raise ValueError(
                'Required property \'environment_id\' not present in EventData JSON'
            )
        if 'session_token' in _dict:
            args['session_token'] = _dict.get('session_token')
        else:
            raise ValueError(
                'Required property \'session_token\' not present in EventData JSON'
            )
        if 'client_timestamp' in _dict:
            args['client_timestamp'] = string_to_datetime(
                _dict.get('client_timestamp'))
        if 'display_rank' in _dict:
            args['display_rank'] = _dict.get('display_rank')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        else:
            raise ValueError(
                'Required property \'collection_id\' not present in EventData JSON'
            )
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        else:
            raise ValueError(
                'Required property \'document_id\' not present in EventData JSON'
            )
        if 'query_id' in _dict:
            args['query_id'] = _dict.get('query_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EventData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'session_token') and self.session_token is not None:
            _dict['session_token'] = self.session_token
        if hasattr(self,
                   'client_timestamp') and self.client_timestamp is not None:
            _dict['client_timestamp'] = datetime_to_string(
                self.client_timestamp)
        if hasattr(self, 'display_rank') and self.display_rank is not None:
            _dict['display_rank'] = self.display_rank
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'query_id') and self.query_id is not None:
            _dict['query_id'] = self.query_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EventData object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EventData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EventData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Expansion():
    """
    An expansion definition. Each object respresents one set of expandable strings. For
    example, you could have expansions for the word `hot` in one object, and expansions
    for the word `cold` in another.

    :attr List[str] input_terms: (optional) A list of terms that will be expanded
          for this expansion. If specified, only the items in this list are expanded.
    :attr List[str] expanded_terms: A list of terms that this expansion will be
          expanded to. If specified without **input_terms**, it also functions as the
          input term list.
    """

    def __init__(self,
                 expanded_terms: List[str],
                 *,
                 input_terms: List[str] = None) -> None:
        """
        Initialize a Expansion object.

        :param List[str] expanded_terms: A list of terms that this expansion will
               be expanded to. If specified without **input_terms**, it also functions as
               the input term list.
        :param List[str] input_terms: (optional) A list of terms that will be
               expanded for this expansion. If specified, only the items in this list are
               expanded.
        """
        self.input_terms = input_terms
        self.expanded_terms = expanded_terms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Expansion':
        """Initialize a Expansion object from a json dictionary."""
        args = {}
        valid_keys = ['input_terms', 'expanded_terms']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Expansion: '
                + ', '.join(bad_keys))
        if 'input_terms' in _dict:
            args['input_terms'] = _dict.get('input_terms')
        if 'expanded_terms' in _dict:
            args['expanded_terms'] = _dict.get('expanded_terms')
        else:
            raise ValueError(
                'Required property \'expanded_terms\' not present in Expansion JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Expansion object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input_terms') and self.input_terms is not None:
            _dict['input_terms'] = self.input_terms
        if hasattr(self, 'expanded_terms') and self.expanded_terms is not None:
            _dict['expanded_terms'] = self.expanded_terms
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Expansion object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Expansion') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Expansion') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Expansions():
    """
    The query expansion definitions for the specified collection.

    :attr List[Expansion] expansions: An array of query expansion definitions.
           Each object in the **expansions** array represents a term or set of terms that
          will be expanded into other terms. Each expansion object can be configured as
          bidirectional or unidirectional. Bidirectional means that all terms are expanded
          to all other terms in the object. Unidirectional means that a set list of terms
          can be expanded into a second list of terms.
           To create a bi-directional expansion specify an **expanded_terms** array. When
          found in a query, all items in the **expanded_terms** array are then expanded to
          the other items in the same array.
           To create a uni-directional expansion, specify both an array of **input_terms**
          and an array of **expanded_terms**. When items in the **input_terms** array are
          present in a query, they are expanded using the items listed in the
          **expanded_terms** array.
    """

    def __init__(self, expansions: List['Expansion']) -> None:
        """
        Initialize a Expansions object.

        :param List[Expansion] expansions: An array of query expansion definitions.
                Each object in the **expansions** array represents a term or set of terms
               that will be expanded into other terms. Each expansion object can be
               configured as bidirectional or unidirectional. Bidirectional means that all
               terms are expanded to all other terms in the object. Unidirectional means
               that a set list of terms can be expanded into a second list of terms.
                To create a bi-directional expansion specify an **expanded_terms** array.
               When found in a query, all items in the **expanded_terms** array are then
               expanded to the other items in the same array.
                To create a uni-directional expansion, specify both an array of
               **input_terms** and an array of **expanded_terms**. When items in the
               **input_terms** array are present in a query, they are expanded using the
               items listed in the **expanded_terms** array.
        """
        self.expansions = expansions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Expansions':
        """Initialize a Expansions object from a json dictionary."""
        args = {}
        valid_keys = ['expansions']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Expansions: '
                + ', '.join(bad_keys))
        if 'expansions' in _dict:
            args['expansions'] = [
                Expansion._from_dict(x) for x in (_dict.get('expansions'))
            ]
        else:
            raise ValueError(
                'Required property \'expansions\' not present in Expansions JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Expansions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'expansions') and self.expansions is not None:
            _dict['expansions'] = [x._to_dict() for x in self.expansions]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Expansions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Expansions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Expansions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Field():
    """
    Object containing field details.

    :attr str field: (optional) The name of the field.
    :attr str type: (optional) The type of the field.
    """

    def __init__(self, *, field: str = None, type: str = None) -> None:
        """
        Initialize a Field object.

        :param str field: (optional) The name of the field.
        :param str type: (optional) The type of the field.
        """
        self.field = field
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Field':
        """Initialize a Field object from a json dictionary."""
        args = {}
        valid_keys = ['field', 'type']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Field: ' +
                ', '.join(bad_keys))
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Field object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Field object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Field') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Field') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        The type of the field.
        """
        NESTED = "nested"
        STRING = "string"
        DATE = "date"
        LONG = "long"
        INTEGER = "integer"
        SHORT = "short"
        BYTE = "byte"
        DOUBLE = "double"
        FLOAT = "float"
        BOOLEAN = "boolean"
        BINARY = "binary"


class FontSetting():
    """
    Font matching configuration.

    :attr int level: (optional) The HTML heading level that any content with the
          matching font is converted to.
    :attr int min_size: (optional) The minimum size of the font to match.
    :attr int max_size: (optional) The maximum size of the font to match.
    :attr bool bold: (optional) When `true`, the font is matched if it is bold.
    :attr bool italic: (optional) When `true`, the font is matched if it is italic.
    :attr str name: (optional) The name of the font.
    """

    def __init__(self,
                 *,
                 level: int = None,
                 min_size: int = None,
                 max_size: int = None,
                 bold: bool = None,
                 italic: bool = None,
                 name: str = None) -> None:
        """
        Initialize a FontSetting object.

        :param int level: (optional) The HTML heading level that any content with
               the matching font is converted to.
        :param int min_size: (optional) The minimum size of the font to match.
        :param int max_size: (optional) The maximum size of the font to match.
        :param bool bold: (optional) When `true`, the font is matched if it is
               bold.
        :param bool italic: (optional) When `true`, the font is matched if it is
               italic.
        :param str name: (optional) The name of the font.
        """
        self.level = level
        self.min_size = min_size
        self.max_size = max_size
        self.bold = bold
        self.italic = italic
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FontSetting':
        """Initialize a FontSetting object from a json dictionary."""
        args = {}
        valid_keys = ['level', 'min_size', 'max_size', 'bold', 'italic', 'name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FontSetting: '
                + ', '.join(bad_keys))
        if 'level' in _dict:
            args['level'] = _dict.get('level')
        if 'min_size' in _dict:
            args['min_size'] = _dict.get('min_size')
        if 'max_size' in _dict:
            args['max_size'] = _dict.get('max_size')
        if 'bold' in _dict:
            args['bold'] = _dict.get('bold')
        if 'italic' in _dict:
            args['italic'] = _dict.get('italic')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FontSetting object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self, 'min_size') and self.min_size is not None:
            _dict['min_size'] = self.min_size
        if hasattr(self, 'max_size') and self.max_size is not None:
            _dict['max_size'] = self.max_size
        if hasattr(self, 'bold') and self.bold is not None:
            _dict['bold'] = self.bold
        if hasattr(self, 'italic') and self.italic is not None:
            _dict['italic'] = self.italic
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FontSetting object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FontSetting') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FontSetting') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Gateway():
    """
    Object describing a specific gateway.

    :attr str gateway_id: (optional) The gateway ID of the gateway.
    :attr str name: (optional) The user defined name of the gateway.
    :attr str status: (optional) The current status of the gateway. `connected`
          means the gateway is connected to the remotly installed gateway. `idle` means
          this gateway is not currently in use.
    :attr str token: (optional) The generated **token** for this gateway. The value
          of this field is used when configuring the remotly installed gateway.
    :attr str token_id: (optional) The generated **token_id** for this gateway. The
          value of this field is used when configuring the remotly installed gateway.
    """

    def __init__(self,
                 *,
                 gateway_id: str = None,
                 name: str = None,
                 status: str = None,
                 token: str = None,
                 token_id: str = None) -> None:
        """
        Initialize a Gateway object.

        :param str gateway_id: (optional) The gateway ID of the gateway.
        :param str name: (optional) The user defined name of the gateway.
        :param str status: (optional) The current status of the gateway.
               `connected` means the gateway is connected to the remotly installed
               gateway. `idle` means this gateway is not currently in use.
        :param str token: (optional) The generated **token** for this gateway. The
               value of this field is used when configuring the remotly installed gateway.
        :param str token_id: (optional) The generated **token_id** for this
               gateway. The value of this field is used when configuring the remotly
               installed gateway.
        """
        self.gateway_id = gateway_id
        self.name = name
        self.status = status
        self.token = token
        self.token_id = token_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Gateway':
        """Initialize a Gateway object from a json dictionary."""
        args = {}
        valid_keys = ['gateway_id', 'name', 'status', 'token', 'token_id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Gateway: ' +
                ', '.join(bad_keys))
        if 'gateway_id' in _dict:
            args['gateway_id'] = _dict.get('gateway_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'token' in _dict:
            args['token'] = _dict.get('token')
        if 'token_id' in _dict:
            args['token_id'] = _dict.get('token_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Gateway object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'gateway_id') and self.gateway_id is not None:
            _dict['gateway_id'] = self.gateway_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'token') and self.token is not None:
            _dict['token'] = self.token
        if hasattr(self, 'token_id') and self.token_id is not None:
            _dict['token_id'] = self.token_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Gateway object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Gateway') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Gateway') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        The current status of the gateway. `connected` means the gateway is connected to
        the remotly installed gateway. `idle` means this gateway is not currently in use.
        """
        CONNECTED = "connected"
        IDLE = "idle"


class GatewayDelete():
    """
    Gatway deletion confirmation.

    :attr str gateway_id: (optional) The gateway ID of the deleted gateway.
    :attr str status: (optional) The status of the request.
    """

    def __init__(self, *, gateway_id: str = None, status: str = None) -> None:
        """
        Initialize a GatewayDelete object.

        :param str gateway_id: (optional) The gateway ID of the deleted gateway.
        :param str status: (optional) The status of the request.
        """
        self.gateway_id = gateway_id
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GatewayDelete':
        """Initialize a GatewayDelete object from a json dictionary."""
        args = {}
        valid_keys = ['gateway_id', 'status']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class GatewayDelete: '
                + ', '.join(bad_keys))
        if 'gateway_id' in _dict:
            args['gateway_id'] = _dict.get('gateway_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GatewayDelete object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'gateway_id') and self.gateway_id is not None:
            _dict['gateway_id'] = self.gateway_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GatewayDelete object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'GatewayDelete') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GatewayDelete') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GatewayList():
    """
    Object containing gateways array.

    :attr List[Gateway] gateways: (optional) Array of configured gateway
          connections.
    """

    def __init__(self, *, gateways: List['Gateway'] = None) -> None:
        """
        Initialize a GatewayList object.

        :param List[Gateway] gateways: (optional) Array of configured gateway
               connections.
        """
        self.gateways = gateways

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GatewayList':
        """Initialize a GatewayList object from a json dictionary."""
        args = {}
        valid_keys = ['gateways']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class GatewayList: '
                + ', '.join(bad_keys))
        if 'gateways' in _dict:
            args['gateways'] = [
                Gateway._from_dict(x) for x in (_dict.get('gateways'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GatewayList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'gateways') and self.gateways is not None:
            _dict['gateways'] = [x._to_dict() for x in self.gateways]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GatewayList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'GatewayList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GatewayList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HtmlSettings():
    """
    A list of HTML conversion settings.

    :attr List[str] exclude_tags_completely: (optional) Array of HTML tags that are
          excluded completely.
    :attr List[str] exclude_tags_keep_content: (optional) Array of HTML tags which
          are excluded but still retain content.
    :attr XPathPatterns keep_content: (optional) Object containing an array of
          XPaths.
    :attr XPathPatterns exclude_content: (optional) Object containing an array of
          XPaths.
    :attr List[str] keep_tag_attributes: (optional) An array of HTML tag attributes
          to keep in the converted document.
    :attr List[str] exclude_tag_attributes: (optional) Array of HTML tag attributes
          to exclude.
    """

    def __init__(self,
                 *,
                 exclude_tags_completely: List[str] = None,
                 exclude_tags_keep_content: List[str] = None,
                 keep_content: 'XPathPatterns' = None,
                 exclude_content: 'XPathPatterns' = None,
                 keep_tag_attributes: List[str] = None,
                 exclude_tag_attributes: List[str] = None) -> None:
        """
        Initialize a HtmlSettings object.

        :param List[str] exclude_tags_completely: (optional) Array of HTML tags
               that are excluded completely.
        :param List[str] exclude_tags_keep_content: (optional) Array of HTML tags
               which are excluded but still retain content.
        :param XPathPatterns keep_content: (optional) Object containing an array of
               XPaths.
        :param XPathPatterns exclude_content: (optional) Object containing an array
               of XPaths.
        :param List[str] keep_tag_attributes: (optional) An array of HTML tag
               attributes to keep in the converted document.
        :param List[str] exclude_tag_attributes: (optional) Array of HTML tag
               attributes to exclude.
        """
        self.exclude_tags_completely = exclude_tags_completely
        self.exclude_tags_keep_content = exclude_tags_keep_content
        self.keep_content = keep_content
        self.exclude_content = exclude_content
        self.keep_tag_attributes = keep_tag_attributes
        self.exclude_tag_attributes = exclude_tag_attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HtmlSettings':
        """Initialize a HtmlSettings object from a json dictionary."""
        args = {}
        valid_keys = [
            'exclude_tags_completely', 'exclude_tags_keep_content',
            'keep_content', 'exclude_content', 'keep_tag_attributes',
            'exclude_tag_attributes'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class HtmlSettings: '
                + ', '.join(bad_keys))
        if 'exclude_tags_completely' in _dict:
            args['exclude_tags_completely'] = _dict.get(
                'exclude_tags_completely')
        if 'exclude_tags_keep_content' in _dict:
            args['exclude_tags_keep_content'] = _dict.get(
                'exclude_tags_keep_content')
        if 'keep_content' in _dict:
            args['keep_content'] = XPathPatterns._from_dict(
                _dict.get('keep_content'))
        if 'exclude_content' in _dict:
            args['exclude_content'] = XPathPatterns._from_dict(
                _dict.get('exclude_content'))
        if 'keep_tag_attributes' in _dict:
            args['keep_tag_attributes'] = _dict.get('keep_tag_attributes')
        if 'exclude_tag_attributes' in _dict:
            args['exclude_tag_attributes'] = _dict.get('exclude_tag_attributes')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HtmlSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'exclude_tags_completely'
                  ) and self.exclude_tags_completely is not None:
            _dict['exclude_tags_completely'] = self.exclude_tags_completely
        if hasattr(self, 'exclude_tags_keep_content'
                  ) and self.exclude_tags_keep_content is not None:
            _dict['exclude_tags_keep_content'] = self.exclude_tags_keep_content
        if hasattr(self, 'keep_content') and self.keep_content is not None:
            _dict['keep_content'] = self.keep_content._to_dict()
        if hasattr(self,
                   'exclude_content') and self.exclude_content is not None:
            _dict['exclude_content'] = self.exclude_content._to_dict()
        if hasattr(
                self,
                'keep_tag_attributes') and self.keep_tag_attributes is not None:
            _dict['keep_tag_attributes'] = self.keep_tag_attributes
        if hasattr(self, 'exclude_tag_attributes'
                  ) and self.exclude_tag_attributes is not None:
            _dict['exclude_tag_attributes'] = self.exclude_tag_attributes
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HtmlSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'HtmlSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HtmlSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IndexCapacity():
    """
    Details about the resource usage and capacity of the environment.

    :attr EnvironmentDocuments documents: (optional) Summary of the document usage
          statistics for the environment.
    :attr DiskUsage disk_usage: (optional) Summary of the disk usage statistics for
          the environment.
    :attr CollectionUsage collections: (optional) Summary of the collection usage in
          the environment.
    """

    def __init__(self,
                 *,
                 documents: 'EnvironmentDocuments' = None,
                 disk_usage: 'DiskUsage' = None,
                 collections: 'CollectionUsage' = None) -> None:
        """
        Initialize a IndexCapacity object.

        :param EnvironmentDocuments documents: (optional) Summary of the document
               usage statistics for the environment.
        :param DiskUsage disk_usage: (optional) Summary of the disk usage
               statistics for the environment.
        :param CollectionUsage collections: (optional) Summary of the collection
               usage in the environment.
        """
        self.documents = documents
        self.disk_usage = disk_usage
        self.collections = collections

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IndexCapacity':
        """Initialize a IndexCapacity object from a json dictionary."""
        args = {}
        valid_keys = ['documents', 'disk_usage', 'collections']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class IndexCapacity: '
                + ', '.join(bad_keys))
        if 'documents' in _dict:
            args['documents'] = EnvironmentDocuments._from_dict(
                _dict.get('documents'))
        if 'disk_usage' in _dict:
            args['disk_usage'] = DiskUsage._from_dict(_dict.get('disk_usage'))
        if 'collections' in _dict:
            args['collections'] = CollectionUsage._from_dict(
                _dict.get('collections'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexCapacity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'documents') and self.documents is not None:
            _dict['documents'] = self.documents._to_dict()
        if hasattr(self, 'disk_usage') and self.disk_usage is not None:
            _dict['disk_usage'] = self.disk_usage._to_dict()
        if hasattr(self, 'collections') and self.collections is not None:
            _dict['collections'] = self.collections._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IndexCapacity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'IndexCapacity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IndexCapacity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListCollectionFieldsResponse():
    """
    The list of fetched fields.
    The fields are returned using a fully qualified name format, however, the format
    differs slightly from that used by the query operations.
      * Fields which contain nested JSON objects are assigned a type of "nested".
      * Fields which belong to a nested object are prefixed with `.properties` (for
    example, `warnings.properties.severity` means that the `warnings` object has a
    property called `severity`).
      * Fields returned from the News collection are prefixed with
    `v{N}-fullnews-t3-{YEAR}.mappings` (for example,
    `v5-fullnews-t3-2016.mappings.text.properties.author`).

    :attr List[Field] fields: (optional) An array containing information about each
          field in the collections.
    """

    def __init__(self, *, fields: List['Field'] = None) -> None:
        """
        Initialize a ListCollectionFieldsResponse object.

        :param List[Field] fields: (optional) An array containing information about
               each field in the collections.
        """
        self.fields = fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCollectionFieldsResponse':
        """Initialize a ListCollectionFieldsResponse object from a json dictionary."""
        args = {}
        valid_keys = ['fields']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ListCollectionFieldsResponse: '
                + ', '.join(bad_keys))
        if 'fields' in _dict:
            args['fields'] = [
                Field._from_dict(x) for x in (_dict.get('fields'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCollectionFieldsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = [x._to_dict() for x in self.fields]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCollectionFieldsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ListCollectionFieldsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCollectionFieldsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListCollectionsResponse():
    """
    Response object containing an array of collection details.

    :attr List[Collection] collections: (optional) An array containing information
          about each collection in the environment.
    """

    def __init__(self, *, collections: List['Collection'] = None) -> None:
        """
        Initialize a ListCollectionsResponse object.

        :param List[Collection] collections: (optional) An array containing
               information about each collection in the environment.
        """
        self.collections = collections

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCollectionsResponse':
        """Initialize a ListCollectionsResponse object from a json dictionary."""
        args = {}
        valid_keys = ['collections']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ListCollectionsResponse: '
                + ', '.join(bad_keys))
        if 'collections' in _dict:
            args['collections'] = [
                Collection._from_dict(x) for x in (_dict.get('collections'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCollectionsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collections') and self.collections is not None:
            _dict['collections'] = [x._to_dict() for x in self.collections]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCollectionsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ListCollectionsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCollectionsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListConfigurationsResponse():
    """
    Object containing an array of available configurations.

    :attr List[Configuration] configurations: (optional) An array of configurations
          that are available for the service instance.
    """

    def __init__(self, *, configurations: List['Configuration'] = None) -> None:
        """
        Initialize a ListConfigurationsResponse object.

        :param List[Configuration] configurations: (optional) An array of
               configurations that are available for the service instance.
        """
        self.configurations = configurations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListConfigurationsResponse':
        """Initialize a ListConfigurationsResponse object from a json dictionary."""
        args = {}
        valid_keys = ['configurations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ListConfigurationsResponse: '
                + ', '.join(bad_keys))
        if 'configurations' in _dict:
            args['configurations'] = [
                Configuration._from_dict(x)
                for x in (_dict.get('configurations'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListConfigurationsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'configurations') and self.configurations is not None:
            _dict['configurations'] = [
                x._to_dict() for x in self.configurations
            ]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListConfigurationsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ListConfigurationsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListConfigurationsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListEnvironmentsResponse():
    """
    Response object containing an array of configured environments.

    :attr List[Environment] environments: (optional) An array of [environments] that
          are available for the service instance.
    """

    def __init__(self, *, environments: List['Environment'] = None) -> None:
        """
        Initialize a ListEnvironmentsResponse object.

        :param List[Environment] environments: (optional) An array of
               [environments] that are available for the service instance.
        """
        self.environments = environments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListEnvironmentsResponse':
        """Initialize a ListEnvironmentsResponse object from a json dictionary."""
        args = {}
        valid_keys = ['environments']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ListEnvironmentsResponse: '
                + ', '.join(bad_keys))
        if 'environments' in _dict:
            args['environments'] = [
                Environment._from_dict(x) for x in (_dict.get('environments'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEnvironmentsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environments') and self.environments is not None:
            _dict['environments'] = [x._to_dict() for x in self.environments]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListEnvironmentsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ListEnvironmentsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEnvironmentsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogQueryResponse():
    """
    Object containing results that match the requested **logs** query.

    :attr int matching_results: (optional) Number of matching results.
    :attr List[LogQueryResponseResult] results: (optional) Array of log query
          response results.
    """

    def __init__(self,
                 *,
                 matching_results: int = None,
                 results: List['LogQueryResponseResult'] = None) -> None:
        """
        Initialize a LogQueryResponse object.

        :param int matching_results: (optional) Number of matching results.
        :param List[LogQueryResponseResult] results: (optional) Array of log query
               response results.
        """
        self.matching_results = matching_results
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogQueryResponse':
        """Initialize a LogQueryResponse object from a json dictionary."""
        args = {}
        valid_keys = ['matching_results', 'results']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LogQueryResponse: '
                + ', '.join(bad_keys))
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'results' in _dict:
            args['results'] = [
                LogQueryResponseResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogQueryResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogQueryResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'LogQueryResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogQueryResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogQueryResponseResult():
    """
    Individual result object for a **logs** query. Each object represents either a query
    to a Discovery collection or an event that is associated with a query.

    :attr str environment_id: (optional) The environment ID that is associated with
          this log entry.
    :attr str customer_id: (optional) The **customer_id** label that was specified
          in the header of the query or event API call that corresponds to this log entry.
    :attr str document_type: (optional) The type of log entry returned.
           **query** indicates that the log represents the results of a call to the single
          collection **query** method.
           **event** indicates that the log represents  a call to the **events** API.
    :attr str natural_language_query: (optional) The value of the
          **natural_language_query** query parameter that was used to create these
          results. Only returned with logs of type **query**.
          **Note:** Other query parameters (such as **filter** or **deduplicate**) might
          have been used with this query, but are not recorded.
    :attr LogQueryResponseResultDocuments document_results: (optional) Object
          containing result information that was returned by the query used to create this
          log entry. Only returned with logs of type `query`.
    :attr datetime created_timestamp: (optional) Date that the log result was
          created. Returned in `YYYY-MM-DDThh:mm:ssZ` format.
    :attr datetime client_timestamp: (optional) Date specified by the user when
          recording an event. Returned in `YYYY-MM-DDThh:mm:ssZ` format. Only returned
          with logs of type **event**.
    :attr str query_id: (optional) Identifier that corresponds to the
          **natural_language_query** string used in the original or associated query. All
          **event** and **query** log entries that have the same original
          **natural_language_query** string also have them same **query_id**. This field
          can be used to recall all **event** and **query** log results that have the same
          original query (**event** logs do not contain the original
          **natural_language_query** field).
    :attr str session_token: (optional) Unique identifier (within a 24-hour period)
          that identifies a single `query` log and any `event` logs that were created for
          it.
          **Note:** If the exact same query is run at the exact same time on different
          days, the **session_token** for those queries might be identical. However, the
          **created_timestamp** differs.
          **Note:** Session tokens are case sensitive. To avoid matching on session tokens
          that are identical except for case, use the exact match operator (`::`) when you
          query for a specific session token.
    :attr str collection_id: (optional) The collection ID of the document associated
          with this event. Only returned with logs of type `event`.
    :attr int display_rank: (optional) The original display rank of the document
          associated with this event. Only returned with logs of type `event`.
    :attr str document_id: (optional) The document ID of the document associated
          with this event. Only returned with logs of type `event`.
    :attr str event_type: (optional) The type of event that this object respresents.
          Possible values are
           -  `query` the log of a query to a collection
           -  `click` the result of a call to the **events** endpoint.
    :attr str result_type: (optional) The type of result that this **event** is
          associated with. Only returned with logs of type `event`.
    """

    def __init__(self,
                 *,
                 environment_id: str = None,
                 customer_id: str = None,
                 document_type: str = None,
                 natural_language_query: str = None,
                 document_results: 'LogQueryResponseResultDocuments' = None,
                 created_timestamp: datetime = None,
                 client_timestamp: datetime = None,
                 query_id: str = None,
                 session_token: str = None,
                 collection_id: str = None,
                 display_rank: int = None,
                 document_id: str = None,
                 event_type: str = None,
                 result_type: str = None) -> None:
        """
        Initialize a LogQueryResponseResult object.

        :param str environment_id: (optional) The environment ID that is associated
               with this log entry.
        :param str customer_id: (optional) The **customer_id** label that was
               specified in the header of the query or event API call that corresponds to
               this log entry.
        :param str document_type: (optional) The type of log entry returned.
                **query** indicates that the log represents the results of a call to the
               single collection **query** method.
                **event** indicates that the log represents  a call to the **events** API.
        :param str natural_language_query: (optional) The value of the
               **natural_language_query** query parameter that was used to create these
               results. Only returned with logs of type **query**.
               **Note:** Other query parameters (such as **filter** or **deduplicate**)
               might  have been used with this query, but are not recorded.
        :param LogQueryResponseResultDocuments document_results: (optional) Object
               containing result information that was returned by the query used to create
               this log entry. Only returned with logs of type `query`.
        :param datetime created_timestamp: (optional) Date that the log result was
               created. Returned in `YYYY-MM-DDThh:mm:ssZ` format.
        :param datetime client_timestamp: (optional) Date specified by the user
               when recording an event. Returned in `YYYY-MM-DDThh:mm:ssZ` format. Only
               returned with logs of type **event**.
        :param str query_id: (optional) Identifier that corresponds to the
               **natural_language_query** string used in the original or associated query.
               All **event** and **query** log entries that have the same original
               **natural_language_query** string also have them same **query_id**. This
               field can be used to recall all **event** and **query** log results that
               have the same original query (**event** logs do not contain the original
               **natural_language_query** field).
        :param str session_token: (optional) Unique identifier (within a 24-hour
               period) that identifies a single `query` log and any `event` logs that were
               created for it.
               **Note:** If the exact same query is run at the exact same time on
               different days, the **session_token** for those queries might be identical.
               However, the **created_timestamp** differs.
               **Note:** Session tokens are case sensitive. To avoid matching on session
               tokens that are identical except for case, use the exact match operator
               (`::`) when you query for a specific session token.
        :param str collection_id: (optional) The collection ID of the document
               associated with this event. Only returned with logs of type `event`.
        :param int display_rank: (optional) The original display rank of the
               document associated with this event. Only returned with logs of type
               `event`.
        :param str document_id: (optional) The document ID of the document
               associated with this event. Only returned with logs of type `event`.
        :param str event_type: (optional) The type of event that this object
               respresents. Possible values are
                -  `query` the log of a query to a collection
                -  `click` the result of a call to the **events** endpoint.
        :param str result_type: (optional) The type of result that this **event**
               is associated with. Only returned with logs of type `event`.
        """
        self.environment_id = environment_id
        self.customer_id = customer_id
        self.document_type = document_type
        self.natural_language_query = natural_language_query
        self.document_results = document_results
        self.created_timestamp = created_timestamp
        self.client_timestamp = client_timestamp
        self.query_id = query_id
        self.session_token = session_token
        self.collection_id = collection_id
        self.display_rank = display_rank
        self.document_id = document_id
        self.event_type = event_type
        self.result_type = result_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogQueryResponseResult':
        """Initialize a LogQueryResponseResult object from a json dictionary."""
        args = {}
        valid_keys = [
            'environment_id', 'customer_id', 'document_type',
            'natural_language_query', 'document_results', 'created_timestamp',
            'client_timestamp', 'query_id', 'session_token', 'collection_id',
            'display_rank', 'document_id', 'event_type', 'result_type'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LogQueryResponseResult: '
                + ', '.join(bad_keys))
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'customer_id' in _dict:
            args['customer_id'] = _dict.get('customer_id')
        if 'document_type' in _dict:
            args['document_type'] = _dict.get('document_type')
        if 'natural_language_query' in _dict:
            args['natural_language_query'] = _dict.get('natural_language_query')
        if 'document_results' in _dict:
            args[
                'document_results'] = LogQueryResponseResultDocuments._from_dict(
                    _dict.get('document_results'))
        if 'created_timestamp' in _dict:
            args['created_timestamp'] = string_to_datetime(
                _dict.get('created_timestamp'))
        if 'client_timestamp' in _dict:
            args['client_timestamp'] = string_to_datetime(
                _dict.get('client_timestamp'))
        if 'query_id' in _dict:
            args['query_id'] = _dict.get('query_id')
        if 'session_token' in _dict:
            args['session_token'] = _dict.get('session_token')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'display_rank' in _dict:
            args['display_rank'] = _dict.get('display_rank')
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'event_type' in _dict:
            args['event_type'] = _dict.get('event_type')
        if 'result_type' in _dict:
            args['result_type'] = _dict.get('result_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogQueryResponseResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'customer_id') and self.customer_id is not None:
            _dict['customer_id'] = self.customer_id
        if hasattr(self, 'document_type') and self.document_type is not None:
            _dict['document_type'] = self.document_type
        if hasattr(self, 'natural_language_query'
                  ) and self.natural_language_query is not None:
            _dict['natural_language_query'] = self.natural_language_query
        if hasattr(self,
                   'document_results') and self.document_results is not None:
            _dict['document_results'] = self.document_results._to_dict()
        if hasattr(self,
                   'created_timestamp') and self.created_timestamp is not None:
            _dict['created_timestamp'] = datetime_to_string(
                self.created_timestamp)
        if hasattr(self,
                   'client_timestamp') and self.client_timestamp is not None:
            _dict['client_timestamp'] = datetime_to_string(
                self.client_timestamp)
        if hasattr(self, 'query_id') and self.query_id is not None:
            _dict['query_id'] = self.query_id
        if hasattr(self, 'session_token') and self.session_token is not None:
            _dict['session_token'] = self.session_token
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'display_rank') and self.display_rank is not None:
            _dict['display_rank'] = self.display_rank
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'event_type') and self.event_type is not None:
            _dict['event_type'] = self.event_type
        if hasattr(self, 'result_type') and self.result_type is not None:
            _dict['result_type'] = self.result_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogQueryResponseResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'LogQueryResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogQueryResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DocumentTypeEnum(Enum):
        """
        The type of log entry returned.
         **query** indicates that the log represents the results of a call to the single
        collection **query** method.
         **event** indicates that the log represents  a call to the **events** API.
        """
        QUERY = "query"
        EVENT = "event"

    class EventTypeEnum(Enum):
        """
        The type of event that this object respresents. Possible values are
         -  `query` the log of a query to a collection
         -  `click` the result of a call to the **events** endpoint.
        """
        CLICK = "click"
        QUERY = "query"

    class ResultTypeEnum(Enum):
        """
        The type of result that this **event** is associated with. Only returned with logs
        of type `event`.
        """
        DOCUMENT = "document"


class LogQueryResponseResultDocuments():
    """
    Object containing result information that was returned by the query used to create
    this log entry. Only returned with logs of type `query`.

    :attr List[LogQueryResponseResultDocumentsResult] results: (optional) Array of
          log query response results.
    :attr int count: (optional) The number of results returned in the query
          associate with this log.
    """

    def __init__(self,
                 *,
                 results: List['LogQueryResponseResultDocumentsResult'] = None,
                 count: int = None) -> None:
        """
        Initialize a LogQueryResponseResultDocuments object.

        :param List[LogQueryResponseResultDocumentsResult] results: (optional)
               Array of log query response results.
        :param int count: (optional) The number of results returned in the query
               associate with this log.
        """
        self.results = results
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogQueryResponseResultDocuments':
        """Initialize a LogQueryResponseResultDocuments object from a json dictionary."""
        args = {}
        valid_keys = ['results', 'count']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LogQueryResponseResultDocuments: '
                + ', '.join(bad_keys))
        if 'results' in _dict:
            args['results'] = [
                LogQueryResponseResultDocumentsResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogQueryResponseResultDocuments object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogQueryResponseResultDocuments object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'LogQueryResponseResultDocuments') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogQueryResponseResultDocuments') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogQueryResponseResultDocumentsResult():
    """
    Each object in the **results** array corresponds to an individual document returned by
    the original query.

    :attr int position: (optional) The result rank of this document. A position of
          `1` indicates that it was the first returned result.
    :attr str document_id: (optional) The **document_id** of the document that this
          result represents.
    :attr float score: (optional) The raw score of this result. A higher score
          indicates a greater match to the query parameters.
    :attr float confidence: (optional) The confidence score of the result's
          analysis. A higher score indicating greater confidence.
    :attr str collection_id: (optional) The **collection_id** of the document
          represented by this result.
    """

    def __init__(self,
                 *,
                 position: int = None,
                 document_id: str = None,
                 score: float = None,
                 confidence: float = None,
                 collection_id: str = None) -> None:
        """
        Initialize a LogQueryResponseResultDocumentsResult object.

        :param int position: (optional) The result rank of this document. A
               position of `1` indicates that it was the first returned result.
        :param str document_id: (optional) The **document_id** of the document that
               this result represents.
        :param float score: (optional) The raw score of this result. A higher score
               indicates a greater match to the query parameters.
        :param float confidence: (optional) The confidence score of the result's
               analysis. A higher score indicating greater confidence.
        :param str collection_id: (optional) The **collection_id** of the document
               represented by this result.
        """
        self.position = position
        self.document_id = document_id
        self.score = score
        self.confidence = confidence
        self.collection_id = collection_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogQueryResponseResultDocumentsResult':
        """Initialize a LogQueryResponseResultDocumentsResult object from a json dictionary."""
        args = {}
        valid_keys = [
            'position', 'document_id', 'score', 'confidence', 'collection_id'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LogQueryResponseResultDocumentsResult: '
                + ', '.join(bad_keys))
        if 'position' in _dict:
            args['position'] = _dict.get('position')
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogQueryResponseResultDocumentsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'position') and self.position is not None:
            _dict['position'] = self.position
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogQueryResponseResultDocumentsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'LogQueryResponseResultDocumentsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogQueryResponseResultDocumentsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetricAggregation():
    """
    An aggregation analyzing log information for queries and events.

    :attr str interval: (optional) The measurement interval for this metric. Metric
          intervals are always 1 day (`1d`).
    :attr str event_type: (optional) The event type associated with this metric
          result. This field, when present, will always be `click`.
    :attr List[MetricAggregationResult] results: (optional) Array of metric
          aggregation query results.
    """

    def __init__(self,
                 *,
                 interval: str = None,
                 event_type: str = None,
                 results: List['MetricAggregationResult'] = None) -> None:
        """
        Initialize a MetricAggregation object.

        :param str interval: (optional) The measurement interval for this metric.
               Metric intervals are always 1 day (`1d`).
        :param str event_type: (optional) The event type associated with this
               metric result. This field, when present, will always be `click`.
        :param List[MetricAggregationResult] results: (optional) Array of metric
               aggregation query results.
        """
        self.interval = interval
        self.event_type = event_type
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricAggregation':
        """Initialize a MetricAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['interval', 'event_type', 'results']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MetricAggregation: '
                + ', '.join(bad_keys))
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        if 'event_type' in _dict:
            args['event_type'] = _dict.get('event_type')
        if 'results' in _dict:
            args['results'] = [
                MetricAggregationResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'event_type') and self.event_type is not None:
            _dict['event_type'] = self.event_type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'MetricAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetricAggregationResult():
    """
    Aggregation result data for the requested metric.

    :attr datetime key_as_string: (optional) Date in string form representing the
          start of this interval.
    :attr int key: (optional) Unix epoch time equivalent of the **key_as_string**,
          that represents the start of this interval.
    :attr int matching_results: (optional) Number of matching results.
    :attr float event_rate: (optional) The number of queries with associated events
          divided by the total number of queries for the interval. Only returned with
          **event_rate** metrics.
    """

    def __init__(self,
                 *,
                 key_as_string: datetime = None,
                 key: int = None,
                 matching_results: int = None,
                 event_rate: float = None) -> None:
        """
        Initialize a MetricAggregationResult object.

        :param datetime key_as_string: (optional) Date in string form representing
               the start of this interval.
        :param int key: (optional) Unix epoch time equivalent of the
               **key_as_string**, that represents the start of this interval.
        :param int matching_results: (optional) Number of matching results.
        :param float event_rate: (optional) The number of queries with associated
               events divided by the total number of queries for the interval. Only
               returned with **event_rate** metrics.
        """
        self.key_as_string = key_as_string
        self.key = key
        self.matching_results = matching_results
        self.event_rate = event_rate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricAggregationResult':
        """Initialize a MetricAggregationResult object from a json dictionary."""
        args = {}
        valid_keys = ['key_as_string', 'key', 'matching_results', 'event_rate']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MetricAggregationResult: '
                + ', '.join(bad_keys))
        if 'key_as_string' in _dict:
            args['key_as_string'] = string_to_datetime(
                _dict.get('key_as_string'))
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'event_rate' in _dict:
            args['event_rate'] = _dict.get('event_rate')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key_as_string') and self.key_as_string is not None:
            _dict['key_as_string'] = datetime_to_string(self.key_as_string)
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'event_rate') and self.event_rate is not None:
            _dict['event_rate'] = self.event_rate
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricAggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'MetricAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetricResponse():
    """
    The response generated from a call to a **metrics** method.

    :attr List[MetricAggregation] aggregations: (optional) Array of metric
          aggregations.
    """

    def __init__(self,
                 *,
                 aggregations: List['MetricAggregation'] = None) -> None:
        """
        Initialize a MetricResponse object.

        :param List[MetricAggregation] aggregations: (optional) Array of metric
               aggregations.
        """
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricResponse':
        """Initialize a MetricResponse object from a json dictionary."""
        args = {}
        valid_keys = ['aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MetricResponse: '
                + ', '.join(bad_keys))
        if 'aggregations' in _dict:
            args['aggregations'] = [
                MetricAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'MetricResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetricTokenAggregation():
    """
    An aggregation analyzing log information for queries and events.

    :attr str event_type: (optional) The event type associated with this metric
          result. This field, when present, will always be `click`.
    :attr List[MetricTokenAggregationResult] results: (optional) Array of results
          for the metric token aggregation.
    """

    def __init__(self,
                 *,
                 event_type: str = None,
                 results: List['MetricTokenAggregationResult'] = None) -> None:
        """
        Initialize a MetricTokenAggregation object.

        :param str event_type: (optional) The event type associated with this
               metric result. This field, when present, will always be `click`.
        :param List[MetricTokenAggregationResult] results: (optional) Array of
               results for the metric token aggregation.
        """
        self.event_type = event_type
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricTokenAggregation':
        """Initialize a MetricTokenAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['event_type', 'results']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MetricTokenAggregation: '
                + ', '.join(bad_keys))
        if 'event_type' in _dict:
            args['event_type'] = _dict.get('event_type')
        if 'results' in _dict:
            args['results'] = [
                MetricTokenAggregationResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricTokenAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event_type') and self.event_type is not None:
            _dict['event_type'] = self.event_type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricTokenAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'MetricTokenAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricTokenAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetricTokenAggregationResult():
    """
    Aggregation result data for the requested metric.

    :attr str key: (optional) The content of the **natural_language_query**
          parameter used in the query that this result represents.
    :attr int matching_results: (optional) Number of matching results.
    :attr float event_rate: (optional) The number of queries with associated events
          divided by the total number of queries currently stored (queries and events are
          stored in the log for 30 days).
    """

    def __init__(self,
                 *,
                 key: str = None,
                 matching_results: int = None,
                 event_rate: float = None) -> None:
        """
        Initialize a MetricTokenAggregationResult object.

        :param str key: (optional) The content of the **natural_language_query**
               parameter used in the query that this result represents.
        :param int matching_results: (optional) Number of matching results.
        :param float event_rate: (optional) The number of queries with associated
               events divided by the total number of queries currently stored (queries and
               events are stored in the log for 30 days).
        """
        self.key = key
        self.matching_results = matching_results
        self.event_rate = event_rate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricTokenAggregationResult':
        """Initialize a MetricTokenAggregationResult object from a json dictionary."""
        args = {}
        valid_keys = ['key', 'matching_results', 'event_rate']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MetricTokenAggregationResult: '
                + ', '.join(bad_keys))
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'event_rate' in _dict:
            args['event_rate'] = _dict.get('event_rate')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricTokenAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'event_rate') and self.event_rate is not None:
            _dict['event_rate'] = self.event_rate
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricTokenAggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'MetricTokenAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricTokenAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetricTokenResponse():
    """
    The response generated from a call to a **metrics** method that evaluates tokens.

    :attr List[MetricTokenAggregation] aggregations: (optional) Array of metric
          token aggregations.
    """

    def __init__(self,
                 *,
                 aggregations: List['MetricTokenAggregation'] = None) -> None:
        """
        Initialize a MetricTokenResponse object.

        :param List[MetricTokenAggregation] aggregations: (optional) Array of
               metric token aggregations.
        """
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetricTokenResponse':
        """Initialize a MetricTokenResponse object from a json dictionary."""
        args = {}
        valid_keys = ['aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MetricTokenResponse: '
                + ', '.join(bad_keys))
        if 'aggregations' in _dict:
            args['aggregations'] = [
                MetricTokenAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetricTokenResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetricTokenResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'MetricTokenResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetricTokenResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentCategories():
    """
    An object that indicates the Categories enrichment will be applied to the specified
    field.

    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize a NluEnrichmentCategories object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentCategories':
        """Initialize a NluEnrichmentCategories object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        args.update(xtra)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentCategories object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __setattr__(self, name: str, value: object) -> None:
        properties = {}
        if not hasattr(self, '_additionalProperties'):
            super(NluEnrichmentCategories,
                  self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(NluEnrichmentCategories, self).__setattr__(name, value)

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentCategories object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentCategories') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentCategories') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentConcepts():
    """
    An object specifiying the concepts enrichment and related parameters.

    :attr int limit: (optional) The maximum number of concepts enrichments to extact
          from each instance of the specified field.
    """

    def __init__(self, *, limit: int = None) -> None:
        """
        Initialize a NluEnrichmentConcepts object.

        :param int limit: (optional) The maximum number of concepts enrichments to
               extact from each instance of the specified field.
        """
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentConcepts':
        """Initialize a NluEnrichmentConcepts object from a json dictionary."""
        args = {}
        valid_keys = ['limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentConcepts: '
                + ', '.join(bad_keys))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentConcepts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentConcepts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentConcepts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentConcepts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentEmotion():
    """
    An object specifying the emotion detection enrichment and related parameters.

    :attr bool document: (optional) When `true`, emotion detection is performed on
          the entire field.
    :attr List[str] targets: (optional) A comma-separated list of target strings
          that will have any associated emotions detected.
    """

    def __init__(self,
                 *,
                 document: bool = None,
                 targets: List[str] = None) -> None:
        """
        Initialize a NluEnrichmentEmotion object.

        :param bool document: (optional) When `true`, emotion detection is
               performed on the entire field.
        :param List[str] targets: (optional) A comma-separated list of target
               strings that will have any associated emotions detected.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentEmotion':
        """Initialize a NluEnrichmentEmotion object from a json dictionary."""
        args = {}
        valid_keys = ['document', 'targets']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentEmotion: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentEmotion object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentEmotion object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentEmotion') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentEmotion') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentEntities():
    """
    An object speficying the Entities enrichment and related parameters.

    :attr bool sentiment: (optional) When `true`, sentiment analysis of entities
          will be performed on the specified field.
    :attr bool emotion: (optional) When `true`, emotion detection of entities will
          be performed on the specified field.
    :attr int limit: (optional) The maximum number of entities to extract for each
          instance of the specified field.
    :attr bool mentions: (optional) When `true`, the number of mentions of each
          identified entity is recorded. The default is `false`.
    :attr bool mention_types: (optional) When `true`, the types of mentions for each
          idetifieid entity is recorded. The default is `false`.
    :attr bool sentence_locations: (optional) When `true`, a list of sentence
          locations for each instance of each identified entity is recorded. The default
          is `false`.
    :attr str model: (optional) The enrichement model to use with entity extraction.
          May be a custom model provided by Watson Knowledge Studio, or the default public
          model `alchemy`.
    """

    def __init__(self,
                 *,
                 sentiment: bool = None,
                 emotion: bool = None,
                 limit: int = None,
                 mentions: bool = None,
                 mention_types: bool = None,
                 sentence_locations: bool = None,
                 model: str = None) -> None:
        """
        Initialize a NluEnrichmentEntities object.

        :param bool sentiment: (optional) When `true`, sentiment analysis of
               entities will be performed on the specified field.
        :param bool emotion: (optional) When `true`, emotion detection of entities
               will be performed on the specified field.
        :param int limit: (optional) The maximum number of entities to extract for
               each instance of the specified field.
        :param bool mentions: (optional) When `true`, the number of mentions of
               each identified entity is recorded. The default is `false`.
        :param bool mention_types: (optional) When `true`, the types of mentions
               for each idetifieid entity is recorded. The default is `false`.
        :param bool sentence_locations: (optional) When `true`, a list of sentence
               locations for each instance of each identified entity is recorded. The
               default is `false`.
        :param str model: (optional) The enrichement model to use with entity
               extraction. May be a custom model provided by Watson Knowledge Studio, or
               the default public model `alchemy`.
        """
        self.sentiment = sentiment
        self.emotion = emotion
        self.limit = limit
        self.mentions = mentions
        self.mention_types = mention_types
        self.sentence_locations = sentence_locations
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentEntities':
        """Initialize a NluEnrichmentEntities object from a json dictionary."""
        args = {}
        valid_keys = [
            'sentiment', 'emotion', 'limit', 'mentions', 'mention_types',
            'sentence_locations', 'model'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentEntities: '
                + ', '.join(bad_keys))
        if 'sentiment' in _dict:
            args['sentiment'] = _dict.get('sentiment')
        if 'emotion' in _dict:
            args['emotion'] = _dict.get('emotion')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'mentions' in _dict:
            args['mentions'] = _dict.get('mentions')
        if 'mention_types' in _dict:
            args['mention_types'] = _dict.get('mention_types')
        if 'sentence_locations' in _dict:
            args['sentence_locations'] = _dict.get('sentence_locations')
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentEntities object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'mentions') and self.mentions is not None:
            _dict['mentions'] = self.mentions
        if hasattr(self, 'mention_types') and self.mention_types is not None:
            _dict['mention_types'] = self.mention_types
        if hasattr(
                self,
                'sentence_locations') and self.sentence_locations is not None:
            _dict['sentence_locations'] = self.sentence_locations
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentEntities object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentEntities') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentEntities') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentFeatures():
    """
    Object containing Natural Language Understanding features to be used.

    :attr NluEnrichmentKeywords keywords: (optional) An object specifying the
          Keyword enrichment and related parameters.
    :attr NluEnrichmentEntities entities: (optional) An object speficying the
          Entities enrichment and related parameters.
    :attr NluEnrichmentSentiment sentiment: (optional) An object specifying the
          sentiment extraction enrichment and related parameters.
    :attr NluEnrichmentEmotion emotion: (optional) An object specifying the emotion
          detection enrichment and related parameters.
    :attr NluEnrichmentCategories categories: (optional) An object that indicates
          the Categories enrichment will be applied to the specified field.
    :attr NluEnrichmentSemanticRoles semantic_roles: (optional) An object
          specifiying the semantic roles enrichment and related parameters.
    :attr NluEnrichmentRelations relations: (optional) An object specifying the
          relations enrichment and related parameters.
    :attr NluEnrichmentConcepts concepts: (optional) An object specifiying the
          concepts enrichment and related parameters.
    """

    def __init__(self,
                 *,
                 keywords: 'NluEnrichmentKeywords' = None,
                 entities: 'NluEnrichmentEntities' = None,
                 sentiment: 'NluEnrichmentSentiment' = None,
                 emotion: 'NluEnrichmentEmotion' = None,
                 categories: 'NluEnrichmentCategories' = None,
                 semantic_roles: 'NluEnrichmentSemanticRoles' = None,
                 relations: 'NluEnrichmentRelations' = None,
                 concepts: 'NluEnrichmentConcepts' = None) -> None:
        """
        Initialize a NluEnrichmentFeatures object.

        :param NluEnrichmentKeywords keywords: (optional) An object specifying the
               Keyword enrichment and related parameters.
        :param NluEnrichmentEntities entities: (optional) An object speficying the
               Entities enrichment and related parameters.
        :param NluEnrichmentSentiment sentiment: (optional) An object specifying
               the sentiment extraction enrichment and related parameters.
        :param NluEnrichmentEmotion emotion: (optional) An object specifying the
               emotion detection enrichment and related parameters.
        :param NluEnrichmentCategories categories: (optional) An object that
               indicates the Categories enrichment will be applied to the specified field.
        :param NluEnrichmentSemanticRoles semantic_roles: (optional) An object
               specifiying the semantic roles enrichment and related parameters.
        :param NluEnrichmentRelations relations: (optional) An object specifying
               the relations enrichment and related parameters.
        :param NluEnrichmentConcepts concepts: (optional) An object specifiying the
               concepts enrichment and related parameters.
        """
        self.keywords = keywords
        self.entities = entities
        self.sentiment = sentiment
        self.emotion = emotion
        self.categories = categories
        self.semantic_roles = semantic_roles
        self.relations = relations
        self.concepts = concepts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentFeatures':
        """Initialize a NluEnrichmentFeatures object from a json dictionary."""
        args = {}
        valid_keys = [
            'keywords', 'entities', 'sentiment', 'emotion', 'categories',
            'semantic_roles', 'relations', 'concepts'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentFeatures: '
                + ', '.join(bad_keys))
        if 'keywords' in _dict:
            args['keywords'] = NluEnrichmentKeywords._from_dict(
                _dict.get('keywords'))
        if 'entities' in _dict:
            args['entities'] = NluEnrichmentEntities._from_dict(
                _dict.get('entities'))
        if 'sentiment' in _dict:
            args['sentiment'] = NluEnrichmentSentiment._from_dict(
                _dict.get('sentiment'))
        if 'emotion' in _dict:
            args['emotion'] = NluEnrichmentEmotion._from_dict(
                _dict.get('emotion'))
        if 'categories' in _dict:
            args['categories'] = NluEnrichmentCategories._from_dict(
                _dict.get('categories'))
        if 'semantic_roles' in _dict:
            args['semantic_roles'] = NluEnrichmentSemanticRoles._from_dict(
                _dict.get('semantic_roles'))
        if 'relations' in _dict:
            args['relations'] = NluEnrichmentRelations._from_dict(
                _dict.get('relations'))
        if 'concepts' in _dict:
            args['concepts'] = NluEnrichmentConcepts._from_dict(
                _dict.get('concepts'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentFeatures object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords._to_dict()
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = self.entities._to_dict()
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment._to_dict()
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = self.categories._to_dict()
        if hasattr(self, 'semantic_roles') and self.semantic_roles is not None:
            _dict['semantic_roles'] = self.semantic_roles._to_dict()
        if hasattr(self, 'relations') and self.relations is not None:
            _dict['relations'] = self.relations._to_dict()
        if hasattr(self, 'concepts') and self.concepts is not None:
            _dict['concepts'] = self.concepts._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentFeatures object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentFeatures') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentFeatures') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentKeywords():
    """
    An object specifying the Keyword enrichment and related parameters.

    :attr bool sentiment: (optional) When `true`, sentiment analysis of keywords
          will be performed on the specified field.
    :attr bool emotion: (optional) When `true`, emotion detection of keywords will
          be performed on the specified field.
    :attr int limit: (optional) The maximum number of keywords to extract for each
          instance of the specified field.
    """

    def __init__(self,
                 *,
                 sentiment: bool = None,
                 emotion: bool = None,
                 limit: int = None) -> None:
        """
        Initialize a NluEnrichmentKeywords object.

        :param bool sentiment: (optional) When `true`, sentiment analysis of
               keywords will be performed on the specified field.
        :param bool emotion: (optional) When `true`, emotion detection of keywords
               will be performed on the specified field.
        :param int limit: (optional) The maximum number of keywords to extract for
               each instance of the specified field.
        """
        self.sentiment = sentiment
        self.emotion = emotion
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentKeywords':
        """Initialize a NluEnrichmentKeywords object from a json dictionary."""
        args = {}
        valid_keys = ['sentiment', 'emotion', 'limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentKeywords: '
                + ', '.join(bad_keys))
        if 'sentiment' in _dict:
            args['sentiment'] = _dict.get('sentiment')
        if 'emotion' in _dict:
            args['emotion'] = _dict.get('emotion')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentKeywords object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentKeywords object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentKeywords') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentKeywords') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentRelations():
    """
    An object specifying the relations enrichment and related parameters.

    :attr str model: (optional) *For use with `natural_language_understanding`
          enrichments only.* The enrichement model to use with relationship extraction.
          May be a custom model provided by Watson Knowledge Studio, the default public
          model is`en-news`.
    """

    def __init__(self, *, model: str = None) -> None:
        """
        Initialize a NluEnrichmentRelations object.

        :param str model: (optional) *For use with `natural_language_understanding`
               enrichments only.* The enrichement model to use with relationship
               extraction. May be a custom model provided by Watson Knowledge Studio, the
               default public model is`en-news`.
        """
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentRelations':
        """Initialize a NluEnrichmentRelations object from a json dictionary."""
        args = {}
        valid_keys = ['model']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentRelations: '
                + ', '.join(bad_keys))
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentRelations object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentRelations object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentRelations') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentRelations') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentSemanticRoles():
    """
    An object specifiying the semantic roles enrichment and related parameters.

    :attr bool entities: (optional) When `true`, entities are extracted from the
          identified sentence parts.
    :attr bool keywords: (optional) When `true`, keywords are extracted from the
          identified sentence parts.
    :attr int limit: (optional) The maximum number of semantic roles enrichments to
          extact from each instance of the specified field.
    """

    def __init__(self,
                 *,
                 entities: bool = None,
                 keywords: bool = None,
                 limit: int = None) -> None:
        """
        Initialize a NluEnrichmentSemanticRoles object.

        :param bool entities: (optional) When `true`, entities are extracted from
               the identified sentence parts.
        :param bool keywords: (optional) When `true`, keywords are extracted from
               the identified sentence parts.
        :param int limit: (optional) The maximum number of semantic roles
               enrichments to extact from each instance of the specified field.
        """
        self.entities = entities
        self.keywords = keywords
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentSemanticRoles':
        """Initialize a NluEnrichmentSemanticRoles object from a json dictionary."""
        args = {}
        valid_keys = ['entities', 'keywords', 'limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentSemanticRoles: '
                + ', '.join(bad_keys))
        if 'entities' in _dict:
            args['entities'] = _dict.get('entities')
        if 'keywords' in _dict:
            args['keywords'] = _dict.get('keywords')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentSemanticRoles object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = self.entities
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentSemanticRoles object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentSemanticRoles') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentSemanticRoles') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentSentiment():
    """
    An object specifying the sentiment extraction enrichment and related parameters.

    :attr bool document: (optional) When `true`, sentiment analysis is performed on
          the entire field.
    :attr List[str] targets: (optional) A comma-separated list of target strings
          that will have any associated sentiment analyzed.
    """

    def __init__(self,
                 *,
                 document: bool = None,
                 targets: List[str] = None) -> None:
        """
        Initialize a NluEnrichmentSentiment object.

        :param bool document: (optional) When `true`, sentiment analysis is
               performed on the entire field.
        :param List[str] targets: (optional) A comma-separated list of target
               strings that will have any associated sentiment analyzed.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NluEnrichmentSentiment':
        """Initialize a NluEnrichmentSentiment object from a json dictionary."""
        args = {}
        valid_keys = ['document', 'targets']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NluEnrichmentSentiment: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentSentiment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NluEnrichmentSentiment object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NluEnrichmentSentiment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NluEnrichmentSentiment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NormalizationOperation():
    """
    Object containing normalization operations.

    :attr str operation: (optional) Identifies what type of operation to perform.
          **copy** - Copies the value of the **source_field** to the **destination_field**
          field. If the **destination_field** already exists, then the value of the
          **source_field** overwrites the original value of the **destination_field**.
          **move** - Renames (moves) the **source_field** to the **destination_field**. If
          the **destination_field** already exists, then the value of the **source_field**
          overwrites the original value of the **destination_field**. Rename is identical
          to copy, except that the **source_field** is removed after the value has been
          copied to the **destination_field** (it is the same as a _copy_ followed by a
          _remove_).
          **merge** - Merges the value of the **source_field** with the value of the
          **destination_field**. The **destination_field** is converted into an array if
          it is not already an array, and the value of the **source_field** is appended to
          the array. This operation removes the **source_field** after the merge. If the
          **source_field** does not exist in the current document, then the
          **destination_field** is still converted into an array (if it is not an array
          already). This conversion ensures the type for **destination_field** is
          consistent across all documents.
          **remove** - Deletes the **source_field** field. The **destination_field** is
          ignored for this operation.
          **remove_nulls** - Removes all nested null (blank) field values from the
          ingested document. **source_field** and **destination_field** are ignored by
          this operation because _remove_nulls_ operates on the entire ingested document.
          Typically, **remove_nulls** is invoked as the last normalization operation (if
          it is invoked at all, it can be time-expensive).
    :attr str source_field: (optional) The source field for the operation.
    :attr str destination_field: (optional) The destination field for the operation.
    """

    def __init__(self,
                 *,
                 operation: str = None,
                 source_field: str = None,
                 destination_field: str = None) -> None:
        """
        Initialize a NormalizationOperation object.

        :param str operation: (optional) Identifies what type of operation to
               perform.
               **copy** - Copies the value of the **source_field** to the
               **destination_field** field. If the **destination_field** already exists,
               then the value of the **source_field** overwrites the original value of the
               **destination_field**.
               **move** - Renames (moves) the **source_field** to the
               **destination_field**. If the **destination_field** already exists, then
               the value of the **source_field** overwrites the original value of the
               **destination_field**. Rename is identical to copy, except that the
               **source_field** is removed after the value has been copied to the
               **destination_field** (it is the same as a _copy_ followed by a _remove_).
               **merge** - Merges the value of the **source_field** with the value of the
               **destination_field**. The **destination_field** is converted into an array
               if it is not already an array, and the value of the **source_field** is
               appended to the array. This operation removes the **source_field** after
               the merge. If the **source_field** does not exist in the current document,
               then the **destination_field** is still converted into an array (if it is
               not an array already). This conversion ensures the type for
               **destination_field** is consistent across all documents.
               **remove** - Deletes the **source_field** field. The **destination_field**
               is ignored for this operation.
               **remove_nulls** - Removes all nested null (blank) field values from the
               ingested document. **source_field** and **destination_field** are ignored
               by this operation because _remove_nulls_ operates on the entire ingested
               document. Typically, **remove_nulls** is invoked as the last normalization
               operation (if it is invoked at all, it can be time-expensive).
        :param str source_field: (optional) The source field for the operation.
        :param str destination_field: (optional) The destination field for the
               operation.
        """
        self.operation = operation
        self.source_field = source_field
        self.destination_field = destination_field

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NormalizationOperation':
        """Initialize a NormalizationOperation object from a json dictionary."""
        args = {}
        valid_keys = ['operation', 'source_field', 'destination_field']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class NormalizationOperation: '
                + ', '.join(bad_keys))
        if 'operation' in _dict:
            args['operation'] = _dict.get('operation')
        if 'source_field' in _dict:
            args['source_field'] = _dict.get('source_field')
        if 'destination_field' in _dict:
            args['destination_field'] = _dict.get('destination_field')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NormalizationOperation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operation') and self.operation is not None:
            _dict['operation'] = self.operation
        if hasattr(self, 'source_field') and self.source_field is not None:
            _dict['source_field'] = self.source_field
        if hasattr(self,
                   'destination_field') and self.destination_field is not None:
            _dict['destination_field'] = self.destination_field
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NormalizationOperation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'NormalizationOperation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NormalizationOperation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperationEnum(Enum):
        """
        Identifies what type of operation to perform.
        **copy** - Copies the value of the **source_field** to the **destination_field**
        field. If the **destination_field** already exists, then the value of the
        **source_field** overwrites the original value of the **destination_field**.
        **move** - Renames (moves) the **source_field** to the **destination_field**. If
        the **destination_field** already exists, then the value of the **source_field**
        overwrites the original value of the **destination_field**. Rename is identical to
        copy, except that the **source_field** is removed after the value has been copied
        to the **destination_field** (it is the same as a _copy_ followed by a _remove_).
        **merge** - Merges the value of the **source_field** with the value of the
        **destination_field**. The **destination_field** is converted into an array if it
        is not already an array, and the value of the **source_field** is appended to the
        array. This operation removes the **source_field** after the merge. If the
        **source_field** does not exist in the current document, then the
        **destination_field** is still converted into an array (if it is not an array
        already). This conversion ensures the type for **destination_field** is consistent
        across all documents.
        **remove** - Deletes the **source_field** field. The **destination_field** is
        ignored for this operation.
        **remove_nulls** - Removes all nested null (blank) field values from the ingested
        document. **source_field** and **destination_field** are ignored by this operation
        because _remove_nulls_ operates on the entire ingested document. Typically,
        **remove_nulls** is invoked as the last normalization operation (if it is invoked
        at all, it can be time-expensive).
        """
        COPY = "copy"
        MOVE = "move"
        MERGE = "merge"
        REMOVE = "remove"
        REMOVE_NULLS = "remove_nulls"


class Notice():
    """
    A notice produced for the collection.

    :attr str notice_id: (optional) Identifies the notice. Many notices might have
          the same ID. This field exists so that user applications can programmatically
          identify a notice and take automatic corrective action. Typical notice IDs
          include: `index_failed`, `index_failed_too_many_requests`,
          `index_failed_incompatible_field`, `index_failed_cluster_unavailable`,
          `ingestion_timeout`, `ingestion_error`, `bad_request`, `internal_error`,
          `missing_model`, `unsupported_model`,
          `smart_document_understanding_failed_incompatible_field`,
          `smart_document_understanding_failed_internal_error`,
          `smart_document_understanding_failed_internal_error`,
          `smart_document_understanding_failed_warning`,
          `smart_document_understanding_page_error`,
          `smart_document_understanding_page_warning`. **Note:** This is not a complete
          list, other values might be returned.
    :attr datetime created: (optional) The creation date of the collection in the
          format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str document_id: (optional) Unique identifier of the document.
    :attr str query_id: (optional) Unique identifier of the query used for relevance
          training.
    :attr str severity: (optional) Severity level of the notice.
    :attr str step: (optional) Ingestion or training step in which the notice
          occurred. Typical step values include: `classify_elements`,
          `smartDocumentUnderstanding`, `ingestion`, `indexing`, `convert`. **Note:** This
          is not a complete list, other values might be returned.
    :attr str description: (optional) The description of the notice.
    """

    def __init__(self,
                 *,
                 notice_id: str = None,
                 created: datetime = None,
                 document_id: str = None,
                 query_id: str = None,
                 severity: str = None,
                 step: str = None,
                 description: str = None) -> None:
        """
        Initialize a Notice object.

        :param str notice_id: (optional) Identifies the notice. Many notices might
               have the same ID. This field exists so that user applications can
               programmatically identify a notice and take automatic corrective action.
               Typical notice IDs include: `index_failed`,
               `index_failed_too_many_requests`, `index_failed_incompatible_field`,
               `index_failed_cluster_unavailable`, `ingestion_timeout`, `ingestion_error`,
               `bad_request`, `internal_error`, `missing_model`, `unsupported_model`,
               `smart_document_understanding_failed_incompatible_field`,
               `smart_document_understanding_failed_internal_error`,
               `smart_document_understanding_failed_internal_error`,
               `smart_document_understanding_failed_warning`,
               `smart_document_understanding_page_error`,
               `smart_document_understanding_page_warning`. **Note:** This is not a
               complete list, other values might be returned.
        :param datetime created: (optional) The creation date of the collection in
               the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str document_id: (optional) Unique identifier of the document.
        :param str query_id: (optional) Unique identifier of the query used for
               relevance training.
        :param str severity: (optional) Severity level of the notice.
        :param str step: (optional) Ingestion or training step in which the notice
               occurred. Typical step values include: `classify_elements`,
               `smartDocumentUnderstanding`, `ingestion`, `indexing`, `convert`. **Note:**
               This is not a complete list, other values might be returned.
        :param str description: (optional) The description of the notice.
        """
        self.notice_id = notice_id
        self.created = created
        self.document_id = document_id
        self.query_id = query_id
        self.severity = severity
        self.step = step
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Notice':
        """Initialize a Notice object from a json dictionary."""
        args = {}
        valid_keys = [
            'notice_id', 'created', 'document_id', 'query_id', 'severity',
            'step', 'description'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Notice: ' +
                ', '.join(bad_keys))
        if 'notice_id' in _dict:
            args['notice_id'] = _dict.get('notice_id')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'query_id' in _dict:
            args['query_id'] = _dict.get('query_id')
        if 'severity' in _dict:
            args['severity'] = _dict.get('severity')
        if 'step' in _dict:
            args['step'] = _dict.get('step')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Notice object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'notice_id') and self.notice_id is not None:
            _dict['notice_id'] = self.notice_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'query_id') and self.query_id is not None:
            _dict['query_id'] = self.query_id
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['severity'] = self.severity
        if hasattr(self, 'step') and self.step is not None:
            _dict['step'] = self.step
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Notice object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Notice') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Notice') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SeverityEnum(Enum):
        """
        Severity level of the notice.
        """
        WARNING = "warning"
        ERROR = "error"


class PdfHeadingDetection():
    """
    Object containing heading detection conversion settings for PDF documents.

    :attr List[FontSetting] fonts: (optional) Array of font matching configurations.
    """

    def __init__(self, *, fonts: List['FontSetting'] = None) -> None:
        """
        Initialize a PdfHeadingDetection object.

        :param List[FontSetting] fonts: (optional) Array of font matching
               configurations.
        """
        self.fonts = fonts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PdfHeadingDetection':
        """Initialize a PdfHeadingDetection object from a json dictionary."""
        args = {}
        valid_keys = ['fonts']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class PdfHeadingDetection: '
                + ', '.join(bad_keys))
        if 'fonts' in _dict:
            args['fonts'] = [
                FontSetting._from_dict(x) for x in (_dict.get('fonts'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PdfHeadingDetection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fonts') and self.fonts is not None:
            _dict['fonts'] = [x._to_dict() for x in self.fonts]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PdfHeadingDetection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'PdfHeadingDetection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PdfHeadingDetection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PdfSettings():
    """
    A list of PDF conversion settings.

    :attr PdfHeadingDetection heading: (optional) Object containing heading
          detection conversion settings for PDF documents.
    """

    def __init__(self, *, heading: 'PdfHeadingDetection' = None) -> None:
        """
        Initialize a PdfSettings object.

        :param PdfHeadingDetection heading: (optional) Object containing heading
               detection conversion settings for PDF documents.
        """
        self.heading = heading

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PdfSettings':
        """Initialize a PdfSettings object from a json dictionary."""
        args = {}
        valid_keys = ['heading']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class PdfSettings: '
                + ', '.join(bad_keys))
        if 'heading' in _dict:
            args['heading'] = PdfHeadingDetection._from_dict(
                _dict.get('heading'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PdfSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'heading') and self.heading is not None:
            _dict['heading'] = self.heading._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PdfSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'PdfSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PdfSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregation():
    """
    An aggregation produced by  Discovery to analyze the input provided.

    :attr str type: (optional) The type of aggregation command used. For example:
          term, filter, max, min, etc.
    :attr List[AggregationResult] results: (optional) Array of aggregation results.
    :attr int matching_results: (optional) Number of matching results.
    :attr List[QueryAggregation] aggregations: (optional) Aggregations returned by
          Discovery.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None) -> None:
        """
        Initialize a QueryAggregation object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregation':
        """Initialize a QueryAggregation object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        args = {}
        valid_keys = ['type', 'results', 'matching_results', 'aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryAggregation: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['histogram'] = 'Histogram'
        mapping['max'] = 'Calculation'
        mapping['min'] = 'Calculation'
        mapping['average'] = 'Calculation'
        mapping['sum'] = 'Calculation'
        mapping['unique_count'] = 'Calculation'
        mapping['term'] = 'Term'
        mapping['filter'] = 'Filter'
        mapping['nested'] = 'Nested'
        mapping['timeslice'] = 'Timeslice'
        mapping['top_hits'] = 'TopHits'
        disc_value = _dict.get('type')
        if disc_value is None:
            raise ValueError(
                'Discriminator property \'type\' not found in QueryAggregation JSON'
            )
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class QueryNoticesResponse():
    """
    Object containing notice query results.

    :attr int matching_results: (optional) The number of matching results.
    :attr List[QueryNoticesResult] results: (optional) Array of document results
          that match the query.
    :attr List[QueryAggregation] aggregations: (optional) Array of aggregation
          results that match the query.
    :attr List[QueryPassages] passages: (optional) Array of passage results that
          match the query.
    :attr int duplicates_removed: (optional) The number of duplicates removed from
          this notices query.
    """

    def __init__(self,
                 *,
                 matching_results: int = None,
                 results: List['QueryNoticesResult'] = None,
                 aggregations: List['QueryAggregation'] = None,
                 passages: List['QueryPassages'] = None,
                 duplicates_removed: int = None) -> None:
        """
        Initialize a QueryNoticesResponse object.

        :param int matching_results: (optional) The number of matching results.
        :param List[QueryNoticesResult] results: (optional) Array of document
               results that match the query.
        :param List[QueryAggregation] aggregations: (optional) Array of aggregation
               results that match the query.
        :param List[QueryPassages] passages: (optional) Array of passage results
               that match the query.
        :param int duplicates_removed: (optional) The number of duplicates removed
               from this notices query.
        """
        self.matching_results = matching_results
        self.results = results
        self.aggregations = aggregations
        self.passages = passages
        self.duplicates_removed = duplicates_removed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryNoticesResponse':
        """Initialize a QueryNoticesResponse object from a json dictionary."""
        args = {}
        valid_keys = [
            'matching_results', 'results', 'aggregations', 'passages',
            'duplicates_removed'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryNoticesResponse: '
                + ', '.join(bad_keys))
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'results' in _dict:
            args['results'] = [
                QueryNoticesResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'passages' in _dict:
            args['passages'] = [
                QueryPassages._from_dict(x) for x in (_dict.get('passages'))
            ]
        if 'duplicates_removed' in _dict:
            args['duplicates_removed'] = _dict.get('duplicates_removed')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryNoticesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'passages') and self.passages is not None:
            _dict['passages'] = [x._to_dict() for x in self.passages]
        if hasattr(
                self,
                'duplicates_removed') and self.duplicates_removed is not None:
            _dict['duplicates_removed'] = self.duplicates_removed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryNoticesResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'QueryNoticesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryNoticesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryNoticesResult():
    """
    Query result object.

    :attr str id: (optional) The unique identifier of the document.
    :attr dict metadata: (optional) Metadata of the document.
    :attr str collection_id: (optional) The collection ID of the collection
          containing the document for this result.
    :attr QueryResultMetadata result_metadata: (optional) Metadata of a query
          result.
    :attr int code: (optional) The internal status code returned by the ingestion
          subsystem indicating the overall result of ingesting the source document.
    :attr str filename: (optional) Name of the original source file (if available).
    :attr str file_type: (optional) The type of the original source file.
    :attr str sha1: (optional) The SHA-1 hash of the original source file (formatted
          as a hexadecimal string).
    :attr List[Notice] notices: (optional) Array of notices for the document.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 metadata: dict = None,
                 collection_id: str = None,
                 result_metadata: 'QueryResultMetadata' = None,
                 code: int = None,
                 filename: str = None,
                 file_type: str = None,
                 sha1: str = None,
                 notices: List['Notice'] = None,
                 **kwargs) -> None:
        """
        Initialize a QueryNoticesResult object.

        :param str id: (optional) The unique identifier of the document.
        :param dict metadata: (optional) Metadata of the document.
        :param str collection_id: (optional) The collection ID of the collection
               containing the document for this result.
        :param QueryResultMetadata result_metadata: (optional) Metadata of a query
               result.
        :param int code: (optional) The internal status code returned by the
               ingestion subsystem indicating the overall result of ingesting the source
               document.
        :param str filename: (optional) Name of the original source file (if
               available).
        :param str file_type: (optional) The type of the original source file.
        :param str sha1: (optional) The SHA-1 hash of the original source file
               (formatted as a hexadecimal string).
        :param List[Notice] notices: (optional) Array of notices for the document.
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.metadata = metadata
        self.collection_id = collection_id
        self.result_metadata = result_metadata
        self.code = code
        self.filename = filename
        self.file_type = file_type
        self.sha1 = sha1
        self.notices = notices
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryNoticesResult':
        """Initialize a QueryNoticesResult object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict.get('id')
            del xtra['id']
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
            del xtra['metadata']
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
            del xtra['collection_id']
        if 'result_metadata' in _dict:
            args['result_metadata'] = QueryResultMetadata._from_dict(
                _dict.get('result_metadata'))
            del xtra['result_metadata']
        if 'code' in _dict:
            args['code'] = _dict.get('code')
            del xtra['code']
        if 'filename' in _dict:
            args['filename'] = _dict.get('filename')
            del xtra['filename']
        if 'file_type' in _dict:
            args['file_type'] = _dict.get('file_type')
            del xtra['file_type']
        if 'sha1' in _dict:
            args['sha1'] = _dict.get('sha1')
            del xtra['sha1']
        if 'notices' in _dict:
            args['notices'] = [
                Notice._from_dict(x) for x in (_dict.get('notices'))
            ]
            del xtra['notices']
        args.update(xtra)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryNoticesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self,
                   'result_metadata') and self.result_metadata is not None:
            _dict['result_metadata'] = self.result_metadata._to_dict()
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'filename') and self.filename is not None:
            _dict['filename'] = self.filename
        if hasattr(self, 'file_type') and self.file_type is not None:
            _dict['file_type'] = self.file_type
        if hasattr(self, 'sha1') and self.sha1 is not None:
            _dict['sha1'] = self.sha1
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = [x._to_dict() for x in self.notices]
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __setattr__(self, name: str, value: object) -> None:
        properties = {
            'id', 'metadata', 'collection_id', 'result_metadata', 'code',
            'filename', 'file_type', 'sha1', 'notices'
        }
        if not hasattr(self, '_additionalProperties'):
            super(QueryNoticesResult, self).__setattr__('_additionalProperties',
                                                        set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(QueryNoticesResult, self).__setattr__(name, value)

    def __str__(self) -> str:
        """Return a `str` version of this QueryNoticesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'QueryNoticesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryNoticesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FileTypeEnum(Enum):
        """
        The type of the original source file.
        """
        PDF = "pdf"
        HTML = "html"
        WORD = "word"
        JSON = "json"


class QueryPassages():
    """
    A passage query result.

    :attr str document_id: (optional) The unique identifier of the document from
          which the passage has been extracted.
    :attr float passage_score: (optional) The confidence score of the passages's
          analysis. A higher score indicates greater confidence.
    :attr str passage_text: (optional) The content of the extracted passage.
    :attr int start_offset: (optional) The position of the first character of the
          extracted passage in the originating field.
    :attr int end_offset: (optional) The position of the last character of the
          extracted passage in the originating field.
    :attr str field: (optional) The label of the field from which the passage has
          been extracted.
    """

    def __init__(self,
                 *,
                 document_id: str = None,
                 passage_score: float = None,
                 passage_text: str = None,
                 start_offset: int = None,
                 end_offset: int = None,
                 field: str = None) -> None:
        """
        Initialize a QueryPassages object.

        :param str document_id: (optional) The unique identifier of the document
               from which the passage has been extracted.
        :param float passage_score: (optional) The confidence score of the
               passages's analysis. A higher score indicates greater confidence.
        :param str passage_text: (optional) The content of the extracted passage.
        :param int start_offset: (optional) The position of the first character of
               the extracted passage in the originating field.
        :param int end_offset: (optional) The position of the last character of the
               extracted passage in the originating field.
        :param str field: (optional) The label of the field from which the passage
               has been extracted.
        """
        self.document_id = document_id
        self.passage_score = passage_score
        self.passage_text = passage_text
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.field = field

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryPassages':
        """Initialize a QueryPassages object from a json dictionary."""
        args = {}
        valid_keys = [
            'document_id', 'passage_score', 'passage_text', 'start_offset',
            'end_offset', 'field'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryPassages: '
                + ', '.join(bad_keys))
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'passage_score' in _dict:
            args['passage_score'] = _dict.get('passage_score')
        if 'passage_text' in _dict:
            args['passage_text'] = _dict.get('passage_text')
        if 'start_offset' in _dict:
            args['start_offset'] = _dict.get('start_offset')
        if 'end_offset' in _dict:
            args['end_offset'] = _dict.get('end_offset')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryPassages object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'passage_score') and self.passage_score is not None:
            _dict['passage_score'] = self.passage_score
        if hasattr(self, 'passage_text') and self.passage_text is not None:
            _dict['passage_text'] = self.passage_text
        if hasattr(self, 'start_offset') and self.start_offset is not None:
            _dict['start_offset'] = self.start_offset
        if hasattr(self, 'end_offset') and self.end_offset is not None:
            _dict['end_offset'] = self.end_offset
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryPassages object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'QueryPassages') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryPassages') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResponse():
    """
    A response containing the documents and aggregations for the query.

    :attr int matching_results: (optional) The number of matching results for the
          query.
    :attr List[QueryResult] results: (optional) Array of document results for the
          query.
    :attr List[QueryAggregation] aggregations: (optional) Array of aggregation
          results for the query.
    :attr List[QueryPassages] passages: (optional) Array of passage results for the
          query.
    :attr int duplicates_removed: (optional) The number of duplicate results
          removed.
    :attr str session_token: (optional) The session token for this query. The
          session token can be used to add events associated with this query to the query
          and event log.
          **Important:** Session tokens are case sensitive.
    :attr RetrievalDetails retrieval_details: (optional) An object contain retrieval
          type information.
    :attr str suggested_query: (optional) The suggestions for a misspelled natural
          language query.
    """

    def __init__(self,
                 *,
                 matching_results: int = None,
                 results: List['QueryResult'] = None,
                 aggregations: List['QueryAggregation'] = None,
                 passages: List['QueryPassages'] = None,
                 duplicates_removed: int = None,
                 session_token: str = None,
                 retrieval_details: 'RetrievalDetails' = None,
                 suggested_query: str = None) -> None:
        """
        Initialize a QueryResponse object.

        :param int matching_results: (optional) The number of matching results for
               the query.
        :param List[QueryResult] results: (optional) Array of document results for
               the query.
        :param List[QueryAggregation] aggregations: (optional) Array of aggregation
               results for the query.
        :param List[QueryPassages] passages: (optional) Array of passage results
               for the query.
        :param int duplicates_removed: (optional) The number of duplicate results
               removed.
        :param str session_token: (optional) The session token for this query. The
               session token can be used to add events associated with this query to the
               query and event log.
               **Important:** Session tokens are case sensitive.
        :param RetrievalDetails retrieval_details: (optional) An object contain
               retrieval type information.
        :param str suggested_query: (optional) The suggestions for a misspelled
               natural language query.
        """
        self.matching_results = matching_results
        self.results = results
        self.aggregations = aggregations
        self.passages = passages
        self.duplicates_removed = duplicates_removed
        self.session_token = session_token
        self.retrieval_details = retrieval_details
        self.suggested_query = suggested_query

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResponse':
        """Initialize a QueryResponse object from a json dictionary."""
        args = {}
        valid_keys = [
            'matching_results', 'results', 'aggregations', 'passages',
            'duplicates_removed', 'session_token', 'retrieval_details',
            'suggested_query'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryResponse: '
                + ', '.join(bad_keys))
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'results' in _dict:
            args['results'] = [
                QueryResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'passages' in _dict:
            args['passages'] = [
                QueryPassages._from_dict(x) for x in (_dict.get('passages'))
            ]
        if 'duplicates_removed' in _dict:
            args['duplicates_removed'] = _dict.get('duplicates_removed')
        if 'session_token' in _dict:
            args['session_token'] = _dict.get('session_token')
        if 'retrieval_details' in _dict:
            args['retrieval_details'] = RetrievalDetails._from_dict(
                _dict.get('retrieval_details'))
        if 'suggested_query' in _dict:
            args['suggested_query'] = _dict.get('suggested_query')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'passages') and self.passages is not None:
            _dict['passages'] = [x._to_dict() for x in self.passages]
        if hasattr(
                self,
                'duplicates_removed') and self.duplicates_removed is not None:
            _dict['duplicates_removed'] = self.duplicates_removed
        if hasattr(self, 'session_token') and self.session_token is not None:
            _dict['session_token'] = self.session_token
        if hasattr(self,
                   'retrieval_details') and self.retrieval_details is not None:
            _dict['retrieval_details'] = self.retrieval_details._to_dict()
        if hasattr(self,
                   'suggested_query') and self.suggested_query is not None:
            _dict['suggested_query'] = self.suggested_query
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'QueryResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResult():
    """
    Query result object.

    :attr str id: (optional) The unique identifier of the document.
    :attr dict metadata: (optional) Metadata of the document.
    :attr str collection_id: (optional) The collection ID of the collection
          containing the document for this result.
    :attr QueryResultMetadata result_metadata: (optional) Metadata of a query
          result.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 metadata: dict = None,
                 collection_id: str = None,
                 result_metadata: 'QueryResultMetadata' = None,
                 **kwargs) -> None:
        """
        Initialize a QueryResult object.

        :param str id: (optional) The unique identifier of the document.
        :param dict metadata: (optional) Metadata of the document.
        :param str collection_id: (optional) The collection ID of the collection
               containing the document for this result.
        :param QueryResultMetadata result_metadata: (optional) Metadata of a query
               result.
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.metadata = metadata
        self.collection_id = collection_id
        self.result_metadata = result_metadata
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResult':
        """Initialize a QueryResult object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict.get('id')
            del xtra['id']
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
            del xtra['metadata']
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
            del xtra['collection_id']
        if 'result_metadata' in _dict:
            args['result_metadata'] = QueryResultMetadata._from_dict(
                _dict.get('result_metadata'))
            del xtra['result_metadata']
        args.update(xtra)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self,
                   'result_metadata') and self.result_metadata is not None:
            _dict['result_metadata'] = self.result_metadata._to_dict()
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __setattr__(self, name: str, value: object) -> None:
        properties = {'id', 'metadata', 'collection_id', 'result_metadata'}
        if not hasattr(self, '_additionalProperties'):
            super(QueryResult, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(QueryResult, self).__setattr__(name, value)

    def __str__(self) -> str:
        """Return a `str` version of this QueryResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'QueryResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResultMetadata():
    """
    Metadata of a query result.

    :attr float score: An unbounded measure of the relevance of a particular result,
          dependent on the query and matching document. A higher score indicates a greater
          match to the query parameters.
    :attr float confidence: (optional) The confidence score for the given result.
          Calculated based on how relevant the result is estimated to be. confidence can
          range from `0.0` to `1.0`. The higher the number, the more relevant the
          document. The `confidence` value for a result was calculated using the model
          specified in the `document_retrieval_strategy` field of the result set.
    """

    def __init__(self, score: float, *, confidence: float = None) -> None:
        """
        Initialize a QueryResultMetadata object.

        :param float score: An unbounded measure of the relevance of a particular
               result, dependent on the query and matching document. A higher score
               indicates a greater match to the query parameters.
        :param float confidence: (optional) The confidence score for the given
               result. Calculated based on how relevant the result is estimated to be.
               confidence can range from `0.0` to `1.0`. The higher the number, the more
               relevant the document. The `confidence` value for a result was calculated
               using the model specified in the `document_retrieval_strategy` field of the
               result set.
        """
        self.score = score
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResultMetadata':
        """Initialize a QueryResultMetadata object from a json dictionary."""
        args = {}
        valid_keys = ['score', 'confidence']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryResultMetadata: '
                + ', '.join(bad_keys))
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        else:
            raise ValueError(
                'Required property \'score\' not present in QueryResultMetadata JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResultMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryResultMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'QueryResultMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryResultMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RetrievalDetails():
    """
    An object contain retrieval type information.

    :attr str document_retrieval_strategy: (optional) Indentifies the document
          retrieval strategy used for this query. `relevancy_training` indicates that the
          results were returned using a relevancy trained model.
          `continuous_relevancy_training` indicates that the results were returned using
          the continuous relevancy training model created by result feedback analysis.
          `untrained` means the results were returned using the standard untrained model.
           **Note**: In the event of trained collections being queried, but the trained
          model is not used to return results, the **document_retrieval_strategy** will be
          listed as `untrained`.
    """

    def __init__(self, *, document_retrieval_strategy: str = None) -> None:
        """
        Initialize a RetrievalDetails object.

        :param str document_retrieval_strategy: (optional) Indentifies the document
               retrieval strategy used for this query. `relevancy_training` indicates that
               the results were returned using a relevancy trained model.
               `continuous_relevancy_training` indicates that the results were returned
               using the continuous relevancy training model created by result feedback
               analysis. `untrained` means the results were returned using the standard
               untrained model.
                **Note**: In the event of trained collections being queried, but the
               trained model is not used to return results, the
               **document_retrieval_strategy** will be listed as `untrained`.
        """
        self.document_retrieval_strategy = document_retrieval_strategy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RetrievalDetails':
        """Initialize a RetrievalDetails object from a json dictionary."""
        args = {}
        valid_keys = ['document_retrieval_strategy']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RetrievalDetails: '
                + ', '.join(bad_keys))
        if 'document_retrieval_strategy' in _dict:
            args['document_retrieval_strategy'] = _dict.get(
                'document_retrieval_strategy')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RetrievalDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_retrieval_strategy'
                  ) and self.document_retrieval_strategy is not None:
            _dict[
                'document_retrieval_strategy'] = self.document_retrieval_strategy
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RetrievalDetails object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'RetrievalDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RetrievalDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DocumentRetrievalStrategyEnum(Enum):
        """
        Indentifies the document retrieval strategy used for this query.
        `relevancy_training` indicates that the results were returned using a relevancy
        trained model. `continuous_relevancy_training` indicates that the results were
        returned using the continuous relevancy training model created by result feedback
        analysis. `untrained` means the results were returned using the standard untrained
        model.
         **Note**: In the event of trained collections being queried, but the trained
        model is not used to return results, the **document_retrieval_strategy** will be
        listed as `untrained`.
        """
        UNTRAINED = "untrained"
        RELEVANCY_TRAINING = "relevancy_training"
        CONTINUOUS_RELEVANCY_TRAINING = "continuous_relevancy_training"


class SduStatus():
    """
    Object containing smart document understanding information for this collection.

    :attr bool enabled: (optional) When `true`, smart document understanding
          conversion is enabled for this collection. All collections created with a
          version date after `2019-04-30` have smart document understanding enabled. If
          `false`, documents added to the collection are converted using the
          **conversion** settings specified in the configuration associated with the
          collection.
    :attr int total_annotated_pages: (optional) The total number of pages annotated
          using smart document understanding in this collection.
    :attr int total_pages: (optional) The current number of pages that can be used
          for training smart document understanding. The `total_pages` number is
          calculated as the total number of pages identified from the documents listed in
          the **total_documents** field.
    :attr int total_documents: (optional) The total number of documents in this
          collection that can be used to train smart document understanding. For **lite**
          plan collections, the maximum is the first 20 uploaded documents (not including
          HTML or JSON documents). For other plans, the maximum is the first 40 uploaded
          documents (not including HTML or JSON documents). When the maximum is reached,
          additional documents uploaded to the collection are not considered for training
          smart document understanding.
    :attr SduStatusCustomFields custom_fields: (optional) Information about custom
          smart document understanding fields that exist in this collection.
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 total_annotated_pages: int = None,
                 total_pages: int = None,
                 total_documents: int = None,
                 custom_fields: 'SduStatusCustomFields' = None) -> None:
        """
        Initialize a SduStatus object.

        :param bool enabled: (optional) When `true`, smart document understanding
               conversion is enabled for this collection. All collections created with a
               version date after `2019-04-30` have smart document understanding enabled.
               If `false`, documents added to the collection are converted using the
               **conversion** settings specified in the configuration associated with the
               collection.
        :param int total_annotated_pages: (optional) The total number of pages
               annotated using smart document understanding in this collection.
        :param int total_pages: (optional) The current number of pages that can be
               used for training smart document understanding. The `total_pages` number is
               calculated as the total number of pages identified from the documents
               listed in the **total_documents** field.
        :param int total_documents: (optional) The total number of documents in
               this collection that can be used to train smart document understanding. For
               **lite** plan collections, the maximum is the first 20 uploaded documents
               (not including HTML or JSON documents). For other plans, the maximum is the
               first 40 uploaded documents (not including HTML or JSON documents). When
               the maximum is reached, additional documents uploaded to the collection are
               not considered for training smart document understanding.
        :param SduStatusCustomFields custom_fields: (optional) Information about
               custom smart document understanding fields that exist in this collection.
        """
        self.enabled = enabled
        self.total_annotated_pages = total_annotated_pages
        self.total_pages = total_pages
        self.total_documents = total_documents
        self.custom_fields = custom_fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SduStatus':
        """Initialize a SduStatus object from a json dictionary."""
        args = {}
        valid_keys = [
            'enabled', 'total_annotated_pages', 'total_pages',
            'total_documents', 'custom_fields'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SduStatus: '
                + ', '.join(bad_keys))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'total_annotated_pages' in _dict:
            args['total_annotated_pages'] = _dict.get('total_annotated_pages')
        if 'total_pages' in _dict:
            args['total_pages'] = _dict.get('total_pages')
        if 'total_documents' in _dict:
            args['total_documents'] = _dict.get('total_documents')
        if 'custom_fields' in _dict:
            args['custom_fields'] = SduStatusCustomFields._from_dict(
                _dict.get('custom_fields'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SduStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'total_annotated_pages'
                  ) and self.total_annotated_pages is not None:
            _dict['total_annotated_pages'] = self.total_annotated_pages
        if hasattr(self, 'total_pages') and self.total_pages is not None:
            _dict['total_pages'] = self.total_pages
        if hasattr(self,
                   'total_documents') and self.total_documents is not None:
            _dict['total_documents'] = self.total_documents
        if hasattr(self, 'custom_fields') and self.custom_fields is not None:
            _dict['custom_fields'] = self.custom_fields._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SduStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SduStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SduStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SduStatusCustomFields():
    """
    Information about custom smart document understanding fields that exist in this
    collection.

    :attr int defined: (optional) The number of custom fields defined for this
          collection.
    :attr int maximum_allowed: (optional) The maximum number of custom fields that
          are allowed in this collection.
    """

    def __init__(self,
                 *,
                 defined: int = None,
                 maximum_allowed: int = None) -> None:
        """
        Initialize a SduStatusCustomFields object.

        :param int defined: (optional) The number of custom fields defined for this
               collection.
        :param int maximum_allowed: (optional) The maximum number of custom fields
               that are allowed in this collection.
        """
        self.defined = defined
        self.maximum_allowed = maximum_allowed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SduStatusCustomFields':
        """Initialize a SduStatusCustomFields object from a json dictionary."""
        args = {}
        valid_keys = ['defined', 'maximum_allowed']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SduStatusCustomFields: '
                + ', '.join(bad_keys))
        if 'defined' in _dict:
            args['defined'] = _dict.get('defined')
        if 'maximum_allowed' in _dict:
            args['maximum_allowed'] = _dict.get('maximum_allowed')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SduStatusCustomFields object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'defined') and self.defined is not None:
            _dict['defined'] = self.defined
        if hasattr(self,
                   'maximum_allowed') and self.maximum_allowed is not None:
            _dict['maximum_allowed'] = self.maximum_allowed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SduStatusCustomFields object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SduStatusCustomFields') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SduStatusCustomFields') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchStatus():
    """
    Information about the Continuous Relevancy Training for this environment.

    :attr str scope: (optional) Current scope of the training. Always returned as
          `environment`.
    :attr str status: (optional) The current status of Continuous Relevancy Training
          for this environment.
    :attr str status_description: (optional) Long description of the current
          Continuous Relevancy Training status.
    :attr date last_trained: (optional) The date stamp of the most recent completed
          training for this environment.
    """

    def __init__(self,
                 *,
                 scope: str = None,
                 status: str = None,
                 status_description: str = None,
                 last_trained: date = None) -> None:
        """
        Initialize a SearchStatus object.

        :param str scope: (optional) Current scope of the training. Always returned
               as `environment`.
        :param str status: (optional) The current status of Continuous Relevancy
               Training for this environment.
        :param str status_description: (optional) Long description of the current
               Continuous Relevancy Training status.
        :param date last_trained: (optional) The date stamp of the most recent
               completed training for this environment.
        """
        self.scope = scope
        self.status = status
        self.status_description = status_description
        self.last_trained = last_trained

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchStatus':
        """Initialize a SearchStatus object from a json dictionary."""
        args = {}
        valid_keys = ['scope', 'status', 'status_description', 'last_trained']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SearchStatus: '
                + ', '.join(bad_keys))
        if 'scope' in _dict:
            args['scope'] = _dict.get('scope')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'status_description' in _dict:
            args['status_description'] = _dict.get('status_description')
        if 'last_trained' in _dict:
            args['last_trained'] = _dict.get('last_trained')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scope') and self.scope is not None:
            _dict['scope'] = self.scope
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(
                self,
                'status_description') and self.status_description is not None:
            _dict['status_description'] = self.status_description
        if hasattr(self, 'last_trained') and self.last_trained is not None:
            _dict['last_trained'] = self.last_trained
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SearchStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        The current status of Continuous Relevancy Training for this environment.
        """
        NO_DATA = "NO_DATA"
        INSUFFICENT_DATA = "INSUFFICENT_DATA"
        TRAINING = "TRAINING"
        TRAINED = "TRAINED"
        NOT_APPLICABLE = "NOT_APPLICABLE"


class SegmentSettings():
    """
    A list of Document Segmentation settings.

    :attr bool enabled: (optional) Enables/disables the Document Segmentation
          feature.
    :attr List[str] selector_tags: (optional) Defines the heading level that splits
          into document segments. Valid values are h1, h2, h3, h4, h5, h6. The content of
          the header field that the segmentation splits at is used as the **title** field
          for that segmented result. Only valid if used with a collection that has
          **enabled** set to `false` in the **smart_document_understanding** object.
    :attr List[str] annotated_fields: (optional) Defines the annotated smart
          document understanding fields that the document is split on. The content of the
          annotated field that the segmentation splits at is used as the **title** field
          for that segmented result. For example, if the field `sub-title` is specified,
          when a document is uploaded each time the smart documement understanding
          conversion encounters a field of type `sub-title` the document is split at that
          point and the content of the field used as the title of the remaining content.
          Thnis split is performed for all instances of the listed fields in the uploaded
          document. Only valid if used with a collection that has **enabled** set to
          `true` in the **smart_document_understanding** object.
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 selector_tags: List[str] = None,
                 annotated_fields: List[str] = None) -> None:
        """
        Initialize a SegmentSettings object.

        :param bool enabled: (optional) Enables/disables the Document Segmentation
               feature.
        :param List[str] selector_tags: (optional) Defines the heading level that
               splits into document segments. Valid values are h1, h2, h3, h4, h5, h6. The
               content of the header field that the segmentation splits at is used as the
               **title** field for that segmented result. Only valid if used with a
               collection that has **enabled** set to `false` in the
               **smart_document_understanding** object.
        :param List[str] annotated_fields: (optional) Defines the annotated smart
               document understanding fields that the document is split on. The content of
               the annotated field that the segmentation splits at is used as the
               **title** field for that segmented result. For example, if the field
               `sub-title` is specified, when a document is uploaded each time the smart
               documement understanding conversion encounters a field of type `sub-title`
               the document is split at that point and the content of the field used as
               the title of the remaining content. Thnis split is performed for all
               instances of the listed fields in the uploaded document. Only valid if used
               with a collection that has **enabled** set to `true` in the
               **smart_document_understanding** object.
        """
        self.enabled = enabled
        self.selector_tags = selector_tags
        self.annotated_fields = annotated_fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SegmentSettings':
        """Initialize a SegmentSettings object from a json dictionary."""
        args = {}
        valid_keys = ['enabled', 'selector_tags', 'annotated_fields']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SegmentSettings: '
                + ', '.join(bad_keys))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'selector_tags' in _dict:
            args['selector_tags'] = _dict.get('selector_tags')
        if 'annotated_fields' in _dict:
            args['annotated_fields'] = _dict.get('annotated_fields')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SegmentSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'selector_tags') and self.selector_tags is not None:
            _dict['selector_tags'] = self.selector_tags
        if hasattr(self,
                   'annotated_fields') and self.annotated_fields is not None:
            _dict['annotated_fields'] = self.annotated_fields
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SegmentSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SegmentSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SegmentSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Source():
    """
    Object containing source parameters for the configuration.

    :attr str type: (optional) The type of source to connect to.
          -  `box` indicates the configuration is to connect an instance of Enterprise
          Box.
          -  `salesforce` indicates the configuration is to connect to Salesforce.
          -  `sharepoint` indicates the configuration is to connect to Microsoft
          SharePoint Online.
          -  `web_crawl` indicates the configuration is to perform a web page crawl.
          -  `cloud_object_storage` indicates the configuration is to connect to a cloud
          object store.
    :attr str credential_id: (optional) The **credential_id** of the credentials to
          use to connect to the source. Credentials are defined using the **credentials**
          method. The **source_type** of the credentials used must match the **type**
          field specified in this object.
    :attr SourceSchedule schedule: (optional) Object containing the schedule
          information for the source.
    :attr SourceOptions options: (optional) The **options** object defines which
          items to crawl from the source system.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 credential_id: str = None,
                 schedule: 'SourceSchedule' = None,
                 options: 'SourceOptions' = None) -> None:
        """
        Initialize a Source object.

        :param str type: (optional) The type of source to connect to.
               -  `box` indicates the configuration is to connect an instance of
               Enterprise Box.
               -  `salesforce` indicates the configuration is to connect to Salesforce.
               -  `sharepoint` indicates the configuration is to connect to Microsoft
               SharePoint Online.
               -  `web_crawl` indicates the configuration is to perform a web page crawl.
               -  `cloud_object_storage` indicates the configuration is to connect to a
               cloud object store.
        :param str credential_id: (optional) The **credential_id** of the
               credentials to use to connect to the source. Credentials are defined using
               the **credentials** method. The **source_type** of the credentials used
               must match the **type** field specified in this object.
        :param SourceSchedule schedule: (optional) Object containing the schedule
               information for the source.
        :param SourceOptions options: (optional) The **options** object defines
               which items to crawl from the source system.
        """
        self.type = type
        self.credential_id = credential_id
        self.schedule = schedule
        self.options = options

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Source':
        """Initialize a Source object from a json dictionary."""
        args = {}
        valid_keys = ['type', 'credential_id', 'schedule', 'options']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Source: ' +
                ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'credential_id' in _dict:
            args['credential_id'] = _dict.get('credential_id')
        if 'schedule' in _dict:
            args['schedule'] = SourceSchedule._from_dict(_dict.get('schedule'))
        if 'options' in _dict:
            args['options'] = SourceOptions._from_dict(_dict.get('options'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Source object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'credential_id') and self.credential_id is not None:
            _dict['credential_id'] = self.credential_id
        if hasattr(self, 'schedule') and self.schedule is not None:
            _dict['schedule'] = self.schedule._to_dict()
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = self.options._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Source object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Source') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Source') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        The type of source to connect to.
        -  `box` indicates the configuration is to connect an instance of Enterprise Box.
        -  `salesforce` indicates the configuration is to connect to Salesforce.
        -  `sharepoint` indicates the configuration is to connect to Microsoft SharePoint
        Online.
        -  `web_crawl` indicates the configuration is to perform a web page crawl.
        -  `cloud_object_storage` indicates the configuration is to connect to a cloud
        object store.
        """
        BOX = "box"
        SALESFORCE = "salesforce"
        SHAREPOINT = "sharepoint"
        WEB_CRAWL = "web_crawl"
        CLOUD_OBJECT_STORAGE = "cloud_object_storage"


class SourceOptions():
    """
    The **options** object defines which items to crawl from the source system.

    :attr List[SourceOptionsFolder] folders: (optional) Array of folders to crawl
          from the Box source. Only valid, and required, when the **type** field of the
          **source** object is set to `box`.
    :attr List[SourceOptionsObject] objects: (optional) Array of Salesforce document
          object types to crawl from the Salesforce source. Only valid, and required, when
          the **type** field of the **source** object is set to `salesforce`.
    :attr List[SourceOptionsSiteColl] site_collections: (optional) Array of
          Microsoft SharePointoint Online site collections to crawl from the SharePoint
          source. Only valid and required when the **type** field of the **source** object
          is set to `sharepoint`.
    :attr List[SourceOptionsWebCrawl] urls: (optional) Array of Web page URLs to
          begin crawling the web from. Only valid and required when the **type** field of
          the **source** object is set to `web_crawl`.
    :attr List[SourceOptionsBuckets] buckets: (optional) Array of cloud object store
          buckets to begin crawling. Only valid and required when the **type** field of
          the **source** object is set to `cloud_object_store`, and the
          **crawl_all_buckets** field is `false` or not specified.
    :attr bool crawl_all_buckets: (optional) When `true`, all buckets in the
          specified cloud object store are crawled. If set to `true`, the **buckets**
          array must not be specified.
    """

    def __init__(self,
                 *,
                 folders: List['SourceOptionsFolder'] = None,
                 objects: List['SourceOptionsObject'] = None,
                 site_collections: List['SourceOptionsSiteColl'] = None,
                 urls: List['SourceOptionsWebCrawl'] = None,
                 buckets: List['SourceOptionsBuckets'] = None,
                 crawl_all_buckets: bool = None) -> None:
        """
        Initialize a SourceOptions object.

        :param List[SourceOptionsFolder] folders: (optional) Array of folders to
               crawl from the Box source. Only valid, and required, when the **type**
               field of the **source** object is set to `box`.
        :param List[SourceOptionsObject] objects: (optional) Array of Salesforce
               document object types to crawl from the Salesforce source. Only valid, and
               required, when the **type** field of the **source** object is set to
               `salesforce`.
        :param List[SourceOptionsSiteColl] site_collections: (optional) Array of
               Microsoft SharePointoint Online site collections to crawl from the
               SharePoint source. Only valid and required when the **type** field of the
               **source** object is set to `sharepoint`.
        :param List[SourceOptionsWebCrawl] urls: (optional) Array of Web page URLs
               to begin crawling the web from. Only valid and required when the **type**
               field of the **source** object is set to `web_crawl`.
        :param List[SourceOptionsBuckets] buckets: (optional) Array of cloud object
               store buckets to begin crawling. Only valid and required when the **type**
               field of the **source** object is set to `cloud_object_store`, and the
               **crawl_all_buckets** field is `false` or not specified.
        :param bool crawl_all_buckets: (optional) When `true`, all buckets in the
               specified cloud object store are crawled. If set to `true`, the **buckets**
               array must not be specified.
        """
        self.folders = folders
        self.objects = objects
        self.site_collections = site_collections
        self.urls = urls
        self.buckets = buckets
        self.crawl_all_buckets = crawl_all_buckets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceOptions':
        """Initialize a SourceOptions object from a json dictionary."""
        args = {}
        valid_keys = [
            'folders', 'objects', 'site_collections', 'urls', 'buckets',
            'crawl_all_buckets'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceOptions: '
                + ', '.join(bad_keys))
        if 'folders' in _dict:
            args['folders'] = [
                SourceOptionsFolder._from_dict(x)
                for x in (_dict.get('folders'))
            ]
        if 'objects' in _dict:
            args['objects'] = [
                SourceOptionsObject._from_dict(x)
                for x in (_dict.get('objects'))
            ]
        if 'site_collections' in _dict:
            args['site_collections'] = [
                SourceOptionsSiteColl._from_dict(x)
                for x in (_dict.get('site_collections'))
            ]
        if 'urls' in _dict:
            args['urls'] = [
                SourceOptionsWebCrawl._from_dict(x) for x in (_dict.get('urls'))
            ]
        if 'buckets' in _dict:
            args['buckets'] = [
                SourceOptionsBuckets._from_dict(x)
                for x in (_dict.get('buckets'))
            ]
        if 'crawl_all_buckets' in _dict:
            args['crawl_all_buckets'] = _dict.get('crawl_all_buckets')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'folders') and self.folders is not None:
            _dict['folders'] = [x._to_dict() for x in self.folders]
        if hasattr(self, 'objects') and self.objects is not None:
            _dict['objects'] = [x._to_dict() for x in self.objects]
        if hasattr(self,
                   'site_collections') and self.site_collections is not None:
            _dict['site_collections'] = [
                x._to_dict() for x in self.site_collections
            ]
        if hasattr(self, 'urls') and self.urls is not None:
            _dict['urls'] = [x._to_dict() for x in self.urls]
        if hasattr(self, 'buckets') and self.buckets is not None:
            _dict['buckets'] = [x._to_dict() for x in self.buckets]
        if hasattr(self,
                   'crawl_all_buckets') and self.crawl_all_buckets is not None:
            _dict['crawl_all_buckets'] = self.crawl_all_buckets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SourceOptionsBuckets():
    """
    Object defining a cloud object store bucket to crawl.

    :attr str name: The name of the cloud object store bucket to crawl.
    :attr int limit: (optional) The number of documents to crawl from this cloud
          object store bucket. If not specified, all documents in the bucket are crawled.
    """

    def __init__(self, name: str, *, limit: int = None) -> None:
        """
        Initialize a SourceOptionsBuckets object.

        :param str name: The name of the cloud object store bucket to crawl.
        :param int limit: (optional) The number of documents to crawl from this
               cloud object store bucket. If not specified, all documents in the bucket
               are crawled.
        """
        self.name = name
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceOptionsBuckets':
        """Initialize a SourceOptionsBuckets object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceOptionsBuckets: '
                + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in SourceOptionsBuckets JSON'
            )
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceOptionsBuckets object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceOptionsBuckets object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceOptionsBuckets') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceOptionsBuckets') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SourceOptionsFolder():
    """
    Object that defines a box folder to crawl with this configuration.

    :attr str owner_user_id: The Box user ID of the user who owns the folder to
          crawl.
    :attr str folder_id: The Box folder ID of the folder to crawl.
    :attr int limit: (optional) The maximum number of documents to crawl for this
          folder. By default, all documents in the folder are crawled.
    """

    def __init__(self,
                 owner_user_id: str,
                 folder_id: str,
                 *,
                 limit: int = None) -> None:
        """
        Initialize a SourceOptionsFolder object.

        :param str owner_user_id: The Box user ID of the user who owns the folder
               to crawl.
        :param str folder_id: The Box folder ID of the folder to crawl.
        :param int limit: (optional) The maximum number of documents to crawl for
               this folder. By default, all documents in the folder are crawled.
        """
        self.owner_user_id = owner_user_id
        self.folder_id = folder_id
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceOptionsFolder':
        """Initialize a SourceOptionsFolder object from a json dictionary."""
        args = {}
        valid_keys = ['owner_user_id', 'folder_id', 'limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceOptionsFolder: '
                + ', '.join(bad_keys))
        if 'owner_user_id' in _dict:
            args['owner_user_id'] = _dict.get('owner_user_id')
        else:
            raise ValueError(
                'Required property \'owner_user_id\' not present in SourceOptionsFolder JSON'
            )
        if 'folder_id' in _dict:
            args['folder_id'] = _dict.get('folder_id')
        else:
            raise ValueError(
                'Required property \'folder_id\' not present in SourceOptionsFolder JSON'
            )
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceOptionsFolder object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'owner_user_id') and self.owner_user_id is not None:
            _dict['owner_user_id'] = self.owner_user_id
        if hasattr(self, 'folder_id') and self.folder_id is not None:
            _dict['folder_id'] = self.folder_id
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceOptionsFolder object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceOptionsFolder') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceOptionsFolder') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SourceOptionsObject():
    """
    Object that defines a Salesforce document object type crawl with this configuration.

    :attr str name: The name of the Salesforce document object to crawl. For
          example, `case`.
    :attr int limit: (optional) The maximum number of documents to crawl for this
          document object. By default, all documents in the document object are crawled.
    """

    def __init__(self, name: str, *, limit: int = None) -> None:
        """
        Initialize a SourceOptionsObject object.

        :param str name: The name of the Salesforce document object to crawl. For
               example, `case`.
        :param int limit: (optional) The maximum number of documents to crawl for
               this document object. By default, all documents in the document object are
               crawled.
        """
        self.name = name
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceOptionsObject':
        """Initialize a SourceOptionsObject object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceOptionsObject: '
                + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in SourceOptionsObject JSON'
            )
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceOptionsObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceOptionsObject object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceOptionsObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceOptionsObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SourceOptionsSiteColl():
    """
    Object that defines a Microsoft SharePoint site collection to crawl with this
    configuration.

    :attr str site_collection_path: The Microsoft SharePoint Online site collection
          path to crawl. The path must be be relative to the **organization_url** that was
          specified in the credentials associated with this source configuration.
    :attr int limit: (optional) The maximum number of documents to crawl for this
          site collection. By default, all documents in the site collection are crawled.
    """

    def __init__(self, site_collection_path: str, *, limit: int = None) -> None:
        """
        Initialize a SourceOptionsSiteColl object.

        :param str site_collection_path: The Microsoft SharePoint Online site
               collection path to crawl. The path must be be relative to the
               **organization_url** that was specified in the credentials associated with
               this source configuration.
        :param int limit: (optional) The maximum number of documents to crawl for
               this site collection. By default, all documents in the site collection are
               crawled.
        """
        self.site_collection_path = site_collection_path
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceOptionsSiteColl':
        """Initialize a SourceOptionsSiteColl object from a json dictionary."""
        args = {}
        valid_keys = ['site_collection_path', 'limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceOptionsSiteColl: '
                + ', '.join(bad_keys))
        if 'site_collection_path' in _dict:
            args['site_collection_path'] = _dict.get('site_collection_path')
        else:
            raise ValueError(
                'Required property \'site_collection_path\' not present in SourceOptionsSiteColl JSON'
            )
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceOptionsSiteColl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'site_collection_path'
                  ) and self.site_collection_path is not None:
            _dict['site_collection_path'] = self.site_collection_path
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceOptionsSiteColl object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceOptionsSiteColl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceOptionsSiteColl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SourceOptionsWebCrawl():
    """
    Object defining which URL to crawl and how to crawl it.

    :attr str url: The starting URL to crawl.
    :attr bool limit_to_starting_hosts: (optional) When `true`, crawls of the
          specified URL are limited to the host part of the **url** field.
    :attr str crawl_speed: (optional) The number of concurrent URLs to fetch.
          `gentle` means one URL is fetched at a time with a delay between each call.
          `normal` means as many as two URLs are fectched concurrently with a short delay
          between fetch calls. `aggressive` means that up to ten URLs are fetched
          concurrently with a short delay between fetch calls.
    :attr bool allow_untrusted_certificate: (optional) When `true`, allows the crawl
          to interact with HTTPS sites with SSL certificates with untrusted signers.
    :attr int maximum_hops: (optional) The maximum number of hops to make from the
          initial URL. When a page is crawled each link on that page will also be crawled
          if it is within the **maximum_hops** from the initial URL. The first page
          crawled is 0 hops, each link crawled from the first page is 1 hop, each link
          crawled from those pages is 2 hops, and so on.
    :attr int request_timeout: (optional) The maximum milliseconds to wait for a
          response from the web server.
    :attr bool override_robots_txt: (optional) When `true`, the crawler will ignore
          any `robots.txt` encountered by the crawler. This should only ever be done when
          crawling a web site the user owns. This must be be set to `true` when a
          **gateway_id** is specied in the **credentials**.
    :attr List[str] blacklist: (optional) Array of URL's to be excluded while
          crawling. The crawler will not follow links which contains this string. For
          example, listing `https://ibm.com/watson` also excludes
          `https://ibm.com/watson/discovery`.
    """

    def __init__(self,
                 url: str,
                 *,
                 limit_to_starting_hosts: bool = None,
                 crawl_speed: str = None,
                 allow_untrusted_certificate: bool = None,
                 maximum_hops: int = None,
                 request_timeout: int = None,
                 override_robots_txt: bool = None,
                 blacklist: List[str] = None) -> None:
        """
        Initialize a SourceOptionsWebCrawl object.

        :param str url: The starting URL to crawl.
        :param bool limit_to_starting_hosts: (optional) When `true`, crawls of the
               specified URL are limited to the host part of the **url** field.
        :param str crawl_speed: (optional) The number of concurrent URLs to fetch.
               `gentle` means one URL is fetched at a time with a delay between each call.
               `normal` means as many as two URLs are fectched concurrently with a short
               delay between fetch calls. `aggressive` means that up to ten URLs are
               fetched concurrently with a short delay between fetch calls.
        :param bool allow_untrusted_certificate: (optional) When `true`, allows the
               crawl to interact with HTTPS sites with SSL certificates with untrusted
               signers.
        :param int maximum_hops: (optional) The maximum number of hops to make from
               the initial URL. When a page is crawled each link on that page will also be
               crawled if it is within the **maximum_hops** from the initial URL. The
               first page crawled is 0 hops, each link crawled from the first page is 1
               hop, each link crawled from those pages is 2 hops, and so on.
        :param int request_timeout: (optional) The maximum milliseconds to wait for
               a response from the web server.
        :param bool override_robots_txt: (optional) When `true`, the crawler will
               ignore any `robots.txt` encountered by the crawler. This should only ever
               be done when crawling a web site the user owns. This must be be set to
               `true` when a **gateway_id** is specied in the **credentials**.
        :param List[str] blacklist: (optional) Array of URL's to be excluded while
               crawling. The crawler will not follow links which contains this string. For
               example, listing `https://ibm.com/watson` also excludes
               `https://ibm.com/watson/discovery`.
        """
        self.url = url
        self.limit_to_starting_hosts = limit_to_starting_hosts
        self.crawl_speed = crawl_speed
        self.allow_untrusted_certificate = allow_untrusted_certificate
        self.maximum_hops = maximum_hops
        self.request_timeout = request_timeout
        self.override_robots_txt = override_robots_txt
        self.blacklist = blacklist

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceOptionsWebCrawl':
        """Initialize a SourceOptionsWebCrawl object from a json dictionary."""
        args = {}
        valid_keys = [
            'url', 'limit_to_starting_hosts', 'crawl_speed',
            'allow_untrusted_certificate', 'maximum_hops', 'request_timeout',
            'override_robots_txt', 'blacklist'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceOptionsWebCrawl: '
                + ', '.join(bad_keys))
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in SourceOptionsWebCrawl JSON'
            )
        if 'limit_to_starting_hosts' in _dict:
            args['limit_to_starting_hosts'] = _dict.get(
                'limit_to_starting_hosts')
        if 'crawl_speed' in _dict:
            args['crawl_speed'] = _dict.get('crawl_speed')
        if 'allow_untrusted_certificate' in _dict:
            args['allow_untrusted_certificate'] = _dict.get(
                'allow_untrusted_certificate')
        if 'maximum_hops' in _dict:
            args['maximum_hops'] = _dict.get('maximum_hops')
        if 'request_timeout' in _dict:
            args['request_timeout'] = _dict.get('request_timeout')
        if 'override_robots_txt' in _dict:
            args['override_robots_txt'] = _dict.get('override_robots_txt')
        if 'blacklist' in _dict:
            args['blacklist'] = _dict.get('blacklist')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceOptionsWebCrawl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'limit_to_starting_hosts'
                  ) and self.limit_to_starting_hosts is not None:
            _dict['limit_to_starting_hosts'] = self.limit_to_starting_hosts
        if hasattr(self, 'crawl_speed') and self.crawl_speed is not None:
            _dict['crawl_speed'] = self.crawl_speed
        if hasattr(self, 'allow_untrusted_certificate'
                  ) and self.allow_untrusted_certificate is not None:
            _dict[
                'allow_untrusted_certificate'] = self.allow_untrusted_certificate
        if hasattr(self, 'maximum_hops') and self.maximum_hops is not None:
            _dict['maximum_hops'] = self.maximum_hops
        if hasattr(self,
                   'request_timeout') and self.request_timeout is not None:
            _dict['request_timeout'] = self.request_timeout
        if hasattr(
                self,
                'override_robots_txt') and self.override_robots_txt is not None:
            _dict['override_robots_txt'] = self.override_robots_txt
        if hasattr(self, 'blacklist') and self.blacklist is not None:
            _dict['blacklist'] = self.blacklist
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceOptionsWebCrawl object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceOptionsWebCrawl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceOptionsWebCrawl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CrawlSpeedEnum(Enum):
        """
        The number of concurrent URLs to fetch. `gentle` means one URL is fetched at a
        time with a delay between each call. `normal` means as many as two URLs are
        fectched concurrently with a short delay between fetch calls. `aggressive` means
        that up to ten URLs are fetched concurrently with a short delay between fetch
        calls.
        """
        GENTLE = "gentle"
        NORMAL = "normal"
        AGGRESSIVE = "aggressive"


class SourceSchedule():
    """
    Object containing the schedule information for the source.

    :attr bool enabled: (optional) When `true`, the source is re-crawled based on
          the **frequency** field in this object. When `false` the source is not
          re-crawled; When `false` and connecting to Salesforce the source is crawled
          annually.
    :attr str time_zone: (optional) The time zone to base source crawl times on.
          Possible values correspond to the IANA (Internet Assigned Numbers Authority)
          time zones list.
    :attr str frequency: (optional) The crawl schedule in the specified
          **time_zone**.
          -  `five_minutes`: Runs every five minutes.
          -  `hourly`: Runs every hour.
          -  `daily`: Runs every day between 00:00 and 06:00.
          -  `weekly`: Runs every week on Sunday between 00:00 and 06:00.
          -  `monthly`: Runs the on the first Sunday of every month between 00:00 and
          06:00.
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 time_zone: str = None,
                 frequency: str = None) -> None:
        """
        Initialize a SourceSchedule object.

        :param bool enabled: (optional) When `true`, the source is re-crawled based
               on the **frequency** field in this object. When `false` the source is not
               re-crawled; When `false` and connecting to Salesforce the source is crawled
               annually.
        :param str time_zone: (optional) The time zone to base source crawl times
               on. Possible values correspond to the IANA (Internet Assigned Numbers
               Authority) time zones list.
        :param str frequency: (optional) The crawl schedule in the specified
               **time_zone**.
               -  `five_minutes`: Runs every five minutes.
               -  `hourly`: Runs every hour.
               -  `daily`: Runs every day between 00:00 and 06:00.
               -  `weekly`: Runs every week on Sunday between 00:00 and 06:00.
               -  `monthly`: Runs the on the first Sunday of every month between 00:00 and
               06:00.
        """
        self.enabled = enabled
        self.time_zone = time_zone
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceSchedule':
        """Initialize a SourceSchedule object from a json dictionary."""
        args = {}
        valid_keys = ['enabled', 'time_zone', 'frequency']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceSchedule: '
                + ', '.join(bad_keys))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'time_zone' in _dict:
            args['time_zone'] = _dict.get('time_zone')
        if 'frequency' in _dict:
            args['frequency'] = _dict.get('frequency')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceSchedule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'time_zone') and self.time_zone is not None:
            _dict['time_zone'] = self.time_zone
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceSchedule object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceSchedule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceSchedule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FrequencyEnum(Enum):
        """
        The crawl schedule in the specified **time_zone**.
        -  `five_minutes`: Runs every five minutes.
        -  `hourly`: Runs every hour.
        -  `daily`: Runs every day between 00:00 and 06:00.
        -  `weekly`: Runs every week on Sunday between 00:00 and 06:00.
        -  `monthly`: Runs the on the first Sunday of every month between 00:00 and 06:00.
        """
        DAILY = "daily"
        WEEKLY = "weekly"
        MONTHLY = "monthly"
        FIVE_MINUTES = "five_minutes"
        HOURLY = "hourly"


class SourceStatus():
    """
    Object containing source crawl status information.

    :attr str status: (optional) The current status of the source crawl for this
          collection. This field returns `not_configured` if the default configuration for
          this source does not have a **source** object defined.
          -  `running` indicates that a crawl to fetch more documents is in progress.
          -  `complete` indicates that the crawl has completed with no errors.
          -  `queued` indicates that the crawl has been paused by the system and will
          automatically restart when possible.
          -  `unknown` indicates that an unidentified error has occured in the service.
    :attr datetime next_crawl: (optional) Date in `RFC 3339` format indicating the
          time of the next crawl attempt.
    """

    def __init__(self,
                 *,
                 status: str = None,
                 next_crawl: datetime = None) -> None:
        """
        Initialize a SourceStatus object.

        :param str status: (optional) The current status of the source crawl for
               this collection. This field returns `not_configured` if the default
               configuration for this source does not have a **source** object defined.
               -  `running` indicates that a crawl to fetch more documents is in progress.
               -  `complete` indicates that the crawl has completed with no errors.
               -  `queued` indicates that the crawl has been paused by the system and will
               automatically restart when possible.
               -  `unknown` indicates that an unidentified error has occured in the
               service.
        :param datetime next_crawl: (optional) Date in `RFC 3339` format indicating
               the time of the next crawl attempt.
        """
        self.status = status
        self.next_crawl = next_crawl

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SourceStatus':
        """Initialize a SourceStatus object from a json dictionary."""
        args = {}
        valid_keys = ['status', 'next_crawl']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SourceStatus: '
                + ', '.join(bad_keys))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'next_crawl' in _dict:
            args['next_crawl'] = string_to_datetime(_dict.get('next_crawl'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SourceStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'next_crawl') and self.next_crawl is not None:
            _dict['next_crawl'] = datetime_to_string(self.next_crawl)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SourceStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SourceStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SourceStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        The current status of the source crawl for this collection. This field returns
        `not_configured` if the default configuration for this source does not have a
        **source** object defined.
        -  `running` indicates that a crawl to fetch more documents is in progress.
        -  `complete` indicates that the crawl has completed with no errors.
        -  `queued` indicates that the crawl has been paused by the system and will
        automatically restart when possible.
        -  `unknown` indicates that an unidentified error has occured in the service.
        """
        RUNNING = "running"
        COMPLETE = "complete"
        NOT_CONFIGURED = "not_configured"
        QUEUED = "queued"
        UNKNOWN = "unknown"


class TokenDictRule():
    """
    An object defining a single tokenizaion rule.

    :attr str text: The string to tokenize.
    :attr List[str] tokens: Array of tokens that the `text` field is split into when
          found.
    :attr List[str] readings: (optional) Array of tokens that represent the content
          of the `text` field in an alternate character set.
    :attr str part_of_speech: The part of speech that the `text` string belongs to.
          For example `noun`. Custom parts of speech can be specified.
    """

    def __init__(self,
                 text: str,
                 tokens: List[str],
                 part_of_speech: str,
                 *,
                 readings: List[str] = None) -> None:
        """
        Initialize a TokenDictRule object.

        :param str text: The string to tokenize.
        :param List[str] tokens: Array of tokens that the `text` field is split
               into when found.
        :param str part_of_speech: The part of speech that the `text` string
               belongs to. For example `noun`. Custom parts of speech can be specified.
        :param List[str] readings: (optional) Array of tokens that represent the
               content of the `text` field in an alternate character set.
        """
        self.text = text
        self.tokens = tokens
        self.readings = readings
        self.part_of_speech = part_of_speech

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TokenDictRule':
        """Initialize a TokenDictRule object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'tokens', 'readings', 'part_of_speech']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TokenDictRule: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in TokenDictRule JSON')
        if 'tokens' in _dict:
            args['tokens'] = _dict.get('tokens')
        else:
            raise ValueError(
                'Required property \'tokens\' not present in TokenDictRule JSON'
            )
        if 'readings' in _dict:
            args['readings'] = _dict.get('readings')
        if 'part_of_speech' in _dict:
            args['part_of_speech'] = _dict.get('part_of_speech')
        else:
            raise ValueError(
                'Required property \'part_of_speech\' not present in TokenDictRule JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TokenDictRule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'tokens') and self.tokens is not None:
            _dict['tokens'] = self.tokens
        if hasattr(self, 'readings') and self.readings is not None:
            _dict['readings'] = self.readings
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TokenDictRule object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TokenDictRule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TokenDictRule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TokenDictStatusResponse():
    """
    Object describing the current status of the wordlist.

    :attr str status: (optional) Current wordlist status for the specified
          collection.
    :attr str type: (optional) The type for this wordlist. Can be
          `tokenization_dictionary` or `stopwords`.
    """

    def __init__(self, *, status: str = None, type: str = None) -> None:
        """
        Initialize a TokenDictStatusResponse object.

        :param str status: (optional) Current wordlist status for the specified
               collection.
        :param str type: (optional) The type for this wordlist. Can be
               `tokenization_dictionary` or `stopwords`.
        """
        self.status = status
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TokenDictStatusResponse':
        """Initialize a TokenDictStatusResponse object from a json dictionary."""
        args = {}
        valid_keys = ['status', 'type']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TokenDictStatusResponse: '
                + ', '.join(bad_keys))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TokenDictStatusResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TokenDictStatusResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TokenDictStatusResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TokenDictStatusResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Current wordlist status for the specified collection.
        """
        ACTIVE = "active"
        PENDING = "pending"
        NOT_FOUND = "not found"


class TopHitsResults():
    """
    Top hit information for this query.

    :attr int matching_results: (optional) Number of matching results.
    :attr List[QueryResult] hits: (optional) Top results returned by the
          aggregation.
    """

    def __init__(self,
                 *,
                 matching_results: int = None,
                 hits: List['QueryResult'] = None) -> None:
        """
        Initialize a TopHitsResults object.

        :param int matching_results: (optional) Number of matching results.
        :param List[QueryResult] hits: (optional) Top results returned by the
               aggregation.
        """
        self.matching_results = matching_results
        self.hits = hits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopHitsResults':
        """Initialize a TopHitsResults object from a json dictionary."""
        args = {}
        valid_keys = ['matching_results', 'hits']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TopHitsResults: '
                + ', '.join(bad_keys))
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'hits' in _dict:
            args['hits'] = [
                QueryResult._from_dict(x) for x in (_dict.get('hits'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopHitsResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'hits') and self.hits is not None:
            _dict['hits'] = [x._to_dict() for x in self.hits]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopHitsResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TopHitsResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopHitsResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingDataSet():
    """
    Training information for a specific collection.

    :attr str environment_id: (optional) The environment id associated with this
          training data set.
    :attr str collection_id: (optional) The collection id associated with this
          training data set.
    :attr List[TrainingQuery] queries: (optional) Array of training queries.
    """

    def __init__(self,
                 *,
                 environment_id: str = None,
                 collection_id: str = None,
                 queries: List['TrainingQuery'] = None) -> None:
        """
        Initialize a TrainingDataSet object.

        :param str environment_id: (optional) The environment id associated with
               this training data set.
        :param str collection_id: (optional) The collection id associated with this
               training data set.
        :param List[TrainingQuery] queries: (optional) Array of training queries.
        """
        self.environment_id = environment_id
        self.collection_id = collection_id
        self.queries = queries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingDataSet':
        """Initialize a TrainingDataSet object from a json dictionary."""
        args = {}
        valid_keys = ['environment_id', 'collection_id', 'queries']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingDataSet: '
                + ', '.join(bad_keys))
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'queries' in _dict:
            args['queries'] = [
                TrainingQuery._from_dict(x) for x in (_dict.get('queries'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingDataSet object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'queries') and self.queries is not None:
            _dict['queries'] = [x._to_dict() for x in self.queries]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingDataSet object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingDataSet') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingDataSet') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingExample():
    """
    Training example details.

    :attr str document_id: (optional) The document ID associated with this training
          example.
    :attr str cross_reference: (optional) The cross reference associated with this
          training example.
    :attr int relevance: (optional) The relevance of the training example.
    """

    def __init__(self,
                 *,
                 document_id: str = None,
                 cross_reference: str = None,
                 relevance: int = None) -> None:
        """
        Initialize a TrainingExample object.

        :param str document_id: (optional) The document ID associated with this
               training example.
        :param str cross_reference: (optional) The cross reference associated with
               this training example.
        :param int relevance: (optional) The relevance of the training example.
        """
        self.document_id = document_id
        self.cross_reference = cross_reference
        self.relevance = relevance

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingExample':
        """Initialize a TrainingExample object from a json dictionary."""
        args = {}
        valid_keys = ['document_id', 'cross_reference', 'relevance']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingExample: '
                + ', '.join(bad_keys))
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'cross_reference' in _dict:
            args['cross_reference'] = _dict.get('cross_reference')
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingExample object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self,
                   'cross_reference') and self.cross_reference is not None:
            _dict['cross_reference'] = self.cross_reference
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingExample object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingExample') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingExample') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingExampleList():
    """
    Object containing an array of training examples.

    :attr List[TrainingExample] examples: (optional) Array of training examples.
    """

    def __init__(self, *, examples: List['TrainingExample'] = None) -> None:
        """
        Initialize a TrainingExampleList object.

        :param List[TrainingExample] examples: (optional) Array of training
               examples.
        """
        self.examples = examples

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingExampleList':
        """Initialize a TrainingExampleList object from a json dictionary."""
        args = {}
        valid_keys = ['examples']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingExampleList: '
                + ', '.join(bad_keys))
        if 'examples' in _dict:
            args['examples'] = [
                TrainingExample._from_dict(x) for x in (_dict.get('examples'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingExampleList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingExampleList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingExampleList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingExampleList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingQuery():
    """
    Training query details.

    :attr str query_id: (optional) The query ID associated with the training query.
    :attr str natural_language_query: (optional) The natural text query for the
          training query.
    :attr str filter: (optional) The filter used on the collection before the
          **natural_language_query** is applied.
    :attr List[TrainingExample] examples: (optional) Array of training examples.
    """

    def __init__(self,
                 *,
                 query_id: str = None,
                 natural_language_query: str = None,
                 filter: str = None,
                 examples: List['TrainingExample'] = None) -> None:
        """
        Initialize a TrainingQuery object.

        :param str query_id: (optional) The query ID associated with the training
               query.
        :param str natural_language_query: (optional) The natural text query for
               the training query.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        :param List[TrainingExample] examples: (optional) Array of training
               examples.
        """
        self.query_id = query_id
        self.natural_language_query = natural_language_query
        self.filter = filter
        self.examples = examples

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingQuery':
        """Initialize a TrainingQuery object from a json dictionary."""
        args = {}
        valid_keys = [
            'query_id', 'natural_language_query', 'filter', 'examples'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingQuery: '
                + ', '.join(bad_keys))
        if 'query_id' in _dict:
            args['query_id'] = _dict.get('query_id')
        if 'natural_language_query' in _dict:
            args['natural_language_query'] = _dict.get('natural_language_query')
        if 'filter' in _dict:
            args['filter'] = _dict.get('filter')
        if 'examples' in _dict:
            args['examples'] = [
                TrainingExample._from_dict(x) for x in (_dict.get('examples'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingQuery object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'query_id') and self.query_id is not None:
            _dict['query_id'] = self.query_id
        if hasattr(self, 'natural_language_query'
                  ) and self.natural_language_query is not None:
            _dict['natural_language_query'] = self.natural_language_query
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingQuery object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingQuery') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingQuery') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingStatus():
    """
    Training status details.

    :attr int total_examples: (optional) The total number of training examples
          uploaded to this collection.
    :attr bool available: (optional) When `true`, the collection has been
          successfully trained.
    :attr bool processing: (optional) When `true`, the collection is currently
          processing training.
    :attr bool minimum_queries_added: (optional) When `true`, the collection has a
          sufficent amount of queries added for training to occur.
    :attr bool minimum_examples_added: (optional) When `true`, the collection has a
          sufficent amount of examples added for training to occur.
    :attr bool sufficient_label_diversity: (optional) When `true`, the collection
          has a sufficent amount of diversity in labeled results for training to occur.
    :attr int notices: (optional) The number of notices associated with this data
          set.
    :attr datetime successfully_trained: (optional) The timestamp of when the
          collection was successfully trained.
    :attr datetime data_updated: (optional) The timestamp of when the data was
          uploaded.
    """

    def __init__(self,
                 *,
                 total_examples: int = None,
                 available: bool = None,
                 processing: bool = None,
                 minimum_queries_added: bool = None,
                 minimum_examples_added: bool = None,
                 sufficient_label_diversity: bool = None,
                 notices: int = None,
                 successfully_trained: datetime = None,
                 data_updated: datetime = None) -> None:
        """
        Initialize a TrainingStatus object.

        :param int total_examples: (optional) The total number of training examples
               uploaded to this collection.
        :param bool available: (optional) When `true`, the collection has been
               successfully trained.
        :param bool processing: (optional) When `true`, the collection is currently
               processing training.
        :param bool minimum_queries_added: (optional) When `true`, the collection
               has a sufficent amount of queries added for training to occur.
        :param bool minimum_examples_added: (optional) When `true`, the collection
               has a sufficent amount of examples added for training to occur.
        :param bool sufficient_label_diversity: (optional) When `true`, the
               collection has a sufficent amount of diversity in labeled results for
               training to occur.
        :param int notices: (optional) The number of notices associated with this
               data set.
        :param datetime successfully_trained: (optional) The timestamp of when the
               collection was successfully trained.
        :param datetime data_updated: (optional) The timestamp of when the data was
               uploaded.
        """
        self.total_examples = total_examples
        self.available = available
        self.processing = processing
        self.minimum_queries_added = minimum_queries_added
        self.minimum_examples_added = minimum_examples_added
        self.sufficient_label_diversity = sufficient_label_diversity
        self.notices = notices
        self.successfully_trained = successfully_trained
        self.data_updated = data_updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingStatus':
        """Initialize a TrainingStatus object from a json dictionary."""
        args = {}
        valid_keys = [
            'total_examples', 'available', 'processing',
            'minimum_queries_added', 'minimum_examples_added',
            'sufficient_label_diversity', 'notices', 'successfully_trained',
            'data_updated'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingStatus: '
                + ', '.join(bad_keys))
        if 'total_examples' in _dict:
            args['total_examples'] = _dict.get('total_examples')
        if 'available' in _dict:
            args['available'] = _dict.get('available')
        if 'processing' in _dict:
            args['processing'] = _dict.get('processing')
        if 'minimum_queries_added' in _dict:
            args['minimum_queries_added'] = _dict.get('minimum_queries_added')
        if 'minimum_examples_added' in _dict:
            args['minimum_examples_added'] = _dict.get('minimum_examples_added')
        if 'sufficient_label_diversity' in _dict:
            args['sufficient_label_diversity'] = _dict.get(
                'sufficient_label_diversity')
        if 'notices' in _dict:
            args['notices'] = _dict.get('notices')
        if 'successfully_trained' in _dict:
            args['successfully_trained'] = string_to_datetime(
                _dict.get('successfully_trained'))
        if 'data_updated' in _dict:
            args['data_updated'] = string_to_datetime(_dict.get('data_updated'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_examples') and self.total_examples is not None:
            _dict['total_examples'] = self.total_examples
        if hasattr(self, 'available') and self.available is not None:
            _dict['available'] = self.available
        if hasattr(self, 'processing') and self.processing is not None:
            _dict['processing'] = self.processing
        if hasattr(self, 'minimum_queries_added'
                  ) and self.minimum_queries_added is not None:
            _dict['minimum_queries_added'] = self.minimum_queries_added
        if hasattr(self, 'minimum_examples_added'
                  ) and self.minimum_examples_added is not None:
            _dict['minimum_examples_added'] = self.minimum_examples_added
        if hasattr(self, 'sufficient_label_diversity'
                  ) and self.sufficient_label_diversity is not None:
            _dict[
                'sufficient_label_diversity'] = self.sufficient_label_diversity
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = self.notices
        if hasattr(self, 'successfully_trained'
                  ) and self.successfully_trained is not None:
            _dict['successfully_trained'] = datetime_to_string(
                self.successfully_trained)
        if hasattr(self, 'data_updated') and self.data_updated is not None:
            _dict['data_updated'] = datetime_to_string(self.data_updated)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordHeadingDetection():
    """
    Object containing heading detection conversion settings for Microsoft Word documents.

    :attr List[FontSetting] fonts: (optional) Array of font matching configurations.
    :attr List[WordStyle] styles: (optional) Array of Microsoft Word styles to
          convert.
    """

    def __init__(self,
                 *,
                 fonts: List['FontSetting'] = None,
                 styles: List['WordStyle'] = None) -> None:
        """
        Initialize a WordHeadingDetection object.

        :param List[FontSetting] fonts: (optional) Array of font matching
               configurations.
        :param List[WordStyle] styles: (optional) Array of Microsoft Word styles to
               convert.
        """
        self.fonts = fonts
        self.styles = styles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WordHeadingDetection':
        """Initialize a WordHeadingDetection object from a json dictionary."""
        args = {}
        valid_keys = ['fonts', 'styles']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WordHeadingDetection: '
                + ', '.join(bad_keys))
        if 'fonts' in _dict:
            args['fonts'] = [
                FontSetting._from_dict(x) for x in (_dict.get('fonts'))
            ]
        if 'styles' in _dict:
            args['styles'] = [
                WordStyle._from_dict(x) for x in (_dict.get('styles'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordHeadingDetection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fonts') and self.fonts is not None:
            _dict['fonts'] = [x._to_dict() for x in self.fonts]
        if hasattr(self, 'styles') and self.styles is not None:
            _dict['styles'] = [x._to_dict() for x in self.styles]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WordHeadingDetection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'WordHeadingDetection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WordHeadingDetection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordSettings():
    """
    A list of Word conversion settings.

    :attr WordHeadingDetection heading: (optional) Object containing heading
          detection conversion settings for Microsoft Word documents.
    """

    def __init__(self, *, heading: 'WordHeadingDetection' = None) -> None:
        """
        Initialize a WordSettings object.

        :param WordHeadingDetection heading: (optional) Object containing heading
               detection conversion settings for Microsoft Word documents.
        """
        self.heading = heading

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WordSettings':
        """Initialize a WordSettings object from a json dictionary."""
        args = {}
        valid_keys = ['heading']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WordSettings: '
                + ', '.join(bad_keys))
        if 'heading' in _dict:
            args['heading'] = WordHeadingDetection._from_dict(
                _dict.get('heading'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'heading') and self.heading is not None:
            _dict['heading'] = self.heading._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WordSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'WordSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WordSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordStyle():
    """
    Microsoft Word styles to convert into a specified HTML head level.

    :attr int level: (optional) HTML head level that content matching this style is
          tagged with.
    :attr List[str] names: (optional) Array of word style names to convert.
    """

    def __init__(self, *, level: int = None, names: List[str] = None) -> None:
        """
        Initialize a WordStyle object.

        :param int level: (optional) HTML head level that content matching this
               style is tagged with.
        :param List[str] names: (optional) Array of word style names to convert.
        """
        self.level = level
        self.names = names

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WordStyle':
        """Initialize a WordStyle object from a json dictionary."""
        args = {}
        valid_keys = ['level', 'names']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WordStyle: '
                + ', '.join(bad_keys))
        if 'level' in _dict:
            args['level'] = _dict.get('level')
        if 'names' in _dict:
            args['names'] = _dict.get('names')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordStyle object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self, 'names') and self.names is not None:
            _dict['names'] = self.names
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WordStyle object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'WordStyle') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WordStyle') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class XPathPatterns():
    """
    Object containing an array of XPaths.

    :attr List[str] xpaths: (optional) An array to XPaths.
    """

    def __init__(self, *, xpaths: List[str] = None) -> None:
        """
        Initialize a XPathPatterns object.

        :param List[str] xpaths: (optional) An array to XPaths.
        """
        self.xpaths = xpaths

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'XPathPatterns':
        """Initialize a XPathPatterns object from a json dictionary."""
        args = {}
        valid_keys = ['xpaths']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class XPathPatterns: '
                + ', '.join(bad_keys))
        if 'xpaths' in _dict:
            args['xpaths'] = _dict.get('xpaths')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a XPathPatterns object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'xpaths') and self.xpaths is not None:
            _dict['xpaths'] = self.xpaths
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this XPathPatterns object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'XPathPatterns') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'XPathPatterns') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Calculation(QueryAggregation):
    """
    Calculation.

    :attr str field: (optional) The field where the aggregation is located in the
          document.
    :attr float value: (optional) Value of the aggregation.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None,
                 field: str = None,
                 value: float = None) -> None:
        """
        Initialize a Calculation object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        :param str field: (optional) The field where the aggregation is located in
               the document.
        :param float value: (optional) Value of the aggregation.
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations
        self.field = field
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Calculation':
        """Initialize a Calculation object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'results', 'matching_results', 'aggregations', 'field',
            'value'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Calculation: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Calculation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Calculation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Calculation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Calculation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Filter(QueryAggregation):
    """
    Filter.

    :attr str match: (optional) The match the aggregated results queried for.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None,
                 match: str = None) -> None:
        """
        Initialize a Filter object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        :param str match: (optional) The match the aggregated results queried for.
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations
        self.match = match

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Filter':
        """Initialize a Filter object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'results', 'matching_results', 'aggregations', 'match'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Filter: ' +
                ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'match' in _dict:
            args['match'] = _dict.get('match')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Filter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'match') and self.match is not None:
            _dict['match'] = self.match
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Filter object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Filter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Filter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Histogram(QueryAggregation):
    """
    Histogram.

    :attr str field: (optional) The field where the aggregation is located in the
          document.
    :attr int interval: (optional) Interval of the aggregation. (For 'histogram'
          type).
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None,
                 field: str = None,
                 interval: int = None) -> None:
        """
        Initialize a Histogram object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        :param str field: (optional) The field where the aggregation is located in
               the document.
        :param int interval: (optional) Interval of the aggregation. (For
               'histogram' type).
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations
        self.field = field
        self.interval = interval

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Histogram':
        """Initialize a Histogram object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'results', 'matching_results', 'aggregations', 'field',
            'interval'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Histogram: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Histogram object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Histogram object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Histogram') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Histogram') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Nested(QueryAggregation):
    """
    Nested.

    :attr str path: (optional) The area of the results the aggregation was
          restricted to.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None,
                 path: str = None) -> None:
        """
        Initialize a Nested object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        :param str path: (optional) The area of the results the aggregation was
               restricted to.
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations
        self.path = path

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Nested':
        """Initialize a Nested object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'results', 'matching_results', 'aggregations', 'path'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Nested: ' +
                ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Nested object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Nested object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Nested') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Nested') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Term(QueryAggregation):
    """
    Term.

    :attr str field: (optional) The field where the aggregation is located in the
          document.
    :attr int count: (optional) The number of terms identified.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None,
                 field: str = None,
                 count: int = None) -> None:
        """
        Initialize a Term object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        :param str field: (optional) The field where the aggregation is located in
               the document.
        :param int count: (optional) The number of terms identified.
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations
        self.field = field
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Term':
        """Initialize a Term object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'results', 'matching_results', 'aggregations', 'field',
            'count'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Term: ' +
                ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Term object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Term object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Term') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Term') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Timeslice(QueryAggregation):
    """
    Timeslice.

    :attr str field: (optional) The field where the aggregation is located in the
          document.
    :attr str interval: (optional) Interval of the aggregation. Valid date interval
          values are second/seconds minute/minutes, hour/hours, day/days, week/weeks,
          month/months, and year/years.
    :attr bool anomaly: (optional) Used to indicate that anomaly detection should be
          performed. Anomaly detection is used to locate unusual datapoints within a time
          series.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None,
                 field: str = None,
                 interval: str = None,
                 anomaly: bool = None) -> None:
        """
        Initialize a Timeslice object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        :param str field: (optional) The field where the aggregation is located in
               the document.
        :param str interval: (optional) Interval of the aggregation. Valid date
               interval values are second/seconds minute/minutes, hour/hours, day/days,
               week/weeks, month/months, and year/years.
        :param bool anomaly: (optional) Used to indicate that anomaly detection
               should be performed. Anomaly detection is used to locate unusual datapoints
               within a time series.
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations
        self.field = field
        self.interval = interval
        self.anomaly = anomaly

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Timeslice':
        """Initialize a Timeslice object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'results', 'matching_results', 'aggregations', 'field',
            'interval', 'anomaly'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Timeslice: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        if 'anomaly' in _dict:
            args['anomaly'] = _dict.get('anomaly')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Timeslice object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'anomaly') and self.anomaly is not None:
            _dict['anomaly'] = self.anomaly
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Timeslice object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Timeslice') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Timeslice') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopHits(QueryAggregation):
    """
    TopHits.

    :attr int size: (optional) Number of top hits returned by the aggregation.
    :attr TopHitsResults hits: (optional)
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['AggregationResult'] = None,
                 matching_results: int = None,
                 aggregations: List['QueryAggregation'] = None,
                 size: int = None,
                 hits: 'TopHitsResults' = None) -> None:
        """
        Initialize a TopHits object.

        :param str type: (optional) The type of aggregation command used. For
               example: term, filter, max, min, etc.
        :param List[AggregationResult] results: (optional) Array of aggregation
               results.
        :param int matching_results: (optional) Number of matching results.
        :param List[QueryAggregation] aggregations: (optional) Aggregations
               returned by Discovery.
        :param int size: (optional) Number of top hits returned by the aggregation.
        :param TopHitsResults hits: (optional)
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations
        self.size = size
        self.hits = hits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopHits':
        """Initialize a TopHits object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'results', 'matching_results', 'aggregations', 'size',
            'hits'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TopHits: ' +
                ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                AggregationResult._from_dict(x) for x in (_dict.get('results'))
            ]
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        if 'hits' in _dict:
            args['hits'] = TopHitsResults._from_dict(_dict.get('hits'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopHits object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'hits') and self.hits is not None:
            _dict['hits'] = self.hits._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopHits object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TopHits') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopHits') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
