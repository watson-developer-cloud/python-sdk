# coding: utf-8

# (C) Copyright IBM Corp. 2019.
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
IBM Watson&trade; Discovery for IBM Cloud Pak for Data is a cognitive search and content
analytics engine that you can add to applications to identify patterns, trends and
actionable insights to drive better decision-making. Securely unify structured and
unstructured data with pre-enriched content, and use a simplified query language to
eliminate the need for manual filtering of results.
"""

import json
from .common import get_sdk_headers
from enum import Enum
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime
from ibm_cloud_sdk_core import get_authenticator_from_environment
from ibm_cloud_sdk_core import read_external_sources
from os.path import basename

##############################################################################
# Service
##############################################################################


class DiscoveryV2(BaseService):
    """The Discovery V2 service."""

    default_service_url = None

    def __init__(
            self,
            version,
            authenticator=None,
    ):
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

        service_url = self.default_service_url
        disable_ssl_verification = False

        config = read_external_sources('discovery')
        if config.get('URL'):
            service_url = config.get('URL')
        if config.get('DISABLE_SSL'):
            disable_ssl_verification = config.get('DISABLE_SSL')

        if not authenticator:
            authenticator = get_authenticator_from_environment('discovery')

        BaseService.__init__(self,
                             service_url=service_url,
                             authenticator=authenticator,
                             disable_ssl_verification=disable_ssl_verification)
        self.version = version

    #########################
    # Collections
    #########################

    def list_collections(self, project_id, **kwargs):
        """
        List collections.

        Lists existing collections for the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'list_collections')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v2/projects/{0}/collections'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Queries
    #########################

    def query(self,
              project_id,
              *,
              collection_ids=None,
              filter=None,
              query=None,
              natural_language_query=None,
              aggregation=None,
              count=None,
              return_=None,
              offset=None,
              sort=None,
              highlight=None,
              spelling_suggestions=None,
              table_results=None,
              suggested_refinements=None,
              passages=None,
              **kwargs):
        """
        Query a project.

        By using this method, you can construct queries. For details, see the [Discovery
        documentation](https://cloud.ibm.com/docs/services/discovery-data?topic=discovery-data-query-concepts).

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param list[str] collection_ids: (optional) A comma-separated list of
               collection IDs to be queried against.
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
        :param str aggregation: (optional) An aggregation search that returns an
               exact answer by combining query search with filters. Useful for
               applications to build lists, tables, and time series. For a full list of
               possible aggregations, see the Query reference.
        :param int count: (optional) Number of results to return.
        :param list[str] return_: (optional) A list of the fields in the document
               hierarchy to return. If this parameter not specified, then all top-level
               fields are returned.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results.
        :param str sort: (optional) A comma-separated list of fields in the
               document to sort on. You can optionally specify a sort direction by
               prefixing the field with `-` for descending or `+` for ascending. Ascending
               is the default sort direction if no prefix is specified. This parameter
               cannot be used in the same query as the **bias** parameter.
        :param bool highlight: (optional) When `true`, a highlight field is
               returned for each result which contains the fields which match the query
               with `<em></em>` tags around the matching query terms.
        :param bool spelling_suggestions: (optional) When `true` and the
               **natural_language_query** parameter is used, the
               **natural_language_query** parameter is spell checked. The most likely
               correction is returned in the **suggested_query** field of the response (if
               one exists).
        :param QueryLargeTableResults table_results: (optional) Configuration for
               table retrieval.
        :param QueryLargeSuggestedRefinements suggested_refinements: (optional)
               Configuration for suggested refinements.
        :param QueryLargePassages passages: (optional) Configuration for passage
               retrieval.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if table_results is not None:
            table_results = self._convert_model(table_results)
        if suggested_refinements is not None:
            suggested_refinements = self._convert_model(suggested_refinements)
        if passages is not None:
            passages = self._convert_model(passages)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'query')
        headers.update(sdk_headers)

        params = {'version': self.version}

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
            'passages': passages
        }

        url = '/v2/projects/{0}/query'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_autocompletion(self,
                           project_id,
                           prefix,
                           *,
                           collection_ids=None,
                           field=None,
                           count=None,
                           **kwargs):
        """
        Get Autocomplete Suggestions.

        Returns completion query suggestions for the specified prefix.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str prefix: The prefix to use for autocompletion. For example, the
               prefix `Ho` could autocomplete to `Hot`, `Housing`, or `How do I upgrade`.
               Possible completions are.
        :param list[str] collection_ids: (optional) Comma separated list of the
               collection IDs. If this parameter is not specified, all collections in the
               project are used.
        :param str field: (optional) The field in the result documents that
               autocompletion suggestions are identified from.
        :param int count: (optional) The number of autocompletion suggestions to
               return.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if prefix is None:
            raise ValueError('prefix must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'get_autocompletion')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'prefix': prefix,
            'collection_ids': self._convert_list(collection_ids),
            'field': field,
            'count': count
        }

        url = '/v2/projects/{0}/autocompletion'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def query_notices(self,
                      project_id,
                      *,
                      filter=None,
                      query=None,
                      natural_language_query=None,
                      count=None,
                      offset=None,
                      **kwargs):
        """
        Query system notices.

        Queries for notices (errors or warnings) that might have been generated by the
        system. Notices are generated when ingesting documents and performing relevance
        training.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str filter: (optional) A cacheable query that excludes documents
               that don't mention the query content. Filter searches are better for
               metadata-type searches and for assessing the concepts in the data set.
        :param str query: (optional) A query search returns all documents in your
               data set with full enrichments and full text, but with the most relevant
               documents listed first.
        :param str natural_language_query: (optional) A natural language query that
               returns relevant documents by utilizing training data and natural language
               understanding.
        :param int count: (optional) Number of results to return. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param int offset: (optional) The number of query results to skip at the
               beginning. For example, if the total number of results that are returned is
               10 and the offset is 8, it returns the last two results. The maximum for
               the **count** and **offset** values together in any one query is **10000**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'query_notices')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'count': count,
            'offset': offset
        }

        url = '/v2/projects/{0}/notices'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def list_fields(self, project_id, *, collection_ids=None, **kwargs):
        """
        List fields.

        Gets a list of the unique fields (and their types) stored in the the specified
        collections.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param list[str] collection_ids: (optional) Comma separated list of the
               collection IDs. If this parameter is not specified, all collections in the
               project are used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'list_fields')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'collection_ids': self._convert_list(collection_ids)
        }

        url = '/v2/projects/{0}/fields'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Component settings
    #########################

    def get_component_settings(self, project_id, **kwargs):
        """
        Configuration settings for components.

        Returns default configuration settings for components.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2',
                                      'get_component_settings')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v2/projects/{0}/component_settings'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Documents
    #########################

    def add_document(self,
                     project_id,
                     collection_id,
                     *,
                     file=None,
                     filename=None,
                     file_content_type=None,
                     metadata=None,
                     x_watson_discovery_force=None,
                     **kwargs):
        """
        Add a document.

        Add a document to a collection with optional metadata.
         Returns immediately after the system has accepted the document for processing.
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
          If the document is uploaded to a collection that has it's data shared with
        another collection, the **X-Watson-Discovery-Force** header must be set to `true`.
         **Note:** Documents can be added with a specific **document_id** by using the
        **_/v2/projects/{project_id}/collections/{collection_id}/documents** method.
        **Note:** This operation only works on collections created to accept direct file
        uploads. It cannot be used to modify a collection that conects to an external
        source such as Microsoft SharePoint.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str collection_id: The ID of the collection.
        :param file file: (optional) The content of the document to ingest. The
               maximum supported file size when adding a file to a collection is 50
               megabytes, the maximum supported file size when testing a confiruration is
               1 megabyte. Files larger than the supported size are rejected.
        :param str filename: (optional) The filename for file.
        :param str file_content_type: (optional) The content type of file.
        :param str metadata: (optional) The maximum supported metadata file size is
               1 MB. Metadata parts larger than 1 MB are rejected. Example:  ``` {
                 "Creator": "Johnny Appleseed",
                 "Subject": "Apples"
               } ```.
        :param bool x_watson_discovery_force: (optional) When `true`, the uploaded
               document is added to the collection even if the data for that collection is
               shared with other collections.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {'X-Watson-Discovery-Force': x_watson_discovery_force}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'add_document')
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
            form_data.append(('metadata', (None, metadata, 'text/plain')))

        url = '/v2/projects/{0}/collections/{1}/documents'.format(
            *self._encode_path_vars(project_id, collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_document(self,
                        project_id,
                        collection_id,
                        document_id,
                        *,
                        file=None,
                        filename=None,
                        file_content_type=None,
                        metadata=None,
                        x_watson_discovery_force=None,
                        **kwargs):
        """
        Update a document.

        Replace an existing document or add a document with a specified **document_id**.
        Starts ingesting a document with optional metadata.
        If the document is uploaded to a collection that has it's data shared with another
        collection, the **X-Watson-Discovery-Force** header must be set to `true`.
        **Note:** When uploading a new document with this method it automatically replaces
        any document stored with the same **document_id** if it exists.
        **Note:** This operation only works on collections created to accept direct file
        uploads. It cannot be used to modify a collection that conects to an external
        source such as Microsoft SharePoint.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param file file: (optional) The content of the document to ingest. The
               maximum supported file size when adding a file to a collection is 50
               megabytes, the maximum supported file size when testing a confiruration is
               1 megabyte. Files larger than the supported size are rejected.
        :param str filename: (optional) The filename for file.
        :param str file_content_type: (optional) The content type of file.
        :param str metadata: (optional) The maximum supported metadata file size is
               1 MB. Metadata parts larger than 1 MB are rejected. Example:  ``` {
                 "Creator": "Johnny Appleseed",
                 "Subject": "Apples"
               } ```.
        :param bool x_watson_discovery_force: (optional) When `true`, the uploaded
               document is added to the collection even if the data for that collection is
               shared with other collections.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if document_id is None:
            raise ValueError('document_id must be provided')

        headers = {'X-Watson-Discovery-Force': x_watson_discovery_force}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'update_document')
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
            form_data.append(('metadata', (None, metadata, 'text/plain')))

        url = '/v2/projects/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(project_id, collection_id, document_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_document(self,
                        project_id,
                        collection_id,
                        document_id,
                        *,
                        x_watson_discovery_force=None,
                        **kwargs):
        """
        Delete a document.

        If the given document ID is invalid, or if the document is not found, then the a
        success response is returned (HTTP status code `200`) with the status set to
        'deleted'.
        **Note:** This operation only works on collections created to accept direct file
        uploads. It cannot be used to modify a collection that conects to an external
        source such as Microsoft SharePoint.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str collection_id: The ID of the collection.
        :param str document_id: The ID of the document.
        :param bool x_watson_discovery_force: (optional) When `true`, the uploaded
               document is added to the collection even if the data for that collection is
               shared with other collections.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if document_id is None:
            raise ValueError('document_id must be provided')

        headers = {'X-Watson-Discovery-Force': x_watson_discovery_force}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'delete_document')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v2/projects/{0}/collections/{1}/documents/{2}'.format(
            *self._encode_path_vars(project_id, collection_id, document_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Training data
    #########################

    def list_training_queries(self, project_id, **kwargs):
        """
        List training queries.

        List the training queries for the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2',
                                      'list_training_queries')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v2/projects/{0}/training_data/queries'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_training_queries(self, project_id, **kwargs):
        """
        Delete training queries.

        Removes all training queries for the specified project.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2',
                                      'delete_training_queries')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v2/projects/{0}/training_data/queries'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=False)
        response = self.send(request)
        return response

    def create_training_query(self,
                              project_id,
                              natural_language_query,
                              examples,
                              *,
                              filter=None,
                              **kwargs):
        """
        Create training query.

        Add a query to the training data for this project. The query can contain a filter
        and natural language query.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str natural_language_query: The natural text query for the training
               query.
        :param list[TrainingExample] examples: Array of training examples.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        examples = [self._convert_model(x) for x in examples]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2',
                                      'create_training_query')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'natural_language_query': natural_language_query,
            'examples': examples,
            'filter': filter
        }

        url = '/v2/projects/{0}/training_data/queries'.format(
            *self._encode_path_vars(project_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_training_query(self, project_id, query_id, **kwargs):
        """
        Get a training data query.

        Get details for a specific training data query, including the query string and all
        examples.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str query_id: The ID of the query used for training.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2', 'get_training_query')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v2/projects/{0}/training_data/queries/{1}'.format(
            *self._encode_path_vars(project_id, query_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_training_query(self,
                              project_id,
                              query_id,
                              natural_language_query,
                              examples,
                              *,
                              filter=None,
                              **kwargs):
        """
        Update a training query.

        Updates an existing training query and it's examples.

        :param str project_id: The ID of the project. This information can be found
               from the deploy page of the Discovery administrative tooling.
        :param str query_id: The ID of the query used for training.
        :param str natural_language_query: The natural text query for the training
               query.
        :param list[TrainingExample] examples: Array of training examples.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if project_id is None:
            raise ValueError('project_id must be provided')
        if query_id is None:
            raise ValueError('query_id must be provided')
        if natural_language_query is None:
            raise ValueError('natural_language_query must be provided')
        if examples is None:
            raise ValueError('examples must be provided')
        examples = [self._convert_model(x) for x in examples]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('discovery', 'V2',
                                      'update_training_query')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'natural_language_query': natural_language_query,
            'examples': examples,
            'filter': filter
        }

        url = '/v2/projects/{0}/training_data/queries/{1}'.format(
            *self._encode_path_vars(project_id, query_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
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


##############################################################################
# Models
##############################################################################


class Collection():
    """
    A collection for storing documents.

    :attr str collection_id: (optional) The unique identifier of the collection.
    :attr str name: (optional) The name of the collection.
    """

    def __init__(self, *, collection_id=None, name=None):
        """
        Initialize a Collection object.

        :param str collection_id: (optional) The unique identifier of the
               collection.
        :param str name: (optional) The name of the collection.
        """
        self.collection_id = collection_id
        self.name = name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Collection object from a json dictionary."""
        args = {}
        valid_keys = ['collection_id', 'name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Collection: '
                + ', '.join(bad_keys))
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
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


class Completions():
    """
    An object containing an array of autocompletion suggestions.

    :attr list[str] completions: (optional) Array of autcomplete suggestion based on
          the provided prefix.
    """

    def __init__(self, *, completions=None):
        """
        Initialize a Completions object.

        :param list[str] completions: (optional) Array of autcomplete suggestion
               based on the provided prefix.
        """
        self.completions = completions

    @classmethod
    def _from_dict(cls, _dict):
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'completions') and self.completions is not None:
            _dict['completions'] = self.completions
        return _dict

    def __str__(self):
        """Return a `str` version of this Completions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
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
                 name=None,
                 label=None,
                 multiple_selections_allowed=None,
                 visualization_type=None):
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
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsAggregation object from a json dictionary."""
        args = {}
        valid_keys = [
            'name', 'label', 'multiple_selections_allowed', 'visualization_type'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ComponentSettingsAggregation: '
                + ', '.join(bad_keys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ComponentSettingsAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class VisualizationTypeEnum(Enum):
        """
        Type of visualization to use when rendering the aggregation.
        """
        AUTO = "auto"
        FACET_TABLE = "facet_table"
        WORD_CLOUD = "word_cloud"
        MAP = "map"


class ComponentSettingsFieldsShown():
    """
    Fields shown in the results section of the UI.

    :attr ComponentSettingsFieldsShownBody body: (optional) Body label.
    :attr ComponentSettingsFieldsShownTitle title: (optional) Title label.
    """

    def __init__(self, *, body=None, title=None):
        """
        Initialize a ComponentSettingsFieldsShown object.

        :param ComponentSettingsFieldsShownBody body: (optional) Body label.
        :param ComponentSettingsFieldsShownTitle title: (optional) Title label.
        """
        self.body = body
        self.title = title

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsFieldsShown object from a json dictionary."""
        args = {}
        valid_keys = ['body', 'title']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ComponentSettingsFieldsShown: '
                + ', '.join(bad_keys))
        if 'body' in _dict:
            args['body'] = ComponentSettingsFieldsShownBody._from_dict(
                _dict.get('body'))
        if 'title' in _dict:
            args['title'] = ComponentSettingsFieldsShownTitle._from_dict(
                _dict.get('title'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body._to_dict()
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this ComponentSettingsFieldsShown object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComponentSettingsFieldsShownBody():
    """
    Body label.

    :attr bool use_passage: (optional) Use the whole passage as the body.
    :attr str field: (optional) Use a specific field as the title.
    """

    def __init__(self, *, use_passage=None, field=None):
        """
        Initialize a ComponentSettingsFieldsShownBody object.

        :param bool use_passage: (optional) Use the whole passage as the body.
        :param str field: (optional) Use a specific field as the title.
        """
        self.use_passage = use_passage
        self.field = field

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsFieldsShownBody object from a json dictionary."""
        args = {}
        valid_keys = ['use_passage', 'field']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ComponentSettingsFieldsShownBody: '
                + ', '.join(bad_keys))
        if 'use_passage' in _dict:
            args['use_passage'] = _dict.get('use_passage')
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'use_passage') and self.use_passage is not None:
            _dict['use_passage'] = self.use_passage
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        return _dict

    def __str__(self):
        """Return a `str` version of this ComponentSettingsFieldsShownBody object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComponentSettingsFieldsShownTitle():
    """
    Title label.

    :attr str field: (optional) Use a specific field as the title.
    """

    def __init__(self, *, field=None):
        """
        Initialize a ComponentSettingsFieldsShownTitle object.

        :param str field: (optional) Use a specific field as the title.
        """
        self.field = field

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsFieldsShownTitle object from a json dictionary."""
        args = {}
        valid_keys = ['field']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ComponentSettingsFieldsShownTitle: '
                + ', '.join(bad_keys))
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        return _dict

    def __str__(self):
        """Return a `str` version of this ComponentSettingsFieldsShownTitle object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComponentSettingsResponse():
    """
    A response containing the default component settings.

    :attr ComponentSettingsFieldsShown fields_shown: (optional) Fields shown in the
          results section of the UI.
    :attr bool autocomplete: (optional) Whether or not autocomplete is enabled.
    :attr bool structured_search: (optional) Whether or not structured search is
          enabled.
    :attr int results_per_page: (optional) Number or results shown per page.
    :attr list[ComponentSettingsAggregation] aggregations: (optional) a list of
          component setting aggregations.
    """

    def __init__(self,
                 *,
                 fields_shown=None,
                 autocomplete=None,
                 structured_search=None,
                 results_per_page=None,
                 aggregations=None):
        """
        Initialize a ComponentSettingsResponse object.

        :param ComponentSettingsFieldsShown fields_shown: (optional) Fields shown
               in the results section of the UI.
        :param bool autocomplete: (optional) Whether or not autocomplete is
               enabled.
        :param bool structured_search: (optional) Whether or not structured search
               is enabled.
        :param int results_per_page: (optional) Number or results shown per page.
        :param list[ComponentSettingsAggregation] aggregations: (optional) a list
               of component setting aggregations.
        """
        self.fields_shown = fields_shown
        self.autocomplete = autocomplete
        self.structured_search = structured_search
        self.results_per_page = results_per_page
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComponentSettingsResponse object from a json dictionary."""
        args = {}
        valid_keys = [
            'fields_shown', 'autocomplete', 'structured_search',
            'results_per_page', 'aggregations'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ComponentSettingsResponse: '
                + ', '.join(bad_keys))
        if 'fields_shown' in _dict:
            args['fields_shown'] = ComponentSettingsFieldsShown._from_dict(
                _dict.get('fields_shown'))
        if 'autocomplete' in _dict:
            args['autocomplete'] = _dict.get('autocomplete')
        if 'structured_search' in _dict:
            args['structured_search'] = _dict.get('structured_search')
        if 'results_per_page' in _dict:
            args['results_per_page'] = _dict.get('results_per_page')
        if 'aggregations' in _dict:
            args['aggregations'] = [
                ComponentSettingsAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fields_shown') and self.fields_shown is not None:
            _dict['fields_shown'] = self.fields_shown._to_dict()
        if hasattr(self, 'autocomplete') and self.autocomplete is not None:
            _dict['autocomplete'] = self.autocomplete
        if hasattr(self,
                   'structured_search') and self.structured_search is not None:
            _dict['structured_search'] = self.structured_search
        if hasattr(self,
                   'results_per_page') and self.results_per_page is not None:
            _dict['results_per_page'] = self.results_per_page
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def __str__(self):
        """Return a `str` version of this ComponentSettingsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteDocumentResponse():
    """
    Information returned when a document is deleted.

    :attr str document_id: (optional) The unique identifier of the document.
    :attr str status: (optional) Status of the document. A deleted document has the
          status deleted.
    """

    def __init__(self, *, document_id=None, status=None):
        """
        Initialize a DeleteDocumentResponse object.

        :param str document_id: (optional) The unique identifier of the document.
        :param str status: (optional) Status of the document. A deleted document
               has the status deleted.
        """
        self.document_id = document_id
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
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

    class StatusEnum(Enum):
        """
        Status of the document. A deleted document has the status deleted.
        """
        DELETED = "deleted"


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

    def __init__(self, *, document_id=None, status=None):
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
    def _from_dict(cls, _dict):
        """Initialize a DocumentAccepted object from a json dictionary."""
        args = {}
        valid_keys = ['document_id', 'status']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentAccepted: '
                + ', '.join(bad_keys))
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

    class StatusEnum(Enum):
        """
        Status of the document in the ingestion process. A status of `processing` is
        returned for documents that are ingested with a *version* date before
        `2019-01-01`. The `pending` status is returned for all others.
        """
        PROCESSING = "processing"
        PENDING = "pending"


class DocumentAttribute():
    """
    List of document attributes.

    :attr str type: (optional) The type of attribute.
    :attr str text: (optional) The text associated with the attribute.
    :attr TableElementLocation location: (optional) The numeric location of the
          identified element in the document, represented with two integers labeled
          `begin` and `end`.
    """

    def __init__(self, *, type=None, text=None, location=None):
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
    def _from_dict(cls, _dict):
        """Initialize a DocumentAttribute object from a json dictionary."""
        args = {}
        valid_keys = ['type', 'text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentAttribute: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = TableElementLocation._from_dict(
                _dict.get('location'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this DocumentAttribute object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Field():
    """
    Object containing field details.

    :attr str field: (optional) The name of the field.
    :attr str type: (optional) The type of the field.
    :attr str collection_id: (optional) The collection Id of the collection where
          the field was found.
    """

    def __init__(self, *, field=None, type=None, collection_id=None):
        """
        Initialize a Field object.

        :param str field: (optional) The name of the field.
        :param str type: (optional) The type of the field.
        :param str collection_id: (optional) The collection Id of the collection
               where the field was found.
        """
        self.field = field
        self.type = type
        self.collection_id = collection_id

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Field object from a json dictionary."""
        args = {}
        valid_keys = ['field', 'type', 'collection_id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Field: ' +
                ', '.join(bad_keys))
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
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


class ListCollectionsResponse():
    """
    Response object containing an array of collection details.

    :attr list[Collection] collections: (optional) An array containing information
          about each collection in the project.
    """

    def __init__(self, *, collections=None):
        """
        Initialize a ListCollectionsResponse object.

        :param list[Collection] collections: (optional) An array containing
               information about each collection in the project.
        """
        self.collections = collections

    @classmethod
    def _from_dict(cls, _dict):
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


class ListFieldsResponse():
    """
    The list of fetched fields.
    The fields are returned using a fully qualified name format, however, the format
    differs slightly from that used by the query operations.
      * Fields which contain nested objects are assigned a type of "nested".
      * Fields which belong to a nested object are prefixed with `.properties` (for
    example, `warnings.properties.severity` means that the `warnings` object has a
    property called `severity`).

    :attr list[Field] fields: (optional) An array containing information about each
          field in the collections.
    """

    def __init__(self, *, fields=None):
        """
        Initialize a ListFieldsResponse object.

        :param list[Field] fields: (optional) An array containing information about
               each field in the collections.
        """
        self.fields = fields

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFieldsResponse object from a json dictionary."""
        args = {}
        valid_keys = ['fields']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ListFieldsResponse: '
                + ', '.join(bad_keys))
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
        """Return a `str` version of this ListFieldsResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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
                 notice_id=None,
                 created=None,
                 document_id=None,
                 collection_id=None,
                 query_id=None,
                 severity=None,
                 step=None,
                 description=None):
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
        :param str collection_id: (optional) Unique identifier of the collection.
        :param str query_id: (optional) Unique identifier of the query used for
               relevance training.
        :param str severity: (optional) Severity level of the notice.
        :param str step: (optional) Ingestion or training step in which the notice
               occurred.
        :param str description: (optional) The description of the notice.
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
    def _from_dict(cls, _dict):
        """Initialize a Notice object from a json dictionary."""
        args = {}
        valid_keys = [
            'notice_id', 'created', 'document_id', 'collection_id', 'query_id',
            'severity', 'step', 'description'
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'notice_id') and self.notice_id is not None:
            _dict['notice_id'] = self.notice_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
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

    class SeverityEnum(Enum):
        """
        Severity level of the notice.
        """
        WARNING = "warning"
        ERROR = "error"


class QueryAggregation():
    """
    An abstract aggregation type produced by Discovery to analyze the input provided.

    :attr str type: The type of aggregation command used. Options include: term,
          histogram, timeslice, nested, filter, min, max, sum, average, unique_count, and
          top_hits.
    """

    def __init__(self, type):
        """
        Initialize a QueryAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        """
        self.type = type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['type']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryAggregation: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in QueryAggregation JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
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


class QueryCalculationAggregation():
    """
    Returns a scalar calculation across all documents for the field specified. Possible
    calculations include min, max, sum, average, and unique_count.

    :attr str field: The field to perform the calculation on.
    :attr float value: (optional) The value of the calculation.
    """

    def __init__(self, type, field, *, value=None):
        """
        Initialize a QueryCalculationAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        :param str field: The field to perform the calculation on.
        :param float value: (optional) The value of the calculation.
        """
        self.field = field
        self.value = value

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryCalculationAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['field', 'value']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryCalculationAggregation: '
                + ', '.join(bad_keys))
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in QueryCalculationAggregation JSON'
            )
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryCalculationAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryFilterAggregation():
    """
    A modifier that will narrow down the document set of the sub aggregations it precedes.

    :attr str match: The filter written in Discovery Query Language syntax applied
          to the documents before sub aggregations are run.
    :attr int matching_results: Number of documents matching the filter.
    :attr list[QueryAggregation] aggregations: (optional) An array of sub
          aggregations.
    """

    def __init__(self, type, match, matching_results, *, aggregations=None):
        """
        Initialize a QueryFilterAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        :param str match: The filter written in Discovery Query Language syntax
               applied to the documents before sub aggregations are run.
        :param int matching_results: Number of documents matching the filter.
        :param list[QueryAggregation] aggregations: (optional) An array of sub
               aggregations.
        """
        self.match = match
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryFilterAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['match', 'matching_results', 'aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryFilterAggregation: '
                + ', '.join(bad_keys))
        if 'match' in _dict:
            args['match'] = _dict.get('match')
        else:
            raise ValueError(
                'Required property \'match\' not present in QueryFilterAggregation JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryFilterAggregation JSON'
            )
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'match') and self.match is not None:
            _dict['match'] = self.match
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryFilterAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryHistogramAggregation():
    """
    Numeric interval segments to categorize documents by using field values from a single
    numeric field to describe the category.

    :attr str field: The numeric field name used to create the histogram.
    :attr int interval: The size of the sections the results are split into.
    :attr list[QueryHistogramAggregationResult] results: (optional) Array of numeric
          intervals.
    """

    def __init__(self, type, field, interval, *, results=None):
        """
        Initialize a QueryHistogramAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        :param str field: The numeric field name used to create the histogram.
        :param int interval: The size of the sections the results are split into.
        :param list[QueryHistogramAggregationResult] results: (optional) Array of
               numeric intervals.
        """
        self.field = field
        self.interval = interval
        self.results = results

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryHistogramAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['field', 'interval', 'results']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryHistogramAggregation: '
                + ', '.join(bad_keys))
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in QueryHistogramAggregation JSON'
            )
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        else:
            raise ValueError(
                'Required property \'interval\' not present in QueryHistogramAggregation JSON'
            )
        if 'results' in _dict:
            args['results'] = [
                QueryHistogramAggregationResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryHistogramAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryHistogramAggregationResult():
    """
    Histogram numeric interval result.

    :attr int key: The value of the upper bound for the numeric segment.
    :attr int matching_results: Number of documents with the specified key as the
          upper bound.
    :attr list[QueryAggregation] aggregations: (optional) An array of sub
          aggregations.
    """

    def __init__(self, key, matching_results, *, aggregations=None):
        """
        Initialize a QueryHistogramAggregationResult object.

        :param int key: The value of the upper bound for the numeric segment.
        :param int matching_results: Number of documents with the specified key as
               the upper bound.
        :param list[QueryAggregation] aggregations: (optional) An array of sub
               aggregations.
        """
        self.key = key
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryHistogramAggregationResult object from a json dictionary."""
        args = {}
        valid_keys = ['key', 'matching_results', 'aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryHistogramAggregationResult: '
                + ', '.join(bad_keys))
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
        """Return a `str` version of this QueryHistogramAggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryLargePassages():
    """
    Configuration for passage retrieval.

    :attr bool enabled: (optional) A passages query that returns the most relevant
          passages from the results.
    :attr bool per_document: (optional) When `true`, passages will be returned
          whithin their respective result.
    :attr int max_per_document: (optional) Maximum number of passages to return per
          result.
    :attr list[str] fields: (optional) A list of fields that passages are drawn
          from. If this parameter not specified, then all top-level fields are included.
    :attr int count: (optional) The maximum number of passages to return. The search
          returns fewer passages if the requested total is not found. The default is `10`.
          The maximum is `100`.
    :attr int characters: (optional) The approximate number of characters that any
          one passage will have.
    """

    def __init__(self,
                 *,
                 enabled=None,
                 per_document=None,
                 max_per_document=None,
                 fields=None,
                 count=None,
                 characters=None):
        """
        Initialize a QueryLargePassages object.

        :param bool enabled: (optional) A passages query that returns the most
               relevant passages from the results.
        :param bool per_document: (optional) When `true`, passages will be returned
               whithin their respective result.
        :param int max_per_document: (optional) Maximum number of passages to
               return per result.
        :param list[str] fields: (optional) A list of fields that passages are
               drawn from. If this parameter not specified, then all top-level fields are
               included.
        :param int count: (optional) The maximum number of passages to return. The
               search returns fewer passages if the requested total is not found. The
               default is `10`. The maximum is `100`.
        :param int characters: (optional) The approximate number of characters that
               any one passage will have.
        """
        self.enabled = enabled
        self.per_document = per_document
        self.max_per_document = max_per_document
        self.fields = fields
        self.count = count
        self.characters = characters

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryLargePassages object from a json dictionary."""
        args = {}
        valid_keys = [
            'enabled', 'per_document', 'max_per_document', 'fields', 'count',
            'characters'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryLargePassages: '
                + ', '.join(bad_keys))
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
        return cls(**args)

    def _to_dict(self):
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
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryLargePassages object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryLargeSuggestedRefinements():
    """
    Configuration for suggested refinements.

    :attr bool enabled: (optional) Whether to perform suggested refinements.
    :attr int count: (optional) Maximum number of suggested refinements texts to be
          returned. The default is `10`. The maximum is `100`.
    """

    def __init__(self, *, enabled=None, count=None):
        """
        Initialize a QueryLargeSuggestedRefinements object.

        :param bool enabled: (optional) Whether to perform suggested refinements.
        :param int count: (optional) Maximum number of suggested refinements texts
               to be returned. The default is `10`. The maximum is `100`.
        """
        self.enabled = enabled
        self.count = count

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryLargeSuggestedRefinements object from a json dictionary."""
        args = {}
        valid_keys = ['enabled', 'count']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryLargeSuggestedRefinements: '
                + ', '.join(bad_keys))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryLargeSuggestedRefinements object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryLargeTableResults():
    """
    Configuration for table retrieval.

    :attr bool enabled: (optional) Whether to enable table retrieval.
    :attr int count: (optional) Maximum number of tables to return.
    """

    def __init__(self, *, enabled=None, count=None):
        """
        Initialize a QueryLargeTableResults object.

        :param bool enabled: (optional) Whether to enable table retrieval.
        :param int count: (optional) Maximum number of tables to return.
        """
        self.enabled = enabled
        self.count = count

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryLargeTableResults object from a json dictionary."""
        args = {}
        valid_keys = ['enabled', 'count']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryLargeTableResults: '
                + ', '.join(bad_keys))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryLargeTableResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryNestedAggregation():
    """
    A restriction that alter the document set used for sub aggregations it precedes to
    nested documents found in the field specified.

    :attr str path: The path to the document field to scope sub aggregations to.
    :attr int matching_results: Number of nested documents found in the specified
          field.
    :attr list[QueryAggregation] aggregations: (optional) An array of sub
          aggregations.
    """

    def __init__(self, type, path, matching_results, *, aggregations=None):
        """
        Initialize a QueryNestedAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        :param str path: The path to the document field to scope sub aggregations
               to.
        :param int matching_results: Number of nested documents found in the
               specified field.
        :param list[QueryAggregation] aggregations: (optional) An array of sub
               aggregations.
        """
        self.path = path
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryNestedAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['path', 'matching_results', 'aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryNestedAggregation: '
                + ', '.join(bad_keys))
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        else:
            raise ValueError(
                'Required property \'path\' not present in QueryNestedAggregation JSON'
            )
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryNestedAggregation JSON'
            )
        if 'aggregations' in _dict:
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'aggregations') and self.aggregations is not None:
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryNestedAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryNoticesResponse():
    """
    Object containing notice query results.

    :attr int matching_results: (optional) The number of matching results.
    :attr list[Notice] notices: (optional) Array of document results that match the
          query.
    """

    def __init__(self, *, matching_results=None, notices=None):
        """
        Initialize a QueryNoticesResponse object.

        :param int matching_results: (optional) The number of matching results.
        :param list[Notice] notices: (optional) Array of document results that
               match the query.
        """
        self.matching_results = matching_results
        self.notices = notices

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryNoticesResponse object from a json dictionary."""
        args = {}
        valid_keys = ['matching_results', 'notices']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryNoticesResponse: '
                + ', '.join(bad_keys))
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        if 'notices' in _dict:
            args['notices'] = [
                Notice._from_dict(x) for x in (_dict.get('notices'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'notices') and self.notices is not None:
            _dict['notices'] = [x._to_dict() for x in self.notices]
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


class QueryResponse():
    """
    A response containing the documents and aggregations for the query.

    :attr int matching_results: (optional) The number of matching results for the
          query.
    :attr list[QueryResult] results: (optional) Array of document results for the
          query.
    :attr list[QueryAggregation] aggregations: (optional) Array of aggregations for
          the query.
    :attr RetrievalDetails retrieval_details: (optional) An object contain retrieval
          type information.
    :attr str suggested_query: (optional) Suggested correction to the submitted
          **natural_language_query** value.
    :attr list[QuerySuggestedRefinement] suggested_refinements: (optional) Array of
          suggested refinments.
    :attr list[QueryTableResult] table_results: (optional) Array of table results.
    """

    def __init__(self,
                 *,
                 matching_results=None,
                 results=None,
                 aggregations=None,
                 retrieval_details=None,
                 suggested_query=None,
                 suggested_refinements=None,
                 table_results=None):
        """
        Initialize a QueryResponse object.

        :param int matching_results: (optional) The number of matching results for
               the query.
        :param list[QueryResult] results: (optional) Array of document results for
               the query.
        :param list[QueryAggregation] aggregations: (optional) Array of
               aggregations for the query.
        :param RetrievalDetails retrieval_details: (optional) An object contain
               retrieval type information.
        :param str suggested_query: (optional) Suggested correction to the
               submitted **natural_language_query** value.
        :param list[QuerySuggestedRefinement] suggested_refinements: (optional)
               Array of suggested refinments.
        :param list[QueryTableResult] table_results: (optional) Array of table
               results.
        """
        self.matching_results = matching_results
        self.results = results
        self.aggregations = aggregations
        self.retrieval_details = retrieval_details
        self.suggested_query = suggested_query
        self.suggested_refinements = suggested_refinements
        self.table_results = table_results

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResponse object from a json dictionary."""
        args = {}
        valid_keys = [
            'matching_results', 'results', 'aggregations', 'retrieval_details',
            'suggested_query', 'suggested_refinements', 'table_results'
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
        if 'retrieval_details' in _dict:
            args['retrieval_details'] = RetrievalDetails._from_dict(
                _dict.get('retrieval_details'))
        if 'suggested_query' in _dict:
            args['suggested_query'] = _dict.get('suggested_query')
        if 'suggested_refinements' in _dict:
            args['suggested_refinements'] = [
                QuerySuggestedRefinement._from_dict(x)
                for x in (_dict.get('suggested_refinements'))
            ]
        if 'table_results' in _dict:
            args['table_results'] = [
                QueryTableResult._from_dict(x)
                for x in (_dict.get('table_results'))
            ]
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
        if hasattr(self,
                   'retrieval_details') and self.retrieval_details is not None:
            _dict['retrieval_details'] = self.retrieval_details._to_dict()
        if hasattr(self,
                   'suggested_query') and self.suggested_query is not None:
            _dict['suggested_query'] = self.suggested_query
        if hasattr(self, 'suggested_refinements'
                  ) and self.suggested_refinements is not None:
            _dict['suggested_refinements'] = [
                x._to_dict() for x in self.suggested_refinements
            ]
        if hasattr(self, 'table_results') and self.table_results is not None:
            _dict['table_results'] = [x._to_dict() for x in self.table_results]
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


class QueryResult():
    """
    Result document for the specified query.

    :attr str document_id: The unique identifier of the document.
    :attr dict metadata: (optional) Metadata of the document.
    :attr QueryResultMetadata result_metadata: Metadata of a query result.
    :attr list[QueryResultPassage] document_passages: (optional) Passages returned
          by Discovery.
    """

    def __init__(self,
                 document_id,
                 result_metadata,
                 *,
                 metadata=None,
                 document_passages=None,
                 **kwargs):
        """
        Initialize a QueryResult object.

        :param str document_id: The unique identifier of the document.
        :param QueryResultMetadata result_metadata: Metadata of a query result.
        :param dict metadata: (optional) Metadata of the document.
        :param list[QueryResultPassage] document_passages: (optional) Passages
               returned by Discovery.
        :param **kwargs: (optional) Any additional properties.
        """
        self.document_id = document_id
        self.metadata = metadata
        self.result_metadata = result_metadata
        self.document_passages = document_passages
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResult object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'document_id' in _dict:
            args['document_id'] = _dict.get('document_id')
            del xtra['document_id']
        else:
            raise ValueError(
                'Required property \'document_id\' not present in QueryResult JSON'
            )
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
            del xtra['metadata']
        if 'result_metadata' in _dict:
            args['result_metadata'] = QueryResultMetadata._from_dict(
                _dict.get('result_metadata'))
            del xtra['result_metadata']
        else:
            raise ValueError(
                'Required property \'result_metadata\' not present in QueryResult JSON'
            )
        if 'document_passages' in _dict:
            args['document_passages'] = [
                QueryResultPassage._from_dict(x)
                for x in (_dict.get('document_passages'))
            ]
            del xtra['document_passages']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self,
                   'result_metadata') and self.result_metadata is not None:
            _dict['result_metadata'] = self.result_metadata._to_dict()
        if hasattr(self,
                   'document_passages') and self.document_passages is not None:
            _dict['document_passages'] = [
                x._to_dict() for x in self.document_passages
            ]
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {
            'document_id', 'metadata', 'result_metadata', 'document_passages'
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


class QueryResultMetadata():
    """
    Metadata of a query result.

    :attr str document_retrieval_source: (optional) The document retrieval source
          that produced this search result.
    :attr str collection_id: The collection id associated with this training data
          set.
    :attr float confidence: (optional) The confidence score for the given result.
          Calculated based on how relevant the result is estimated to be. confidence can
          range from `0.0` to `1.0`. The higher the number, the more relevant the
          document. The `confidence` value for a result was calculated using the model
          specified in the `document_retrieval_strategy` field of the result set. This
          field is only returned if the **natural_language_query** parameter is specified
          in the query.
    """

    def __init__(self,
                 collection_id,
                 *,
                 document_retrieval_source=None,
                 confidence=None):
        """
        Initialize a QueryResultMetadata object.

        :param str collection_id: The collection id associated with this training
               data set.
        :param str document_retrieval_source: (optional) The document retrieval
               source that produced this search result.
        :param float confidence: (optional) The confidence score for the given
               result. Calculated based on how relevant the result is estimated to be.
               confidence can range from `0.0` to `1.0`. The higher the number, the more
               relevant the document. The `confidence` value for a result was calculated
               using the model specified in the `document_retrieval_strategy` field of the
               result set. This field is only returned if the **natural_language_query**
               parameter is specified in the query.
        """
        self.document_retrieval_source = document_retrieval_source
        self.collection_id = collection_id
        self.confidence = confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResultMetadata object from a json dictionary."""
        args = {}
        valid_keys = [
            'document_retrieval_source', 'collection_id', 'confidence'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryResultMetadata: '
                + ', '.join(bad_keys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this QueryResultMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DocumentRetrievalSourceEnum(Enum):
        """
        The document retrieval source that produced this search result.
        """
        SEARCH = "search"
        CURATION = "curation"


class QueryResultPassage():
    """
    A passage query result.

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
                 passage_text=None,
                 start_offset=None,
                 end_offset=None,
                 field=None):
        """
        Initialize a QueryResultPassage object.

        :param str passage_text: (optional) The content of the extracted passage.
        :param int start_offset: (optional) The position of the first character of
               the extracted passage in the originating field.
        :param int end_offset: (optional) The position of the last character of the
               extracted passage in the originating field.
        :param str field: (optional) The label of the field from which the passage
               has been extracted.
        """
        self.passage_text = passage_text
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.field = field

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryResultPassage object from a json dictionary."""
        args = {}
        valid_keys = ['passage_text', 'start_offset', 'end_offset', 'field']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryResultPassage: '
                + ', '.join(bad_keys))
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
        """Return a `str` version of this QueryResultPassage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QuerySuggestedRefinement():
    """
    A suggested additional query term or terms user to filter results.

    :attr str text: (optional) The text used to filter.
    """

    def __init__(self, *, text=None):
        """
        Initialize a QuerySuggestedRefinement object.

        :param str text: (optional) The text used to filter.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QuerySuggestedRefinement object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QuerySuggestedRefinement: '
                + ', '.join(bad_keys))
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
        """Return a `str` version of this QuerySuggestedRefinement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
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
                 table_id=None,
                 source_document_id=None,
                 collection_id=None,
                 table_html=None,
                 table_html_offset=None,
                 table=None):
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
    def _from_dict(cls, _dict):
        """Initialize a QueryTableResult object from a json dictionary."""
        args = {}
        valid_keys = [
            'table_id', 'source_document_id', 'collection_id', 'table_html',
            'table_html_offset', 'table'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryTableResult: '
                + ', '.join(bad_keys))
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
            args['table'] = TableResultTable._from_dict(_dict.get('table'))
        return cls(**args)

    def _to_dict(self):
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
            _dict['table'] = self.table._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryTableResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTermAggregation():
    """
    Returns the top values for the field specified.

    :attr str field: The field in the document used to generate top values from.
    :attr int count: (optional) The number of top values returned.
    :attr list[QueryTermAggregationResult] results: (optional) Array of top values
          for the field.
    """

    def __init__(self, type, field, *, count=None, results=None):
        """
        Initialize a QueryTermAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        :param str field: The field in the document used to generate top values
               from.
        :param int count: (optional) The number of top values returned.
        :param list[QueryTermAggregationResult] results: (optional) Array of top
               values for the field.
        """
        self.field = field
        self.count = count
        self.results = results

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTermAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['field', 'count', 'results']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryTermAggregation: '
                + ', '.join(bad_keys))
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in QueryTermAggregation JSON'
            )
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'results' in _dict:
            args['results'] = [
                QueryTermAggregationResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryTermAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTermAggregationResult():
    """
    Top value result for the term aggregation.

    :attr str key: Value of the field with a non-zero frequency in the document set.
    :attr int matching_results: Number of documents containing the 'key'.
    :attr list[QueryAggregation] aggregations: (optional) An array of sub
          aggregations.
    """

    def __init__(self, key, matching_results, *, aggregations=None):
        """
        Initialize a QueryTermAggregationResult object.

        :param str key: Value of the field with a non-zero frequency in the
               document set.
        :param int matching_results: Number of documents containing the 'key'.
        :param list[QueryAggregation] aggregations: (optional) An array of sub
               aggregations.
        """
        self.key = key
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTermAggregationResult object from a json dictionary."""
        args = {}
        valid_keys = ['key', 'matching_results', 'aggregations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryTermAggregationResult: '
                + ', '.join(bad_keys))
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
        """Return a `str` version of this QueryTermAggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTimesliceAggregation():
    """
    A specialized histogram aggregation that uses dates to create interval segments.

    :attr str field: The date field name used to create the timeslice.
    :attr str interval: The date interval value. Valid values are seconds, minutes,
          hours, days, weeks, and years.
    :attr list[QueryTimesliceAggregationResult] results: (optional) Array of
          aggregation results.
    """

    def __init__(self, type, field, interval, *, results=None):
        """
        Initialize a QueryTimesliceAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        :param str field: The date field name used to create the timeslice.
        :param str interval: The date interval value. Valid values are seconds,
               minutes, hours, days, weeks, and years.
        :param list[QueryTimesliceAggregationResult] results: (optional) Array of
               aggregation results.
        """
        self.field = field
        self.interval = interval
        self.results = results

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTimesliceAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['field', 'interval', 'results']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryTimesliceAggregation: '
                + ', '.join(bad_keys))
        if 'field' in _dict:
            args['field'] = _dict.get('field')
        else:
            raise ValueError(
                'Required property \'field\' not present in QueryTimesliceAggregation JSON'
            )
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        else:
            raise ValueError(
                'Required property \'interval\' not present in QueryTimesliceAggregation JSON'
            )
        if 'results' in _dict:
            args['results'] = [
                QueryTimesliceAggregationResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'field') and self.field is not None:
            _dict['field'] = self.field
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryTimesliceAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTimesliceAggregationResult():
    """
    A timeslice interval segment.

    :attr str key_as_string: String date value of the upper bound for the timeslice
          interval in ISO-8601 format.
    :attr int key: Numeric date value of the upper bound for the timeslice interval
          in UNIX miliseconds since epoch.
    :attr int matching_results: Number of documents with the specified key as the
          upper bound.
    :attr list[QueryAggregation] aggregations: (optional) An array of sub
          aggregations.
    """

    def __init__(self,
                 key_as_string,
                 key,
                 matching_results,
                 *,
                 aggregations=None):
        """
        Initialize a QueryTimesliceAggregationResult object.

        :param str key_as_string: String date value of the upper bound for the
               timeslice interval in ISO-8601 format.
        :param int key: Numeric date value of the upper bound for the timeslice
               interval in UNIX miliseconds since epoch.
        :param int matching_results: Number of documents with the specified key as
               the upper bound.
        :param list[QueryAggregation] aggregations: (optional) An array of sub
               aggregations.
        """
        self.key_as_string = key_as_string
        self.key = key
        self.matching_results = matching_results
        self.aggregations = aggregations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTimesliceAggregationResult object from a json dictionary."""
        args = {}
        valid_keys = [
            'key_as_string', 'key', 'matching_results', 'aggregations'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryTimesliceAggregationResult: '
                + ', '.join(bad_keys))
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
            args['aggregations'] = [
                QueryAggregation._from_dict(x)
                for x in (_dict.get('aggregations'))
            ]
        return cls(**args)

    def _to_dict(self):
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
            _dict['aggregations'] = [x._to_dict() for x in self.aggregations]
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryTimesliceAggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTopHitsAggregation():
    """
    Returns the top documents ranked by the score of the query.

    :attr int size: The number of documents to return.
    :attr QueryTopHitsAggregationResult hits: (optional)
    """

    def __init__(self, type, size, *, hits=None):
        """
        Initialize a QueryTopHitsAggregation object.

        :param str type: The type of aggregation command used. Options include:
               term, histogram, timeslice, nested, filter, min, max, sum, average,
               unique_count, and top_hits.
        :param int size: The number of documents to return.
        :param QueryTopHitsAggregationResult hits: (optional)
        """
        self.size = size
        self.hits = hits

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTopHitsAggregation object from a json dictionary."""
        args = {}
        valid_keys = ['size', 'hits']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryTopHitsAggregation: '
                + ', '.join(bad_keys))
        if 'size' in _dict:
            args['size'] = _dict.get('size')
        else:
            raise ValueError(
                'Required property \'size\' not present in QueryTopHitsAggregation JSON'
            )
        if 'hits' in _dict:
            args['hits'] = QueryTopHitsAggregationResult._from_dict(
                _dict.get('hits'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'size') and self.size is not None:
            _dict['size'] = self.size
        if hasattr(self, 'hits') and self.hits is not None:
            _dict['hits'] = self.hits._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryTopHitsAggregation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QueryTopHitsAggregationResult():
    """
    A query response containing the matching documents for the preceding aggregations.

    :attr int matching_results: Number of matching results.
    :attr list[dict] hits: (optional) An array of the document results.
    """

    def __init__(self, matching_results, *, hits=None):
        """
        Initialize a QueryTopHitsAggregationResult object.

        :param int matching_results: Number of matching results.
        :param list[dict] hits: (optional) An array of the document results.
        """
        self.matching_results = matching_results
        self.hits = hits

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QueryTopHitsAggregationResult object from a json dictionary."""
        args = {}
        valid_keys = ['matching_results', 'hits']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class QueryTopHitsAggregationResult: '
                + ', '.join(bad_keys))
        if 'matching_results' in _dict:
            args['matching_results'] = _dict.get('matching_results')
        else:
            raise ValueError(
                'Required property \'matching_results\' not present in QueryTopHitsAggregationResult JSON'
            )
        if 'hits' in _dict:
            args['hits'] = _dict.get('hits')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'matching_results') and self.matching_results is not None:
            _dict['matching_results'] = self.matching_results
        if hasattr(self, 'hits') and self.hits is not None:
            _dict['hits'] = self.hits
        return _dict

    def __str__(self):
        """Return a `str` version of this QueryTopHitsAggregationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RetrievalDetails():
    """
    An object contain retrieval type information.

    :attr str document_retrieval_strategy: (optional) Indentifies the document
          retrieval strategy used for this query. `relevancy_training` indicates that the
          results were returned using a relevancy trained model.
           **Note**: In the event of trained collections being queried, but the trained
          model is not used to return results, the **document_retrieval_strategy** will be
          listed as `untrained`.
    """

    def __init__(self, *, document_retrieval_strategy=None):
        """
        Initialize a RetrievalDetails object.

        :param str document_retrieval_strategy: (optional) Indentifies the document
               retrieval strategy used for this query. `relevancy_training` indicates that
               the results were returned using a relevancy trained model.
                **Note**: In the event of trained collections being queried, but the
               trained model is not used to return results, the
               **document_retrieval_strategy** will be listed as `untrained`.
        """
        self.document_retrieval_strategy = document_retrieval_strategy

    @classmethod
    def _from_dict(cls, _dict):
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_retrieval_strategy'
                  ) and self.document_retrieval_strategy is not None:
            _dict[
                'document_retrieval_strategy'] = self.document_retrieval_strategy
        return _dict

    def __str__(self):
        """Return a `str` version of this RetrievalDetails object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class DocumentRetrievalStrategyEnum(Enum):
        """
        Indentifies the document retrieval strategy used for this query.
        `relevancy_training` indicates that the results were returned using a relevancy
        trained model.
         **Note**: In the event of trained collections being queried, but the trained
        model is not used to return results, the **document_retrieval_strategy** will be
        listed as `untrained`.
        """
        UNTRAINED = "untrained"
        RELEVANCY_TRAINING = "relevancy_training"


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
    :attr list[TableRowHeaderIds] row_header_ids: (optional) A list of table row
          header ids.
    :attr list[TableRowHeaderTexts] row_header_texts: (optional) A list of table row
          header texts.
    :attr list[TableRowHeaderTextsNormalized] row_header_texts_normalized:
          (optional) A list of table row header texts normalized.
    :attr list[TableColumnHeaderIds] column_header_ids: (optional) A list of table
          column header ids.
    :attr list[TableColumnHeaderTexts] column_header_texts: (optional) A list of
          table column header texts.
    :attr list[TableColumnHeaderTextsNormalized] column_header_texts_normalized:
          (optional) A list of table column header texts normalized.
    :attr list[DocumentAttribute] attributes: (optional) A list of document
          attributes.
    """

    def __init__(self,
                 *,
                 cell_id=None,
                 location=None,
                 text=None,
                 row_index_begin=None,
                 row_index_end=None,
                 column_index_begin=None,
                 column_index_end=None,
                 row_header_ids=None,
                 row_header_texts=None,
                 row_header_texts_normalized=None,
                 column_header_ids=None,
                 column_header_texts=None,
                 column_header_texts_normalized=None,
                 attributes=None):
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
        :param list[TableRowHeaderIds] row_header_ids: (optional) A list of table
               row header ids.
        :param list[TableRowHeaderTexts] row_header_texts: (optional) A list of
               table row header texts.
        :param list[TableRowHeaderTextsNormalized] row_header_texts_normalized:
               (optional) A list of table row header texts normalized.
        :param list[TableColumnHeaderIds] column_header_ids: (optional) A list of
               table column header ids.
        :param list[TableColumnHeaderTexts] column_header_texts: (optional) A list
               of table column header texts.
        :param list[TableColumnHeaderTextsNormalized]
               column_header_texts_normalized: (optional) A list of table column header
               texts normalized.
        :param list[DocumentAttribute] attributes: (optional) A list of document
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
    def _from_dict(cls, _dict):
        """Initialize a TableBodyCells object from a json dictionary."""
        args = {}
        valid_keys = [
            'cell_id', 'location', 'text', 'row_index_begin', 'row_index_end',
            'column_index_begin', 'column_index_end', 'row_header_ids',
            'row_header_texts', 'row_header_texts_normalized',
            'column_header_ids', 'column_header_texts',
            'column_header_texts_normalized', 'attributes'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableBodyCells: '
                + ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation._from_dict(
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
                TableRowHeaderIds._from_dict(x)
                for x in (_dict.get('row_header_ids'))
            ]
        if 'row_header_texts' in _dict:
            args['row_header_texts'] = [
                TableRowHeaderTexts._from_dict(x)
                for x in (_dict.get('row_header_texts'))
            ]
        if 'row_header_texts_normalized' in _dict:
            args['row_header_texts_normalized'] = [
                TableRowHeaderTextsNormalized._from_dict(x)
                for x in (_dict.get('row_header_texts_normalized'))
            ]
        if 'column_header_ids' in _dict:
            args['column_header_ids'] = [
                TableColumnHeaderIds._from_dict(x)
                for x in (_dict.get('column_header_ids'))
            ]
        if 'column_header_texts' in _dict:
            args['column_header_texts'] = [
                TableColumnHeaderTexts._from_dict(x)
                for x in (_dict.get('column_header_texts'))
            ]
        if 'column_header_texts_normalized' in _dict:
            args['column_header_texts_normalized'] = [
                TableColumnHeaderTextsNormalized._from_dict(x)
                for x in (_dict.get('column_header_texts_normalized'))
            ]
        if 'attributes' in _dict:
            args['attributes'] = [
                DocumentAttribute._from_dict(x)
                for x in (_dict.get('attributes'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
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
            _dict['row_header_ids'] = [
                x._to_dict() for x in self.row_header_ids
            ]
        if hasattr(self,
                   'row_header_texts') and self.row_header_texts is not None:
            _dict['row_header_texts'] = [
                x._to_dict() for x in self.row_header_texts
            ]
        if hasattr(self, 'row_header_texts_normalized'
                  ) and self.row_header_texts_normalized is not None:
            _dict['row_header_texts_normalized'] = [
                x._to_dict() for x in self.row_header_texts_normalized
            ]
        if hasattr(self,
                   'column_header_ids') and self.column_header_ids is not None:
            _dict['column_header_ids'] = [
                x._to_dict() for x in self.column_header_ids
            ]
        if hasattr(
                self,
                'column_header_texts') and self.column_header_texts is not None:
            _dict['column_header_texts'] = [
                x._to_dict() for x in self.column_header_texts
            ]
        if hasattr(self, 'column_header_texts_normalized'
                  ) and self.column_header_texts_normalized is not None:
            _dict['column_header_texts_normalized'] = [
                x._to_dict() for x in self.column_header_texts_normalized
            ]
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x._to_dict() for x in self.attributes]
        return _dict

    def __str__(self):
        """Return a `str` version of this TableBodyCells object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
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

    def __init__(self, *, cell_id=None, location=None, text=None):
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
    def _from_dict(cls, _dict):
        """Initialize a TableCellKey object from a json dictionary."""
        args = {}
        valid_keys = ['cell_id', 'location', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableCellKey: '
                + ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation._from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this TableCellKey object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
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

    def __init__(self, *, cell_id=None, location=None, text=None):
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
    def _from_dict(cls, _dict):
        """Initialize a TableCellValues object from a json dictionary."""
        args = {}
        valid_keys = ['cell_id', 'location', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableCellValues: '
                + ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation._from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this TableCellValues object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaderIds():
    """
    An array of values, each being the `id` value of a column header that is applicable to
    the current cell.

    :attr str id: (optional) The `id` value of a column header.
    """

    def __init__(self, *, id=None):
        """
        Initialize a TableColumnHeaderIds object.

        :param str id: (optional) The `id` value of a column header.
        """
        self.id = id

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaderIds object from a json dictionary."""
        args = {}
        valid_keys = ['id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableColumnHeaderIds: '
                + ', '.join(bad_keys))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def __str__(self):
        """Return a `str` version of this TableColumnHeaderIds object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaderTexts():
    """
    An array of values, each being the `text` value of a column header that is applicable
    to the current cell.

    :attr str text: (optional) The `text` value of a column header.
    """

    def __init__(self, *, text=None):
        """
        Initialize a TableColumnHeaderTexts object.

        :param str text: (optional) The `text` value of a column header.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaderTexts object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableColumnHeaderTexts: '
                + ', '.join(bad_keys))
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
        """Return a `str` version of this TableColumnHeaderTexts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaderTextsNormalized():
    """
    If you provide customization input, the normalized version of the column header texts
    according to the customization; otherwise, the same value as `column_header_texts`.

    :attr str text_normalized: (optional) The normalized version of a column header
          text.
    """

    def __init__(self, *, text_normalized=None):
        """
        Initialize a TableColumnHeaderTextsNormalized object.

        :param str text_normalized: (optional) The normalized version of a column
               header text.
        """
        self.text_normalized = text_normalized

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaderTextsNormalized object from a json dictionary."""
        args = {}
        valid_keys = ['text_normalized']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableColumnHeaderTextsNormalized: '
                + ', '.join(bad_keys))
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        return _dict

    def __str__(self):
        """Return a `str` version of this TableColumnHeaderTextsNormalized object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableColumnHeaders():
    """
    Column-level cells, each applicable as a header to other cells in the same column as
    itself, of the current table.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr object location: (optional) The location of the column header cell in the
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
                 cell_id=None,
                 location=None,
                 text=None,
                 text_normalized=None,
                 row_index_begin=None,
                 row_index_end=None,
                 column_index_begin=None,
                 column_index_end=None):
        """
        Initialize a TableColumnHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param object location: (optional) The location of the column header cell
               in the current table as defined by its `begin` and `end` offsets,
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
    def _from_dict(cls, _dict):
        """Initialize a TableColumnHeaders object from a json dictionary."""
        args = {}
        valid_keys = [
            'cell_id', 'location', 'text', 'text_normalized', 'row_index_begin',
            'row_index_end', 'column_index_begin', 'column_index_end'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableColumnHeaders: '
                + ', '.join(bad_keys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this TableColumnHeaders object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableElementLocation():
    """
    The numeric location of the identified element in the document, represented with two
    integers labeled `begin` and `end`.

    :attr int begin: The element's `begin` index.
    :attr int end: The element's `end` index.
    """

    def __init__(self, begin, end):
        """
        Initialize a TableElementLocation object.

        :param int begin: The element's `begin` index.
        :param int end: The element's `end` index.
        """
        self.begin = begin
        self.end = end

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableElementLocation object from a json dictionary."""
        args = {}
        valid_keys = ['begin', 'end']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableElementLocation: '
                + ', '.join(bad_keys))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        return _dict

    def __str__(self):
        """Return a `str` version of this TableElementLocation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableHeaders():
    """
    The contents of the current table's header.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr object location: (optional) The location of the table header cell in the
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
                 cell_id=None,
                 location=None,
                 text=None,
                 row_index_begin=None,
                 row_index_end=None,
                 column_index_begin=None,
                 column_index_end=None):
        """
        Initialize a TableHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param object location: (optional) The location of the table header cell in
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
    def _from_dict(cls, _dict):
        """Initialize a TableHeaders object from a json dictionary."""
        args = {}
        valid_keys = [
            'cell_id', 'location', 'text', 'row_index_begin', 'row_index_end',
            'column_index_begin', 'column_index_end'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableHeaders: '
                + ', '.join(bad_keys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this TableHeaders object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableKeyValuePairs():
    """
    Key-value pairs detected across cell boundaries.

    :attr TableCellKey key: (optional) A key in a key-value pair.
    :attr list[TableCellValues] value: (optional) A list of values in a key-value
          pair.
    """

    def __init__(self, *, key=None, value=None):
        """
        Initialize a TableKeyValuePairs object.

        :param TableCellKey key: (optional) A key in a key-value pair.
        :param list[TableCellValues] value: (optional) A list of values in a
               key-value pair.
        """
        self.key = key
        self.value = value

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableKeyValuePairs object from a json dictionary."""
        args = {}
        valid_keys = ['key', 'value']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableKeyValuePairs: '
                + ', '.join(bad_keys))
        if 'key' in _dict:
            args['key'] = TableCellKey._from_dict(_dict.get('key'))
        if 'value' in _dict:
            args['value'] = [
                TableCellValues._from_dict(x) for x in (_dict.get('value'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key._to_dict()
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = [x._to_dict() for x in self.value]
        return _dict

    def __str__(self):
        """Return a `str` version of this TableKeyValuePairs object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
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
    :attr list[TableHeaders] table_headers: (optional) An array of table-level cells
          that apply as headers to all the other cells in the current table.
    :attr list[TableRowHeaders] row_headers: (optional) An array of row-level cells,
          each applicable as a header to other cells in the same row as itself, of the
          current table.
    :attr list[TableColumnHeaders] column_headers: (optional) An array of
          column-level cells, each applicable as a header to other cells in the same
          column as itself, of the current table.
    :attr list[TableKeyValuePairs] key_value_pairs: (optional) An array of key-value
          pairs identified in the current table.
    :attr list[TableBodyCells] body_cells: (optional) An array of cells that are
          neither table header nor column header nor row header cells, of the current
          table with corresponding row and column header associations.
    :attr list[TableTextLocation] contexts: (optional) An array of lists of textual
          entries across the document related to the current table being parsed.
    """

    def __init__(self,
                 *,
                 location=None,
                 text=None,
                 section_title=None,
                 title=None,
                 table_headers=None,
                 row_headers=None,
                 column_headers=None,
                 key_value_pairs=None,
                 body_cells=None,
                 contexts=None):
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
        :param list[TableHeaders] table_headers: (optional) An array of table-level
               cells that apply as headers to all the other cells in the current table.
        :param list[TableRowHeaders] row_headers: (optional) An array of row-level
               cells, each applicable as a header to other cells in the same row as
               itself, of the current table.
        :param list[TableColumnHeaders] column_headers: (optional) An array of
               column-level cells, each applicable as a header to other cells in the same
               column as itself, of the current table.
        :param list[TableKeyValuePairs] key_value_pairs: (optional) An array of
               key-value pairs identified in the current table.
        :param list[TableBodyCells] body_cells: (optional) An array of cells that
               are neither table header nor column header nor row header cells, of the
               current table with corresponding row and column header associations.
        :param list[TableTextLocation] contexts: (optional) An array of lists of
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
    def _from_dict(cls, _dict):
        """Initialize a TableResultTable object from a json dictionary."""
        args = {}
        valid_keys = [
            'location', 'text', 'section_title', 'title', 'table_headers',
            'row_headers', 'column_headers', 'key_value_pairs', 'body_cells',
            'contexts'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableResultTable: '
                + ', '.join(bad_keys))
        if 'location' in _dict:
            args['location'] = TableElementLocation._from_dict(
                _dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'section_title' in _dict:
            args['section_title'] = TableTextLocation._from_dict(
                _dict.get('section_title'))
        if 'title' in _dict:
            args['title'] = TableTextLocation._from_dict(_dict.get('title'))
        if 'table_headers' in _dict:
            args['table_headers'] = [
                TableHeaders._from_dict(x) for x in (_dict.get('table_headers'))
            ]
        if 'row_headers' in _dict:
            args['row_headers'] = [
                TableRowHeaders._from_dict(x)
                for x in (_dict.get('row_headers'))
            ]
        if 'column_headers' in _dict:
            args['column_headers'] = [
                TableColumnHeaders._from_dict(x)
                for x in (_dict.get('column_headers'))
            ]
        if 'key_value_pairs' in _dict:
            args['key_value_pairs'] = [
                TableKeyValuePairs._from_dict(x)
                for x in (_dict.get('key_value_pairs'))
            ]
        if 'body_cells' in _dict:
            args['body_cells'] = [
                TableBodyCells._from_dict(x) for x in (_dict.get('body_cells'))
            ]
        if 'contexts' in _dict:
            args['contexts'] = [
                TableTextLocation._from_dict(x) for x in (_dict.get('contexts'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'section_title') and self.section_title is not None:
            _dict['section_title'] = self.section_title._to_dict()
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title._to_dict()
        if hasattr(self, 'table_headers') and self.table_headers is not None:
            _dict['table_headers'] = [x._to_dict() for x in self.table_headers]
        if hasattr(self, 'row_headers') and self.row_headers is not None:
            _dict['row_headers'] = [x._to_dict() for x in self.row_headers]
        if hasattr(self, 'column_headers') and self.column_headers is not None:
            _dict['column_headers'] = [
                x._to_dict() for x in self.column_headers
            ]
        if hasattr(self,
                   'key_value_pairs') and self.key_value_pairs is not None:
            _dict['key_value_pairs'] = [
                x._to_dict() for x in self.key_value_pairs
            ]
        if hasattr(self, 'body_cells') and self.body_cells is not None:
            _dict['body_cells'] = [x._to_dict() for x in self.body_cells]
        if hasattr(self, 'contexts') and self.contexts is not None:
            _dict['contexts'] = [x._to_dict() for x in self.contexts]
        return _dict

    def __str__(self):
        """Return a `str` version of this TableResultTable object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableRowHeaderIds():
    """
    An array of values, each being the `id` value of a row header that is applicable to
    this body cell.

    :attr str id: (optional) The `id` values of a row header.
    """

    def __init__(self, *, id=None):
        """
        Initialize a TableRowHeaderIds object.

        :param str id: (optional) The `id` values of a row header.
        """
        self.id = id

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaderIds object from a json dictionary."""
        args = {}
        valid_keys = ['id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableRowHeaderIds: '
                + ', '.join(bad_keys))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def __str__(self):
        """Return a `str` version of this TableRowHeaderIds object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableRowHeaderTexts():
    """
    An array of values, each being the `text` value of a row header that is applicable to
    this body cell.

    :attr str text: (optional) The `text` value of a row header.
    """

    def __init__(self, *, text=None):
        """
        Initialize a TableRowHeaderTexts object.

        :param str text: (optional) The `text` value of a row header.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaderTexts object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableRowHeaderTexts: '
                + ', '.join(bad_keys))
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
        """Return a `str` version of this TableRowHeaderTexts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableRowHeaderTextsNormalized():
    """
    If you provide customization input, the normalized version of the row header texts
    according to the customization; otherwise, the same value as `row_header_texts`.

    :attr str text_normalized: (optional) The normalized version of a row header
          text.
    """

    def __init__(self, *, text_normalized=None):
        """
        Initialize a TableRowHeaderTextsNormalized object.

        :param str text_normalized: (optional) The normalized version of a row
               header text.
        """
        self.text_normalized = text_normalized

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaderTextsNormalized object from a json dictionary."""
        args = {}
        valid_keys = ['text_normalized']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableRowHeaderTextsNormalized: '
                + ', '.join(bad_keys))
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        return _dict

    def __str__(self):
        """Return a `str` version of this TableRowHeaderTextsNormalized object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
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
                 cell_id=None,
                 location=None,
                 text=None,
                 text_normalized=None,
                 row_index_begin=None,
                 row_index_end=None,
                 column_index_begin=None,
                 column_index_end=None):
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
    def _from_dict(cls, _dict):
        """Initialize a TableRowHeaders object from a json dictionary."""
        args = {}
        valid_keys = [
            'cell_id', 'location', 'text', 'text_normalized', 'row_index_begin',
            'row_index_end', 'column_index_begin', 'column_index_end'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableRowHeaders: '
                + ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = TableElementLocation._from_dict(
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
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

    def __str__(self):
        """Return a `str` version of this TableRowHeaders object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
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

    def __init__(self, *, text=None, location=None):
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
    def _from_dict(cls, _dict):
        """Initialize a TableTextLocation object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableTextLocation: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = TableElementLocation._from_dict(
                _dict.get('location'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this TableTextLocation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingExample():
    """
    Object containing example response details for a training query.

    :attr str document_id: The document ID associated with this training example.
    :attr str collection_id: The collection ID associated with this training
          example.
    :attr int relevance: The relevance of the training example.
    :attr date created: (optional) The date and time the example was created.
    :attr date updated: (optional) The date and time the example was updated.
    """

    def __init__(self,
                 document_id,
                 collection_id,
                 relevance,
                 *,
                 created=None,
                 updated=None):
        """
        Initialize a TrainingExample object.

        :param str document_id: The document ID associated with this training
               example.
        :param str collection_id: The collection ID associated with this training
               example.
        :param int relevance: The relevance of the training example.
        :param date created: (optional) The date and time the example was created.
        :param date updated: (optional) The date and time the example was updated.
        """
        self.document_id = document_id
        self.collection_id = collection_id
        self.relevance = relevance
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingExample object from a json dictionary."""
        args = {}
        valid_keys = [
            'document_id', 'collection_id', 'relevance', 'created', 'updated'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingExample: '
                + ', '.join(bad_keys))
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
            args['created'] = _dict.get('created')
        if 'updated' in _dict:
            args['updated'] = _dict.get('updated')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_id') and self.document_id is not None:
            _dict['document_id'] = self.document_id
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = self.updated
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


class TrainingQuery():
    """
    Object containing training query details.

    :attr str query_id: (optional) The query ID associated with the training query.
    :attr str natural_language_query: The natural text query for the training query.
    :attr str filter: (optional) The filter used on the collection before the
          **natural_language_query** is applied.
    :attr date created: (optional) The date and time the query was created.
    :attr date updated: (optional) The date and time the query was updated.
    :attr list[TrainingExample] examples: Array of training examples.
    """

    def __init__(self,
                 natural_language_query,
                 examples,
                 *,
                 query_id=None,
                 filter=None,
                 created=None,
                 updated=None):
        """
        Initialize a TrainingQuery object.

        :param str natural_language_query: The natural text query for the training
               query.
        :param list[TrainingExample] examples: Array of training examples.
        :param str query_id: (optional) The query ID associated with the training
               query.
        :param str filter: (optional) The filter used on the collection before the
               **natural_language_query** is applied.
        :param date created: (optional) The date and time the query was created.
        :param date updated: (optional) The date and time the query was updated.
        """
        self.query_id = query_id
        self.natural_language_query = natural_language_query
        self.filter = filter
        self.created = created
        self.updated = updated
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingQuery object from a json dictionary."""
        args = {}
        valid_keys = [
            'query_id', 'natural_language_query', 'filter', 'created',
            'updated', 'examples'
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
        else:
            raise ValueError(
                'Required property \'natural_language_query\' not present in TrainingQuery JSON'
            )
        if 'filter' in _dict:
            args['filter'] = _dict.get('filter')
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'updated' in _dict:
            args['updated'] = _dict.get('updated')
        if 'examples' in _dict:
            args['examples'] = [
                TrainingExample._from_dict(x) for x in (_dict.get('examples'))
            ]
        else:
            raise ValueError(
                'Required property \'examples\' not present in TrainingQuery JSON'
            )
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = self.updated
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


class TrainingQuerySet():
    """
    Object specifying the training queries contained in the identified training set.

    :attr list[TrainingQuery] queries: (optional) Array of training queries.
    """

    def __init__(self, *, queries=None):
        """
        Initialize a TrainingQuerySet object.

        :param list[TrainingQuery] queries: (optional) Array of training queries.
        """
        self.queries = queries

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingQuerySet object from a json dictionary."""
        args = {}
        valid_keys = ['queries']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingQuerySet: '
                + ', '.join(bad_keys))
        if 'queries' in _dict:
            args['queries'] = [
                TrainingQuery._from_dict(x) for x in (_dict.get('queries'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'queries') and self.queries is not None:
            _dict['queries'] = [x._to_dict() for x in self.queries]
        return _dict

    def __str__(self):
        """Return a `str` version of this TrainingQuerySet object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
