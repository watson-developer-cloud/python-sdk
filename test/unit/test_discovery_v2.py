# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Unit Tests for DiscoveryV2
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_watson.discovery_v2 import *

version = 'testString'

_service = DiscoveryV2(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.discovery.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Collections
##############################################################################
# region

class TestListCollections():
    """
    Test Class for list_collections
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_collections_all_params(self):
        """
        list_collections()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_collections(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_collections_value_error(self):
        """
        test_list_collections_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_collections(**req_copy)



class TestCreateCollection():
    """
    Test Class for create_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_collection_all_params(self):
        """
        create_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        name = 'testString'
        description = 'testString'
        language = 'en'
        enrichments = [collection_enrichment_model]

        # Invoke method
        response = _service.create_collection(
            project_id,
            name,
            description=description,
            language=language,
            enrichments=enrichments,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['language'] == 'en'
        assert req_body['enrichments'] == [collection_enrichment_model]


    @responses.activate
    def test_create_collection_value_error(self):
        """
        test_create_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        name = 'testString'
        description = 'testString'
        language = 'en'
        enrichments = [collection_enrichment_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_collection(**req_copy)



class TestGetCollection():
    """
    Test Class for get_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_collection_all_params(self):
        """
        get_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.get_collection(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_collection_value_error(self):
        """
        test_get_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_collection(**req_copy)



class TestUpdateCollection():
    """
    Test Class for update_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_collection_all_params(self):
        """
        update_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        name = 'testString'
        description = 'testString'
        enrichments = [collection_enrichment_model]

        # Invoke method
        response = _service.update_collection(
            project_id,
            collection_id,
            name=name,
            description=description,
            enrichments=enrichments,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['enrichments'] == [collection_enrichment_model]


    @responses.activate
    def test_update_collection_value_error(self):
        """
        test_update_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        name = 'testString'
        description = 'testString'
        enrichments = [collection_enrichment_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_collection(**req_copy)



class TestDeleteCollection():
    """
    Test Class for delete_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_collection_all_params(self):
        """
        delete_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_collection(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_collection_value_error(self):
        """
        test_delete_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_collection(**req_copy)



# endregion
##############################################################################
# End of Service: Collections
##############################################################################

##############################################################################
# Start of Service: Queries
##############################################################################
# region

class TestQuery():
    """
    Test Class for query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_query_all_params(self):
        """
        query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"document_id": "document_id", "metadata": {"mapKey": "anyValue"}, "result_metadata": {"document_retrieval_source": "search", "collection_id": "collection_id", "confidence": 10}, "document_passages": [{"passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field", "confidence": 0, "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}], "aggregations": [{"type": "filter", "match": "match", "matching_results": 16}], "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query", "suggested_refinements": [{"text": "text"}], "table_results": [{"table_id": "table_id", "source_document_id": "source_document_id", "collection_id": "collection_id", "table_html": "table_html", "table_html_offset": 17, "table": {"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"text": "text", "location": {"begin": 5, "end": 3}}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": [{"id": "id"}], "row_header_texts": [{"text": "text"}], "row_header_texts_normalized": [{"text_normalized": "text_normalized"}], "column_header_ids": [{"id": "id"}], "column_header_texts": [{"text": "text"}], "column_header_texts_normalized": [{"text_normalized": "text_normalized"}], "attributes": [{"type": "type", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}]}}], "passages": [{"passage_text": "passage_text", "passage_score": 13, "document_id": "document_id", "collection_id": "collection_id", "start_offset": 12, "end_offset": 10, "field": "field", "confidence": 0, "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a QueryLargeTableResults model
        query_large_table_results_model = {}
        query_large_table_results_model['enabled'] = True
        query_large_table_results_model['count'] = 38

        # Construct a dict representation of a QueryLargeSuggestedRefinements model
        query_large_suggested_refinements_model = {}
        query_large_suggested_refinements_model['enabled'] = True
        query_large_suggested_refinements_model['count'] = 1

        # Construct a dict representation of a QueryLargePassages model
        query_large_passages_model = {}
        query_large_passages_model['enabled'] = True
        query_large_passages_model['per_document'] = True
        query_large_passages_model['max_per_document'] = 38
        query_large_passages_model['fields'] = ['testString']
        query_large_passages_model['count'] = 400
        query_large_passages_model['characters'] = 50
        query_large_passages_model['find_answers'] = False
        query_large_passages_model['max_answers_per_passage'] = 38

        # Set up parameter values
        project_id = 'testString'
        collection_ids = ['testString']
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        aggregation = 'testString'
        count = 38
        return_ = ['testString']
        offset = 38
        sort = 'testString'
        highlight = True
        spelling_suggestions = True
        table_results = query_large_table_results_model
        suggested_refinements = query_large_suggested_refinements_model
        passages = query_large_passages_model

        # Invoke method
        response = _service.query(
            project_id,
            collection_ids=collection_ids,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            aggregation=aggregation,
            count=count,
            return_=return_,
            offset=offset,
            sort=sort,
            highlight=highlight,
            spelling_suggestions=spelling_suggestions,
            table_results=table_results,
            suggested_refinements=suggested_refinements,
            passages=passages,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['collection_ids'] == ['testString']
        assert req_body['filter'] == 'testString'
        assert req_body['query'] == 'testString'
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['aggregation'] == 'testString'
        assert req_body['count'] == 38
        assert req_body['return'] == ['testString']
        assert req_body['offset'] == 38
        assert req_body['sort'] == 'testString'
        assert req_body['highlight'] == True
        assert req_body['spelling_suggestions'] == True
        assert req_body['table_results'] == query_large_table_results_model
        assert req_body['suggested_refinements'] == query_large_suggested_refinements_model
        assert req_body['passages'] == query_large_passages_model


    @responses.activate
    def test_query_required_params(self):
        """
        test_query_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"document_id": "document_id", "metadata": {"mapKey": "anyValue"}, "result_metadata": {"document_retrieval_source": "search", "collection_id": "collection_id", "confidence": 10}, "document_passages": [{"passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field", "confidence": 0, "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}], "aggregations": [{"type": "filter", "match": "match", "matching_results": 16}], "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query", "suggested_refinements": [{"text": "text"}], "table_results": [{"table_id": "table_id", "source_document_id": "source_document_id", "collection_id": "collection_id", "table_html": "table_html", "table_html_offset": 17, "table": {"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"text": "text", "location": {"begin": 5, "end": 3}}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": [{"id": "id"}], "row_header_texts": [{"text": "text"}], "row_header_texts_normalized": [{"text_normalized": "text_normalized"}], "column_header_ids": [{"id": "id"}], "column_header_texts": [{"text": "text"}], "column_header_texts_normalized": [{"text_normalized": "text_normalized"}], "attributes": [{"type": "type", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}]}}], "passages": [{"passage_text": "passage_text", "passage_score": 13, "document_id": "document_id", "collection_id": "collection_id", "start_offset": 12, "end_offset": 10, "field": "field", "confidence": 0, "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.query(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_query_value_error(self):
        """
        test_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"document_id": "document_id", "metadata": {"mapKey": "anyValue"}, "result_metadata": {"document_retrieval_source": "search", "collection_id": "collection_id", "confidence": 10}, "document_passages": [{"passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field", "confidence": 0, "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}], "aggregations": [{"type": "filter", "match": "match", "matching_results": 16}], "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query", "suggested_refinements": [{"text": "text"}], "table_results": [{"table_id": "table_id", "source_document_id": "source_document_id", "collection_id": "collection_id", "table_html": "table_html", "table_html_offset": 17, "table": {"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"text": "text", "location": {"begin": 5, "end": 3}}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": [{"id": "id"}], "row_header_texts": [{"text": "text"}], "row_header_texts_normalized": [{"text_normalized": "text_normalized"}], "column_header_ids": [{"id": "id"}], "column_header_texts": [{"text": "text"}], "column_header_texts_normalized": [{"text_normalized": "text_normalized"}], "attributes": [{"type": "type", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}]}}], "passages": [{"passage_text": "passage_text", "passage_score": 13, "document_id": "document_id", "collection_id": "collection_id", "start_offset": 12, "end_offset": 10, "field": "field", "confidence": 0, "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query(**req_copy)



class TestGetAutocompletion():
    """
    Test Class for get_autocompletion
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_autocompletion_all_params(self):
        """
        get_autocompletion()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        prefix = 'testString'
        collection_ids = ['testString']
        field = 'testString'
        count = 38

        # Invoke method
        response = _service.get_autocompletion(
            project_id,
            prefix,
            collection_ids=collection_ids,
            field=field,
            count=count,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'prefix={}'.format(prefix) in query_string
        assert 'collection_ids={}'.format(','.join(collection_ids)) in query_string
        assert 'field={}'.format(field) in query_string
        assert 'count={}'.format(count) in query_string


    @responses.activate
    def test_get_autocompletion_required_params(self):
        """
        test_get_autocompletion_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        prefix = 'testString'

        # Invoke method
        response = _service.get_autocompletion(
            project_id,
            prefix,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'prefix={}'.format(prefix) in query_string


    @responses.activate
    def test_get_autocompletion_value_error(self):
        """
        test_get_autocompletion_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        prefix = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "prefix": prefix,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_autocompletion(**req_copy)



class TestQueryCollectionNotices():
    """
    Test Class for query_collection_notices
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_query_collection_notices_all_params(self):
        """
        query_collection_notices()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        count = 38
        offset = 38

        # Invoke method
        response = _service.query_collection_notices(
            project_id,
            collection_id,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            count=count,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string
        assert 'query={}'.format(query) in query_string
        assert 'natural_language_query={}'.format(natural_language_query) in query_string
        assert 'count={}'.format(count) in query_string
        assert 'offset={}'.format(offset) in query_string


    @responses.activate
    def test_query_collection_notices_required_params(self):
        """
        test_query_collection_notices_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.query_collection_notices(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_query_collection_notices_value_error(self):
        """
        test_query_collection_notices_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query_collection_notices(**req_copy)



class TestQueryNotices():
    """
    Test Class for query_notices
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_query_notices_all_params(self):
        """
        query_notices()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        count = 38
        offset = 38

        # Invoke method
        response = _service.query_notices(
            project_id,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            count=count,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string
        assert 'query={}'.format(query) in query_string
        assert 'natural_language_query={}'.format(natural_language_query) in query_string
        assert 'count={}'.format(count) in query_string
        assert 'offset={}'.format(offset) in query_string


    @responses.activate
    def test_query_notices_required_params(self):
        """
        test_query_notices_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.query_notices(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_query_notices_value_error(self):
        """
        test_query_notices_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query_notices(**req_copy)



class TestListFields():
    """
    Test Class for list_fields
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_fields_all_params(self):
        """
        list_fields()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested", "collection_id": "collection_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_ids = ['testString']

        # Invoke method
        response = _service.list_fields(
            project_id,
            collection_ids=collection_ids,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'collection_ids={}'.format(','.join(collection_ids)) in query_string


    @responses.activate
    def test_list_fields_required_params(self):
        """
        test_list_fields_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested", "collection_id": "collection_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_fields(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_fields_value_error(self):
        """
        test_list_fields_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested", "collection_id": "collection_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_fields(**req_copy)



# endregion
##############################################################################
# End of Service: Queries
##############################################################################

##############################################################################
# Start of Service: ComponentSettings
##############################################################################
# region

class TestGetComponentSettings():
    """
    Test Class for get_component_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_component_settings_all_params(self):
        """
        get_component_settings()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/component_settings')
        mock_response = '{"fields_shown": {"body": {"use_passage": false, "field": "field"}, "title": {"field": "field"}}, "autocomplete": true, "structured_search": false, "results_per_page": 16, "aggregations": [{"name": "name", "label": "label", "multiple_selections_allowed": false, "visualization_type": "auto"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.get_component_settings(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_component_settings_value_error(self):
        """
        test_get_component_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/component_settings')
        mock_response = '{"fields_shown": {"body": {"use_passage": false, "field": "field"}, "title": {"field": "field"}}, "autocomplete": true, "structured_search": false, "results_per_page": 16, "aggregations": [{"name": "name", "label": "label", "multiple_selections_allowed": false, "visualization_type": "auto"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_component_settings(**req_copy)



# endregion
##############################################################################
# End of Service: ComponentSettings
##############################################################################

##############################################################################
# Start of Service: Documents
##############################################################################
# region

class TestAddDocument():
    """
    Test Class for add_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_document_all_params(self):
        """
        add_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'
        x_watson_discovery_force = False

        # Invoke method
        response = _service.add_document(
            project_id,
            collection_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            x_watson_discovery_force=x_watson_discovery_force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_add_document_required_params(self):
        """
        test_add_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.add_document(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_add_document_value_error(self):
        """
        test_add_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_document(**req_copy)



class TestUpdateDocument():
    """
    Test Class for update_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_document_all_params(self):
        """
        update_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'
        x_watson_discovery_force = False

        # Invoke method
        response = _service.update_document(
            project_id,
            collection_id,
            document_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            x_watson_discovery_force=x_watson_discovery_force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_update_document_required_params(self):
        """
        test_update_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.update_document(
            project_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_update_document_value_error(self):
        """
        test_update_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_document(**req_copy)



class TestDeleteDocument():
    """
    Test Class for delete_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_document_all_params(self):
        """
        delete_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'
        x_watson_discovery_force = False

        # Invoke method
        response = _service.delete_document(
            project_id,
            collection_id,
            document_id,
            x_watson_discovery_force=x_watson_discovery_force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_document_required_params(self):
        """
        test_delete_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.delete_document(
            project_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_document_value_error(self):
        """
        test_delete_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_document(**req_copy)



# endregion
##############################################################################
# End of Service: Documents
##############################################################################

##############################################################################
# Start of Service: TrainingData
##############################################################################
# region

class TestListTrainingQueries():
    """
    Test Class for list_training_queries
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_training_queries_all_params(self):
        """
        list_training_queries()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries')
        mock_response = '{"queries": [{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_training_queries(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_training_queries_value_error(self):
        """
        test_list_training_queries_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries')
        mock_response = '{"queries": [{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_training_queries(**req_copy)



class TestDeleteTrainingQueries():
    """
    Test Class for delete_training_queries
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_training_queries_all_params(self):
        """
        delete_training_queries()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.delete_training_queries(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_training_queries_value_error(self):
        """
        test_delete_training_queries_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_training_queries(**req_copy)



class TestCreateTrainingQuery():
    """
    Test Class for create_training_query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_training_query_all_params(self):
        """
        create_training_query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Invoke method
        response = _service.create_training_query(
            project_id,
            natural_language_query,
            examples,
            filter=filter,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['examples'] == [training_example_model]
        assert req_body['filter'] == 'testString'


    @responses.activate
    def test_create_training_query_value_error(self):
        """
        test_create_training_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "natural_language_query": natural_language_query,
            "examples": examples,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_training_query(**req_copy)



class TestGetTrainingQuery():
    """
    Test Class for get_training_query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_training_query_all_params(self):
        """
        get_training_query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Invoke method
        response = _service.get_training_query(
            project_id,
            query_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_training_query_value_error(self):
        """
        test_get_training_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_training_query(**req_copy)



class TestUpdateTrainingQuery():
    """
    Test Class for update_training_query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_training_query_all_params(self):
        """
        update_training_query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Invoke method
        response = _service.update_training_query(
            project_id,
            query_id,
            natural_language_query,
            examples,
            filter=filter,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['examples'] == [training_example_model]
        assert req_body['filter'] == 'testString'


    @responses.activate
    def test_update_training_query_value_error(self):
        """
        test_update_training_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "query_id": query_id,
            "natural_language_query": natural_language_query,
            "examples": examples,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_training_query(**req_copy)



class TestDeleteTrainingQuery():
    """
    Test Class for delete_training_query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_training_query_all_params(self):
        """
        delete_training_query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Invoke method
        response = _service.delete_training_query(
            project_id,
            query_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_training_query_value_error(self):
        """
        test_delete_training_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/training_data/queries/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_training_query(**req_copy)



# endregion
##############################################################################
# End of Service: TrainingData
##############################################################################

##############################################################################
# Start of Service: Analyze
##############################################################################
# region

class TestAnalyzeDocument():
    """
    Test Class for analyze_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_analyze_document_all_params(self):
        """
        analyze_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/analyze')
        mock_response = '{"notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "result": {"metadata": {"mapKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'

        # Invoke method
        response = _service.analyze_document(
            project_id,
            collection_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_analyze_document_required_params(self):
        """
        test_analyze_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/analyze')
        mock_response = '{"notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "result": {"metadata": {"mapKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.analyze_document(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_analyze_document_value_error(self):
        """
        test_analyze_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/collections/testString/analyze')
        mock_response = '{"notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "result": {"metadata": {"mapKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.analyze_document(**req_copy)



# endregion
##############################################################################
# End of Service: Analyze
##############################################################################

##############################################################################
# Start of Service: Enrichments
##############################################################################
# region

class TestListEnrichments():
    """
    Test Class for list_enrichments
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_enrichments_all_params(self):
        """
        list_enrichments()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments')
        mock_response = '{"enrichments": [{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_enrichments(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_enrichments_value_error(self):
        """
        test_list_enrichments_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments')
        mock_response = '{"enrichments": [{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_enrichments(**req_copy)



class TestCreateEnrichment():
    """
    Test Class for create_enrichment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_enrichment_all_params(self):
        """
        create_enrichment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'

        # Construct a dict representation of a CreateEnrichment model
        create_enrichment_model = {}
        create_enrichment_model['name'] = 'testString'
        create_enrichment_model['description'] = 'testString'
        create_enrichment_model['type'] = 'dictionary'
        create_enrichment_model['options'] = enrichment_options_model

        # Set up parameter values
        project_id = 'testString'
        enrichment = create_enrichment_model
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_enrichment(
            project_id,
            enrichment,
            file=file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_enrichment_required_params(self):
        """
        test_create_enrichment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'

        # Construct a dict representation of a CreateEnrichment model
        create_enrichment_model = {}
        create_enrichment_model['name'] = 'testString'
        create_enrichment_model['description'] = 'testString'
        create_enrichment_model['type'] = 'dictionary'
        create_enrichment_model['options'] = enrichment_options_model

        # Set up parameter values
        project_id = 'testString'
        enrichment = create_enrichment_model

        # Invoke method
        response = _service.create_enrichment(
            project_id,
            enrichment,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_enrichment_value_error(self):
        """
        test_create_enrichment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'

        # Construct a dict representation of a CreateEnrichment model
        create_enrichment_model = {}
        create_enrichment_model['name'] = 'testString'
        create_enrichment_model['description'] = 'testString'
        create_enrichment_model['type'] = 'dictionary'
        create_enrichment_model['options'] = enrichment_options_model

        # Set up parameter values
        project_id = 'testString'
        enrichment = create_enrichment_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment": enrichment,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_enrichment(**req_copy)



class TestGetEnrichment():
    """
    Test Class for get_enrichment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_enrichment_all_params(self):
        """
        get_enrichment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Invoke method
        response = _service.get_enrichment(
            project_id,
            enrichment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_enrichment_value_error(self):
        """
        test_get_enrichment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment_id": enrichment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_enrichment(**req_copy)



class TestUpdateEnrichment():
    """
    Test Class for update_enrichment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_enrichment_all_params(self):
        """
        update_enrichment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.update_enrichment(
            project_id,
            enrichment_id,
            name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_update_enrichment_value_error(self):
        """
        test_update_enrichment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment_id": enrichment_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_enrichment(**req_copy)



class TestDeleteEnrichment():
    """
    Test Class for delete_enrichment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_enrichment_all_params(self):
        """
        delete_enrichment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Invoke method
        response = _service.delete_enrichment(
            project_id,
            enrichment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_enrichment_value_error(self):
        """
        test_delete_enrichment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString/enrichments/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment_id": enrichment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_enrichment(**req_copy)



# endregion
##############################################################################
# End of Service: Enrichments
##############################################################################

##############################################################################
# Start of Service: Projects
##############################################################################
# region

class TestListProjects():
    """
    Test Class for list_projects
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_projects_all_params(self):
        """
        list_projects()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects')
        mock_response = '{"projects": [{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_projects()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_projects_value_error(self):
        """
        test_list_projects_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects')
        mock_response = '{"projects": [{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_projects(**req_copy)



class TestCreateProject():
    """
    Test Class for create_project
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_project_all_params(self):
        """
        create_project()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a DefaultQueryParamsPassages model
        default_query_params_passages_model = {}
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsTableResults model
        default_query_params_table_results_model = {}
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsSuggestedRefinements model
        default_query_params_suggested_refinements_model = {}
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        # Construct a dict representation of a DefaultQueryParams model
        default_query_params_model = {}
        default_query_params_model['collection_ids'] = ['testString']
        default_query_params_model['passages'] = default_query_params_passages_model
        default_query_params_model['table_results'] = default_query_params_table_results_model
        default_query_params_model['aggregation'] = 'testString'
        default_query_params_model['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model['spelling_suggestions'] = True
        default_query_params_model['highlight'] = True
        default_query_params_model['count'] = 38
        default_query_params_model['sort'] = 'testString'
        default_query_params_model['return'] = ['testString']

        # Set up parameter values
        name = 'testString'
        type = 'document_retrieval'
        default_query_parameters = default_query_params_model

        # Invoke method
        response = _service.create_project(
            name,
            type,
            default_query_parameters=default_query_parameters,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'document_retrieval'
        assert req_body['default_query_parameters'] == default_query_params_model


    @responses.activate
    def test_create_project_value_error(self):
        """
        test_create_project_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a DefaultQueryParamsPassages model
        default_query_params_passages_model = {}
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsTableResults model
        default_query_params_table_results_model = {}
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsSuggestedRefinements model
        default_query_params_suggested_refinements_model = {}
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        # Construct a dict representation of a DefaultQueryParams model
        default_query_params_model = {}
        default_query_params_model['collection_ids'] = ['testString']
        default_query_params_model['passages'] = default_query_params_passages_model
        default_query_params_model['table_results'] = default_query_params_table_results_model
        default_query_params_model['aggregation'] = 'testString'
        default_query_params_model['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model['spelling_suggestions'] = True
        default_query_params_model['highlight'] = True
        default_query_params_model['count'] = 38
        default_query_params_model['sort'] = 'testString'
        default_query_params_model['return'] = ['testString']

        # Set up parameter values
        name = 'testString'
        type = 'document_retrieval'
        default_query_parameters = default_query_params_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_project(**req_copy)



class TestGetProject():
    """
    Test Class for get_project
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_project_all_params(self):
        """
        get_project()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.get_project(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_project_value_error(self):
        """
        test_get_project_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_project(**req_copy)



class TestUpdateProject():
    """
    Test Class for update_project
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_project_all_params(self):
        """
        update_project()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        name = 'testString'

        # Invoke method
        response = _service.update_project(
            project_id,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'


    @responses.activate
    def test_update_project_required_params(self):
        """
        test_update_project_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.update_project(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_project_value_error(self):
        """
        test_update_project_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_project(**req_copy)



class TestDeleteProject():
    """
    Test Class for delete_project
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_project_all_params(self):
        """
        delete_project()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.delete_project(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_project_value_error(self):
        """
        test_delete_project_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/projects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_project(**req_copy)



# endregion
##############################################################################
# End of Service: Projects
##############################################################################

##############################################################################
# Start of Service: UserData
##############################################################################
# region

class TestDeleteUserData():
    """
    Test Class for delete_user_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_user_data_all_params(self):
        """
        delete_user_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customer_id = 'testString'

        # Invoke method
        response = _service.delete_user_data(
            customer_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'customer_id={}'.format(customer_id) in query_string


    @responses.activate
    def test_delete_user_data_value_error(self):
        """
        test_delete_user_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customer_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customer_id": customer_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_user_data(**req_copy)



# endregion
##############################################################################
# End of Service: UserData
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AnalyzedDocument():
    """
    Test Class for AnalyzedDocument
    """

    def test_analyzed_document_serialization(self):
        """
        Test serialization/deserialization for AnalyzedDocument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice
        notice_model['notice_id'] = 'testString'
        notice_model['created'] = "2019-01-01T12:00:00Z"
        notice_model['document_id'] = 'testString'
        notice_model['collection_id'] = 'testString'
        notice_model['query_id'] = 'testString'
        notice_model['severity'] = 'warning'
        notice_model['step'] = 'testString'
        notice_model['description'] = 'testString'

        analyzed_result_model = {} # AnalyzedResult
        analyzed_result_model['metadata'] = {}
        analyzed_result_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a AnalyzedDocument model
        analyzed_document_model_json = {}
        analyzed_document_model_json['notices'] = [notice_model]
        analyzed_document_model_json['result'] = analyzed_result_model

        # Construct a model instance of AnalyzedDocument by calling from_dict on the json representation
        analyzed_document_model = AnalyzedDocument.from_dict(analyzed_document_model_json)
        assert analyzed_document_model != False

        # Construct a model instance of AnalyzedDocument by calling from_dict on the json representation
        analyzed_document_model_dict = AnalyzedDocument.from_dict(analyzed_document_model_json).__dict__
        analyzed_document_model2 = AnalyzedDocument(**analyzed_document_model_dict)

        # Verify the model instances are equivalent
        assert analyzed_document_model == analyzed_document_model2

        # Convert model instance back to dict and verify no loss of data
        analyzed_document_model_json2 = analyzed_document_model.to_dict()
        assert analyzed_document_model_json2 == analyzed_document_model_json

class TestModel_AnalyzedResult():
    """
    Test Class for AnalyzedResult
    """

    def test_analyzed_result_serialization(self):
        """
        Test serialization/deserialization for AnalyzedResult
        """

        # Construct a json representation of a AnalyzedResult model
        analyzed_result_model_json = {}
        analyzed_result_model_json['metadata'] = {}
        analyzed_result_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of AnalyzedResult by calling from_dict on the json representation
        analyzed_result_model = AnalyzedResult.from_dict(analyzed_result_model_json)
        assert analyzed_result_model != False

        # Construct a model instance of AnalyzedResult by calling from_dict on the json representation
        analyzed_result_model_dict = AnalyzedResult.from_dict(analyzed_result_model_json).__dict__
        analyzed_result_model2 = AnalyzedResult(**analyzed_result_model_dict)

        # Verify the model instances are equivalent
        assert analyzed_result_model == analyzed_result_model2

        # Convert model instance back to dict and verify no loss of data
        analyzed_result_model_json2 = analyzed_result_model.to_dict()
        assert analyzed_result_model_json2 == analyzed_result_model_json

        # Test get_properties and set_properties methods.
        analyzed_result_model.set_properties({})
        actual_dict = analyzed_result_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': { 'foo': 'bar' }}
        analyzed_result_model.set_properties(expected_dict)
        actual_dict = analyzed_result_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_Collection():
    """
    Test Class for Collection
    """

    def test_collection_serialization(self):
        """
        Test serialization/deserialization for Collection
        """

        # Construct a json representation of a Collection model
        collection_model_json = {}
        collection_model_json['collection_id'] = 'testString'
        collection_model_json['name'] = 'testString'

        # Construct a model instance of Collection by calling from_dict on the json representation
        collection_model = Collection.from_dict(collection_model_json)
        assert collection_model != False

        # Construct a model instance of Collection by calling from_dict on the json representation
        collection_model_dict = Collection.from_dict(collection_model_json).__dict__
        collection_model2 = Collection(**collection_model_dict)

        # Verify the model instances are equivalent
        assert collection_model == collection_model2

        # Convert model instance back to dict and verify no loss of data
        collection_model_json2 = collection_model.to_dict()
        assert collection_model_json2 == collection_model_json

class TestModel_CollectionDetails():
    """
    Test Class for CollectionDetails
    """

    def test_collection_details_serialization(self):
        """
        Test serialization/deserialization for CollectionDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        collection_enrichment_model = {} # CollectionEnrichment
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Construct a json representation of a CollectionDetails model
        collection_details_model_json = {}
        collection_details_model_json['collection_id'] = 'testString'
        collection_details_model_json['name'] = 'testString'
        collection_details_model_json['description'] = 'testString'
        collection_details_model_json['created'] = "2019-01-01T12:00:00Z"
        collection_details_model_json['language'] = 'en'
        collection_details_model_json['enrichments'] = [collection_enrichment_model]

        # Construct a model instance of CollectionDetails by calling from_dict on the json representation
        collection_details_model = CollectionDetails.from_dict(collection_details_model_json)
        assert collection_details_model != False

        # Construct a model instance of CollectionDetails by calling from_dict on the json representation
        collection_details_model_dict = CollectionDetails.from_dict(collection_details_model_json).__dict__
        collection_details_model2 = CollectionDetails(**collection_details_model_dict)

        # Verify the model instances are equivalent
        assert collection_details_model == collection_details_model2

        # Convert model instance back to dict and verify no loss of data
        collection_details_model_json2 = collection_details_model.to_dict()
        assert collection_details_model_json2 == collection_details_model_json

class TestModel_CollectionEnrichment():
    """
    Test Class for CollectionEnrichment
    """

    def test_collection_enrichment_serialization(self):
        """
        Test serialization/deserialization for CollectionEnrichment
        """

        # Construct a json representation of a CollectionEnrichment model
        collection_enrichment_model_json = {}
        collection_enrichment_model_json['enrichment_id'] = 'testString'
        collection_enrichment_model_json['fields'] = ['testString']

        # Construct a model instance of CollectionEnrichment by calling from_dict on the json representation
        collection_enrichment_model = CollectionEnrichment.from_dict(collection_enrichment_model_json)
        assert collection_enrichment_model != False

        # Construct a model instance of CollectionEnrichment by calling from_dict on the json representation
        collection_enrichment_model_dict = CollectionEnrichment.from_dict(collection_enrichment_model_json).__dict__
        collection_enrichment_model2 = CollectionEnrichment(**collection_enrichment_model_dict)

        # Verify the model instances are equivalent
        assert collection_enrichment_model == collection_enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        collection_enrichment_model_json2 = collection_enrichment_model.to_dict()
        assert collection_enrichment_model_json2 == collection_enrichment_model_json

class TestModel_Completions():
    """
    Test Class for Completions
    """

    def test_completions_serialization(self):
        """
        Test serialization/deserialization for Completions
        """

        # Construct a json representation of a Completions model
        completions_model_json = {}
        completions_model_json['completions'] = ['testString']

        # Construct a model instance of Completions by calling from_dict on the json representation
        completions_model = Completions.from_dict(completions_model_json)
        assert completions_model != False

        # Construct a model instance of Completions by calling from_dict on the json representation
        completions_model_dict = Completions.from_dict(completions_model_json).__dict__
        completions_model2 = Completions(**completions_model_dict)

        # Verify the model instances are equivalent
        assert completions_model == completions_model2

        # Convert model instance back to dict and verify no loss of data
        completions_model_json2 = completions_model.to_dict()
        assert completions_model_json2 == completions_model_json

class TestModel_ComponentSettingsAggregation():
    """
    Test Class for ComponentSettingsAggregation
    """

    def test_component_settings_aggregation_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsAggregation
        """

        # Construct a json representation of a ComponentSettingsAggregation model
        component_settings_aggregation_model_json = {}
        component_settings_aggregation_model_json['name'] = 'testString'
        component_settings_aggregation_model_json['label'] = 'testString'
        component_settings_aggregation_model_json['multiple_selections_allowed'] = True
        component_settings_aggregation_model_json['visualization_type'] = 'auto'

        # Construct a model instance of ComponentSettingsAggregation by calling from_dict on the json representation
        component_settings_aggregation_model = ComponentSettingsAggregation.from_dict(component_settings_aggregation_model_json)
        assert component_settings_aggregation_model != False

        # Construct a model instance of ComponentSettingsAggregation by calling from_dict on the json representation
        component_settings_aggregation_model_dict = ComponentSettingsAggregation.from_dict(component_settings_aggregation_model_json).__dict__
        component_settings_aggregation_model2 = ComponentSettingsAggregation(**component_settings_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_aggregation_model == component_settings_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_aggregation_model_json2 = component_settings_aggregation_model.to_dict()
        assert component_settings_aggregation_model_json2 == component_settings_aggregation_model_json

class TestModel_ComponentSettingsFieldsShown():
    """
    Test Class for ComponentSettingsFieldsShown
    """

    def test_component_settings_fields_shown_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsFieldsShown
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_settings_fields_shown_body_model = {} # ComponentSettingsFieldsShownBody
        component_settings_fields_shown_body_model['use_passage'] = True
        component_settings_fields_shown_body_model['field'] = 'testString'

        component_settings_fields_shown_title_model = {} # ComponentSettingsFieldsShownTitle
        component_settings_fields_shown_title_model['field'] = 'testString'

        # Construct a json representation of a ComponentSettingsFieldsShown model
        component_settings_fields_shown_model_json = {}
        component_settings_fields_shown_model_json['body'] = component_settings_fields_shown_body_model
        component_settings_fields_shown_model_json['title'] = component_settings_fields_shown_title_model

        # Construct a model instance of ComponentSettingsFieldsShown by calling from_dict on the json representation
        component_settings_fields_shown_model = ComponentSettingsFieldsShown.from_dict(component_settings_fields_shown_model_json)
        assert component_settings_fields_shown_model != False

        # Construct a model instance of ComponentSettingsFieldsShown by calling from_dict on the json representation
        component_settings_fields_shown_model_dict = ComponentSettingsFieldsShown.from_dict(component_settings_fields_shown_model_json).__dict__
        component_settings_fields_shown_model2 = ComponentSettingsFieldsShown(**component_settings_fields_shown_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_fields_shown_model == component_settings_fields_shown_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_fields_shown_model_json2 = component_settings_fields_shown_model.to_dict()
        assert component_settings_fields_shown_model_json2 == component_settings_fields_shown_model_json

class TestModel_ComponentSettingsFieldsShownBody():
    """
    Test Class for ComponentSettingsFieldsShownBody
    """

    def test_component_settings_fields_shown_body_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsFieldsShownBody
        """

        # Construct a json representation of a ComponentSettingsFieldsShownBody model
        component_settings_fields_shown_body_model_json = {}
        component_settings_fields_shown_body_model_json['use_passage'] = True
        component_settings_fields_shown_body_model_json['field'] = 'testString'

        # Construct a model instance of ComponentSettingsFieldsShownBody by calling from_dict on the json representation
        component_settings_fields_shown_body_model = ComponentSettingsFieldsShownBody.from_dict(component_settings_fields_shown_body_model_json)
        assert component_settings_fields_shown_body_model != False

        # Construct a model instance of ComponentSettingsFieldsShownBody by calling from_dict on the json representation
        component_settings_fields_shown_body_model_dict = ComponentSettingsFieldsShownBody.from_dict(component_settings_fields_shown_body_model_json).__dict__
        component_settings_fields_shown_body_model2 = ComponentSettingsFieldsShownBody(**component_settings_fields_shown_body_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_fields_shown_body_model == component_settings_fields_shown_body_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_fields_shown_body_model_json2 = component_settings_fields_shown_body_model.to_dict()
        assert component_settings_fields_shown_body_model_json2 == component_settings_fields_shown_body_model_json

class TestModel_ComponentSettingsFieldsShownTitle():
    """
    Test Class for ComponentSettingsFieldsShownTitle
    """

    def test_component_settings_fields_shown_title_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsFieldsShownTitle
        """

        # Construct a json representation of a ComponentSettingsFieldsShownTitle model
        component_settings_fields_shown_title_model_json = {}
        component_settings_fields_shown_title_model_json['field'] = 'testString'

        # Construct a model instance of ComponentSettingsFieldsShownTitle by calling from_dict on the json representation
        component_settings_fields_shown_title_model = ComponentSettingsFieldsShownTitle.from_dict(component_settings_fields_shown_title_model_json)
        assert component_settings_fields_shown_title_model != False

        # Construct a model instance of ComponentSettingsFieldsShownTitle by calling from_dict on the json representation
        component_settings_fields_shown_title_model_dict = ComponentSettingsFieldsShownTitle.from_dict(component_settings_fields_shown_title_model_json).__dict__
        component_settings_fields_shown_title_model2 = ComponentSettingsFieldsShownTitle(**component_settings_fields_shown_title_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_fields_shown_title_model == component_settings_fields_shown_title_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_fields_shown_title_model_json2 = component_settings_fields_shown_title_model.to_dict()
        assert component_settings_fields_shown_title_model_json2 == component_settings_fields_shown_title_model_json

class TestModel_ComponentSettingsResponse():
    """
    Test Class for ComponentSettingsResponse
    """

    def test_component_settings_response_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_settings_fields_shown_body_model = {} # ComponentSettingsFieldsShownBody
        component_settings_fields_shown_body_model['use_passage'] = True
        component_settings_fields_shown_body_model['field'] = 'testString'

        component_settings_fields_shown_title_model = {} # ComponentSettingsFieldsShownTitle
        component_settings_fields_shown_title_model['field'] = 'testString'

        component_settings_fields_shown_model = {} # ComponentSettingsFieldsShown
        component_settings_fields_shown_model['body'] = component_settings_fields_shown_body_model
        component_settings_fields_shown_model['title'] = component_settings_fields_shown_title_model

        component_settings_aggregation_model = {} # ComponentSettingsAggregation
        component_settings_aggregation_model['name'] = 'testString'
        component_settings_aggregation_model['label'] = 'testString'
        component_settings_aggregation_model['multiple_selections_allowed'] = True
        component_settings_aggregation_model['visualization_type'] = 'auto'

        # Construct a json representation of a ComponentSettingsResponse model
        component_settings_response_model_json = {}
        component_settings_response_model_json['fields_shown'] = component_settings_fields_shown_model
        component_settings_response_model_json['autocomplete'] = True
        component_settings_response_model_json['structured_search'] = True
        component_settings_response_model_json['results_per_page'] = 38
        component_settings_response_model_json['aggregations'] = [component_settings_aggregation_model]

        # Construct a model instance of ComponentSettingsResponse by calling from_dict on the json representation
        component_settings_response_model = ComponentSettingsResponse.from_dict(component_settings_response_model_json)
        assert component_settings_response_model != False

        # Construct a model instance of ComponentSettingsResponse by calling from_dict on the json representation
        component_settings_response_model_dict = ComponentSettingsResponse.from_dict(component_settings_response_model_json).__dict__
        component_settings_response_model2 = ComponentSettingsResponse(**component_settings_response_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_response_model == component_settings_response_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_response_model_json2 = component_settings_response_model.to_dict()
        assert component_settings_response_model_json2 == component_settings_response_model_json

class TestModel_CreateEnrichment():
    """
    Test Class for CreateEnrichment
    """

    def test_create_enrichment_serialization(self):
        """
        Test serialization/deserialization for CreateEnrichment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'

        # Construct a json representation of a CreateEnrichment model
        create_enrichment_model_json = {}
        create_enrichment_model_json['name'] = 'testString'
        create_enrichment_model_json['description'] = 'testString'
        create_enrichment_model_json['type'] = 'dictionary'
        create_enrichment_model_json['options'] = enrichment_options_model

        # Construct a model instance of CreateEnrichment by calling from_dict on the json representation
        create_enrichment_model = CreateEnrichment.from_dict(create_enrichment_model_json)
        assert create_enrichment_model != False

        # Construct a model instance of CreateEnrichment by calling from_dict on the json representation
        create_enrichment_model_dict = CreateEnrichment.from_dict(create_enrichment_model_json).__dict__
        create_enrichment_model2 = CreateEnrichment(**create_enrichment_model_dict)

        # Verify the model instances are equivalent
        assert create_enrichment_model == create_enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        create_enrichment_model_json2 = create_enrichment_model.to_dict()
        assert create_enrichment_model_json2 == create_enrichment_model_json

class TestModel_DefaultQueryParams():
    """
    Test Class for DefaultQueryParams
    """

    def test_default_query_params_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParams
        """

        # Construct dict forms of any model objects needed in order to build this model.

        default_query_params_passages_model = {} # DefaultQueryParamsPassages
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        default_query_params_table_results_model = {} # DefaultQueryParamsTableResults
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        default_query_params_suggested_refinements_model = {} # DefaultQueryParamsSuggestedRefinements
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        # Construct a json representation of a DefaultQueryParams model
        default_query_params_model_json = {}
        default_query_params_model_json['collection_ids'] = ['testString']
        default_query_params_model_json['passages'] = default_query_params_passages_model
        default_query_params_model_json['table_results'] = default_query_params_table_results_model
        default_query_params_model_json['aggregation'] = 'testString'
        default_query_params_model_json['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model_json['spelling_suggestions'] = True
        default_query_params_model_json['highlight'] = True
        default_query_params_model_json['count'] = 38
        default_query_params_model_json['sort'] = 'testString'
        default_query_params_model_json['return'] = ['testString']

        # Construct a model instance of DefaultQueryParams by calling from_dict on the json representation
        default_query_params_model = DefaultQueryParams.from_dict(default_query_params_model_json)
        assert default_query_params_model != False

        # Construct a model instance of DefaultQueryParams by calling from_dict on the json representation
        default_query_params_model_dict = DefaultQueryParams.from_dict(default_query_params_model_json).__dict__
        default_query_params_model2 = DefaultQueryParams(**default_query_params_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_model == default_query_params_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_model_json2 = default_query_params_model.to_dict()
        assert default_query_params_model_json2 == default_query_params_model_json

class TestModel_DefaultQueryParamsPassages():
    """
    Test Class for DefaultQueryParamsPassages
    """

    def test_default_query_params_passages_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParamsPassages
        """

        # Construct a json representation of a DefaultQueryParamsPassages model
        default_query_params_passages_model_json = {}
        default_query_params_passages_model_json['enabled'] = True
        default_query_params_passages_model_json['count'] = 38
        default_query_params_passages_model_json['fields'] = ['testString']
        default_query_params_passages_model_json['characters'] = 38
        default_query_params_passages_model_json['per_document'] = True
        default_query_params_passages_model_json['max_per_document'] = 38

        # Construct a model instance of DefaultQueryParamsPassages by calling from_dict on the json representation
        default_query_params_passages_model = DefaultQueryParamsPassages.from_dict(default_query_params_passages_model_json)
        assert default_query_params_passages_model != False

        # Construct a model instance of DefaultQueryParamsPassages by calling from_dict on the json representation
        default_query_params_passages_model_dict = DefaultQueryParamsPassages.from_dict(default_query_params_passages_model_json).__dict__
        default_query_params_passages_model2 = DefaultQueryParamsPassages(**default_query_params_passages_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_passages_model == default_query_params_passages_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_passages_model_json2 = default_query_params_passages_model.to_dict()
        assert default_query_params_passages_model_json2 == default_query_params_passages_model_json

class TestModel_DefaultQueryParamsSuggestedRefinements():
    """
    Test Class for DefaultQueryParamsSuggestedRefinements
    """

    def test_default_query_params_suggested_refinements_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParamsSuggestedRefinements
        """

        # Construct a json representation of a DefaultQueryParamsSuggestedRefinements model
        default_query_params_suggested_refinements_model_json = {}
        default_query_params_suggested_refinements_model_json['enabled'] = True
        default_query_params_suggested_refinements_model_json['count'] = 38

        # Construct a model instance of DefaultQueryParamsSuggestedRefinements by calling from_dict on the json representation
        default_query_params_suggested_refinements_model = DefaultQueryParamsSuggestedRefinements.from_dict(default_query_params_suggested_refinements_model_json)
        assert default_query_params_suggested_refinements_model != False

        # Construct a model instance of DefaultQueryParamsSuggestedRefinements by calling from_dict on the json representation
        default_query_params_suggested_refinements_model_dict = DefaultQueryParamsSuggestedRefinements.from_dict(default_query_params_suggested_refinements_model_json).__dict__
        default_query_params_suggested_refinements_model2 = DefaultQueryParamsSuggestedRefinements(**default_query_params_suggested_refinements_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_suggested_refinements_model == default_query_params_suggested_refinements_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_suggested_refinements_model_json2 = default_query_params_suggested_refinements_model.to_dict()
        assert default_query_params_suggested_refinements_model_json2 == default_query_params_suggested_refinements_model_json

class TestModel_DefaultQueryParamsTableResults():
    """
    Test Class for DefaultQueryParamsTableResults
    """

    def test_default_query_params_table_results_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParamsTableResults
        """

        # Construct a json representation of a DefaultQueryParamsTableResults model
        default_query_params_table_results_model_json = {}
        default_query_params_table_results_model_json['enabled'] = True
        default_query_params_table_results_model_json['count'] = 38
        default_query_params_table_results_model_json['per_document'] = 38

        # Construct a model instance of DefaultQueryParamsTableResults by calling from_dict on the json representation
        default_query_params_table_results_model = DefaultQueryParamsTableResults.from_dict(default_query_params_table_results_model_json)
        assert default_query_params_table_results_model != False

        # Construct a model instance of DefaultQueryParamsTableResults by calling from_dict on the json representation
        default_query_params_table_results_model_dict = DefaultQueryParamsTableResults.from_dict(default_query_params_table_results_model_json).__dict__
        default_query_params_table_results_model2 = DefaultQueryParamsTableResults(**default_query_params_table_results_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_table_results_model == default_query_params_table_results_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_table_results_model_json2 = default_query_params_table_results_model.to_dict()
        assert default_query_params_table_results_model_json2 == default_query_params_table_results_model_json

class TestModel_DeleteDocumentResponse():
    """
    Test Class for DeleteDocumentResponse
    """

    def test_delete_document_response_serialization(self):
        """
        Test serialization/deserialization for DeleteDocumentResponse
        """

        # Construct a json representation of a DeleteDocumentResponse model
        delete_document_response_model_json = {}
        delete_document_response_model_json['document_id'] = 'testString'
        delete_document_response_model_json['status'] = 'deleted'

        # Construct a model instance of DeleteDocumentResponse by calling from_dict on the json representation
        delete_document_response_model = DeleteDocumentResponse.from_dict(delete_document_response_model_json)
        assert delete_document_response_model != False

        # Construct a model instance of DeleteDocumentResponse by calling from_dict on the json representation
        delete_document_response_model_dict = DeleteDocumentResponse.from_dict(delete_document_response_model_json).__dict__
        delete_document_response_model2 = DeleteDocumentResponse(**delete_document_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_document_response_model == delete_document_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_document_response_model_json2 = delete_document_response_model.to_dict()
        assert delete_document_response_model_json2 == delete_document_response_model_json

class TestModel_DocumentAccepted():
    """
    Test Class for DocumentAccepted
    """

    def test_document_accepted_serialization(self):
        """
        Test serialization/deserialization for DocumentAccepted
        """

        # Construct a json representation of a DocumentAccepted model
        document_accepted_model_json = {}
        document_accepted_model_json['document_id'] = 'testString'
        document_accepted_model_json['status'] = 'processing'

        # Construct a model instance of DocumentAccepted by calling from_dict on the json representation
        document_accepted_model = DocumentAccepted.from_dict(document_accepted_model_json)
        assert document_accepted_model != False

        # Construct a model instance of DocumentAccepted by calling from_dict on the json representation
        document_accepted_model_dict = DocumentAccepted.from_dict(document_accepted_model_json).__dict__
        document_accepted_model2 = DocumentAccepted(**document_accepted_model_dict)

        # Verify the model instances are equivalent
        assert document_accepted_model == document_accepted_model2

        # Convert model instance back to dict and verify no loss of data
        document_accepted_model_json2 = document_accepted_model.to_dict()
        assert document_accepted_model_json2 == document_accepted_model_json

class TestModel_DocumentAttribute():
    """
    Test Class for DocumentAttribute
    """

    def test_document_attribute_serialization(self):
        """
        Test serialization/deserialization for DocumentAttribute
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a DocumentAttribute model
        document_attribute_model_json = {}
        document_attribute_model_json['type'] = 'testString'
        document_attribute_model_json['text'] = 'testString'
        document_attribute_model_json['location'] = table_element_location_model

        # Construct a model instance of DocumentAttribute by calling from_dict on the json representation
        document_attribute_model = DocumentAttribute.from_dict(document_attribute_model_json)
        assert document_attribute_model != False

        # Construct a model instance of DocumentAttribute by calling from_dict on the json representation
        document_attribute_model_dict = DocumentAttribute.from_dict(document_attribute_model_json).__dict__
        document_attribute_model2 = DocumentAttribute(**document_attribute_model_dict)

        # Verify the model instances are equivalent
        assert document_attribute_model == document_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        document_attribute_model_json2 = document_attribute_model.to_dict()
        assert document_attribute_model_json2 == document_attribute_model_json

class TestModel_Enrichment():
    """
    Test Class for Enrichment
    """

    def test_enrichment_serialization(self):
        """
        Test serialization/deserialization for Enrichment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'

        # Construct a json representation of a Enrichment model
        enrichment_model_json = {}
        enrichment_model_json['enrichment_id'] = 'testString'
        enrichment_model_json['name'] = 'testString'
        enrichment_model_json['description'] = 'testString'
        enrichment_model_json['type'] = 'part_of_speech'
        enrichment_model_json['options'] = enrichment_options_model

        # Construct a model instance of Enrichment by calling from_dict on the json representation
        enrichment_model = Enrichment.from_dict(enrichment_model_json)
        assert enrichment_model != False

        # Construct a model instance of Enrichment by calling from_dict on the json representation
        enrichment_model_dict = Enrichment.from_dict(enrichment_model_json).__dict__
        enrichment_model2 = Enrichment(**enrichment_model_dict)

        # Verify the model instances are equivalent
        assert enrichment_model == enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        enrichment_model_json2 = enrichment_model.to_dict()
        assert enrichment_model_json2 == enrichment_model_json

class TestModel_EnrichmentOptions():
    """
    Test Class for EnrichmentOptions
    """

    def test_enrichment_options_serialization(self):
        """
        Test serialization/deserialization for EnrichmentOptions
        """

        # Construct a json representation of a EnrichmentOptions model
        enrichment_options_model_json = {}
        enrichment_options_model_json['languages'] = ['testString']
        enrichment_options_model_json['entity_type'] = 'testString'
        enrichment_options_model_json['regular_expression'] = 'testString'
        enrichment_options_model_json['result_field'] = 'testString'

        # Construct a model instance of EnrichmentOptions by calling from_dict on the json representation
        enrichment_options_model = EnrichmentOptions.from_dict(enrichment_options_model_json)
        assert enrichment_options_model != False

        # Construct a model instance of EnrichmentOptions by calling from_dict on the json representation
        enrichment_options_model_dict = EnrichmentOptions.from_dict(enrichment_options_model_json).__dict__
        enrichment_options_model2 = EnrichmentOptions(**enrichment_options_model_dict)

        # Verify the model instances are equivalent
        assert enrichment_options_model == enrichment_options_model2

        # Convert model instance back to dict and verify no loss of data
        enrichment_options_model_json2 = enrichment_options_model.to_dict()
        assert enrichment_options_model_json2 == enrichment_options_model_json

class TestModel_Enrichments():
    """
    Test Class for Enrichments
    """

    def test_enrichments_serialization(self):
        """
        Test serialization/deserialization for Enrichments
        """

        # Construct dict forms of any model objects needed in order to build this model.

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'

        enrichment_model = {} # Enrichment
        enrichment_model['enrichment_id'] = 'testString'
        enrichment_model['name'] = 'testString'
        enrichment_model['description'] = 'testString'
        enrichment_model['type'] = 'part_of_speech'
        enrichment_model['options'] = enrichment_options_model

        # Construct a json representation of a Enrichments model
        enrichments_model_json = {}
        enrichments_model_json['enrichments'] = [enrichment_model]

        # Construct a model instance of Enrichments by calling from_dict on the json representation
        enrichments_model = Enrichments.from_dict(enrichments_model_json)
        assert enrichments_model != False

        # Construct a model instance of Enrichments by calling from_dict on the json representation
        enrichments_model_dict = Enrichments.from_dict(enrichments_model_json).__dict__
        enrichments_model2 = Enrichments(**enrichments_model_dict)

        # Verify the model instances are equivalent
        assert enrichments_model == enrichments_model2

        # Convert model instance back to dict and verify no loss of data
        enrichments_model_json2 = enrichments_model.to_dict()
        assert enrichments_model_json2 == enrichments_model_json

class TestModel_Field():
    """
    Test Class for Field
    """

    def test_field_serialization(self):
        """
        Test serialization/deserialization for Field
        """

        # Construct a json representation of a Field model
        field_model_json = {}
        field_model_json['field'] = 'testString'
        field_model_json['type'] = 'nested'
        field_model_json['collection_id'] = 'testString'

        # Construct a model instance of Field by calling from_dict on the json representation
        field_model = Field.from_dict(field_model_json)
        assert field_model != False

        # Construct a model instance of Field by calling from_dict on the json representation
        field_model_dict = Field.from_dict(field_model_json).__dict__
        field_model2 = Field(**field_model_dict)

        # Verify the model instances are equivalent
        assert field_model == field_model2

        # Convert model instance back to dict and verify no loss of data
        field_model_json2 = field_model.to_dict()
        assert field_model_json2 == field_model_json

class TestModel_ListCollectionsResponse():
    """
    Test Class for ListCollectionsResponse
    """

    def test_list_collections_response_serialization(self):
        """
        Test serialization/deserialization for ListCollectionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        collection_model = {} # Collection
        collection_model['collection_id'] = 'f1360220-ea2d-4271-9d62-89a910b13c37'
        collection_model['name'] = 'example'

        # Construct a json representation of a ListCollectionsResponse model
        list_collections_response_model_json = {}
        list_collections_response_model_json['collections'] = [collection_model]

        # Construct a model instance of ListCollectionsResponse by calling from_dict on the json representation
        list_collections_response_model = ListCollectionsResponse.from_dict(list_collections_response_model_json)
        assert list_collections_response_model != False

        # Construct a model instance of ListCollectionsResponse by calling from_dict on the json representation
        list_collections_response_model_dict = ListCollectionsResponse.from_dict(list_collections_response_model_json).__dict__
        list_collections_response_model2 = ListCollectionsResponse(**list_collections_response_model_dict)

        # Verify the model instances are equivalent
        assert list_collections_response_model == list_collections_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_collections_response_model_json2 = list_collections_response_model.to_dict()
        assert list_collections_response_model_json2 == list_collections_response_model_json

class TestModel_ListFieldsResponse():
    """
    Test Class for ListFieldsResponse
    """

    def test_list_fields_response_serialization(self):
        """
        Test serialization/deserialization for ListFieldsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        field_model = {} # Field
        field_model['field'] = 'testString'
        field_model['type'] = 'nested'
        field_model['collection_id'] = 'testString'

        # Construct a json representation of a ListFieldsResponse model
        list_fields_response_model_json = {}
        list_fields_response_model_json['fields'] = [field_model]

        # Construct a model instance of ListFieldsResponse by calling from_dict on the json representation
        list_fields_response_model = ListFieldsResponse.from_dict(list_fields_response_model_json)
        assert list_fields_response_model != False

        # Construct a model instance of ListFieldsResponse by calling from_dict on the json representation
        list_fields_response_model_dict = ListFieldsResponse.from_dict(list_fields_response_model_json).__dict__
        list_fields_response_model2 = ListFieldsResponse(**list_fields_response_model_dict)

        # Verify the model instances are equivalent
        assert list_fields_response_model == list_fields_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_fields_response_model_json2 = list_fields_response_model.to_dict()
        assert list_fields_response_model_json2 == list_fields_response_model_json

class TestModel_ListProjectsResponse():
    """
    Test Class for ListProjectsResponse
    """

    def test_list_projects_response_serialization(self):
        """
        Test serialization/deserialization for ListProjectsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_list_details_relevancy_training_status_model = {} # ProjectListDetailsRelevancyTrainingStatus
        project_list_details_relevancy_training_status_model['data_updated'] = 'testString'
        project_list_details_relevancy_training_status_model['total_examples'] = 38
        project_list_details_relevancy_training_status_model['sufficient_label_diversity'] = True
        project_list_details_relevancy_training_status_model['processing'] = True
        project_list_details_relevancy_training_status_model['minimum_examples_added'] = True
        project_list_details_relevancy_training_status_model['successfully_trained'] = 'testString'
        project_list_details_relevancy_training_status_model['available'] = True
        project_list_details_relevancy_training_status_model['notices'] = 38
        project_list_details_relevancy_training_status_model['minimum_queries_added'] = True

        project_list_details_model = {} # ProjectListDetails
        project_list_details_model['project_id'] = 'testString'
        project_list_details_model['name'] = 'testString'
        project_list_details_model['type'] = 'document_retrieval'
        project_list_details_model['relevancy_training_status'] = project_list_details_relevancy_training_status_model
        project_list_details_model['collection_count'] = 38

        # Construct a json representation of a ListProjectsResponse model
        list_projects_response_model_json = {}
        list_projects_response_model_json['projects'] = [project_list_details_model]

        # Construct a model instance of ListProjectsResponse by calling from_dict on the json representation
        list_projects_response_model = ListProjectsResponse.from_dict(list_projects_response_model_json)
        assert list_projects_response_model != False

        # Construct a model instance of ListProjectsResponse by calling from_dict on the json representation
        list_projects_response_model_dict = ListProjectsResponse.from_dict(list_projects_response_model_json).__dict__
        list_projects_response_model2 = ListProjectsResponse(**list_projects_response_model_dict)

        # Verify the model instances are equivalent
        assert list_projects_response_model == list_projects_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_projects_response_model_json2 = list_projects_response_model.to_dict()
        assert list_projects_response_model_json2 == list_projects_response_model_json

class TestModel_Notice():
    """
    Test Class for Notice
    """

    def test_notice_serialization(self):
        """
        Test serialization/deserialization for Notice
        """

        # Construct a json representation of a Notice model
        notice_model_json = {}
        notice_model_json['notice_id'] = 'testString'
        notice_model_json['created'] = "2019-01-01T12:00:00Z"
        notice_model_json['document_id'] = 'testString'
        notice_model_json['collection_id'] = 'testString'
        notice_model_json['query_id'] = 'testString'
        notice_model_json['severity'] = 'warning'
        notice_model_json['step'] = 'testString'
        notice_model_json['description'] = 'testString'

        # Construct a model instance of Notice by calling from_dict on the json representation
        notice_model = Notice.from_dict(notice_model_json)
        assert notice_model != False

        # Construct a model instance of Notice by calling from_dict on the json representation
        notice_model_dict = Notice.from_dict(notice_model_json).__dict__
        notice_model2 = Notice(**notice_model_dict)

        # Verify the model instances are equivalent
        assert notice_model == notice_model2

        # Convert model instance back to dict and verify no loss of data
        notice_model_json2 = notice_model.to_dict()
        assert notice_model_json2 == notice_model_json

class TestModel_ProjectDetails():
    """
    Test Class for ProjectDetails
    """

    def test_project_details_serialization(self):
        """
        Test serialization/deserialization for ProjectDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_list_details_relevancy_training_status_model = {} # ProjectListDetailsRelevancyTrainingStatus
        project_list_details_relevancy_training_status_model['data_updated'] = 'testString'
        project_list_details_relevancy_training_status_model['total_examples'] = 38
        project_list_details_relevancy_training_status_model['sufficient_label_diversity'] = True
        project_list_details_relevancy_training_status_model['processing'] = True
        project_list_details_relevancy_training_status_model['minimum_examples_added'] = True
        project_list_details_relevancy_training_status_model['successfully_trained'] = 'testString'
        project_list_details_relevancy_training_status_model['available'] = True
        project_list_details_relevancy_training_status_model['notices'] = 38
        project_list_details_relevancy_training_status_model['minimum_queries_added'] = True

        default_query_params_passages_model = {} # DefaultQueryParamsPassages
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        default_query_params_table_results_model = {} # DefaultQueryParamsTableResults
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        default_query_params_suggested_refinements_model = {} # DefaultQueryParamsSuggestedRefinements
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        default_query_params_model = {} # DefaultQueryParams
        default_query_params_model['collection_ids'] = ['testString']
        default_query_params_model['passages'] = default_query_params_passages_model
        default_query_params_model['table_results'] = default_query_params_table_results_model
        default_query_params_model['aggregation'] = 'testString'
        default_query_params_model['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model['spelling_suggestions'] = True
        default_query_params_model['highlight'] = True
        default_query_params_model['count'] = 38
        default_query_params_model['sort'] = 'testString'
        default_query_params_model['return'] = ['testString']

        # Construct a json representation of a ProjectDetails model
        project_details_model_json = {}
        project_details_model_json['project_id'] = 'testString'
        project_details_model_json['name'] = 'testString'
        project_details_model_json['type'] = 'document_retrieval'
        project_details_model_json['relevancy_training_status'] = project_list_details_relevancy_training_status_model
        project_details_model_json['collection_count'] = 38
        project_details_model_json['default_query_parameters'] = default_query_params_model

        # Construct a model instance of ProjectDetails by calling from_dict on the json representation
        project_details_model = ProjectDetails.from_dict(project_details_model_json)
        assert project_details_model != False

        # Construct a model instance of ProjectDetails by calling from_dict on the json representation
        project_details_model_dict = ProjectDetails.from_dict(project_details_model_json).__dict__
        project_details_model2 = ProjectDetails(**project_details_model_dict)

        # Verify the model instances are equivalent
        assert project_details_model == project_details_model2

        # Convert model instance back to dict and verify no loss of data
        project_details_model_json2 = project_details_model.to_dict()
        assert project_details_model_json2 == project_details_model_json

class TestModel_ProjectListDetails():
    """
    Test Class for ProjectListDetails
    """

    def test_project_list_details_serialization(self):
        """
        Test serialization/deserialization for ProjectListDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_list_details_relevancy_training_status_model = {} # ProjectListDetailsRelevancyTrainingStatus
        project_list_details_relevancy_training_status_model['data_updated'] = 'testString'
        project_list_details_relevancy_training_status_model['total_examples'] = 38
        project_list_details_relevancy_training_status_model['sufficient_label_diversity'] = True
        project_list_details_relevancy_training_status_model['processing'] = True
        project_list_details_relevancy_training_status_model['minimum_examples_added'] = True
        project_list_details_relevancy_training_status_model['successfully_trained'] = 'testString'
        project_list_details_relevancy_training_status_model['available'] = True
        project_list_details_relevancy_training_status_model['notices'] = 38
        project_list_details_relevancy_training_status_model['minimum_queries_added'] = True

        # Construct a json representation of a ProjectListDetails model
        project_list_details_model_json = {}
        project_list_details_model_json['project_id'] = 'testString'
        project_list_details_model_json['name'] = 'testString'
        project_list_details_model_json['type'] = 'document_retrieval'
        project_list_details_model_json['relevancy_training_status'] = project_list_details_relevancy_training_status_model
        project_list_details_model_json['collection_count'] = 38

        # Construct a model instance of ProjectListDetails by calling from_dict on the json representation
        project_list_details_model = ProjectListDetails.from_dict(project_list_details_model_json)
        assert project_list_details_model != False

        # Construct a model instance of ProjectListDetails by calling from_dict on the json representation
        project_list_details_model_dict = ProjectListDetails.from_dict(project_list_details_model_json).__dict__
        project_list_details_model2 = ProjectListDetails(**project_list_details_model_dict)

        # Verify the model instances are equivalent
        assert project_list_details_model == project_list_details_model2

        # Convert model instance back to dict and verify no loss of data
        project_list_details_model_json2 = project_list_details_model.to_dict()
        assert project_list_details_model_json2 == project_list_details_model_json

class TestModel_ProjectListDetailsRelevancyTrainingStatus():
    """
    Test Class for ProjectListDetailsRelevancyTrainingStatus
    """

    def test_project_list_details_relevancy_training_status_serialization(self):
        """
        Test serialization/deserialization for ProjectListDetailsRelevancyTrainingStatus
        """

        # Construct a json representation of a ProjectListDetailsRelevancyTrainingStatus model
        project_list_details_relevancy_training_status_model_json = {}
        project_list_details_relevancy_training_status_model_json['data_updated'] = 'testString'
        project_list_details_relevancy_training_status_model_json['total_examples'] = 38
        project_list_details_relevancy_training_status_model_json['sufficient_label_diversity'] = True
        project_list_details_relevancy_training_status_model_json['processing'] = True
        project_list_details_relevancy_training_status_model_json['minimum_examples_added'] = True
        project_list_details_relevancy_training_status_model_json['successfully_trained'] = 'testString'
        project_list_details_relevancy_training_status_model_json['available'] = True
        project_list_details_relevancy_training_status_model_json['notices'] = 38
        project_list_details_relevancy_training_status_model_json['minimum_queries_added'] = True

        # Construct a model instance of ProjectListDetailsRelevancyTrainingStatus by calling from_dict on the json representation
        project_list_details_relevancy_training_status_model = ProjectListDetailsRelevancyTrainingStatus.from_dict(project_list_details_relevancy_training_status_model_json)
        assert project_list_details_relevancy_training_status_model != False

        # Construct a model instance of ProjectListDetailsRelevancyTrainingStatus by calling from_dict on the json representation
        project_list_details_relevancy_training_status_model_dict = ProjectListDetailsRelevancyTrainingStatus.from_dict(project_list_details_relevancy_training_status_model_json).__dict__
        project_list_details_relevancy_training_status_model2 = ProjectListDetailsRelevancyTrainingStatus(**project_list_details_relevancy_training_status_model_dict)

        # Verify the model instances are equivalent
        assert project_list_details_relevancy_training_status_model == project_list_details_relevancy_training_status_model2

        # Convert model instance back to dict and verify no loss of data
        project_list_details_relevancy_training_status_model_json2 = project_list_details_relevancy_training_status_model.to_dict()
        assert project_list_details_relevancy_training_status_model_json2 == project_list_details_relevancy_training_status_model_json

class TestModel_QueryAggregation():
    """
    Test Class for QueryAggregation
    """

    def test_query_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregation
        """

        # Construct a json representation of a QueryAggregation model
        query_aggregation_model_json = {}
        query_aggregation_model_json['type'] = 'testString'

        # Construct a model instance of QueryAggregation by calling from_dict on the json representation
        query_aggregation_model = QueryAggregation.from_dict(query_aggregation_model_json)
        assert query_aggregation_model != False

        # Construct a copy of the model instance by calling from_dict on the output of to_dict
        query_aggregation_model_json2 = query_aggregation_model.to_dict()
        query_aggregation_model2 = QueryAggregation.from_dict(query_aggregation_model_json2)

        # Verify the model instances are equivalent
        assert query_aggregation_model == query_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_model_json2 = query_aggregation_model.to_dict()
        assert query_aggregation_model_json2 == query_aggregation_model_json

class TestModel_QueryGroupByAggregationResult():
    """
    Test Class for QueryGroupByAggregationResult
    """

    def test_query_group_by_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryGroupByAggregationResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_aggregation_model = {} # QueryFilterAggregation
        query_aggregation_model['type'] = 'filter'
        query_aggregation_model['match'] = 'testString'
        query_aggregation_model['matching_results'] = 26

        # Construct a json representation of a QueryGroupByAggregationResult model
        query_group_by_aggregation_result_model_json = {}
        query_group_by_aggregation_result_model_json['key'] = 'testString'
        query_group_by_aggregation_result_model_json['matching_results'] = 38
        query_group_by_aggregation_result_model_json['relevancy'] = 72.5
        query_group_by_aggregation_result_model_json['total_matching_documents'] = 38
        query_group_by_aggregation_result_model_json['estimated_matching_documents'] = 38
        query_group_by_aggregation_result_model_json['aggregations'] = [query_aggregation_model]

        # Construct a model instance of QueryGroupByAggregationResult by calling from_dict on the json representation
        query_group_by_aggregation_result_model = QueryGroupByAggregationResult.from_dict(query_group_by_aggregation_result_model_json)
        assert query_group_by_aggregation_result_model != False

        # Construct a model instance of QueryGroupByAggregationResult by calling from_dict on the json representation
        query_group_by_aggregation_result_model_dict = QueryGroupByAggregationResult.from_dict(query_group_by_aggregation_result_model_json).__dict__
        query_group_by_aggregation_result_model2 = QueryGroupByAggregationResult(**query_group_by_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_group_by_aggregation_result_model == query_group_by_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_group_by_aggregation_result_model_json2 = query_group_by_aggregation_result_model.to_dict()
        assert query_group_by_aggregation_result_model_json2 == query_group_by_aggregation_result_model_json

class TestModel_QueryHistogramAggregationResult():
    """
    Test Class for QueryHistogramAggregationResult
    """

    def test_query_histogram_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryHistogramAggregationResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_aggregation_model = {} # QueryFilterAggregation
        query_aggregation_model['type'] = 'filter'
        query_aggregation_model['match'] = 'testString'
        query_aggregation_model['matching_results'] = 26

        # Construct a json representation of a QueryHistogramAggregationResult model
        query_histogram_aggregation_result_model_json = {}
        query_histogram_aggregation_result_model_json['key'] = 26
        query_histogram_aggregation_result_model_json['matching_results'] = 38
        query_histogram_aggregation_result_model_json['aggregations'] = [query_aggregation_model]

        # Construct a model instance of QueryHistogramAggregationResult by calling from_dict on the json representation
        query_histogram_aggregation_result_model = QueryHistogramAggregationResult.from_dict(query_histogram_aggregation_result_model_json)
        assert query_histogram_aggregation_result_model != False

        # Construct a model instance of QueryHistogramAggregationResult by calling from_dict on the json representation
        query_histogram_aggregation_result_model_dict = QueryHistogramAggregationResult.from_dict(query_histogram_aggregation_result_model_json).__dict__
        query_histogram_aggregation_result_model2 = QueryHistogramAggregationResult(**query_histogram_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_histogram_aggregation_result_model == query_histogram_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_histogram_aggregation_result_model_json2 = query_histogram_aggregation_result_model.to_dict()
        assert query_histogram_aggregation_result_model_json2 == query_histogram_aggregation_result_model_json

class TestModel_QueryLargePassages():
    """
    Test Class for QueryLargePassages
    """

    def test_query_large_passages_serialization(self):
        """
        Test serialization/deserialization for QueryLargePassages
        """

        # Construct a json representation of a QueryLargePassages model
        query_large_passages_model_json = {}
        query_large_passages_model_json['enabled'] = True
        query_large_passages_model_json['per_document'] = True
        query_large_passages_model_json['max_per_document'] = 38
        query_large_passages_model_json['fields'] = ['testString']
        query_large_passages_model_json['count'] = 400
        query_large_passages_model_json['characters'] = 50
        query_large_passages_model_json['find_answers'] = False
        query_large_passages_model_json['max_answers_per_passage'] = 38

        # Construct a model instance of QueryLargePassages by calling from_dict on the json representation
        query_large_passages_model = QueryLargePassages.from_dict(query_large_passages_model_json)
        assert query_large_passages_model != False

        # Construct a model instance of QueryLargePassages by calling from_dict on the json representation
        query_large_passages_model_dict = QueryLargePassages.from_dict(query_large_passages_model_json).__dict__
        query_large_passages_model2 = QueryLargePassages(**query_large_passages_model_dict)

        # Verify the model instances are equivalent
        assert query_large_passages_model == query_large_passages_model2

        # Convert model instance back to dict and verify no loss of data
        query_large_passages_model_json2 = query_large_passages_model.to_dict()
        assert query_large_passages_model_json2 == query_large_passages_model_json

class TestModel_QueryLargeSuggestedRefinements():
    """
    Test Class for QueryLargeSuggestedRefinements
    """

    def test_query_large_suggested_refinements_serialization(self):
        """
        Test serialization/deserialization for QueryLargeSuggestedRefinements
        """

        # Construct a json representation of a QueryLargeSuggestedRefinements model
        query_large_suggested_refinements_model_json = {}
        query_large_suggested_refinements_model_json['enabled'] = True
        query_large_suggested_refinements_model_json['count'] = 1

        # Construct a model instance of QueryLargeSuggestedRefinements by calling from_dict on the json representation
        query_large_suggested_refinements_model = QueryLargeSuggestedRefinements.from_dict(query_large_suggested_refinements_model_json)
        assert query_large_suggested_refinements_model != False

        # Construct a model instance of QueryLargeSuggestedRefinements by calling from_dict on the json representation
        query_large_suggested_refinements_model_dict = QueryLargeSuggestedRefinements.from_dict(query_large_suggested_refinements_model_json).__dict__
        query_large_suggested_refinements_model2 = QueryLargeSuggestedRefinements(**query_large_suggested_refinements_model_dict)

        # Verify the model instances are equivalent
        assert query_large_suggested_refinements_model == query_large_suggested_refinements_model2

        # Convert model instance back to dict and verify no loss of data
        query_large_suggested_refinements_model_json2 = query_large_suggested_refinements_model.to_dict()
        assert query_large_suggested_refinements_model_json2 == query_large_suggested_refinements_model_json

class TestModel_QueryLargeTableResults():
    """
    Test Class for QueryLargeTableResults
    """

    def test_query_large_table_results_serialization(self):
        """
        Test serialization/deserialization for QueryLargeTableResults
        """

        # Construct a json representation of a QueryLargeTableResults model
        query_large_table_results_model_json = {}
        query_large_table_results_model_json['enabled'] = True
        query_large_table_results_model_json['count'] = 38

        # Construct a model instance of QueryLargeTableResults by calling from_dict on the json representation
        query_large_table_results_model = QueryLargeTableResults.from_dict(query_large_table_results_model_json)
        assert query_large_table_results_model != False

        # Construct a model instance of QueryLargeTableResults by calling from_dict on the json representation
        query_large_table_results_model_dict = QueryLargeTableResults.from_dict(query_large_table_results_model_json).__dict__
        query_large_table_results_model2 = QueryLargeTableResults(**query_large_table_results_model_dict)

        # Verify the model instances are equivalent
        assert query_large_table_results_model == query_large_table_results_model2

        # Convert model instance back to dict and verify no loss of data
        query_large_table_results_model_json2 = query_large_table_results_model.to_dict()
        assert query_large_table_results_model_json2 == query_large_table_results_model_json

class TestModel_QueryNoticesResponse():
    """
    Test Class for QueryNoticesResponse
    """

    def test_query_notices_response_serialization(self):
        """
        Test serialization/deserialization for QueryNoticesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice
        notice_model['notice_id'] = 'testString'
        notice_model['created'] = "2019-01-01T12:00:00Z"
        notice_model['document_id'] = 'testString'
        notice_model['collection_id'] = 'testString'
        notice_model['query_id'] = 'testString'
        notice_model['severity'] = 'warning'
        notice_model['step'] = 'testString'
        notice_model['description'] = 'testString'

        # Construct a json representation of a QueryNoticesResponse model
        query_notices_response_model_json = {}
        query_notices_response_model_json['matching_results'] = 38
        query_notices_response_model_json['notices'] = [notice_model]

        # Construct a model instance of QueryNoticesResponse by calling from_dict on the json representation
        query_notices_response_model = QueryNoticesResponse.from_dict(query_notices_response_model_json)
        assert query_notices_response_model != False

        # Construct a model instance of QueryNoticesResponse by calling from_dict on the json representation
        query_notices_response_model_dict = QueryNoticesResponse.from_dict(query_notices_response_model_json).__dict__
        query_notices_response_model2 = QueryNoticesResponse(**query_notices_response_model_dict)

        # Verify the model instances are equivalent
        assert query_notices_response_model == query_notices_response_model2

        # Convert model instance back to dict and verify no loss of data
        query_notices_response_model_json2 = query_notices_response_model.to_dict()
        assert query_notices_response_model_json2 == query_notices_response_model_json

class TestModel_QueryResponse():
    """
    Test Class for QueryResponse
    """

    def test_query_response_serialization(self):
        """
        Test serialization/deserialization for QueryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['document_retrieval_source'] = 'search'
        query_result_metadata_model['collection_id'] = 'testString'
        query_result_metadata_model['confidence'] = 72.5

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        query_result_passage_model = {} # QueryResultPassage
        query_result_passage_model['passage_text'] = 'testString'
        query_result_passage_model['start_offset'] = 38
        query_result_passage_model['end_offset'] = 38
        query_result_passage_model['field'] = 'testString'
        query_result_passage_model['confidence'] = 0
        query_result_passage_model['answers'] = [result_passage_answer_model]

        query_result_model = {} # QueryResult
        query_result_model['document_id'] = 'testString'
        query_result_model['metadata'] = {}
        query_result_model['result_metadata'] = query_result_metadata_model
        query_result_model['document_passages'] = [query_result_passage_model]
        query_result_model['id'] = { 'foo': 'bar' }

        query_aggregation_model = {} # QueryFilterAggregation
        query_aggregation_model['type'] = 'filter'
        query_aggregation_model['match'] = 'testString'
        query_aggregation_model['matching_results'] = 26

        retrieval_details_model = {} # RetrievalDetails
        retrieval_details_model['document_retrieval_strategy'] = 'untrained'

        query_suggested_refinement_model = {} # QuerySuggestedRefinement
        query_suggested_refinement_model['text'] = 'testString'

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_text_location_model = {} # TableTextLocation
        table_text_location_model['text'] = 'testString'
        table_text_location_model['location'] = table_element_location_model

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = { 'foo': 'bar' }
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        table_row_headers_model = {} # TableRowHeaders
        table_row_headers_model['cell_id'] = 'testString'
        table_row_headers_model['location'] = table_element_location_model
        table_row_headers_model['text'] = 'testString'
        table_row_headers_model['text_normalized'] = 'testString'
        table_row_headers_model['row_index_begin'] = 26
        table_row_headers_model['row_index_end'] = 26
        table_row_headers_model['column_index_begin'] = 26
        table_row_headers_model['column_index_end'] = 26

        table_column_headers_model = {} # TableColumnHeaders
        table_column_headers_model['cell_id'] = 'testString'
        table_column_headers_model['location'] = { 'foo': 'bar' }
        table_column_headers_model['text'] = 'testString'
        table_column_headers_model['text_normalized'] = 'testString'
        table_column_headers_model['row_index_begin'] = 26
        table_column_headers_model['row_index_end'] = 26
        table_column_headers_model['column_index_begin'] = 26
        table_column_headers_model['column_index_end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        table_key_value_pairs_model = {} # TableKeyValuePairs
        table_key_value_pairs_model['key'] = table_cell_key_model
        table_key_value_pairs_model['value'] = [table_cell_values_model]

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        table_body_cells_model = {} # TableBodyCells
        table_body_cells_model['cell_id'] = 'testString'
        table_body_cells_model['location'] = table_element_location_model
        table_body_cells_model['text'] = 'testString'
        table_body_cells_model['row_index_begin'] = 26
        table_body_cells_model['row_index_end'] = 26
        table_body_cells_model['column_index_begin'] = 26
        table_body_cells_model['column_index_end'] = 26
        table_body_cells_model['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model['attributes'] = [document_attribute_model]

        table_result_table_model = {} # TableResultTable
        table_result_table_model['location'] = table_element_location_model
        table_result_table_model['text'] = 'testString'
        table_result_table_model['section_title'] = table_text_location_model
        table_result_table_model['title'] = table_text_location_model
        table_result_table_model['table_headers'] = [table_headers_model]
        table_result_table_model['row_headers'] = [table_row_headers_model]
        table_result_table_model['column_headers'] = [table_column_headers_model]
        table_result_table_model['key_value_pairs'] = [table_key_value_pairs_model]
        table_result_table_model['body_cells'] = [table_body_cells_model]
        table_result_table_model['contexts'] = [table_text_location_model]

        query_table_result_model = {} # QueryTableResult
        query_table_result_model['table_id'] = 'testString'
        query_table_result_model['source_document_id'] = 'testString'
        query_table_result_model['collection_id'] = 'testString'
        query_table_result_model['table_html'] = 'testString'
        query_table_result_model['table_html_offset'] = 38
        query_table_result_model['table'] = table_result_table_model

        query_response_passage_model = {} # QueryResponsePassage
        query_response_passage_model['passage_text'] = 'testString'
        query_response_passage_model['passage_score'] = 72.5
        query_response_passage_model['document_id'] = 'testString'
        query_response_passage_model['collection_id'] = 'testString'
        query_response_passage_model['start_offset'] = 38
        query_response_passage_model['end_offset'] = 38
        query_response_passage_model['field'] = 'testString'
        query_response_passage_model['confidence'] = 0
        query_response_passage_model['answers'] = [result_passage_answer_model]

        # Construct a json representation of a QueryResponse model
        query_response_model_json = {}
        query_response_model_json['matching_results'] = 38
        query_response_model_json['results'] = [query_result_model]
        query_response_model_json['aggregations'] = [query_aggregation_model]
        query_response_model_json['retrieval_details'] = retrieval_details_model
        query_response_model_json['suggested_query'] = 'testString'
        query_response_model_json['suggested_refinements'] = [query_suggested_refinement_model]
        query_response_model_json['table_results'] = [query_table_result_model]
        query_response_model_json['passages'] = [query_response_passage_model]

        # Construct a model instance of QueryResponse by calling from_dict on the json representation
        query_response_model = QueryResponse.from_dict(query_response_model_json)
        assert query_response_model != False

        # Construct a model instance of QueryResponse by calling from_dict on the json representation
        query_response_model_dict = QueryResponse.from_dict(query_response_model_json).__dict__
        query_response_model2 = QueryResponse(**query_response_model_dict)

        # Verify the model instances are equivalent
        assert query_response_model == query_response_model2

        # Convert model instance back to dict and verify no loss of data
        query_response_model_json2 = query_response_model.to_dict()
        assert query_response_model_json2 == query_response_model_json

class TestModel_QueryResponsePassage():
    """
    Test Class for QueryResponsePassage
    """

    def test_query_response_passage_serialization(self):
        """
        Test serialization/deserialization for QueryResponsePassage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        # Construct a json representation of a QueryResponsePassage model
        query_response_passage_model_json = {}
        query_response_passage_model_json['passage_text'] = 'testString'
        query_response_passage_model_json['passage_score'] = 72.5
        query_response_passage_model_json['document_id'] = 'testString'
        query_response_passage_model_json['collection_id'] = 'testString'
        query_response_passage_model_json['start_offset'] = 38
        query_response_passage_model_json['end_offset'] = 38
        query_response_passage_model_json['field'] = 'testString'
        query_response_passage_model_json['confidence'] = 0
        query_response_passage_model_json['answers'] = [result_passage_answer_model]

        # Construct a model instance of QueryResponsePassage by calling from_dict on the json representation
        query_response_passage_model = QueryResponsePassage.from_dict(query_response_passage_model_json)
        assert query_response_passage_model != False

        # Construct a model instance of QueryResponsePassage by calling from_dict on the json representation
        query_response_passage_model_dict = QueryResponsePassage.from_dict(query_response_passage_model_json).__dict__
        query_response_passage_model2 = QueryResponsePassage(**query_response_passage_model_dict)

        # Verify the model instances are equivalent
        assert query_response_passage_model == query_response_passage_model2

        # Convert model instance back to dict and verify no loss of data
        query_response_passage_model_json2 = query_response_passage_model.to_dict()
        assert query_response_passage_model_json2 == query_response_passage_model_json

class TestModel_QueryResult():
    """
    Test Class for QueryResult
    """

    def test_query_result_serialization(self):
        """
        Test serialization/deserialization for QueryResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['document_retrieval_source'] = 'search'
        query_result_metadata_model['collection_id'] = 'testString'
        query_result_metadata_model['confidence'] = 72.5

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        query_result_passage_model = {} # QueryResultPassage
        query_result_passage_model['passage_text'] = 'testString'
        query_result_passage_model['start_offset'] = 38
        query_result_passage_model['end_offset'] = 38
        query_result_passage_model['field'] = 'testString'
        query_result_passage_model['confidence'] = 0
        query_result_passage_model['answers'] = [result_passage_answer_model]

        # Construct a json representation of a QueryResult model
        query_result_model_json = {}
        query_result_model_json['document_id'] = 'testString'
        query_result_model_json['metadata'] = {}
        query_result_model_json['result_metadata'] = query_result_metadata_model
        query_result_model_json['document_passages'] = [query_result_passage_model]
        query_result_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of QueryResult by calling from_dict on the json representation
        query_result_model = QueryResult.from_dict(query_result_model_json)
        assert query_result_model != False

        # Construct a model instance of QueryResult by calling from_dict on the json representation
        query_result_model_dict = QueryResult.from_dict(query_result_model_json).__dict__
        query_result_model2 = QueryResult(**query_result_model_dict)

        # Verify the model instances are equivalent
        assert query_result_model == query_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_model_json2 = query_result_model.to_dict()
        assert query_result_model_json2 == query_result_model_json

        # Test get_properties and set_properties methods.
        query_result_model.set_properties({})
        actual_dict = query_result_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': { 'foo': 'bar' }}
        query_result_model.set_properties(expected_dict)
        actual_dict = query_result_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_QueryResultMetadata():
    """
    Test Class for QueryResultMetadata
    """

    def test_query_result_metadata_serialization(self):
        """
        Test serialization/deserialization for QueryResultMetadata
        """

        # Construct a json representation of a QueryResultMetadata model
        query_result_metadata_model_json = {}
        query_result_metadata_model_json['document_retrieval_source'] = 'search'
        query_result_metadata_model_json['collection_id'] = 'testString'
        query_result_metadata_model_json['confidence'] = 72.5

        # Construct a model instance of QueryResultMetadata by calling from_dict on the json representation
        query_result_metadata_model = QueryResultMetadata.from_dict(query_result_metadata_model_json)
        assert query_result_metadata_model != False

        # Construct a model instance of QueryResultMetadata by calling from_dict on the json representation
        query_result_metadata_model_dict = QueryResultMetadata.from_dict(query_result_metadata_model_json).__dict__
        query_result_metadata_model2 = QueryResultMetadata(**query_result_metadata_model_dict)

        # Verify the model instances are equivalent
        assert query_result_metadata_model == query_result_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_metadata_model_json2 = query_result_metadata_model.to_dict()
        assert query_result_metadata_model_json2 == query_result_metadata_model_json

class TestModel_QueryResultPassage():
    """
    Test Class for QueryResultPassage
    """

    def test_query_result_passage_serialization(self):
        """
        Test serialization/deserialization for QueryResultPassage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        # Construct a json representation of a QueryResultPassage model
        query_result_passage_model_json = {}
        query_result_passage_model_json['passage_text'] = 'testString'
        query_result_passage_model_json['start_offset'] = 38
        query_result_passage_model_json['end_offset'] = 38
        query_result_passage_model_json['field'] = 'testString'
        query_result_passage_model_json['confidence'] = 0
        query_result_passage_model_json['answers'] = [result_passage_answer_model]

        # Construct a model instance of QueryResultPassage by calling from_dict on the json representation
        query_result_passage_model = QueryResultPassage.from_dict(query_result_passage_model_json)
        assert query_result_passage_model != False

        # Construct a model instance of QueryResultPassage by calling from_dict on the json representation
        query_result_passage_model_dict = QueryResultPassage.from_dict(query_result_passage_model_json).__dict__
        query_result_passage_model2 = QueryResultPassage(**query_result_passage_model_dict)

        # Verify the model instances are equivalent
        assert query_result_passage_model == query_result_passage_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_passage_model_json2 = query_result_passage_model.to_dict()
        assert query_result_passage_model_json2 == query_result_passage_model_json

class TestModel_QuerySuggestedRefinement():
    """
    Test Class for QuerySuggestedRefinement
    """

    def test_query_suggested_refinement_serialization(self):
        """
        Test serialization/deserialization for QuerySuggestedRefinement
        """

        # Construct a json representation of a QuerySuggestedRefinement model
        query_suggested_refinement_model_json = {}
        query_suggested_refinement_model_json['text'] = 'testString'

        # Construct a model instance of QuerySuggestedRefinement by calling from_dict on the json representation
        query_suggested_refinement_model = QuerySuggestedRefinement.from_dict(query_suggested_refinement_model_json)
        assert query_suggested_refinement_model != False

        # Construct a model instance of QuerySuggestedRefinement by calling from_dict on the json representation
        query_suggested_refinement_model_dict = QuerySuggestedRefinement.from_dict(query_suggested_refinement_model_json).__dict__
        query_suggested_refinement_model2 = QuerySuggestedRefinement(**query_suggested_refinement_model_dict)

        # Verify the model instances are equivalent
        assert query_suggested_refinement_model == query_suggested_refinement_model2

        # Convert model instance back to dict and verify no loss of data
        query_suggested_refinement_model_json2 = query_suggested_refinement_model.to_dict()
        assert query_suggested_refinement_model_json2 == query_suggested_refinement_model_json

class TestModel_QueryTableResult():
    """
    Test Class for QueryTableResult
    """

    def test_query_table_result_serialization(self):
        """
        Test serialization/deserialization for QueryTableResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_text_location_model = {} # TableTextLocation
        table_text_location_model['text'] = 'testString'
        table_text_location_model['location'] = table_element_location_model

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = { 'foo': 'bar' }
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        table_row_headers_model = {} # TableRowHeaders
        table_row_headers_model['cell_id'] = 'testString'
        table_row_headers_model['location'] = table_element_location_model
        table_row_headers_model['text'] = 'testString'
        table_row_headers_model['text_normalized'] = 'testString'
        table_row_headers_model['row_index_begin'] = 26
        table_row_headers_model['row_index_end'] = 26
        table_row_headers_model['column_index_begin'] = 26
        table_row_headers_model['column_index_end'] = 26

        table_column_headers_model = {} # TableColumnHeaders
        table_column_headers_model['cell_id'] = 'testString'
        table_column_headers_model['location'] = { 'foo': 'bar' }
        table_column_headers_model['text'] = 'testString'
        table_column_headers_model['text_normalized'] = 'testString'
        table_column_headers_model['row_index_begin'] = 26
        table_column_headers_model['row_index_end'] = 26
        table_column_headers_model['column_index_begin'] = 26
        table_column_headers_model['column_index_end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        table_key_value_pairs_model = {} # TableKeyValuePairs
        table_key_value_pairs_model['key'] = table_cell_key_model
        table_key_value_pairs_model['value'] = [table_cell_values_model]

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        table_body_cells_model = {} # TableBodyCells
        table_body_cells_model['cell_id'] = 'testString'
        table_body_cells_model['location'] = table_element_location_model
        table_body_cells_model['text'] = 'testString'
        table_body_cells_model['row_index_begin'] = 26
        table_body_cells_model['row_index_end'] = 26
        table_body_cells_model['column_index_begin'] = 26
        table_body_cells_model['column_index_end'] = 26
        table_body_cells_model['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model['attributes'] = [document_attribute_model]

        table_result_table_model = {} # TableResultTable
        table_result_table_model['location'] = table_element_location_model
        table_result_table_model['text'] = 'testString'
        table_result_table_model['section_title'] = table_text_location_model
        table_result_table_model['title'] = table_text_location_model
        table_result_table_model['table_headers'] = [table_headers_model]
        table_result_table_model['row_headers'] = [table_row_headers_model]
        table_result_table_model['column_headers'] = [table_column_headers_model]
        table_result_table_model['key_value_pairs'] = [table_key_value_pairs_model]
        table_result_table_model['body_cells'] = [table_body_cells_model]
        table_result_table_model['contexts'] = [table_text_location_model]

        # Construct a json representation of a QueryTableResult model
        query_table_result_model_json = {}
        query_table_result_model_json['table_id'] = 'testString'
        query_table_result_model_json['source_document_id'] = 'testString'
        query_table_result_model_json['collection_id'] = 'testString'
        query_table_result_model_json['table_html'] = 'testString'
        query_table_result_model_json['table_html_offset'] = 38
        query_table_result_model_json['table'] = table_result_table_model

        # Construct a model instance of QueryTableResult by calling from_dict on the json representation
        query_table_result_model = QueryTableResult.from_dict(query_table_result_model_json)
        assert query_table_result_model != False

        # Construct a model instance of QueryTableResult by calling from_dict on the json representation
        query_table_result_model_dict = QueryTableResult.from_dict(query_table_result_model_json).__dict__
        query_table_result_model2 = QueryTableResult(**query_table_result_model_dict)

        # Verify the model instances are equivalent
        assert query_table_result_model == query_table_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_table_result_model_json2 = query_table_result_model.to_dict()
        assert query_table_result_model_json2 == query_table_result_model_json

class TestModel_QueryTermAggregationResult():
    """
    Test Class for QueryTermAggregationResult
    """

    def test_query_term_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTermAggregationResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_aggregation_model = {} # QueryFilterAggregation
        query_aggregation_model['type'] = 'filter'
        query_aggregation_model['match'] = 'testString'
        query_aggregation_model['matching_results'] = 26

        # Construct a json representation of a QueryTermAggregationResult model
        query_term_aggregation_result_model_json = {}
        query_term_aggregation_result_model_json['key'] = 'testString'
        query_term_aggregation_result_model_json['matching_results'] = 38
        query_term_aggregation_result_model_json['relevancy'] = 72.5
        query_term_aggregation_result_model_json['total_matching_documents'] = 38
        query_term_aggregation_result_model_json['estimated_matching_documents'] = 38
        query_term_aggregation_result_model_json['aggregations'] = [query_aggregation_model]

        # Construct a model instance of QueryTermAggregationResult by calling from_dict on the json representation
        query_term_aggregation_result_model = QueryTermAggregationResult.from_dict(query_term_aggregation_result_model_json)
        assert query_term_aggregation_result_model != False

        # Construct a model instance of QueryTermAggregationResult by calling from_dict on the json representation
        query_term_aggregation_result_model_dict = QueryTermAggregationResult.from_dict(query_term_aggregation_result_model_json).__dict__
        query_term_aggregation_result_model2 = QueryTermAggregationResult(**query_term_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_term_aggregation_result_model == query_term_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_term_aggregation_result_model_json2 = query_term_aggregation_result_model.to_dict()
        assert query_term_aggregation_result_model_json2 == query_term_aggregation_result_model_json

class TestModel_QueryTimesliceAggregationResult():
    """
    Test Class for QueryTimesliceAggregationResult
    """

    def test_query_timeslice_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTimesliceAggregationResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_aggregation_model = {} # QueryFilterAggregation
        query_aggregation_model['type'] = 'filter'
        query_aggregation_model['match'] = 'testString'
        query_aggregation_model['matching_results'] = 26

        # Construct a json representation of a QueryTimesliceAggregationResult model
        query_timeslice_aggregation_result_model_json = {}
        query_timeslice_aggregation_result_model_json['key_as_string'] = 'testString'
        query_timeslice_aggregation_result_model_json['key'] = 26
        query_timeslice_aggregation_result_model_json['matching_results'] = 26
        query_timeslice_aggregation_result_model_json['aggregations'] = [query_aggregation_model]

        # Construct a model instance of QueryTimesliceAggregationResult by calling from_dict on the json representation
        query_timeslice_aggregation_result_model = QueryTimesliceAggregationResult.from_dict(query_timeslice_aggregation_result_model_json)
        assert query_timeslice_aggregation_result_model != False

        # Construct a model instance of QueryTimesliceAggregationResult by calling from_dict on the json representation
        query_timeslice_aggregation_result_model_dict = QueryTimesliceAggregationResult.from_dict(query_timeslice_aggregation_result_model_json).__dict__
        query_timeslice_aggregation_result_model2 = QueryTimesliceAggregationResult(**query_timeslice_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_timeslice_aggregation_result_model == query_timeslice_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_timeslice_aggregation_result_model_json2 = query_timeslice_aggregation_result_model.to_dict()
        assert query_timeslice_aggregation_result_model_json2 == query_timeslice_aggregation_result_model_json

class TestModel_QueryTopHitsAggregationResult():
    """
    Test Class for QueryTopHitsAggregationResult
    """

    def test_query_top_hits_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTopHitsAggregationResult
        """

        # Construct a json representation of a QueryTopHitsAggregationResult model
        query_top_hits_aggregation_result_model_json = {}
        query_top_hits_aggregation_result_model_json['matching_results'] = 38
        query_top_hits_aggregation_result_model_json['hits'] = [{}]

        # Construct a model instance of QueryTopHitsAggregationResult by calling from_dict on the json representation
        query_top_hits_aggregation_result_model = QueryTopHitsAggregationResult.from_dict(query_top_hits_aggregation_result_model_json)
        assert query_top_hits_aggregation_result_model != False

        # Construct a model instance of QueryTopHitsAggregationResult by calling from_dict on the json representation
        query_top_hits_aggregation_result_model_dict = QueryTopHitsAggregationResult.from_dict(query_top_hits_aggregation_result_model_json).__dict__
        query_top_hits_aggregation_result_model2 = QueryTopHitsAggregationResult(**query_top_hits_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_top_hits_aggregation_result_model == query_top_hits_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_top_hits_aggregation_result_model_json2 = query_top_hits_aggregation_result_model.to_dict()
        assert query_top_hits_aggregation_result_model_json2 == query_top_hits_aggregation_result_model_json

class TestModel_ResultPassageAnswer():
    """
    Test Class for ResultPassageAnswer
    """

    def test_result_passage_answer_serialization(self):
        """
        Test serialization/deserialization for ResultPassageAnswer
        """

        # Construct a json representation of a ResultPassageAnswer model
        result_passage_answer_model_json = {}
        result_passage_answer_model_json['answer_text'] = 'testString'
        result_passage_answer_model_json['start_offset'] = 38
        result_passage_answer_model_json['end_offset'] = 38
        result_passage_answer_model_json['confidence'] = 0

        # Construct a model instance of ResultPassageAnswer by calling from_dict on the json representation
        result_passage_answer_model = ResultPassageAnswer.from_dict(result_passage_answer_model_json)
        assert result_passage_answer_model != False

        # Construct a model instance of ResultPassageAnswer by calling from_dict on the json representation
        result_passage_answer_model_dict = ResultPassageAnswer.from_dict(result_passage_answer_model_json).__dict__
        result_passage_answer_model2 = ResultPassageAnswer(**result_passage_answer_model_dict)

        # Verify the model instances are equivalent
        assert result_passage_answer_model == result_passage_answer_model2

        # Convert model instance back to dict and verify no loss of data
        result_passage_answer_model_json2 = result_passage_answer_model.to_dict()
        assert result_passage_answer_model_json2 == result_passage_answer_model_json

class TestModel_RetrievalDetails():
    """
    Test Class for RetrievalDetails
    """

    def test_retrieval_details_serialization(self):
        """
        Test serialization/deserialization for RetrievalDetails
        """

        # Construct a json representation of a RetrievalDetails model
        retrieval_details_model_json = {}
        retrieval_details_model_json['document_retrieval_strategy'] = 'untrained'

        # Construct a model instance of RetrievalDetails by calling from_dict on the json representation
        retrieval_details_model = RetrievalDetails.from_dict(retrieval_details_model_json)
        assert retrieval_details_model != False

        # Construct a model instance of RetrievalDetails by calling from_dict on the json representation
        retrieval_details_model_dict = RetrievalDetails.from_dict(retrieval_details_model_json).__dict__
        retrieval_details_model2 = RetrievalDetails(**retrieval_details_model_dict)

        # Verify the model instances are equivalent
        assert retrieval_details_model == retrieval_details_model2

        # Convert model instance back to dict and verify no loss of data
        retrieval_details_model_json2 = retrieval_details_model.to_dict()
        assert retrieval_details_model_json2 == retrieval_details_model_json

class TestModel_TableBodyCells():
    """
    Test Class for TableBodyCells
    """

    def test_table_body_cells_serialization(self):
        """
        Test serialization/deserialization for TableBodyCells
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        # Construct a json representation of a TableBodyCells model
        table_body_cells_model_json = {}
        table_body_cells_model_json['cell_id'] = 'testString'
        table_body_cells_model_json['location'] = table_element_location_model
        table_body_cells_model_json['text'] = 'testString'
        table_body_cells_model_json['row_index_begin'] = 26
        table_body_cells_model_json['row_index_end'] = 26
        table_body_cells_model_json['column_index_begin'] = 26
        table_body_cells_model_json['column_index_end'] = 26
        table_body_cells_model_json['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model_json['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model_json['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model_json['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model_json['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model_json['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model_json['attributes'] = [document_attribute_model]

        # Construct a model instance of TableBodyCells by calling from_dict on the json representation
        table_body_cells_model = TableBodyCells.from_dict(table_body_cells_model_json)
        assert table_body_cells_model != False

        # Construct a model instance of TableBodyCells by calling from_dict on the json representation
        table_body_cells_model_dict = TableBodyCells.from_dict(table_body_cells_model_json).__dict__
        table_body_cells_model2 = TableBodyCells(**table_body_cells_model_dict)

        # Verify the model instances are equivalent
        assert table_body_cells_model == table_body_cells_model2

        # Convert model instance back to dict and verify no loss of data
        table_body_cells_model_json2 = table_body_cells_model.to_dict()
        assert table_body_cells_model_json2 == table_body_cells_model_json

class TestModel_TableCellKey():
    """
    Test Class for TableCellKey
    """

    def test_table_cell_key_serialization(self):
        """
        Test serialization/deserialization for TableCellKey
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableCellKey model
        table_cell_key_model_json = {}
        table_cell_key_model_json['cell_id'] = 'testString'
        table_cell_key_model_json['location'] = table_element_location_model
        table_cell_key_model_json['text'] = 'testString'

        # Construct a model instance of TableCellKey by calling from_dict on the json representation
        table_cell_key_model = TableCellKey.from_dict(table_cell_key_model_json)
        assert table_cell_key_model != False

        # Construct a model instance of TableCellKey by calling from_dict on the json representation
        table_cell_key_model_dict = TableCellKey.from_dict(table_cell_key_model_json).__dict__
        table_cell_key_model2 = TableCellKey(**table_cell_key_model_dict)

        # Verify the model instances are equivalent
        assert table_cell_key_model == table_cell_key_model2

        # Convert model instance back to dict and verify no loss of data
        table_cell_key_model_json2 = table_cell_key_model.to_dict()
        assert table_cell_key_model_json2 == table_cell_key_model_json

class TestModel_TableCellValues():
    """
    Test Class for TableCellValues
    """

    def test_table_cell_values_serialization(self):
        """
        Test serialization/deserialization for TableCellValues
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableCellValues model
        table_cell_values_model_json = {}
        table_cell_values_model_json['cell_id'] = 'testString'
        table_cell_values_model_json['location'] = table_element_location_model
        table_cell_values_model_json['text'] = 'testString'

        # Construct a model instance of TableCellValues by calling from_dict on the json representation
        table_cell_values_model = TableCellValues.from_dict(table_cell_values_model_json)
        assert table_cell_values_model != False

        # Construct a model instance of TableCellValues by calling from_dict on the json representation
        table_cell_values_model_dict = TableCellValues.from_dict(table_cell_values_model_json).__dict__
        table_cell_values_model2 = TableCellValues(**table_cell_values_model_dict)

        # Verify the model instances are equivalent
        assert table_cell_values_model == table_cell_values_model2

        # Convert model instance back to dict and verify no loss of data
        table_cell_values_model_json2 = table_cell_values_model.to_dict()
        assert table_cell_values_model_json2 == table_cell_values_model_json

class TestModel_TableColumnHeaderIds():
    """
    Test Class for TableColumnHeaderIds
    """

    def test_table_column_header_ids_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaderIds
        """

        # Construct a json representation of a TableColumnHeaderIds model
        table_column_header_ids_model_json = {}
        table_column_header_ids_model_json['id'] = 'testString'

        # Construct a model instance of TableColumnHeaderIds by calling from_dict on the json representation
        table_column_header_ids_model = TableColumnHeaderIds.from_dict(table_column_header_ids_model_json)
        assert table_column_header_ids_model != False

        # Construct a model instance of TableColumnHeaderIds by calling from_dict on the json representation
        table_column_header_ids_model_dict = TableColumnHeaderIds.from_dict(table_column_header_ids_model_json).__dict__
        table_column_header_ids_model2 = TableColumnHeaderIds(**table_column_header_ids_model_dict)

        # Verify the model instances are equivalent
        assert table_column_header_ids_model == table_column_header_ids_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_header_ids_model_json2 = table_column_header_ids_model.to_dict()
        assert table_column_header_ids_model_json2 == table_column_header_ids_model_json

class TestModel_TableColumnHeaderTexts():
    """
    Test Class for TableColumnHeaderTexts
    """

    def test_table_column_header_texts_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaderTexts
        """

        # Construct a json representation of a TableColumnHeaderTexts model
        table_column_header_texts_model_json = {}
        table_column_header_texts_model_json['text'] = 'testString'

        # Construct a model instance of TableColumnHeaderTexts by calling from_dict on the json representation
        table_column_header_texts_model = TableColumnHeaderTexts.from_dict(table_column_header_texts_model_json)
        assert table_column_header_texts_model != False

        # Construct a model instance of TableColumnHeaderTexts by calling from_dict on the json representation
        table_column_header_texts_model_dict = TableColumnHeaderTexts.from_dict(table_column_header_texts_model_json).__dict__
        table_column_header_texts_model2 = TableColumnHeaderTexts(**table_column_header_texts_model_dict)

        # Verify the model instances are equivalent
        assert table_column_header_texts_model == table_column_header_texts_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_header_texts_model_json2 = table_column_header_texts_model.to_dict()
        assert table_column_header_texts_model_json2 == table_column_header_texts_model_json

class TestModel_TableColumnHeaderTextsNormalized():
    """
    Test Class for TableColumnHeaderTextsNormalized
    """

    def test_table_column_header_texts_normalized_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaderTextsNormalized
        """

        # Construct a json representation of a TableColumnHeaderTextsNormalized model
        table_column_header_texts_normalized_model_json = {}
        table_column_header_texts_normalized_model_json['text_normalized'] = 'testString'

        # Construct a model instance of TableColumnHeaderTextsNormalized by calling from_dict on the json representation
        table_column_header_texts_normalized_model = TableColumnHeaderTextsNormalized.from_dict(table_column_header_texts_normalized_model_json)
        assert table_column_header_texts_normalized_model != False

        # Construct a model instance of TableColumnHeaderTextsNormalized by calling from_dict on the json representation
        table_column_header_texts_normalized_model_dict = TableColumnHeaderTextsNormalized.from_dict(table_column_header_texts_normalized_model_json).__dict__
        table_column_header_texts_normalized_model2 = TableColumnHeaderTextsNormalized(**table_column_header_texts_normalized_model_dict)

        # Verify the model instances are equivalent
        assert table_column_header_texts_normalized_model == table_column_header_texts_normalized_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_header_texts_normalized_model_json2 = table_column_header_texts_normalized_model.to_dict()
        assert table_column_header_texts_normalized_model_json2 == table_column_header_texts_normalized_model_json

class TestModel_TableColumnHeaders():
    """
    Test Class for TableColumnHeaders
    """

    def test_table_column_headers_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaders
        """

        # Construct a json representation of a TableColumnHeaders model
        table_column_headers_model_json = {}
        table_column_headers_model_json['cell_id'] = 'testString'
        table_column_headers_model_json['location'] = { 'foo': 'bar' }
        table_column_headers_model_json['text'] = 'testString'
        table_column_headers_model_json['text_normalized'] = 'testString'
        table_column_headers_model_json['row_index_begin'] = 26
        table_column_headers_model_json['row_index_end'] = 26
        table_column_headers_model_json['column_index_begin'] = 26
        table_column_headers_model_json['column_index_end'] = 26

        # Construct a model instance of TableColumnHeaders by calling from_dict on the json representation
        table_column_headers_model = TableColumnHeaders.from_dict(table_column_headers_model_json)
        assert table_column_headers_model != False

        # Construct a model instance of TableColumnHeaders by calling from_dict on the json representation
        table_column_headers_model_dict = TableColumnHeaders.from_dict(table_column_headers_model_json).__dict__
        table_column_headers_model2 = TableColumnHeaders(**table_column_headers_model_dict)

        # Verify the model instances are equivalent
        assert table_column_headers_model == table_column_headers_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_headers_model_json2 = table_column_headers_model.to_dict()
        assert table_column_headers_model_json2 == table_column_headers_model_json

class TestModel_TableElementLocation():
    """
    Test Class for TableElementLocation
    """

    def test_table_element_location_serialization(self):
        """
        Test serialization/deserialization for TableElementLocation
        """

        # Construct a json representation of a TableElementLocation model
        table_element_location_model_json = {}
        table_element_location_model_json['begin'] = 26
        table_element_location_model_json['end'] = 26

        # Construct a model instance of TableElementLocation by calling from_dict on the json representation
        table_element_location_model = TableElementLocation.from_dict(table_element_location_model_json)
        assert table_element_location_model != False

        # Construct a model instance of TableElementLocation by calling from_dict on the json representation
        table_element_location_model_dict = TableElementLocation.from_dict(table_element_location_model_json).__dict__
        table_element_location_model2 = TableElementLocation(**table_element_location_model_dict)

        # Verify the model instances are equivalent
        assert table_element_location_model == table_element_location_model2

        # Convert model instance back to dict and verify no loss of data
        table_element_location_model_json2 = table_element_location_model.to_dict()
        assert table_element_location_model_json2 == table_element_location_model_json

class TestModel_TableHeaders():
    """
    Test Class for TableHeaders
    """

    def test_table_headers_serialization(self):
        """
        Test serialization/deserialization for TableHeaders
        """

        # Construct a json representation of a TableHeaders model
        table_headers_model_json = {}
        table_headers_model_json['cell_id'] = 'testString'
        table_headers_model_json['location'] = { 'foo': 'bar' }
        table_headers_model_json['text'] = 'testString'
        table_headers_model_json['row_index_begin'] = 26
        table_headers_model_json['row_index_end'] = 26
        table_headers_model_json['column_index_begin'] = 26
        table_headers_model_json['column_index_end'] = 26

        # Construct a model instance of TableHeaders by calling from_dict on the json representation
        table_headers_model = TableHeaders.from_dict(table_headers_model_json)
        assert table_headers_model != False

        # Construct a model instance of TableHeaders by calling from_dict on the json representation
        table_headers_model_dict = TableHeaders.from_dict(table_headers_model_json).__dict__
        table_headers_model2 = TableHeaders(**table_headers_model_dict)

        # Verify the model instances are equivalent
        assert table_headers_model == table_headers_model2

        # Convert model instance back to dict and verify no loss of data
        table_headers_model_json2 = table_headers_model.to_dict()
        assert table_headers_model_json2 == table_headers_model_json

class TestModel_TableKeyValuePairs():
    """
    Test Class for TableKeyValuePairs
    """

    def test_table_key_value_pairs_serialization(self):
        """
        Test serialization/deserialization for TableKeyValuePairs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        # Construct a json representation of a TableKeyValuePairs model
        table_key_value_pairs_model_json = {}
        table_key_value_pairs_model_json['key'] = table_cell_key_model
        table_key_value_pairs_model_json['value'] = [table_cell_values_model]

        # Construct a model instance of TableKeyValuePairs by calling from_dict on the json representation
        table_key_value_pairs_model = TableKeyValuePairs.from_dict(table_key_value_pairs_model_json)
        assert table_key_value_pairs_model != False

        # Construct a model instance of TableKeyValuePairs by calling from_dict on the json representation
        table_key_value_pairs_model_dict = TableKeyValuePairs.from_dict(table_key_value_pairs_model_json).__dict__
        table_key_value_pairs_model2 = TableKeyValuePairs(**table_key_value_pairs_model_dict)

        # Verify the model instances are equivalent
        assert table_key_value_pairs_model == table_key_value_pairs_model2

        # Convert model instance back to dict and verify no loss of data
        table_key_value_pairs_model_json2 = table_key_value_pairs_model.to_dict()
        assert table_key_value_pairs_model_json2 == table_key_value_pairs_model_json

class TestModel_TableResultTable():
    """
    Test Class for TableResultTable
    """

    def test_table_result_table_serialization(self):
        """
        Test serialization/deserialization for TableResultTable
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_text_location_model = {} # TableTextLocation
        table_text_location_model['text'] = 'testString'
        table_text_location_model['location'] = table_element_location_model

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = { 'foo': 'bar' }
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        table_row_headers_model = {} # TableRowHeaders
        table_row_headers_model['cell_id'] = 'testString'
        table_row_headers_model['location'] = table_element_location_model
        table_row_headers_model['text'] = 'testString'
        table_row_headers_model['text_normalized'] = 'testString'
        table_row_headers_model['row_index_begin'] = 26
        table_row_headers_model['row_index_end'] = 26
        table_row_headers_model['column_index_begin'] = 26
        table_row_headers_model['column_index_end'] = 26

        table_column_headers_model = {} # TableColumnHeaders
        table_column_headers_model['cell_id'] = 'testString'
        table_column_headers_model['location'] = { 'foo': 'bar' }
        table_column_headers_model['text'] = 'testString'
        table_column_headers_model['text_normalized'] = 'testString'
        table_column_headers_model['row_index_begin'] = 26
        table_column_headers_model['row_index_end'] = 26
        table_column_headers_model['column_index_begin'] = 26
        table_column_headers_model['column_index_end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        table_key_value_pairs_model = {} # TableKeyValuePairs
        table_key_value_pairs_model['key'] = table_cell_key_model
        table_key_value_pairs_model['value'] = [table_cell_values_model]

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        table_body_cells_model = {} # TableBodyCells
        table_body_cells_model['cell_id'] = 'testString'
        table_body_cells_model['location'] = table_element_location_model
        table_body_cells_model['text'] = 'testString'
        table_body_cells_model['row_index_begin'] = 26
        table_body_cells_model['row_index_end'] = 26
        table_body_cells_model['column_index_begin'] = 26
        table_body_cells_model['column_index_end'] = 26
        table_body_cells_model['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model['attributes'] = [document_attribute_model]

        # Construct a json representation of a TableResultTable model
        table_result_table_model_json = {}
        table_result_table_model_json['location'] = table_element_location_model
        table_result_table_model_json['text'] = 'testString'
        table_result_table_model_json['section_title'] = table_text_location_model
        table_result_table_model_json['title'] = table_text_location_model
        table_result_table_model_json['table_headers'] = [table_headers_model]
        table_result_table_model_json['row_headers'] = [table_row_headers_model]
        table_result_table_model_json['column_headers'] = [table_column_headers_model]
        table_result_table_model_json['key_value_pairs'] = [table_key_value_pairs_model]
        table_result_table_model_json['body_cells'] = [table_body_cells_model]
        table_result_table_model_json['contexts'] = [table_text_location_model]

        # Construct a model instance of TableResultTable by calling from_dict on the json representation
        table_result_table_model = TableResultTable.from_dict(table_result_table_model_json)
        assert table_result_table_model != False

        # Construct a model instance of TableResultTable by calling from_dict on the json representation
        table_result_table_model_dict = TableResultTable.from_dict(table_result_table_model_json).__dict__
        table_result_table_model2 = TableResultTable(**table_result_table_model_dict)

        # Verify the model instances are equivalent
        assert table_result_table_model == table_result_table_model2

        # Convert model instance back to dict and verify no loss of data
        table_result_table_model_json2 = table_result_table_model.to_dict()
        assert table_result_table_model_json2 == table_result_table_model_json

class TestModel_TableRowHeaderIds():
    """
    Test Class for TableRowHeaderIds
    """

    def test_table_row_header_ids_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaderIds
        """

        # Construct a json representation of a TableRowHeaderIds model
        table_row_header_ids_model_json = {}
        table_row_header_ids_model_json['id'] = 'testString'

        # Construct a model instance of TableRowHeaderIds by calling from_dict on the json representation
        table_row_header_ids_model = TableRowHeaderIds.from_dict(table_row_header_ids_model_json)
        assert table_row_header_ids_model != False

        # Construct a model instance of TableRowHeaderIds by calling from_dict on the json representation
        table_row_header_ids_model_dict = TableRowHeaderIds.from_dict(table_row_header_ids_model_json).__dict__
        table_row_header_ids_model2 = TableRowHeaderIds(**table_row_header_ids_model_dict)

        # Verify the model instances are equivalent
        assert table_row_header_ids_model == table_row_header_ids_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_header_ids_model_json2 = table_row_header_ids_model.to_dict()
        assert table_row_header_ids_model_json2 == table_row_header_ids_model_json

class TestModel_TableRowHeaderTexts():
    """
    Test Class for TableRowHeaderTexts
    """

    def test_table_row_header_texts_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaderTexts
        """

        # Construct a json representation of a TableRowHeaderTexts model
        table_row_header_texts_model_json = {}
        table_row_header_texts_model_json['text'] = 'testString'

        # Construct a model instance of TableRowHeaderTexts by calling from_dict on the json representation
        table_row_header_texts_model = TableRowHeaderTexts.from_dict(table_row_header_texts_model_json)
        assert table_row_header_texts_model != False

        # Construct a model instance of TableRowHeaderTexts by calling from_dict on the json representation
        table_row_header_texts_model_dict = TableRowHeaderTexts.from_dict(table_row_header_texts_model_json).__dict__
        table_row_header_texts_model2 = TableRowHeaderTexts(**table_row_header_texts_model_dict)

        # Verify the model instances are equivalent
        assert table_row_header_texts_model == table_row_header_texts_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_header_texts_model_json2 = table_row_header_texts_model.to_dict()
        assert table_row_header_texts_model_json2 == table_row_header_texts_model_json

class TestModel_TableRowHeaderTextsNormalized():
    """
    Test Class for TableRowHeaderTextsNormalized
    """

    def test_table_row_header_texts_normalized_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaderTextsNormalized
        """

        # Construct a json representation of a TableRowHeaderTextsNormalized model
        table_row_header_texts_normalized_model_json = {}
        table_row_header_texts_normalized_model_json['text_normalized'] = 'testString'

        # Construct a model instance of TableRowHeaderTextsNormalized by calling from_dict on the json representation
        table_row_header_texts_normalized_model = TableRowHeaderTextsNormalized.from_dict(table_row_header_texts_normalized_model_json)
        assert table_row_header_texts_normalized_model != False

        # Construct a model instance of TableRowHeaderTextsNormalized by calling from_dict on the json representation
        table_row_header_texts_normalized_model_dict = TableRowHeaderTextsNormalized.from_dict(table_row_header_texts_normalized_model_json).__dict__
        table_row_header_texts_normalized_model2 = TableRowHeaderTextsNormalized(**table_row_header_texts_normalized_model_dict)

        # Verify the model instances are equivalent
        assert table_row_header_texts_normalized_model == table_row_header_texts_normalized_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_header_texts_normalized_model_json2 = table_row_header_texts_normalized_model.to_dict()
        assert table_row_header_texts_normalized_model_json2 == table_row_header_texts_normalized_model_json

class TestModel_TableRowHeaders():
    """
    Test Class for TableRowHeaders
    """

    def test_table_row_headers_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaders
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableRowHeaders model
        table_row_headers_model_json = {}
        table_row_headers_model_json['cell_id'] = 'testString'
        table_row_headers_model_json['location'] = table_element_location_model
        table_row_headers_model_json['text'] = 'testString'
        table_row_headers_model_json['text_normalized'] = 'testString'
        table_row_headers_model_json['row_index_begin'] = 26
        table_row_headers_model_json['row_index_end'] = 26
        table_row_headers_model_json['column_index_begin'] = 26
        table_row_headers_model_json['column_index_end'] = 26

        # Construct a model instance of TableRowHeaders by calling from_dict on the json representation
        table_row_headers_model = TableRowHeaders.from_dict(table_row_headers_model_json)
        assert table_row_headers_model != False

        # Construct a model instance of TableRowHeaders by calling from_dict on the json representation
        table_row_headers_model_dict = TableRowHeaders.from_dict(table_row_headers_model_json).__dict__
        table_row_headers_model2 = TableRowHeaders(**table_row_headers_model_dict)

        # Verify the model instances are equivalent
        assert table_row_headers_model == table_row_headers_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_headers_model_json2 = table_row_headers_model.to_dict()
        assert table_row_headers_model_json2 == table_row_headers_model_json

class TestModel_TableTextLocation():
    """
    Test Class for TableTextLocation
    """

    def test_table_text_location_serialization(self):
        """
        Test serialization/deserialization for TableTextLocation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableTextLocation model
        table_text_location_model_json = {}
        table_text_location_model_json['text'] = 'testString'
        table_text_location_model_json['location'] = table_element_location_model

        # Construct a model instance of TableTextLocation by calling from_dict on the json representation
        table_text_location_model = TableTextLocation.from_dict(table_text_location_model_json)
        assert table_text_location_model != False

        # Construct a model instance of TableTextLocation by calling from_dict on the json representation
        table_text_location_model_dict = TableTextLocation.from_dict(table_text_location_model_json).__dict__
        table_text_location_model2 = TableTextLocation(**table_text_location_model_dict)

        # Verify the model instances are equivalent
        assert table_text_location_model == table_text_location_model2

        # Convert model instance back to dict and verify no loss of data
        table_text_location_model_json2 = table_text_location_model.to_dict()
        assert table_text_location_model_json2 == table_text_location_model_json

class TestModel_TrainingExample():
    """
    Test Class for TrainingExample
    """

    def test_training_example_serialization(self):
        """
        Test serialization/deserialization for TrainingExample
        """

        # Construct a json representation of a TrainingExample model
        training_example_model_json = {}
        training_example_model_json['document_id'] = 'testString'
        training_example_model_json['collection_id'] = 'testString'
        training_example_model_json['relevance'] = 38
        training_example_model_json['created'] = "2019-01-01T12:00:00Z"
        training_example_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of TrainingExample by calling from_dict on the json representation
        training_example_model = TrainingExample.from_dict(training_example_model_json)
        assert training_example_model != False

        # Construct a model instance of TrainingExample by calling from_dict on the json representation
        training_example_model_dict = TrainingExample.from_dict(training_example_model_json).__dict__
        training_example_model2 = TrainingExample(**training_example_model_dict)

        # Verify the model instances are equivalent
        assert training_example_model == training_example_model2

        # Convert model instance back to dict and verify no loss of data
        training_example_model_json2 = training_example_model.to_dict()
        assert training_example_model_json2 == training_example_model_json

class TestModel_TrainingQuery():
    """
    Test Class for TrainingQuery
    """

    def test_training_query_serialization(self):
        """
        Test serialization/deserialization for TrainingQuery
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_example_model = {} # TrainingExample
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38
        training_example_model['created'] = "2019-01-01T12:00:00Z"
        training_example_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a TrainingQuery model
        training_query_model_json = {}
        training_query_model_json['query_id'] = 'testString'
        training_query_model_json['natural_language_query'] = 'testString'
        training_query_model_json['filter'] = 'testString'
        training_query_model_json['created'] = "2019-01-01T12:00:00Z"
        training_query_model_json['updated'] = "2019-01-01T12:00:00Z"
        training_query_model_json['examples'] = [training_example_model]

        # Construct a model instance of TrainingQuery by calling from_dict on the json representation
        training_query_model = TrainingQuery.from_dict(training_query_model_json)
        assert training_query_model != False

        # Construct a model instance of TrainingQuery by calling from_dict on the json representation
        training_query_model_dict = TrainingQuery.from_dict(training_query_model_json).__dict__
        training_query_model2 = TrainingQuery(**training_query_model_dict)

        # Verify the model instances are equivalent
        assert training_query_model == training_query_model2

        # Convert model instance back to dict and verify no loss of data
        training_query_model_json2 = training_query_model.to_dict()
        assert training_query_model_json2 == training_query_model_json

class TestModel_TrainingQuerySet():
    """
    Test Class for TrainingQuerySet
    """

    def test_training_query_set_serialization(self):
        """
        Test serialization/deserialization for TrainingQuerySet
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_example_model = {} # TrainingExample
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38
        training_example_model['created'] = "2019-01-01T12:00:00Z"
        training_example_model['updated'] = "2019-01-01T12:00:00Z"

        training_query_model = {} # TrainingQuery
        training_query_model['query_id'] = 'testString'
        training_query_model['natural_language_query'] = 'testString'
        training_query_model['filter'] = 'testString'
        training_query_model['created'] = "2019-01-01T12:00:00Z"
        training_query_model['updated'] = "2019-01-01T12:00:00Z"
        training_query_model['examples'] = [training_example_model]

        # Construct a json representation of a TrainingQuerySet model
        training_query_set_model_json = {}
        training_query_set_model_json['queries'] = [training_query_model]

        # Construct a model instance of TrainingQuerySet by calling from_dict on the json representation
        training_query_set_model = TrainingQuerySet.from_dict(training_query_set_model_json)
        assert training_query_set_model != False

        # Construct a model instance of TrainingQuerySet by calling from_dict on the json representation
        training_query_set_model_dict = TrainingQuerySet.from_dict(training_query_set_model_json).__dict__
        training_query_set_model2 = TrainingQuerySet(**training_query_set_model_dict)

        # Verify the model instances are equivalent
        assert training_query_set_model == training_query_set_model2

        # Convert model instance back to dict and verify no loss of data
        training_query_set_model_json2 = training_query_set_model.to_dict()
        assert training_query_set_model_json2 == training_query_set_model_json

class TestModel_QueryCalculationAggregation():
    """
    Test Class for QueryCalculationAggregation
    """

    def test_query_calculation_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryCalculationAggregation
        """

        # Construct a json representation of a QueryCalculationAggregation model
        query_calculation_aggregation_model_json = {}
        query_calculation_aggregation_model_json['type'] = 'unique_count'
        query_calculation_aggregation_model_json['field'] = 'testString'
        query_calculation_aggregation_model_json['value'] = 72.5

        # Construct a model instance of QueryCalculationAggregation by calling from_dict on the json representation
        query_calculation_aggregation_model = QueryCalculationAggregation.from_dict(query_calculation_aggregation_model_json)
        assert query_calculation_aggregation_model != False

        # Construct a model instance of QueryCalculationAggregation by calling from_dict on the json representation
        query_calculation_aggregation_model_dict = QueryCalculationAggregation.from_dict(query_calculation_aggregation_model_json).__dict__
        query_calculation_aggregation_model2 = QueryCalculationAggregation(**query_calculation_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_calculation_aggregation_model == query_calculation_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_calculation_aggregation_model_json2 = query_calculation_aggregation_model.to_dict()
        assert query_calculation_aggregation_model_json2 == query_calculation_aggregation_model_json

class TestModel_QueryFilterAggregation():
    """
    Test Class for QueryFilterAggregation
    """

    def test_query_filter_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryFilterAggregation
        """

        # Construct a json representation of a QueryFilterAggregation model
        query_filter_aggregation_model_json = {}
        query_filter_aggregation_model_json['type'] = 'filter'
        query_filter_aggregation_model_json['match'] = 'testString'
        query_filter_aggregation_model_json['matching_results'] = 26

        # Construct a model instance of QueryFilterAggregation by calling from_dict on the json representation
        query_filter_aggregation_model = QueryFilterAggregation.from_dict(query_filter_aggregation_model_json)
        assert query_filter_aggregation_model != False

        # Construct a model instance of QueryFilterAggregation by calling from_dict on the json representation
        query_filter_aggregation_model_dict = QueryFilterAggregation.from_dict(query_filter_aggregation_model_json).__dict__
        query_filter_aggregation_model2 = QueryFilterAggregation(**query_filter_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_filter_aggregation_model == query_filter_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_filter_aggregation_model_json2 = query_filter_aggregation_model.to_dict()
        assert query_filter_aggregation_model_json2 == query_filter_aggregation_model_json

class TestModel_QueryGroupByAggregation():
    """
    Test Class for QueryGroupByAggregation
    """

    def test_query_group_by_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryGroupByAggregation
        """

        # Construct a json representation of a QueryGroupByAggregation model
        query_group_by_aggregation_model_json = {}
        query_group_by_aggregation_model_json['type'] = 'group_by'

        # Construct a model instance of QueryGroupByAggregation by calling from_dict on the json representation
        query_group_by_aggregation_model = QueryGroupByAggregation.from_dict(query_group_by_aggregation_model_json)
        assert query_group_by_aggregation_model != False

        # Construct a model instance of QueryGroupByAggregation by calling from_dict on the json representation
        query_group_by_aggregation_model_dict = QueryGroupByAggregation.from_dict(query_group_by_aggregation_model_json).__dict__
        query_group_by_aggregation_model2 = QueryGroupByAggregation(**query_group_by_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_group_by_aggregation_model == query_group_by_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_group_by_aggregation_model_json2 = query_group_by_aggregation_model.to_dict()
        assert query_group_by_aggregation_model_json2 == query_group_by_aggregation_model_json

class TestModel_QueryHistogramAggregation():
    """
    Test Class for QueryHistogramAggregation
    """

    def test_query_histogram_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryHistogramAggregation
        """

        # Construct a json representation of a QueryHistogramAggregation model
        query_histogram_aggregation_model_json = {}
        query_histogram_aggregation_model_json['type'] = 'histogram'
        query_histogram_aggregation_model_json['field'] = 'testString'
        query_histogram_aggregation_model_json['interval'] = 38
        query_histogram_aggregation_model_json['name'] = 'testString'

        # Construct a model instance of QueryHistogramAggregation by calling from_dict on the json representation
        query_histogram_aggregation_model = QueryHistogramAggregation.from_dict(query_histogram_aggregation_model_json)
        assert query_histogram_aggregation_model != False

        # Construct a model instance of QueryHistogramAggregation by calling from_dict on the json representation
        query_histogram_aggregation_model_dict = QueryHistogramAggregation.from_dict(query_histogram_aggregation_model_json).__dict__
        query_histogram_aggregation_model2 = QueryHistogramAggregation(**query_histogram_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_histogram_aggregation_model == query_histogram_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_histogram_aggregation_model_json2 = query_histogram_aggregation_model.to_dict()
        assert query_histogram_aggregation_model_json2 == query_histogram_aggregation_model_json

class TestModel_QueryNestedAggregation():
    """
    Test Class for QueryNestedAggregation
    """

    def test_query_nested_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryNestedAggregation
        """

        # Construct a json representation of a QueryNestedAggregation model
        query_nested_aggregation_model_json = {}
        query_nested_aggregation_model_json['type'] = 'nested'
        query_nested_aggregation_model_json['path'] = 'testString'
        query_nested_aggregation_model_json['matching_results'] = 26

        # Construct a model instance of QueryNestedAggregation by calling from_dict on the json representation
        query_nested_aggregation_model = QueryNestedAggregation.from_dict(query_nested_aggregation_model_json)
        assert query_nested_aggregation_model != False

        # Construct a model instance of QueryNestedAggregation by calling from_dict on the json representation
        query_nested_aggregation_model_dict = QueryNestedAggregation.from_dict(query_nested_aggregation_model_json).__dict__
        query_nested_aggregation_model2 = QueryNestedAggregation(**query_nested_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_nested_aggregation_model == query_nested_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_nested_aggregation_model_json2 = query_nested_aggregation_model.to_dict()
        assert query_nested_aggregation_model_json2 == query_nested_aggregation_model_json

class TestModel_QueryTermAggregation():
    """
    Test Class for QueryTermAggregation
    """

    def test_query_term_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryTermAggregation
        """

        # Construct a json representation of a QueryTermAggregation model
        query_term_aggregation_model_json = {}
        query_term_aggregation_model_json['type'] = 'term'
        query_term_aggregation_model_json['field'] = 'testString'
        query_term_aggregation_model_json['count'] = 38
        query_term_aggregation_model_json['name'] = 'testString'

        # Construct a model instance of QueryTermAggregation by calling from_dict on the json representation
        query_term_aggregation_model = QueryTermAggregation.from_dict(query_term_aggregation_model_json)
        assert query_term_aggregation_model != False

        # Construct a model instance of QueryTermAggregation by calling from_dict on the json representation
        query_term_aggregation_model_dict = QueryTermAggregation.from_dict(query_term_aggregation_model_json).__dict__
        query_term_aggregation_model2 = QueryTermAggregation(**query_term_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_term_aggregation_model == query_term_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_term_aggregation_model_json2 = query_term_aggregation_model.to_dict()
        assert query_term_aggregation_model_json2 == query_term_aggregation_model_json

class TestModel_QueryTimesliceAggregation():
    """
    Test Class for QueryTimesliceAggregation
    """

    def test_query_timeslice_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryTimesliceAggregation
        """

        # Construct a json representation of a QueryTimesliceAggregation model
        query_timeslice_aggregation_model_json = {}
        query_timeslice_aggregation_model_json['type'] = 'timeslice'
        query_timeslice_aggregation_model_json['field'] = 'testString'
        query_timeslice_aggregation_model_json['interval'] = 'testString'
        query_timeslice_aggregation_model_json['name'] = 'testString'

        # Construct a model instance of QueryTimesliceAggregation by calling from_dict on the json representation
        query_timeslice_aggregation_model = QueryTimesliceAggregation.from_dict(query_timeslice_aggregation_model_json)
        assert query_timeslice_aggregation_model != False

        # Construct a model instance of QueryTimesliceAggregation by calling from_dict on the json representation
        query_timeslice_aggregation_model_dict = QueryTimesliceAggregation.from_dict(query_timeslice_aggregation_model_json).__dict__
        query_timeslice_aggregation_model2 = QueryTimesliceAggregation(**query_timeslice_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_timeslice_aggregation_model == query_timeslice_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_timeslice_aggregation_model_json2 = query_timeslice_aggregation_model.to_dict()
        assert query_timeslice_aggregation_model_json2 == query_timeslice_aggregation_model_json

class TestModel_QueryTopHitsAggregation():
    """
    Test Class for QueryTopHitsAggregation
    """

    def test_query_top_hits_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryTopHitsAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_top_hits_aggregation_result_model = {} # QueryTopHitsAggregationResult
        query_top_hits_aggregation_result_model['matching_results'] = 38
        query_top_hits_aggregation_result_model['hits'] = [{}]

        # Construct a json representation of a QueryTopHitsAggregation model
        query_top_hits_aggregation_model_json = {}
        query_top_hits_aggregation_model_json['type'] = 'top_hits'
        query_top_hits_aggregation_model_json['size'] = 38
        query_top_hits_aggregation_model_json['name'] = 'testString'
        query_top_hits_aggregation_model_json['hits'] = query_top_hits_aggregation_result_model

        # Construct a model instance of QueryTopHitsAggregation by calling from_dict on the json representation
        query_top_hits_aggregation_model = QueryTopHitsAggregation.from_dict(query_top_hits_aggregation_model_json)
        assert query_top_hits_aggregation_model != False

        # Construct a model instance of QueryTopHitsAggregation by calling from_dict on the json representation
        query_top_hits_aggregation_model_dict = QueryTopHitsAggregation.from_dict(query_top_hits_aggregation_model_json).__dict__
        query_top_hits_aggregation_model2 = QueryTopHitsAggregation(**query_top_hits_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_top_hits_aggregation_model == query_top_hits_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_top_hits_aggregation_model_json2 = query_top_hits_aggregation_model.to_dict()
        assert query_top_hits_aggregation_model_json2 == query_top_hits_aggregation_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
