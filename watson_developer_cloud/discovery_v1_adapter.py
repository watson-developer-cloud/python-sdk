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

from .discovery_v1 import DiscoveryV1

class DiscoveryV1Adapter(DiscoveryV1):
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
                        passages=None,
                        passages_fields=None,
                        passages_count=None,
                        passages_characters=None,
                        bias=None,
                        logging_opt_out=None,
                        **kwargs):
        """
        Long environment queries.

        Complex queries might be too long for a standard method query. By using this
        method, you can construct longer queries. However, these queries may take longer
        to complete than the standard method. For details, see the [Discovery service
        documentation](https://console.bluemix.net/docs/services/discovery/using.html).

        :param str environment_id: The ID of the environment.
        :param list[str] collection_ids: A comma-separated list of collection IDs to be
        queried against.
        :param str filter: A cacheable query that limits the documents returned to exclude
        any documents that don't mention the query content. Filter searches are better for
        metadata type searches and when you are trying to get a sense of concepts in the
        data set.
        :param str query: A query search returns all documents in your data set with full
        enrichments and full text, but with the most relevant documents listed first. Use
        a query search when you want to find the most relevant search results. You cannot
        use **natural_language_query** and **query** at the same time.
        :param str natural_language_query: A natural language query that returns relevant
        documents by utilizing training data and natural language understanding. You
        cannot use **natural_language_query** and **query** at the same time.
        :param str aggregation: An aggregation search uses combinations of filters and
        query search to return an exact answer. Aggregations are useful for building
        applications, because you can use them to build lists, tables, and time series.
        For a full list of possible aggregrations, see the Query reference.
        :param int count: Number of results to return.
        :param list[str] return_fields: A comma separated list of the portion of the
        document hierarchy to return.
        :param int offset: The number of query results to skip at the beginning. For
        example, if the total number of results that are returned is 10, and the offset is
        8, it returns the last two results.
        :param list[str] sort: A comma separated list of fields in the document to sort
        on. You can optionally specify a sort direction by prefixing the field with `-`
        for descending or `+` for ascending. Ascending is the default sort direction if no
        prefix is specified.
        :param bool highlight: When true a highlight field is returned for each result
        which contains the fields that match the query with `<em></em>` tags around the
        matching query terms. Defaults to false.
        :param bool deduplicate: When `true` and used with a Watson Discovery News
        collection, duplicate results (based on the contents of the **title** field) are
        removed. Duplicate comparison is limited to the current query only; **offset** is
        not considered. This parameter is currently Beta functionality.
        :param str deduplicate_field: When specified, duplicate results based on the field
        specified are removed from the returned results. Duplicate comparison is limited
        to the current query only, **offset** is not considered. This parameter is
        currently Beta functionality.
        :param bool similar: When `true`, results are returned based on their similarity
        to the document IDs specified in the **similar.document_ids** parameter.
        :param list[str] similar_document_ids: A comma-separated list of document IDs that
        will be used to find similar documents.
        **Note:** If the **natural_language_query** parameter is also specified, it will
        be used to expand the scope of the document similarity search to include the
        natural language query. Other query parameters, such as **filter** and **query**
        are subsequently applied and reduce the query scope.
        :param list[str] similar_fields: A comma-separated list of field names that will
        be used as a basis for comparison to identify similar documents. If not specified,
        the entire document is used for comparison.
        :param bool passages: A passages query that returns the most relevant passages
        from the results.
        :param list[str] passages_fields: A comma-separated list of fields that passages
        are drawn from. If this parameter not specified, then all top-level fields are
        included.
        :param int passages_count: The maximum number of passages to return. The search
        returns fewer passages if the requested total is not found. The default is `10`.
        The maximum is `100`.
        :param int passages_characters: The approximate number of characters that any one
        passage will have. The default is `400`. The minimum is `50`. The maximum is
        `2000`.
        :param str bias: Field which the returned results will be biased against. The
        specified field must be either a **date** or **number** format. When a **date**
        type field is specified returned results are biased towards field values closer to
        the current date. When a **number** type field is specified, returned results are
        biased towards higher field values. This parameter cannot be used in the same
        query as the **sort** parameter.
        :param bool logging_opt_out: If `true`, queries are not stored in the Discovery
        **Logs** endpoint.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {'X-Watson-Logging-Opt-Out': logging_opt_out}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'collection_ids': self._convert_list(collection_ids),
            'filter': filter,
            'query': query,
            'natural_language_query': natural_language_query,
            'aggregation': aggregation,
            'count': count,
            'return': self._convert_list(return_fields),
            'offset': offset,
            'sort': self._convert_list(sort),
            'highlight': highlight,
            'deduplicate': deduplicate,
            'deduplicate.field': deduplicate_field,
            'similar': similar,
            'similar.document_ids': self._convert_list(similar_document_ids),
            'similar.fields': self._convert_list(similar_fields),
            'passages': passages,
            'passages.fields': self._convert_list(passages_fields),
            'passages.count': passages_count,
            'passages.characters': passages_characters,
            'bias': bias
        }
        url = '/v1/environments/{0}/query'.format(
            *self._encode_path_vars(environment_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
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
              logging_opt_out=None,
              collection_ids=None,
              bias=None,
              **kwargs):
        """
        Long collection queries.

        Complex queries might be too long for a standard method query. By using this
        method, you can construct longer queries. However, these queries may take longer
        to complete than the standard method. For details, see the [Discovery service
        documentation](https://console.bluemix.net/docs/services/discovery/using.html).

        :param str environment_id: The ID of the environment.
        :param str collection_id: The ID of the collection.
        :param str filter: A cacheable query that limits the documents returned to exclude
        any documents that don't mention the query content. Filter searches are better for
        metadata type searches and when you are trying to get a sense of concepts in the
        data set.
        :param str query: A query search returns all documents in your data set with full
        enrichments and full text, but with the most relevant documents listed first. Use
        a query search when you want to find the most relevant search results. You cannot
        use **natural_language_query** and **query** at the same time.
        :param str natural_language_query: A natural language query that returns relevant
        documents by utilizing training data and natural language understanding. You
        cannot use **natural_language_query** and **query** at the same time.
        :param bool passages: A passages query that returns the most relevant passages
        from the results.
        :param str aggregation: An aggregation search uses combinations of filters and
        query search to return an exact answer. Aggregations are useful for building
        applications, because you can use them to build lists, tables, and time series.
        For a full list of possible aggregrations, see the Query reference.
        :param int count: Number of results to return.
        :param list[str] return_fields: A comma separated list of the portion of the
        document hierarchy to return.
        :param int offset: The number of query results to skip at the beginning. For
        example, if the total number of results that are returned is 10, and the offset is
        8, it returns the last two results.
        :param list[str] sort: A comma separated list of fields in the document to sort
        on. You can optionally specify a sort direction by prefixing the field with `-`
        for descending or `+` for ascending. Ascending is the default sort direction if no
        prefix is specified.
        :param bool highlight: When true a highlight field is returned for each result
        which contains the fields that match the query with `<em></em>` tags around the
        matching query terms. Defaults to false.
        :param list[str] passages_fields: A comma-separated list of fields that passages
        are drawn from. If this parameter not specified, then all top-level fields are
        included.
        :param int passages_count: The maximum number of passages to return. The search
        returns fewer passages if the requested total is not found. The default is `10`.
        The maximum is `100`.
        :param int passages_characters: The approximate number of characters that any one
        passage will have. The default is `400`. The minimum is `50`. The maximum is
        `2000`.
        :param bool deduplicate: When `true` and used with a Watson Discovery News
        collection, duplicate results (based on the contents of the **title** field) are
        removed. Duplicate comparison is limited to the current query only; **offset** is
        not considered. This parameter is currently Beta functionality.
        :param str deduplicate_field: When specified, duplicate results based on the field
        specified are removed from the returned results. Duplicate comparison is limited
        to the current query only, **offset** is not considered. This parameter is
        currently Beta functionality.
        :param bool similar: When `true`, results are returned based on their similarity
        to the document IDs specified in the **similar.document_ids** parameter.
        :param list[str] similar_document_ids: A comma-separated list of document IDs that
        will be used to find similar documents.
        **Note:** If the **natural_language_query** parameter is also specified, it will
        be used to expand the scope of the document similarity search to include the
        natural language query. Other query parameters, such as **filter** and **query**
        are subsequently applied and reduce the query scope.
        :param list[str] similar_fields: A comma-separated list of field names that will
        be used as a basis for comparison to identify similar documents. If not specified,
        the entire document is used for comparison.
        :param bool logging_opt_out: If `true`, queries are not stored in the Discovery
        **Logs** endpoint.
        :param str collection_ids: A comma-separated list of collection IDs to be queried
        against. Required when querying multiple collections, invalid when performing a
        single collection query.
        :param str bias: Field which the returned results will be biased against. The
        specified field must be either a **date** or **number** format. When a **date**
        type field is specified returned results are biased towards field values closer to
        the current date. When a **number** type field is specified, returned results are
        biased towards higher field values. This parameter cannot be used in the same
        query as the **sort** parameter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        if collection_id is None:
            raise ValueError('collection_id must be provided')
        headers = {'X-Watson-Logging-Opt-Out': logging_opt_out}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
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
            'similar.fields': self._convert_list(similar_fields),
            'collection_ids': collection_ids,
            'bias': bias
        }
        url = '/v1/environments/{0}/collections/{1}/query'.format(
            *self._encode_path_vars(environment_id, collection_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response
