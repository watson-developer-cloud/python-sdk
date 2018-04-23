# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
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
The IBM Watson Discovery Service is a cognitive search and content analytics engine that
you can add to applications to identify patterns, trends and actionable insights to drive
better decision-making. Securely unify structured and unstructured data with pre-enriched
content, and use a simplified query language to eliminate the need for manual filtering of
results.
"""

from __future__ import absolute_import

import json
from .watson_service import datetime_to_string, string_to_datetime
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class DiscoveryV1(WatsonService):
    """The Discovery V1 service."""

    default_url = 'https://gateway.watsonplatform.net/discovery/api'

    def __init__(self,
                 version,
                 url=default_url,
                 username=None,
                 password=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
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

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway.watsonplatform.net/discovery/api").
               The base url may differ between Bluemix regions.

        :param str username: The username used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of Bluemix. When running on
               Bluemix, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        :param str password: The password used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of Bluemix. When running on
               Bluemix, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        :param str iam_api_key: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.ng.bluemix.net/identity/token'.
        """

        WatsonService.__init__(
            self,
            vcap_services_name='discovery',
            url=url,
            username=username,
            password=password,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)
        self.version = version

    #########################
    # Environments
    #########################

    def create_environment(self, name, description=None, size=None, **kwargs):
        """
        Add an environment.

        Creates a new environment.  You can create only one environment per service
        instance. An attempt to create another environment results in an error.

        :param str name: Name that identifies the environment.
        :param str description: Description of the environment.
        :param int size: **Deprecated**: Size of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Environment` response.
        :rtype: dict
        """
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'name': name, 'description': description, 'size': size}
        url = '/v1/environments'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_environment(self, environment_id, **kwargs):
        """
        Delete environment.

        :param str environment_id: The ID of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DeleteEnvironmentResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_environment(self, environment_id, **kwargs):
        """
        Get environment info.

        :param str environment_id: The ID of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Environment` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_environments(self, name=None, **kwargs):
        """
        List environments.

        List existing environments for the service instance.

        :param str name: Show only the environment with the given name.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ListEnvironmentsResponse` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version, 'name': name}
        url = '/v1/environments'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_fields(self, environment_id, collection_ids, **kwargs):
        """
        List fields in specified collections.

        Gets a list of the unique fields (and their types) stored in the indexes of the
        specified collections.

        :param str environment_id: The ID of the environment.
        :param list[str] collection_ids: A comma-separated list of collection IDs to be queried against.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ListCollectionFieldsResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_ids is None:
            raise ValueError('collection_ids must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'collection_ids': self._convert_list(collection_ids)
        }
        url = '/v1/environments/{0}/fields'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_environment(self,
                           environment_id,
                           name=None,
                           description=None,
                           **kwargs):
        """
        Update an environment.

        Updates an environment. The environment's `name` and  `description` parameters can
        be changed. You must specify a `name` for the environment.

        :param str environment_id: The ID of the environment.
        :param str name: Name that identifies the environment.
        :param str description: Description of the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Environment` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'name': name, 'description': description}
        url = '/v1/environments/{0}'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Configurations
    #########################

    def create_configuration(self,
                             environment_id,
                             name,
                             description=None,
                             conversions=None,
                             enrichments=None,
                             normalizations=None,
                             **kwargs):
        """
        Add configuration.

        Creates a new configuration.  If the input configuration contains the
        `configuration_id`, `created`, or `updated` properties, then they are ignored and
        overridden by the system, and an error is not returned so that the overridden
        fields do not need to be removed when copying a configuration.  The configuration
        can contain unrecognized JSON fields. Any such fields are ignored and do not
        generate an error. This makes it easier to use newer configuration files with
        older versions of the API and the service. It also makes it possible for the
        tooling to add additional metadata and information to the configuration.

        :param str environment_id: The ID of the environment.
        :param str name: The name of the configuration.
        :param str description: The description of the configuration, if available.
        :param Conversions conversions: The document conversion settings for the configuration.
        :param list[Enrichment] enrichments: An array of document enrichment settings for the configuration.
        :param list[NormalizationOperation] normalizations: Defines operations that can be used to transform the final output JSON into a normalized form. Operations are executed in the order that they appear in the array.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Configuration` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if conversions is not None:
            conversions = self._convert_model(conversions, Conversions)
        if enrichments is not None:
            enrichments = [
                self._convert_model(x, Enrichment) for x in enrichments
            ]
        if normalizations is not None:
            normalizations = [
                self._convert_model(x, NormalizationOperation)
                for x in normalizations
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'name': name,
            'description': description,
            'conversions': conversions,
            'enrichments': enrichments,
            'normalizations': normalizations
        }
        url = '/v1/environments/{0}/configurations'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_configuration(self, environment_id, configuration_id, **kwargs):
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
        :return: A `dict` containing the `DeleteConfigurationResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if configuration_id is None:
            raise ValueError('configuration_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/configurations/{1}'.format(
            *self._encode_path_vars(environment_id, configuration_id))
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_configuration(self, environment_id, configuration_id, **kwargs):
        """
        Get configuration details.

        :param str environment_id: The ID of the environment.
        :param str configuration_id: The ID of the configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Configuration` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if configuration_id is None:
            raise ValueError('configuration_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/configurations/{1}'.format(
            *self._encode_path_vars(environment_id, configuration_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_configurations(self, environment_id, name=None, **kwargs):
        """
        List configurations.

        Lists existing configurations for the service instance.

        :param str environment_id: The ID of the environment.
        :param str name: Find configurations with the given name.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ListConfigurationsResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version, 'name': name}
        url = '/v1/environments/{0}/configurations'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_configuration(self,
                             environment_id,
                             configuration_id,
                             name,
                             description=None,
                             conversions=None,
                             enrichments=None,
                             normalizations=None,
                             **kwargs):
        """
        Update a configuration.

        Replaces an existing configuration.   * Completely replaces the original
        configuration.   * The `configuration_id`, `updated`, and `created` fields are
        accepted in the request, but they are ignored, and an error is not generated. It
        is also acceptable for users to submit an updated configuration with none of the
        three properties.   * Documents are processed with a snapshot of the configuration
        as it was at the time the document was submitted to be ingested. This means that
        already submitted documents will not see any updates made to the configuration.

        :param str environment_id: The ID of the environment.
        :param str configuration_id: The ID of the configuration.
        :param str name: The name of the configuration.
        :param str description: The description of the configuration, if available.
        :param Conversions conversions: The document conversion settings for the configuration.
        :param list[Enrichment] enrichments: An array of document enrichment settings for the configuration.
        :param list[NormalizationOperation] normalizations: Defines operations that can be used to transform the final output JSON into a normalized form. Operations are executed in the order that they appear in the array.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Configuration` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if configuration_id is None:
            raise ValueError('configuration_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if conversions is not None:
            conversions = self._convert_model(conversions, Conversions)
        if enrichments is not None:
            enrichments = [
                self._convert_model(x, Enrichment) for x in enrichments
            ]
        if normalizations is not None:
            normalizations = [
                self._convert_model(x, NormalizationOperation)
                for x in normalizations
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'name': name,
            'description': description,
            'conversions': conversions,
            'enrichments': enrichments,
            'normalizations': normalizations
        }
        url = '/v1/environments/{0}/configurations/{1}'.format(
            *self._encode_path_vars(environment_id, configuration_id))
        response = self.request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Test your configuration on a document
    #########################

    def test_configuration_in_environment(self,
                                          environment_id,
                                          configuration=None,
                                          step=None,
                                          configuration_id=None,
                                          file=None,
                                          metadata=None,
                                          file_content_type=None,
                                          filename=None,
                                          **kwargs):
        """
        Test configuration.

        Runs a sample document through the default or your configuration and returns
        diagnostic information designed to help you understand how the document was
        processed. The document is not added to the index.

        :param str environment_id: The ID of the environment.
        :param str configuration: The configuration to use to process the document. If this part is provided, then the provided configuration is used to process the document. If the `configuration_id` is also provided (both are present at the same time), then request is rejected. The maximum supported configuration size is 1 MB. Configuration parts larger than 1 MB are rejected. See the `GET /configurations/{configuration_id}` operation for an example configuration.
        :param str step: Specify to only run the input document through the given step instead of running the input document through the entire ingestion workflow. Valid values are `convert`, `enrich`, and `normalize`.
        :param str configuration_id: The ID of the configuration to use to process the document. If the `configuration` form part is also provided (both are present at the same time), then request will be rejected.
        :param file file: The content of the document to ingest. The maximum supported file size is 50 megabytes. Files larger than 50 megabytes is rejected.
        :param str metadata: If you're using the Data Crawler to upload your documents, you can test a document against the type of metadata that the Data Crawler might send. The maximum supported metadata file size is 1 MB. Metadata parts larger than 1 MB are rejected. Example:  ``` {   \"Creator\": \"Johnny Appleseed\",   \"Subject\": \"Apples\" } ```.
        :param str file_content_type: The content type of file.
        :param str filename: The filename for file.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TestDocument` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'step': step,
            'configuration_id': configuration_id
        }
        configuration_tuple = None
        if configuration:
            configuration_tuple = (None, configuration, 'text/plain')
        file_tuple = None
        if file:
            if not filename and hasattr(file, 'name'):
                filename = file.name
            if not filename:
                raise ValueError('filename must be provided')
            mime_type = file_content_type or 'application/octet-stream'
            file_tuple = (filename, file, mime_type)
        metadata_tuple = None
        if metadata:
            metadata_tuple = (None, metadata, 'text/plain')
        url = '/v1/environments/{0}/preview'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={
                'configuration': configuration_tuple,
                'file': file_tuple,
                'metadata': metadata_tuple
            },
            accept_json=True)
        return response

    #########################
    # Collections
    #########################

    def create_collection(self,
                          environment_id,
                          name,
                          description=None,
                          configuration_id=None,
                          language=None,
                          **kwargs):
        """
        Create a collection.

        :param str environment_id: The ID of the environment.
        :param str name: The name of the collection to be created.
        :param str description: A description of the collection.
        :param str configuration_id: The ID of the configuration in which the collection is to be created.
        :param str language: The language of the documents stored in the collection, in the form of an ISO 639-1 language code.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Collection` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'name': name,
            'description': description,
            'configuration_id': configuration_id,
            'language': language
        }
        url = '/v1/environments/{0}/collections'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_collection(self, environment_id, collection_id, **kwargs):
        """
        Delete a collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DeleteCollectionResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_collection(self, environment_id, collection_id, **kwargs):
        """
        Get collection details.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Collection` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_collection_fields(self, environment_id, collection_id, **kwargs):
        """
        List unique fields.

        Gets a list of the unique fields (and their types) stored in the index.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ListCollectionFieldsResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/fields'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_collections(self, environment_id, name=None, **kwargs):
        """
        List collections.

        Lists existing collections for the service instance.

        :param str environment_id: The ID of the environment.
        :param str name: Find collections with the given name.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ListCollectionsResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version, 'name': name}
        url = '/v1/environments/{0}/collections'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_collection(self,
                          environment_id,
                          collection_id,
                          name,
                          description=None,
                          configuration_id=None,
                          **kwargs):
        """
        Update a collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str name: The name of the collection.
        :param str description: A description of the collection.
        :param str configuration_id: The ID of the configuration in which the collection is to be updated.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Collection` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'name': name,
            'description': description,
            'configuration_id': configuration_id
        }
        url = '/v1/environments/{0}/collections/{1}'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Expansions
    #########################

    def create_expansions(self, environment_id, collection_id, expansions,
                          **kwargs):
        """
        Set the expansion list.

        Create or replace the Expansion list for this collection. The maximum number of
        expanded terms per collection is `500`. The current expansion list is replaced
        with the uploaded content.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param list[Expansion] expansions: An array of query expansion definitions.    Each object in the `expansions` array represents a term or set of terms that will be expanded into other terms. Each expansion object can be configured so that all terms are expanded to all other terms in the object - bi-directional, or a set list of terms can be expanded into a second list of terms - uni-directional.   To create a bi-directional expansion specify an `expanded_terms` array. When found in a query, all items in the `expanded_terms` array are then expanded to the other items in the same array.   To create a uni-directional expansion, specify both an array of `input_terms` and an array of `expanded_terms`. When items in the `input_terms` array are present in a query, they are expanded using the items listed in the `expanded_terms` array.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Expansions` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if expansions is None:
            raise ValueError('expansions must be provided')
        expansions = [self._convert_model(x, Expansion) for x in expansions]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'expansions': expansions}
        url = '/v1/environments/{0}/collections/{1}/expansions'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_expansions(self, environment_id, collection_id, **kwargs):
        """
        Delete the expansions list.

        Remove the expansion information for this collection. The expansion list must be
        deleted to disable query expansion for a collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/expansions'.format(
            *self._encode_path_vars(environment_id, collection_id))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def list_expansions(self, environment_id, collection_id, **kwargs):
        """
        List current expansions.

        Returns the current expansion list for the specified collection. If an expansion
        list is not specified, an object with empty expansion arrays is returned.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Expansions` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/expansions'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    #########################
    # Documents
    #########################

    def add_document(self,
                     environment_id,
                     collection_id,
                     file=None,
                     metadata=None,
                     file_content_type=None,
                     filename=None,
                     **kwargs):
        """
        Add a document.

        Add a document to a collection with optional metadata.    * The `version` query
        parameter is still required.    * Returns immediately after the system has
        accepted the document for processing.    * The user must provide document content,
        metadata, or both. If the request is missing both document content and metadata,
        it is rejected.    * The user can set the `Content-Type` parameter on the `file`
        part to indicate the media type of the document. If the `Content-Type` parameter
        is missing or is one of the generic media types (for example,
        `application/octet-stream`), then the service attempts to automatically detect the
        document's media type.    * The following field names are reserved and will be
        filtered out if present after normalization: `id`, `score`, `highlight`, and any
        field with the prefix of: `_`, `+`, or `-`    * Fields with empty name values
        after normalization are filtered out before indexing.    * Fields containing the
        following characters after normalization are filtered out before indexing: `#` and
        `,`.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param file file: The content of the document to ingest. The maximum supported file size is 50 megabytes. Files larger than 50 megabytes is rejected.
        :param str metadata: If you're using the Data Crawler to upload your documents, you can test a document against the type of metadata that the Data Crawler might send. The maximum supported metadata file size is 1 MB. Metadata parts larger than 1 MB are rejected. Example:  ``` {   \"Creator\": \"Johnny Appleseed\",   \"Subject\": \"Apples\" } ```.
        :param str file_content_type: The content type of file.
        :param str filename: The filename for file.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DocumentAccepted` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        file_tuple = None
        if file:
            if not filename and hasattr(file, 'name'):
                filename = file.name
            if not filename:
                raise ValueError('filename must be provided')
            mime_type = file_content_type or 'application/octet-stream'
            file_tuple = (filename, file, mime_type)
        metadata_tuple = None
        if metadata:
            metadata_tuple = (None, metadata, 'text/plain')
        url = '/v1/environments/{0}/collections/{1}/documents'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={'file': file_tuple,
                   'metadata': metadata_tuple},
            accept_json=True)
        return response

    def delete_document(self, environment_id, collection_id, document_id,
                        **kwargs):
        """
        Delete a document.

        If the given document ID is invalid, or if the document is not found, then the a
        success response is returned (HTTP status code `200`) with the status set to
        'deleted'.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DeleteDocumentResponse` response.
        :rtype: dict
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
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, document_id))
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_document_status(self, environment_id, collection_id, document_id,
                            **kwargs):
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
        :return: A `dict` containing the `DocumentStatus` response.
        :rtype: dict
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
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, document_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_document(self,
                        environment_id,
                        collection_id,
                        document_id,
                        file=None,
                        metadata=None,
                        file_content_type=None,
                        filename=None,
                        **kwargs):
        """
        Update a document.

        Replace an existing document. Starts ingesting a document with optional metadata.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param file file: The content of the document to ingest. The maximum supported file size is 50 megabytes. Files larger than 50 megabytes is rejected.
        :param str metadata: If you're using the Data Crawler to upload your documents, you can test a document against the type of metadata that the Data Crawler might send. The maximum supported metadata file size is 1 MB. Metadata parts larger than 1 MB are rejected. Example:  ``` {   \"Creator\": \"Johnny Appleseed\",   \"Subject\": \"Apples\" } ```.
        :param str file_content_type: The content type of file.
        :param str filename: The filename for file.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DocumentAccepted` response.
        :rtype: dict
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
        params = {'version': self.version}
        file_tuple = None
        if file:
            if not filename and hasattr(file, 'name'):
                filename = file.name
            if not filename:
                raise ValueError('filename must be provided')
            mime_type = file_content_type or 'application/octet-stream'
            file_tuple = (filename, file, mime_type)
        metadata_tuple = None
        if metadata:
            metadata_tuple = (None, metadata, 'text/plain')
        url = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, document_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={'file': file_tuple,
                   'metadata': metadata_tuple},
            accept_json=True)
        return response

    #########################
    # Queries
    #########################

    def federated_query(self,
                        environment_id,
                        collection_ids,
                        filter=None,
                        query=None,
                        natural_language_query=None,
                        aggregation=None,
                        count=None,
                        return_fields=None,
                        offset=None,
                        sort=None,
                        highlight=None,
                        deduplicate=None,
                        deduplicate_field=None,
                        similar=None,
                        similar_document_ids=None,
                        similar_fields=None,
                        **kwargs):
        """
        Query documents in multiple collections.

        See the [Discovery service
        documentation](https://console.bluemix.net/docs/services/discovery/using.html) for
        more details.

        :param str environment_id: The ID of the environment.
        :param list[str] collection_ids: A comma-separated list of collection IDs to be queried against.
        :param str filter: A cacheable query that limits the documents returned to exclude any documents that don't mention the query content. Filter searches are better for metadata type searches and when you are trying to get a sense of concepts in the data set.
        :param str query: A query search returns all documents in your data set with full enrichments and full text, but with the most relevant documents listed first. Use a query search when you want to find the most relevant search results. You cannot use `natural_language_query` and `query` at the same time.
        :param str natural_language_query: A natural language query that returns relevant documents by utilizing training data and natural language understanding. You cannot use `natural_language_query` and `query` at the same time.
        :param str aggregation: An aggregation search uses combinations of filters and query search to return an exact answer. Aggregations are useful for building applications, because you can use them to build lists, tables, and time series. For a full list of possible aggregrations, see the Query reference.
        :param int count: Number of documents to return.
        :param list[str] return_fields: A comma separated list of the portion of the document hierarchy to return.
        :param int offset: The number of query results to skip at the beginning. For example, if the total number of results that are returned is 10, and the offset is 8, it returns the last two results.
        :param list[str] sort: A comma separated list of fields in the document to sort on. You can optionally specify a sort direction by prefixing the field with `-` for descending or `+` for ascending. Ascending is the default sort direction if no prefix is specified.
        :param bool highlight: When true a highlight field is returned for each result which contains the fields that match the query with `<em></em>` tags around the matching query terms. Defaults to false.
        :param bool deduplicate: When `true` and used with a Watson Discovery News collection, duplicate results (based on the contents of the `title` field) are removed. Duplicate comparison is limited to the current query only, `offset` is not considered. Defaults to `false`. This parameter is currently Beta functionality.
        :param str deduplicate_field: When specified, duplicate results based on the field specified are removed from the returned results. Duplicate comparison is limited to the current query only, `offset` is not considered. This parameter is currently Beta functionality.
        :param bool similar: When `true`, results are returned based on their similarity to the document IDs specified in the `similar.document_ids` parameter. The default is `false`.
        :param list[str] similar_document_ids: A comma-separated list of document IDs that will be used to find similar documents.   **Note:** If the `natural_language_query` parameter is also specified, it will be used to expand the scope of the document similarity search to include the natural language query. Other query parameters, such as `filter` and `query` are subsequently applied and reduce the query scope.
        :param list[str] similar_fields: A comma-separated list of field names that will be used as a basis for comparison to identify similar documents. If not specified, the entire document is used for comparison.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `QueryResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_ids is None:
            raise ValueError('collection_ids must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'collection_ids': self._convert_list(collection_ids),
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'aggregation': aggregation,
            'count': count,
            'return_fields': self._convert_list(return_fields),
            'offset': offset,
            'sort': self._convert_list(sort),
            'highlight': highlight,
            'deduplicate': deduplicate,
            'deduplicate.field': deduplicate_field,
            'similar': similar,
            'similar.document_ids': self._convert_list(similar_document_ids),
            'similar.fields': self._convert_list(similar_fields)
        }
        url = '/v1/environments/{0}/query'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def federated_query_notices(self,
                                environment_id,
                                collection_ids,
                                filter=None,
                                query=None,
                                natural_language_query=None,
                                aggregation=None,
                                count=None,
                                return_fields=None,
                                offset=None,
                                sort=None,
                                highlight=None,
                                deduplicate_field=None,
                                similar=None,
                                similar_document_ids=None,
                                similar_fields=None,
                                **kwargs):
        """
        Query multiple collection system notices.

        Queries for notices (errors or warnings) that might have been generated by the
        system. Notices are generated when ingesting documents and performing relevance
        training. See the [Discovery service
        documentation](https://console.bluemix.net/docs/services/discovery/using.html) for
        more details on the query language.

        :param str environment_id: The ID of the environment.
        :param list[str] collection_ids: A comma-separated list of collection IDs to be queried against.
        :param str filter: A cacheable query that limits the documents returned to exclude any documents that don't mention the query content. Filter searches are better for metadata type searches and when you are trying to get a sense of concepts in the data set.
        :param str query: A query search returns all documents in your data set with full enrichments and full text, but with the most relevant documents listed first. Use a query search when you want to find the most relevant search results. You cannot use `natural_language_query` and `query` at the same time.
        :param str natural_language_query: A natural language query that returns relevant documents by utilizing training data and natural language understanding. You cannot use `natural_language_query` and `query` at the same time.
        :param str aggregation: An aggregation search uses combinations of filters and query search to return an exact answer. Aggregations are useful for building applications, because you can use them to build lists, tables, and time series. For a full list of possible aggregrations, see the Query reference.
        :param int count: Number of documents to return.
        :param list[str] return_fields: A comma separated list of the portion of the document hierarchy to return.
        :param int offset: The number of query results to skip at the beginning. For example, if the total number of results that are returned is 10, and the offset is 8, it returns the last two results.
        :param list[str] sort: A comma separated list of fields in the document to sort on. You can optionally specify a sort direction by prefixing the field with `-` for descending or `+` for ascending. Ascending is the default sort direction if no prefix is specified.
        :param bool highlight: When true a highlight field is returned for each result which contains the fields that match the query with `<em></em>` tags around the matching query terms. Defaults to false.
        :param str deduplicate_field: When specified, duplicate results based on the field specified are removed from the returned results. Duplicate comparison is limited to the current query only, `offset` is not considered. This parameter is currently Beta functionality.
        :param bool similar: When `true`, results are returned based on their similarity to the document IDs specified in the `similar.document_ids` parameter. The default is `false`.
        :param list[str] similar_document_ids: A comma-separated list of document IDs that will be used to find similar documents.   **Note:** If the `natural_language_query` parameter is also specified, it will be used to expand the scope of the document similarity search to include the natural language query. Other query parameters, such as `filter` and `query` are subsequently applied and reduce the query scope.
        :param list[str] similar_fields: A comma-separated list of field names that will be used as a basis for comparison to identify similar documents. If not specified, the entire document is used for comparison.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `QueryNoticesResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_ids is None:
            raise ValueError('collection_ids must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'collection_ids': self._convert_list(collection_ids),
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'aggregation': aggregation,
            'count': count,
            'return_fields': self._convert_list(return_fields),
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
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def query(self,
              environment_id,
              collection_id,
              filter=None,
              query=None,
              natural_language_query=None,
              passages=None,
              aggregation=None,
              count=None,
              return_fields=None,
              offset=None,
              sort=None,
              highlight=None,
              passages_fields=None,
              passages_count=None,
              passages_characters=None,
              deduplicate=None,
              deduplicate_field=None,
              similar=None,
              similar_document_ids=None,
              similar_fields=None,
              **kwargs):
        """
        Query documents.

        See the [Discovery service
        documentation](https://console.bluemix.net/docs/services/discovery/using.html) for
        more details.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str filter: A cacheable query that limits the documents returned to exclude any documents that don't mention the query content. Filter searches are better for metadata type searches and when you are trying to get a sense of concepts in the data set.
        :param str query: A query search returns all documents in your data set with full enrichments and full text, but with the most relevant documents listed first. Use a query search when you want to find the most relevant search results. You cannot use `natural_language_query` and `query` at the same time.
        :param str natural_language_query: A natural language query that returns relevant documents by utilizing training data and natural language understanding. You cannot use `natural_language_query` and `query` at the same time.
        :param bool passages: A passages query that returns the most relevant passages from the results.
        :param str aggregation: An aggregation search uses combinations of filters and query search to return an exact answer. Aggregations are useful for building applications, because you can use them to build lists, tables, and time series. For a full list of possible aggregrations, see the Query reference.
        :param int count: Number of documents to return.
        :param list[str] return_fields: A comma separated list of the portion of the document hierarchy to return.
        :param int offset: The number of query results to skip at the beginning. For example, if the total number of results that are returned is 10, and the offset is 8, it returns the last two results.
        :param list[str] sort: A comma separated list of fields in the document to sort on. You can optionally specify a sort direction by prefixing the field with `-` for descending or `+` for ascending. Ascending is the default sort direction if no prefix is specified.
        :param bool highlight: When true a highlight field is returned for each result which contains the fields that match the query with `<em></em>` tags around the matching query terms. Defaults to false.
        :param list[str] passages_fields: A comma-separated list of fields that passages are drawn from. If this parameter not specified, then all top-level fields are included.
        :param int passages_count: The maximum number of passages to return. The search returns fewer passages if the requested total is not found. The default is `10`. The maximum is `100`.
        :param int passages_characters: The approximate number of characters that any one passage will have. The default is `400`. The minimum is `50`. The maximum is `2000`.
        :param bool deduplicate: When `true` and used with a Watson Discovery News collection, duplicate results (based on the contents of the `title` field) are removed. Duplicate comparison is limited to the current query only, `offset` is not considered. Defaults to `false`. This parameter is currently Beta functionality.
        :param str deduplicate_field: When specified, duplicate results based on the field specified are removed from the returned results. Duplicate comparison is limited to the current query only, `offset` is not considered. This parameter is currently Beta functionality.
        :param bool similar: When `true`, results are returned based on their similarity to the document IDs specified in the `similar.document_ids` parameter. The default is `false`.
        :param list[str] similar_document_ids: A comma-separated list of document IDs that will be used to find similar documents.   **Note:** If the `natural_language_query` parameter is also specified, it will be used to expand the scope of the document similarity search to include the natural language query. Other query parameters, such as `filter` and `query` are subsequently applied and reduce the query scope.
        :param list[str] similar_fields: A comma-separated list of field names that will be used as a basis for comparison to identify similar documents. If not specified, the entire document is used for comparison.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `QueryResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'passages': passages,
            'aggregation': aggregation,
            'count': count,
            'return': self._convert_list(return_fields),
            'offset': offset,
            'sort': self._convert_list(sort),
            'highlight': highlight,
            'passages.fields': self._convert_list(passages_fields),
            'passages.count': passages_count,
            'passages.characters': passages_characters,
            'deduplicate': deduplicate,
            'deduplicate.field': deduplicate_field,
            'similar': similar,
            'similar.document_ids': self._convert_list(similar_document_ids),
            'similar.fields': self._convert_list(similar_fields)
        }
        url = '/v1/environments/{0}/collections/{1}/query'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def query_entities(self,
                       environment_id,
                       collection_id,
                       feature=None,
                       entity=None,
                       context=None,
                       count=None,
                       evidence_count=None,
                       **kwargs):
        """
        Knowledge Graph entity query.

        See the [Knowledge Graph
        documentation](https://console.bluemix.net/docs/services/discovery/building-kg.html)
        for more details.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str feature: The entity query feature to perform. Supported features are `disambiguate` and `similar_entities`.
        :param QueryEntitiesEntity entity: A text string that appears within the entity text field.
        :param QueryEntitiesContext context: Entity text to provide context for the queried entity and rank based on that association. For example, if you wanted to query the city of London in England your query would look for `London` with the context of `England`.
        :param int count: The number of results to return. The default is `10`. The maximum is `1000`.
        :param int evidence_count: The number of evidence items to return for each result. The default is `0`. The maximum number of evidence items per query is 10,000.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `QueryEntitiesResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if entity is not None:
            entity = self._convert_model(entity, QueryEntitiesEntity)
        if context is not None:
            context = self._convert_model(context, QueryEntitiesContext)
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'feature': feature,
            'entity': entity,
            'context': context,
            'count': count,
            'evidence_count': evidence_count
        }
        url = '/v1/environments/{0}/collections/{1}/query_entities'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def query_notices(self,
                      environment_id,
                      collection_id,
                      filter=None,
                      query=None,
                      natural_language_query=None,
                      passages=None,
                      aggregation=None,
                      count=None,
                      return_fields=None,
                      offset=None,
                      sort=None,
                      highlight=None,
                      passages_fields=None,
                      passages_count=None,
                      passages_characters=None,
                      deduplicate_field=None,
                      similar=None,
                      similar_document_ids=None,
                      similar_fields=None,
                      **kwargs):
        """
        Query system notices.

        Queries for notices (errors or warnings) that might have been generated by the
        system. Notices are generated when ingesting documents and performing relevance
        training. See the [Discovery service
        documentation](https://console.bluemix.net/docs/services/discovery/using.html) for
        more details on the query language.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str filter: A cacheable query that limits the documents returned to exclude any documents that don't mention the query content. Filter searches are better for metadata type searches and when you are trying to get a sense of concepts in the data set.
        :param str query: A query search returns all documents in your data set with full enrichments and full text, but with the most relevant documents listed first. Use a query search when you want to find the most relevant search results. You cannot use `natural_language_query` and `query` at the same time.
        :param str natural_language_query: A natural language query that returns relevant documents by utilizing training data and natural language understanding. You cannot use `natural_language_query` and `query` at the same time.
        :param bool passages: A passages query that returns the most relevant passages from the results.
        :param str aggregation: An aggregation search uses combinations of filters and query search to return an exact answer. Aggregations are useful for building applications, because you can use them to build lists, tables, and time series. For a full list of possible aggregrations, see the Query reference.
        :param int count: Number of documents to return.
        :param list[str] return_fields: A comma separated list of the portion of the document hierarchy to return.
        :param int offset: The number of query results to skip at the beginning. For example, if the total number of results that are returned is 10, and the offset is 8, it returns the last two results.
        :param list[str] sort: A comma separated list of fields in the document to sort on. You can optionally specify a sort direction by prefixing the field with `-` for descending or `+` for ascending. Ascending is the default sort direction if no prefix is specified.
        :param bool highlight: When true a highlight field is returned for each result which contains the fields that match the query with `<em></em>` tags around the matching query terms. Defaults to false.
        :param list[str] passages_fields: A comma-separated list of fields that passages are drawn from. If this parameter not specified, then all top-level fields are included.
        :param int passages_count: The maximum number of passages to return. The search returns fewer passages if the requested total is not found. The default is `10`. The maximum is `100`.
        :param int passages_characters: The approximate number of characters that any one passage will have. The default is `400`. The minimum is `50`. The maximum is `2000`.
        :param str deduplicate_field: When specified, duplicate results based on the field specified are removed from the returned results. Duplicate comparison is limited to the current query only, `offset` is not considered. This parameter is currently Beta functionality.
        :param bool similar: When `true`, results are returned based on their similarity to the document IDs specified in the `similar.document_ids` parameter. The default is `false`.
        :param list[str] similar_document_ids: A comma-separated list of document IDs that will be used to find similar documents.   **Note:** If the `natural_language_query` parameter is also specified, it will be used to expand the scope of the document similarity search to include the natural language query. Other query parameters, such as `filter` and `query` are subsequently applied and reduce the query scope.
        :param list[str] similar_fields: A comma-separated list of field names that will be used as a basis for comparison to identify similar documents. If not specified, the entire document is used for comparison.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `QueryNoticesResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'passages': passages,
            'aggregation': aggregation,
            'count': count,
            'return_fields': self._convert_list(return_fields),
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
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def query_relations(self,
                        environment_id,
                        collection_id,
                        entities=None,
                        context=None,
                        sort=None,
                        filter=None,
                        count=None,
                        evidence_count=None,
                        **kwargs):
        """
        Knowledge Graph relationship query.

        See the [Knowledge Graph
        documentation](https://console.bluemix.net/docs/services/discovery/building-kg.html)
        for more details.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param list[QueryRelationsEntity] entities: An array of entities to find relationships for.
        :param QueryEntitiesContext context: Entity text to provide context for the queried entity and rank based on that association. For example, if you wanted to query the city of London in England your query would look for `London` with the context of `England`.
        :param str sort: The sorting method for the relationships, can be `score` or `frequency`. `frequency` is the number of unique times each entity is identified. The default is `score`.
        :param QueryRelationsFilter filter: Filters to apply to the relationship query.
        :param int count: The number of results to return. The default is `10`. The maximum is `1000`.
        :param int evidence_count: The number of evidence items to return for each result. The default is `0`. The maximum number of evidence items per query is 10,000.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `QueryRelationsResponse` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if entities is not None:
            entities = [
                self._convert_model(x, QueryRelationsEntity) for x in entities
            ]
        if context is not None:
            context = self._convert_model(context, QueryEntitiesContext)
        if filter is not None:
            filter = self._convert_model(filter, QueryRelationsFilter)
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'entities': entities,
            'context': context,
            'sort': sort,
            'filter': filter,
            'count': count,
            'evidence_count': evidence_count
        }
        url = '/v1/environments/{0}/collections/{1}/query_relations'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Training Data
    #########################

    def add_training_data(self,
                          environment_id,
                          collection_id,
                          natural_language_query=None,
                          filter=None,
                          examples=None,
                          **kwargs):
        """
        Adds a query to the training data for this collection. The query can contain a
        filter and natural language query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str natural_language_query:
        :param str filter:
        :param list[TrainingExample] examples:
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TrainingQuery` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if examples is not None:
            examples = [
                self._convert_model(x, TrainingExample) for x in examples
            ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'natural_language_query': natural_language_query,
            'filter': filter,
            'examples': examples
        }
        url = '/v1/environments/{0}/collections/{1}/training_data'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def create_training_example(self,
                                environment_id,
                                collection_id,
                                query_id,
                                document_id=None,
                                cross_reference=None,
                                relevance=None,
                                **kwargs):
        """
        Adds a new example to this training data query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str document_id:
        :param str cross_reference:
        :param int relevance:
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TrainingExample` response.
        :rtype: dict
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
        params = {'version': self.version}
        data = {
            'document_id': document_id,
            'cross_reference': cross_reference,
            'relevance': relevance
        }
        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def delete_all_training_data(self, environment_id, collection_id, **kwargs):
        """
        Clears all training data for this collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/training_data'.format(
            *self._encode_path_vars(environment_id, collection_id))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def delete_training_data(self, environment_id, collection_id, query_id,
                             **kwargs):
        """
        Removes the training data and all associated examples from the training data set.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/training_data/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def delete_training_example(self, environment_id, collection_id, query_id,
                                example_id, **kwargs):
        """
        Removes the example with the given ID for the training data query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str example_id: The ID of the document as it is indexed.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id,
                                    example_id))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_training_data(self, environment_id, collection_id, query_id,
                          **kwargs):
        """
        Shows details for a specific training data query, including the query string and
        all examples.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TrainingQuery` response.
        :rtype: dict
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
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/training_data/{2}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_training_example(self, environment_id, collection_id, query_id,
                             example_id, **kwargs):
        """
        Gets the details for this training example.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str example_id: The ID of the document as it is indexed.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TrainingExample` response.
        :rtype: dict
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
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id,
                                    example_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_training_data(self, environment_id, collection_id, **kwargs):
        """
        Lists the training data for this collection.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TrainingDataSet` response.
        :rtype: dict
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/training_data'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_training_examples(self, environment_id, collection_id, query_id,
                               **kwargs):
        """
        List all examples for this training data query.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TrainingExampleList` response.
        :rtype: dict
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
        params = {'version': self.version}
        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_training_example(self,
                                environment_id,
                                collection_id,
                                query_id,
                                example_id,
                                cross_reference=None,
                                relevance=None,
                                **kwargs):
        """
        Changes the label or cross reference query for this training example.

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str query_id: The ID of the query used for training.
        :param str example_id: The ID of the document as it is indexed.
        :param str cross_reference:
        :param int relevance:
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `TrainingExample` response.
        :rtype: dict
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
        params = {'version': self.version}
        data = {'cross_reference': cross_reference, 'relevance': relevance}
        url = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(
            *self._encode_path_vars(environment_id, collection_id, query_id,
                                    example_id))
        response = self.request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class AggregationResult(object):
    """
    AggregationResult.

    :attr str key: (optional) Key that matched the aggregation type.
    :attr int matching_results: (optional) Number of matching results.
    :attr list[QueryAggregation] aggregations: (optional) Aggregations returned in the case of chained aggregations.
    """

    def __init__(self, key=None, matching_results=None, aggregations=None):
        """
        Initialize a AggregationResult object.

        :param str key: (optional) Key that matched the aggregation type.
        :param int matching_results: (optional) Number of matching results.
        :param list[QueryAggregation] aggregations: (optional) Aggregations returned in the case of chained aggregations.
        """
        self.key = key
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AggregationResult object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this AggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Collection(object):
    """
    A collection for storing documents.

    :attr str collection_id: (optional) The unique identifier of the collection.
    :attr str name: (optional) The name of the collection.
    :attr str description: (optional) The description of the collection.
    :attr datetime created: (optional) The creation date of the collection in the format yyyy-MM-dd'T'HH:mmcon:ss.SSS'Z'.
    :attr datetime updated: (optional) The timestamp of when the collection was last updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str status: (optional) The status of the collection.
    :attr str configuration_id: (optional) The unique identifier of the collection's configuration.
    :attr str language: (optional) The language of the documents stored in the collection. Permitted values include `en` (English), `de` (German), and `es` (Spanish).
    :attr DocumentCounts document_counts: (optional) The object providing information about the documents in the collection. Present only when retrieving details of a collection.
    :attr CollectionDiskUsage disk_usage: (optional) The object providing information about the disk usage of the collection. Present only when retrieving details of a collection.
    :attr TrainingStatus training_status: (optional) Provides information about the status of relevance training for collection.
    """

    def __init__(self,
                 collection_id=None,
                 name=None,
                 description=None,
                 created=None,
                 updated=None,
                 status=None,
                 configuration_id=None,
                 language=None,
                 document_counts=None,
                 disk_usage=None,
                 training_status=None):
        """
        Initialize a Collection object.

        :param str collection_id: (optional) The unique identifier of the collection.
        :param str name: (optional) The name of the collection.
        :param str description: (optional) The description of the collection.
        :param datetime created: (optional) The creation date of the collection in the format yyyy-MM-dd'T'HH:mmcon:ss.SSS'Z'.
        :param datetime updated: (optional) The timestamp of when the collection was last updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str status: (optional) The status of the collection.
        :param str configuration_id: (optional) The unique identifier of the collection's configuration.
        :param str language: (optional) The language of the documents stored in the collection. Permitted values include `en` (English), `de` (German), and `es` (Spanish).
        :param DocumentCounts document_counts: (optional) The object providing information about the documents in the collection. Present only when retrieving details of a collection.
        :param CollectionDiskUsage disk_usage: (optional) The object providing information about the disk usage of the collection. Present only when retrieving details of a collection.
        :param TrainingStatus training_status: (optional) Provides information about the status of relevance training for collection.
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Collection object from a json dictionary."""
        args = {}
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
        return cls(**args)

    def _to_dict(self):
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
        return _dict

    def __str__(self):
        """Return a `str` version of this Collection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionDiskUsage(object):
    """
    Summary of the disk usage statistics for this collection.

    :attr int used_bytes: (optional) Number of bytes used by the collection.
    """

    def __init__(self, used_bytes=None):
        """
        Initialize a CollectionDiskUsage object.

        :param int used_bytes: (optional) Number of bytes used by the collection.
        """
        self.used_bytes = used_bytes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionDiskUsage object from a json dictionary."""
        args = {}
        if 'used_bytes' in _dict:
            args['used_bytes'] = _dict.get('used_bytes')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'used_bytes') and self.used_bytes is not None:
            _dict['used_bytes'] = self.used_bytes
        return _dict

    def __str__(self):
        """Return a `str` version of this CollectionDiskUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionUsage(object):
    """
    Summary of the collection usage in the environment.

    :attr int available: (optional) Number of active collections in the environment.
    :attr int maximum_allowed: (optional) Total number of collections allowed in the environment.
    """

    def __init__(self, available=None, maximum_allowed=None):
        """
        Initialize a CollectionUsage object.

        :param int available: (optional) Number of active collections in the environment.
        :param int maximum_allowed: (optional) Total number of collections allowed in the environment.
        """
        self.available = available
        self.maximum_allowed = maximum_allowed

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionUsage object from a json dictionary."""
        args = {}
        if 'available' in _dict:
            args['available'] = _dict.get('available')
        if 'maximum_allowed' in _dict:
            args['maximum_allowed'] = _dict.get('maximum_allowed')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'available') and self.available is not None:
            _dict['available'] = self.available
        if hasattr(self,
                   'maximum_allowed') and self.maximum_allowed is not None:
            _dict['maximum_allowed'] = self.maximum_allowed
        return _dict

    def __str__(self):
        """Return a `str` version of this CollectionUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Configuration(object):
    """
    A custom configuration for the environment.

    :attr str configuration_id: (optional) The unique identifier of the configuration.
    :attr str name: The name of the configuration.
    :attr datetime created: (optional) The creation date of the configuration in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr datetime updated: (optional) The timestamp of when the configuration was last updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str description: (optional) The description of the configuration, if available.
    :attr Conversions conversions: (optional) The document conversion settings for the configuration.
    :attr list[Enrichment] enrichments: (optional) An array of document enrichment settings for the configuration.
    :attr list[NormalizationOperation] normalizations: (optional) Defines operations that can be used to transform the final output JSON into a normalized form. Operations are executed in the order that they appear in the array.
    """

    def __init__(self,
                 name,
                 configuration_id=None,
                 created=None,
                 updated=None,
                 description=None,
                 conversions=None,
                 enrichments=None,
                 normalizations=None):
        """
        Initialize a Configuration object.

        :param str name: The name of the configuration.
        :param str configuration_id: (optional) The unique identifier of the configuration.
        :param datetime created: (optional) The creation date of the configuration in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param datetime updated: (optional) The timestamp of when the configuration was last updated in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str description: (optional) The description of the configuration, if available.
        :param Conversions conversions: (optional) The document conversion settings for the configuration.
        :param list[Enrichment] enrichments: (optional) An array of document enrichment settings for the configuration.
        :param list[NormalizationOperation] normalizations: (optional) Defines operations that can be used to transform the final output JSON into a normalized form. Operations are executed in the order that they appear in the array.
        """
        self.configuration_id = configuration_id
        self.name = name
        self.created = created
        self.updated = updated
        self.description = description
        self.conversions = conversions
        self.enrichments = enrichments
        self.normalizations = normalizations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Configuration object from a json dictionary."""
        args = {}
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
        return cls(**args)

    def _to_dict(self):
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
        return _dict

    def __str__(self):
        """Return a `str` version of this Configuration object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Conversions(object):
    """
    Document conversion settings.

    :attr PdfSettings pdf: (optional) A list of PDF conversion settings.
    :attr WordSettings word: (optional) A list of Word conversion settings.
    :attr HtmlSettings html: (optional) A list of HTML conversion settings.
    :attr SegmentSettings segment: (optional) A list of Document Segmentation settings.
    :attr list[NormalizationOperation] json_normalizations: (optional) Defines operations that can be used to transform the final output JSON into a normalized form. Operations are executed in the order that they appear in the array.
    """

    def __init__(self,
                 pdf=None,
                 word=None,
                 html=None,
                 segment=None,
                 json_normalizations=None):
        """
        Initialize a Conversions object.

        :param PdfSettings pdf: (optional) A list of PDF conversion settings.
        :param WordSettings word: (optional) A list of Word conversion settings.
        :param HtmlSettings html: (optional) A list of HTML conversion settings.
        :param SegmentSettings segment: (optional) A list of Document Segmentation settings.
        :param list[NormalizationOperation] json_normalizations: (optional) Defines operations that can be used to transform the final output JSON into a normalized form. Operations are executed in the order that they appear in the array.
        """
        self.pdf = pdf
        self.word = word
        self.html = html
        self.segment = segment
        self.json_normalizations = json_normalizations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Conversions object from a json dictionary."""
        args = {}
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
        return cls(**args)

    def _to_dict(self):
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
        return _dict

    def __str__(self):
        """Return a `str` version of this Conversions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteCollectionResponse(object):
    """
    DeleteCollectionResponse.

    :attr str collection_id: The unique identifier of the collection that is being deleted.
    :attr str status: The status of the collection. The status of a successful deletion operation is `deleted`.
    """

    def __init__(self, collection_id, status):
        """
        Initialize a DeleteCollectionResponse object.

        :param str collection_id: The unique identifier of the collection that is being deleted.
        :param str status: The status of the collection. The status of a successful deletion operation is `deleted`.
        """
        self.collection_id = collection_id
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteCollectionResponse object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def __str__(self):
        """Return a `str` version of this DeleteCollectionResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteConfigurationResponse(object):
    """
    DeleteConfigurationResponse.

    :attr str configuration_id: The unique identifier for the configuration.
    :attr str status: Status of the configuration. A deleted configuration has the status deleted.
    :attr list[Notice] notices: (optional) An array of notice messages, if any.
    """

    def __init__(self, configuration_id, status, notices=None):
        """
        Initialize a DeleteConfigurationResponse object.

        :param str configuration_id: The unique identifier for the configuration.
        :param str status: Status of the configuration. A deleted configuration has the status deleted.
        :param list[Notice] notices: (optional) An array of notice messages, if any.
        """
        self.configuration_id = configuration_id
        self.status = status
        self.notices = notices

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteConfigurationResponse object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this DeleteConfigurationResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteDocumentResponse(object):
    """
    DeleteDocumentResponse.

    :attr str document_id: (optional) The unique identifier of the document.
    :attr str status: (optional) Status of the document. A deleted document has the status deleted.
    """

    def __init__(self, document_id=None, status=None):
        """
        Initialize a DeleteDocumentResponse object.

        :param str document_id: (optional) The unique identifier of the document.
        :param str status: (optional) Status of the document. A deleted document has the status deleted.
        """
        self.document_id = document_id
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteDocumentResponse object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def __str__(self):
        """Return a `str` version of this DeleteDocumentResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteEnvironmentResponse(object):
    """
    DeleteEnvironmentResponse.

    :attr str environment_id: The unique identifier for the environment.
    :attr str status: Status of the environment.
    """

    def __init__(self, environment_id, status):
        """
        Initialize a DeleteEnvironmentResponse object.

        :param str environment_id: The unique identifier for the environment.
        :param str status: Status of the environment.
        """
        self.environment_id = environment_id
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteEnvironmentResponse object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def __str__(self):
        """Return a `str` version of this DeleteEnvironmentResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DiskUsage(object):
    """
    Summary of the disk usage statistics for the environment.

    :attr int used_bytes: (optional) Number of bytes used on the environment's disk capacity.
    :attr int maximum_allowed_bytes: (optional) Total number of bytes available in the environment's disk capacity.
    :attr int total_bytes: (optional) **Deprecated**: Total number of bytes available in the environment's disk capacity.
    :attr str used: (optional) **Deprecated**: Amount of disk capacity used, in KB or GB format.
    :attr str total: (optional) **Deprecated**: Total amount of the environment's disk capacity, in KB or GB format.
    :attr float percent_used: (optional) **Deprecated**: Percentage of the environment's disk capacity that is being used.
    """

    def __init__(self,
                 used_bytes=None,
                 maximum_allowed_bytes=None,
                 total_bytes=None,
                 used=None,
                 total=None,
                 percent_used=None):
        """
        Initialize a DiskUsage object.

        :param int used_bytes: (optional) Number of bytes used on the environment's disk capacity.
        :param int maximum_allowed_bytes: (optional) Total number of bytes available in the environment's disk capacity.
        :param int total_bytes: (optional) **Deprecated**: Total number of bytes available in the environment's disk capacity.
        :param str used: (optional) **Deprecated**: Amount of disk capacity used, in KB or GB format.
        :param str total: (optional) **Deprecated**: Total amount of the environment's disk capacity, in KB or GB format.
        :param float percent_used: (optional) **Deprecated**: Percentage of the environment's disk capacity that is being used.
        """
        self.used_bytes = used_bytes
        self.maximum_allowed_bytes = maximum_allowed_bytes
        self.total_bytes = total_bytes
        self.used = used
        self.total = total
        self.percent_used = percent_used

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DiskUsage object from a json dictionary."""
        args = {}
        if 'used_bytes' in _dict:
            args['used_bytes'] = _dict.get('used_bytes')
        if 'maximum_allowed_bytes' in _dict:
            args['maximum_allowed_bytes'] = _dict.get('maximum_allowed_bytes')
        if 'total_bytes' in _dict:
            args['total_bytes'] = _dict.get('total_bytes')
        if 'used' in _dict:
            args['used'] = _dict.get('used')
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        if 'percent_used' in _dict:
            args['percent_used'] = _dict.get('percent_used')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'used_bytes') and self.used_bytes is not None:
            _dict['used_bytes'] = self.used_bytes
        if hasattr(self, 'maximum_allowed_bytes'
                  ) and self.maximum_allowed_bytes is not None:
            _dict['maximum_allowed_bytes'] = self.maximum_allowed_bytes
        if hasattr(self, 'total_bytes') and self.total_bytes is not None:
            _dict['total_bytes'] = self.total_bytes
        if hasattr(self, 'used') and self.used is not None:
            _dict['used'] = self.used
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        if hasattr(self, 'percent_used') and self.percent_used is not None:
            _dict['percent_used'] = self.percent_used
        return _dict

    def __str__(self):
        """Return a `str` version of this DiskUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentAccepted(object):
    """
    DocumentAccepted.

    :attr str document_id: (optional) The unique identifier of the ingested document.
    :attr str status: (optional) Status of the document in the ingestion process.
    :attr list[Notice] notices: (optional) Array of notices produced by the document-ingestion process.
    """

    def __init__(self, document_id=None, status=None, notices=None):
        """
        Initialize a DocumentAccepted object.

        :param str document_id: (optional) The unique identifier of the ingested document.
        :param str status: (optional) Status of the document in the ingestion process.
        :param list[Notice] notices: (optional) Array of notices produced by the document-ingestion process.
        """
        self.document_id = document_id
        self.status = status
        self.notices = notices

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentAccepted object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'notices' in _dict:
            args['notices'] = [
                Notice._from_dict(x) for x in (_dict.get('notices'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = [x._to_dict() for x in self.notices]
        return _dict

    def __str__(self):
        """Return a `str` version of this DocumentAccepted object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentCounts(object):
    """
    DocumentCounts.

    :attr int available: (optional) The total number of available documents in the collection.
    :attr int processing: (optional) The number of documents in the collection that are currently being processed.
    :attr int failed: (optional) The number of documents in the collection that failed to be ingested.
    """

    def __init__(self, available=None, processing=None, failed=None):
        """
        Initialize a DocumentCounts object.

        :param int available: (optional) The total number of available documents in the collection.
        :param int processing: (optional) The number of documents in the collection that are currently being processed.
        :param int failed: (optional) The number of documents in the collection that failed to be ingested.
        """
        self.available = available
        self.processing = processing
        self.failed = failed

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentCounts object from a json dictionary."""
        args = {}
        if 'available' in _dict:
            args['available'] = _dict.get('available')
        if 'processing' in _dict:
            args['processing'] = _dict.get('processing')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'available') and self.available is not None:
            _dict['available'] = self.available
        if hasattr(self, 'processing') and self.processing is not None:
            _dict['processing'] = self.processing
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        return _dict

    def __str__(self):
        """Return a `str` version of this DocumentCounts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentSnapshot(object):
    """
    DocumentSnapshot.

    :attr str step: (optional)
    :attr object snapshot: (optional)
    """

    def __init__(self, step=None, snapshot=None):
        """
        Initialize a DocumentSnapshot object.

        :param str step: (optional)
        :param object snapshot: (optional)
        """
        self.step = step
        self.snapshot = snapshot

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentSnapshot object from a json dictionary."""
        args = {}
        if 'step' in _dict:
            args['step'] = _dict.get('step')
        if 'snapshot' in _dict:
            args['snapshot'] = _dict.get('snapshot')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'step') and self.step is not None:
            _dict['step'] = self.step
        if hasattr(self, 'snapshot') and self.snapshot is not None:
            _dict['snapshot'] = self.snapshot
        return _dict

    def __str__(self):
        """Return a `str` version of this DocumentSnapshot object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentStatus(object):
    """
    Status information about a submitted document.

    :attr str document_id: The unique identifier of the document.
    :attr str configuration_id: (optional) The unique identifier for the configuration.
    :attr datetime created: (optional) The creation date of the document in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr datetime updated: (optional) Date of the most recent document update, in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str status: Status of the document in the ingestion process.
    :attr str status_description: Description of the document status.
    :attr str filename: (optional) Name of the original source file (if available).
    :attr str file_type: (optional) The type of the original source file.
    :attr str sha1: (optional) The SHA-1 hash of the original source file (formatted as a hexadecimal string).
    :attr list[Notice] notices: Array of notices produced by the document-ingestion process.
    """

    def __init__(self,
                 document_id,
                 status,
                 status_description,
                 notices,
                 configuration_id=None,
                 created=None,
                 updated=None,
                 filename=None,
                 file_type=None,
                 sha1=None):
        """
        Initialize a DocumentStatus object.

        :param str document_id: The unique identifier of the document.
        :param str status: Status of the document in the ingestion process.
        :param str status_description: Description of the document status.
        :param list[Notice] notices: Array of notices produced by the document-ingestion process.
        :param str configuration_id: (optional) The unique identifier for the configuration.
        :param datetime created: (optional) The creation date of the document in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param datetime updated: (optional) Date of the most recent document update, in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str filename: (optional) Name of the original source file (if available).
        :param str file_type: (optional) The type of the original source file.
        :param str sha1: (optional) The SHA-1 hash of the original source file (formatted as a hexadecimal string).
        """
        self.document_id = document_id
        self.configuration_id = configuration_id
        self.created = created
        self.updated = updated
        self.status = status
        self.status_description = status_description
        self.filename = filename
        self.file_type = file_type
        self.sha1 = sha1
        self.notices = notices

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentStatus object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        else:
            raise ValueError(
                'Required property \'document_id\' not present in DocumentStatus JSON'
            )
        if 'configuration_id' in _dict:
            args['configuration_id'] = _dict.get('configuration_id')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self,
                   'configuration_id') and self.configuration_id is not None:
            _dict['configuration_id'] = self.configuration_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
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

    def __str__(self):
        """Return a `str` version of this DocumentStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Enrichment(object):
    """
    Enrichment.

    :attr str description: (optional) Describes what the enrichment step does.
    :attr str destination_field: Field where enrichments will be stored. This field must already exist or be at most 1 level deeper than an existing field. For example, if `text` is a top-level field with no sub-fields, `text.foo` is a valid destination but `text.foo.bar` is not.
    :attr str source_field: Field to be enriched.
    :attr bool overwrite: (optional) Indicates that the enrichments will overwrite the destination_field field if it already exists.
    :attr str enrichment_name: Name of the enrichment service to call. Current options are `natural_language_understanding` and `elements`.   When using `natual_language_understanding`, the `options` object must contain Natural Language Understanding Options.   When using `elements` the `options` object must contain Element Classification options. Additionally, when using the `elements` enrichment the configuration specified and files ingested must meet all the criteria specified in [the documentation](https://console.bluemix.net/docs/services/discovery/element-classification.html)     Previous API versions also supported `alchemy_language`.
    :attr bool ignore_downstream_errors: (optional) If true, then most errors generated during the enrichment process will be treated as warnings and will not cause the document to fail processing.
    :attr EnrichmentOptions options: (optional) A list of options specific to the enrichment.
    """

    def __init__(self,
                 destination_field,
                 source_field,
                 enrichment_name,
                 description=None,
                 overwrite=None,
                 ignore_downstream_errors=None,
                 options=None):
        """
        Initialize a Enrichment object.

        :param str destination_field: Field where enrichments will be stored. This field must already exist or be at most 1 level deeper than an existing field. For example, if `text` is a top-level field with no sub-fields, `text.foo` is a valid destination but `text.foo.bar` is not.
        :param str source_field: Field to be enriched.
        :param str enrichment_name: Name of the enrichment service to call. Current options are `natural_language_understanding` and `elements`.   When using `natual_language_understanding`, the `options` object must contain Natural Language Understanding Options.   When using `elements` the `options` object must contain Element Classification options. Additionally, when using the `elements` enrichment the configuration specified and files ingested must meet all the criteria specified in [the documentation](https://console.bluemix.net/docs/services/discovery/element-classification.html)     Previous API versions also supported `alchemy_language`.
        :param str description: (optional) Describes what the enrichment step does.
        :param bool overwrite: (optional) Indicates that the enrichments will overwrite the destination_field field if it already exists.
        :param bool ignore_downstream_errors: (optional) If true, then most errors generated during the enrichment process will be treated as warnings and will not cause the document to fail processing.
        :param EnrichmentOptions options: (optional) A list of options specific to the enrichment.
        """
        self.description = description
        self.destination_field = destination_field
        self.source_field = source_field
        self.overwrite = overwrite
        self.enrichment_name = enrichment_name
        self.ignore_downstream_errors = ignore_downstream_errors
        self.options = options

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Enrichment object from a json dictionary."""
        args = {}
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
        if 'enrichment' in _dict or 'enrichment_name' in _dict:
            args['enrichment_name'] = _dict.get('enrichment') or _dict.get(
                'enrichment_name')
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

    def _to_dict(self):
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
        if hasattr(self,
                   'enrichment_name') and self.enrichment_name is not None:
            _dict['enrichment'] = self.enrichment_name
        if hasattr(self, 'ignore_downstream_errors'
                  ) and self.ignore_downstream_errors is not None:
            _dict['ignore_downstream_errors'] = self.ignore_downstream_errors
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = self.options._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this Enrichment object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnrichmentOptions(object):
    """
    Options which are specific to a particular enrichment.

    :attr NluEnrichmentFeatures features: (optional) An object representing the enrichment features that will be applied to the specified field.
    :attr str model: (optional) *For use with `elements` enrichments only.* The element extraction model to use. Models available are: `contract`.
    """

    def __init__(self, features=None, model=None):
        """
        Initialize a EnrichmentOptions object.

        :param NluEnrichmentFeatures features: (optional) An object representing the enrichment features that will be applied to the specified field.
        :param str model: (optional) *For use with `elements` enrichments only.* The element extraction model to use. Models available are: `contract`.
        """
        self.features = features
        self.model = model

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnrichmentOptions object from a json dictionary."""
        args = {}
        if 'features' in _dict:
            args['features'] = NluEnrichmentFeatures._from_dict(
                _dict.get('features'))
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = self.features._to_dict()
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def __str__(self):
        """Return a `str` version of this EnrichmentOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Environment(object):
    """
    Details about an environment.

    :attr str environment_id: (optional) Unique identifier for the environment.
    :attr str name: (optional) Name that identifies the environment.
    :attr str description: (optional) Description of the environment.
    :attr datetime created: (optional) Creation date of the environment, in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr datetime updated: (optional) Date of most recent environment update, in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str status: (optional) Status of the environment.
    :attr bool read_only: (optional) If true, then the environment contains read-only collections which are maintained by IBM.
    :attr int size: (optional) **Deprecated**: Size of the environment.
    :attr IndexCapacity index_capacity: (optional) Details about the resource usage and capacity of the environment.
    """

    def __init__(self,
                 environment_id=None,
                 name=None,
                 description=None,
                 created=None,
                 updated=None,
                 status=None,
                 read_only=None,
                 size=None,
                 index_capacity=None):
        """
        Initialize a Environment object.

        :param str environment_id: (optional) Unique identifier for the environment.
        :param str name: (optional) Name that identifies the environment.
        :param str description: (optional) Description of the environment.
        :param datetime created: (optional) Creation date of the environment, in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param datetime updated: (optional) Date of most recent environment update, in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str status: (optional) Status of the environment.
        :param bool read_only: (optional) If true, then the environment contains read-only collections which are maintained by IBM.
        :param int size: (optional) **Deprecated**: Size of the environment.
        :param IndexCapacity index_capacity: (optional) Details about the resource usage and capacity of the environment.
        """
        self.environment_id = environment_id
        self.name = name
        self.description = description
        self.created = created
        self.updated = updated
        self.status = status
        self.read_only = read_only
        self.size = size
        self.index_capacity = index_capacity

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Environment object from a json dictionary."""
        args = {}
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
        if 'index_capacity' in _dict:
            args['index_capacity'] = IndexCapacity._from_dict(
                _dict.get('index_capacity'))
        return cls(**args)

    def _to_dict(self):
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
        if hasattr(self, 'index_capacity') and self.index_capacity is not None:
            _dict['index_capacity'] = self.index_capacity._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this Environment object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentDocuments(object):
    """
    Summary of the document usage statistics for the environment.

    :attr int indexed: (optional) Number of documents indexed for the environment.
    :attr int maximum_allowed: (optional) Total number of documents allowed in the environment's capacity.
    """

    def __init__(self, indexed=None, maximum_allowed=None):
        """
        Initialize a EnvironmentDocuments object.

        :param int indexed: (optional) Number of documents indexed for the environment.
        :param int maximum_allowed: (optional) Total number of documents allowed in the environment's capacity.
        """
        self.indexed = indexed
        self.maximum_allowed = maximum_allowed

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentDocuments object from a json dictionary."""
        args = {}
        if 'indexed' in _dict:
            args['indexed'] = _dict.get('indexed')
        if 'maximum_allowed' in _dict:
            args['maximum_allowed'] = _dict.get('maximum_allowed')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'indexed') and self.indexed is not None:
            _dict['indexed'] = self.indexed
        if hasattr(self,
                   'maximum_allowed') and self.maximum_allowed is not None:
            _dict['maximum_allowed'] = self.maximum_allowed
        return _dict

    def __str__(self):
        """Return a `str` version of this EnvironmentDocuments object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Expansion(object):
    """
    An expansion definition. Each object respresents one set of expandable strings. For
    example, you could have expansions for the word `hot` in one object, and expansions
    for the word `cold` in another.

    :attr list[str] input_terms: (optional) A list of terms that will be expanded for this expansion. If specified, only the items in this list are expanded.
    :attr list[str] expanded_terms: A list of terms that this expansion will be expanded to. If specified without `input_terms`, it also functions as the input term list.
    """

    def __init__(self, expanded_terms, input_terms=None):
        """
        Initialize a Expansion object.

        :param list[str] expanded_terms: A list of terms that this expansion will be expanded to. If specified without `input_terms`, it also functions as the input term list.
        :param list[str] input_terms: (optional) A list of terms that will be expanded for this expansion. If specified, only the items in this list are expanded.
        """
        self.input_terms = input_terms
        self.expanded_terms = expanded_terms

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Expansion object from a json dictionary."""
        args = {}
        if 'input_terms' in _dict:
            args['input_terms'] = _dict.get('input_terms')
        if 'expanded_terms' in _dict:
            args['expanded_terms'] = _dict.get('expanded_terms')
        else:
            raise ValueError(
                'Required property \'expanded_terms\' not present in Expansion JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input_terms') and self.input_terms is not None:
            _dict['input_terms'] = self.input_terms
        if hasattr(self, 'expanded_terms') and self.expanded_terms is not None:
            _dict['expanded_terms'] = self.expanded_terms
        return _dict

    def __str__(self):
        """Return a `str` version of this Expansion object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Expansions(object):
    """
    The query expansion definitions for the specified collection.

    :attr list[Expansion] expansions: An array of query expansion definitions.    Each object in the `expansions` array represents a term or set of terms that will be expanded into other terms. Each expansion object can be configured so that all terms are expanded to all other terms in the object - bi-directional, or a set list of terms can be expanded into a second list of terms - uni-directional.   To create a bi-directional expansion specify an `expanded_terms` array. When found in a query, all items in the `expanded_terms` array are then expanded to the other items in the same array.   To create a uni-directional expansion, specify both an array of `input_terms` and an array of `expanded_terms`. When items in the `input_terms` array are present in a query, they are expanded using the items listed in the `expanded_terms` array.
    """

    def __init__(self, expansions):
        """
        Initialize a Expansions object.

        :param list[Expansion] expansions: An array of query expansion definitions.    Each object in the `expansions` array represents a term or set of terms that will be expanded into other terms. Each expansion object can be configured so that all terms are expanded to all other terms in the object - bi-directional, or a set list of terms can be expanded into a second list of terms - uni-directional.   To create a bi-directional expansion specify an `expanded_terms` array. When found in a query, all items in the `expanded_terms` array are then expanded to the other items in the same array.   To create a uni-directional expansion, specify both an array of `input_terms` and an array of `expanded_terms`. When items in the `input_terms` array are present in a query, they are expanded using the items listed in the `expanded_terms` array.
        """
        self.expansions = expansions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Expansions object from a json dictionary."""
        args = {}
        if 'expansions' in _dict:
            args['expansions'] = [
                Expansion._from_dict(x) for x in (_dict.get('expansions'))
            ]
        else:
            raise ValueError(
                'Required property \'expansions\' not present in Expansions JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'expansions') and self.expansions is not None:
            _dict['expansions'] = [x._to_dict() for x in self.expansions]
        return _dict

    def __str__(self):
        """Return a `str` version of this Expansions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Field(object):
    """
    Field.

    :attr str field_name: (optional) The name of the field.
    :attr str field_type: (optional) The type of the field.
    """

    def __init__(self, field_name=None, field_type=None):
        """
        Initialize a Field object.

        :param str field_name: (optional) The name of the field.
        :param str field_type: (optional) The type of the field.
        """
        self.field_name = field_name
        self.field_type = field_type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Field object from a json dictionary."""
        args = {}
        if 'field' in _dict or 'field_name' in _dict:
            args['field_name'] = _dict.get('field') or _dict.get('field_name')
        if 'type' in _dict or 'field_type' in _dict:
            args['field_type'] = _dict.get('type') or _dict.get('field_type')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field_name') and self.field_name is not None:
            _dict['field'] = self.field_name
        if hasattr(self, 'field_type') and self.field_type is not None:
            _dict['type'] = self.field_type
        return _dict

    def __str__(self):
        """Return a `str` version of this Field object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FontSetting(object):
    """
    FontSetting.

    :attr int level: (optional)
    :attr int min_size: (optional)
    :attr int max_size: (optional)
    :attr bool bold: (optional)
    :attr bool italic: (optional)
    :attr str name: (optional)
    """

    def __init__(self,
                 level=None,
                 min_size=None,
                 max_size=None,
                 bold=None,
                 italic=None,
                 name=None):
        """
        Initialize a FontSetting object.

        :param int level: (optional)
        :param int min_size: (optional)
        :param int max_size: (optional)
        :param bool bold: (optional)
        :param bool italic: (optional)
        :param str name: (optional)
        """
        self.level = level
        self.min_size = min_size
        self.max_size = max_size
        self.bold = bold
        self.italic = italic
        self.name = name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FontSetting object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this FontSetting object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HtmlSettings(object):
    """
    A list of HTML conversion settings.

    :attr list[str] exclude_tags_completely: (optional)
    :attr list[str] exclude_tags_keep_content: (optional)
    :attr XPathPatterns keep_content: (optional)
    :attr XPathPatterns exclude_content: (optional)
    :attr list[str] keep_tag_attributes: (optional)
    :attr list[str] exclude_tag_attributes: (optional)
    """

    def __init__(self,
                 exclude_tags_completely=None,
                 exclude_tags_keep_content=None,
                 keep_content=None,
                 exclude_content=None,
                 keep_tag_attributes=None,
                 exclude_tag_attributes=None):
        """
        Initialize a HtmlSettings object.

        :param list[str] exclude_tags_completely: (optional)
        :param list[str] exclude_tags_keep_content: (optional)
        :param XPathPatterns keep_content: (optional)
        :param XPathPatterns exclude_content: (optional)
        :param list[str] keep_tag_attributes: (optional)
        :param list[str] exclude_tag_attributes: (optional)
        """
        self.exclude_tags_completely = exclude_tags_completely
        self.exclude_tags_keep_content = exclude_tags_keep_content
        self.keep_content = keep_content
        self.exclude_content = exclude_content
        self.keep_tag_attributes = keep_tag_attributes
        self.exclude_tag_attributes = exclude_tag_attributes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HtmlSettings object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this HtmlSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IndexCapacity(object):
    """
    Details about the resource usage and capacity of the environment.

    :attr EnvironmentDocuments documents: (optional) Summary of the document usage statistics for the environment.
    :attr DiskUsage disk_usage: (optional) Summary of the disk usage of the environment.
    :attr CollectionUsage collections: (optional) Summary of the collection usage in the environment.
    :attr MemoryUsage memory_usage: (optional) **Deprecated**: Summary of the memory usage of the environment.
    """

    def __init__(self,
                 documents=None,
                 disk_usage=None,
                 collections=None,
                 memory_usage=None):
        """
        Initialize a IndexCapacity object.

        :param EnvironmentDocuments documents: (optional) Summary of the document usage statistics for the environment.
        :param DiskUsage disk_usage: (optional) Summary of the disk usage of the environment.
        :param CollectionUsage collections: (optional) Summary of the collection usage in the environment.
        :param MemoryUsage memory_usage: (optional) **Deprecated**: Summary of the memory usage of the environment.
        """
        self.documents = documents
        self.disk_usage = disk_usage
        self.collections = collections
        self.memory_usage = memory_usage

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IndexCapacity object from a json dictionary."""
        args = {}
        if 'documents' in _dict:
            args['documents'] = EnvironmentDocuments._from_dict(
                _dict.get('documents'))
        if 'disk_usage' in _dict:
            args['disk_usage'] = DiskUsage._from_dict(_dict.get('disk_usage'))
        if 'collections' in _dict:
            args['collections'] = CollectionUsage._from_dict(
                _dict.get('collections'))
        if 'memory_usage' in _dict:
            args['memory_usage'] = MemoryUsage._from_dict(
                _dict.get('memory_usage'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'documents') and self.documents is not None:
            _dict['documents'] = self.documents._to_dict()
        if hasattr(self, 'disk_usage') and self.disk_usage is not None:
            _dict['disk_usage'] = self.disk_usage._to_dict()
        if hasattr(self, 'collections') and self.collections is not None:
            _dict['collections'] = self.collections._to_dict()
        if hasattr(self, 'memory_usage') and self.memory_usage is not None:
            _dict['memory_usage'] = self.memory_usage._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this IndexCapacity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListCollectionFieldsResponse(object):
    """
    The list of fetched fields.  The fields are returned using a fully qualified name
    format, however, the format differs slightly from that used by the query operations.
     * Fields which contain nested JSON objects are assigned a type of "nested".    *
    Fields which belong to a nested object are prefixed with `.properties` (for example,
    `warnings.properties.severity` means that the `warnings` object has a property called
    `severity`).    * Fields returned from the News collection are prefixed with
    `v{N}-fullnews-t3-{YEAR}.mappings` (for example,
    `v5-fullnews-t3-2016.mappings.text.properties.author`).

    :attr list[Field] fields: (optional) An array containing information about each field in the collections.
    """

    def __init__(self, fields=None):
        """
        Initialize a ListCollectionFieldsResponse object.

        :param list[Field] fields: (optional) An array containing information about each field in the collections.
        """
        self.fields = fields

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCollectionFieldsResponse object from a json dictionary."""
        args = {}
        if 'fields' in _dict:
            args['fields'] = [
                Field._from_dict(x) for x in (_dict.get('fields'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = [x._to_dict() for x in self.fields]
        return _dict

    def __str__(self):
        """Return a `str` version of this ListCollectionFieldsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListCollectionsResponse(object):
    """
    ListCollectionsResponse.

    :attr list[Collection] collections: (optional) An array containing information about each collection in the environment.
    """

    def __init__(self, collections=None):
        """
        Initialize a ListCollectionsResponse object.

        :param list[Collection] collections: (optional) An array containing information about each collection in the environment.
        """
        self.collections = collections

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCollectionsResponse object from a json dictionary."""
        args = {}
        if 'collections' in _dict:
            args['collections'] = [
                Collection._from_dict(x) for x in (_dict.get('collections'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collections') and self.collections is not None:
            _dict['collections'] = [x._to_dict() for x in self.collections]
        return _dict

    def __str__(self):
        """Return a `str` version of this ListCollectionsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListConfigurationsResponse(object):
    """
    ListConfigurationsResponse.

    :attr list[Configuration] configurations: (optional) An array of Configurations that are available for the service instance.
    """

    def __init__(self, configurations=None):
        """
        Initialize a ListConfigurationsResponse object.

        :param list[Configuration] configurations: (optional) An array of Configurations that are available for the service instance.
        """
        self.configurations = configurations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListConfigurationsResponse object from a json dictionary."""
        args = {}
        if 'configurations' in _dict:
            args['configurations'] = [
                Configuration._from_dict(x)
                for x in (_dict.get('configurations'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'configurations') and self.configurations is not None:
            _dict['configurations'] = [
                x._to_dict() for x in self.configurations
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this ListConfigurationsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListEnvironmentsResponse(object):
    """
    ListEnvironmentsResponse.

    :attr list[Environment] environments: (optional) An array of [environments] that are available for the service instance.
    """

    def __init__(self, environments=None):
        """
        Initialize a ListEnvironmentsResponse object.

        :param list[Environment] environments: (optional) An array of [environments] that are available for the service instance.
        """
        self.environments = environments

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEnvironmentsResponse object from a json dictionary."""
        args = {}
        if 'environments' in _dict:
            args['environments'] = [
                Environment._from_dict(x) for x in (_dict.get('environments'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environments') and self.environments is not None:
            _dict['environments'] = [x._to_dict() for x in self.environments]
        return _dict

    def __str__(self):
        """Return a `str` version of this ListEnvironmentsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MemoryUsage(object):
    """
    **Deprecated**: Summary of the memory usage statistics for this environment.

    :attr int used_bytes: (optional) **Deprecated**: Number of bytes used in the environment's memory capacity.
    :attr int total_bytes: (optional) **Deprecated**: Total number of bytes available in the environment's memory capacity.
    :attr str used: (optional) **Deprecated**: Amount of memory capacity used, in KB or GB format.
    :attr str total: (optional) **Deprecated**: Total amount of the environment's memory capacity, in KB or GB format.
    :attr float percent_used: (optional) **Deprecated**: Percentage of the environment's memory capacity that is being used.
    """

    def __init__(self,
                 used_bytes=None,
                 total_bytes=None,
                 used=None,
                 total=None,
                 percent_used=None):
        """
        Initialize a MemoryUsage object.

        :param int used_bytes: (optional) **Deprecated**: Number of bytes used in the environment's memory capacity.
        :param int total_bytes: (optional) **Deprecated**: Total number of bytes available in the environment's memory capacity.
        :param str used: (optional) **Deprecated**: Amount of memory capacity used, in KB or GB format.
        :param str total: (optional) **Deprecated**: Total amount of the environment's memory capacity, in KB or GB format.
        :param float percent_used: (optional) **Deprecated**: Percentage of the environment's memory capacity that is being used.
        """
        self.used_bytes = used_bytes
        self.total_bytes = total_bytes
        self.used = used
        self.total = total
        self.percent_used = percent_used

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MemoryUsage object from a json dictionary."""
        args = {}
        if 'used_bytes' in _dict:
            args['used_bytes'] = _dict.get('used_bytes')
        if 'total_bytes' in _dict:
            args['total_bytes'] = _dict.get('total_bytes')
        if 'used' in _dict:
            args['used'] = _dict.get('used')
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        if 'percent_used' in _dict:
            args['percent_used'] = _dict.get('percent_used')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'used_bytes') and self.used_bytes is not None:
            _dict['used_bytes'] = self.used_bytes
        if hasattr(self, 'total_bytes') and self.total_bytes is not None:
            _dict['total_bytes'] = self.total_bytes
        if hasattr(self, 'used') and self.used is not None:
            _dict['used'] = self.used
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        if hasattr(self, 'percent_used') and self.percent_used is not None:
            _dict['percent_used'] = self.percent_used
        return _dict

    def __str__(self):
        """Return a `str` version of this MemoryUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentCategories(object):
    """
    An object that indicates the Categories enrichment will be applied to the specified
    field.

    """

    def __init__(self, **kwargs):
        """
        Initialize a NluEnrichmentCategories object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentCategories object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {}
        if not hasattr(self, '_additionalProperties'):
            super(NluEnrichmentCategories, self).__setattr__(
                '_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(NluEnrichmentCategories, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this NluEnrichmentCategories object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentEmotion(object):
    """
    An object specifying the emotion detection enrichment and related parameters.

    :attr bool document: (optional) When `true`, emotion detection is performed on the entire field.
    :attr list[str] targets: (optional) A comma-separated list of target strings that will have any associated emotions detected.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a NluEnrichmentEmotion object.

        :param bool document: (optional) When `true`, emotion detection is performed on the entire field.
        :param list[str] targets: (optional) A comma-separated list of target strings that will have any associated emotions detected.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentEmotion object from a json dictionary."""
        args = {}
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def __str__(self):
        """Return a `str` version of this NluEnrichmentEmotion object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentEntities(object):
    """
    An object speficying the Entities enrichment and related parameters.

    :attr bool sentiment: (optional) When `true`, sentiment analysis of entities will be performed on the specified field.
    :attr bool emotion: (optional) When `true`, emotion detection of entities will be performed on the specified field.
    :attr int limit: (optional) The maximum number of entities to extract for each instance of the specified field.
    :attr bool mentions: (optional) When `true`, the number of mentions of each identified entity is recorded. The default is `false`.
    :attr bool mention_types: (optional) When `true`, the types of mentions for each idetifieid entity is recorded. The default is `false`.
    :attr bool sentence_location: (optional) When `true`, a list of sentence locations for each instance of each identified entity is recorded. The default is `false`.
    :attr str model: (optional) The enrichement model to use with entity extraction. May be a custom model provided by Watson Knowledge Studio, the public model for use with Knowledge Graph `en-news`, or the default public model `alchemy`.
    """

    def __init__(self,
                 sentiment=None,
                 emotion=None,
                 limit=None,
                 mentions=None,
                 mention_types=None,
                 sentence_location=None,
                 model=None):
        """
        Initialize a NluEnrichmentEntities object.

        :param bool sentiment: (optional) When `true`, sentiment analysis of entities will be performed on the specified field.
        :param bool emotion: (optional) When `true`, emotion detection of entities will be performed on the specified field.
        :param int limit: (optional) The maximum number of entities to extract for each instance of the specified field.
        :param bool mentions: (optional) When `true`, the number of mentions of each identified entity is recorded. The default is `false`.
        :param bool mention_types: (optional) When `true`, the types of mentions for each idetifieid entity is recorded. The default is `false`.
        :param bool sentence_location: (optional) When `true`, a list of sentence locations for each instance of each identified entity is recorded. The default is `false`.
        :param str model: (optional) The enrichement model to use with entity extraction. May be a custom model provided by Watson Knowledge Studio, the public model for use with Knowledge Graph `en-news`, or the default public model `alchemy`.
        """
        self.sentiment = sentiment
        self.emotion = emotion
        self.limit = limit
        self.mentions = mentions
        self.mention_types = mention_types
        self.sentence_location = sentence_location
        self.model = model

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentEntities object from a json dictionary."""
        args = {}
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
        if 'sentence_location' in _dict:
            args['sentence_location'] = _dict.get('sentence_location')
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    def _to_dict(self):
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
        if hasattr(self,
                   'sentence_location') and self.sentence_location is not None:
            _dict['sentence_location'] = self.sentence_location
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def __str__(self):
        """Return a `str` version of this NluEnrichmentEntities object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentFeatures(object):
    """
    NluEnrichmentFeatures.

    :attr NluEnrichmentKeywords keywords: (optional) An object specifying the Keyword enrichment and related parameters.
    :attr NluEnrichmentEntities entities: (optional) An object speficying the Entities enrichment and related parameters.
    :attr NluEnrichmentSentiment sentiment: (optional) An object specifying the sentiment extraction enrichment and related parameters.
    :attr NluEnrichmentEmotion emotion: (optional) An object specifying the emotion detection enrichment and related parameters.
    :attr NluEnrichmentCategories categories: (optional) An object specifying the categories enrichment and related parameters.
    :attr NluEnrichmentSemanticRoles semantic_roles: (optional) An object specifiying the semantic roles enrichment and related parameters.
    :attr NluEnrichmentRelations relations: (optional) An object specifying the relations enrichment and related parameters.
    """

    def __init__(self,
                 keywords=None,
                 entities=None,
                 sentiment=None,
                 emotion=None,
                 categories=None,
                 semantic_roles=None,
                 relations=None):
        """
        Initialize a NluEnrichmentFeatures object.

        :param NluEnrichmentKeywords keywords: (optional) An object specifying the Keyword enrichment and related parameters.
        :param NluEnrichmentEntities entities: (optional) An object speficying the Entities enrichment and related parameters.
        :param NluEnrichmentSentiment sentiment: (optional) An object specifying the sentiment extraction enrichment and related parameters.
        :param NluEnrichmentEmotion emotion: (optional) An object specifying the emotion detection enrichment and related parameters.
        :param NluEnrichmentCategories categories: (optional) An object specifying the categories enrichment and related parameters.
        :param NluEnrichmentSemanticRoles semantic_roles: (optional) An object specifiying the semantic roles enrichment and related parameters.
        :param NluEnrichmentRelations relations: (optional) An object specifying the relations enrichment and related parameters.
        """
        self.keywords = keywords
        self.entities = entities
        self.sentiment = sentiment
        self.emotion = emotion
        self.categories = categories
        self.semantic_roles = semantic_roles
        self.relations = relations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentFeatures object from a json dictionary."""
        args = {}
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
        return cls(**args)

    def _to_dict(self):
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
        return _dict

    def __str__(self):
        """Return a `str` version of this NluEnrichmentFeatures object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentKeywords(object):
    """
    An object specifying the Keyword enrichment and related parameters.

    :attr bool sentiment: (optional) When `true`, sentiment analysis of keywords will be performed on the specified field.
    :attr bool emotion: (optional) When `true`, emotion detection of keywords will be performed on the specified field.
    :attr int limit: (optional) The maximum number of keywords to extract for each instance of the specified field.
    """

    def __init__(self, sentiment=None, emotion=None, limit=None):
        """
        Initialize a NluEnrichmentKeywords object.

        :param bool sentiment: (optional) When `true`, sentiment analysis of keywords will be performed on the specified field.
        :param bool emotion: (optional) When `true`, emotion detection of keywords will be performed on the specified field.
        :param int limit: (optional) The maximum number of keywords to extract for each instance of the specified field.
        """
        self.sentiment = sentiment
        self.emotion = emotion
        self.limit = limit

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentKeywords object from a json dictionary."""
        args = {}
        if 'sentiment' in _dict:
            args['sentiment'] = _dict.get('sentiment')
        if 'emotion' in _dict:
            args['emotion'] = _dict.get('emotion')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def __str__(self):
        """Return a `str` version of this NluEnrichmentKeywords object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentRelations(object):
    """
    An object specifying the relations enrichment and related parameters.

    :attr str model: (optional) *For use with `natural_language_understanding` enrichments only.* The enrichement model to use with relationship extraction. May be a custom model provided by Watson Knowledge Studio, the public model for use with Knowledge Graph `en-news`, the default is`en-news`.
    """

    def __init__(self, model=None):
        """
        Initialize a NluEnrichmentRelations object.

        :param str model: (optional) *For use with `natural_language_understanding` enrichments only.* The enrichement model to use with relationship extraction. May be a custom model provided by Watson Knowledge Studio, the public model for use with Knowledge Graph `en-news`, the default is`en-news`.
        """
        self.model = model

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentRelations object from a json dictionary."""
        args = {}
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def __str__(self):
        """Return a `str` version of this NluEnrichmentRelations object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentSemanticRoles(object):
    """
    An object specifiying the semantic roles enrichment and related parameters.

    :attr bool entities: (optional) When `true` entities are extracted from the identified sentence parts.
    :attr bool keywords: (optional) When `true`, keywords are extracted from the identified sentence parts.
    :attr int limit: (optional) The maximum number of semantic roles enrichments to extact from each instance of the specified field.
    """

    def __init__(self, entities=None, keywords=None, limit=None):
        """
        Initialize a NluEnrichmentSemanticRoles object.

        :param bool entities: (optional) When `true` entities are extracted from the identified sentence parts.
        :param bool keywords: (optional) When `true`, keywords are extracted from the identified sentence parts.
        :param int limit: (optional) The maximum number of semantic roles enrichments to extact from each instance of the specified field.
        """
        self.entities = entities
        self.keywords = keywords
        self.limit = limit

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentSemanticRoles object from a json dictionary."""
        args = {}
        if 'entities' in _dict:
            args['entities'] = _dict.get('entities')
        if 'keywords' in _dict:
            args['keywords'] = _dict.get('keywords')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = self.entities
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def __str__(self):
        """Return a `str` version of this NluEnrichmentSemanticRoles object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NluEnrichmentSentiment(object):
    """
    An object specifying the sentiment extraction enrichment and related parameters.

    :attr bool document: (optional) When `true`, sentiment analysis is performed on the entire field.
    :attr list[str] targets: (optional) A comma-separated list of target strings that will have any associated sentiment analyzed.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a NluEnrichmentSentiment object.

        :param bool document: (optional) When `true`, sentiment analysis is performed on the entire field.
        :param list[str] targets: (optional) A comma-separated list of target strings that will have any associated sentiment analyzed.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NluEnrichmentSentiment object from a json dictionary."""
        args = {}
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def __str__(self):
        """Return a `str` version of this NluEnrichmentSentiment object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class NormalizationOperation(object):
    """
    NormalizationOperation.

    :attr str operation: (optional) Identifies what type of operation to perform.   **copy** - Copies the value of the `source_field` to the `destination_field` field. If the `destination_field` already exists, then the value of the `source_field` overwrites the original value of the `destination_field`.   **move** - Renames (moves) the `source_field` to the `destination_field`. If the `destination_field` already exists, then the value of the `source_field` overwrites the original value of the `destination_field`. Rename is identical to copy, except that the `source_field` is removed after the value has been copied to the `destination_field` (it is the same as a _copy_ followed by a _remove_).   **merge** - Merges the value of the `source_field` with the value of the `destination_field`. The `destination_field` is converted into an array if it is not already an array, and the value of the `source_field` is appended to the array. This operation removes the `source_field` after the merge. If the `source_field` does not exist in the current document, then the `destination_field` is still converted into an array (if it is not an array already). This is ensures the type for `destination_field` is consistent across all documents.   **remove** - Deletes the `source_field` field. The `destination_field` is ignored for this operation.   **remove_nulls** - Removes all nested null (blank) leif values from the JSON tree. `source_field` and `destination_field` are ignored by this operation because _remove_nulls_ operates on the entire JSON tree. Typically, `remove_nulls` is invoked as the last normalization operation (if it is inoked at all, it can be time-expensive).
    :attr str source_field: (optional) The source field for the operation.
    :attr str destination_field: (optional) The destination field for the operation.
    """

    def __init__(self,
                 operation=None,
                 source_field=None,
                 destination_field=None):
        """
        Initialize a NormalizationOperation object.

        :param str operation: (optional) Identifies what type of operation to perform.   **copy** - Copies the value of the `source_field` to the `destination_field` field. If the `destination_field` already exists, then the value of the `source_field` overwrites the original value of the `destination_field`.   **move** - Renames (moves) the `source_field` to the `destination_field`. If the `destination_field` already exists, then the value of the `source_field` overwrites the original value of the `destination_field`. Rename is identical to copy, except that the `source_field` is removed after the value has been copied to the `destination_field` (it is the same as a _copy_ followed by a _remove_).   **merge** - Merges the value of the `source_field` with the value of the `destination_field`. The `destination_field` is converted into an array if it is not already an array, and the value of the `source_field` is appended to the array. This operation removes the `source_field` after the merge. If the `source_field` does not exist in the current document, then the `destination_field` is still converted into an array (if it is not an array already). This is ensures the type for `destination_field` is consistent across all documents.   **remove** - Deletes the `source_field` field. The `destination_field` is ignored for this operation.   **remove_nulls** - Removes all nested null (blank) leif values from the JSON tree. `source_field` and `destination_field` are ignored by this operation because _remove_nulls_ operates on the entire JSON tree. Typically, `remove_nulls` is invoked as the last normalization operation (if it is inoked at all, it can be time-expensive).
        :param str source_field: (optional) The source field for the operation.
        :param str destination_field: (optional) The destination field for the operation.
        """
        self.operation = operation
        self.source_field = source_field
        self.destination_field = destination_field

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NormalizationOperation object from a json dictionary."""
        args = {}
        if 'operation' in _dict:
            args['operation'] = _dict.get('operation')
        if 'source_field' in _dict:
            args['source_field'] = _dict.get('source_field')
        if 'destination_field' in _dict:
            args['destination_field'] = _dict.get('destination_field')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this NormalizationOperation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Notice(object):
    """
    A notice produced for the collection.

    :attr str notice_id: (optional) Identifies the notice. Many notices might have the same ID. This field exists so that user applications can programmatically identify a notice and take automatic corrective action.
    :attr datetime created: (optional) The creation date of the collection in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str document_id: (optional) Unique identifier of the document.
    :attr str query_id: (optional) Unique identifier of the query used for relevance training.
    :attr str severity: (optional) Severity level of the notice.
    :attr str step: (optional) Ingestion or training step in which the notice occurred.
    :attr str description: (optional) The description of the notice.
    """

    def __init__(self,
                 notice_id=None,
                 created=None,
                 document_id=None,
                 query_id=None,
                 severity=None,
                 step=None,
                 description=None):
        """
        Initialize a Notice object.

        :param str notice_id: (optional) Identifies the notice. Many notices might have the same ID. This field exists so that user applications can programmatically identify a notice and take automatic corrective action.
        :param datetime created: (optional) The creation date of the collection in the format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
        :param str document_id: (optional) Unique identifier of the document.
        :param str query_id: (optional) Unique identifier of the query used for relevance training.
        :param str severity: (optional) Severity level of the notice.
        :param str step: (optional) Ingestion or training step in which the notice occurred.
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
    def _from_dict(cls, _dict):
        """Initialize a Notice object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Notice object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PdfHeadingDetection(object):
    """
    PdfHeadingDetection.

    :attr list[FontSetting] fonts: (optional)
    """

    def __init__(self, fonts=None):
        """
        Initialize a PdfHeadingDetection object.

        :param list[FontSetting] fonts: (optional)
        """
        self.fonts = fonts

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PdfHeadingDetection object from a json dictionary."""
        args = {}
        if 'fonts' in _dict:
            args['fonts'] = [
                FontSetting._from_dict(x) for x in (_dict.get('fonts'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fonts') and self.fonts is not None:
            _dict['fonts'] = [x._to_dict() for x in self.fonts]
        return _dict

    def __str__(self):
        """Return a `str` version of this PdfHeadingDetection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PdfSettings(object):
    """
    A list of PDF conversion settings.

    :attr PdfHeadingDetection heading: (optional)
    """

    def __init__(self, heading=None):
        """
        Initialize a PdfSettings object.

        :param PdfHeadingDetection heading: (optional)
        """
        self.heading = heading

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PdfSettings object from a json dictionary."""
        args = {}
        if 'heading' in _dict:
            args['heading'] = PdfHeadingDetection._from_dict(
                _dict.get('heading'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'heading') and self.heading is not None:
            _dict['heading'] = self.heading._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this PdfSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregation(object):
    """
    An aggregation produced by the Discovery service to analyze the input provided.

    :attr str type: (optional) The type of aggregation command used. For example: term, filter, max, min, etc.
    :attr list[AggregationResult] results: (optional)
    :attr int matching_results: (optional) Number of matching results.
    :attr list[QueryAggregation] aggregations: (optional) Aggregations returned by the Discovery service.
    """

    def __init__(self,
                 type=None,
                 results=None,
                 matching_results=None,
                 aggregations=None):
        """
        Initialize a QueryAggregation object.

        :param str type: (optional) The type of aggregation command used. For example: term, filter, max, min, etc.
        :param list[AggregationResult] results: (optional)
        :param int matching_results: (optional) Number of matching results.
        :param list[QueryAggregation] aggregations: (optional) Aggregations returned by the Discovery service.
        """
        self.type = type
        self.results = results
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregation object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this QueryAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryEntitiesContext(object):
    """
    Entity text to provide context for the queried entity and rank based on that
    association. For example, if you wanted to query the city of London in England your
    query would look for `London` with the context of `England`.

    :attr str text: (optional) Entity text to provide context for the queried entity and rank based on that association. For example, if you wanted to query the city of London in England your query would look for `London` with the context of `England`.
    """

    def __init__(self, text=None):
        """
        Initialize a QueryEntitiesContext object.

        :param str text: (optional) Entity text to provide context for the queried entity and rank based on that association. For example, if you wanted to query the city of London in England your query would look for `London` with the context of `England`.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryEntitiesContext object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryEntitiesContext object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryEntitiesEntity(object):
    """
    A text string that appears within the entity text field.

    :attr str text: (optional) Entity text content.
    :attr str type: (optional) The type of the specified entity.
    """

    def __init__(self, text=None, type=None):
        """
        Initialize a QueryEntitiesEntity object.

        :param str text: (optional) Entity text content.
        :param str type: (optional) The type of the specified entity.
        """
        self.text = text
        self.type = type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryEntitiesEntity object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryEntitiesEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryEntitiesResponse(object):
    """
    An array of entities resulting from the query.

    :attr list[QueryEntitiesResponseItem] entities: (optional)
    """

    def __init__(self, entities=None):
        """
        Initialize a QueryEntitiesResponse object.

        :param list[QueryEntitiesResponseItem] entities: (optional)
        """
        self.entities = entities

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryEntitiesResponse object from a json dictionary."""
        args = {}
        if 'entities' in _dict:
            args['entities'] = [
                QueryEntitiesResponseItem._from_dict(x)
                for x in (_dict.get('entities'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryEntitiesResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryEntitiesResponseItem(object):
    """
    Object containing Entity query response information.

    :attr str text: (optional) Entity text content.
    :attr str type: (optional) The type of the result entity.
    :attr list[QueryEvidence] evidence: (optional) List of different evidentiary items to support the result.
    """

    def __init__(self, text=None, type=None, evidence=None):
        """
        Initialize a QueryEntitiesResponseItem object.

        :param str text: (optional) Entity text content.
        :param str type: (optional) The type of the result entity.
        :param list[QueryEvidence] evidence: (optional) List of different evidentiary items to support the result.
        """
        self.text = text
        self.type = type
        self.evidence = evidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryEntitiesResponseItem object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'evidence' in _dict:
            args['evidence'] = [
                QueryEvidence._from_dict(x) for x in (_dict.get('evidence'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'evidence') and self.evidence is not None:
            _dict['evidence'] = [x._to_dict() for x in self.evidence]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryEntitiesResponseItem object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryEvidence(object):
    """
    Description of evidence location supporting Knoweldge Graph query result.

    :attr str document_id: (optional) The docuemnt ID (as indexed in Discovery) of the evidence location.
    :attr str field: (optional) The field of the document where the supporting evidence was identified.
    :attr int start_offset: (optional) The start location of the evidence in the identified field. This value is inclusive.
    :attr int end_offset: (optional) The end location of the evidence in the identified field. This value is inclusive.
    :attr list[QueryEvidenceEntity] entities: (optional) An array of entity objects that show evidence of the result.
    """

    def __init__(self,
                 document_id=None,
                 field=None,
                 start_offset=None,
                 end_offset=None,
                 entities=None):
        """
        Initialize a QueryEvidence object.

        :param str document_id: (optional) The docuemnt ID (as indexed in Discovery) of the evidence location.
        :param str field: (optional) The field of the document where the supporting evidence was identified.
        :param int start_offset: (optional) The start location of the evidence in the identified field. This value is inclusive.
        :param int end_offset: (optional) The end location of the evidence in the identified field. This value is inclusive.
        :param list[QueryEvidenceEntity] entities: (optional) An array of entity objects that show evidence of the result.
        """
        self.document_id = document_id
        self.field = field
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.entities = entities

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryEvidence object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'start_offset' in _dict:
            args['start_offset'] = _dict.get('start_offset')
        if 'end_offset' in _dict:
            args['end_offset'] = _dict.get('end_offset')
        if 'entities' in _dict:
            args['entities'] = [
                QueryEvidenceEntity._from_dict(x)
                for x in (_dict.get('entities'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'start_offset') and self.start_offset is not None:
            _dict['start_offset'] = self.start_offset
        if hasattr(self, 'end_offset') and self.end_offset is not None:
            _dict['end_offset'] = self.end_offset
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryEvidence object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryEvidenceEntity(object):
    """
    Entity description and location within evidence field.

    :attr str type: (optional) The entity type for this entity. Possible types vary based on model used.
    :attr str text: (optional) The original text of this entity as found in the evidence field.
    :attr int start_offset: (optional) The start location of the entity text in the identified field. This value is inclusive.
    :attr int end_offset: (optional) The end location of the entity text in the identified field. This value is exclusive.
    """

    def __init__(self, type=None, text=None, start_offset=None,
                 end_offset=None):
        """
        Initialize a QueryEvidenceEntity object.

        :param str type: (optional) The entity type for this entity. Possible types vary based on model used.
        :param str text: (optional) The original text of this entity as found in the evidence field.
        :param int start_offset: (optional) The start location of the entity text in the identified field. This value is inclusive.
        :param int end_offset: (optional) The end location of the entity text in the identified field. This value is exclusive.
        """
        self.type = type
        self.text = text
        self.start_offset = start_offset
        self.end_offset = end_offset

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryEvidenceEntity object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'start_offset' in _dict:
            args['start_offset'] = _dict.get('start_offset')
        if 'end_offset' in _dict:
            args['end_offset'] = _dict.get('end_offset')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'start_offset') and self.start_offset is not None:
            _dict['start_offset'] = self.start_offset
        if hasattr(self, 'end_offset') and self.end_offset is not None:
            _dict['end_offset'] = self.end_offset
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryEvidenceEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryFilterType(object):
    """
    QueryFilterType.

    :attr list[str] exclude: (optional) A comma-separated list of types to exclude.
    :attr list[str] include: (optional) A comma-separated list of types to include. All other types are excluded.
    """

    def __init__(self, exclude=None, include=None):
        """
        Initialize a QueryFilterType object.

        :param list[str] exclude: (optional) A comma-separated list of types to exclude.
        :param list[str] include: (optional) A comma-separated list of types to include. All other types are excluded.
        """
        self.exclude = exclude
        self.include = include

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryFilterType object from a json dictionary."""
        args = {}
        if 'exclude' in _dict:
            args['exclude'] = _dict.get('exclude')
        if 'include' in _dict:
            args['include'] = _dict.get('include')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'exclude') and self.exclude is not None:
            _dict['exclude'] = self.exclude
        if hasattr(self, 'include') and self.include is not None:
            _dict['include'] = self.include
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryFilterType object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryNoticesResponse(object):
    """
    QueryNoticesResponse.

    :attr int matching_results: (optional)
    :attr list[QueryNoticesResult] results: (optional)
    :attr list[QueryAggregation] aggregations: (optional)
    :attr list[QueryPassages] passages: (optional)
    :attr int duplicates_removed: (optional)
    """

    def __init__(self,
                 matching_results=None,
                 results=None,
                 aggregations=None,
                 passages=None,
                 duplicates_removed=None):
        """
        Initialize a QueryNoticesResponse object.

        :param int matching_results: (optional)
        :param list[QueryNoticesResult] results: (optional)
        :param list[QueryAggregation] aggregations: (optional)
        :param list[QueryPassages] passages: (optional)
        :param int duplicates_removed: (optional)
        """
        self.matching_results = matching_results
        self.results = results
        self.aggregations = aggregations
        self.passages = passages
        self.duplicates_removed = duplicates_removed

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryNoticesResponse object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this QueryNoticesResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryNoticesResult(object):
    """
    QueryNoticesResult.

    :attr str id: (optional) The unique identifier of the document.
    :attr float score: (optional) *Deprecated* This field is now part of the `result_metadata` object.
    :attr object metadata: (optional) Metadata of the document.
    :attr str collection_id: (optional) The collection ID of the collection containing the document for this result.
    :attr QueryResultResultMetadata result_metadata: (optional) Metadata of the query result.
    :attr int code: (optional) The internal status code returned by the ingestion subsystem indicating the overall result of ingesting the source document.
    :attr str filename: (optional) Name of the original source file (if available).
    :attr str file_type: (optional) The type of the original source file.
    :attr str sha1: (optional) The SHA-1 hash of the original source file (formatted as a hexadecimal string).
    :attr list[Notice] notices: (optional) Array of notices for the document.
    """

    def __init__(self,
                 id=None,
                 score=None,
                 metadata=None,
                 collection_id=None,
                 result_metadata=None,
                 code=None,
                 filename=None,
                 file_type=None,
                 sha1=None,
                 notices=None,
                 **kwargs):
        """
        Initialize a QueryNoticesResult object.

        :param str id: (optional) The unique identifier of the document.
        :param float score: (optional) *Deprecated* This field is now part of the `result_metadata` object.
        :param object metadata: (optional) Metadata of the document.
        :param str collection_id: (optional) The collection ID of the collection containing the document for this result.
        :param QueryResultResultMetadata result_metadata: (optional) Metadata of the query result.
        :param int code: (optional) The internal status code returned by the ingestion subsystem indicating the overall result of ingesting the source document.
        :param str filename: (optional) Name of the original source file (if available).
        :param str file_type: (optional) The type of the original source file.
        :param str sha1: (optional) The SHA-1 hash of the original source file (formatted as a hexadecimal string).
        :param list[Notice] notices: (optional) Array of notices for the document.
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.score = score
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
    def _from_dict(cls, _dict):
        """Initialize a QueryNoticesResult object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict.get('id')
            del xtra['id']
        if 'score' in _dict:
            args['score'] = _dict.get('score')
            del xtra['score']
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
            del xtra['metadata']
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
            del xtra['collection_id']
        if 'result_metadata' in _dict:
            args['result_metadata'] = QueryResultResultMetadata._from_dict(
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
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

    def __setattr__(self, name, value):
        properties = {
            'id', 'score', 'metadata', 'collection_id', 'result_metadata',
            'code', 'filename', 'file_type', 'sha1', 'notices'
        }
        if not hasattr(self, '_additionalProperties'):
            super(QueryNoticesResult, self).__setattr__('_additionalProperties',
                                                        set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(QueryNoticesResult, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this QueryNoticesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryPassages(object):
    """
    QueryPassages.

    :attr str document_id: (optional) The unique identifier of the document from which the passage has been extracted.
    :attr float passage_score: (optional) The confidence score of the passages's analysis. A higher score indicates greater confidence.
    :attr str passage_text: (optional) The content of the extracted passage.
    :attr int start_offset: (optional) The position of the first character of the extracted passage in the originating field.
    :attr int end_offset: (optional) The position of the last character of the extracted passage in the originating field.
    :attr str field: (optional) The label of the field from which the passage has been extracted.
    """

    def __init__(self,
                 document_id=None,
                 passage_score=None,
                 passage_text=None,
                 start_offset=None,
                 end_offset=None,
                 field=None):
        """
        Initialize a QueryPassages object.

        :param str document_id: (optional) The unique identifier of the document from which the passage has been extracted.
        :param float passage_score: (optional) The confidence score of the passages's analysis. A higher score indicates greater confidence.
        :param str passage_text: (optional) The content of the extracted passage.
        :param int start_offset: (optional) The position of the first character of the extracted passage in the originating field.
        :param int end_offset: (optional) The position of the last character of the extracted passage in the originating field.
        :param str field: (optional) The label of the field from which the passage has been extracted.
        """
        self.document_id = document_id
        self.passage_score = passage_score
        self.passage_text = passage_text
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.field = field

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryPassages object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this QueryPassages object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryRelationsArgument(object):
    """
    QueryRelationsArgument.

    :attr list[QueryEntitiesEntity] entities: (optional)
    """

    def __init__(self, entities=None):
        """
        Initialize a QueryRelationsArgument object.

        :param list[QueryEntitiesEntity] entities: (optional)
        """
        self.entities = entities

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryRelationsArgument object from a json dictionary."""
        args = {}
        if 'entities' in _dict:
            args['entities'] = [
                QueryEntitiesEntity._from_dict(x)
                for x in (_dict.get('entities'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryRelationsArgument object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryRelationsEntity(object):
    """
    QueryRelationsEntity.

    :attr str text: (optional) Entity text content.
    :attr str type: (optional) The type of the specified entity.
    :attr bool exact: (optional) If false, implicit querying is performed. The default is `false`.
    """

    def __init__(self, text=None, type=None, exact=None):
        """
        Initialize a QueryRelationsEntity object.

        :param str text: (optional) Entity text content.
        :param str type: (optional) The type of the specified entity.
        :param bool exact: (optional) If false, implicit querying is performed. The default is `false`.
        """
        self.text = text
        self.type = type
        self.exact = exact

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryRelationsEntity object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'exact' in _dict:
            args['exact'] = _dict.get('exact')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'exact') and self.exact is not None:
            _dict['exact'] = self.exact
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryRelationsEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryRelationsFilter(object):
    """
    QueryRelationsFilter.

    :attr QueryFilterType relation_types: (optional) A list of relation types to include or exclude from the query.
    :attr QueryFilterType entity_types: (optional) A list of entity types to include or exclude from the query.
    :attr list[str] document_ids: (optional) A comma-separated list of document IDs to include in the query.
    """

    def __init__(self,
                 relation_types=None,
                 entity_types=None,
                 document_ids=None):
        """
        Initialize a QueryRelationsFilter object.

        :param QueryFilterType relation_types: (optional) A list of relation types to include or exclude from the query.
        :param QueryFilterType entity_types: (optional) A list of entity types to include or exclude from the query.
        :param list[str] document_ids: (optional) A comma-separated list of document IDs to include in the query.
        """
        self.relation_types = relation_types
        self.entity_types = entity_types
        self.document_ids = document_ids

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryRelationsFilter object from a json dictionary."""
        args = {}
        if 'relation_types' in _dict:
            args['relation_types'] = QueryFilterType._from_dict(
                _dict.get('relation_types'))
        if 'entity_types' in _dict:
            args['entity_types'] = QueryFilterType._from_dict(
                _dict.get('entity_types'))
        if 'document_ids' in _dict:
            args['document_ids'] = _dict.get('document_ids')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'relation_types') and self.relation_types is not None:
            _dict['relation_types'] = self.relation_types._to_dict()
        if hasattr(self, 'entity_types') and self.entity_types is not None:
            _dict['entity_types'] = self.entity_types._to_dict()
        if hasattr(self, 'document_ids') and self.document_ids is not None:
            _dict['document_ids'] = self.document_ids
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryRelationsFilter object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryRelationsRelationship(object):
    """
    QueryRelationsRelationship.

    :attr str type: (optional) The identified relationship type.
    :attr int frequency: (optional) The number of times the relationship is mentioned.
    :attr list[QueryRelationsArgument] arguments: (optional) Information about the relationship.
    :attr list[QueryEvidence] evidence: (optional) List of different evidentiary items to support the result.
    """

    def __init__(self, type=None, frequency=None, arguments=None,
                 evidence=None):
        """
        Initialize a QueryRelationsRelationship object.

        :param str type: (optional) The identified relationship type.
        :param int frequency: (optional) The number of times the relationship is mentioned.
        :param list[QueryRelationsArgument] arguments: (optional) Information about the relationship.
        :param list[QueryEvidence] evidence: (optional) List of different evidentiary items to support the result.
        """
        self.type = type
        self.frequency = frequency
        self.arguments = arguments
        self.evidence = evidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryRelationsRelationship object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'frequency' in _dict:
            args['frequency'] = _dict.get('frequency')
        if 'arguments' in _dict:
            args['arguments'] = [
                QueryRelationsArgument._from_dict(x)
                for x in (_dict.get('arguments'))
            ]
        if 'evidence' in _dict:
            args['evidence'] = [
                QueryEvidence._from_dict(x) for x in (_dict.get('evidence'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        if hasattr(self, 'arguments') and self.arguments is not None:
            _dict['arguments'] = [x._to_dict() for x in self.arguments]
        if hasattr(self, 'evidence') and self.evidence is not None:
            _dict['evidence'] = [x._to_dict() for x in self.evidence]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryRelationsRelationship object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryRelationsResponse(object):
    """
    QueryRelationsResponse.

    :attr list[QueryRelationsRelationship] relations: (optional)
    """

    def __init__(self, relations=None):
        """
        Initialize a QueryRelationsResponse object.

        :param list[QueryRelationsRelationship] relations: (optional)
        """
        self.relations = relations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryRelationsResponse object from a json dictionary."""
        args = {}
        if 'relations' in _dict:
            args['relations'] = [
                QueryRelationsRelationship._from_dict(x)
                for x in (_dict.get('relations'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'relations') and self.relations is not None:
            _dict['relations'] = [x._to_dict() for x in self.relations]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryRelationsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResponse(object):
    """
    A response containing the documents and aggregations for the query.

    :attr int matching_results: (optional)
    :attr list[QueryResult] results: (optional)
    :attr list[QueryAggregation] aggregations: (optional)
    :attr list[QueryPassages] passages: (optional)
    :attr int duplicates_removed: (optional)
    """

    def __init__(self,
                 matching_results=None,
                 results=None,
                 aggregations=None,
                 passages=None,
                 duplicates_removed=None):
        """
        Initialize a QueryResponse object.

        :param int matching_results: (optional)
        :param list[QueryResult] results: (optional)
        :param list[QueryAggregation] aggregations: (optional)
        :param list[QueryPassages] passages: (optional)
        :param int duplicates_removed: (optional)
        """
        self.matching_results = matching_results
        self.results = results
        self.aggregations = aggregations
        self.passages = passages
        self.duplicates_removed = duplicates_removed

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResponse object from a json dictionary."""
        args = {}
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
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this QueryResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResult(object):
    """
    QueryResult.

    :attr str id: (optional) The unique identifier of the document.
    :attr float score: (optional) *Deprecated* This field is now part of the `result_metadata` object.
    :attr object metadata: (optional) Metadata of the document.
    :attr str collection_id: (optional) The collection ID of the collection containing the document for this result.
    :attr QueryResultResultMetadata result_metadata: (optional) Metadata of the query result.
    """

    def __init__(self,
                 id=None,
                 score=None,
                 metadata=None,
                 collection_id=None,
                 result_metadata=None,
                 **kwargs):
        """
        Initialize a QueryResult object.

        :param str id: (optional) The unique identifier of the document.
        :param float score: (optional) *Deprecated* This field is now part of the `result_metadata` object.
        :param object metadata: (optional) Metadata of the document.
        :param str collection_id: (optional) The collection ID of the collection containing the document for this result.
        :param QueryResultResultMetadata result_metadata: (optional) Metadata of the query result.
        :param **kwargs: (optional) Any additional properties.
        """
        self.id = id
        self.score = score
        self.metadata = metadata
        self.collection_id = collection_id
        self.result_metadata = result_metadata
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResult object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'id' in _dict:
            args['id'] = _dict.get('id')
            del xtra['id']
        if 'score' in _dict:
            args['score'] = _dict.get('score')
            del xtra['score']
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
            del xtra['metadata']
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
            del xtra['collection_id']
        if 'result_metadata' in _dict:
            args['result_metadata'] = QueryResultResultMetadata._from_dict(
                _dict.get('result_metadata'))
            del xtra['result_metadata']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
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

    def __setattr__(self, name, value):
        properties = {
            'id', 'score', 'metadata', 'collection_id', 'result_metadata'
        }
        if not hasattr(self, '_additionalProperties'):
            super(QueryResult, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(QueryResult, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this QueryResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResultResultMetadata(object):
    """
    Metadata of a query result.

    :attr float score: (optional) The confidence score of the result's analysis. A higher score indicating greater confidence.
    """

    def __init__(self, score=None):
        """
        Initialize a QueryResultResultMetadata object.

        :param float score: (optional) The confidence score of the result's analysis. A higher score indicating greater confidence.
        """
        self.score = score

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResultResultMetadata object from a json dictionary."""
        args = {}
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryResultResultMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SegmentSettings(object):
    """
    A list of Document Segmentation settings.

    :attr bool enabled: (optional) Enables/disables the Document Segmentation feature.
    :attr list[str] selector_tags: (optional) Defines the heading level that splits into document segments. Valid values are h1, h2, h3, h4, h5, h6.
    """

    def __init__(self, enabled=None, selector_tags=None):
        """
        Initialize a SegmentSettings object.

        :param bool enabled: (optional) Enables/disables the Document Segmentation feature.
        :param list[str] selector_tags: (optional) Defines the heading level that splits into document segments. Valid values are h1, h2, h3, h4, h5, h6.
        """
        self.enabled = enabled
        self.selector_tags = selector_tags

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SegmentSettings object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'selector_tags' in _dict:
            args['selector_tags'] = _dict.get('selector_tags')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'selector_tags') and self.selector_tags is not None:
            _dict['selector_tags'] = self.selector_tags
        return _dict

    def __str__(self):
        """Return a `str` version of this SegmentSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TestDocument(object):
    """
    TestDocument.

    :attr str configuration_id: (optional) The unique identifier for the configuration.
    :attr str status: (optional) Status of the preview operation.
    :attr int enriched_field_units: (optional) The number of 10-kB chunks of field data that were enriched. This can be used to estimate the cost of running a real ingestion.
    :attr str original_media_type: (optional) Format of the test document.
    :attr list[DocumentSnapshot] snapshots: (optional) An array of objects that describe each step in the preview process.
    :attr list[Notice] notices: (optional) An array of notice messages about the preview operation.
    """

    def __init__(self,
                 configuration_id=None,
                 status=None,
                 enriched_field_units=None,
                 original_media_type=None,
                 snapshots=None,
                 notices=None):
        """
        Initialize a TestDocument object.

        :param str configuration_id: (optional) The unique identifier for the configuration.
        :param str status: (optional) Status of the preview operation.
        :param int enriched_field_units: (optional) The number of 10-kB chunks of field data that were enriched. This can be used to estimate the cost of running a real ingestion.
        :param str original_media_type: (optional) Format of the test document.
        :param list[DocumentSnapshot] snapshots: (optional) An array of objects that describe each step in the preview process.
        :param list[Notice] notices: (optional) An array of notice messages about the preview operation.
        """
        self.configuration_id = configuration_id
        self.status = status
        self.enriched_field_units = enriched_field_units
        self.original_media_type = original_media_type
        self.snapshots = snapshots
        self.notices = notices

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TestDocument object from a json dictionary."""
        args = {}
        if 'configuration_id' in _dict:
            args['configuration_id'] = _dict.get('configuration_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'enriched_field_units' in _dict:
            args['enriched_field_units'] = _dict.get('enriched_field_units')
        if 'original_media_type' in _dict:
            args['original_media_type'] = _dict.get('original_media_type')
        if 'snapshots' in _dict:
            args['snapshots'] = [
                DocumentSnapshot._from_dict(x) for x in (_dict.get('snapshots'))
            ]
        if 'notices' in _dict:
            args['notices'] = [
                Notice._from_dict(x) for x in (_dict.get('notices'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'configuration_id') and self.configuration_id is not None:
            _dict['configuration_id'] = self.configuration_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'enriched_field_units'
                  ) and self.enriched_field_units is not None:
            _dict['enriched_field_units'] = self.enriched_field_units
        if hasattr(
                self,
                'original_media_type') and self.original_media_type is not None:
            _dict['original_media_type'] = self.original_media_type
        if hasattr(self, 'snapshots') and self.snapshots is not None:
            _dict['snapshots'] = [x._to_dict() for x in self.snapshots]
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = [x._to_dict() for x in self.notices]
        return _dict

    def __str__(self):
        """Return a `str` version of this TestDocument object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingDataSet(object):
    """
    TrainingDataSet.

    :attr str environment_id: (optional)
    :attr str collection_id: (optional)
    :attr list[TrainingQuery] queries: (optional)
    """

    def __init__(self, environment_id=None, collection_id=None, queries=None):
        """
        Initialize a TrainingDataSet object.

        :param str environment_id: (optional)
        :param str collection_id: (optional)
        :param list[TrainingQuery] queries: (optional)
        """
        self.environment_id = environment_id
        self.collection_id = collection_id
        self.queries = queries

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingDataSet object from a json dictionary."""
        args = {}
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'queries' in _dict:
            args['queries'] = [
                TrainingQuery._from_dict(x) for x in (_dict.get('queries'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'queries') and self.queries is not None:
            _dict['queries'] = [x._to_dict() for x in self.queries]
        return _dict

    def __str__(self):
        """Return a `str` version of this TrainingDataSet object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingExample(object):
    """
    TrainingExample.

    :attr str document_id: (optional)
    :attr str cross_reference: (optional)
    :attr int relevance: (optional)
    """

    def __init__(self, document_id=None, cross_reference=None, relevance=None):
        """
        Initialize a TrainingExample object.

        :param str document_id: (optional)
        :param str cross_reference: (optional)
        :param int relevance: (optional)
        """
        self.document_id = document_id
        self.cross_reference = cross_reference
        self.relevance = relevance

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingExample object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'cross_reference' in _dict:
            args['cross_reference'] = _dict.get('cross_reference')
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this TrainingExample object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingExampleList(object):
    """
    TrainingExampleList.

    :attr list[TrainingExample] examples: (optional)
    """

    def __init__(self, examples=None):
        """
        Initialize a TrainingExampleList object.

        :param list[TrainingExample] examples: (optional)
        """
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingExampleList object from a json dictionary."""
        args = {}
        if 'examples' in _dict:
            args['examples'] = [
                TrainingExample._from_dict(x) for x in (_dict.get('examples'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        return _dict

    def __str__(self):
        """Return a `str` version of this TrainingExampleList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingQuery(object):
    """
    TrainingQuery.

    :attr str query_id: (optional)
    :attr str natural_language_query: (optional)
    :attr str filter: (optional)
    :attr list[TrainingExample] examples: (optional)
    """

    def __init__(self,
                 query_id=None,
                 natural_language_query=None,
                 filter=None,
                 examples=None):
        """
        Initialize a TrainingQuery object.

        :param str query_id: (optional)
        :param str natural_language_query: (optional)
        :param str filter: (optional)
        :param list[TrainingExample] examples: (optional)
        """
        self.query_id = query_id
        self.natural_language_query = natural_language_query
        self.filter = filter
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingQuery object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this TrainingQuery object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingStatus(object):
    """
    TrainingStatus.

    :attr int total_examples: (optional)
    :attr bool available: (optional)
    :attr bool processing: (optional)
    :attr bool minimum_queries_added: (optional)
    :attr bool minimum_examples_added: (optional)
    :attr bool sufficient_label_diversity: (optional)
    :attr int notices: (optional)
    :attr datetime successfully_trained: (optional)
    :attr datetime data_updated: (optional)
    """

    def __init__(self,
                 total_examples=None,
                 available=None,
                 processing=None,
                 minimum_queries_added=None,
                 minimum_examples_added=None,
                 sufficient_label_diversity=None,
                 notices=None,
                 successfully_trained=None,
                 data_updated=None):
        """
        Initialize a TrainingStatus object.

        :param int total_examples: (optional)
        :param bool available: (optional)
        :param bool processing: (optional)
        :param bool minimum_queries_added: (optional)
        :param bool minimum_examples_added: (optional)
        :param bool sufficient_label_diversity: (optional)
        :param int notices: (optional)
        :param datetime successfully_trained: (optional)
        :param datetime data_updated: (optional)
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
    def _from_dict(cls, _dict):
        """Initialize a TrainingStatus object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this TrainingStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordHeadingDetection(object):
    """
    WordHeadingDetection.

    :attr list[FontSetting] fonts: (optional)
    :attr list[WordStyle] styles: (optional)
    """

    def __init__(self, fonts=None, styles=None):
        """
        Initialize a WordHeadingDetection object.

        :param list[FontSetting] fonts: (optional)
        :param list[WordStyle] styles: (optional)
        """
        self.fonts = fonts
        self.styles = styles

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordHeadingDetection object from a json dictionary."""
        args = {}
        if 'fonts' in _dict:
            args['fonts'] = [
                FontSetting._from_dict(x) for x in (_dict.get('fonts'))
            ]
        if 'styles' in _dict:
            args['styles'] = [
                WordStyle._from_dict(x) for x in (_dict.get('styles'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fonts') and self.fonts is not None:
            _dict['fonts'] = [x._to_dict() for x in self.fonts]
        if hasattr(self, 'styles') and self.styles is not None:
            _dict['styles'] = [x._to_dict() for x in self.styles]
        return _dict

    def __str__(self):
        """Return a `str` version of this WordHeadingDetection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordSettings(object):
    """
    A list of Word conversion settings.

    :attr WordHeadingDetection heading: (optional)
    """

    def __init__(self, heading=None):
        """
        Initialize a WordSettings object.

        :param WordHeadingDetection heading: (optional)
        """
        self.heading = heading

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordSettings object from a json dictionary."""
        args = {}
        if 'heading' in _dict:
            args['heading'] = WordHeadingDetection._from_dict(
                _dict.get('heading'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'heading') and self.heading is not None:
            _dict['heading'] = self.heading._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this WordSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordStyle(object):
    """
    WordStyle.

    :attr int level: (optional)
    :attr list[str] names: (optional)
    """

    def __init__(self, level=None, names=None):
        """
        Initialize a WordStyle object.

        :param int level: (optional)
        :param list[str] names: (optional)
        """
        self.level = level
        self.names = names

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordStyle object from a json dictionary."""
        args = {}
        if 'level' in _dict:
            args['level'] = _dict.get('level')
        if 'names' in _dict:
            args['names'] = _dict.get('names')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self, 'names') and self.names is not None:
            _dict['names'] = self.names
        return _dict

    def __str__(self):
        """Return a `str` version of this WordStyle object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class XPathPatterns(object):
    """
    XPathPatterns.

    :attr list[str] xpaths: (optional)
    """

    def __init__(self, xpaths=None):
        """
        Initialize a XPathPatterns object.

        :param list[str] xpaths: (optional)
        """
        self.xpaths = xpaths

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a XPathPatterns object from a json dictionary."""
        args = {}
        if 'xpaths' in _dict:
            args['xpaths'] = _dict.get('xpaths')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'xpaths') and self.xpaths is not None:
            _dict['xpaths'] = self.xpaths
        return _dict

    def __str__(self):
        """Return a `str` version of this XPathPatterns object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
