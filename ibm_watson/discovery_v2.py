# coding: utf-8

# (C) Copyright IBM Corp. 2019, 2023.
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

# IBM OpenAPI SDK Code Generator Version: 3.64.1-cee95189-20230124-211647
"""
IBM Watson&reg; Discovery is a cognitive search and content analytics engine that you can
add to applications to identify patterns, trends and actionable insights to drive better
decision-making. Securely unify structured and unstructured data with pre-enriched
content, and use a simplified query language to eliminate the need for manual filtering of
results.

API Version: 2.0
See: https://cloud.ibm.com/docs/discovery-data
"""

from datetime import datetime
from enum import Enum
from os.path import basename
from typing import BinaryIO, Dict, List
import json
import sys

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class DiscoveryV2(BaseService):
    """The Discovery V2 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.discovery.watson.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'discovery'

    def __init__(
        self,
        version: str,
        authenticator: Authenticator = None,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Discovery service.

        :param str version: Release date of the version of the API you want to use.
               Specify dates in YYYY-MM-DD format. The current version is `2020-08-30`.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if version is None:
            raise ValueError('version must be provided')

        if not authenticator:
            authenticator = get_authenticator_from_environment(service_name)
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.version = version
        self.configure_service(service_name)

    #########################
    # Projects
    #########################

    def list_projects(self, **kwargs) -> DetailedResponse:
        """
        List projects.

        Lists existing projects for this instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListProjectsResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_projects')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/projects'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_project(self,
                       name: str,
                       type: str,
                       *,
                       default_query_parameters: 'DefaultQueryParams' = None,
                       **kwargs) -> DetailedResponse:
        """
        Create a project.

        Create a new project for this instance.

        :param str name: The human readable name of this project.
        :param str type: The type of project.
               The `content_intelligence` type is a *Document Retrieval for Contracts*
               project and the `other` type is a *Custom* project.
               The `content_mining` and `content_intelligence` types are available with
               Premium plan managed deployments and installed deployments only.
        :param DefaultQueryParams default_query_parameters: (optional) Default
               query parameters for this project.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectDetails` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if default_query_parameters is not None:
            default_query_parameters = convert_model(default_query_parameters)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_project')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'type': type,
            'default_query_parameters': default_query_parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/projects'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_project(self, project_id: str, **kwargs) -> DetailedResponse:
        """
        Get project.

        Get details on the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectDetails` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_project')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_project(self,
                       project_id: str,
                       *,
                       name: str = None,
                       **kwargs) -> DetailedResponse:
        """
        Update a project.

        Update the specified project's name.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str name: (optional) The new name to give this project.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectDetails` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_project')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_project(self, project_id: str, **kwargs) -> DetailedResponse:
        """
        Delete a project.

        Deletes the specified project.
        **Important:** Deleting a project deletes everything that is part of the specified
        project, including all collections.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_project')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def list_fields(self,
                    project_id: str,
                    *,
                    collection_ids: List[str] = None,
                    **kwargs) -> DetailedResponse:
        """
        List fields.

        Gets a list of the unique fields (and their types) stored in the specified
        collections.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param List[str] collection_ids: (optional) Comma separated list of the
               collection IDs. If this parameter is not specified, all collections in the
               project are used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListFieldsResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_fields')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'collection_ids': convert_list(collection_ids),
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/fields'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Collections
    #########################

    def list_collections(self, project_id: str, **kwargs) -> DetailedResponse:
        """
        List collections.

        Lists existing collections for the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCollectionsResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_collections')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_collection(self,
                          project_id: str,
                          name: str,
                          *,
                          description: str = None,
                          language: str = None,
                          enrichments: List['CollectionEnrichment'] = None,
                          **kwargs) -> DetailedResponse:
        """
        Create a collection.

        Create a new collection in the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str name: The name of the collection.
        :param str description: (optional) A description of the collection.
        :param str language: (optional) The language of the collection. For a list
               of supported languages, see the [product
               documentation](/docs/discovery-data?topic=discovery-data-language-support).
        :param List[CollectionEnrichment] enrichments: (optional) An array of
               enrichments that are applied to this collection. To get a list of
               enrichments that are available for a project, use the [List
               enrichments](#listenrichments) method.
               If no enrichments are specified when the collection is created, the default
               enrichments for the project type are applied. For more information about
               project default settings, see the [product
               documentation](/docs/discovery-data?topic=discovery-data-project-defaults).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CollectionDetails` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if enrichments is not None:
            enrichments = [convert_model(x) for x in enrichments]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_collection')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
            'language': language,
            'enrichments': enrichments,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_collection(self, project_id: str, collection_id: str,
                       **kwargs) -> DetailedResponse:
        """
        Get collection.

        Get details about the specified collection.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CollectionDetails` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_collection')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_collection(self,
                          project_id: str,
                          collection_id: str,
                          *,
                          name: str = None,
                          description: str = None,
                          enrichments: List['CollectionEnrichment'] = None,
                          **kwargs) -> DetailedResponse:
        """
        Update a collection.

        Updates the specified collection's name, description, and enrichments.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param str name: (optional) The new name of the collection.
        :param str description: (optional) The new description of the collection.
        :param List[CollectionEnrichment] enrichments: (optional) An array of
               enrichments that are applied to this collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CollectionDetails` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        if enrichments is not None:
            enrichments = [convert_model(x) for x in enrichments]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_collection')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
            'enrichments': enrichments,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_collection(self, project_id: str, collection_id: str,
                          **kwargs) -> DetailedResponse:
        """
        Delete a collection.

        Deletes the specified collection from the project. All documents stored in the
        specified collection and not shared is also deleted.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_collection')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Documents
    #########################

    def list_documents(self,
                       project_id: str,
                       collection_id: str,
                       *,
                       count: int = None,
                       status: str = None,
                       has_notices: bool = None,
                       is_parent: bool = None,
                       parent_document_id: str = None,
                       sha256: str = None,
                       **kwargs) -> DetailedResponse:
        """
        List documents.

        Lists the documents in the specified collection. The list includes only the
        document ID of each document and returns information for up to 10,000 documents.
        **Note**: This method is available only from Cloud Pak for Data version 4.0.9 and
        later installed instances and from Plus and Enterprise plan IBM Cloud-managed
        instances. It is not currently available from Premium plan instances.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param int count: (optional) The maximum number of documents to return. Up
               to 1,000 documents are returned by default. The maximum number allowed is
               10,000.
        :param str status: (optional) Filters the documents to include only
               documents with the specified ingestion status. The options include:
               * `available`: Ingestion is finished and the document is indexed.
               * `failed`: Ingestion is finished, but the document is not indexed because
               of an error.
               * `pending`: The document is uploaded, but the ingestion process is not
               started.
               * `processing`: Ingestion is in progress.
               You can specify one status value or add a comma-separated list of more than
               one status value. For example, `available,failed`.
        :param bool has_notices: (optional) If set to `true`, only documents that
               have notices, meaning documents for which warnings or errors were generated
               during the ingestion, are returned. If set to `false`, only documents that
               don't have notices are returned. If unspecified, no filter based on notices
               is applied.
               Notice details are not available in the result, but you can use the [Query
               collection notices](#querycollectionnotices) method to find details by
               adding the parameter `query=notices.document_id:{document-id}`.
        :param bool is_parent: (optional) If set to `true`, only parent documents,
               meaning documents that were split during the ingestion process and resulted
               in two or more child documents, are returned. If set to `false`, only child
               documents are returned. If unspecified, no filter based on the parent or
               child relationship is applied.
               CSV files, for example, are split into separate documents per line and JSON
               files are split into separate documents per object.
        :param str parent_document_id: (optional) Filters the documents to include
               only child documents that were generated when the specified parent document
               was processed.
        :param str sha256: (optional) Filters the documents to include only
               documents with the specified SHA-256 hash. Format the hash as a hexadecimal
               string.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListDocumentsResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_documents')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'count': count,
            'status': status,
            'has_notices': has_notices,
            'is_parent': is_parent,
            'parent_document_id': parent_document_id,
            'sha256': sha256,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/documents'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def add_document(self,
                     project_id: str,
                     collection_id: str,
                     *,
                     file: BinaryIO = None,
                     filename: str = None,
                     file_content_type: str = None,
                     metadata: str = None,
                     x_watson_discovery_force: bool = None,
                     **kwargs) -> DetailedResponse:
        """
        Add a document.

        Add a document to a collection with optional metadata.
        Returns immediately after the system has accepted the document for processing.
        Use this method to upload a file to the collection. You cannot use this method to
        crawl an external data source.
         * For a list of supported file types, see the [product
        documentation](/docs/discovery-data?topic=discovery-data-collections#supportedfiletypes).
         * You must provide document content, metadata, or both. If the request is missing
        both document content and metadata, it is rejected.
          * You can set the **Content-Type** parameter on the **file** part to indicate
        the media type of the document. If the **Content-Type** parameter is missing or is
        one of the generic media types (for example, `application/octet-stream`), then the
        service attempts to automatically detect the document's media type.
         *  If the document is uploaded to a collection that shares its data with another
        collection, the **X-Watson-Discovery-Force** header must be set to `true`.
         * In curl requests only, you can assign an ID to a document that you add by
        appending the ID to the endpoint
        (`/v2/projects/{project_id}/collections/{collection_id}/documents/{document_id}`).
        If a document already exists with the specified ID, it is replaced.
        For more information about how certain file types and field names are handled when
        a file is added to a collection, see the [product
        documentation](/docs/discovery-data?topic=discovery-data-index-overview#field-name-limits).

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param BinaryIO file: (optional) When adding a document, the content of the
               document to ingest. For maximum supported file size limits, see [the
               documentation](/docs/discovery-data?topic=discovery-data-collections#collections-doc-limits).
               When analyzing a document, the content of the document to analyze but not
               ingest. Only the `application/json` content type is supported currently.
               For maximum supported file size limits, see [the product
               documentation](/docs/discovery-data?topic=discovery-data-analyzeapi#analyzeapi-limits).
        :param str filename: (optional) The filename for file.
        :param str file_content_type: (optional) The content type of file.
        :param str metadata: (optional) Add information about the file that you
               want to include in the response.
               The maximum supported metadata file size is 1 MB. Metadata parts larger
               than 1 MB are rejected.
               Example:
                ```
                {
                 "filename": "favorites2.json",
                 "file_type": "json"
                }.
        :param bool x_watson_discovery_force: (optional) When `true`, the uploaded
               document is added to the collection even if the data for that collection is
               shared with other collections.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentAccepted` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {
            'X-Watson-Discovery-Force': x_watson_discovery_force,
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='add_document')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        if file:
            if not filename and hasattr(file, 'name'):
                filename = basename(file.name)
            if not filename:
                raise ValueError('filename must be provided')
            form_data.append(('file', (filename, file, file_content_type or
                                       'application/octet-stream')))
        if metadata:
            form_data.append(('metadata', (None, metadata, 'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/documents'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    def get_document(self, project_id: str, collection_id: str,
                     document_id: str, **kwargs) -> DetailedResponse:
        """
        Get document details.

        Get details about a specific document, whether the document is added by uploading
        a file or by crawling an external data source.
        **Note**: This method is available only from Cloud Pak for Data version 4.0.9 and
        later installed instances and from Plus and Enterprise plan IBM Cloud-managed
        instances. It is not currently available from Premium plan instances.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentDetails` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_document')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id', 'document_id']
        path_param_values = self.encode_path_vars(project_id, collection_id,
                                                  document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/documents/{document_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_document(self,
                        project_id: str,
                        collection_id: str,
                        document_id: str,
                        *,
                        file: BinaryIO = None,
                        filename: str = None,
                        file_content_type: str = None,
                        metadata: str = None,
                        x_watson_discovery_force: bool = None,
                        **kwargs) -> DetailedResponse:
        """
        Update a document.

        Replace an existing document or add a document with a specified document ID.
        Starts ingesting a document with optional metadata.
        Use this method to upload a file to a collection. You cannot use this method to
        crawl an external data source.
        If the document is uploaded to a collection that shares its data with another
        collection, the **X-Watson-Discovery-Force** header must be set to `true`.
        **Notes:**
         * Uploading a new document with this method automatically replaces any existing
        document stored with the same document ID.
         * If an uploaded document is split into child documents during ingestion, all
        existing child documents are overwritten, even if the updated version of the
        document has fewer child documents.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param BinaryIO file: (optional) When adding a document, the content of the
               document to ingest. For maximum supported file size limits, see [the
               documentation](/docs/discovery-data?topic=discovery-data-collections#collections-doc-limits).
               When analyzing a document, the content of the document to analyze but not
               ingest. Only the `application/json` content type is supported currently.
               For maximum supported file size limits, see [the product
               documentation](/docs/discovery-data?topic=discovery-data-analyzeapi#analyzeapi-limits).
        :param str filename: (optional) The filename for file.
        :param str file_content_type: (optional) The content type of file.
        :param str metadata: (optional) Add information about the file that you
               want to include in the response.
               The maximum supported metadata file size is 1 MB. Metadata parts larger
               than 1 MB are rejected.
               Example:
                ```
                {
                 "filename": "favorites2.json",
                 "file_type": "json"
                }.
        :param bool x_watson_discovery_force: (optional) When `true`, the uploaded
               document is added to the collection even if the data for that collection is
               shared with other collections.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentAccepted` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        headers = {
            'X-Watson-Discovery-Force': x_watson_discovery_force,
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_document')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        if file:
            if not filename and hasattr(file, 'name'):
                filename = basename(file.name)
            if not filename:
                raise ValueError('filename must be provided')
            form_data.append(('file', (filename, file, file_content_type or
                                       'application/octet-stream')))
        if metadata:
            form_data.append(('metadata', (None, metadata, 'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id', 'document_id']
        path_param_values = self.encode_path_vars(project_id, collection_id,
                                                  document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/documents/{document_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    def delete_document(self,
                        project_id: str,
                        collection_id: str,
                        document_id: str,
                        *,
                        x_watson_discovery_force: bool = None,
                        **kwargs) -> DetailedResponse:
        """
        Delete a document.

        Deletes the document with the document ID that you specify from the collection.
        Removes uploaded documents from the collection permanently. If you delete a
        document that was added by crawling an external data source, the document will be
        added again with the next scheduled crawl of the data source. The delete function
        removes the document from the collection, not from the external data source.
        **Note:** Files such as CSV or JSON files generate subdocuments when they are
        added to a collection. If you delete a subdocument, and then repeat the action
        that created it, the deleted document is added back in to your collection. To
        remove subdocuments that are generated by an uploaded file, delete the original
        document instead. You can get the document ID of the original document from the
        `parent_document_id` of the subdocument result.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param bool x_watson_discovery_force: (optional) When `true`, the uploaded
               document is added to the collection even if the data for that collection is
               shared with other collections.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteDocumentResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        if not document_id:
            raise ValueError('document_id must be provided')
        headers = {
            'X-Watson-Discovery-Force': x_watson_discovery_force,
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_document')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id', 'document_id']
        path_param_values = self.encode_path_vars(project_id, collection_id,
                                                  document_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/documents/{document_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Queries
    #########################

    def query(self,
              project_id: str,
              *,
              collection_ids: List[str] = None,
              filter: str = None,
              query: str = None,
              natural_language_query: str = None,
              aggregation: str = None,
              count: int = None,
              return_: List[str] = None,
              offset: int = None,
              sort: str = None,
              highlight: bool = None,
              spelling_suggestions: bool = None,
              table_results: 'QueryLargeTableResults' = None,
              suggested_refinements: 'QueryLargeSuggestedRefinements' = None,
              passages: 'QueryLargePassages' = None,
              similar: 'QueryLargeSimilar' = None,
              **kwargs) -> DetailedResponse:
        """
        Query a project.

        Search your data by submitting queries that are written in natural language or
        formatted in the Discovery Query Language. For more information, see the
        [Discovery
        documentation](/docs/discovery-data?topic=discovery-data-query-concepts). The
        default query parameters differ by project type. For more information about the
        project default settings, see the [Discovery
        documentation](/docs/discovery-data?topic=discovery-data-query-defaults). See [the
        Projects API documentation](#create-project) for details about how to set custom
        default query settings.
        The length of the UTF-8 encoding of the POST body cannot exceed 10,000 bytes,
        which is roughly equivalent to 10,000 characters in English.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param List[str] collection_ids: (optional) A comma-separated list of
               collection IDs to be queried against.
        :param str filter: (optional) Searches for documents that match the
               Discovery Query Language criteria that is specified as input. Filter calls
               are cached and are faster than query calls because the results are not
               ordered by relevance. When used with the **aggregation**, **query**, or
               **natural_language_query** parameters, the **filter** parameter runs first.
               This parameter is useful for limiting results to those that contain
               specific metadata values.
        :param str query: (optional) A query search that is written in the
               Discovery Query Language and returns all matching documents in your data
               set with full enrichments and full text, and with the most relevant
               documents listed first. Use a query search when you want to find the most
               relevant search results.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by using training data and natural language
               understanding.
        :param str aggregation: (optional) An aggregation search that returns an
               exact answer by combining query search with filters. Useful for
               applications to build lists, tables, and time series. For more information
               about the supported types of aggregations, see the [Discovery
               documentation](/docs/discovery-data?topic=discovery-data-query-aggregations).
        :param int count: (optional) Number of results to return.
        :param List[str] return_: (optional) A list of the fields in the document
               hierarchy to return. You can specify both root-level (`text`) and nested
               (`extracted_metadata.filename`) fields. If this parameter is an empty list,
               then all fields are returned.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results.
        :param str sort: (optional) A comma-separated list of fields in the
               document to sort on. You can optionally specify a sort direction by
               prefixing the field with `-` for descending or `+` for ascending. Ascending
               is the default sort direction if no prefix is specified.
        :param bool highlight: (optional) When `true`, a highlight field is
               returned for each result that contains fields that match the query. The
               matching query terms are emphasized with surrounding `<em></em>` tags. This
               parameter is ignored if **passages.enabled** and **passages.per_document**
               are `true`, in which case passages are returned for each document instead
               of highlights.
        :param bool spelling_suggestions: (optional) When `true` and the
               **natural_language_query** parameter is used, the
               **natural_language_query** parameter is spell checked. The most likely
               correction is returned in the **suggested_query** field of the response (if
               one exists).
        :param QueryLargeTableResults table_results: (optional) Configuration for
               table retrieval.
        :param QueryLargeSuggestedRefinements suggested_refinements: (optional)
               Configuration for suggested refinements.
               **Note**: The **suggested_refinements** parameter that identified dynamic
               facets from the data is deprecated.
        :param QueryLargePassages passages: (optional) Configuration for passage
               retrieval.
        :param QueryLargeSimilar similar: (optional) Finds results from documents
               that are similar to documents of interest. Use this parameter to add a
               *More like these* function to your search. You can include this parameter
               with or without a **query**, **filter** or **natural_language_query**
               parameter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QueryResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if table_results is not None:
            table_results = convert_model(table_results)
        if suggested_refinements is not None:
            suggested_refinements = convert_model(suggested_refinements)
        if passages is not None:
            passages = convert_model(passages)
        if similar is not None:
            similar = convert_model(similar)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='query')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'collection_ids': collection_ids,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'aggregation': aggregation,
            'count': count,
            'return': return_,
            'offset': offset,
            'sort': sort,
            'highlight': highlight,
            'spelling_suggestions': spelling_suggestions,
            'table_results': table_results,
            'suggested_refinements': suggested_refinements,
            'passages': passages,
            'similar': similar,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/query'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_autocompletion(self,
                           project_id: str,
                           prefix: str,
                           *,
                           collection_ids: List[str] = None,
                           field: str = None,
                           count: int = None,
                           **kwargs) -> DetailedResponse:
        """
        Get Autocomplete Suggestions.

        Returns completion query suggestions for the specified prefix.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str prefix: The prefix to use for autocompletion. For example, the
               prefix `Ho` could autocomplete to `hot`, `housing`, or `how`.
        :param List[str] collection_ids: (optional) Comma separated list of the
               collection IDs. If this parameter is not specified, all collections in the
               project are used.
        :param str field: (optional) The field in the result documents that
               autocompletion suggestions are identified from.
        :param int count: (optional) The number of autocompletion suggestions to
               return.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Completions` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not prefix:
            raise ValueError('prefix must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_autocompletion')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'prefix': prefix,
            'collection_ids': convert_list(collection_ids),
            'field': field,
            'count': count,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/autocompletion'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def query_collection_notices(self,
                                 project_id: str,
                                 collection_id: str,
                                 *,
                                 filter: str = None,
                                 query: str = None,
                                 natural_language_query: str = None,
                                 count: int = None,
                                 offset: int = None,
                                 **kwargs) -> DetailedResponse:
        """
        Query collection notices.

        Finds collection-level notices (errors and warnings) that are generated when
        documents are ingested.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param str filter: (optional) Searches for documents that match the
               Discovery Query Language criteria that is specified as input. Filter calls
               are cached and are faster than query calls because the results are not
               ordered by relevance. When used with the `aggregation`, `query`, or
               `natural_language_query` parameters, the `filter` parameter runs first.
               This parameter is useful for limiting results to those that contain
               specific metadata values.
        :param str query: (optional) A query search that is written in the
               Discovery Query Language and returns all matching documents in your data
               set with full enrichments and full text, and with the most relevant
               documents listed first.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by using training data and natural language
               understanding.
        :param int count: (optional) Number of results to return. The maximum for
               the **count** and **offset** values together in any one query is
               **10,000**.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QueryNoticesResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='query_collection_notices')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'count': count,
            'offset': offset,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/notices'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def query_notices(self,
                      project_id: str,
                      *,
                      filter: str = None,
                      query: str = None,
                      natural_language_query: str = None,
                      count: int = None,
                      offset: int = None,
                      **kwargs) -> DetailedResponse:
        """
        Query project notices.

        Finds project-level notices (errors and warnings). Currently, project-level
        notices are generated by relevancy training.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str filter: (optional) Searches for documents that match the
               Discovery Query Language criteria that is specified as input. Filter calls
               are cached and are faster than query calls because the results are not
               ordered by relevance. When used with the `aggregation`, `query`, or
               `natural_language_query` parameters, the `filter` parameter runs first.
               This parameter is useful for limiting results to those that contain
               specific metadata values.
        :param str query: (optional) A query search that is written in the
               Discovery Query Language and returns all matching documents in your data
               set with full enrichments and full text, and with the most relevant
               documents listed first.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by using training data and natural language
               understanding.
        :param int count: (optional) Number of results to return. The maximum for
               the **count** and **offset** values together in any one query is
               **10,000**.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QueryNoticesResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='query_notices')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'count': count,
            'offset': offset,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/notices'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Query modifications
    #########################

    def get_stopword_list(self, project_id: str, collection_id: str,
                          **kwargs) -> DetailedResponse:
        """
        Get a custom stop words list.

        Returns the custom stop words list that is used by the collection. For information
        about the default stop words lists that are applied to queries, see [the product
        documentation](/docs/discovery-data?topic=discovery-data-stopwords).

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StopWordList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_stopword_list')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/stopwords'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_stopword_list(self,
                             project_id: str,
                             collection_id: str,
                             *,
                             stopwords: List[str] = None,
                             **kwargs) -> DetailedResponse:
        """
        Create a custom stop words list.

        Adds a list of custom stop words. Stop words are words that you want the service
        to ignore when they occur in a query because they're not useful in distinguishing
        the semantic meaning of the query. The stop words list cannot contain more than 1
        million characters.
        A default stop words list is used by all collections. The default list is applied
        both at indexing time and at query time. A custom stop words list that you add is
        used at query time only.
        The custom stop words list augments the default stop words list; you cannot remove
        stop words. For information about the default stop words lists per language, see
        [the product documentation](/docs/discovery-data?topic=discovery-data-stopwords).

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param List[str] stopwords: (optional) List of stop words.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StopWordList` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_stopword_list')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'stopwords': stopwords,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/stopwords'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_stopword_list(self, project_id: str, collection_id: str,
                             **kwargs) -> DetailedResponse:
        """
        Delete a custom stop words list.

        Deletes a custom stop words list to stop using it in queries against the
        collection. After a custom stop words list is deleted, the default stop words list
        is used.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_stopword_list')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/stopwords'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def list_expansions(self, project_id: str, collection_id: str,
                        **kwargs) -> DetailedResponse:
        """
        Get the expansion list.

        Returns the current expansion list for the specified collection. If an expansion
        list is not specified, an empty expansions array is returned.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Expansions` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_expansions')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/expansions'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_expansions(self, project_id: str, collection_id: str,
                          expansions: List['Expansion'],
                          **kwargs) -> DetailedResponse:
        """
        Create or update an expansion list.

        Creates or replaces the expansion list for this collection. An expansion list
        introduces alternative wording for key terms that are mentioned in your
        collection. By identifying synonyms or common misspellings, you expand the scope
        of a query beyond exact matches. The maximum number of expanded terms allowed per
        collection is 5,000.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param List[Expansion] expansions: An array of query expansion definitions.
                Each object in the **expansions** array represents a term or set of terms
               that will be expanded into other terms. Each expansion object can be
               configured as `bidirectional` or `unidirectional`.
               * **Bidirectional**: Each entry in the `expanded_terms` list expands to
               include all expanded terms. For example, a query for `ibm` expands to `ibm
               OR international business machines OR big blue`.
               * **Unidirectional**: The terms in `input_terms` in the query are replaced
               by the terms in `expanded_terms`. For example, a query for the often
               misused term `on premise` is converted to `on premises OR on-premises` and
               does not contain the original term. If you want an input term to be
               included in the query, then repeat the input term in the expanded terms
               list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Expansions` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        if expansions is None:
            raise ValueError('expansions must be provided')
        expansions = [convert_model(x) for x in expansions]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_expansions')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'expansions': expansions,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/expansions'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_expansions(self, project_id: str, collection_id: str,
                          **kwargs) -> DetailedResponse:
        """
        Delete the expansion list.

        Removes the expansion information for this collection. To disable query expansion
        for a collection, delete the expansion list.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_expansions')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/expansions'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Component settings
    #########################

    def get_component_settings(self, project_id: str,
                               **kwargs) -> DetailedResponse:
        """
        List component settings.

        Returns default configuration settings for components.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ComponentSettingsResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_component_settings')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/component_settings'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Training data
    #########################

    def list_training_queries(self, project_id: str,
                              **kwargs) -> DetailedResponse:
        """
        List training queries.

        List the training queries for the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrainingQuerySet` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_training_queries')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/training_data/queries'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def delete_training_queries(self, project_id: str,
                                **kwargs) -> DetailedResponse:
        """
        Delete training queries.

        Removes all training queries for the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_training_queries')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/training_data/queries'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_training_query(self,
                              project_id: str,
                              natural_language_query: str,
                              examples: List['TrainingExample'],
                              *,
                              filter: str = None,
                              **kwargs) -> DetailedResponse:
        """
        Create training query.

        Add a query to the training data for this project. The query can contain a filter
        and natural language query.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str natural_language_query: The natural text query that is used as
               the training query.
        :param List[TrainingExample] examples: Array of training examples.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrainingQuery` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if natural_language_query is None:
            raise ValueError('natural_language_query must be provided')
        if examples is None:
            raise ValueError('examples must be provided')
        examples = [convert_model(x) for x in examples]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_training_query')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'natural_language_query': natural_language_query,
            'examples': examples,
            'filter': filter,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/training_data/queries'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_training_query(self, project_id: str, query_id: str,
                           **kwargs) -> DetailedResponse:
        """
        Get a training data query.

        Get details for a specific training data query, including the query string and all
        examples.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrainingQuery` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not query_id:
            raise ValueError('query_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_training_query')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'query_id']
        path_param_values = self.encode_path_vars(project_id, query_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/training_data/queries/{query_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_training_query(self,
                              project_id: str,
                              query_id: str,
                              natural_language_query: str,
                              examples: List['TrainingExample'],
                              *,
                              filter: str = None,
                              **kwargs) -> DetailedResponse:
        """
        Update a training query.

        Updates an existing training query and it's examples.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str query_id: The ID of the query used for training.
        :param str natural_language_query: The natural text query that is used as
               the training query.
        :param List[TrainingExample] examples: Array of training examples.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrainingQuery` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not query_id:
            raise ValueError('query_id must be provided')
        if natural_language_query is None:
            raise ValueError('natural_language_query must be provided')
        if examples is None:
            raise ValueError('examples must be provided')
        examples = [convert_model(x) for x in examples]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_training_query')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'natural_language_query': natural_language_query,
            'examples': examples,
            'filter': filter,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'query_id']
        path_param_values = self.encode_path_vars(project_id, query_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/training_data/queries/{query_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_training_query(self, project_id: str, query_id: str,
                              **kwargs) -> DetailedResponse:
        """
        Delete a training data query.

        Removes details from a training data query, including the query string and all
        examples.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not query_id:
            raise ValueError('query_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_training_query')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'query_id']
        path_param_values = self.encode_path_vars(project_id, query_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/training_data/queries/{query_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Enrichments
    #########################

    def list_enrichments(self, project_id: str, **kwargs) -> DetailedResponse:
        """
        List enrichments.

        Lists the enrichments available to this project. The *Part of Speech* and
        *Sentiment of Phrases* enrichments might be listed, but are reserved for internal
        use only.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Enrichments` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_enrichments')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/enrichments'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_enrichment(self,
                          project_id: str,
                          enrichment: 'CreateEnrichment',
                          *,
                          file: BinaryIO = None,
                          **kwargs) -> DetailedResponse:
        """
        Create an enrichment.

        Create an enrichment for use with the specified project. To apply the enrichment
        to a collection in the project, use the [Collections
        API](/apidocs/discovery-data#createcollection).

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param CreateEnrichment enrichment: Information about a specific
               enrichment.
        :param BinaryIO file: (optional) The enrichment file to upload. Expected
               file types per enrichment are as follows:
               * CSV for `dictionary`
               * PEAR for `uima_annotator` and `rule_based` (Explorer)
               * ZIP for `watson_knowledge_studio_model` and `rule_based` (Studio Advanced
               Rule Editor).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Enrichment` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if enrichment is None:
            raise ValueError('enrichment must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_enrichment')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        form_data.append(
            ('enrichment', (None, json.dumps(enrichment), 'application/json')))
        if file:
            form_data.append(('file', (None, file, 'application/octet-stream')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/enrichments'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    def get_enrichment(self, project_id: str, enrichment_id: str,
                       **kwargs) -> DetailedResponse:
        """
        Get enrichment.

        Get details about a specific enrichment.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str enrichment_id: The ID of the enrichment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Enrichment` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not enrichment_id:
            raise ValueError('enrichment_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_enrichment')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'enrichment_id']
        path_param_values = self.encode_path_vars(project_id, enrichment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/enrichments/{enrichment_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_enrichment(self,
                          project_id: str,
                          enrichment_id: str,
                          name: str,
                          *,
                          description: str = None,
                          **kwargs) -> DetailedResponse:
        """
        Update an enrichment.

        Updates an existing enrichment's name and description.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str enrichment_id: The ID of the enrichment.
        :param str name: A new name for the enrichment.
        :param str description: (optional) A new description for the enrichment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Enrichment` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not enrichment_id:
            raise ValueError('enrichment_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_enrichment')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'enrichment_id']
        path_param_values = self.encode_path_vars(project_id, enrichment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/enrichments/{enrichment_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_enrichment(self, project_id: str, enrichment_id: str,
                          **kwargs) -> DetailedResponse:
        """
        Delete an enrichment.

        Deletes an existing enrichment from the specified project.
        **Note:** Only enrichments that have been manually created can be deleted.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str enrichment_id: The ID of the enrichment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not enrichment_id:
            raise ValueError('enrichment_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_enrichment')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'enrichment_id']
        path_param_values = self.encode_path_vars(project_id, enrichment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/enrichments/{enrichment_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Document classifiers
    #########################

    def list_document_classifiers(self, project_id: str,
                                  **kwargs) -> DetailedResponse:
        """
        List document classifiers.

        Get a list of the document classifiers in a project. Returns only the name and
        classifier ID of each document classifier.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifiers` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_document_classifiers')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_document_classifier(self,
                                   project_id: str,
                                   training_data: BinaryIO,
                                   classifier: 'CreateDocumentClassifier',
                                   *,
                                   test_data: BinaryIO = None,
                                   **kwargs) -> DetailedResponse:
        """
        Create a document classifier.

        Create a document classifier. You can use the API to create a document classifier
        in any project type. After you create a document classifier, you can use the
        Enrichments API to create a classifier enrichment, and then the Collections API to
        apply the enrichment to a collection in the project.
        **Note:** This method is supported on installed instances (IBM Cloud Pak for Data)
        or IBM Cloud-managed Premium or Enterprise plan instances.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param BinaryIO training_data: The training data CSV file to upload. The
               CSV file must have headers. The file must include a field that contains the
               text you want to classify and a field that contains the classification
               labels that you want to use to classify your data. If you want to specify
               multiple values in a single field, use a semicolon as the value separator.
               For a sample file, see [the product
               documentation](/docs/discovery-data?topic=discovery-data-cm-doc-classifier).
        :param CreateDocumentClassifier classifier: An object that manages the
               settings and data that is required to train a document classification
               model.
        :param BinaryIO test_data: (optional) The CSV with test data to upload. The
               column values in the test file must be the same as the column values in the
               training data file. If no test data is provided, the training data is split
               into two separate groups of training and test data.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifier` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')
        if classifier is None:
            raise ValueError('classifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_document_classifier')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        form_data.append(('training_data', (None, training_data, 'text/csv')))
        form_data.append(
            ('classifier', (None, json.dumps(classifier), 'application/json')))
        if test_data:
            form_data.append(('test_data', (None, test_data, 'text/csv')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    def get_document_classifier(self, project_id: str, classifier_id: str,
                                **kwargs) -> DetailedResponse:
        """
        Get a document classifier.

        Get details about a specific document classifier.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifier` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_document_classifier')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'classifier_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_document_classifier(self,
                                   project_id: str,
                                   classifier_id: str,
                                   classifier: 'UpdateDocumentClassifier',
                                   *,
                                   training_data: BinaryIO = None,
                                   test_data: BinaryIO = None,
                                   **kwargs) -> DetailedResponse:
        """
        Update a document classifier.

        Update the document classifier name or description, update the training data, or
        add or update the test data.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param UpdateDocumentClassifier classifier: An object that contains a new
               name or description for a document classifier, updated training data, or
               new or updated test data.
        :param BinaryIO training_data: (optional) The training data CSV file to
               upload. The CSV file must have headers. The file must include a field that
               contains the text you want to classify and a field that contains the
               classification labels that you want to use to classify your data. If you
               want to specify multiple values in a single column, use a semicolon as the
               value separator. For a sample file, see [the product
               documentation](/docs/discovery-data?topic=discovery-data-cm-doc-classifier).
        :param BinaryIO test_data: (optional) The CSV with test data to upload. The
               column values in the test file must be the same as the column values in the
               training data file. If no test data is provided, the training data is split
               into two separate groups of training and test data.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifier` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        if classifier is None:
            raise ValueError('classifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_document_classifier')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        form_data.append(
            ('classifier', (None, json.dumps(classifier), 'application/json')))
        if training_data:
            form_data.append(
                ('training_data', (None, training_data, 'text/csv')))
        if test_data:
            form_data.append(('test_data', (None, test_data, 'text/csv')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'classifier_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    def delete_document_classifier(self, project_id: str, classifier_id: str,
                                   **kwargs) -> DetailedResponse:
        """
        Delete a document classifier.

        Deletes an existing document classifier from the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_document_classifier')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'classifier_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Document classifier models
    #########################

    def list_document_classifier_models(self, project_id: str,
                                        classifier_id: str,
                                        **kwargs) -> DetailedResponse:
        """
        List document classifier models.

        Get a list of the document classifier models in a project. Returns only the name
        and model ID of each document classifier model.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifierModels` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_document_classifier_models')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'classifier_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}/models'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def create_document_classifier_model(
            self,
            project_id: str,
            classifier_id: str,
            name: str,
            *,
            description: str = None,
            learning_rate: float = None,
            l1_regularization_strengths: List[float] = None,
            l2_regularization_strengths: List[float] = None,
            training_max_steps: int = None,
            improvement_ratio: float = None,
            **kwargs) -> DetailedResponse:
        """
        Create a document classifier model.

        Create a document classifier model by training a model that uses the data and
        classifier settings defined in the specified document classifier.
        **Note:** This method is supported on installed intances (IBM Cloud Pak for Data)
        or IBM Cloud-managed Premium or Enterprise plan instances.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param str name: The name of the document classifier model.
        :param str description: (optional) A description of the document classifier
               model.
        :param float learning_rate: (optional) A tuning parameter in an
               optimization algorithm that determines the step size at each iteration of
               the training process. It influences how much of any newly acquired
               information overrides the existing information, and therefore is said to
               represent the speed at which a machine learning model learns. The default
               value is `0.1`.
        :param List[float] l1_regularization_strengths: (optional) Avoids
               overfitting by shrinking the coefficient of less important features to
               zero, which removes some features altogether. You can specify many values
               for hyper-parameter optimization. The default value is `[0.000001]`.
        :param List[float] l2_regularization_strengths: (optional) A method you can
               apply to avoid overfitting your model on the training data. You can specify
               many values for hyper-parameter optimization. The default value is
               `[0.000001]`.
        :param int training_max_steps: (optional) Maximum number of training steps
               to complete. This setting is useful if you need the training process to
               finish in a specific time frame to fit into an automated process. The
               default value is ten million.
        :param float improvement_ratio: (optional) Stops the training run early if
               the improvement ratio is not met by the time the process reaches a certain
               point. The default value is `0.00001`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifierModel` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_document_classifier_model')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
            'learning_rate': learning_rate,
            'l1_regularization_strengths': l1_regularization_strengths,
            'l2_regularization_strengths': l2_regularization_strengths,
            'training_max_steps': training_max_steps,
            'improvement_ratio': improvement_ratio,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'classifier_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}/models'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_document_classifier_model(self, project_id: str, classifier_id: str,
                                      model_id: str,
                                      **kwargs) -> DetailedResponse:
        """
        Get a document classifier model.

        Get details about a specific document classifier model.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param str model_id: The ID of the classifier model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifierModel` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_document_classifier_model')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'classifier_id', 'model_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id,
                                                  model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}/models/{model_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_document_classifier_model(self,
                                         project_id: str,
                                         classifier_id: str,
                                         model_id: str,
                                         *,
                                         name: str = None,
                                         description: str = None,
                                         **kwargs) -> DetailedResponse:
        """
        Update a document classifier model.

        Update the document classifier model name or description.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param str model_id: The ID of the classifier model.
        :param str name: (optional) A new name for the enrichment.
        :param str description: (optional) A new description for the enrichment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DocumentClassifierModel` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_document_classifier_model')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'classifier_id', 'model_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id,
                                                  model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}/models/{model_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_document_classifier_model(self, project_id: str,
                                         classifier_id: str, model_id: str,
                                         **kwargs) -> DetailedResponse:
        """
        Delete a document classifier model.

        Deletes an existing document classifier model from the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str classifier_id: The ID of the classifier.
        :param str model_id: The ID of the classifier model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not classifier_id:
            raise ValueError('classifier_id must be provided')
        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_document_classifier_model')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'classifier_id', 'model_id']
        path_param_values = self.encode_path_vars(project_id, classifier_id,
                                                  model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/document_classifiers/{classifier_id}/models/{model_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Analyze
    #########################

    def analyze_document(self,
                         project_id: str,
                         collection_id: str,
                         *,
                         file: BinaryIO = None,
                         filename: str = None,
                         file_content_type: str = None,
                         metadata: str = None,
                         **kwargs) -> DetailedResponse:
        """
        Analyze a Document.

        Process a document and return it for realtime use. Supports JSON files only.
        The file is not stored in the collection, but is processed according to the
        collection's configuration settings. To get results, enrichments must be applied
        to a field in the collection that also exists in the file that you want to
        analyze. For example, to analyze text in a `Quote` field, you must apply
        enrichments to the `Quote` field in the collection configuration. Then, when you
        analyze the file, the text in the `Quote` field is analyzed and results are
        written to a field named `enriched_Quote`.
        **Note:** This method is supported with Enterprise plan deployments and installed
        deployments only.

        :param str project_id: The ID of the project. This information can be found
               from the *Integrate and Deploy* page in Discovery.
        :param str collection_id: The ID of the collection.
        :param BinaryIO file: (optional) When adding a document, the content of the
               document to ingest. For maximum supported file size limits, see [the
               documentation](/docs/discovery-data?topic=discovery-data-collections#collections-doc-limits).
               When analyzing a document, the content of the document to analyze but not
               ingest. Only the `application/json` content type is supported currently.
               For maximum supported file size limits, see [the product
               documentation](/docs/discovery-data?topic=discovery-data-analyzeapi#analyzeapi-limits).
        :param str filename: (optional) The filename for file.
        :param str file_content_type: (optional) The content type of file.
        :param str metadata: (optional) Add information about the file that you
               want to include in the response.
               The maximum supported metadata file size is 1 MB. Metadata parts larger
               than 1 MB are rejected.
               Example:
                ```
                {
                 "filename": "favorites2.json",
                 "file_type": "json"
                }.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyzedDocument` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not collection_id:
            raise ValueError('collection_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='analyze_document')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        if file:
            if not filename and hasattr(file, 'name'):
                filename = basename(file.name)
            if not filename:
                raise ValueError('filename must be provided')
            form_data.append(('file', (filename, file, file_content_type or
                                       'application/octet-stream')))
        if metadata:
            form_data.append(('metadata', (None, metadata, 'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'collection_id']
        path_param_values = self.encode_path_vars(project_id, collection_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/projects/{project_id}/collections/{collection_id}/analyze'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(self, customer_id: str, **kwargs) -> DetailedResponse:
        """
        Delete labeled data.

        Deletes all data associated with a specified customer ID. The method has no effect
        if no data is associated with the customer ID.
        You associate a customer ID with data by passing the **X-Watson-Metadata** header
        with a request that passes data. For more information about personal data and
        customer IDs, see [Information
        security](/docs/discovery-data?topic=discovery-data-information-security#information-security).
        **Note:** This method is only supported on IBM Cloud instances of Discovery.

        :param str customer_id: The customer ID for which all data is to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customer_id:
            raise ValueError('customer_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_user_data')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'customer_id': customer_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/v2/user_data'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


class AddDocumentEnums:
    """
    Enums for add_document parameters.
    """

    class FileContentType(str, Enum):
        """
        The content type of file.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        APPLICATION_PDF = 'application/pdf'
        TEXT_HTML = 'text/html'
        APPLICATION_XHTML_XML = 'application/xhtml+xml'


class UpdateDocumentEnums:
    """
    Enums for update_document parameters.
    """

    class FileContentType(str, Enum):
        """
        The content type of file.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        APPLICATION_PDF = 'application/pdf'
        TEXT_HTML = 'text/html'
        APPLICATION_XHTML_XML = 'application/xhtml+xml'


class AnalyzeDocumentEnums:
    """
    Enums for analyze_document parameters.
    """

    class FileContentType(str, Enum):
        """
        The content type of file.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        APPLICATION_PDF = 'application/pdf'
        TEXT_HTML = 'text/html'
        APPLICATION_XHTML_XML = 'application/xhtml+xml'


##############################################################################
# Models
##############################################################################


class AnalyzedDocument():
    """
    An object that contains the converted document and any identified enrichments.
    Root-level fields from the original file are returned also.

    :attr List[Notice] notices: (optional) Array of notices that are triggered when
          the files are processed.
    :attr AnalyzedResult result: (optional) Result of the document analysis.
    """

    def __init__(self,
                 *,
                 notices: List['Notice'] = None,
                 result: 'AnalyzedResult' = None) -> None:
        """
        Initialize a AnalyzedDocument object.

        :param List[Notice] notices: (optional) Array of notices that are triggered
               when the files are processed.
        :param AnalyzedResult result: (optional) Result of the document analysis.
        """
        self.notices = notices
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyzedDocument':
        """Initialize a AnalyzedDocument object from a json dictionary."""
        args = {}
        if 'notices' in _dict:
            args['notices'] = [
                Notice.from_dict(v) for v in _dict.get('notices')
            ]
        if 'result' in _dict:
            args['result'] = AnalyzedResult.from_dict(_dict.get('result'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyzedDocument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'notices') and self.notices is not None:
            notices_list = []
            for v in self.notices:
                if isinstance(v, dict):
                    notices_list.append(v)
                else:
                    notices_list.append(v.to_dict())
            _dict['notices'] = notices_list
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyzedDocument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyzedDocument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyzedDocument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyzedResult():
    """
    Result of the document analysis.

    :attr dict metadata: (optional) Metadata that was specified with the request.
    """

    # The set of defined properties for the class
    _properties = frozenset(['metadata'])

    def __init__(self, *, metadata: dict = None, **kwargs) -> None:
        """
        Initialize a AnalyzedResult object.

        :param dict metadata: (optional) Metadata that was specified with the
               request.
        :param **kwargs: (optional) Any additional properties.
        """
        self.metadata = metadata
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyzedResult':
        """Initialize a AnalyzedResult object from a json dictionary."""
        args = {}
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        args.update(
            {k: v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyzedResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        for _key in [
                k for k in vars(self).keys()
                if k not in AnalyzedResult._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of AnalyzedResult"""
        _dict = {}

        for _key in [
                k for k in vars(self).keys()
                if k not in AnalyzedResult._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of AnalyzedResult"""
        for _key in [
                k for k in vars(self).keys()
                if k not in AnalyzedResult._properties
        ]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in AnalyzedResult._properties:
                setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this AnalyzedResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyzedResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyzedResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifierFederatedModel():
    """
    An object with details for creating federated document classifier models.

    :attr str field: Name of the field that contains the values from which multiple
          classifier models are defined. For example, you can specify a field that lists
          product lines to create a separate model per product line.
    """

    def __init__(self, field: str) -> None:
        """
        Initialize a ClassifierFederatedModel object.

        :param str field: Name of the field that contains the values from which
               multiple classifier models are defined. For example, you can specify a
               field that lists product lines to create a separate model per product line.
        """
        self.field = field

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifierFederatedModel':
        """Initialize a ClassifierFederatedModel object from a json dictionary."""
        args = {}
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in ClassifierFederatedModel JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifierFederatedModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifierFederatedModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassifierFederatedModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifierFederatedModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifierModelEvaluation():
    """
    An object that contains information about a trained document classifier model.

    :attr ModelEvaluationMicroAverage micro_average: A micro-average aggregates the
          contributions of all classes to compute the average metric. Classes refers to
          the classification labels that are specified in the **answer_field**.
    :attr ModelEvaluationMacroAverage macro_average: A macro-average computes metric
          independently for each class and then takes the average. Class refers to the
          classification label that is specified in the **answer_field**.
    :attr List[PerClassModelEvaluation] per_class: An array of evaluation metrics,
          one set of metrics for each class, where class refers to the classification
          label that is specified in the **answer_field**.
    """

    def __init__(self, micro_average: 'ModelEvaluationMicroAverage',
                 macro_average: 'ModelEvaluationMacroAverage',
                 per_class: List['PerClassModelEvaluation']) -> None:
        """
        Initialize a ClassifierModelEvaluation object.

        :param ModelEvaluationMicroAverage micro_average: A micro-average
               aggregates the contributions of all classes to compute the average metric.
               Classes refers to the classification labels that are specified in the
               **answer_field**.
        :param ModelEvaluationMacroAverage macro_average: A macro-average computes
               metric independently for each class and then takes the average. Class
               refers to the classification label that is specified in the
               **answer_field**.
        :param List[PerClassModelEvaluation] per_class: An array of evaluation
               metrics, one set of metrics for each class, where class refers to the
               classification label that is specified in the **answer_field**.
        """
        self.micro_average = micro_average
        self.macro_average = macro_average
        self.per_class = per_class

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifierModelEvaluation':
        """Initialize a ClassifierModelEvaluation object from a json dictionary."""
        args = {}
        if 'micro_average' in _dict:
            args['micro_average'] = ModelEvaluationMicroAverage.from_dict(
                _dict.get('micro_average'))
        else:
            raise ValueError(
                'Required property \'micro_average\' not present in ClassifierModelEvaluation JSON'
            )
        if 'macro_average' in _dict:
            args['macro_average'] = ModelEvaluationMacroAverage.from_dict(
                _dict.get('macro_average'))
        else:
            raise ValueError(
                'Required property \'macro_average\' not present in ClassifierModelEvaluation JSON'
            )
        if 'per_class' in _dict:
            args['per_class'] = [
                PerClassModelEvaluation.from_dict(v)
                for v in _dict.get('per_class')
            ]
        else:
            raise ValueError(
                'Required property \'per_class\' not present in ClassifierModelEvaluation JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifierModelEvaluation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'micro_average') and self.micro_average is not None:
            if isinstance(self.micro_average, dict):
                _dict['micro_average'] = self.micro_average
            else:
                _dict['micro_average'] = self.micro_average.to_dict()
        if hasattr(self, 'macro_average') and self.macro_average is not None:
            if isinstance(self.macro_average, dict):
                _dict['macro_average'] = self.macro_average
            else:
                _dict['macro_average'] = self.macro_average.to_dict()
        if hasattr(self, 'per_class') and self.per_class is not None:
            per_class_list = []
            for v in self.per_class:
                if isinstance(v, dict):
                    per_class_list.append(v)
                else:
                    per_class_list.append(v.to_dict())
            _dict['per_class'] = per_class_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifierModelEvaluation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassifierModelEvaluation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifierModelEvaluation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Collection():
    """
    A collection for storing documents.

    :attr str collection_id: (optional) The unique identifier of the collection.
    :attr str name: (optional) The name of the collection.
    """

    def __init__(self, *, collection_id: str = None, name: str = None) -> None:
        """
        Initialize a Collection object.

        :param str name: (optional) The name of the collection.
        """
        self.collection_id = collection_id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Collection':
        """Initialize a Collection object from a json dictionary."""
        args = {}
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Collection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and getattr(
                self, 'collection_id') is not None:
            _dict['collection_id'] = getattr(self, 'collection_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Collection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Collection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Collection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionDetails():
    """
    A collection for storing documents.

    :attr str collection_id: (optional) The unique identifier of the collection.
    :attr str name: The name of the collection.
    :attr str description: (optional) A description of the collection.
    :attr datetime created: (optional) The date that the collection was created.
    :attr str language: (optional) The language of the collection. For a list of
          supported languages, see the [product
          documentation](/docs/discovery-data?topic=discovery-data-language-support).
    :attr List[CollectionEnrichment] enrichments: (optional) An array of enrichments
          that are applied to this collection. To get a list of enrichments that are
          available for a project, use the [List enrichments](#listenrichments) method.
          If no enrichments are specified when the collection is created, the default
          enrichments for the project type are applied. For more information about project
          default settings, see the [product
          documentation](/docs/discovery-data?topic=discovery-data-project-defaults).
    :attr CollectionDetailsSmartDocumentUnderstanding smart_document_understanding:
          (optional) An object that describes the Smart Document Understanding model for a
          collection.
    """

    def __init__(
        self,
        name: str,
        *,
        collection_id: str = None,
        description: str = None,
        created: datetime = None,
        language: str = None,
        enrichments: List['CollectionEnrichment'] = None,
        smart_document_understanding:
        'CollectionDetailsSmartDocumentUnderstanding' = None
    ) -> None:
        """
        Initialize a CollectionDetails object.

        :param str name: The name of the collection.
        :param str description: (optional) A description of the collection.
        :param str language: (optional) The language of the collection. For a list
               of supported languages, see the [product
               documentation](/docs/discovery-data?topic=discovery-data-language-support).
        :param List[CollectionEnrichment] enrichments: (optional) An array of
               enrichments that are applied to this collection. To get a list of
               enrichments that are available for a project, use the [List
               enrichments](#listenrichments) method.
               If no enrichments are specified when the collection is created, the default
               enrichments for the project type are applied. For more information about
               project default settings, see the [product
               documentation](/docs/discovery-data?topic=discovery-data-project-defaults).
        """
        self.collection_id = collection_id
        self.name = name
        self.description = description
        self.created = created
        self.language = language
        self.enrichments = enrichments
        self.smart_document_understanding = smart_document_understanding

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionDetails':
        """Initialize a CollectionDetails object from a json dictionary."""
        args = {}
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in CollectionDetails JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'enrichments' in _dict:
            args['enrichments'] = [
                CollectionEnrichment.from_dict(v)
                for v in _dict.get('enrichments')
            ]
        if 'smart_document_understanding' in _dict:
            args[
                'smart_document_understanding'] = CollectionDetailsSmartDocumentUnderstanding.from_dict(
                    _dict.get('smart_document_understanding'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and getattr(
                self, 'collection_id') is not None:
            _dict['collection_id'] = getattr(self, 'collection_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'enrichments') and self.enrichments is not None:
            enrichments_list = []
            for v in self.enrichments:
                if isinstance(v, dict):
                    enrichments_list.append(v)
                else:
                    enrichments_list.append(v.to_dict())
            _dict['enrichments'] = enrichments_list
        if hasattr(self, 'smart_document_understanding') and getattr(
                self, 'smart_document_understanding') is not None:
            if isinstance(getattr(self, 'smart_document_understanding'), dict):
                _dict['smart_document_understanding'] = getattr(
                    self, 'smart_document_understanding')
            else:
                _dict['smart_document_understanding'] = getattr(
                    self, 'smart_document_understanding').to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CollectionDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionDetailsSmartDocumentUnderstanding():
    """
    An object that describes the Smart Document Understanding model for a collection.

    :attr bool enabled: (optional) When `true`, smart document understanding
          conversion is enabled for the collection.
    :attr str model: (optional) Specifies the type of Smart Document Understanding
          (SDU) model that is enabled for the collection. The following types of models
          are supported:
           * `custom`: A user-trained model is applied.
           * `pre_trained`: A pretrained model is applied. This type of model is applied
          automatically to *Document Retrieval for Contracts* projects.
           * `text_extraction`: An SDU model that extracts text and metadata from the
          content. This model is enabled in collections by default regardless of the types
          of documents in the collection (as long as the service plan supports SDU
          models).
          You can apply user-trained or pretrained models to collections from the
          *Identify fields* page of the product user interface. For more information, see
          [the product
          documentation](/docs/discovery-data?topic=discovery-data-configuring-fields).
    """

    def __init__(self, *, enabled: bool = None, model: str = None) -> None:
        """
        Initialize a CollectionDetailsSmartDocumentUnderstanding object.

        :param bool enabled: (optional) When `true`, smart document understanding
               conversion is enabled for the collection.
        :param str model: (optional) Specifies the type of Smart Document
               Understanding (SDU) model that is enabled for the collection. The following
               types of models are supported:
                * `custom`: A user-trained model is applied.
                * `pre_trained`: A pretrained model is applied. This type of model is
               applied automatically to *Document Retrieval for Contracts* projects.
                * `text_extraction`: An SDU model that extracts text and metadata from the
               content. This model is enabled in collections by default regardless of the
               types of documents in the collection (as long as the service plan supports
               SDU models).
               You can apply user-trained or pretrained models to collections from the
               *Identify fields* page of the product user interface. For more information,
               see [the product
               documentation](/docs/discovery-data?topic=discovery-data-configuring-fields).
        """
        self.enabled = enabled
        self.model = model

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'CollectionDetailsSmartDocumentUnderstanding':
        """Initialize a CollectionDetailsSmartDocumentUnderstanding object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionDetailsSmartDocumentUnderstanding object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionDetailsSmartDocumentUnderstanding object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'CollectionDetailsSmartDocumentUnderstanding') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'CollectionDetailsSmartDocumentUnderstanding') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModelEnum(str, Enum):
        """
        Specifies the type of Smart Document Understanding (SDU) model that is enabled for
        the collection. The following types of models are supported:
         * `custom`: A user-trained model is applied.
         * `pre_trained`: A pretrained model is applied. This type of model is applied
        automatically to *Document Retrieval for Contracts* projects.
         * `text_extraction`: An SDU model that extracts text and metadata from the
        content. This model is enabled in collections by default regardless of the types
        of documents in the collection (as long as the service plan supports SDU models).
        You can apply user-trained or pretrained models to collections from the *Identify
        fields* page of the product user interface. For more information, see [the product
        documentation](/docs/discovery-data?topic=discovery-data-configuring-fields).
        """
        CUSTOM = 'custom'
        PRE_TRAINED = 'pre_trained'
        TEXT_EXTRACTION = 'text_extraction'


class CollectionEnrichment():
    """
    An object describing an enrichment for a collection.

    :attr str enrichment_id: (optional) The unique identifier of this enrichment.
          For more information about how to determine the ID of an enrichment, see [the
          product
          documentation](/docs/discovery-data?topic=discovery-data-manage-enrichments#enrichments-ids).
    :attr List[str] fields: (optional) An array of field names that the enrichment
          is applied to.
          If you apply an enrichment to a field from a JSON file, the data is converted to
          an array automatically, even if the field contains a single value.
    """

    def __init__(self,
                 *,
                 enrichment_id: str = None,
                 fields: List[str] = None) -> None:
        """
        Initialize a CollectionEnrichment object.

        :param str enrichment_id: (optional) The unique identifier of this
               enrichment. For more information about how to determine the ID of an
               enrichment, see [the product
               documentation](/docs/discovery-data?topic=discovery-data-manage-enrichments#enrichments-ids).
        :param List[str] fields: (optional) An array of field names that the
               enrichment is applied to.
               If you apply an enrichment to a field from a JSON file, the data is
               converted to an array automatically, even if the field contains a single
               value.
        """
        self.enrichment_id = enrichment_id
        self.fields = fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionEnrichment':
        """Initialize a CollectionEnrichment object from a json dictionary."""
        args = {}
        if 'enrichment_id' in _dict:
            args['enrichment_id'] = _dict.get('enrichment_id')
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionEnrichment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enrichment_id') and self.enrichment_id is not None:
            _dict['enrichment_id'] = self.enrichment_id
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionEnrichment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CollectionEnrichment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionEnrichment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Completions():
    """
    An object that contains an array of autocompletion suggestions.

    :attr List[str] completions: (optional) Array of autocomplete suggestion based
          on the provided prefix.
    """

    def __init__(self, *, completions: List[str] = None) -> None:
        """
        Initialize a Completions object.

        :param List[str] completions: (optional) Array of autocomplete suggestion
               based on the provided prefix.
        """
        self.completions = completions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Completions':
        """Initialize a Completions object from a json dictionary."""
        args = {}
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
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Completions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Completions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComponentSettingsAggregation():
    """
    Display settings for aggregations.

    :attr str name: (optional) Identifier used to map aggregation settings to
          aggregation configuration.
    :attr str label: (optional) User-friendly alias for the aggregation.
    :attr bool multiple_selections_allowed: (optional) Whether users is allowed to
          select more than one of the aggregation terms.
    :attr str visualization_type: (optional) Type of visualization to use when
          rendering the aggregation.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 label: str = None,
                 multiple_selections_allowed: bool = None,
                 visualization_type: str = None) -> None:
        """
        Initialize a ComponentSettingsAggregation object.

        :param str name: (optional) Identifier used to map aggregation settings to
               aggregation configuration.
        :param str label: (optional) User-friendly alias for the aggregation.
        :param bool multiple_selections_allowed: (optional) Whether users is
               allowed to select more than one of the aggregation terms.
        :param str visualization_type: (optional) Type of visualization to use when
               rendering the aggregation.
        """
        self.name = name
        self.label = label
        self.multiple_selections_allowed = multiple_selections_allowed
        self.visualization_type = visualization_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComponentSettingsAggregation':
        """Initialize a ComponentSettingsAggregation object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'multiple_selections_allowed' in _dict:
            args['multiple_selections_allowed'] = _dict.get(
                'multiple_selections_allowed')
        if 'visualization_type' in _dict:
            args['visualization_type'] = _dict.get('visualization_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'multiple_selections_allowed'
                  ) and self.multiple_selections_allowed is not None:
            _dict[
                'multiple_selections_allowed'] = self.multiple_selections_allowed
        if hasattr(
                self,
                'visualization_type') and self.visualization_type is not None:
            _dict['visualization_type'] = self.visualization_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComponentSettingsAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComponentSettingsAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComponentSettingsAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class VisualizationTypeEnum(str, Enum):
        """
        Type of visualization to use when rendering the aggregation.
        """
        AUTO = 'auto'
        FACET_TABLE = 'facet_table'
        WORD_CLOUD = 'word_cloud'
        MAP = 'map'


class ComponentSettingsFieldsShown():
    """
    Fields shown in the results section of the UI.

    :attr ComponentSettingsFieldsShownBody body: (optional) Body label.
    :attr ComponentSettingsFieldsShownTitle title: (optional) Title label.
    """

    def __init__(self,
                 *,
                 body: 'ComponentSettingsFieldsShownBody' = None,
                 title: 'ComponentSettingsFieldsShownTitle' = None) -> None:
        """
        Initialize a ComponentSettingsFieldsShown object.

        :param ComponentSettingsFieldsShownBody body: (optional) Body label.
        :param ComponentSettingsFieldsShownTitle title: (optional) Title label.
        """
        self.body = body
        self.title = title

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComponentSettingsFieldsShown':
        """Initialize a ComponentSettingsFieldsShown object from a json dictionary."""
        args = {}
        if 'body' in _dict:
            args['body'] = ComponentSettingsFieldsShownBody.from_dict(
                _dict.get('body'))
        if 'title' in _dict:
            args['title'] = ComponentSettingsFieldsShownTitle.from_dict(
                _dict.get('title'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsFieldsShown object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'body') and self.body is not None:
            if isinstance(self.body, dict):
                _dict['body'] = self.body
            else:
                _dict['body'] = self.body.to_dict()
        if hasattr(self, 'title') and self.title is not None:
            if isinstance(self.title, dict):
                _dict['title'] = self.title
            else:
                _dict['title'] = self.title.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComponentSettingsFieldsShown object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComponentSettingsFieldsShown') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComponentSettingsFieldsShown') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComponentSettingsFieldsShownBody():
    """
    Body label.

    :attr bool use_passage: (optional) Use the whole passage as the body.
    :attr str field: (optional) Use a specific field as the title.
    """

    def __init__(self, *, use_passage: bool = None, field: str = None) -> None:
        """
        Initialize a ComponentSettingsFieldsShownBody object.

        :param bool use_passage: (optional) Use the whole passage as the body.
        :param str field: (optional) Use a specific field as the title.
        """
        self.use_passage = use_passage
        self.field = field

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComponentSettingsFieldsShownBody':
        """Initialize a ComponentSettingsFieldsShownBody object from a json dictionary."""
        args = {}
        if 'use_passage' in _dict:
            args['use_passage'] = _dict.get('use_passage')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsFieldsShownBody object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'use_passage') and self.use_passage is not None:
            _dict['use_passage'] = self.use_passage
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComponentSettingsFieldsShownBody object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComponentSettingsFieldsShownBody') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComponentSettingsFieldsShownBody') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComponentSettingsFieldsShownTitle():
    """
    Title label.

    :attr str field: (optional) Use a specific field as the title.
    """

    def __init__(self, *, field: str = None) -> None:
        """
        Initialize a ComponentSettingsFieldsShownTitle object.

        :param str field: (optional) Use a specific field as the title.
        """
        self.field = field

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComponentSettingsFieldsShownTitle':
        """Initialize a ComponentSettingsFieldsShownTitle object from a json dictionary."""
        args = {}
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsFieldsShownTitle object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComponentSettingsFieldsShownTitle object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComponentSettingsFieldsShownTitle') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComponentSettingsFieldsShownTitle') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComponentSettingsResponse():
    """
    The default component settings for this project.

    :attr ComponentSettingsFieldsShown fields_shown: (optional) Fields shown in the
          results section of the UI.
    :attr bool autocomplete: (optional) Whether or not autocomplete is enabled.
    :attr bool structured_search: (optional) Whether or not structured search is
          enabled.
    :attr int results_per_page: (optional) Number or results shown per page.
    :attr List[ComponentSettingsAggregation] aggregations: (optional) a list of
          component setting aggregations.
    """

    def __init__(
            self,
            *,
            fields_shown: 'ComponentSettingsFieldsShown' = None,
            autocomplete: bool = None,
            structured_search: bool = None,
            results_per_page: int = None,
            aggregations: List['ComponentSettingsAggregation'] = None) -> None:
        """
        Initialize a ComponentSettingsResponse object.

        :param ComponentSettingsFieldsShown fields_shown: (optional) Fields shown
               in the results section of the UI.
        :param bool autocomplete: (optional) Whether or not autocomplete is
               enabled.
        :param bool structured_search: (optional) Whether or not structured search
               is enabled.
        :param int results_per_page: (optional) Number or results shown per page.
        :param List[ComponentSettingsAggregation] aggregations: (optional) a list
               of component setting aggregations.
        """
        self.fields_shown = fields_shown
        self.autocomplete = autocomplete
        self.structured_search = structured_search
        self.results_per_page = results_per_page
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComponentSettingsResponse':
        """Initialize a ComponentSettingsResponse object from a json dictionary."""
        args = {}
        if 'fields_shown' in _dict:
            args['fields_shown'] = ComponentSettingsFieldsShown.from_dict(
                _dict.get('fields_shown'))
        if 'autocomplete' in _dict:
            args['autocomplete'] = _dict.get('autocomplete')
        if 'structured_search' in _dict:
            args['structured_search'] = _dict.get('structured_search')
        if 'results_per_page' in _dict:
            args['results_per_page'] = _dict.get('results_per_page')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                ComponentSettingsAggregation.from_dict(v)
                for v in _dict.get('aggregations')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fields_shown') and self.fields_shown is not None:
            if isinstance(self.fields_shown, dict):
                _dict['fields_shown'] = self.fields_shown
            else:
                _dict['fields_shown'] = self.fields_shown.to_dict()
        if hasattr(self, 'autocomplete') and self.autocomplete is not None:
            _dict['autocomplete'] = self.autocomplete
        if hasattr(self,
                   'structured_search') and self.structured_search is not None:
            _dict['structured_search'] = self.structured_search
        if hasattr(self,
                   'results_per_page') and self.results_per_page is not None:
            _dict['results_per_page'] = self.results_per_page
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            aggregations_list = []
            for v in self.aggregations:
                if isinstance(v, dict):
                    aggregations_list.append(v)
                else:
                    aggregations_list.append(v.to_dict())
            _dict['aggregations'] = aggregations_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComponentSettingsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComponentSettingsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComponentSettingsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateDocumentClassifier():
    """
    An object that manages the settings and data that is required to train a document
    classification model.

    :attr str name: A human-readable name of the document classifier.
    :attr str description: (optional) A description of the document classifier.
    :attr str language: The language of the training data that is associated with
          the document classifier. Language is specified by using the ISO 639-1 language
          code, such as `en` for English or `ja` for Japanese.
    :attr str answer_field: The name of the field from the training and test data
          that contains the classification labels.
    :attr List[DocumentClassifierEnrichment] enrichments: (optional) An array of
          enrichments to apply to the data that is used to train and test the document
          classifier. The output from the enrichments is used as features by the
          classifier to classify the document content both during training and at run
          time.
    :attr ClassifierFederatedModel federated_classification: (optional) An object
          with details for creating federated document classifier models.
    """

    def __init__(
            self,
            name: str,
            language: str,
            answer_field: str,
            *,
            description: str = None,
            enrichments: List['DocumentClassifierEnrichment'] = None,
            federated_classification: 'ClassifierFederatedModel' = None
    ) -> None:
        """
        Initialize a CreateDocumentClassifier object.

        :param str name: A human-readable name of the document classifier.
        :param str language: The language of the training data that is associated
               with the document classifier. Language is specified by using the ISO 639-1
               language code, such as `en` for English or `ja` for Japanese.
        :param str answer_field: The name of the field from the training and test
               data that contains the classification labels.
        :param str description: (optional) A description of the document
               classifier.
        :param List[DocumentClassifierEnrichment] enrichments: (optional) An array
               of enrichments to apply to the data that is used to train and test the
               document classifier. The output from the enrichments is used as features by
               the classifier to classify the document content both during training and at
               run time.
        :param ClassifierFederatedModel federated_classification: (optional) An
               object with details for creating federated document classifier models.
        """
        self.name = name
        self.description = description
        self.language = language
        self.answer_field = answer_field
        self.enrichments = enrichments
        self.federated_classification = federated_classification

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateDocumentClassifier':
        """Initialize a CreateDocumentClassifier object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in CreateDocumentClassifier JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in CreateDocumentClassifier JSON'
            )
        if 'answer_field' in _dict:
            args['answer_field'] = _dict.get('answer_field')
        else:
            raise ValueError(
                'Required property \'answer_field\' not present in CreateDocumentClassifier JSON'
            )
        if 'enrichments' in _dict:
            args['enrichments'] = [
                DocumentClassifierEnrichment.from_dict(v)
                for v in _dict.get('enrichments')
            ]
        if 'federated_classification' in _dict:
            args[
                'federated_classification'] = ClassifierFederatedModel.from_dict(
                    _dict.get('federated_classification'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateDocumentClassifier object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'answer_field') and self.answer_field is not None:
            _dict['answer_field'] = self.answer_field
        if hasattr(self, 'enrichments') and self.enrichments is not None:
            enrichments_list = []
            for v in self.enrichments:
                if isinstance(v, dict):
                    enrichments_list.append(v)
                else:
                    enrichments_list.append(v.to_dict())
            _dict['enrichments'] = enrichments_list
        if hasattr(self, 'federated_classification'
                  ) and self.federated_classification is not None:
            if isinstance(self.federated_classification, dict):
                _dict[
                    'federated_classification'] = self.federated_classification
            else:
                _dict[
                    'federated_classification'] = self.federated_classification.to_dict(
                    )
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateDocumentClassifier object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateDocumentClassifier') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateDocumentClassifier') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateEnrichment():
    """
    Information about a specific enrichment.

    :attr str name: (optional) The human readable name for this enrichment.
    :attr str description: (optional) The description of this enrichment.
    :attr str type: (optional) The type of this enrichment. The following types are
          supported:
          * `classifier`: Creates a document classifier enrichment from a document
          classifier model that you create by using the [Document classifier
          API](/apidocs/discovery-data#createdocumentclassifier). **Note**: A text
          classifier enrichment can be created only from the product user interface.
          * `dictionary`: Creates a custom dictionary enrichment that you define in a CSV
          file.
          * `regular_expression`: Creates a custom regular expression enrichment from
          regex syntax that you specify in the request.
          * `rule_based`: Creates an enrichment from an advanced rules model that is
          created and exported as a ZIP file from Watson Knowledge Studio.
          * `uima_annotator`: Creates an enrichment from a custom UIMA text analysis model
          that is defined in a PEAR file created in one of the following ways:
              * Watson Explorer Content Analytics Studio. **Note**: Supported in IBM Cloud
          Pak for Data instances only.
              * Rule-based model that is created in Watson Knowledge Studio.
          * `watson_knowledge_studio_model`: Creates an enrichment from a Watson Knowledge
          Studio machine learning model that is defined in a ZIP file.
    :attr EnrichmentOptions options: (optional) An object that contains options for
          the current enrichment. Starting with version `2020-08-30`, the enrichment
          options are not included in responses from the List Enrichments method.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 type: str = None,
                 options: 'EnrichmentOptions' = None) -> None:
        """
        Initialize a CreateEnrichment object.

        :param str name: (optional) The human readable name for this enrichment.
        :param str description: (optional) The description of this enrichment.
        :param str type: (optional) The type of this enrichment. The following
               types are supported:
               * `classifier`: Creates a document classifier enrichment from a document
               classifier model that you create by using the [Document classifier
               API](/apidocs/discovery-data#createdocumentclassifier). **Note**: A text
               classifier enrichment can be created only from the product user interface.
               * `dictionary`: Creates a custom dictionary enrichment that you define in a
               CSV file.
               * `regular_expression`: Creates a custom regular expression enrichment from
               regex syntax that you specify in the request.
               * `rule_based`: Creates an enrichment from an advanced rules model that is
               created and exported as a ZIP file from Watson Knowledge Studio.
               * `uima_annotator`: Creates an enrichment from a custom UIMA text analysis
               model that is defined in a PEAR file created in one of the following ways:
                   * Watson Explorer Content Analytics Studio. **Note**: Supported in IBM
               Cloud Pak for Data instances only.
                   * Rule-based model that is created in Watson Knowledge Studio.
               * `watson_knowledge_studio_model`: Creates an enrichment from a Watson
               Knowledge Studio machine learning model that is defined in a ZIP file.
        :param EnrichmentOptions options: (optional) An object that contains
               options for the current enrichment. Starting with version `2020-08-30`, the
               enrichment options are not included in responses from the List Enrichments
               method.
        """
        self.name = name
        self.description = description
        self.type = type
        self.options = options

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateEnrichment':
        """Initialize a CreateEnrichment object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'options' in _dict:
            args['options'] = EnrichmentOptions.from_dict(_dict.get('options'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateEnrichment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'options') and self.options is not None:
            if isinstance(self.options, dict):
                _dict['options'] = self.options
            else:
                _dict['options'] = self.options.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateEnrichment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateEnrichment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateEnrichment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of this enrichment. The following types are supported:
        * `classifier`: Creates a document classifier enrichment from a document
        classifier model that you create by using the [Document classifier
        API](/apidocs/discovery-data#createdocumentclassifier). **Note**: A text
        classifier enrichment can be created only from the product user interface.
        * `dictionary`: Creates a custom dictionary enrichment that you define in a CSV
        file.
        * `regular_expression`: Creates a custom regular expression enrichment from regex
        syntax that you specify in the request.
        * `rule_based`: Creates an enrichment from an advanced rules model that is created
        and exported as a ZIP file from Watson Knowledge Studio.
        * `uima_annotator`: Creates an enrichment from a custom UIMA text analysis model
        that is defined in a PEAR file created in one of the following ways:
            * Watson Explorer Content Analytics Studio. **Note**: Supported in IBM Cloud
        Pak for Data instances only.
            * Rule-based model that is created in Watson Knowledge Studio.
        * `watson_knowledge_studio_model`: Creates an enrichment from a Watson Knowledge
        Studio machine learning model that is defined in a ZIP file.
        """
        CLASSIFIER = 'classifier'
        DICTIONARY = 'dictionary'
        REGULAR_EXPRESSION = 'regular_expression'
        UIMA_ANNOTATOR = 'uima_annotator'
        RULE_BASED = 'rule_based'
        WATSON_KNOWLEDGE_STUDIO_MODEL = 'watson_knowledge_studio_model'


class DefaultQueryParams():
    """
    Default query parameters for this project.

    :attr List[str] collection_ids: (optional) An array of collection identifiers to
          query. If empty or omitted all collections in the project are queried.
    :attr DefaultQueryParamsPassages passages: (optional) Default settings
          configuration for passage search options.
    :attr DefaultQueryParamsTableResults table_results: (optional) Default project
          query settings for table results.
    :attr str aggregation: (optional) A string representing the default aggregation
          query for the project.
    :attr DefaultQueryParamsSuggestedRefinements suggested_refinements: (optional)
          Object that contains suggested refinement settings.
          **Note**: The `suggested_refinements` parameter that identified dynamic facets
          from the data is deprecated.
    :attr bool spelling_suggestions: (optional) When `true`, a spelling suggestions
          for the query are returned by default.
    :attr bool highlight: (optional) When `true`, highlights for the query are
          returned by default.
    :attr int count: (optional) The number of document results returned by default.
    :attr str sort: (optional) A comma separated list of document fields to sort
          results by default.
    :attr List[str] return_: (optional) An array of field names to return in
          document results if present by default.
    """

    def __init__(self,
                 *,
                 collection_ids: List[str] = None,
                 passages: 'DefaultQueryParamsPassages' = None,
                 table_results: 'DefaultQueryParamsTableResults' = None,
                 aggregation: str = None,
                 suggested_refinements:
                 'DefaultQueryParamsSuggestedRefinements' = None,
                 spelling_suggestions: bool = None,
                 highlight: bool = None,
                 count: int = None,
                 sort: str = None,
                 return_: List[str] = None) -> None:
        """
        Initialize a DefaultQueryParams object.

        :param List[str] collection_ids: (optional) An array of collection
               identifiers to query. If empty or omitted all collections in the project
               are queried.
        :param DefaultQueryParamsPassages passages: (optional) Default settings
               configuration for passage search options.
        :param DefaultQueryParamsTableResults table_results: (optional) Default
               project query settings for table results.
        :param str aggregation: (optional) A string representing the default
               aggregation query for the project.
        :param DefaultQueryParamsSuggestedRefinements suggested_refinements:
               (optional) Object that contains suggested refinement settings.
               **Note**: The `suggested_refinements` parameter that identified dynamic
               facets from the data is deprecated.
        :param bool spelling_suggestions: (optional) When `true`, a spelling
               suggestions for the query are returned by default.
        :param bool highlight: (optional) When `true`, highlights for the query are
               returned by default.
        :param int count: (optional) The number of document results returned by
               default.
        :param str sort: (optional) A comma separated list of document fields to
               sort results by default.
        :param List[str] return_: (optional) An array of field names to return in
               document results if present by default.
        """
        self.collection_ids = collection_ids
        self.passages = passages
        self.table_results = table_results
        self.aggregation = aggregation
        self.suggested_refinements = suggested_refinements
        self.spelling_suggestions = spelling_suggestions
        self.highlight = highlight
        self.count = count
        self.sort = sort
        self.return_ = return_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefaultQueryParams':
        """Initialize a DefaultQueryParams object from a json dictionary."""
        args = {}
        if 'collection_ids' in _dict:
            args['collection_ids'] = _dict.get('collection_ids')
        if 'passages' in _dict:
            args['passages'] = DefaultQueryParamsPassages.from_dict(
                _dict.get('passages'))
        if 'table_results' in _dict:
            args['table_results'] = DefaultQueryParamsTableResults.from_dict(
                _dict.get('table_results'))
        if 'aggregation' in _dict:
            args['aggregation'] = _dict.get('aggregation')
        if 'suggested_refinements' in _dict:
            args[
                'suggested_refinements'] = DefaultQueryParamsSuggestedRefinements.from_dict(
                    _dict.get('suggested_refinements'))
        if 'spelling_suggestions' in _dict:
            args['spelling_suggestions'] = _dict.get('spelling_suggestions')
        if 'highlight' in _dict:
            args['highlight'] = _dict.get('highlight')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'sort' in _dict:
            args['sort'] = _dict.get('sort')
        if 'return' in _dict:
            args['return_'] = _dict.get('return')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefaultQueryParams object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_ids') and self.collection_ids is not None:
            _dict['collection_ids'] = self.collection_ids
        if hasattr(self, 'passages') and self.passages is not None:
            if isinstance(self.passages, dict):
                _dict['passages'] = self.passages
            else:
                _dict['passages'] = self.passages.to_dict()
        if hasattr(self, 'table_results') and self.table_results is not None:
            if isinstance(self.table_results, dict):
                _dict['table_results'] = self.table_results
            else:
                _dict['table_results'] = self.table_results.to_dict()
        if hasattr(self, 'aggregation') and self.aggregation is not None:
            _dict['aggregation'] = self.aggregation
        if hasattr(self, 'suggested_refinements'
                  ) and self.suggested_refinements is not None:
            if isinstance(self.suggested_refinements, dict):
                _dict['suggested_refinements'] = self.suggested_refinements
            else:
                _dict[
                    'suggested_refinements'] = self.suggested_refinements.to_dict(
                    )
        if hasattr(self, 'spelling_suggestions'
                  ) and self.spelling_suggestions is not None:
            _dict['spelling_suggestions'] = self.spelling_suggestions
        if hasattr(self, 'highlight') and self.highlight is not None:
            _dict['highlight'] = self.highlight
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'sort') and self.sort is not None:
            _dict['sort'] = self.sort
        if hasattr(self, 'return_') and self.return_ is not None:
            _dict['return'] = self.return_
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefaultQueryParams object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultQueryParams') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultQueryParams') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefaultQueryParamsPassages():
    """
    Default settings configuration for passage search options.

    :attr bool enabled: (optional) When `true`, a passage search is performed by
          default.
    :attr int count: (optional) The number of passages to return.
    :attr List[str] fields: (optional) An array of field names to perform the
          passage search on.
    :attr int characters: (optional) The approximate number of characters that each
          returned passage will contain.
    :attr bool per_document: (optional) When `true` the number of passages that can
          be returned from a single document is restricted to the *max_per_document*
          value.
    :attr int max_per_document: (optional) The default maximum number of passages
          that can be taken from a single document as the result of a passage query.
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 count: int = None,
                 fields: List[str] = None,
                 characters: int = None,
                 per_document: bool = None,
                 max_per_document: int = None) -> None:
        """
        Initialize a DefaultQueryParamsPassages object.

        :param bool enabled: (optional) When `true`, a passage search is performed
               by default.
        :param int count: (optional) The number of passages to return.
        :param List[str] fields: (optional) An array of field names to perform the
               passage search on.
        :param int characters: (optional) The approximate number of characters that
               each returned passage will contain.
        :param bool per_document: (optional) When `true` the number of passages
               that can be returned from a single document is restricted to the
               *max_per_document* value.
        :param int max_per_document: (optional) The default maximum number of
               passages that can be taken from a single document as the result of a
               passage query.
        """
        self.enabled = enabled
        self.count = count
        self.fields = fields
        self.characters = characters
        self.per_document = per_document
        self.max_per_document = max_per_document

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefaultQueryParamsPassages':
        """Initialize a DefaultQueryParamsPassages object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        if 'characters' in _dict:
            args['characters'] = _dict.get('characters')
        if 'per_document' in _dict:
            args['per_document'] = _dict.get('per_document')
        if 'max_per_document' in _dict:
            args['max_per_document'] = _dict.get('max_per_document')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefaultQueryParamsPassages object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        if hasattr(self, 'characters') and self.characters is not None:
            _dict['characters'] = self.characters
        if hasattr(self, 'per_document') and self.per_document is not None:
            _dict['per_document'] = self.per_document
        if hasattr(self,
                   'max_per_document') and self.max_per_document is not None:
            _dict['max_per_document'] = self.max_per_document
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefaultQueryParamsPassages object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultQueryParamsPassages') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultQueryParamsPassages') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefaultQueryParamsSuggestedRefinements():
    """
    Object that contains suggested refinement settings.
    **Note**: The `suggested_refinements` parameter that identified dynamic facets from
    the data is deprecated.

    :attr bool enabled: (optional) When `true`, suggested refinements for the query
          are returned by default.
    :attr int count: (optional) The number of suggested refinements to return by
          default.
    """

    def __init__(self, *, enabled: bool = None, count: int = None) -> None:
        """
        Initialize a DefaultQueryParamsSuggestedRefinements object.

        :param bool enabled: (optional) When `true`, suggested refinements for the
               query are returned by default.
        :param int count: (optional) The number of suggested refinements to return
               by default.
        """
        self.enabled = enabled
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefaultQueryParamsSuggestedRefinements':
        """Initialize a DefaultQueryParamsSuggestedRefinements object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefaultQueryParamsSuggestedRefinements object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefaultQueryParamsSuggestedRefinements object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultQueryParamsSuggestedRefinements') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultQueryParamsSuggestedRefinements') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefaultQueryParamsTableResults():
    """
    Default project query settings for table results.

    :attr bool enabled: (optional) When `true`, a table results for the query are
          returned by default.
    :attr int count: (optional) The number of table results to return by default.
    :attr int per_document: (optional) The number of table results to include in
          each result document.
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 count: int = None,
                 per_document: int = None) -> None:
        """
        Initialize a DefaultQueryParamsTableResults object.

        :param bool enabled: (optional) When `true`, a table results for the query
               are returned by default.
        :param int count: (optional) The number of table results to return by
               default.
        :param int per_document: (optional) The number of table results to include
               in each result document.
        """
        self.enabled = enabled
        self.count = count
        self.per_document = per_document

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefaultQueryParamsTableResults':
        """Initialize a DefaultQueryParamsTableResults object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'per_document' in _dict:
            args['per_document'] = _dict.get('per_document')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefaultQueryParamsTableResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'per_document') and self.per_document is not None:
            _dict['per_document'] = self.per_document
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefaultQueryParamsTableResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultQueryParamsTableResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultQueryParamsTableResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteDocumentResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteDocumentResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the document. A deleted document has the status deleted.
        """
        DELETED = 'deleted'


class DocumentAccepted():
    """
    Information returned after an uploaded document is accepted.

    :attr str document_id: (optional) The unique identifier of the ingested
          document.
    :attr str status: (optional) Status of the document in the ingestion process. A
          status of `processing` is returned for documents that are ingested with a
          *version* date before `2019-01-01`. The `pending` status is returned for all
          others.
    """

    def __init__(self, *, document_id: str = None, status: str = None) -> None:
        """
        Initialize a DocumentAccepted object.

        :param str document_id: (optional) The unique identifier of the ingested
               document.
        :param str status: (optional) Status of the document in the ingestion
               process. A status of `processing` is returned for documents that are
               ingested with a *version* date before `2019-01-01`. The `pending` status is
               returned for all others.
        """
        self.document_id = document_id
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentAccepted':
        """Initialize a DocumentAccepted object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentAccepted object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentAccepted') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentAccepted') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the document in the ingestion process. A status of `processing` is
        returned for documents that are ingested with a *version* date before
        `2019-01-01`. The `pending` status is returned for all others.
        """
        PROCESSING = 'processing'
        PENDING = 'pending'


class DocumentAttribute():
    """
    List of document attributes.

    :attr str type: (optional) The type of attribute.
    :attr str text: (optional) The text associated with the attribute.
    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 text: str = None,
                 location: 'TableElementLocation' = None) -> None:
        """
        Initialize a DocumentAttribute object.

        :param str type: (optional) The type of attribute.
        :param str text: (optional) The text associated with the attribute.
        :param TableElementLocation location: (optional) The numeric location of
               the identified element in the document, represented with two integers
               labeled `begin` and `end`.
        """
        self.type = type
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentAttribute':
        """Initialize a DocumentAttribute object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = TableElementLocation.from_dict(
                _dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentAttribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            if isinstance(self.location, dict):
                _dict['location'] = self.location
            else:
                _dict['location'] = self.location.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentClassifier():
    """
    Information about a document classifier.

    :attr str classifier_id: (optional) A unique identifier of the document
          classifier.
    :attr str name: A human-readable name of the document classifier.
    :attr str description: (optional) A description of the document classifier.
    :attr datetime created: (optional) The date that the document classifier was
          created.
    :attr str language: (optional) The language of the training data that is
          associated with the document classifier. Language is specified by using the ISO
          639-1 language code, such as `en` for English or `ja` for Japanese.
    :attr List[DocumentClassifierEnrichment] enrichments: (optional) An array of
          enrichments to apply to the data that is used to train and test the document
          classifier. The output from the enrichments is used as features by the
          classifier to classify the document content both during training and at run
          time.
    :attr List[str] recognized_fields: (optional) An array of fields that are used
          to train the document classifier. The same set of fields must exist in the
          training data, the test data, and the documents where the resulting document
          classifier enrichment is applied at run time.
    :attr str answer_field: (optional) The name of the field from the training and
          test data that contains the classification labels.
    :attr str training_data_file: (optional) Name of the CSV file with training data
          that is used to train the document classifier.
    :attr str test_data_file: (optional) Name of the CSV file with data that is used
          to test the document classifier. If no test data is provided, a subset of the
          training data is used for testing purposes.
    :attr ClassifierFederatedModel federated_classification: (optional) An object
          with details for creating federated document classifier models.
    """

    def __init__(
            self,
            name: str,
            *,
            classifier_id: str = None,
            description: str = None,
            created: datetime = None,
            language: str = None,
            enrichments: List['DocumentClassifierEnrichment'] = None,
            recognized_fields: List[str] = None,
            answer_field: str = None,
            training_data_file: str = None,
            test_data_file: str = None,
            federated_classification: 'ClassifierFederatedModel' = None
    ) -> None:
        """
        Initialize a DocumentClassifier object.

        :param str name: A human-readable name of the document classifier.
        :param str description: (optional) A description of the document
               classifier.
        :param str language: (optional) The language of the training data that is
               associated with the document classifier. Language is specified by using the
               ISO 639-1 language code, such as `en` for English or `ja` for Japanese.
        :param List[DocumentClassifierEnrichment] enrichments: (optional) An array
               of enrichments to apply to the data that is used to train and test the
               document classifier. The output from the enrichments is used as features by
               the classifier to classify the document content both during training and at
               run time.
        :param List[str] recognized_fields: (optional) An array of fields that are
               used to train the document classifier. The same set of fields must exist in
               the training data, the test data, and the documents where the resulting
               document classifier enrichment is applied at run time.
        :param str answer_field: (optional) The name of the field from the training
               and test data that contains the classification labels.
        :param str training_data_file: (optional) Name of the CSV file with
               training data that is used to train the document classifier.
        :param str test_data_file: (optional) Name of the CSV file with data that
               is used to test the document classifier. If no test data is provided, a
               subset of the training data is used for testing purposes.
        :param ClassifierFederatedModel federated_classification: (optional) An
               object with details for creating federated document classifier models.
        """
        self.classifier_id = classifier_id
        self.name = name
        self.description = description
        self.created = created
        self.language = language
        self.enrichments = enrichments
        self.recognized_fields = recognized_fields
        self.answer_field = answer_field
        self.training_data_file = training_data_file
        self.test_data_file = test_data_file
        self.federated_classification = federated_classification

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentClassifier':
        """Initialize a DocumentClassifier object from a json dictionary."""
        args = {}
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in DocumentClassifier JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'enrichments' in _dict:
            args['enrichments'] = [
                DocumentClassifierEnrichment.from_dict(v)
                for v in _dict.get('enrichments')
            ]
        if 'recognized_fields' in _dict:
            args['recognized_fields'] = _dict.get('recognized_fields')
        if 'answer_field' in _dict:
            args['answer_field'] = _dict.get('answer_field')
        if 'training_data_file' in _dict:
            args['training_data_file'] = _dict.get('training_data_file')
        if 'test_data_file' in _dict:
            args['test_data_file'] = _dict.get('test_data_file')
        if 'federated_classification' in _dict:
            args[
                'federated_classification'] = ClassifierFederatedModel.from_dict(
                    _dict.get('federated_classification'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentClassifier object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifier_id') and getattr(
                self, 'classifier_id') is not None:
            _dict['classifier_id'] = getattr(self, 'classifier_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'enrichments') and self.enrichments is not None:
            enrichments_list = []
            for v in self.enrichments:
                if isinstance(v, dict):
                    enrichments_list.append(v)
                else:
                    enrichments_list.append(v.to_dict())
            _dict['enrichments'] = enrichments_list
        if hasattr(self,
                   'recognized_fields') and self.recognized_fields is not None:
            _dict['recognized_fields'] = self.recognized_fields
        if hasattr(self, 'answer_field') and self.answer_field is not None:
            _dict['answer_field'] = self.answer_field
        if hasattr(
                self,
                'training_data_file') and self.training_data_file is not None:
            _dict['training_data_file'] = self.training_data_file
        if hasattr(self, 'test_data_file') and self.test_data_file is not None:
            _dict['test_data_file'] = self.test_data_file
        if hasattr(self, 'federated_classification'
                  ) and self.federated_classification is not None:
            if isinstance(self.federated_classification, dict):
                _dict[
                    'federated_classification'] = self.federated_classification
            else:
                _dict[
                    'federated_classification'] = self.federated_classification.to_dict(
                    )
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentClassifier object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentClassifier') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentClassifier') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentClassifierEnrichment():
    """
    An object that describes enrichments that are applied to the training and test data
    that is used by the document classifier.

    :attr str enrichment_id: A unique identifier of the enrichment.
    :attr List[str] fields: An array of field names where the enrichment is applied.
    """

    def __init__(self, enrichment_id: str, fields: List[str]) -> None:
        """
        Initialize a DocumentClassifierEnrichment object.

        :param str enrichment_id: A unique identifier of the enrichment.
        :param List[str] fields: An array of field names where the enrichment is
               applied.
        """
        self.enrichment_id = enrichment_id
        self.fields = fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentClassifierEnrichment':
        """Initialize a DocumentClassifierEnrichment object from a json dictionary."""
        args = {}
        if 'enrichment_id' in _dict:
            args['enrichment_id'] = _dict.get('enrichment_id')
        else:
            raise ValueError(
                'Required property \'enrichment_id\' not present in DocumentClassifierEnrichment JSON'
            )
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        else:
            raise ValueError(
                'Required property \'fields\' not present in DocumentClassifierEnrichment JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentClassifierEnrichment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enrichment_id') and self.enrichment_id is not None:
            _dict['enrichment_id'] = self.enrichment_id
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentClassifierEnrichment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentClassifierEnrichment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentClassifierEnrichment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentClassifierModel():
    """
    Information about a document classifier model.

    :attr str model_id: (optional) A unique identifier of the document classifier
          model.
    :attr str name: A human-readable name of the document classifier model.
    :attr str description: (optional) A description of the document classifier
          model.
    :attr datetime created: (optional) The date that the document classifier model
          was created.
    :attr datetime updated: (optional) The date that the document classifier model
          was last updated.
    :attr str training_data_file: (optional) Name of the CSV file that contains the
          training data that is used to train the document classifier model.
    :attr str test_data_file: (optional) Name of the CSV file that contains data
          that is used to test the document classifier model. If no test data is provided,
          a subset of the training data is used for testing purposes.
    :attr str status: (optional) The status of the training run.
    :attr ClassifierModelEvaluation evaluation: (optional) An object that contains
          information about a trained document classifier model.
    :attr str enrichment_id: (optional) A unique identifier of the enrichment that
          is generated by this document classifier model.
    :attr datetime deployed_at: (optional) The date that the document classifier
          model was deployed.
    """

    def __init__(self,
                 name: str,
                 *,
                 model_id: str = None,
                 description: str = None,
                 created: datetime = None,
                 updated: datetime = None,
                 training_data_file: str = None,
                 test_data_file: str = None,
                 status: str = None,
                 evaluation: 'ClassifierModelEvaluation' = None,
                 enrichment_id: str = None,
                 deployed_at: datetime = None) -> None:
        """
        Initialize a DocumentClassifierModel object.

        :param str name: A human-readable name of the document classifier model.
        :param str description: (optional) A description of the document classifier
               model.
        :param str training_data_file: (optional) Name of the CSV file that
               contains the training data that is used to train the document classifier
               model.
        :param str test_data_file: (optional) Name of the CSV file that contains
               data that is used to test the document classifier model. If no test data is
               provided, a subset of the training data is used for testing purposes.
        :param str status: (optional) The status of the training run.
        :param ClassifierModelEvaluation evaluation: (optional) An object that
               contains information about a trained document classifier model.
        :param str enrichment_id: (optional) A unique identifier of the enrichment
               that is generated by this document classifier model.
        """
        self.model_id = model_id
        self.name = name
        self.description = description
        self.created = created
        self.updated = updated
        self.training_data_file = training_data_file
        self.test_data_file = test_data_file
        self.status = status
        self.evaluation = evaluation
        self.enrichment_id = enrichment_id
        self.deployed_at = deployed_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentClassifierModel':
        """Initialize a DocumentClassifierModel object from a json dictionary."""
        args = {}
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in DocumentClassifierModel JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'training_data_file' in _dict:
            args['training_data_file'] = _dict.get('training_data_file')
        if 'test_data_file' in _dict:
            args['test_data_file'] = _dict.get('test_data_file')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'evaluation' in _dict:
            args['evaluation'] = ClassifierModelEvaluation.from_dict(
                _dict.get('evaluation'))
        if 'enrichment_id' in _dict:
            args['enrichment_id'] = _dict.get('enrichment_id')
        if 'deployed_at' in _dict:
            args['deployed_at'] = string_to_datetime(_dict.get('deployed_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentClassifierModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model_id') and getattr(self, 'model_id') is not None:
            _dict['model_id'] = getattr(self, 'model_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(
                self,
                'training_data_file') and self.training_data_file is not None:
            _dict['training_data_file'] = self.training_data_file
        if hasattr(self, 'test_data_file') and self.test_data_file is not None:
            _dict['test_data_file'] = self.test_data_file
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'evaluation') and self.evaluation is not None:
            if isinstance(self.evaluation, dict):
                _dict['evaluation'] = self.evaluation
            else:
                _dict['evaluation'] = self.evaluation.to_dict()
        if hasattr(self, 'enrichment_id') and self.enrichment_id is not None:
            _dict['enrichment_id'] = self.enrichment_id
        if hasattr(self, 'deployed_at') and getattr(self,
                                                    'deployed_at') is not None:
            _dict['deployed_at'] = datetime_to_string(
                getattr(self, 'deployed_at'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentClassifierModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentClassifierModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentClassifierModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the training run.
        """
        TRAINING = 'training'
        AVAILABLE = 'available'
        FAILED = 'failed'


class DocumentClassifierModels():
    """
    An object that contains a list of document classifier model definitions.

    :attr List[DocumentClassifierModel] models: (optional) An array of document
          classifier model definitions.
    """

    def __init__(self,
                 *,
                 models: List['DocumentClassifierModel'] = None) -> None:
        """
        Initialize a DocumentClassifierModels object.

        :param List[DocumentClassifierModel] models: (optional) An array of
               document classifier model definitions.
        """
        self.models = models

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentClassifierModels':
        """Initialize a DocumentClassifierModels object from a json dictionary."""
        args = {}
        if 'models' in _dict:
            args['models'] = [
                DocumentClassifierModel.from_dict(v)
                for v in _dict.get('models')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentClassifierModels object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            models_list = []
            for v in self.models:
                if isinstance(v, dict):
                    models_list.append(v)
                else:
                    models_list.append(v.to_dict())
            _dict['models'] = models_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentClassifierModels object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentClassifierModels') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentClassifierModels') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentClassifiers():
    """
    An object that contains a list of document classifier definitions.

    :attr List[DocumentClassifier] classifiers: (optional) An array of document
          classifier definitions.
    """

    def __init__(self,
                 *,
                 classifiers: List['DocumentClassifier'] = None) -> None:
        """
        Initialize a DocumentClassifiers object.

        :param List[DocumentClassifier] classifiers: (optional) An array of
               document classifier definitions.
        """
        self.classifiers = classifiers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentClassifiers':
        """Initialize a DocumentClassifiers object from a json dictionary."""
        args = {}
        if 'classifiers' in _dict:
            args['classifiers'] = [
                DocumentClassifier.from_dict(v)
                for v in _dict.get('classifiers')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentClassifiers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifiers') and self.classifiers is not None:
            classifiers_list = []
            for v in self.classifiers:
                if isinstance(v, dict):
                    classifiers_list.append(v)
                else:
                    classifiers_list.append(v.to_dict())
            _dict['classifiers'] = classifiers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentClassifiers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentClassifiers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentClassifiers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentDetails():
    """
    Information about a document.

    :attr str document_id: (optional) The unique identifier of the document.
    :attr datetime created: (optional) Date and time that the document is added to
          the collection. For a child document, the date and time when the process that
          generates the child document runs. The date-time format is
          `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.
    :attr datetime updated: (optional) Date and time that the document is finished
          being processed and is indexed. This date changes whenever the document is
          reprocessed, including for enrichment changes. The date-time format is
          `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.
    :attr str status: (optional) The status of the ingestion of the document. The
          possible values are:
          * `available`: Ingestion is finished and the document is indexed.
          * `failed`: Ingestion is finished, but the document is not indexed because of an
          error.
          * `pending`: The document is uploaded, but the ingestion process is not started.
          * `processing`: Ingestion is in progress.
    :attr List[Notice] notices: (optional) Array of JSON objects for notices,
          meaning warning or error messages, that are produced by the document ingestion
          process. The array does not include notices that are produced for child
          documents that are generated when a document is processed.
    :attr DocumentDetailsChildren children: (optional) Information about the child
          documents that are generated from a single document during ingestion or other
          processing.
    :attr str filename: (optional) Name of the original source file (if available).
    :attr str file_type: (optional) The type of the original source file, such as
          `csv`, `excel`, `html`, `json`, `pdf`, `text`, `word`, and so on.
    :attr str sha256: (optional) The SHA-256 hash of the original source file. The
          hash is formatted as a hexadecimal string.
    """

    def __init__(self,
                 *,
                 document_id: str = None,
                 created: datetime = None,
                 updated: datetime = None,
                 status: str = None,
                 notices: List['Notice'] = None,
                 children: 'DocumentDetailsChildren' = None,
                 filename: str = None,
                 file_type: str = None,
                 sha256: str = None) -> None:
        """
        Initialize a DocumentDetails object.

        :param str status: (optional) The status of the ingestion of the document.
               The possible values are:
               * `available`: Ingestion is finished and the document is indexed.
               * `failed`: Ingestion is finished, but the document is not indexed because
               of an error.
               * `pending`: The document is uploaded, but the ingestion process is not
               started.
               * `processing`: Ingestion is in progress.
        :param List[Notice] notices: (optional) Array of JSON objects for notices,
               meaning warning or error messages, that are produced by the document
               ingestion process. The array does not include notices that are produced for
               child documents that are generated when a document is processed.
        :param DocumentDetailsChildren children: (optional) Information about the
               child documents that are generated from a single document during ingestion
               or other processing.
        :param str filename: (optional) Name of the original source file (if
               available).
        :param str file_type: (optional) The type of the original source file, such
               as `csv`, `excel`, `html`, `json`, `pdf`, `text`, `word`, and so on.
        :param str sha256: (optional) The SHA-256 hash of the original source file.
               The hash is formatted as a hexadecimal string.
        """
        self.document_id = document_id
        self.created = created
        self.updated = updated
        self.status = status
        self.notices = notices
        self.children = children
        self.filename = filename
        self.file_type = file_type
        self.sha256 = sha256

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentDetails':
        """Initialize a DocumentDetails object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'notices' in _dict:
            args['notices'] = [
                Notice.from_dict(v) for v in _dict.get('notices')
            ]
        if 'children' in _dict:
            args['children'] = DocumentDetailsChildren.from_dict(
                _dict.get('children'))
        if 'filename' in _dict:
            args['filename'] = _dict.get('filename')
        if 'file_type' in _dict:
            args['file_type'] = _dict.get('file_type')
        if 'sha256' in _dict:
            args['sha256'] = _dict.get('sha256')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and getattr(self,
                                                    'document_id') is not None:
            _dict['document_id'] = getattr(self, 'document_id')
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'notices') and self.notices is not None:
            notices_list = []
            for v in self.notices:
                if isinstance(v, dict):
                    notices_list.append(v)
                else:
                    notices_list.append(v.to_dict())
            _dict['notices'] = notices_list
        if hasattr(self, 'children') and self.children is not None:
            if isinstance(self.children, dict):
                _dict['children'] = self.children
            else:
                _dict['children'] = self.children.to_dict()
        if hasattr(self, 'filename') and self.filename is not None:
            _dict['filename'] = self.filename
        if hasattr(self, 'file_type') and self.file_type is not None:
            _dict['file_type'] = self.file_type
        if hasattr(self, 'sha256') and self.sha256 is not None:
            _dict['sha256'] = self.sha256
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the ingestion of the document. The possible values are:
        * `available`: Ingestion is finished and the document is indexed.
        * `failed`: Ingestion is finished, but the document is not indexed because of an
        error.
        * `pending`: The document is uploaded, but the ingestion process is not started.
        * `processing`: Ingestion is in progress.
        """
        AVAILABLE = 'available'
        FAILED = 'failed'
        PENDING = 'pending'
        PROCESSING = 'processing'


class DocumentDetailsChildren():
    """
    Information about the child documents that are generated from a single document during
    ingestion or other processing.

    :attr bool have_notices: (optional) Indicates whether the child documents have
          any notices. The value is `false` if the document does not have child documents.
    :attr int count: (optional) Number of child documents. The value is `0` when
          processing of the document doesn't generate any child documents.
    """

    def __init__(self, *, have_notices: bool = None, count: int = None) -> None:
        """
        Initialize a DocumentDetailsChildren object.

        :param bool have_notices: (optional) Indicates whether the child documents
               have any notices. The value is `false` if the document does not have child
               documents.
        :param int count: (optional) Number of child documents. The value is `0`
               when processing of the document doesn't generate any child documents.
        """
        self.have_notices = have_notices
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentDetailsChildren':
        """Initialize a DocumentDetailsChildren object from a json dictionary."""
        args = {}
        if 'have_notices' in _dict:
            args['have_notices'] = _dict.get('have_notices')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentDetailsChildren object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'have_notices') and self.have_notices is not None:
            _dict['have_notices'] = self.have_notices
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentDetailsChildren object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentDetailsChildren') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentDetailsChildren') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Enrichment():
    """
    Information about a specific enrichment.

    :attr str enrichment_id: (optional) The unique identifier of this enrichment.
    :attr str name: (optional) The human readable name for this enrichment.
    :attr str description: (optional) The description of this enrichment.
    :attr str type: (optional) The type of this enrichment.
    :attr EnrichmentOptions options: (optional) An object that contains options for
          the current enrichment. Starting with version `2020-08-30`, the enrichment
          options are not included in responses from the List Enrichments method.
    """

    def __init__(self,
                 *,
                 enrichment_id: str = None,
                 name: str = None,
                 description: str = None,
                 type: str = None,
                 options: 'EnrichmentOptions' = None) -> None:
        """
        Initialize a Enrichment object.

        :param str name: (optional) The human readable name for this enrichment.
        :param str description: (optional) The description of this enrichment.
        :param str type: (optional) The type of this enrichment.
        :param EnrichmentOptions options: (optional) An object that contains
               options for the current enrichment. Starting with version `2020-08-30`, the
               enrichment options are not included in responses from the List Enrichments
               method.
        """
        self.enrichment_id = enrichment_id
        self.name = name
        self.description = description
        self.type = type
        self.options = options

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Enrichment':
        """Initialize a Enrichment object from a json dictionary."""
        args = {}
        if 'enrichment_id' in _dict:
            args['enrichment_id'] = _dict.get('enrichment_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'options' in _dict:
            args['options'] = EnrichmentOptions.from_dict(_dict.get('options'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Enrichment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enrichment_id') and getattr(
                self, 'enrichment_id') is not None:
            _dict['enrichment_id'] = getattr(self, 'enrichment_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'options') and self.options is not None:
            if isinstance(self.options, dict):
                _dict['options'] = self.options
            else:
                _dict['options'] = self.options.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Enrichment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Enrichment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Enrichment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of this enrichment.
        """
        PART_OF_SPEECH = 'part_of_speech'
        SENTIMENT = 'sentiment'
        NATURAL_LANGUAGE_UNDERSTANDING = 'natural_language_understanding'
        DICTIONARY = 'dictionary'
        REGULAR_EXPRESSION = 'regular_expression'
        UIMA_ANNOTATOR = 'uima_annotator'
        RULE_BASED = 'rule_based'
        WATSON_KNOWLEDGE_STUDIO_MODEL = 'watson_knowledge_studio_model'
        CLASSIFIER = 'classifier'


class EnrichmentOptions():
    """
    An object that contains options for the current enrichment. Starting with version
    `2020-08-30`, the enrichment options are not included in responses from the List
    Enrichments method.

    :attr List[str] languages: (optional) An array of supported languages for this
          enrichment. When creating an enrichment, only specify a language that is used by
          the model or in the dictionary. Required when **type** is `dictionary`. Optional
          when **type** is `rule_based`. Not valid when creating any other type of
          enrichment.
    :attr str entity_type: (optional) The name of the entity type. This value is
          used as the field name in the index. Required when **type** is `dictionary` or
          `regular_expression`. Not valid when creating any other type of enrichment.
    :attr str regular_expression: (optional) The regular expression to apply for
          this enrichment. Required when **type** is `regular_expression`. Not valid when
          creating any other type of enrichment.
    :attr str result_field: (optional) The name of the result document field that
          this enrichment creates. Required when **type** is `rule_based` or `classifier`.
          Not valid when creating any other type of enrichment.
    :attr str classifier_id: (optional) A unique identifier of the document
          classifier. Required when **type** is `classifier`. Not valid when creating any
          other type of enrichment.
    :attr str model_id: (optional) A unique identifier of the document classifier
          model. Required when **type** is `classifier`. Not valid when creating any other
          type of enrichment.
    :attr float confidence_threshold: (optional) Specifies a threshold. Only classes
          with evaluation confidence scores that are higher than the specified threshold
          are included in the output. Optional when **type** is `classifier`. Not valid
          when creating any other type of enrichment.
    :attr int top_k: (optional) Evaluates only the classes that fall in the top set
          of results when ranked by confidence. For example, if set to `5`, then the top
          five classes for each document are evaluated. If set to 0, the
          **confidence_threshold** is used to determine the predicted classes. Optional
          when **type** is `classifier`. Not valid when creating any other type of
          enrichment.
    """

    def __init__(self,
                 *,
                 languages: List[str] = None,
                 entity_type: str = None,
                 regular_expression: str = None,
                 result_field: str = None,
                 classifier_id: str = None,
                 model_id: str = None,
                 confidence_threshold: float = None,
                 top_k: int = None) -> None:
        """
        Initialize a EnrichmentOptions object.

        :param List[str] languages: (optional) An array of supported languages for
               this enrichment. When creating an enrichment, only specify a language that
               is used by the model or in the dictionary. Required when **type** is
               `dictionary`. Optional when **type** is `rule_based`. Not valid when
               creating any other type of enrichment.
        :param str entity_type: (optional) The name of the entity type. This value
               is used as the field name in the index. Required when **type** is
               `dictionary` or `regular_expression`. Not valid when creating any other
               type of enrichment.
        :param str regular_expression: (optional) The regular expression to apply
               for this enrichment. Required when **type** is `regular_expression`. Not
               valid when creating any other type of enrichment.
        :param str result_field: (optional) The name of the result document field
               that this enrichment creates. Required when **type** is `rule_based` or
               `classifier`. Not valid when creating any other type of enrichment.
        :param str classifier_id: (optional) A unique identifier of the document
               classifier. Required when **type** is `classifier`. Not valid when creating
               any other type of enrichment.
        :param str model_id: (optional) A unique identifier of the document
               classifier model. Required when **type** is `classifier`. Not valid when
               creating any other type of enrichment.
        :param float confidence_threshold: (optional) Specifies a threshold. Only
               classes with evaluation confidence scores that are higher than the
               specified threshold are included in the output. Optional when **type** is
               `classifier`. Not valid when creating any other type of enrichment.
        :param int top_k: (optional) Evaluates only the classes that fall in the
               top set of results when ranked by confidence. For example, if set to `5`,
               then the top five classes for each document are evaluated. If set to 0, the
               **confidence_threshold** is used to determine the predicted classes.
               Optional when **type** is `classifier`. Not valid when creating any other
               type of enrichment.
        """
        self.languages = languages
        self.entity_type = entity_type
        self.regular_expression = regular_expression
        self.result_field = result_field
        self.classifier_id = classifier_id
        self.model_id = model_id
        self.confidence_threshold = confidence_threshold
        self.top_k = top_k

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnrichmentOptions':
        """Initialize a EnrichmentOptions object from a json dictionary."""
        args = {}
        if 'languages' in _dict:
            args['languages'] = _dict.get('languages')
        if 'entity_type' in _dict:
            args['entity_type'] = _dict.get('entity_type')
        if 'regular_expression' in _dict:
            args['regular_expression'] = _dict.get('regular_expression')
        if 'result_field' in _dict:
            args['result_field'] = _dict.get('result_field')
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'confidence_threshold' in _dict:
            args['confidence_threshold'] = _dict.get('confidence_threshold')
        if 'top_k' in _dict:
            args['top_k'] = _dict.get('top_k')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnrichmentOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'languages') and self.languages is not None:
            _dict['languages'] = self.languages
        if hasattr(self, 'entity_type') and self.entity_type is not None:
            _dict['entity_type'] = self.entity_type
        if hasattr(
                self,
                'regular_expression') and self.regular_expression is not None:
            _dict['regular_expression'] = self.regular_expression
        if hasattr(self, 'result_field') and self.result_field is not None:
            _dict['result_field'] = self.result_field
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'confidence_threshold'
                  ) and self.confidence_threshold is not None:
            _dict['confidence_threshold'] = self.confidence_threshold
        if hasattr(self, 'top_k') and self.top_k is not None:
            _dict['top_k'] = self.top_k
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnrichmentOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnrichmentOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnrichmentOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Enrichments():
    """
    An object that contains an array of enrichment definitions.

    :attr List[Enrichment] enrichments: (optional) An array of enrichment
          definitions.
    """

    def __init__(self, *, enrichments: List['Enrichment'] = None) -> None:
        """
        Initialize a Enrichments object.

        :param List[Enrichment] enrichments: (optional) An array of enrichment
               definitions.
        """
        self.enrichments = enrichments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Enrichments':
        """Initialize a Enrichments object from a json dictionary."""
        args = {}
        if 'enrichments' in _dict:
            args['enrichments'] = [
                Enrichment.from_dict(v) for v in _dict.get('enrichments')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Enrichments object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enrichments') and self.enrichments is not None:
            enrichments_list = []
            for v in self.enrichments:
                if isinstance(v, dict):
                    enrichments_list.append(v)
                else:
                    enrichments_list.append(v.to_dict())
            _dict['enrichments'] = enrichments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Enrichments object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Enrichments') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Enrichments') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Expansion():
    """
    An expansion definition. Each object respresents one set of expandable strings. For
    example, you could have expansions for the word `hot` in one object, and expansions
    for the word `cold` in another. Follow these guidelines when you add terms:
    * Specify the terms in lowercase. Lowercase terms expand to uppercase.
    * Multiword terms are supported only in bidirectional expansions.
    * Do not specify a term that is specified in the stop words list for the collection.

    :attr List[str] input_terms: (optional) A list of terms that will be expanded
          for this expansion. If specified, only the items in this list are expanded.
    :attr List[str] expanded_terms: A list of terms that this expansion will be
          expanded to. If specified without **input_terms**, the list also functions as
          the input term list.
    """

    def __init__(self,
                 expanded_terms: List[str],
                 *,
                 input_terms: List[str] = None) -> None:
        """
        Initialize a Expansion object.

        :param List[str] expanded_terms: A list of terms that this expansion will
               be expanded to. If specified without **input_terms**, the list also
               functions as the input term list.
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
        return json.dumps(self.to_dict(), indent=2)

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
          `bidirectional` or `unidirectional`.
          * **Bidirectional**: Each entry in the `expanded_terms` list expands to include
          all expanded terms. For example, a query for `ibm` expands to `ibm OR
          international business machines OR big blue`.
          * **Unidirectional**: The terms in `input_terms` in the query are replaced by
          the terms in `expanded_terms`. For example, a query for the often misused term
          `on premise` is converted to `on premises OR on-premises` and does not contain
          the original term. If you want an input term to be included in the query, then
          repeat the input term in the expanded terms list.
    """

    def __init__(self, expansions: List['Expansion']) -> None:
        """
        Initialize a Expansions object.

        :param List[Expansion] expansions: An array of query expansion definitions.
                Each object in the **expansions** array represents a term or set of terms
               that will be expanded into other terms. Each expansion object can be
               configured as `bidirectional` or `unidirectional`.
               * **Bidirectional**: Each entry in the `expanded_terms` list expands to
               include all expanded terms. For example, a query for `ibm` expands to `ibm
               OR international business machines OR big blue`.
               * **Unidirectional**: The terms in `input_terms` in the query are replaced
               by the terms in `expanded_terms`. For example, a query for the often
               misused term `on premise` is converted to `on premises OR on-premises` and
               does not contain the original term. If you want an input term to be
               included in the query, then repeat the input term in the expanded terms
               list.
        """
        self.expansions = expansions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Expansions':
        """Initialize a Expansions object from a json dictionary."""
        args = {}
        if 'expansions' in _dict:
            args['expansions'] = [
                Expansion.from_dict(v) for v in _dict.get('expansions')
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
            expansions_list = []
            for v in self.expansions:
                if isinstance(v, dict):
                    expansions_list.append(v)
                else:
                    expansions_list.append(v.to_dict())
            _dict['expansions'] = expansions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Expansions object."""
        return json.dumps(self.to_dict(), indent=2)

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
    Object that contains field details.

    :attr str field: (optional) The name of the field.
    :attr str type: (optional) The type of the field.
    :attr str collection_id: (optional) The collection Id of the collection where
          the field was found.
    """

    def __init__(self,
                 *,
                 field: str = None,
                 type: str = None,
                 collection_id: str = None) -> None:
        """
        Initialize a Field object.

        """
        self.field = field
        self.type = type
        self.collection_id = collection_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Field':
        """Initialize a Field object from a json dictionary."""
        args = {}
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Field object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and getattr(self, 'field') is not None:
            _dict['field'] = getattr(self, 'field')
        if hasattr(self, 'type') and getattr(self, 'type') is not None:
            _dict['type'] = getattr(self, 'type')
        if hasattr(self, 'collection_id') and getattr(
                self, 'collection_id') is not None:
            _dict['collection_id'] = getattr(self, 'collection_id')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Field object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Field') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Field') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of the field.
        """
        NESTED = 'nested'
        STRING = 'string'
        DATE = 'date'
        LONG = 'long'
        INTEGER = 'integer'
        SHORT = 'short'
        BYTE = 'byte'
        DOUBLE = 'double'
        FLOAT = 'float'
        BOOLEAN = 'boolean'
        BINARY = 'binary'


class ListCollectionsResponse():
    """
    Response object that contains an array of collection details.

    :attr List[Collection] collections: (optional) An array that contains
          information about each collection in the project.
    """

    def __init__(self, *, collections: List['Collection'] = None) -> None:
        """
        Initialize a ListCollectionsResponse object.

        :param List[Collection] collections: (optional) An array that contains
               information about each collection in the project.
        """
        self.collections = collections

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCollectionsResponse':
        """Initialize a ListCollectionsResponse object from a json dictionary."""
        args = {}
        if 'collections' in _dict:
            args['collections'] = [
                Collection.from_dict(v) for v in _dict.get('collections')
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
            collections_list = []
            for v in self.collections:
                if isinstance(v, dict):
                    collections_list.append(v)
                else:
                    collections_list.append(v.to_dict())
            _dict['collections'] = collections_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCollectionsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListCollectionsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCollectionsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListDocumentsResponse():
    """
    Response object that contains an array of documents.

    :attr int matching_results: (optional) The number of matching results for the
          document query.
    :attr List[DocumentDetails] documents: (optional) An array that lists the
          documents in a collection. Only the document ID of each document is returned in
          the list. You can use the [Get document](#getdocument) method to get more
          information about an individual document.
    """

    def __init__(self,
                 *,
                 matching_results: int = None,
                 documents: List['DocumentDetails'] = None) -> None:
        """
        Initialize a ListDocumentsResponse object.

        :param int matching_results: (optional) The number of matching results for
               the document query.
        :param List[DocumentDetails] documents: (optional) An array that lists the
               documents in a collection. Only the document ID of each document is
               returned in the list. You can use the [Get document](#getdocument) method
               to get more information about an individual document.
        """
        self.matching_results = matching_results
        self.documents = documents

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListDocumentsResponse':
        """Initialize a ListDocumentsResponse object from a json dictionary."""
        args = {}
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'documents' in _dict:
            args['documents'] = [
                DocumentDetails.from_dict(v) for v in _dict.get('documents')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListDocumentsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'documents') and self.documents is not None:
            documents_list = []
            for v in self.documents:
                if isinstance(v, dict):
                    documents_list.append(v)
                else:
                    documents_list.append(v.to_dict())
            _dict['documents'] = documents_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListDocumentsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListDocumentsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListDocumentsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListFieldsResponse():
    """
    The list of fetched fields.
    The fields are returned using a fully qualified name format, however, the format
    differs slightly from that used by the query operations.
      * Fields which contain nested objects are assigned a type of "nested".
      * Fields which belong to a nested object are prefixed with `.properties` (for
    example, `warnings.properties.severity` means that the `warnings` object has a
    property called `severity`).

    :attr List[Field] fields: (optional) An array that contains information about
          each field in the collections.
    """

    def __init__(self, *, fields: List['Field'] = None) -> None:
        """
        Initialize a ListFieldsResponse object.

        :param List[Field] fields: (optional) An array that contains information
               about each field in the collections.
        """
        self.fields = fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListFieldsResponse':
        """Initialize a ListFieldsResponse object from a json dictionary."""
        args = {}
        if 'fields' in _dict:
            args['fields'] = [Field.from_dict(v) for v in _dict.get('fields')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFieldsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fields') and self.fields is not None:
            fields_list = []
            for v in self.fields:
                if isinstance(v, dict):
                    fields_list.append(v)
                else:
                    fields_list.append(v.to_dict())
            _dict['fields'] = fields_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListFieldsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListFieldsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListFieldsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListProjectsResponse():
    """
    A list of projects in this instance.

    :attr List[ProjectListDetails] projects: (optional) An array of project details.
    """

    def __init__(self, *, projects: List['ProjectListDetails'] = None) -> None:
        """
        Initialize a ListProjectsResponse object.

        :param List[ProjectListDetails] projects: (optional) An array of project
               details.
        """
        self.projects = projects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListProjectsResponse':
        """Initialize a ListProjectsResponse object from a json dictionary."""
        args = {}
        if 'projects' in _dict:
            args['projects'] = [
                ProjectListDetails.from_dict(v) for v in _dict.get('projects')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListProjectsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'projects') and self.projects is not None:
            projects_list = []
            for v in self.projects:
                if isinstance(v, dict):
                    projects_list.append(v)
                else:
                    projects_list.append(v.to_dict())
            _dict['projects'] = projects_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListProjectsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListProjectsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListProjectsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ModelEvaluationMacroAverage():
    """
    A macro-average computes metric independently for each class and then takes the
    average. Class refers to the classification label that is specified in the
    **answer_field**.

    :attr float precision: A metric that measures how many of the overall documents
          are classified correctly.
    :attr float recall: A metric that measures how often documents that should be
          classified into certain classes are classified into those classes.
    :attr float f1: A metric that measures whether the optimal balance between
          precision and recall is reached. The F1 score can be interpreted as a weighted
          average of the precision and recall values. An F1 score reaches its best value
          at 1 and worst value at 0.
    """

    def __init__(self, precision: float, recall: float, f1: float) -> None:
        """
        Initialize a ModelEvaluationMacroAverage object.

        :param float precision: A metric that measures how many of the overall
               documents are classified correctly.
        :param float recall: A metric that measures how often documents that should
               be classified into certain classes are classified into those classes.
        :param float f1: A metric that measures whether the optimal balance between
               precision and recall is reached. The F1 score can be interpreted as a
               weighted average of the precision and recall values. An F1 score reaches
               its best value at 1 and worst value at 0.
        """
        self.precision = precision
        self.recall = recall
        self.f1 = f1

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelEvaluationMacroAverage':
        """Initialize a ModelEvaluationMacroAverage object from a json dictionary."""
        args = {}
        if 'precision' in _dict:
            args['precision'] = _dict.get('precision')
        else:
            raise ValueError(
                'Required property \'precision\' not present in ModelEvaluationMacroAverage JSON'
            )
        if 'recall' in _dict:
            args['recall'] = _dict.get('recall')
        else:
            raise ValueError(
                'Required property \'recall\' not present in ModelEvaluationMacroAverage JSON'
            )
        if 'f1' in _dict:
            args['f1'] = _dict.get('f1')
        else:
            raise ValueError(
                'Required property \'f1\' not present in ModelEvaluationMacroAverage JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelEvaluationMacroAverage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'precision') and self.precision is not None:
            _dict['precision'] = self.precision
        if hasattr(self, 'recall') and self.recall is not None:
            _dict['recall'] = self.recall
        if hasattr(self, 'f1') and self.f1 is not None:
            _dict['f1'] = self.f1
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelEvaluationMacroAverage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelEvaluationMacroAverage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelEvaluationMacroAverage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ModelEvaluationMicroAverage():
    """
    A micro-average aggregates the contributions of all classes to compute the average
    metric. Classes refers to the classification labels that are specified in the
    **answer_field**.

    :attr float precision: A metric that measures how many of the overall documents
          are classified correctly.
    :attr float recall: A metric that measures how often documents that should be
          classified into certain classes are classified into those classes.
    :attr float f1: A metric that measures whether the optimal balance between
          precision and recall is reached. The F1 score can be interpreted as a weighted
          average of the precision and recall values. An F1 score reaches its best value
          at 1 and worst value at 0.
    """

    def __init__(self, precision: float, recall: float, f1: float) -> None:
        """
        Initialize a ModelEvaluationMicroAverage object.

        :param float precision: A metric that measures how many of the overall
               documents are classified correctly.
        :param float recall: A metric that measures how often documents that should
               be classified into certain classes are classified into those classes.
        :param float f1: A metric that measures whether the optimal balance between
               precision and recall is reached. The F1 score can be interpreted as a
               weighted average of the precision and recall values. An F1 score reaches
               its best value at 1 and worst value at 0.
        """
        self.precision = precision
        self.recall = recall
        self.f1 = f1

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ModelEvaluationMicroAverage':
        """Initialize a ModelEvaluationMicroAverage object from a json dictionary."""
        args = {}
        if 'precision' in _dict:
            args['precision'] = _dict.get('precision')
        else:
            raise ValueError(
                'Required property \'precision\' not present in ModelEvaluationMicroAverage JSON'
            )
        if 'recall' in _dict:
            args['recall'] = _dict.get('recall')
        else:
            raise ValueError(
                'Required property \'recall\' not present in ModelEvaluationMicroAverage JSON'
            )
        if 'f1' in _dict:
            args['f1'] = _dict.get('f1')
        else:
            raise ValueError(
                'Required property \'f1\' not present in ModelEvaluationMicroAverage JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ModelEvaluationMicroAverage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'precision') and self.precision is not None:
            _dict['precision'] = self.precision
        if hasattr(self, 'recall') and self.recall is not None:
            _dict['recall'] = self.recall
        if hasattr(self, 'f1') and self.f1 is not None:
            _dict['f1'] = self.f1
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ModelEvaluationMicroAverage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ModelEvaluationMicroAverage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ModelEvaluationMicroAverage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Notice():
    """
    A notice produced for the collection.

    :attr str notice_id: (optional) Identifies the notice. Many notices might have
          the same ID. This field exists so that user applications can programmatically
          identify a notice and take automatic corrective action. Typical notice IDs
          include:
          `index_failed`, `index_failed_too_many_requests`,
          `index_failed_incompatible_field`, `index_failed_cluster_unavailable`,
          `ingestion_timeout`, `ingestion_error`, `bad_request`, `internal_error`,
          `missing_model`, `unsupported_model`,
          `smart_document_understanding_failed_incompatible_field`,
          `smart_document_understanding_failed_internal_error`,
          `smart_document_understanding_failed_internal_error`,
          `smart_document_understanding_failed_warning`,
          `smart_document_understanding_page_error`,
          `smart_document_understanding_page_warning`. **Note:** This is not a complete
          list. Other values might be returned.
    :attr datetime created: (optional) The creation date of the collection in the
          format yyyy-MM-dd'T'HH:mm:ss.SSS'Z'.
    :attr str document_id: (optional) Unique identifier of the document.
    :attr str collection_id: (optional) Unique identifier of the collection.
    :attr str query_id: (optional) Unique identifier of the query used for relevance
          training.
    :attr str severity: (optional) Severity level of the notice.
    :attr str step: (optional) Ingestion or training step in which the notice
          occurred.
    :attr str description: (optional) The description of the notice.
    """

    def __init__(self,
                 *,
                 notice_id: str = None,
                 created: datetime = None,
                 document_id: str = None,
                 collection_id: str = None,
                 query_id: str = None,
                 severity: str = None,
                 step: str = None,
                 description: str = None) -> None:
        """
        Initialize a Notice object.

        """
        self.notice_id = notice_id
        self.created = created
        self.document_id = document_id
        self.collection_id = collection_id
        self.query_id = query_id
        self.severity = severity
        self.step = step
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Notice':
        """Initialize a Notice object from a json dictionary."""
        args = {}
        if 'notice_id' in _dict:
            args['notice_id'] = _dict.get('notice_id')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
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
        if hasattr(self, 'notice_id') and getattr(self,
                                                  'notice_id') is not None:
            _dict['notice_id'] = getattr(self, 'notice_id')
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'document_id') and getattr(self,
                                                    'document_id') is not None:
            _dict['document_id'] = getattr(self, 'document_id')
        if hasattr(self, 'collection_id') and getattr(
                self, 'collection_id') is not None:
            _dict['collection_id'] = getattr(self, 'collection_id')
        if hasattr(self, 'query_id') and getattr(self, 'query_id') is not None:
            _dict['query_id'] = getattr(self, 'query_id')
        if hasattr(self, 'severity') and getattr(self, 'severity') is not None:
            _dict['severity'] = getattr(self, 'severity')
        if hasattr(self, 'step') and getattr(self, 'step') is not None:
            _dict['step'] = getattr(self, 'step')
        if hasattr(self, 'description') and getattr(self,
                                                    'description') is not None:
            _dict['description'] = getattr(self, 'description')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Notice object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Notice') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Notice') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SeverityEnum(str, Enum):
        """
        Severity level of the notice.
        """
        WARNING = 'warning'
        ERROR = 'error'


class PerClassModelEvaluation():
    """
    An object that measures the metrics from a training run for each classification label
    separately.

    :attr str name: Class name. Each class name is derived from a value in the
          **answer_field**.
    :attr float precision: A metric that measures how many of the overall documents
          are classified correctly.
    :attr float recall: A metric that measures how often documents that should be
          classified into certain classes are classified into those classes.
    :attr float f1: A metric that measures whether the optimal balance between
          precision and recall is reached. The F1 score can be interpreted as a weighted
          average of the precision and recall values. An F1 score reaches its best value
          at 1 and worst value at 0.
    """

    def __init__(self, name: str, precision: float, recall: float,
                 f1: float) -> None:
        """
        Initialize a PerClassModelEvaluation object.

        :param str name: Class name. Each class name is derived from a value in the
               **answer_field**.
        :param float precision: A metric that measures how many of the overall
               documents are classified correctly.
        :param float recall: A metric that measures how often documents that should
               be classified into certain classes are classified into those classes.
        :param float f1: A metric that measures whether the optimal balance between
               precision and recall is reached. The F1 score can be interpreted as a
               weighted average of the precision and recall values. An F1 score reaches
               its best value at 1 and worst value at 0.
        """
        self.name = name
        self.precision = precision
        self.recall = recall
        self.f1 = f1

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PerClassModelEvaluation':
        """Initialize a PerClassModelEvaluation object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in PerClassModelEvaluation JSON'
            )
        if 'precision' in _dict:
            args['precision'] = _dict.get('precision')
        else:
            raise ValueError(
                'Required property \'precision\' not present in PerClassModelEvaluation JSON'
            )
        if 'recall' in _dict:
            args['recall'] = _dict.get('recall')
        else:
            raise ValueError(
                'Required property \'recall\' not present in PerClassModelEvaluation JSON'
            )
        if 'f1' in _dict:
            args['f1'] = _dict.get('f1')
        else:
            raise ValueError(
                'Required property \'f1\' not present in PerClassModelEvaluation JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PerClassModelEvaluation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'precision') and self.precision is not None:
            _dict['precision'] = self.precision
        if hasattr(self, 'recall') and self.recall is not None:
            _dict['recall'] = self.recall
        if hasattr(self, 'f1') and self.f1 is not None:
            _dict['f1'] = self.f1
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PerClassModelEvaluation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PerClassModelEvaluation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PerClassModelEvaluation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectDetails():
    """
    Detailed information about the specified project.

    :attr str project_id: (optional) The unique identifier of this project.
    :attr str name: (optional) The human readable name of this project.
    :attr str type: (optional) The type of project.
          The `content_intelligence` type is a *Document Retrieval for Contracts* project
          and the `other` type is a *Custom* project.
          The `content_mining` and `content_intelligence` types are available with Premium
          plan managed deployments and installed deployments only.
    :attr ProjectListDetailsRelevancyTrainingStatus relevancy_training_status:
          (optional) Relevancy training status information for this project.
    :attr int collection_count: (optional) The number of collections configured in
          this project.
    :attr DefaultQueryParams default_query_parameters: (optional) Default query
          parameters for this project.
    """

    def __init__(self,
                 *,
                 project_id: str = None,
                 name: str = None,
                 type: str = None,
                 relevancy_training_status:
                 'ProjectListDetailsRelevancyTrainingStatus' = None,
                 collection_count: int = None,
                 default_query_parameters: 'DefaultQueryParams' = None) -> None:
        """
        Initialize a ProjectDetails object.

        :param str name: (optional) The human readable name of this project.
        :param str type: (optional) The type of project.
               The `content_intelligence` type is a *Document Retrieval for Contracts*
               project and the `other` type is a *Custom* project.
               The `content_mining` and `content_intelligence` types are available with
               Premium plan managed deployments and installed deployments only.
        :param DefaultQueryParams default_query_parameters: (optional) Default
               query parameters for this project.
        """
        self.project_id = project_id
        self.name = name
        self.type = type
        self.relevancy_training_status = relevancy_training_status
        self.collection_count = collection_count
        self.default_query_parameters = default_query_parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectDetails':
        """Initialize a ProjectDetails object from a json dictionary."""
        args = {}
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'relevancy_training_status' in _dict:
            args[
                'relevancy_training_status'] = ProjectListDetailsRelevancyTrainingStatus.from_dict(
                    _dict.get('relevancy_training_status'))
        if 'collection_count' in _dict:
            args['collection_count'] = _dict.get('collection_count')
        if 'default_query_parameters' in _dict:
            args['default_query_parameters'] = DefaultQueryParams.from_dict(
                _dict.get('default_query_parameters'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'project_id') and getattr(self,
                                                   'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'relevancy_training_status') and getattr(
                self, 'relevancy_training_status') is not None:
            if isinstance(getattr(self, 'relevancy_training_status'), dict):
                _dict['relevancy_training_status'] = getattr(
                    self, 'relevancy_training_status')
            else:
                _dict['relevancy_training_status'] = getattr(
                    self, 'relevancy_training_status').to_dict()
        if hasattr(self, 'collection_count') and getattr(
                self, 'collection_count') is not None:
            _dict['collection_count'] = getattr(self, 'collection_count')
        if hasattr(self, 'default_query_parameters'
                  ) and self.default_query_parameters is not None:
            if isinstance(self.default_query_parameters, dict):
                _dict[
                    'default_query_parameters'] = self.default_query_parameters
            else:
                _dict[
                    'default_query_parameters'] = self.default_query_parameters.to_dict(
                    )
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of project.
        The `content_intelligence` type is a *Document Retrieval for Contracts* project
        and the `other` type is a *Custom* project.
        The `content_mining` and `content_intelligence` types are available with Premium
        plan managed deployments and installed deployments only.
        """
        DOCUMENT_RETRIEVAL = 'document_retrieval'
        CONVERSATIONAL_SEARCH = 'conversational_search'
        CONTENT_MINING = 'content_mining'
        CONTENT_INTELLIGENCE = 'content_intelligence'
        OTHER = 'other'


class ProjectListDetails():
    """
    Details about a specific project.

    :attr str project_id: (optional) The unique identifier of this project.
    :attr str name: (optional) The human readable name of this project.
    :attr str type: (optional) The type of project.
          The `content_intelligence` type is a *Document Retrieval for Contracts* project
          and the `other` type is a *Custom* project.
          The `content_mining` and `content_intelligence` types are available with Premium
          plan managed deployments and installed deployments only.
    :attr ProjectListDetailsRelevancyTrainingStatus relevancy_training_status:
          (optional) Relevancy training status information for this project.
    :attr int collection_count: (optional) The number of collections configured in
          this project.
    """

    def __init__(self,
                 *,
                 project_id: str = None,
                 name: str = None,
                 type: str = None,
                 relevancy_training_status:
                 'ProjectListDetailsRelevancyTrainingStatus' = None,
                 collection_count: int = None) -> None:
        """
        Initialize a ProjectListDetails object.

        :param str name: (optional) The human readable name of this project.
        :param str type: (optional) The type of project.
               The `content_intelligence` type is a *Document Retrieval for Contracts*
               project and the `other` type is a *Custom* project.
               The `content_mining` and `content_intelligence` types are available with
               Premium plan managed deployments and installed deployments only.
        """
        self.project_id = project_id
        self.name = name
        self.type = type
        self.relevancy_training_status = relevancy_training_status
        self.collection_count = collection_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectListDetails':
        """Initialize a ProjectListDetails object from a json dictionary."""
        args = {}
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'relevancy_training_status' in _dict:
            args[
                'relevancy_training_status'] = ProjectListDetailsRelevancyTrainingStatus.from_dict(
                    _dict.get('relevancy_training_status'))
        if 'collection_count' in _dict:
            args['collection_count'] = _dict.get('collection_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectListDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'project_id') and getattr(self,
                                                   'project_id') is not None:
            _dict['project_id'] = getattr(self, 'project_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'relevancy_training_status') and getattr(
                self, 'relevancy_training_status') is not None:
            if isinstance(getattr(self, 'relevancy_training_status'), dict):
                _dict['relevancy_training_status'] = getattr(
                    self, 'relevancy_training_status')
            else:
                _dict['relevancy_training_status'] = getattr(
                    self, 'relevancy_training_status').to_dict()
        if hasattr(self, 'collection_count') and getattr(
                self, 'collection_count') is not None:
            _dict['collection_count'] = getattr(self, 'collection_count')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectListDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectListDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectListDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of project.
        The `content_intelligence` type is a *Document Retrieval for Contracts* project
        and the `other` type is a *Custom* project.
        The `content_mining` and `content_intelligence` types are available with Premium
        plan managed deployments and installed deployments only.
        """
        DOCUMENT_RETRIEVAL = 'document_retrieval'
        CONVERSATIONAL_SEARCH = 'conversational_search'
        CONTENT_MINING = 'content_mining'
        CONTENT_INTELLIGENCE = 'content_intelligence'
        OTHER = 'other'


class ProjectListDetailsRelevancyTrainingStatus():
    """
    Relevancy training status information for this project.

    :attr str data_updated: (optional) When the training data was updated.
    :attr int total_examples: (optional) The total number of examples.
    :attr bool sufficient_label_diversity: (optional) When `true`, sufficient label
          diversity is present to allow training for this project.
    :attr bool processing: (optional) When `true`, the relevancy training is in
          processing.
    :attr bool minimum_examples_added: (optional) When `true`, the minimum number of
          examples required to train has been met.
    :attr str successfully_trained: (optional) The time that the most recent
          successful training occurred.
    :attr bool available: (optional) When `true`, relevancy training is available
          when querying collections in the project.
    :attr int notices: (optional) The number of notices generated during the
          relevancy training.
    :attr bool minimum_queries_added: (optional) When `true`, the minimum number of
          queries required to train has been met.
    """

    def __init__(self,
                 *,
                 data_updated: str = None,
                 total_examples: int = None,
                 sufficient_label_diversity: bool = None,
                 processing: bool = None,
                 minimum_examples_added: bool = None,
                 successfully_trained: str = None,
                 available: bool = None,
                 notices: int = None,
                 minimum_queries_added: bool = None) -> None:
        """
        Initialize a ProjectListDetailsRelevancyTrainingStatus object.

        :param str data_updated: (optional) When the training data was updated.
        :param int total_examples: (optional) The total number of examples.
        :param bool sufficient_label_diversity: (optional) When `true`, sufficient
               label diversity is present to allow training for this project.
        :param bool processing: (optional) When `true`, the relevancy training is
               in processing.
        :param bool minimum_examples_added: (optional) When `true`, the minimum
               number of examples required to train has been met.
        :param str successfully_trained: (optional) The time that the most recent
               successful training occurred.
        :param bool available: (optional) When `true`, relevancy training is
               available when querying collections in the project.
        :param int notices: (optional) The number of notices generated during the
               relevancy training.
        :param bool minimum_queries_added: (optional) When `true`, the minimum
               number of queries required to train has been met.
        """
        self.data_updated = data_updated
        self.total_examples = total_examples
        self.sufficient_label_diversity = sufficient_label_diversity
        self.processing = processing
        self.minimum_examples_added = minimum_examples_added
        self.successfully_trained = successfully_trained
        self.available = available
        self.notices = notices
        self.minimum_queries_added = minimum_queries_added

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'ProjectListDetailsRelevancyTrainingStatus':
        """Initialize a ProjectListDetailsRelevancyTrainingStatus object from a json dictionary."""
        args = {}
        if 'data_updated' in _dict:
            args['data_updated'] = _dict.get('data_updated')
        if 'total_examples' in _dict:
            args['total_examples'] = _dict.get('total_examples')
        if 'sufficient_label_diversity' in _dict:
            args['sufficient_label_diversity'] = _dict.get(
                'sufficient_label_diversity')
        if 'processing' in _dict:
            args['processing'] = _dict.get('processing')
        if 'minimum_examples_added' in _dict:
            args['minimum_examples_added'] = _dict.get('minimum_examples_added')
        if 'successfully_trained' in _dict:
            args['successfully_trained'] = _dict.get('successfully_trained')
        if 'available' in _dict:
            args['available'] = _dict.get('available')
        if 'notices' in _dict:
            args['notices'] = _dict.get('notices')
        if 'minimum_queries_added' in _dict:
            args['minimum_queries_added'] = _dict.get('minimum_queries_added')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectListDetailsRelevancyTrainingStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data_updated') and self.data_updated is not None:
            _dict['data_updated'] = self.data_updated
        if hasattr(self, 'total_examples') and self.total_examples is not None:
            _dict['total_examples'] = self.total_examples
        if hasattr(self, 'sufficient_label_diversity'
                  ) and self.sufficient_label_diversity is not None:
            _dict[
                'sufficient_label_diversity'] = self.sufficient_label_diversity
        if hasattr(self, 'processing') and self.processing is not None:
            _dict['processing'] = self.processing
        if hasattr(self, 'minimum_examples_added'
                  ) and self.minimum_examples_added is not None:
            _dict['minimum_examples_added'] = self.minimum_examples_added
        if hasattr(self, 'successfully_trained'
                  ) and self.successfully_trained is not None:
            _dict['successfully_trained'] = self.successfully_trained
        if hasattr(self, 'available') and self.available is not None:
            _dict['available'] = self.available
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = self.notices
        if hasattr(self, 'minimum_queries_added'
                  ) and self.minimum_queries_added is not None:
            _dict['minimum_queries_added'] = self.minimum_queries_added
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectListDetailsRelevancyTrainingStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'ProjectListDetailsRelevancyTrainingStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'ProjectListDetailsRelevancyTrainingStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregation():
    """
    An object that defines how to aggregate query results.

    """

    def __init__(self) -> None:
        """
        Initialize a QueryAggregation object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'QueryAggregationQueryTermAggregation',
                'QueryAggregationQueryGroupByAggregation',
                'QueryAggregationQueryHistogramAggregation',
                'QueryAggregationQueryTimesliceAggregation',
                'QueryAggregationQueryNestedAggregation',
                'QueryAggregationQueryFilterAggregation',
                'QueryAggregationQueryCalculationAggregation',
                'QueryAggregationQueryTopHitsAggregation',
                'QueryAggregationQueryPairAggregation',
                'QueryAggregationQueryTrendAggregation',
                'QueryAggregationQueryTopicAggregation'
            ]))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregation':
        """Initialize a QueryAggregation object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = (
            "Cannot convert dictionary into an instance of base class 'QueryAggregation'. "
            + "The discriminator value should map to a valid subclass: {1}"
        ).format(", ".join([
            'QueryAggregationQueryTermAggregation',
            'QueryAggregationQueryGroupByAggregation',
            'QueryAggregationQueryHistogramAggregation',
            'QueryAggregationQueryTimesliceAggregation',
            'QueryAggregationQueryNestedAggregation',
            'QueryAggregationQueryFilterAggregation',
            'QueryAggregationQueryCalculationAggregation',
            'QueryAggregationQueryTopHitsAggregation',
            'QueryAggregationQueryPairAggregation',
            'QueryAggregationQueryTrendAggregation',
            'QueryAggregationQueryTopicAggregation'
        ]))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a QueryAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['term'] = 'QueryAggregationQueryTermAggregation'
        mapping['group_by'] = 'QueryAggregationQueryGroupByAggregation'
        mapping['histogram'] = 'QueryAggregationQueryHistogramAggregation'
        mapping['timeslice'] = 'QueryAggregationQueryTimesliceAggregation'
        mapping['nested'] = 'QueryAggregationQueryNestedAggregation'
        mapping['filter'] = 'QueryAggregationQueryFilterAggregation'
        mapping['min'] = 'QueryAggregationQueryCalculationAggregation'
        mapping['max'] = 'QueryAggregationQueryCalculationAggregation'
        mapping['sum'] = 'QueryAggregationQueryCalculationAggregation'
        mapping['average'] = 'QueryAggregationQueryCalculationAggregation'
        mapping['unique_count'] = 'QueryAggregationQueryCalculationAggregation'
        mapping['top_hits'] = 'QueryAggregationQueryTopHitsAggregation'
        mapping['pair'] = 'QueryAggregationQueryPairAggregation'
        mapping['trend'] = 'QueryAggregationQueryTrendAggregation'
        mapping['topic'] = 'QueryAggregationQueryTopicAggregation'
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


class QueryGroupByAggregationResult():
    """
    Result group for the `group_by` aggregation.

    :attr str key: The condition that is met by the documents in this group. For
          example, `YEARTXT<2000`.
    :attr int matching_results: Number of documents that meet the query and
          condition.
    :attr float relevancy: (optional) The relevancy for this group. Returned only if
          `relevancy:true` is specified in the request.
    :attr int total_matching_documents: (optional) Number of documents that meet the
          condition in the whole set of documents in this collection. Returned only when
          `relevancy:true` is specified in the request.
    :attr float estimated_matching_results: (optional) The number of documents that
          are estimated to match the query and condition. Returned only when
          `relevancy:true` is specified in the request.
    :attr List[dict] aggregations: (optional) An array of subaggregations. Returned
          only when this aggregation is returned as a subaggregation.
    """

    def __init__(self,
                 key: str,
                 matching_results: int,
                 *,
                 relevancy: float = None,
                 total_matching_documents: int = None,
                 estimated_matching_results: float = None,
                 aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryGroupByAggregationResult object.

        :param str key: The condition that is met by the documents in this group.
               For example, `YEARTXT<2000`.
        :param int matching_results: Number of documents that meet the query and
               condition.
        :param float relevancy: (optional) The relevancy for this group. Returned
               only if `relevancy:true` is specified in the request.
        :param int total_matching_documents: (optional) Number of documents that
               meet the condition in the whole set of documents in this collection.
               Returned only when `relevancy:true` is specified in the request.
        :param float estimated_matching_results: (optional) The number of documents
               that are estimated to match the query and condition. Returned only when
               `relevancy:true` is specified in the request.
        :param List[dict] aggregations: (optional) An array of subaggregations.
               Returned only when this aggregation is returned as a subaggregation.
        """
        self.key = key
        self.matching_results = matching_results
        self.relevancy = relevancy
        self.total_matching_documents = total_matching_documents
        self.estimated_matching_results = estimated_matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryGroupByAggregationResult':
        """Initialize a QueryGroupByAggregationResult object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError(
                'Required property \'key\' not present in QueryGroupByAggregationResult JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryGroupByAggregationResult JSON'
            )
        if 'relevancy' in _dict:
            args['relevancy'] = _dict.get('relevancy')
        if 'total_matching_documents' in _dict:
            args['total_matching_documents'] = _dict.get(
                'total_matching_documents')
        if 'estimated_matching_results' in _dict:
            args['estimated_matching_results'] = _dict.get(
                'estimated_matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryGroupByAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'relevancy') and self.relevancy is not None:
            _dict['relevancy'] = self.relevancy
        if hasattr(self, 'total_matching_documents'
                  ) and self.total_matching_documents is not None:
            _dict['total_matching_documents'] = self.total_matching_documents
        if hasattr(self, 'estimated_matching_results'
                  ) and self.estimated_matching_results is not None:
            _dict[
                'estimated_matching_results'] = self.estimated_matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryGroupByAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryGroupByAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryGroupByAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryHistogramAggregationResult():
    """
    Histogram numeric interval result.

    :attr int key: The value of the upper bound for the numeric segment.
    :attr int matching_results: Number of documents with the specified key as the
          upper bound.
    :attr List[dict] aggregations: (optional) An array of subaggregations. Returned
          only when this aggregation is returned as a subaggregation.
    """

    def __init__(self,
                 key: int,
                 matching_results: int,
                 *,
                 aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryHistogramAggregationResult object.

        :param int key: The value of the upper bound for the numeric segment.
        :param int matching_results: Number of documents with the specified key as
               the upper bound.
        :param List[dict] aggregations: (optional) An array of subaggregations.
               Returned only when this aggregation is returned as a subaggregation.
        """
        self.key = key
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryHistogramAggregationResult':
        """Initialize a QueryHistogramAggregationResult object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError(
                'Required property \'key\' not present in QueryHistogramAggregationResult JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryHistogramAggregationResult JSON'
            )
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryHistogramAggregationResult object from a json dictionary."""
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
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryHistogramAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryHistogramAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryHistogramAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryLargePassages():
    """
    Configuration for passage retrieval.

    :attr bool enabled: (optional) A passages query that returns the most relevant
          passages from the results.
    :attr bool per_document: (optional) If `true`, ranks the documents by document
          quality, and then returns the highest-ranked passages per document in a
          `document_passages` field for each document entry in the results list of the
          response.
          If `false`, ranks the passages from all of the documents by passage quality
          regardless of the document quality and returns them in a separate `passages`
          field in the response.
    :attr int max_per_document: (optional) Maximum number of passages to return per
          document in the result. Ignored if **passages.per_document** is `false`.
    :attr List[str] fields: (optional) A list of fields to extract passages from. By
          default, passages are extracted from the `text` and `title` fields only. If you
          add this parameter and specify an empty list (`[]`) as its value, then the
          service searches all root-level fields for suitable passages.
    :attr int count: (optional) The maximum number of passages to return. Ignored if
          **passages.per_document** is `true`.
    :attr int characters: (optional) The approximate number of characters that any
          one passage will have.
    :attr bool find_answers: (optional) When true, `answer` objects are returned as
          part of each passage in the query results. The primary difference between an
          `answer` and a `passage` is that the length of a passage is defined by the
          query, where the length of an `answer` is calculated by Discovery based on how
          much text is needed to answer the question.
          This parameter is ignored if passages are not enabled for the query, or no
          **natural_language_query** is specified.
          If the **find_answers** parameter is set to `true` and **per_document**
          parameter is also set to `true`, then the document search results and the
          passage search results within each document are reordered using the answer
          confidences. The goal of this reordering is to place the best answer as the
          first answer of the first passage of the first document. Similarly, if the
          **find_answers** parameter is set to `true` and **per_document** parameter is
          set to `false`, then the passage search results are reordered in decreasing
          order of the highest confidence answer for each document and passage.
          The **find_answers** parameter is available only on managed instances of
          Discovery.
    :attr int max_answers_per_passage: (optional) The number of `answer` objects to
          return per passage if the **find_answers** parmeter is specified as `true`.
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 per_document: bool = None,
                 max_per_document: int = None,
                 fields: List[str] = None,
                 count: int = None,
                 characters: int = None,
                 find_answers: bool = None,
                 max_answers_per_passage: int = None) -> None:
        """
        Initialize a QueryLargePassages object.

        :param bool enabled: (optional) A passages query that returns the most
               relevant passages from the results.
        :param bool per_document: (optional) If `true`, ranks the documents by
               document quality, and then returns the highest-ranked passages per document
               in a `document_passages` field for each document entry in the results list
               of the response.
               If `false`, ranks the passages from all of the documents by passage quality
               regardless of the document quality and returns them in a separate
               `passages` field in the response.
        :param int max_per_document: (optional) Maximum number of passages to
               return per document in the result. Ignored if **passages.per_document** is
               `false`.
        :param List[str] fields: (optional) A list of fields to extract passages
               from. By default, passages are extracted from the `text` and `title` fields
               only. If you add this parameter and specify an empty list (`[]`) as its
               value, then the service searches all root-level fields for suitable
               passages.
        :param int count: (optional) The maximum number of passages to return.
               Ignored if **passages.per_document** is `true`.
        :param int characters: (optional) The approximate number of characters that
               any one passage will have.
        :param bool find_answers: (optional) When true, `answer` objects are
               returned as part of each passage in the query results. The primary
               difference between an `answer` and a `passage` is that the length of a
               passage is defined by the query, where the length of an `answer` is
               calculated by Discovery based on how much text is needed to answer the
               question.
               This parameter is ignored if passages are not enabled for the query, or no
               **natural_language_query** is specified.
               If the **find_answers** parameter is set to `true` and **per_document**
               parameter is also set to `true`, then the document search results and the
               passage search results within each document are reordered using the answer
               confidences. The goal of this reordering is to place the best answer as the
               first answer of the first passage of the first document. Similarly, if the
               **find_answers** parameter is set to `true` and **per_document** parameter
               is set to `false`, then the passage search results are reordered in
               decreasing order of the highest confidence answer for each document and
               passage.
               The **find_answers** parameter is available only on managed instances of
               Discovery.
        :param int max_answers_per_passage: (optional) The number of `answer`
               objects to return per passage if the **find_answers** parmeter is specified
               as `true`.
        """
        self.enabled = enabled
        self.per_document = per_document
        self.max_per_document = max_per_document
        self.fields = fields
        self.count = count
        self.characters = characters
        self.find_answers = find_answers
        self.max_answers_per_passage = max_answers_per_passage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryLargePassages':
        """Initialize a QueryLargePassages object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'per_document' in _dict:
            args['per_document'] = _dict.get('per_document')
        if 'max_per_document' in _dict:
            args['max_per_document'] = _dict.get('max_per_document')
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'characters' in _dict:
            args['characters'] = _dict.get('characters')
        if 'find_answers' in _dict:
            args['find_answers'] = _dict.get('find_answers')
        if 'max_answers_per_passage' in _dict:
            args['max_answers_per_passage'] = _dict.get(
                'max_answers_per_passage')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryLargePassages object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'per_document') and self.per_document is not None:
            _dict['per_document'] = self.per_document
        if hasattr(self,
                   'max_per_document') and self.max_per_document is not None:
            _dict['max_per_document'] = self.max_per_document
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'characters') and self.characters is not None:
            _dict['characters'] = self.characters
        if hasattr(self, 'find_answers') and self.find_answers is not None:
            _dict['find_answers'] = self.find_answers
        if hasattr(self, 'max_answers_per_passage'
                  ) and self.max_answers_per_passage is not None:
            _dict['max_answers_per_passage'] = self.max_answers_per_passage
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryLargePassages object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryLargePassages') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryLargePassages') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryLargeSimilar():
    """
    Finds results from documents that are similar to documents of interest. Use this
    parameter to add a *More like these* function to your search. You can include this
    parameter with or without a **query**, **filter** or **natural_language_query**
    parameter.

    :attr bool enabled: (optional) When `true`, includes documents in the query
          results that are similar to documents you specify.
    :attr List[str] document_ids: (optional) The list of documents of interest.
          Required if **enabled** is `true`.
    :attr List[str] fields: (optional) Looks for similarities in the specified
          subset of fields in the documents. If not specified, all of the document fields
          are used.
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 document_ids: List[str] = None,
                 fields: List[str] = None) -> None:
        """
        Initialize a QueryLargeSimilar object.

        :param bool enabled: (optional) When `true`, includes documents in the
               query results that are similar to documents you specify.
        :param List[str] document_ids: (optional) The list of documents of
               interest. Required if **enabled** is `true`.
        :param List[str] fields: (optional) Looks for similarities in the specified
               subset of fields in the documents. If not specified, all of the document
               fields are used.
        """
        self.enabled = enabled
        self.document_ids = document_ids
        self.fields = fields

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryLargeSimilar':
        """Initialize a QueryLargeSimilar object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'document_ids' in _dict:
            args['document_ids'] = _dict.get('document_ids')
        if 'fields' in _dict:
            args['fields'] = _dict.get('fields')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryLargeSimilar object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'document_ids') and self.document_ids is not None:
            _dict['document_ids'] = self.document_ids
        if hasattr(self, 'fields') and self.fields is not None:
            _dict['fields'] = self.fields
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryLargeSimilar object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryLargeSimilar') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryLargeSimilar') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryLargeSuggestedRefinements():
    """
    Configuration for suggested refinements.
    **Note**: The **suggested_refinements** parameter that identified dynamic facets from
    the data is deprecated.

    :attr bool enabled: (optional) Whether to perform suggested refinements.
    :attr int count: (optional) Maximum number of suggested refinements texts to be
          returned. The maximum is `100`.
    """

    def __init__(self, *, enabled: bool = None, count: int = None) -> None:
        """
        Initialize a QueryLargeSuggestedRefinements object.

        :param bool enabled: (optional) Whether to perform suggested refinements.
        :param int count: (optional) Maximum number of suggested refinements texts
               to be returned. The maximum is `100`.
        """
        self.enabled = enabled
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryLargeSuggestedRefinements':
        """Initialize a QueryLargeSuggestedRefinements object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryLargeSuggestedRefinements object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryLargeSuggestedRefinements object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryLargeSuggestedRefinements') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryLargeSuggestedRefinements') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryLargeTableResults():
    """
    Configuration for table retrieval.

    :attr bool enabled: (optional) Whether to enable table retrieval.
    :attr int count: (optional) Maximum number of tables to return.
    """

    def __init__(self, *, enabled: bool = None, count: int = None) -> None:
        """
        Initialize a QueryLargeTableResults object.

        :param bool enabled: (optional) Whether to enable table retrieval.
        :param int count: (optional) Maximum number of tables to return.
        """
        self.enabled = enabled
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryLargeTableResults':
        """Initialize a QueryLargeTableResults object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryLargeTableResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryLargeTableResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryLargeTableResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryLargeTableResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryNoticesResponse():
    """
    Object that contains notice query results.

    :attr int matching_results: (optional) The number of matching results.
    :attr List[Notice] notices: (optional) Array of document results that match the
          query.
    """

    def __init__(self,
                 *,
                 matching_results: int = None,
                 notices: List['Notice'] = None) -> None:
        """
        Initialize a QueryNoticesResponse object.

        :param int matching_results: (optional) The number of matching results.
        :param List[Notice] notices: (optional) Array of document results that
               match the query.
        """
        self.matching_results = matching_results
        self.notices = notices

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryNoticesResponse':
        """Initialize a QueryNoticesResponse object from a json dictionary."""
        args = {}
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'notices' in _dict:
            args['notices'] = [
                Notice.from_dict(v) for v in _dict.get('notices')
            ]
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
        if hasattr(self, 'notices') and self.notices is not None:
            notices_list = []
            for v in self.notices:
                if isinstance(v, dict):
                    notices_list.append(v)
                else:
                    notices_list.append(v.to_dict())
            _dict['notices'] = notices_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryNoticesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryNoticesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryNoticesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryPairAggregationResult():
    """
    Result for the `pair` aggregation.

    :attr List[dict] aggregations: (optional) Array of subaggregations of type
          `term`, `group_by`, `histogram`, or `timeslice`. Each element of the matrix that
          is returned contains a **relevancy** value that is calculated from the
          combination of each value from the first and second aggregations.
    """

    def __init__(self, *, aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryPairAggregationResult object.

        :param List[dict] aggregations: (optional) Array of subaggregations of type
               `term`, `group_by`, `histogram`, or `timeslice`. Each element of the matrix
               that is returned contains a **relevancy** value that is calculated from the
               combination of each value from the first and second aggregations.
        """
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryPairAggregationResult':
        """Initialize a QueryPairAggregationResult object from a json dictionary."""
        args = {}
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryPairAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryPairAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryPairAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryPairAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResponse():
    """
    A response that contains the documents and aggregations for the query.

    :attr int matching_results: (optional) The number of matching results for the
          query. Results that match due to a curation only are not counted in the total.
    :attr List[QueryResult] results: (optional) Array of document results for the
          query.
    :attr List[QueryAggregation] aggregations: (optional) Array of aggregations for
          the query.
    :attr RetrievalDetails retrieval_details: (optional) An object contain retrieval
          type information.
    :attr str suggested_query: (optional) Suggested correction to the submitted
          **natural_language_query** value.
    :attr List[QuerySuggestedRefinement] suggested_refinements: (optional)
          Deprecated: Array of suggested refinements. **Note**: The
          `suggested_refinements` parameter that identified dynamic facets from the data
          is deprecated.
    :attr List[QueryTableResult] table_results: (optional) Array of table results.
    :attr List[QueryResponsePassage] passages: (optional) Passages that best match
          the query from across all of the collections in the project. Returned if
          **passages.per_document** is `false`.
    """

    def __init__(self,
                 *,
                 matching_results: int = None,
                 results: List['QueryResult'] = None,
                 aggregations: List['QueryAggregation'] = None,
                 retrieval_details: 'RetrievalDetails' = None,
                 suggested_query: str = None,
                 suggested_refinements: List['QuerySuggestedRefinement'] = None,
                 table_results: List['QueryTableResult'] = None,
                 passages: List['QueryResponsePassage'] = None) -> None:
        """
        Initialize a QueryResponse object.

        :param int matching_results: (optional) The number of matching results for
               the query. Results that match due to a curation only are not counted in the
               total.
        :param List[QueryResult] results: (optional) Array of document results for
               the query.
        :param List[QueryAggregation] aggregations: (optional) Array of
               aggregations for the query.
        :param RetrievalDetails retrieval_details: (optional) An object contain
               retrieval type information.
        :param str suggested_query: (optional) Suggested correction to the
               submitted **natural_language_query** value.
        :param List[QuerySuggestedRefinement] suggested_refinements: (optional)
               Deprecated: Array of suggested refinements. **Note**: The
               `suggested_refinements` parameter that identified dynamic facets from the
               data is deprecated.
        :param List[QueryTableResult] table_results: (optional) Array of table
               results.
        :param List[QueryResponsePassage] passages: (optional) Passages that best
               match the query from across all of the collections in the project. Returned
               if **passages.per_document** is `false`.
        """
        self.matching_results = matching_results
        self.results = results
        self.aggregations = aggregations
        self.retrieval_details = retrieval_details
        self.suggested_query = suggested_query
        self.suggested_refinements = suggested_refinements
        self.table_results = table_results
        self.passages = passages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResponse':
        """Initialize a QueryResponse object from a json dictionary."""
        args = {}
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'results' in _dict:
            args['results'] = [
                QueryResult.from_dict(v) for v in _dict.get('results')
            ]
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation.from_dict(v) for v in _dict.get('aggregations')
            ]
        if 'retrieval_details' in _dict:
            args['retrieval_details'] = RetrievalDetails.from_dict(
                _dict.get('retrieval_details'))
        if 'suggested_query' in _dict:
            args['suggested_query'] = _dict.get('suggested_query')
        if 'suggested_refinements' in _dict:
            args['suggested_refinements'] = [
                QuerySuggestedRefinement.from_dict(v)
                for v in _dict.get('suggested_refinements')
            ]
        if 'table_results' in _dict:
            args['table_results'] = [
                QueryTableResult.from_dict(v)
                for v in _dict.get('table_results')
            ]
        if 'passages' in _dict:
            args['passages'] = [
                QueryResponsePassage.from_dict(v) for v in _dict.get('passages')
            ]
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
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            aggregations_list = []
            for v in self.aggregations:
                if isinstance(v, dict):
                    aggregations_list.append(v)
                else:
                    aggregations_list.append(v.to_dict())
            _dict['aggregations'] = aggregations_list
        if hasattr(self,
                   'retrieval_details') and self.retrieval_details is not None:
            if isinstance(self.retrieval_details, dict):
                _dict['retrieval_details'] = self.retrieval_details
            else:
                _dict['retrieval_details'] = self.retrieval_details.to_dict()
        if hasattr(self,
                   'suggested_query') and self.suggested_query is not None:
            _dict['suggested_query'] = self.suggested_query
        if hasattr(self, 'suggested_refinements'
                  ) and self.suggested_refinements is not None:
            suggested_refinements_list = []
            for v in self.suggested_refinements:
                if isinstance(v, dict):
                    suggested_refinements_list.append(v)
                else:
                    suggested_refinements_list.append(v.to_dict())
            _dict['suggested_refinements'] = suggested_refinements_list
        if hasattr(self, 'table_results') and self.table_results is not None:
            table_results_list = []
            for v in self.table_results:
                if isinstance(v, dict):
                    table_results_list.append(v)
                else:
                    table_results_list.append(v.to_dict())
            _dict['table_results'] = table_results_list
        if hasattr(self, 'passages') and self.passages is not None:
            passages_list = []
            for v in self.passages:
                if isinstance(v, dict):
                    passages_list.append(v)
                else:
                    passages_list.append(v.to_dict())
            _dict['passages'] = passages_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResponsePassage():
    """
    A passage query response.

    :attr str passage_text: (optional) The content of the extracted passage.
    :attr float passage_score: (optional) The confidence score of the passage's
          analysis. A higher score indicates greater confidence. The score is used to rank
          the passages from all documents and is returned only if
          **passages.per_document** is `false`.
    :attr str document_id: (optional) The unique identifier of the ingested
          document.
    :attr str collection_id: (optional) The unique identifier of the collection.
    :attr int start_offset: (optional) The position of the first character of the
          extracted passage in the originating field.
    :attr int end_offset: (optional) The position after the last character of the
          extracted passage in the originating field.
    :attr str field: (optional) The label of the field from which the passage has
          been extracted.
    :attr List[ResultPassageAnswer] answers: (optional) An array of extracted
          answers to the specified query. Returned for natural language queries when
          **passages.per_document** is `false`.
    """

    def __init__(self,
                 *,
                 passage_text: str = None,
                 passage_score: float = None,
                 document_id: str = None,
                 collection_id: str = None,
                 start_offset: int = None,
                 end_offset: int = None,
                 field: str = None,
                 answers: List['ResultPassageAnswer'] = None) -> None:
        """
        Initialize a QueryResponsePassage object.

        :param str passage_text: (optional) The content of the extracted passage.
        :param float passage_score: (optional) The confidence score of the
               passage's analysis. A higher score indicates greater confidence. The score
               is used to rank the passages from all documents and is returned only if
               **passages.per_document** is `false`.
        :param str document_id: (optional) The unique identifier of the ingested
               document.
        :param str collection_id: (optional) The unique identifier of the
               collection.
        :param int start_offset: (optional) The position of the first character of
               the extracted passage in the originating field.
        :param int end_offset: (optional) The position after the last character of
               the extracted passage in the originating field.
        :param str field: (optional) The label of the field from which the passage
               has been extracted.
        :param List[ResultPassageAnswer] answers: (optional) An array of extracted
               answers to the specified query. Returned for natural language queries when
               **passages.per_document** is `false`.
        """
        self.passage_text = passage_text
        self.passage_score = passage_score
        self.document_id = document_id
        self.collection_id = collection_id
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.field = field
        self.answers = answers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResponsePassage':
        """Initialize a QueryResponsePassage object from a json dictionary."""
        args = {}
        if 'passage_text' in _dict:
            args['passage_text'] = _dict.get('passage_text')
        if 'passage_score' in _dict:
            args['passage_score'] = _dict.get('passage_score')
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'start_offset' in _dict:
            args['start_offset'] = _dict.get('start_offset')
        if 'end_offset' in _dict:
            args['end_offset'] = _dict.get('end_offset')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'answers' in _dict:
            args['answers'] = [
                ResultPassageAnswer.from_dict(v) for v in _dict.get('answers')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResponsePassage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'passage_text') and self.passage_text is not None:
            _dict['passage_text'] = self.passage_text
        if hasattr(self, 'passage_score') and self.passage_score is not None:
            _dict['passage_score'] = self.passage_score
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'start_offset') and self.start_offset is not None:
            _dict['start_offset'] = self.start_offset
        if hasattr(self, 'end_offset') and self.end_offset is not None:
            _dict['end_offset'] = self.end_offset
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'answers') and self.answers is not None:
            answers_list = []
            for v in self.answers:
                if isinstance(v, dict):
                    answers_list.append(v)
                else:
                    answers_list.append(v.to_dict())
            _dict['answers'] = answers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryResponsePassage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryResponsePassage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryResponsePassage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryResult():
    """
    Result document for the specified query.

    :attr str document_id: The unique identifier of the document.
    :attr dict metadata: (optional) Metadata of the document.
    :attr QueryResultMetadata result_metadata: Metadata of a query result.
    :attr List[QueryResultPassage] document_passages: (optional) Passages from the
          document that best matches the query. Returned if **passages.per_document** is
          `true`.
    """

    # The set of defined properties for the class
    _properties = frozenset(
        ['document_id', 'metadata', 'result_metadata', 'document_passages'])

    def __init__(self,
                 document_id: str,
                 result_metadata: 'QueryResultMetadata',
                 *,
                 metadata: dict = None,
                 document_passages: List['QueryResultPassage'] = None,
                 **kwargs) -> None:
        """
        Initialize a QueryResult object.

        :param str document_id: The unique identifier of the document.
        :param QueryResultMetadata result_metadata: Metadata of a query result.
        :param dict metadata: (optional) Metadata of the document.
        :param List[QueryResultPassage] document_passages: (optional) Passages from
               the document that best matches the query. Returned if
               **passages.per_document** is `true`.
        :param **kwargs: (optional) Any additional properties.
        """
        self.document_id = document_id
        self.metadata = metadata
        self.result_metadata = result_metadata
        self.document_passages = document_passages
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResult':
        """Initialize a QueryResult object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        else:
            raise ValueError(
                'Required property \'document_id\' not present in QueryResult JSON'
            )
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'result_metadata' in _dict:
            args['result_metadata'] = QueryResultMetadata.from_dict(
                _dict.get('result_metadata'))
        else:
            raise ValueError(
                'Required property \'result_metadata\' not present in QueryResult JSON'
            )
        if 'document_passages' in _dict:
            args['document_passages'] = [
                QueryResultPassage.from_dict(v)
                for v in _dict.get('document_passages')
            ]
        args.update(
            {k: v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self,
                   'result_metadata') and self.result_metadata is not None:
            if isinstance(self.result_metadata, dict):
                _dict['result_metadata'] = self.result_metadata
            else:
                _dict['result_metadata'] = self.result_metadata.to_dict()
        if hasattr(self,
                   'document_passages') and self.document_passages is not None:
            document_passages_list = []
            for v in self.document_passages:
                if isinstance(v, dict):
                    document_passages_list.append(v)
                else:
                    document_passages_list.append(v.to_dict())
            _dict['document_passages'] = document_passages_list
        for _key in [
                k for k in vars(self).keys() if k not in QueryResult._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of QueryResult"""
        _dict = {}

        for _key in [
                k for k in vars(self).keys() if k not in QueryResult._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of QueryResult"""
        for _key in [
                k for k in vars(self).keys() if k not in QueryResult._properties
        ]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in QueryResult._properties:
                setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this QueryResult object."""
        return json.dumps(self.to_dict(), indent=2)

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

    :attr str document_retrieval_source: (optional) The document retrieval source
          that produced this search result.
    :attr str collection_id: The collection id associated with this training data
          set.
    :attr float confidence: (optional) The confidence score for the given result.
          Calculated based on how relevant the result is estimated to be. The score can
          range from `0.0` to `1.0`. The higher the number, the more relevant the
          document. The `confidence` value for a result was calculated using the model
          specified in the `document_retrieval_strategy` field of the result set. This
          field is returned only if the **natural_language_query** parameter is specified
          in the query.
    """

    def __init__(self,
                 collection_id: str,
                 *,
                 document_retrieval_source: str = None,
                 confidence: float = None) -> None:
        """
        Initialize a QueryResultMetadata object.

        :param str collection_id: The collection id associated with this training
               data set.
        :param str document_retrieval_source: (optional) The document retrieval
               source that produced this search result.
        :param float confidence: (optional) The confidence score for the given
               result. Calculated based on how relevant the result is estimated to be. The
               score can range from `0.0` to `1.0`. The higher the number, the more
               relevant the document. The `confidence` value for a result was calculated
               using the model specified in the `document_retrieval_strategy` field of the
               result set. This field is returned only if the **natural_language_query**
               parameter is specified in the query.
        """
        self.document_retrieval_source = document_retrieval_source
        self.collection_id = collection_id
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResultMetadata':
        """Initialize a QueryResultMetadata object from a json dictionary."""
        args = {}
        if 'document_retrieval_source' in _dict:
            args['document_retrieval_source'] = _dict.get(
                'document_retrieval_source')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        else:
            raise ValueError(
                'Required property \'collection_id\' not present in QueryResultMetadata JSON'
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
        if hasattr(self, 'document_retrieval_source'
                  ) and self.document_retrieval_source is not None:
            _dict['document_retrieval_source'] = self.document_retrieval_source
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryResultMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryResultMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryResultMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DocumentRetrievalSourceEnum(str, Enum):
        """
        The document retrieval source that produced this search result.
        """
        SEARCH = 'search'
        CURATION = 'curation'


class QueryResultPassage():
    """
    A passage query result.

    :attr str passage_text: (optional) The content of the extracted passage.
    :attr int start_offset: (optional) The position of the first character of the
          extracted passage in the originating field.
    :attr int end_offset: (optional) The position after the last character of the
          extracted passage in the originating field.
    :attr str field: (optional) The label of the field from which the passage has
          been extracted.
    :attr List[ResultPassageAnswer] answers: (optional) An arry of extracted answers
          to the specified query. Returned for natural language queries when
          **passages.per_document** is `true`.
    """

    def __init__(self,
                 *,
                 passage_text: str = None,
                 start_offset: int = None,
                 end_offset: int = None,
                 field: str = None,
                 answers: List['ResultPassageAnswer'] = None) -> None:
        """
        Initialize a QueryResultPassage object.

        :param str passage_text: (optional) The content of the extracted passage.
        :param int start_offset: (optional) The position of the first character of
               the extracted passage in the originating field.
        :param int end_offset: (optional) The position after the last character of
               the extracted passage in the originating field.
        :param str field: (optional) The label of the field from which the passage
               has been extracted.
        :param List[ResultPassageAnswer] answers: (optional) An arry of extracted
               answers to the specified query. Returned for natural language queries when
               **passages.per_document** is `true`.
        """
        self.passage_text = passage_text
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.field = field
        self.answers = answers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryResultPassage':
        """Initialize a QueryResultPassage object from a json dictionary."""
        args = {}
        if 'passage_text' in _dict:
            args['passage_text'] = _dict.get('passage_text')
        if 'start_offset' in _dict:
            args['start_offset'] = _dict.get('start_offset')
        if 'end_offset' in _dict:
            args['end_offset'] = _dict.get('end_offset')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'answers' in _dict:
            args['answers'] = [
                ResultPassageAnswer.from_dict(v) for v in _dict.get('answers')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResultPassage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'passage_text') and self.passage_text is not None:
            _dict['passage_text'] = self.passage_text
        if hasattr(self, 'start_offset') and self.start_offset is not None:
            _dict['start_offset'] = self.start_offset
        if hasattr(self, 'end_offset') and self.end_offset is not None:
            _dict['end_offset'] = self.end_offset
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'answers') and self.answers is not None:
            answers_list = []
            for v in self.answers:
                if isinstance(v, dict):
                    answers_list.append(v)
                else:
                    answers_list.append(v.to_dict())
            _dict['answers'] = answers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryResultPassage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryResultPassage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryResultPassage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QuerySuggestedRefinement():
    """
    A suggested additional query term or terms user to filter results. **Note**: The
    `suggested_refinements` parameter is deprecated.

    :attr str text: (optional) The text used to filter.
    """

    def __init__(self, *, text: str = None) -> None:
        """
        Initialize a QuerySuggestedRefinement object.

        :param str text: (optional) The text used to filter.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QuerySuggestedRefinement':
        """Initialize a QuerySuggestedRefinement object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QuerySuggestedRefinement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QuerySuggestedRefinement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QuerySuggestedRefinement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QuerySuggestedRefinement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTableResult():
    """
    A tables whose content or context match a search query.

    :attr str table_id: (optional) The identifier for the retrieved table.
    :attr str source_document_id: (optional) The identifier of the document the
          table was retrieved from.
    :attr str collection_id: (optional) The identifier of the collection the table
          was retrieved from.
    :attr str table_html: (optional) HTML snippet of the table info.
    :attr int table_html_offset: (optional) The offset of the table html snippet in
          the original document html.
    :attr TableResultTable table: (optional) Full table object retrieved from Table
          Understanding Enrichment.
    """

    def __init__(self,
                 *,
                 table_id: str = None,
                 source_document_id: str = None,
                 collection_id: str = None,
                 table_html: str = None,
                 table_html_offset: int = None,
                 table: 'TableResultTable' = None) -> None:
        """
        Initialize a QueryTableResult object.

        :param str table_id: (optional) The identifier for the retrieved table.
        :param str source_document_id: (optional) The identifier of the document
               the table was retrieved from.
        :param str collection_id: (optional) The identifier of the collection the
               table was retrieved from.
        :param str table_html: (optional) HTML snippet of the table info.
        :param int table_html_offset: (optional) The offset of the table html
               snippet in the original document html.
        :param TableResultTable table: (optional) Full table object retrieved from
               Table Understanding Enrichment.
        """
        self.table_id = table_id
        self.source_document_id = source_document_id
        self.collection_id = collection_id
        self.table_html = table_html
        self.table_html_offset = table_html_offset
        self.table = table

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryTableResult':
        """Initialize a QueryTableResult object from a json dictionary."""
        args = {}
        if 'table_id' in _dict:
            args['table_id'] = _dict.get('table_id')
        if 'source_document_id' in _dict:
            args['source_document_id'] = _dict.get('source_document_id')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'table_html' in _dict:
            args['table_html'] = _dict.get('table_html')
        if 'table_html_offset' in _dict:
            args['table_html_offset'] = _dict.get('table_html_offset')
        if 'table' in _dict:
            args['table'] = TableResultTable.from_dict(_dict.get('table'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTableResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'table_id') and self.table_id is not None:
            _dict['table_id'] = self.table_id
        if hasattr(
                self,
                'source_document_id') and self.source_document_id is not None:
            _dict['source_document_id'] = self.source_document_id
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'table_html') and self.table_html is not None:
            _dict['table_html'] = self.table_html
        if hasattr(self,
                   'table_html_offset') and self.table_html_offset is not None:
            _dict['table_html_offset'] = self.table_html_offset
        if hasattr(self, 'table') and self.table is not None:
            if isinstance(self.table, dict):
                _dict['table'] = self.table
            else:
                _dict['table'] = self.table.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryTableResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryTableResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryTableResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTermAggregationResult():
    """
    Top value result for the `term` aggregation.

    :attr str key: Value of the field with a nonzero frequency in the document set.
    :attr int matching_results: Number of documents that contain the 'key'.
    :attr float relevancy: (optional) The relevancy score for this result. Returned
          only if `relevancy:true` is specified in the request.
    :attr int total_matching_documents: (optional) Number of documents in the
          collection that contain the term in the specified field. Returned only when
          `relevancy:true` is specified in the request.
    :attr float estimated_matching_results: (optional) Number of documents that are
          estimated to match the query and also meet the condition. Returned only when
          `relevancy:true` is specified in the request.
    :attr List[dict] aggregations: (optional) An array of subaggregations. Returned
          only when this aggregation is combined with other aggregations in the request or
          is returned as a subaggregation.
    """

    def __init__(self,
                 key: str,
                 matching_results: int,
                 *,
                 relevancy: float = None,
                 total_matching_documents: int = None,
                 estimated_matching_results: float = None,
                 aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryTermAggregationResult object.

        :param str key: Value of the field with a nonzero frequency in the document
               set.
        :param int matching_results: Number of documents that contain the 'key'.
        :param float relevancy: (optional) The relevancy score for this result.
               Returned only if `relevancy:true` is specified in the request.
        :param int total_matching_documents: (optional) Number of documents in the
               collection that contain the term in the specified field. Returned only when
               `relevancy:true` is specified in the request.
        :param float estimated_matching_results: (optional) Number of documents
               that are estimated to match the query and also meet the condition. Returned
               only when `relevancy:true` is specified in the request.
        :param List[dict] aggregations: (optional) An array of subaggregations.
               Returned only when this aggregation is combined with other aggregations in
               the request or is returned as a subaggregation.
        """
        self.key = key
        self.matching_results = matching_results
        self.relevancy = relevancy
        self.total_matching_documents = total_matching_documents
        self.estimated_matching_results = estimated_matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryTermAggregationResult':
        """Initialize a QueryTermAggregationResult object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError(
                'Required property \'key\' not present in QueryTermAggregationResult JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryTermAggregationResult JSON'
            )
        if 'relevancy' in _dict:
            args['relevancy'] = _dict.get('relevancy')
        if 'total_matching_documents' in _dict:
            args['total_matching_documents'] = _dict.get(
                'total_matching_documents')
        if 'estimated_matching_results' in _dict:
            args['estimated_matching_results'] = _dict.get(
                'estimated_matching_results')
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTermAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'relevancy') and self.relevancy is not None:
            _dict['relevancy'] = self.relevancy
        if hasattr(self, 'total_matching_documents'
                  ) and self.total_matching_documents is not None:
            _dict['total_matching_documents'] = self.total_matching_documents
        if hasattr(self, 'estimated_matching_results'
                  ) and self.estimated_matching_results is not None:
            _dict[
                'estimated_matching_results'] = self.estimated_matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryTermAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryTermAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryTermAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTimesliceAggregationResult():
    """
    A timeslice interval segment.

    :attr str key_as_string: String date value of the upper bound for the timeslice
          interval in ISO-8601 format.
    :attr int key: Numeric date value of the upper bound for the timeslice interval
          in UNIX milliseconds since epoch.
    :attr int matching_results: Number of documents with the specified key as the
          upper bound.
    :attr List[dict] aggregations: (optional) An array of subaggregations. Returned
          only when this aggregation is returned as a subaggregation.
    """

    def __init__(self,
                 key_as_string: str,
                 key: int,
                 matching_results: int,
                 *,
                 aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryTimesliceAggregationResult object.

        :param str key_as_string: String date value of the upper bound for the
               timeslice interval in ISO-8601 format.
        :param int key: Numeric date value of the upper bound for the timeslice
               interval in UNIX milliseconds since epoch.
        :param int matching_results: Number of documents with the specified key as
               the upper bound.
        :param List[dict] aggregations: (optional) An array of subaggregations.
               Returned only when this aggregation is returned as a subaggregation.
        """
        self.key_as_string = key_as_string
        self.key = key
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryTimesliceAggregationResult':
        """Initialize a QueryTimesliceAggregationResult object from a json dictionary."""
        args = {}
        if 'key_as_string' in _dict:
            args['key_as_string'] = _dict.get('key_as_string')
        else:
            raise ValueError(
                'Required property \'key_as_string\' not present in QueryTimesliceAggregationResult JSON'
            )
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        else:
            raise ValueError(
                'Required property \'key\' not present in QueryTimesliceAggregationResult JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryTimesliceAggregationResult JSON'
            )
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTimesliceAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key_as_string') and self.key_as_string is not None:
            _dict['key_as_string'] = self.key_as_string
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryTimesliceAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryTimesliceAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryTimesliceAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTopHitsAggregationResult():
    """
    A query response that contains the matching documents for the preceding aggregations.

    :attr int matching_results: Number of matching results.
    :attr List[dict] hits: (optional) An array of the document results in an ordered
          list.
    """

    def __init__(self,
                 matching_results: int,
                 *,
                 hits: List[dict] = None) -> None:
        """
        Initialize a QueryTopHitsAggregationResult object.

        :param int matching_results: Number of matching results.
        :param List[dict] hits: (optional) An array of the document results in an
               ordered list.
        """
        self.matching_results = matching_results
        self.hits = hits

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryTopHitsAggregationResult':
        """Initialize a QueryTopHitsAggregationResult object from a json dictionary."""
        args = {}
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryTopHitsAggregationResult JSON'
            )
        if 'hits' in _dict:
            args['hits'] = _dict.get('hits')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTopHitsAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'hits') and self.hits is not None:
            _dict['hits'] = self.hits
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryTopHitsAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryTopHitsAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryTopHitsAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTopicAggregationResult():
    """
    Result for the `topic` aggregation.

    :attr List[dict] aggregations: (optional) Array of subaggregations  of type
          `term` or `group_by` and `timeslice`. Each element of the matrix that is
          returned contains a **topic_indicator** that is calculated from the combination
          of each aggregation value and segment of time.
    """

    def __init__(self, *, aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryTopicAggregationResult object.

        :param List[dict] aggregations: (optional) Array of subaggregations  of
               type `term` or `group_by` and `timeslice`. Each element of the matrix that
               is returned contains a **topic_indicator** that is calculated from the
               combination of each aggregation value and segment of time.
        """
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryTopicAggregationResult':
        """Initialize a QueryTopicAggregationResult object from a json dictionary."""
        args = {}
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTopicAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryTopicAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryTopicAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryTopicAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTrendAggregationResult():
    """
    Result for the `trend` aggregation.

    :attr List[dict] aggregations: (optional) Array of subaggregations of type
          `term` or `group_by` and `timeslice`. Each element of the matrix that is
          returned contains a **trend_indicator** that is calculated from the combination
          of each aggregation value and segment of time.
    """

    def __init__(self, *, aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryTrendAggregationResult object.

        :param List[dict] aggregations: (optional) Array of subaggregations of type
               `term` or `group_by` and `timeslice`. Each element of the matrix that is
               returned contains a **trend_indicator** that is calculated from the
               combination of each aggregation value and segment of time.
        """
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryTrendAggregationResult':
        """Initialize a QueryTrendAggregationResult object from a json dictionary."""
        args = {}
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTrendAggregationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryTrendAggregationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryTrendAggregationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryTrendAggregationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResultPassageAnswer():
    """
    Object that contains a potential answer to the specified query.

    :attr str answer_text: (optional) Answer text for the specified query as
          identified by Discovery.
    :attr int start_offset: (optional) The position of the first character of the
          extracted answer in the originating field.
    :attr int end_offset: (optional) The position after the last character of the
          extracted answer in the originating field.
    :attr float confidence: (optional) An estimate of the probability that the
          answer is relevant.
    """

    def __init__(self,
                 *,
                 answer_text: str = None,
                 start_offset: int = None,
                 end_offset: int = None,
                 confidence: float = None) -> None:
        """
        Initialize a ResultPassageAnswer object.

        :param str answer_text: (optional) Answer text for the specified query as
               identified by Discovery.
        :param int start_offset: (optional) The position of the first character of
               the extracted answer in the originating field.
        :param int end_offset: (optional) The position after the last character of
               the extracted answer in the originating field.
        :param float confidence: (optional) An estimate of the probability that the
               answer is relevant.
        """
        self.answer_text = answer_text
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultPassageAnswer':
        """Initialize a ResultPassageAnswer object from a json dictionary."""
        args = {}
        if 'answer_text' in _dict:
            args['answer_text'] = _dict.get('answer_text')
        if 'start_offset' in _dict:
            args['start_offset'] = _dict.get('start_offset')
        if 'end_offset' in _dict:
            args['end_offset'] = _dict.get('end_offset')
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultPassageAnswer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'answer_text') and self.answer_text is not None:
            _dict['answer_text'] = self.answer_text
        if hasattr(self, 'start_offset') and self.start_offset is not None:
            _dict['start_offset'] = self.start_offset
        if hasattr(self, 'end_offset') and self.end_offset is not None:
            _dict['end_offset'] = self.end_offset
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResultPassageAnswer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultPassageAnswer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultPassageAnswer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RetrievalDetails():
    """
    An object contain retrieval type information.

    :attr str document_retrieval_strategy: (optional) Identifies the document
          retrieval strategy used for this query. `relevancy_training` indicates that the
          results were returned using a relevancy trained model.
          **Note**: In the event of trained collections being queried, but the trained
          model is not used to return results, the **document_retrieval_strategy** is
          listed as `untrained`.
    """

    def __init__(self, *, document_retrieval_strategy: str = None) -> None:
        """
        Initialize a RetrievalDetails object.

        :param str document_retrieval_strategy: (optional) Identifies the document
               retrieval strategy used for this query. `relevancy_training` indicates that
               the results were returned using a relevancy trained model.
               **Note**: In the event of trained collections being queried, but the
               trained model is not used to return results, the
               **document_retrieval_strategy** is listed as `untrained`.
        """
        self.document_retrieval_strategy = document_retrieval_strategy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RetrievalDetails':
        """Initialize a RetrievalDetails object from a json dictionary."""
        args = {}
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
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RetrievalDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RetrievalDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DocumentRetrievalStrategyEnum(str, Enum):
        """
        Identifies the document retrieval strategy used for this query.
        `relevancy_training` indicates that the results were returned using a relevancy
        trained model.
        **Note**: In the event of trained collections being queried, but the trained model
        is not used to return results, the **document_retrieval_strategy** is listed as
        `untrained`.
        """
        UNTRAINED = 'untrained'
        RELEVANCY_TRAINING = 'relevancy_training'


class StopWordList():
    """
    List of words to filter out of text that is submitted in queries.

    :attr List[str] stopwords: List of stop words.
    """

    def __init__(self, stopwords: List[str]) -> None:
        """
        Initialize a StopWordList object.

        :param List[str] stopwords: List of stop words.
        """
        self.stopwords = stopwords

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StopWordList':
        """Initialize a StopWordList object from a json dictionary."""
        args = {}
        if 'stopwords' in _dict:
            args['stopwords'] = _dict.get('stopwords')
        else:
            raise ValueError(
                'Required property \'stopwords\' not present in StopWordList JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StopWordList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'stopwords') and self.stopwords is not None:
            _dict['stopwords'] = self.stopwords
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StopWordList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StopWordList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StopWordList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableBodyCells():
    """
    Cells that are not table header, column header, or row header cells.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    :attr str text: (optional) The textual contents of this cell from the input
          document without associated markup content.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row`
          location in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row`
          location in the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's
          `column` location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
          location in the current table.
    :attr List[TableRowHeaderIds] row_header_ids: (optional) A list of table row
          header ids.
    :attr List[TableRowHeaderTexts] row_header_texts: (optional) A list of table row
          header texts.
    :attr List[TableRowHeaderTextsNormalized] row_header_texts_normalized:
          (optional) A list of table row header texts normalized.
    :attr List[TableColumnHeaderIds] column_header_ids: (optional) A list of table
          column header ids.
    :attr List[TableColumnHeaderTexts] column_header_texts: (optional) A list of
          table column header texts.
    :attr List[TableColumnHeaderTextsNormalized] column_header_texts_normalized:
          (optional) A list of table column header texts normalized.
    :attr List[DocumentAttribute] attributes: (optional) A list of document
          attributes.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: 'TableElementLocation' = None,
                 text: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None,
                 row_header_ids: List['TableRowHeaderIds'] = None,
                 row_header_texts: List['TableRowHeaderTexts'] = None,
                 row_header_texts_normalized: List[
                     'TableRowHeaderTextsNormalized'] = None,
                 column_header_ids: List['TableColumnHeaderIds'] = None,
                 column_header_texts: List['TableColumnHeaderTexts'] = None,
                 column_header_texts_normalized: List[
                     'TableColumnHeaderTextsNormalized'] = None,
                 attributes: List['DocumentAttribute'] = None) -> None:
        """
        Initialize a TableBodyCells object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param TableElementLocation location: (optional) The numeric location of
               the identified element in the document, represented with two integers
               labeled `begin` and `end`.
        :param str text: (optional) The textual contents of this cell from the
               input document without associated markup content.
        :param int row_index_begin: (optional) The `begin` index of this cell's
               `row` location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row`
               location in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
               `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's
               `column` location in the current table.
        :param List[TableRowHeaderIds] row_header_ids: (optional) A list of table
               row header ids.
        :param List[TableRowHeaderTexts] row_header_texts: (optional) A list of
               table row header texts.
        :param List[TableRowHeaderTextsNormalized] row_header_texts_normalized:
               (optional) A list of table row header texts normalized.
        :param List[TableColumnHeaderIds] column_header_ids: (optional) A list of
               table column header ids.
        :param List[TableColumnHeaderTexts] column_header_texts: (optional) A list
               of table column header texts.
        :param List[TableColumnHeaderTextsNormalized]
               column_header_texts_normalized: (optional) A list of table column header
               texts normalized.
        :param List[DocumentAttribute] attributes: (optional) A list of document
               attributes.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text
        self.row_index_begin = row_index_begin
        self.row_index_end = row_index_end
        self.column_index_begin = column_index_begin
        self.column_index_end = column_index_end
        self.row_header_ids = row_header_ids
        self.row_header_texts = row_header_texts
        self.row_header_texts_normalized = row_header_texts_normalized
        self.column_header_ids = column_header_ids
        self.column_header_texts = column_header_texts
        self.column_header_texts_normalized = column_header_texts_normalized
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableBodyCells':
        """Initialize a TableBodyCells object from a json dictionary."""
        args = {}
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation.from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'row_index_begin' in _dict:
            args['row_index_begin'] = _dict.get('row_index_begin')
        if 'row_index_end' in _dict:
            args['row_index_end'] = _dict.get('row_index_end')
        if 'column_index_begin' in _dict:
            args['column_index_begin'] = _dict.get('column_index_begin')
        if 'column_index_end' in _dict:
            args['column_index_end'] = _dict.get('column_index_end')
        if 'row_header_ids' in _dict:
            args['row_header_ids'] = [
                TableRowHeaderIds.from_dict(v)
                for v in _dict.get('row_header_ids')
            ]
        if 'row_header_texts' in _dict:
            args['row_header_texts'] = [
                TableRowHeaderTexts.from_dict(v)
                for v in _dict.get('row_header_texts')
            ]
        if 'row_header_texts_normalized' in _dict:
            args['row_header_texts_normalized'] = [
                TableRowHeaderTextsNormalized.from_dict(v)
                for v in _dict.get('row_header_texts_normalized')
            ]
        if 'column_header_ids' in _dict:
            args['column_header_ids'] = [
                TableColumnHeaderIds.from_dict(v)
                for v in _dict.get('column_header_ids')
            ]
        if 'column_header_texts' in _dict:
            args['column_header_texts'] = [
                TableColumnHeaderTexts.from_dict(v)
                for v in _dict.get('column_header_texts')
            ]
        if 'column_header_texts_normalized' in _dict:
            args['column_header_texts_normalized'] = [
                TableColumnHeaderTextsNormalized.from_dict(v)
                for v in _dict.get('column_header_texts_normalized')
            ]
        if 'attributes' in _dict:
            args['attributes'] = [
                DocumentAttribute.from_dict(v) for v in _dict.get('attributes')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableBodyCells object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            if isinstance(self.location, dict):
                _dict['location'] = self.location
            else:
                _dict['location'] = self.location.to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'row_index_begin') and self.row_index_begin is not None:
            _dict['row_index_begin'] = self.row_index_begin
        if hasattr(self, 'row_index_end') and self.row_index_end is not None:
            _dict['row_index_end'] = self.row_index_end
        if hasattr(
                self,
                'column_index_begin') and self.column_index_begin is not None:
            _dict['column_index_begin'] = self.column_index_begin
        if hasattr(self,
                   'column_index_end') and self.column_index_end is not None:
            _dict['column_index_end'] = self.column_index_end
        if hasattr(self, 'row_header_ids') and self.row_header_ids is not None:
            row_header_ids_list = []
            for v in self.row_header_ids:
                if isinstance(v, dict):
                    row_header_ids_list.append(v)
                else:
                    row_header_ids_list.append(v.to_dict())
            _dict['row_header_ids'] = row_header_ids_list
        if hasattr(self,
                   'row_header_texts') and self.row_header_texts is not None:
            row_header_texts_list = []
            for v in self.row_header_texts:
                if isinstance(v, dict):
                    row_header_texts_list.append(v)
                else:
                    row_header_texts_list.append(v.to_dict())
            _dict['row_header_texts'] = row_header_texts_list
        if hasattr(self, 'row_header_texts_normalized'
                  ) and self.row_header_texts_normalized is not None:
            row_header_texts_normalized_list = []
            for v in self.row_header_texts_normalized:
                if isinstance(v, dict):
                    row_header_texts_normalized_list.append(v)
                else:
                    row_header_texts_normalized_list.append(v.to_dict())
            _dict[
                'row_header_texts_normalized'] = row_header_texts_normalized_list
        if hasattr(self,
                   'column_header_ids') and self.column_header_ids is not None:
            column_header_ids_list = []
            for v in self.column_header_ids:
                if isinstance(v, dict):
                    column_header_ids_list.append(v)
                else:
                    column_header_ids_list.append(v.to_dict())
            _dict['column_header_ids'] = column_header_ids_list
        if hasattr(
                self,
                'column_header_texts') and self.column_header_texts is not None:
            column_header_texts_list = []
            for v in self.column_header_texts:
                if isinstance(v, dict):
                    column_header_texts_list.append(v)
                else:
                    column_header_texts_list.append(v.to_dict())
            _dict['column_header_texts'] = column_header_texts_list
        if hasattr(self, 'column_header_texts_normalized'
                  ) and self.column_header_texts_normalized is not None:
            column_header_texts_normalized_list = []
            for v in self.column_header_texts_normalized:
                if isinstance(v, dict):
                    column_header_texts_normalized_list.append(v)
                else:
                    column_header_texts_normalized_list.append(v.to_dict())
            _dict[
                'column_header_texts_normalized'] = column_header_texts_normalized_list
        if hasattr(self, 'attributes') and self.attributes is not None:
            attributes_list = []
            for v in self.attributes:
                if isinstance(v, dict):
                    attributes_list.append(v)
                else:
                    attributes_list.append(v.to_dict())
            _dict['attributes'] = attributes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableBodyCells object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableBodyCells') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableBodyCells') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableCellKey():
    """
    A key in a key-value pair.

    :attr str cell_id: (optional) The unique ID of the key in the table.
    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    :attr str text: (optional) The text content of the table cell without HTML
          markup.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: 'TableElementLocation' = None,
                 text: str = None) -> None:
        """
        Initialize a TableCellKey object.

        :param str cell_id: (optional) The unique ID of the key in the table.
        :param TableElementLocation location: (optional) The numeric location of
               the identified element in the document, represented with two integers
               labeled `begin` and `end`.
        :param str text: (optional) The text content of the table cell without HTML
               markup.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableCellKey':
        """Initialize a TableCellKey object from a json dictionary."""
        args = {}
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation.from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableCellKey object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            if isinstance(self.location, dict):
                _dict['location'] = self.location
            else:
                _dict['location'] = self.location.to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableCellKey object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableCellKey') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableCellKey') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableCellValues():
    """
    A value in a key-value pair.

    :attr str cell_id: (optional) The unique ID of the value in the table.
    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    :attr str text: (optional) The text content of the table cell without HTML
          markup.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: 'TableElementLocation' = None,
                 text: str = None) -> None:
        """
        Initialize a TableCellValues object.

        :param str cell_id: (optional) The unique ID of the value in the table.
        :param TableElementLocation location: (optional) The numeric location of
               the identified element in the document, represented with two integers
               labeled `begin` and `end`.
        :param str text: (optional) The text content of the table cell without HTML
               markup.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableCellValues':
        """Initialize a TableCellValues object from a json dictionary."""
        args = {}
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation.from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableCellValues object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            if isinstance(self.location, dict):
                _dict['location'] = self.location
            else:
                _dict['location'] = self.location.to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableCellValues object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableCellValues') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableCellValues') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaderIds():
    """
    An array of values, each being the `id` value of a column header that is applicable to
    the current cell.

    :attr str id: (optional) The `id` value of a column header.
    """

    def __init__(self, *, id: str = None) -> None:
        """
        Initialize a TableColumnHeaderIds object.

        :param str id: (optional) The `id` value of a column header.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableColumnHeaderIds':
        """Initialize a TableColumnHeaderIds object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaderIds object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableColumnHeaderIds object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableColumnHeaderIds') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableColumnHeaderIds') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaderTexts():
    """
    An array of values, each being the `text` value of a column header that is applicable
    to the current cell.

    :attr str text: (optional) The `text` value of a column header.
    """

    def __init__(self, *, text: str = None) -> None:
        """
        Initialize a TableColumnHeaderTexts object.

        :param str text: (optional) The `text` value of a column header.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableColumnHeaderTexts':
        """Initialize a TableColumnHeaderTexts object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaderTexts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableColumnHeaderTexts object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableColumnHeaderTexts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableColumnHeaderTexts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaderTextsNormalized():
    """
    If you provide customization input, the normalized version of the column header texts
    according to the customization; otherwise, the same value as `column_header_texts`.

    :attr str text_normalized: (optional) The normalized version of a column header
          text.
    """

    def __init__(self, *, text_normalized: str = None) -> None:
        """
        Initialize a TableColumnHeaderTextsNormalized object.

        :param str text_normalized: (optional) The normalized version of a column
               header text.
        """
        self.text_normalized = text_normalized

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableColumnHeaderTextsNormalized':
        """Initialize a TableColumnHeaderTextsNormalized object from a json dictionary."""
        args = {}
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaderTextsNormalized object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableColumnHeaderTextsNormalized object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableColumnHeaderTextsNormalized') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableColumnHeaderTextsNormalized') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaders():
    """
    Column-level cells, each applicable as a header to other cells in the same column as
    itself, of the current table.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr dict location: (optional) The location of the column header cell in the
          current table as defined by its `begin` and `end` offsets, respectfully, in the
          input document.
    :attr str text: (optional) The textual contents of this cell from the input
          document without associated markup content.
    :attr str text_normalized: (optional) If you provide customization input, the
          normalized version of the cell text according to the customization; otherwise,
          the same value as `text`.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row`
          location in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row`
          location in the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's
          `column` location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
          location in the current table.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: dict = None,
                 text: str = None,
                 text_normalized: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None) -> None:
        """
        Initialize a TableColumnHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param dict location: (optional) The location of the column header cell in
               the current table as defined by its `begin` and `end` offsets,
               respectfully, in the input document.
        :param str text: (optional) The textual contents of this cell from the
               input document without associated markup content.
        :param str text_normalized: (optional) If you provide customization input,
               the normalized version of the cell text according to the customization;
               otherwise, the same value as `text`.
        :param int row_index_begin: (optional) The `begin` index of this cell's
               `row` location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row`
               location in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
               `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's
               `column` location in the current table.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text
        self.text_normalized = text_normalized
        self.row_index_begin = row_index_begin
        self.row_index_end = row_index_end
        self.column_index_begin = column_index_begin
        self.column_index_end = column_index_end

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableColumnHeaders':
        """Initialize a TableColumnHeaders object from a json dictionary."""
        args = {}
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'row_index_begin' in _dict:
            args['row_index_begin'] = _dict.get('row_index_begin')
        if 'row_index_end' in _dict:
            args['row_index_end'] = _dict.get('row_index_end')
        if 'column_index_begin' in _dict:
            args['column_index_begin'] = _dict.get('column_index_begin')
        if 'column_index_end' in _dict:
            args['column_index_end'] = _dict.get('column_index_end')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaders object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self,
                   'row_index_begin') and self.row_index_begin is not None:
            _dict['row_index_begin'] = self.row_index_begin
        if hasattr(self, 'row_index_end') and self.row_index_end is not None:
            _dict['row_index_end'] = self.row_index_end
        if hasattr(
                self,
                'column_index_begin') and self.column_index_begin is not None:
            _dict['column_index_begin'] = self.column_index_begin
        if hasattr(self,
                   'column_index_end') and self.column_index_end is not None:
            _dict['column_index_end'] = self.column_index_end
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableColumnHeaders object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableColumnHeaders') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableColumnHeaders') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableElementLocation():
    """
    The numeric location of the identified element in the document, represented with two
    integers labeled `begin` and `end`.

    :attr int begin: The element's `begin` index.
    :attr int end: The element's `end` index.
    """

    def __init__(self, begin: int, end: int) -> None:
        """
        Initialize a TableElementLocation object.

        :param int begin: The element's `begin` index.
        :param int end: The element's `end` index.
        """
        self.begin = begin
        self.end = end

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableElementLocation':
        """Initialize a TableElementLocation object from a json dictionary."""
        args = {}
        if 'begin' in _dict:
            args['begin'] = _dict.get('begin')
        else:
            raise ValueError(
                'Required property \'begin\' not present in TableElementLocation JSON'
            )
        if 'end' in _dict:
            args['end'] = _dict.get('end')
        else:
            raise ValueError(
                'Required property \'end\' not present in TableElementLocation JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableElementLocation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableElementLocation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableElementLocation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableElementLocation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableHeaders():
    """
    The contents of the current table's header.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr dict location: (optional) The location of the table header cell in the
          current table as defined by its `begin` and `end` offsets, respectfully, in the
          input document.
    :attr str text: (optional) The textual contents of the cell from the input
          document without associated markup content.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row`
          location in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row`
          location in the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's
          `column` location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
          location in the current table.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: dict = None,
                 text: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None) -> None:
        """
        Initialize a TableHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param dict location: (optional) The location of the table header cell in
               the current table as defined by its `begin` and `end` offsets,
               respectfully, in the input document.
        :param str text: (optional) The textual contents of the cell from the input
               document without associated markup content.
        :param int row_index_begin: (optional) The `begin` index of this cell's
               `row` location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row`
               location in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
               `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's
               `column` location in the current table.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text
        self.row_index_begin = row_index_begin
        self.row_index_end = row_index_end
        self.column_index_begin = column_index_begin
        self.column_index_end = column_index_end

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableHeaders':
        """Initialize a TableHeaders object from a json dictionary."""
        args = {}
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'row_index_begin' in _dict:
            args['row_index_begin'] = _dict.get('row_index_begin')
        if 'row_index_end' in _dict:
            args['row_index_end'] = _dict.get('row_index_end')
        if 'column_index_begin' in _dict:
            args['column_index_begin'] = _dict.get('column_index_begin')
        if 'column_index_end' in _dict:
            args['column_index_end'] = _dict.get('column_index_end')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableHeaders object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'row_index_begin') and self.row_index_begin is not None:
            _dict['row_index_begin'] = self.row_index_begin
        if hasattr(self, 'row_index_end') and self.row_index_end is not None:
            _dict['row_index_end'] = self.row_index_end
        if hasattr(
                self,
                'column_index_begin') and self.column_index_begin is not None:
            _dict['column_index_begin'] = self.column_index_begin
        if hasattr(self,
                   'column_index_end') and self.column_index_end is not None:
            _dict['column_index_end'] = self.column_index_end
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableHeaders object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableHeaders') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableHeaders') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableKeyValuePairs():
    """
    Key-value pairs detected across cell boundaries.

    :attr TableCellKey key: (optional) A key in a key-value pair.
    :attr List[TableCellValues] value: (optional) A list of values in a key-value
          pair.
    """

    def __init__(self,
                 *,
                 key: 'TableCellKey' = None,
                 value: List['TableCellValues'] = None) -> None:
        """
        Initialize a TableKeyValuePairs object.

        :param TableCellKey key: (optional) A key in a key-value pair.
        :param List[TableCellValues] value: (optional) A list of values in a
               key-value pair.
        """
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableKeyValuePairs':
        """Initialize a TableKeyValuePairs object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = TableCellKey.from_dict(_dict.get('key'))
        if 'value' in _dict:
            args['value'] = [
                TableCellValues.from_dict(v) for v in _dict.get('value')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableKeyValuePairs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            if isinstance(self.key, dict):
                _dict['key'] = self.key
            else:
                _dict['key'] = self.key.to_dict()
        if hasattr(self, 'value') and self.value is not None:
            value_list = []
            for v in self.value:
                if isinstance(v, dict):
                    value_list.append(v)
                else:
                    value_list.append(v.to_dict())
            _dict['value'] = value_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableKeyValuePairs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableKeyValuePairs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableKeyValuePairs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableResultTable():
    """
    Full table object retrieved from Table Understanding Enrichment.

    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    :attr str text: (optional) The textual contents of the current table from the
          input document without associated markup content.
    :attr TableTextLocation section_title: (optional) Text and associated location
          within a table.
    :attr TableTextLocation title: (optional) Text and associated location within a
          table.
    :attr List[TableHeaders] table_headers: (optional) An array of table-level cells
          that apply as headers to all the other cells in the current table.
    :attr List[TableRowHeaders] row_headers: (optional) An array of row-level cells,
          each applicable as a header to other cells in the same row as itself, of the
          current table.
    :attr List[TableColumnHeaders] column_headers: (optional) An array of
          column-level cells, each applicable as a header to other cells in the same
          column as itself, of the current table.
    :attr List[TableKeyValuePairs] key_value_pairs: (optional) An array of key-value
          pairs identified in the current table.
    :attr List[TableBodyCells] body_cells: (optional) An array of cells that are
          neither table header nor column header nor row header cells, of the current
          table with corresponding row and column header associations.
    :attr List[TableTextLocation] contexts: (optional) An array of lists of textual
          entries across the document related to the current table being parsed.
    """

    def __init__(self,
                 *,
                 location: 'TableElementLocation' = None,
                 text: str = None,
                 section_title: 'TableTextLocation' = None,
                 title: 'TableTextLocation' = None,
                 table_headers: List['TableHeaders'] = None,
                 row_headers: List['TableRowHeaders'] = None,
                 column_headers: List['TableColumnHeaders'] = None,
                 key_value_pairs: List['TableKeyValuePairs'] = None,
                 body_cells: List['TableBodyCells'] = None,
                 contexts: List['TableTextLocation'] = None) -> None:
        """
        Initialize a TableResultTable object.

        :param TableElementLocation location: (optional) The numeric location of
               the identified element in the document, represented with two integers
               labeled `begin` and `end`.
        :param str text: (optional) The textual contents of the current table from
               the input document without associated markup content.
        :param TableTextLocation section_title: (optional) Text and associated
               location within a table.
        :param TableTextLocation title: (optional) Text and associated location
               within a table.
        :param List[TableHeaders] table_headers: (optional) An array of table-level
               cells that apply as headers to all the other cells in the current table.
        :param List[TableRowHeaders] row_headers: (optional) An array of row-level
               cells, each applicable as a header to other cells in the same row as
               itself, of the current table.
        :param List[TableColumnHeaders] column_headers: (optional) An array of
               column-level cells, each applicable as a header to other cells in the same
               column as itself, of the current table.
        :param List[TableKeyValuePairs] key_value_pairs: (optional) An array of
               key-value pairs identified in the current table.
        :param List[TableBodyCells] body_cells: (optional) An array of cells that
               are neither table header nor column header nor row header cells, of the
               current table with corresponding row and column header associations.
        :param List[TableTextLocation] contexts: (optional) An array of lists of
               textual entries across the document related to the current table being
               parsed.
        """
        self.location = location
        self.text = text
        self.section_title = section_title
        self.title = title
        self.table_headers = table_headers
        self.row_headers = row_headers
        self.column_headers = column_headers
        self.key_value_pairs = key_value_pairs
        self.body_cells = body_cells
        self.contexts = contexts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableResultTable':
        """Initialize a TableResultTable object from a json dictionary."""
        args = {}
        if 'location' in _dict:
            args['location'] = TableElementLocation.from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'section_title' in _dict:
            args['section_title'] = TableTextLocation.from_dict(
                _dict.get('section_title'))
        if 'title' in _dict:
            args['title'] = TableTextLocation.from_dict(_dict.get('title'))
        if 'table_headers' in _dict:
            args['table_headers'] = [
                TableHeaders.from_dict(v) for v in _dict.get('table_headers')
            ]
        if 'row_headers' in _dict:
            args['row_headers'] = [
                TableRowHeaders.from_dict(v) for v in _dict.get('row_headers')
            ]
        if 'column_headers' in _dict:
            args['column_headers'] = [
                TableColumnHeaders.from_dict(v)
                for v in _dict.get('column_headers')
            ]
        if 'key_value_pairs' in _dict:
            args['key_value_pairs'] = [
                TableKeyValuePairs.from_dict(v)
                for v in _dict.get('key_value_pairs')
            ]
        if 'body_cells' in _dict:
            args['body_cells'] = [
                TableBodyCells.from_dict(v) for v in _dict.get('body_cells')
            ]
        if 'contexts' in _dict:
            args['contexts'] = [
                TableTextLocation.from_dict(v) for v in _dict.get('contexts')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableResultTable object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            if isinstance(self.location, dict):
                _dict['location'] = self.location
            else:
                _dict['location'] = self.location.to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'section_title') and self.section_title is not None:
            if isinstance(self.section_title, dict):
                _dict['section_title'] = self.section_title
            else:
                _dict['section_title'] = self.section_title.to_dict()
        if hasattr(self, 'title') and self.title is not None:
            if isinstance(self.title, dict):
                _dict['title'] = self.title
            else:
                _dict['title'] = self.title.to_dict()
        if hasattr(self, 'table_headers') and self.table_headers is not None:
            table_headers_list = []
            for v in self.table_headers:
                if isinstance(v, dict):
                    table_headers_list.append(v)
                else:
                    table_headers_list.append(v.to_dict())
            _dict['table_headers'] = table_headers_list
        if hasattr(self, 'row_headers') and self.row_headers is not None:
            row_headers_list = []
            for v in self.row_headers:
                if isinstance(v, dict):
                    row_headers_list.append(v)
                else:
                    row_headers_list.append(v.to_dict())
            _dict['row_headers'] = row_headers_list
        if hasattr(self, 'column_headers') and self.column_headers is not None:
            column_headers_list = []
            for v in self.column_headers:
                if isinstance(v, dict):
                    column_headers_list.append(v)
                else:
                    column_headers_list.append(v.to_dict())
            _dict['column_headers'] = column_headers_list
        if hasattr(self,
                   'key_value_pairs') and self.key_value_pairs is not None:
            key_value_pairs_list = []
            for v in self.key_value_pairs:
                if isinstance(v, dict):
                    key_value_pairs_list.append(v)
                else:
                    key_value_pairs_list.append(v.to_dict())
            _dict['key_value_pairs'] = key_value_pairs_list
        if hasattr(self, 'body_cells') and self.body_cells is not None:
            body_cells_list = []
            for v in self.body_cells:
                if isinstance(v, dict):
                    body_cells_list.append(v)
                else:
                    body_cells_list.append(v.to_dict())
            _dict['body_cells'] = body_cells_list
        if hasattr(self, 'contexts') and self.contexts is not None:
            contexts_list = []
            for v in self.contexts:
                if isinstance(v, dict):
                    contexts_list.append(v)
                else:
                    contexts_list.append(v.to_dict())
            _dict['contexts'] = contexts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableResultTable object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableResultTable') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableResultTable') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableRowHeaderIds():
    """
    An array of values, each being the `id` value of a row header that is applicable to
    this body cell.

    :attr str id: (optional) The `id` values of a row header.
    """

    def __init__(self, *, id: str = None) -> None:
        """
        Initialize a TableRowHeaderIds object.

        :param str id: (optional) The `id` values of a row header.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableRowHeaderIds':
        """Initialize a TableRowHeaderIds object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaderIds object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableRowHeaderIds object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableRowHeaderIds') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableRowHeaderIds') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableRowHeaderTexts():
    """
    An array of values, each being the `text` value of a row header that is applicable to
    this body cell.

    :attr str text: (optional) The `text` value of a row header.
    """

    def __init__(self, *, text: str = None) -> None:
        """
        Initialize a TableRowHeaderTexts object.

        :param str text: (optional) The `text` value of a row header.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableRowHeaderTexts':
        """Initialize a TableRowHeaderTexts object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaderTexts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableRowHeaderTexts object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableRowHeaderTexts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableRowHeaderTexts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableRowHeaderTextsNormalized():
    """
    If you provide customization input, the normalized version of the row header texts
    according to the customization; otherwise, the same value as `row_header_texts`.

    :attr str text_normalized: (optional) The normalized version of a row header
          text.
    """

    def __init__(self, *, text_normalized: str = None) -> None:
        """
        Initialize a TableRowHeaderTextsNormalized object.

        :param str text_normalized: (optional) The normalized version of a row
               header text.
        """
        self.text_normalized = text_normalized

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableRowHeaderTextsNormalized':
        """Initialize a TableRowHeaderTextsNormalized object from a json dictionary."""
        args = {}
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaderTextsNormalized object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableRowHeaderTextsNormalized object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableRowHeaderTextsNormalized') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableRowHeaderTextsNormalized') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableRowHeaders():
    """
    Row-level cells, each applicable as a header to other cells in the same row as itself,
    of the current table.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    :attr str text: (optional) The textual contents of this cell from the input
          document without associated markup content.
    :attr str text_normalized: (optional) If you provide customization input, the
          normalized version of the cell text according to the customization; otherwise,
          the same value as `text`.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row`
          location in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row`
          location in the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's
          `column` location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
          location in the current table.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: 'TableElementLocation' = None,
                 text: str = None,
                 text_normalized: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None) -> None:
        """
        Initialize a TableRowHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param TableElementLocation location: (optional) The numeric location of
               the identified element in the document, represented with two integers
               labeled `begin` and `end`.
        :param str text: (optional) The textual contents of this cell from the
               input document without associated markup content.
        :param str text_normalized: (optional) If you provide customization input,
               the normalized version of the cell text according to the customization;
               otherwise, the same value as `text`.
        :param int row_index_begin: (optional) The `begin` index of this cell's
               `row` location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row`
               location in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
               `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's
               `column` location in the current table.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text
        self.text_normalized = text_normalized
        self.row_index_begin = row_index_begin
        self.row_index_end = row_index_end
        self.column_index_begin = column_index_begin
        self.column_index_end = column_index_end

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableRowHeaders':
        """Initialize a TableRowHeaders object from a json dictionary."""
        args = {}
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation.from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'row_index_begin' in _dict:
            args['row_index_begin'] = _dict.get('row_index_begin')
        if 'row_index_end' in _dict:
            args['row_index_end'] = _dict.get('row_index_end')
        if 'column_index_begin' in _dict:
            args['column_index_begin'] = _dict.get('column_index_begin')
        if 'column_index_end' in _dict:
            args['column_index_end'] = _dict.get('column_index_end')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaders object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            if isinstance(self.location, dict):
                _dict['location'] = self.location
            else:
                _dict['location'] = self.location.to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self,
                   'row_index_begin') and self.row_index_begin is not None:
            _dict['row_index_begin'] = self.row_index_begin
        if hasattr(self, 'row_index_end') and self.row_index_end is not None:
            _dict['row_index_end'] = self.row_index_end
        if hasattr(
                self,
                'column_index_begin') and self.column_index_begin is not None:
            _dict['column_index_begin'] = self.column_index_begin
        if hasattr(self,
                   'column_index_end') and self.column_index_end is not None:
            _dict['column_index_end'] = self.column_index_end
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableRowHeaders object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableRowHeaders') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableRowHeaders') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableTextLocation():
    """
    Text and associated location within a table.

    :attr str text: (optional) The text retrieved.
    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: 'TableElementLocation' = None) -> None:
        """
        Initialize a TableTextLocation object.

        :param str text: (optional) The text retrieved.
        :param TableElementLocation location: (optional) The numeric location of
               the identified element in the document, represented with two integers
               labeled `begin` and `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableTextLocation':
        """Initialize a TableTextLocation object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = TableElementLocation.from_dict(
                _dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableTextLocation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            if isinstance(self.location, dict):
                _dict['location'] = self.location
            else:
                _dict['location'] = self.location.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableTextLocation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TableTextLocation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableTextLocation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingExample():
    """
    Object that contains example response details for a training query.

    :attr str document_id: The document ID associated with this training example.
    :attr str collection_id: The collection ID associated with this training
          example.
    :attr int relevance: The relevance of the training example.
    :attr datetime created: (optional) The date and time the example was created.
    :attr datetime updated: (optional) The date and time the example was updated.
    """

    def __init__(self,
                 document_id: str,
                 collection_id: str,
                 relevance: int,
                 *,
                 created: datetime = None,
                 updated: datetime = None) -> None:
        """
        Initialize a TrainingExample object.

        :param str document_id: The document ID associated with this training
               example.
        :param str collection_id: The collection ID associated with this training
               example.
        :param int relevance: The relevance of the training example.
        """
        self.document_id = document_id
        self.collection_id = collection_id
        self.relevance = relevance
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingExample':
        """Initialize a TrainingExample object from a json dictionary."""
        args = {}
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
        else:
            raise ValueError(
                'Required property \'document_id\' not present in TrainingExample JSON'
            )
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        else:
            raise ValueError(
                'Required property \'collection_id\' not present in TrainingExample JSON'
            )
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
        else:
            raise ValueError(
                'Required property \'relevance\' not present in TrainingExample JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
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
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingExample object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrainingExample') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingExample') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingQuery():
    """
    Object that contains training query details.

    :attr str query_id: (optional) The query ID associated with the training query.
    :attr str natural_language_query: The natural text query that is used as the
          training query.
    :attr str filter: (optional) The filter used on the collection before the
          **natural_language_query** is applied.
    :attr datetime created: (optional) The date and time the query was created.
    :attr datetime updated: (optional) The date and time the query was updated.
    :attr List[TrainingExample] examples: Array of training examples.
    """

    def __init__(self,
                 natural_language_query: str,
                 examples: List['TrainingExample'],
                 *,
                 query_id: str = None,
                 filter: str = None,
                 created: datetime = None,
                 updated: datetime = None) -> None:
        """
        Initialize a TrainingQuery object.

        :param str natural_language_query: The natural text query that is used as
               the training query.
        :param List[TrainingExample] examples: Array of training examples.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        """
        self.query_id = query_id
        self.natural_language_query = natural_language_query
        self.filter = filter
        self.created = created
        self.updated = updated
        self.examples = examples

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingQuery':
        """Initialize a TrainingQuery object from a json dictionary."""
        args = {}
        if 'query_id' in _dict:
            args['query_id'] = _dict.get('query_id')
        if 'natural_language_query' in _dict:
            args['natural_language_query'] = _dict.get('natural_language_query')
        else:
            raise ValueError(
                'Required property \'natural_language_query\' not present in TrainingQuery JSON'
            )
        if 'filter' in _dict:
            args['filter'] = _dict.get('filter')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'examples' in _dict:
            args['examples'] = [
                TrainingExample.from_dict(v) for v in _dict.get('examples')
            ]
        else:
            raise ValueError(
                'Required property \'examples\' not present in TrainingQuery JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingQuery object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'query_id') and getattr(self, 'query_id') is not None:
            _dict['query_id'] = getattr(self, 'query_id')
        if hasattr(self, 'natural_language_query'
                  ) and self.natural_language_query is not None:
            _dict['natural_language_query'] = self.natural_language_query
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'examples') and self.examples is not None:
            examples_list = []
            for v in self.examples:
                if isinstance(v, dict):
                    examples_list.append(v)
                else:
                    examples_list.append(v.to_dict())
            _dict['examples'] = examples_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingQuery object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrainingQuery') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingQuery') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingQuerySet():
    """
    Object specifying the training queries contained in the identified training set.

    :attr List[TrainingQuery] queries: (optional) Array of training queries. At
          least 50 queries are required for training to begin. A maximum of 10,000 queries
          are returned.
    """

    def __init__(self, *, queries: List['TrainingQuery'] = None) -> None:
        """
        Initialize a TrainingQuerySet object.

        :param List[TrainingQuery] queries: (optional) Array of training queries.
               At least 50 queries are required for training to begin. A maximum of 10,000
               queries are returned.
        """
        self.queries = queries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingQuerySet':
        """Initialize a TrainingQuerySet object from a json dictionary."""
        args = {}
        if 'queries' in _dict:
            args['queries'] = [
                TrainingQuery.from_dict(v) for v in _dict.get('queries')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingQuerySet object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'queries') and self.queries is not None:
            queries_list = []
            for v in self.queries:
                if isinstance(v, dict):
                    queries_list.append(v)
                else:
                    queries_list.append(v.to_dict())
            _dict['queries'] = queries_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingQuerySet object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrainingQuerySet') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingQuerySet') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdateDocumentClassifier():
    """
    An object that contains a new name or description for a document classifier, updated
    training data, or new or updated test data.

    :attr str name: (optional) A new name for the classifier.
    :attr str description: (optional) A new description for the classifier.
    """

    def __init__(self, *, name: str = None, description: str = None) -> None:
        """
        Initialize a UpdateDocumentClassifier object.

        :param str name: (optional) A new name for the classifier.
        :param str description: (optional) A new description for the classifier.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateDocumentClassifier':
        """Initialize a UpdateDocumentClassifier object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateDocumentClassifier object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateDocumentClassifier object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateDocumentClassifier') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateDocumentClassifier') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryCalculationAggregation(QueryAggregation):
    """
    Returns a scalar calculation across all documents for the field specified. Possible
    calculations include min, max, sum, average, and unique_count.

    :attr str type: (optional) Specifies the calculation type, such as 'average`,
          `max`, `min`, `sum`, or `unique_count`.
    :attr str field: The field to perform the calculation on.
    :attr float value: (optional) The value of the calculation.
    """

    def __init__(self,
                 field: str,
                 *,
                 type: str = None,
                 value: float = None) -> None:
        """
        Initialize a QueryAggregationQueryCalculationAggregation object.

        :param str field: The field to perform the calculation on.
        :param str type: (optional) Specifies the calculation type, such as
               'average`, `max`, `min`, `sum`, or `unique_count`.
        :param float value: (optional) The value of the calculation.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.field = field
        self.value = value

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'QueryAggregationQueryCalculationAggregation':
        """Initialize a QueryAggregationQueryCalculationAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in QueryAggregationQueryCalculationAggregation JSON'
            )
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryCalculationAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryCalculationAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'QueryAggregationQueryCalculationAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'QueryAggregationQueryCalculationAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryFilterAggregation(QueryAggregation):
    """
    A modifier that narrows the document set of the subaggregations it precedes.

    :attr str type: (optional) Specifies that the aggregation type is `filter`.
    :attr str match: The filter that is written in Discovery Query Language syntax
          and is applied to the documents before subaggregations are run.
    :attr int matching_results: Number of documents that match the filter.
    :attr List[dict] aggregations: (optional) An array of subaggregations.
    """

    def __init__(self,
                 match: str,
                 matching_results: int,
                 *,
                 type: str = None,
                 aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryAggregationQueryFilterAggregation object.

        :param str match: The filter that is written in Discovery Query Language
               syntax and is applied to the documents before subaggregations are run.
        :param int matching_results: Number of documents that match the filter.
        :param str type: (optional) Specifies that the aggregation type is
               `filter`.
        :param List[dict] aggregations: (optional) An array of subaggregations.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.match = match
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregationQueryFilterAggregation':
        """Initialize a QueryAggregationQueryFilterAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'match' in _dict:
            args['match'] = _dict.get('match')
        else:
            raise ValueError(
                'Required property \'match\' not present in QueryAggregationQueryFilterAggregation JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryAggregationQueryFilterAggregation JSON'
            )
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryFilterAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'match') and self.match is not None:
            _dict['match'] = self.match
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryFilterAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryFilterAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryFilterAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryGroupByAggregation(QueryAggregation):
    """
    Separates document results into groups that meet the conditions you specify.

    :attr str type: (optional) Specifies that the aggregation type is `group_by`.
    :attr List[QueryGroupByAggregationResult] results: (optional) An array of
          results.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 results: List['QueryGroupByAggregationResult'] = None) -> None:
        """
        Initialize a QueryAggregationQueryGroupByAggregation object.

        :param str type: (optional) Specifies that the aggregation type is
               `group_by`.
        :param List[QueryGroupByAggregationResult] results: (optional) An array of
               results.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.results = results

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'QueryAggregationQueryGroupByAggregation':
        """Initialize a QueryAggregationQueryGroupByAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'results' in _dict:
            args['results'] = [
                QueryGroupByAggregationResult.from_dict(v)
                for v in _dict.get('results')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryGroupByAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryGroupByAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryGroupByAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryGroupByAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryHistogramAggregation(QueryAggregation):
    """
    Numeric interval segments to categorize documents by using field values from a single
    numeric field to describe the category.

    :attr str type: (optional) Specifies that the aggregation type is `histogram`.
    :attr str field: The numeric field name used to create the histogram.
    :attr int interval: The size of the sections that the results are split into.
    :attr str name: (optional) Identifier that can optionally be specified in the
          query request of this aggregation.
    :attr List[QueryHistogramAggregationResult] results: (optional) Array of numeric
          intervals.
    """

    def __init__(
            self,
            field: str,
            interval: int,
            *,
            type: str = None,
            name: str = None,
            results: List['QueryHistogramAggregationResult'] = None) -> None:
        """
        Initialize a QueryAggregationQueryHistogramAggregation object.

        :param str field: The numeric field name used to create the histogram.
        :param int interval: The size of the sections that the results are split
               into.
        :param str type: (optional) Specifies that the aggregation type is
               `histogram`.
        :param str name: (optional) Identifier that can optionally be specified in
               the query request of this aggregation.
        :param List[QueryHistogramAggregationResult] results: (optional) Array of
               numeric intervals.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.field = field
        self.interval = interval
        self.name = name
        self.results = results

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'QueryAggregationQueryHistogramAggregation':
        """Initialize a QueryAggregationQueryHistogramAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in QueryAggregationQueryHistogramAggregation JSON'
            )
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        else:
            raise ValueError(
                'Required property \'interval\' not present in QueryAggregationQueryHistogramAggregation JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'results' in _dict:
            args['results'] = [
                QueryHistogramAggregationResult.from_dict(v)
                for v in _dict.get('results')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryHistogramAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryHistogramAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'QueryAggregationQueryHistogramAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'QueryAggregationQueryHistogramAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryNestedAggregation(QueryAggregation):
    """
    A restriction that alters the document set that is used by the aggregations that it
    precedes. Subsequent aggregations are applied to nested documents from the specified
    field.

    :attr str type: (optional) Specifies that the aggregation type is `nested`.
    :attr str path: The path to the document field to scope subsequent aggregations
          to.
    :attr int matching_results: Number of nested documents found in the specified
          field.
    :attr List[dict] aggregations: (optional) An array of subaggregations.
    """

    def __init__(self,
                 path: str,
                 matching_results: int,
                 *,
                 type: str = None,
                 aggregations: List[dict] = None) -> None:
        """
        Initialize a QueryAggregationQueryNestedAggregation object.

        :param str path: The path to the document field to scope subsequent
               aggregations to.
        :param int matching_results: Number of nested documents found in the
               specified field.
        :param str type: (optional) Specifies that the aggregation type is
               `nested`.
        :param List[dict] aggregations: (optional) An array of subaggregations.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.path = path
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregationQueryNestedAggregation':
        """Initialize a QueryAggregationQueryNestedAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        else:
            raise ValueError(
                'Required property \'path\' not present in QueryAggregationQueryNestedAggregation JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryAggregationQueryNestedAggregation JSON'
            )
        if 'aggregations' in _dict:
            args['aggregations'] = _dict.get('aggregations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryNestedAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = self.aggregations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryNestedAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryNestedAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryNestedAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryPairAggregation(QueryAggregation):
    """
    Calculates relevancy values using combinations of document sets from results of the
    specified pair of aggregations.

    :attr str type: (optional) Specifies that the aggregation type is `pair`.
    :attr str first: (optional) Specifies the first aggregation in the pair. The
          aggregation must be a `term`, `group_by`, `histogram`, or `timeslice`
          aggregation type.
    :attr str second: (optional) Specifies the second aggregation in the pair. The
          aggregation must be a `term`, `group_by`, `histogram`, or `timeslice`
          aggregation type.
    :attr bool show_estimated_matching_results: (optional) Indicates whether to
          include estimated matching result information.
    :attr bool show_total_matching_documents: (optional) Indicates whether to
          include total matching documents information.
    :attr List[QueryPairAggregationResult] results: (optional) An array of
          aggregations.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 first: str = None,
                 second: str = None,
                 show_estimated_matching_results: bool = None,
                 show_total_matching_documents: bool = None,
                 results: List['QueryPairAggregationResult'] = None) -> None:
        """
        Initialize a QueryAggregationQueryPairAggregation object.

        :param str type: (optional) Specifies that the aggregation type is `pair`.
        :param str first: (optional) Specifies the first aggregation in the pair.
               The aggregation must be a `term`, `group_by`, `histogram`, or `timeslice`
               aggregation type.
        :param str second: (optional) Specifies the second aggregation in the pair.
               The aggregation must be a `term`, `group_by`, `histogram`, or `timeslice`
               aggregation type.
        :param bool show_estimated_matching_results: (optional) Indicates whether
               to include estimated matching result information.
        :param bool show_total_matching_documents: (optional) Indicates whether to
               include total matching documents information.
        :param List[QueryPairAggregationResult] results: (optional) An array of
               aggregations.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.first = first
        self.second = second
        self.show_estimated_matching_results = show_estimated_matching_results
        self.show_total_matching_documents = show_total_matching_documents
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregationQueryPairAggregation':
        """Initialize a QueryAggregationQueryPairAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'first' in _dict:
            args['first'] = _dict.get('first')
        if 'second' in _dict:
            args['second'] = _dict.get('second')
        if 'show_estimated_matching_results' in _dict:
            args['show_estimated_matching_results'] = _dict.get(
                'show_estimated_matching_results')
        if 'show_total_matching_documents' in _dict:
            args['show_total_matching_documents'] = _dict.get(
                'show_total_matching_documents')
        if 'results' in _dict:
            args['results'] = [
                QueryPairAggregationResult.from_dict(v)
                for v in _dict.get('results')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryPairAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first
        if hasattr(self, 'second') and self.second is not None:
            _dict['second'] = self.second
        if hasattr(self, 'show_estimated_matching_results'
                  ) and self.show_estimated_matching_results is not None:
            _dict[
                'show_estimated_matching_results'] = self.show_estimated_matching_results
        if hasattr(self, 'show_total_matching_documents'
                  ) and self.show_total_matching_documents is not None:
            _dict[
                'show_total_matching_documents'] = self.show_total_matching_documents
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryPairAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryPairAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryPairAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryTermAggregation(QueryAggregation):
    """
    Returns results from the field that is specified.

    :attr str type: (optional) Specifies that the aggregation type is `term`.
    :attr str field: (optional) The field in the document where the values come
          from.
    :attr int count: (optional) The number of results returned. Not returned if
          `relevancy:true` is specified in the request.
    :attr str name: (optional) Identifier specified in the query request of this
          aggregation. Not returned if `relevancy:true` is specified in the request.
    :attr List[QueryTermAggregationResult] results: (optional) An array of results.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 field: str = None,
                 count: int = None,
                 name: str = None,
                 results: List['QueryTermAggregationResult'] = None) -> None:
        """
        Initialize a QueryAggregationQueryTermAggregation object.

        :param str type: (optional) Specifies that the aggregation type is `term`.
        :param str field: (optional) The field in the document where the values
               come from.
        :param int count: (optional) The number of results returned. Not returned
               if `relevancy:true` is specified in the request.
        :param str name: (optional) Identifier specified in the query request of
               this aggregation. Not returned if `relevancy:true` is specified in the
               request.
        :param List[QueryTermAggregationResult] results: (optional) An array of
               results.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.field = field
        self.count = count
        self.name = name
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregationQueryTermAggregation':
        """Initialize a QueryAggregationQueryTermAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'results' in _dict:
            args['results'] = [
                QueryTermAggregationResult.from_dict(v)
                for v in _dict.get('results')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryTermAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryTermAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryTermAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryTermAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryTimesliceAggregation(QueryAggregation):
    """
    A specialized histogram aggregation that uses dates to create interval segments.

    :attr str type: (optional) Specifies that the aggregation type is `timeslice`.
    :attr str field: The date field name used to create the timeslice.
    :attr str interval: The date interval value. Valid values are seconds, minutes,
          hours, days, weeks, and years.
    :attr str name: (optional) Identifier that can optionally be specified in the
          query request of this aggregation.
    :attr List[QueryTimesliceAggregationResult] results: (optional) Array of
          aggregation results.
    """

    def __init__(
            self,
            field: str,
            interval: str,
            *,
            type: str = None,
            name: str = None,
            results: List['QueryTimesliceAggregationResult'] = None) -> None:
        """
        Initialize a QueryAggregationQueryTimesliceAggregation object.

        :param str field: The date field name used to create the timeslice.
        :param str interval: The date interval value. Valid values are seconds,
               minutes, hours, days, weeks, and years.
        :param str type: (optional) Specifies that the aggregation type is
               `timeslice`.
        :param str name: (optional) Identifier that can optionally be specified in
               the query request of this aggregation.
        :param List[QueryTimesliceAggregationResult] results: (optional) Array of
               aggregation results.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.field = field
        self.interval = interval
        self.name = name
        self.results = results

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'QueryAggregationQueryTimesliceAggregation':
        """Initialize a QueryAggregationQueryTimesliceAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in QueryAggregationQueryTimesliceAggregation JSON'
            )
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        else:
            raise ValueError(
                'Required property \'interval\' not present in QueryAggregationQueryTimesliceAggregation JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'results' in _dict:
            args['results'] = [
                QueryTimesliceAggregationResult.from_dict(v)
                for v in _dict.get('results')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryTimesliceAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryTimesliceAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'QueryAggregationQueryTimesliceAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'QueryAggregationQueryTimesliceAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryTopHitsAggregation(QueryAggregation):
    """
    Returns the top documents ranked by the score of the query.

    :attr str type: (optional) Specifies that the aggregation type is `top_hits`.
    :attr int size: The number of documents to return.
    :attr str name: (optional) Identifier specified in the query request of this
          aggregation.
    :attr QueryTopHitsAggregationResult hits: (optional) A query response that
          contains the matching documents for the preceding aggregations.
    """

    def __init__(self,
                 size: int,
                 *,
                 type: str = None,
                 name: str = None,
                 hits: 'QueryTopHitsAggregationResult' = None) -> None:
        """
        Initialize a QueryAggregationQueryTopHitsAggregation object.

        :param int size: The number of documents to return.
        :param str type: (optional) Specifies that the aggregation type is
               `top_hits`.
        :param str name: (optional) Identifier specified in the query request of
               this aggregation.
        :param QueryTopHitsAggregationResult hits: (optional) A query response that
               contains the matching documents for the preceding aggregations.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.size = size
        self.name = name
        self.hits = hits

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'QueryAggregationQueryTopHitsAggregation':
        """Initialize a QueryAggregationQueryTopHitsAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        else:
            raise ValueError(
                'Required property \'size\' not present in QueryAggregationQueryTopHitsAggregation JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'hits' in _dict:
            args['hits'] = QueryTopHitsAggregationResult.from_dict(
                _dict.get('hits'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryTopHitsAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'hits') and self.hits is not None:
            if isinstance(self.hits, dict):
                _dict['hits'] = self.hits
            else:
                _dict['hits'] = self.hits.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryTopHitsAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryTopHitsAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryTopHitsAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryTopicAggregation(QueryAggregation):
    """
    Detects how much the frequency of a given facet value deviates from the expected
    average for the given time period. This aggregation type does not use data from
    previous time periods. It calculates an index by using the averages of frequency
    counts of other facet values for the given time period.

    :attr str type: (optional) Specifies that the aggregation type is `topic`.
    :attr str facet: (optional) Specifies the `term` or `group_by` aggregation for
          the facet that you want to analyze.
    :attr str time_segments: (optional) Specifies the `timeslice` aggregation that
          defines the time segments.
    :attr bool show_estimated_matching_results: (optional) Indicates whether to
          include estimated matching result information.
    :attr bool show_total_matching_documents: (optional) Indicates whether to
          include total matching documents information.
    :attr List[QueryTopicAggregationResult] results: (optional) An array of
          aggregations.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 facet: str = None,
                 time_segments: str = None,
                 show_estimated_matching_results: bool = None,
                 show_total_matching_documents: bool = None,
                 results: List['QueryTopicAggregationResult'] = None) -> None:
        """
        Initialize a QueryAggregationQueryTopicAggregation object.

        :param str type: (optional) Specifies that the aggregation type is `topic`.
        :param str facet: (optional) Specifies the `term` or `group_by` aggregation
               for the facet that you want to analyze.
        :param str time_segments: (optional) Specifies the `timeslice` aggregation
               that defines the time segments.
        :param bool show_estimated_matching_results: (optional) Indicates whether
               to include estimated matching result information.
        :param bool show_total_matching_documents: (optional) Indicates whether to
               include total matching documents information.
        :param List[QueryTopicAggregationResult] results: (optional) An array of
               aggregations.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.facet = facet
        self.time_segments = time_segments
        self.show_estimated_matching_results = show_estimated_matching_results
        self.show_total_matching_documents = show_total_matching_documents
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregationQueryTopicAggregation':
        """Initialize a QueryAggregationQueryTopicAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'facet' in _dict:
            args['facet'] = _dict.get('facet')
        if 'time_segments' in _dict:
            args['time_segments'] = _dict.get('time_segments')
        if 'show_estimated_matching_results' in _dict:
            args['show_estimated_matching_results'] = _dict.get(
                'show_estimated_matching_results')
        if 'show_total_matching_documents' in _dict:
            args['show_total_matching_documents'] = _dict.get(
                'show_total_matching_documents')
        if 'results' in _dict:
            args['results'] = [
                QueryTopicAggregationResult.from_dict(v)
                for v in _dict.get('results')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryTopicAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'facet') and self.facet is not None:
            _dict['facet'] = self.facet
        if hasattr(self, 'time_segments') and self.time_segments is not None:
            _dict['time_segments'] = self.time_segments
        if hasattr(self, 'show_estimated_matching_results'
                  ) and self.show_estimated_matching_results is not None:
            _dict[
                'show_estimated_matching_results'] = self.show_estimated_matching_results
        if hasattr(self, 'show_total_matching_documents'
                  ) and self.show_total_matching_documents is not None:
            _dict[
                'show_total_matching_documents'] = self.show_total_matching_documents
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryTopicAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryTopicAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryTopicAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryAggregationQueryTrendAggregation(QueryAggregation):
    """
    Detects sharp and unexpected changes in the frequency of a facet or facet value over
    time based on the past history of frequency changes of the facet value.

    :attr str type: (optional) Specifies that the aggregation type is `trend`.
    :attr str facet: (optional) Specifies the `term` or `group_by` aggregation for
          the facet that you want to analyze.
    :attr str time_segments: (optional) Specifies the `timeslice` aggregation that
          defines the time segments.
    :attr bool show_estimated_matching_results: (optional) Indicates whether to
          include estimated matching result information.
    :attr bool show_total_matching_documents: (optional) Indicates whether to
          include total matching documents information.
    :attr List[QueryTrendAggregationResult] results: (optional) An array of
          aggregations.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 facet: str = None,
                 time_segments: str = None,
                 show_estimated_matching_results: bool = None,
                 show_total_matching_documents: bool = None,
                 results: List['QueryTrendAggregationResult'] = None) -> None:
        """
        Initialize a QueryAggregationQueryTrendAggregation object.

        :param str type: (optional) Specifies that the aggregation type is `trend`.
        :param str facet: (optional) Specifies the `term` or `group_by` aggregation
               for the facet that you want to analyze.
        :param str time_segments: (optional) Specifies the `timeslice` aggregation
               that defines the time segments.
        :param bool show_estimated_matching_results: (optional) Indicates whether
               to include estimated matching result information.
        :param bool show_total_matching_documents: (optional) Indicates whether to
               include total matching documents information.
        :param List[QueryTrendAggregationResult] results: (optional) An array of
               aggregations.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.facet = facet
        self.time_segments = time_segments
        self.show_estimated_matching_results = show_estimated_matching_results
        self.show_total_matching_documents = show_total_matching_documents
        self.results = results

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QueryAggregationQueryTrendAggregation':
        """Initialize a QueryAggregationQueryTrendAggregation object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'facet' in _dict:
            args['facet'] = _dict.get('facet')
        if 'time_segments' in _dict:
            args['time_segments'] = _dict.get('time_segments')
        if 'show_estimated_matching_results' in _dict:
            args['show_estimated_matching_results'] = _dict.get(
                'show_estimated_matching_results')
        if 'show_total_matching_documents' in _dict:
            args['show_total_matching_documents'] = _dict.get(
                'show_total_matching_documents')
        if 'results' in _dict:
            args['results'] = [
                QueryTrendAggregationResult.from_dict(v)
                for v in _dict.get('results')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregationQueryTrendAggregation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'facet') and self.facet is not None:
            _dict['facet'] = self.facet
        if hasattr(self, 'time_segments') and self.time_segments is not None:
            _dict['time_segments'] = self.time_segments
        if hasattr(self, 'show_estimated_matching_results'
                  ) and self.show_estimated_matching_results is not None:
            _dict[
                'show_estimated_matching_results'] = self.show_estimated_matching_results
        if hasattr(self, 'show_total_matching_documents'
                  ) and self.show_total_matching_documents is not None:
            _dict[
                'show_total_matching_documents'] = self.show_total_matching_documents
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QueryAggregationQueryTrendAggregation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QueryAggregationQueryTrendAggregation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QueryAggregationQueryTrendAggregation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
