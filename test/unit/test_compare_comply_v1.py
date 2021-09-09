# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2018, 2021.
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
Unit Tests for CompareComplyV1
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
from ibm_watson.compare_comply_v1 import *

version = 'testString'

_service = CompareComplyV1(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.compare-comply.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: HTMLConversion
##############################################################################
# region

class TestConvertToHtml():
    """
    Test Class for convert_to_html
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
    def test_convert_to_html_all_params(self):
        """
        convert_to_html()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/html_conversion')
        mock_response = '{"num_pages": "num_pages", "author": "author", "publication_date": "publication_date", "title": "title", "html": "html"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()
        file_content_type = 'application/pdf'
        model = 'contracts'

        # Invoke method
        response = _service.convert_to_html(
            file,
            file_content_type=file_content_type,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_convert_to_html_required_params(self):
        """
        test_convert_to_html_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/html_conversion')
        mock_response = '{"num_pages": "num_pages", "author": "author", "publication_date": "publication_date", "title": "title", "html": "html"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.convert_to_html(
            file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_convert_to_html_value_error(self):
        """
        test_convert_to_html_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/html_conversion')
        mock_response = '{"num_pages": "num_pages", "author": "author", "publication_date": "publication_date", "title": "title", "html": "html"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "file": file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.convert_to_html(**req_copy)



# endregion
##############################################################################
# End of Service: HTMLConversion
##############################################################################

##############################################################################
# Start of Service: ElementClassification
##############################################################################
# region

class TestClassifyElements():
    """
    Test Class for classify_elements
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
    def test_classify_elements_all_params(self):
        """
        classify_elements()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/element_classification')
        mock_response = '{"document": {"title": "title", "html": "html", "hash": "hash", "label": "label"}, "model_id": "model_id", "model_version": "model_version", "elements": [{"location": {"begin": 5, "end": 3}, "text": "text", "types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "effective_dates": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_amounts": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "termination_dates": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_types": [{"confidence_level": "High", "text": "text", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_terms": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "payment_terms": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_currencies": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "tables": [{"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"location": {"begin": 5, "end": 3}, "text": "text"}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": ["row_header_ids"], "row_header_texts": ["row_header_texts"], "row_header_texts_normalized": ["row_header_texts_normalized"], "column_header_ids": ["column_header_ids"], "column_header_texts": ["column_header_texts"], "column_header_texts_normalized": ["column_header_texts_normalized"], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}]}], "document_structure": {"section_titles": [{"text": "text", "location": {"begin": 5, "end": 3}, "level": 5, "element_locations": [{"begin": 5, "end": 3}]}], "leading_sentences": [{"text": "text", "location": {"begin": 5, "end": 3}, "element_locations": [{"begin": 5, "end": 3}]}], "paragraphs": [{"location": {"begin": 5, "end": 3}}]}, "parties": [{"party": "party", "role": "role", "importance": "Primary", "addresses": [{"text": "text", "location": {"begin": 5, "end": 3}}], "contacts": [{"name": "name", "role": "role"}], "mentions": [{"text": "text", "location": {"begin": 5, "end": 3}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()
        file_content_type = 'application/pdf'
        model = 'contracts'

        # Invoke method
        response = _service.classify_elements(
            file,
            file_content_type=file_content_type,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_classify_elements_required_params(self):
        """
        test_classify_elements_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/element_classification')
        mock_response = '{"document": {"title": "title", "html": "html", "hash": "hash", "label": "label"}, "model_id": "model_id", "model_version": "model_version", "elements": [{"location": {"begin": 5, "end": 3}, "text": "text", "types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "effective_dates": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_amounts": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "termination_dates": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_types": [{"confidence_level": "High", "text": "text", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_terms": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "payment_terms": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_currencies": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "tables": [{"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"location": {"begin": 5, "end": 3}, "text": "text"}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": ["row_header_ids"], "row_header_texts": ["row_header_texts"], "row_header_texts_normalized": ["row_header_texts_normalized"], "column_header_ids": ["column_header_ids"], "column_header_texts": ["column_header_texts"], "column_header_texts_normalized": ["column_header_texts_normalized"], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}]}], "document_structure": {"section_titles": [{"text": "text", "location": {"begin": 5, "end": 3}, "level": 5, "element_locations": [{"begin": 5, "end": 3}]}], "leading_sentences": [{"text": "text", "location": {"begin": 5, "end": 3}, "element_locations": [{"begin": 5, "end": 3}]}], "paragraphs": [{"location": {"begin": 5, "end": 3}}]}, "parties": [{"party": "party", "role": "role", "importance": "Primary", "addresses": [{"text": "text", "location": {"begin": 5, "end": 3}}], "contacts": [{"name": "name", "role": "role"}], "mentions": [{"text": "text", "location": {"begin": 5, "end": 3}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.classify_elements(
            file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_classify_elements_value_error(self):
        """
        test_classify_elements_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/element_classification')
        mock_response = '{"document": {"title": "title", "html": "html", "hash": "hash", "label": "label"}, "model_id": "model_id", "model_version": "model_version", "elements": [{"location": {"begin": 5, "end": 3}, "text": "text", "types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "effective_dates": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_amounts": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "termination_dates": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_types": [{"confidence_level": "High", "text": "text", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_terms": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "payment_terms": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "interpretation": {"value": "value", "numeric_value": 13, "unit": "unit"}, "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "contract_currencies": [{"confidence_level": "High", "text": "text", "text_normalized": "text_normalized", "provenance_ids": ["provenance_ids"], "location": {"begin": 5, "end": 3}}], "tables": [{"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"location": {"begin": 5, "end": 3}, "text": "text"}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": ["row_header_ids"], "row_header_texts": ["row_header_texts"], "row_header_texts_normalized": ["row_header_texts_normalized"], "column_header_ids": ["column_header_ids"], "column_header_texts": ["column_header_texts"], "column_header_texts_normalized": ["column_header_texts_normalized"], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}]}], "document_structure": {"section_titles": [{"text": "text", "location": {"begin": 5, "end": 3}, "level": 5, "element_locations": [{"begin": 5, "end": 3}]}], "leading_sentences": [{"text": "text", "location": {"begin": 5, "end": 3}, "element_locations": [{"begin": 5, "end": 3}]}], "paragraphs": [{"location": {"begin": 5, "end": 3}}]}, "parties": [{"party": "party", "role": "role", "importance": "Primary", "addresses": [{"text": "text", "location": {"begin": 5, "end": 3}}], "contacts": [{"name": "name", "role": "role"}], "mentions": [{"text": "text", "location": {"begin": 5, "end": 3}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "file": file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.classify_elements(**req_copy)



# endregion
##############################################################################
# End of Service: ElementClassification
##############################################################################

##############################################################################
# Start of Service: Tables
##############################################################################
# region

class TestExtractTables():
    """
    Test Class for extract_tables
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
    def test_extract_tables_all_params(self):
        """
        extract_tables()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/tables')
        mock_response = '{"document": {"html": "html", "title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "tables": [{"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"location": {"begin": 5, "end": 3}, "text": "text"}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": ["row_header_ids"], "row_header_texts": ["row_header_texts"], "row_header_texts_normalized": ["row_header_texts_normalized"], "column_header_ids": ["column_header_ids"], "column_header_texts": ["column_header_texts"], "column_header_texts_normalized": ["column_header_texts_normalized"], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()
        file_content_type = 'application/pdf'
        model = 'contracts'

        # Invoke method
        response = _service.extract_tables(
            file,
            file_content_type=file_content_type,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_extract_tables_required_params(self):
        """
        test_extract_tables_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/tables')
        mock_response = '{"document": {"html": "html", "title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "tables": [{"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"location": {"begin": 5, "end": 3}, "text": "text"}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": ["row_header_ids"], "row_header_texts": ["row_header_texts"], "row_header_texts_normalized": ["row_header_texts_normalized"], "column_header_ids": ["column_header_ids"], "column_header_texts": ["column_header_texts"], "column_header_texts_normalized": ["column_header_texts_normalized"], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.extract_tables(
            file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_extract_tables_value_error(self):
        """
        test_extract_tables_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/tables')
        mock_response = '{"document": {"html": "html", "title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "tables": [{"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"location": {"begin": 5, "end": 3}, "text": "text"}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": ["row_header_ids"], "row_header_texts": ["row_header_texts"], "row_header_texts_normalized": ["row_header_texts_normalized"], "column_header_ids": ["column_header_ids"], "column_header_texts": ["column_header_texts"], "column_header_texts_normalized": ["column_header_texts_normalized"], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "file": file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.extract_tables(**req_copy)



# endregion
##############################################################################
# End of Service: Tables
##############################################################################

##############################################################################
# Start of Service: Comparison
##############################################################################
# region

class TestCompareDocuments():
    """
    Test Class for compare_documents
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
    def test_compare_documents_all_params(self):
        """
        compare_documents()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/comparison')
        mock_response = '{"model_id": "model_id", "model_version": "model_version", "documents": [{"title": "title", "html": "html", "hash": "hash", "label": "label"}], "aligned_elements": [{"element_pair": [{"document_label": "document_label", "text": "text", "location": {"begin": 5, "end": 3}, "types": [{"label": {"nature": "nature", "party": "party"}}], "categories": [{"label": "Amendments"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "identical_text": true, "provenance_ids": ["provenance_ids"], "significant_elements": true}], "unaligned_elements": [{"document_label": "document_label", "location": {"begin": 5, "end": 3}, "text": "text", "types": [{"label": {"nature": "nature", "party": "party"}}], "categories": [{"label": "Amendments"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file_1 = io.BytesIO(b'This is a mock file.').getvalue()
        file_2 = io.BytesIO(b'This is a mock file.').getvalue()
        file_1_content_type = 'application/pdf'
        file_2_content_type = 'application/pdf'
        file_1_label = 'file_1'
        file_2_label = 'file_2'
        model = 'contracts'

        # Invoke method
        response = _service.compare_documents(
            file_1,
            file_2,
            file_1_content_type=file_1_content_type,
            file_2_content_type=file_2_content_type,
            file_1_label=file_1_label,
            file_2_label=file_2_label,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'file_1_label={}'.format(file_1_label) in query_string
        assert 'file_2_label={}'.format(file_2_label) in query_string
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_compare_documents_required_params(self):
        """
        test_compare_documents_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/comparison')
        mock_response = '{"model_id": "model_id", "model_version": "model_version", "documents": [{"title": "title", "html": "html", "hash": "hash", "label": "label"}], "aligned_elements": [{"element_pair": [{"document_label": "document_label", "text": "text", "location": {"begin": 5, "end": 3}, "types": [{"label": {"nature": "nature", "party": "party"}}], "categories": [{"label": "Amendments"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "identical_text": true, "provenance_ids": ["provenance_ids"], "significant_elements": true}], "unaligned_elements": [{"document_label": "document_label", "location": {"begin": 5, "end": 3}, "text": "text", "types": [{"label": {"nature": "nature", "party": "party"}}], "categories": [{"label": "Amendments"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file_1 = io.BytesIO(b'This is a mock file.').getvalue()
        file_2 = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.compare_documents(
            file_1,
            file_2,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_compare_documents_value_error(self):
        """
        test_compare_documents_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/comparison')
        mock_response = '{"model_id": "model_id", "model_version": "model_version", "documents": [{"title": "title", "html": "html", "hash": "hash", "label": "label"}], "aligned_elements": [{"element_pair": [{"document_label": "document_label", "text": "text", "location": {"begin": 5, "end": 3}, "types": [{"label": {"nature": "nature", "party": "party"}}], "categories": [{"label": "Amendments"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}], "identical_text": true, "provenance_ids": ["provenance_ids"], "significant_elements": true}], "unaligned_elements": [{"document_label": "document_label", "location": {"begin": 5, "end": 3}, "text": "text", "types": [{"label": {"nature": "nature", "party": "party"}}], "categories": [{"label": "Amendments"}], "attributes": [{"type": "Currency", "text": "text", "location": {"begin": 5, "end": 3}}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        file_1 = io.BytesIO(b'This is a mock file.').getvalue()
        file_2 = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "file_1": file_1,
            "file_2": file_2,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.compare_documents(**req_copy)



# endregion
##############################################################################
# End of Service: Comparison
##############################################################################

##############################################################################
# Start of Service: Feedback
##############################################################################
# region

class TestAddFeedback():
    """
    Test Class for add_feedback
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
    def test_add_feedback_all_params(self):
        """
        add_feedback()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback')
        mock_response = '{"feedback_id": "feedback_id", "user_id": "user_id", "comment": "comment", "created": "2019-01-01T12:00:00.000Z", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ShortDoc model
        short_doc_model = {}
        short_doc_model['title'] = 'testString'
        short_doc_model['hash'] = 'testString'

        # Construct a dict representation of a Location model
        location_model = {}
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a dict representation of a Label model
        label_model = {}
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        # Construct a dict representation of a TypeLabel model
        type_label_model = {}
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        # Construct a dict representation of a Category model
        category_model = {}
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        # Construct a dict representation of a OriginalLabelsIn model
        original_labels_in_model = {}
        original_labels_in_model['types'] = [type_label_model]
        original_labels_in_model['categories'] = [category_model]

        # Construct a dict representation of a UpdatedLabelsIn model
        updated_labels_in_model = {}
        updated_labels_in_model['types'] = [type_label_model]
        updated_labels_in_model['categories'] = [category_model]

        # Construct a dict representation of a FeedbackDataInput model
        feedback_data_input_model = {}
        feedback_data_input_model['feedback_type'] = 'testString'
        feedback_data_input_model['document'] = short_doc_model
        feedback_data_input_model['model_id'] = 'testString'
        feedback_data_input_model['model_version'] = 'testString'
        feedback_data_input_model['location'] = location_model
        feedback_data_input_model['text'] = 'testString'
        feedback_data_input_model['original_labels'] = original_labels_in_model
        feedback_data_input_model['updated_labels'] = updated_labels_in_model

        # Set up parameter values
        feedback_data = feedback_data_input_model
        user_id = 'testString'
        comment = 'testString'

        # Invoke method
        response = _service.add_feedback(
            feedback_data,
            user_id=user_id,
            comment=comment,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['feedback_data'] == feedback_data_input_model
        assert req_body['user_id'] == 'testString'
        assert req_body['comment'] == 'testString'


    @responses.activate
    def test_add_feedback_value_error(self):
        """
        test_add_feedback_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback')
        mock_response = '{"feedback_id": "feedback_id", "user_id": "user_id", "comment": "comment", "created": "2019-01-01T12:00:00.000Z", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ShortDoc model
        short_doc_model = {}
        short_doc_model['title'] = 'testString'
        short_doc_model['hash'] = 'testString'

        # Construct a dict representation of a Location model
        location_model = {}
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a dict representation of a Label model
        label_model = {}
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        # Construct a dict representation of a TypeLabel model
        type_label_model = {}
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        # Construct a dict representation of a Category model
        category_model = {}
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        # Construct a dict representation of a OriginalLabelsIn model
        original_labels_in_model = {}
        original_labels_in_model['types'] = [type_label_model]
        original_labels_in_model['categories'] = [category_model]

        # Construct a dict representation of a UpdatedLabelsIn model
        updated_labels_in_model = {}
        updated_labels_in_model['types'] = [type_label_model]
        updated_labels_in_model['categories'] = [category_model]

        # Construct a dict representation of a FeedbackDataInput model
        feedback_data_input_model = {}
        feedback_data_input_model['feedback_type'] = 'testString'
        feedback_data_input_model['document'] = short_doc_model
        feedback_data_input_model['model_id'] = 'testString'
        feedback_data_input_model['model_version'] = 'testString'
        feedback_data_input_model['location'] = location_model
        feedback_data_input_model['text'] = 'testString'
        feedback_data_input_model['original_labels'] = original_labels_in_model
        feedback_data_input_model['updated_labels'] = updated_labels_in_model

        # Set up parameter values
        feedback_data = feedback_data_input_model
        user_id = 'testString'
        comment = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "feedback_data": feedback_data,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_feedback(**req_copy)



class TestListFeedback():
    """
    Test Class for list_feedback
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
    def test_list_feedback_all_params(self):
        """
        list_feedback()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback')
        mock_response = '{"feedback": [{"feedback_id": "feedback_id", "created": "2019-01-01T12:00:00.000Z", "comment": "comment", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feedback_type = 'testString'
        document_title = 'testString'
        model_id = 'testString'
        model_version = 'testString'
        category_removed = 'testString'
        category_added = 'testString'
        category_not_changed = 'testString'
        type_removed = 'testString'
        type_added = 'testString'
        type_not_changed = 'testString'
        page_limit = 100
        cursor = 'testString'
        sort = 'testString'
        include_total = True

        # Invoke method
        response = _service.list_feedback(
            feedback_type=feedback_type,
            document_title=document_title,
            model_id=model_id,
            model_version=model_version,
            category_removed=category_removed,
            category_added=category_added,
            category_not_changed=category_not_changed,
            type_removed=type_removed,
            type_added=type_added,
            type_not_changed=type_not_changed,
            page_limit=page_limit,
            cursor=cursor,
            sort=sort,
            include_total=include_total,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'feedback_type={}'.format(feedback_type) in query_string
        assert 'document_title={}'.format(document_title) in query_string
        assert 'model_id={}'.format(model_id) in query_string
        assert 'model_version={}'.format(model_version) in query_string
        assert 'category_removed={}'.format(category_removed) in query_string
        assert 'category_added={}'.format(category_added) in query_string
        assert 'category_not_changed={}'.format(category_not_changed) in query_string
        assert 'type_removed={}'.format(type_removed) in query_string
        assert 'type_added={}'.format(type_added) in query_string
        assert 'type_not_changed={}'.format(type_not_changed) in query_string
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'include_total={}'.format('true' if include_total else 'false') in query_string


    @responses.activate
    def test_list_feedback_required_params(self):
        """
        test_list_feedback_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback')
        mock_response = '{"feedback": [{"feedback_id": "feedback_id", "created": "2019-01-01T12:00:00.000Z", "comment": "comment", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_feedback()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_feedback_value_error(self):
        """
        test_list_feedback_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback')
        mock_response = '{"feedback": [{"feedback_id": "feedback_id", "created": "2019-01-01T12:00:00.000Z", "comment": "comment", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}]}'
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
                _service.list_feedback(**req_copy)



class TestGetFeedback():
    """
    Test Class for get_feedback
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
    def test_get_feedback_all_params(self):
        """
        get_feedback()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback/testString')
        mock_response = '{"feedback_id": "feedback_id", "created": "2019-01-01T12:00:00.000Z", "comment": "comment", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feedback_id = 'testString'
        model = 'contracts'

        # Invoke method
        response = _service.get_feedback(
            feedback_id,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_get_feedback_required_params(self):
        """
        test_get_feedback_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback/testString')
        mock_response = '{"feedback_id": "feedback_id", "created": "2019-01-01T12:00:00.000Z", "comment": "comment", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feedback_id = 'testString'

        # Invoke method
        response = _service.get_feedback(
            feedback_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_feedback_value_error(self):
        """
        test_get_feedback_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback/testString')
        mock_response = '{"feedback_id": "feedback_id", "created": "2019-01-01T12:00:00.000Z", "comment": "comment", "feedback_data": {"feedback_type": "feedback_type", "document": {"title": "title", "hash": "hash"}, "model_id": "model_id", "model_version": "model_version", "location": {"begin": 5, "end": 3}, "text": "text", "original_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "updated_labels": {"types": [{"label": {"nature": "nature", "party": "party"}, "provenance_ids": ["provenance_ids"], "modification": "added"}], "categories": [{"label": "Amendments", "provenance_ids": ["provenance_ids"], "modification": "added"}]}, "pagination": {"refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor", "refresh_url": "refresh_url", "next_url": "next_url", "total": 5}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feedback_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "feedback_id": feedback_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_feedback(**req_copy)



class TestDeleteFeedback():
    """
    Test Class for delete_feedback
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
    def test_delete_feedback_all_params(self):
        """
        delete_feedback()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback/testString')
        mock_response = '{"status": 6, "message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feedback_id = 'testString'
        model = 'contracts'

        # Invoke method
        response = _service.delete_feedback(
            feedback_id,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_delete_feedback_required_params(self):
        """
        test_delete_feedback_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback/testString')
        mock_response = '{"status": 6, "message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feedback_id = 'testString'

        # Invoke method
        response = _service.delete_feedback(
            feedback_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_feedback_value_error(self):
        """
        test_delete_feedback_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/feedback/testString')
        mock_response = '{"status": 6, "message": "message"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        feedback_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "feedback_id": feedback_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_feedback(**req_copy)



# endregion
##############################################################################
# End of Service: Feedback
##############################################################################

##############################################################################
# Start of Service: Batches
##############################################################################
# region

class TestCreateBatch():
    """
    Test Class for create_batch
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
    def test_create_batch_all_params(self):
        """
        create_batch()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        function = 'html_conversion'
        input_credentials_file = io.BytesIO(b'This is a mock file.').getvalue()
        input_bucket_location = 'testString'
        input_bucket_name = 'testString'
        output_credentials_file = io.BytesIO(b'This is a mock file.').getvalue()
        output_bucket_location = 'testString'
        output_bucket_name = 'testString'
        model = 'contracts'

        # Invoke method
        response = _service.create_batch(
            function,
            input_credentials_file,
            input_bucket_location,
            input_bucket_name,
            output_credentials_file,
            output_bucket_location,
            output_bucket_name,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'function={}'.format(function) in query_string
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_create_batch_required_params(self):
        """
        test_create_batch_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        function = 'html_conversion'
        input_credentials_file = io.BytesIO(b'This is a mock file.').getvalue()
        input_bucket_location = 'testString'
        input_bucket_name = 'testString'
        output_credentials_file = io.BytesIO(b'This is a mock file.').getvalue()
        output_bucket_location = 'testString'
        output_bucket_name = 'testString'

        # Invoke method
        response = _service.create_batch(
            function,
            input_credentials_file,
            input_bucket_location,
            input_bucket_name,
            output_credentials_file,
            output_bucket_location,
            output_bucket_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'function={}'.format(function) in query_string


    @responses.activate
    def test_create_batch_value_error(self):
        """
        test_create_batch_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        function = 'html_conversion'
        input_credentials_file = io.BytesIO(b'This is a mock file.').getvalue()
        input_bucket_location = 'testString'
        input_bucket_name = 'testString'
        output_credentials_file = io.BytesIO(b'This is a mock file.').getvalue()
        output_bucket_location = 'testString'
        output_bucket_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "function": function,
            "input_credentials_file": input_credentials_file,
            "input_bucket_location": input_bucket_location,
            "input_bucket_name": input_bucket_name,
            "output_credentials_file": output_credentials_file,
            "output_bucket_location": output_bucket_location,
            "output_bucket_name": output_bucket_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_batch(**req_copy)



class TestListBatches():
    """
    Test Class for list_batches
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
    def test_list_batches_all_params(self):
        """
        list_batches()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches')
        mock_response = '{"batches": [{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_batches()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_batches_value_error(self):
        """
        test_list_batches_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches')
        mock_response = '{"batches": [{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
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
                _service.list_batches(**req_copy)



class TestGetBatch():
    """
    Test Class for get_batch
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
    def test_get_batch_all_params(self):
        """
        get_batch()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches/testString')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        batch_id = 'testString'

        # Invoke method
        response = _service.get_batch(
            batch_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_batch_value_error(self):
        """
        test_get_batch_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches/testString')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        batch_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "batch_id": batch_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_batch(**req_copy)



class TestUpdateBatch():
    """
    Test Class for update_batch
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
    def test_update_batch_all_params(self):
        """
        update_batch()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches/testString')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        batch_id = 'testString'
        action = 'rescan'
        model = 'contracts'

        # Invoke method
        response = _service.update_batch(
            batch_id,
            action,
            model=model,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'action={}'.format(action) in query_string
        assert 'model={}'.format(model) in query_string


    @responses.activate
    def test_update_batch_required_params(self):
        """
        test_update_batch_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches/testString')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        batch_id = 'testString'
        action = 'rescan'

        # Invoke method
        response = _service.update_batch(
            batch_id,
            action,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'action={}'.format(action) in query_string


    @responses.activate
    def test_update_batch_value_error(self):
        """
        test_update_batch_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/batches/testString')
        mock_response = '{"function": "element_classification", "input_bucket_location": "input_bucket_location", "input_bucket_name": "input_bucket_name", "output_bucket_location": "output_bucket_location", "output_bucket_name": "output_bucket_name", "batch_id": "batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "status", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        batch_id = 'testString'
        action = 'rescan'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "batch_id": batch_id,
            "action": action,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_batch(**req_copy)



# endregion
##############################################################################
# End of Service: Batches
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Address():
    """
    Test Class for Address
    """

    def test_address_serialization(self):
        """
        Test serialization/deserialization for Address
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a Address model
        address_model_json = {}
        address_model_json['text'] = 'testString'
        address_model_json['location'] = location_model

        # Construct a model instance of Address by calling from_dict on the json representation
        address_model = Address.from_dict(address_model_json)
        assert address_model != False

        # Construct a model instance of Address by calling from_dict on the json representation
        address_model_dict = Address.from_dict(address_model_json).__dict__
        address_model2 = Address(**address_model_dict)

        # Verify the model instances are equivalent
        assert address_model == address_model2

        # Convert model instance back to dict and verify no loss of data
        address_model_json2 = address_model.to_dict()
        assert address_model_json2 == address_model_json

class TestModel_AlignedElement():
    """
    Test Class for AlignedElement
    """

    def test_aligned_element_serialization(self):
        """
        Test serialization/deserialization for AlignedElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_comparison_model = {} # TypeLabelComparison
        type_label_comparison_model['label'] = label_model

        category_comparison_model = {} # CategoryComparison
        category_comparison_model['label'] = 'Amendments'

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        element_pair_model = {} # ElementPair
        element_pair_model['document_label'] = 'testString'
        element_pair_model['text'] = 'testString'
        element_pair_model['location'] = location_model
        element_pair_model['types'] = [type_label_comparison_model]
        element_pair_model['categories'] = [category_comparison_model]
        element_pair_model['attributes'] = [attribute_model]

        # Construct a json representation of a AlignedElement model
        aligned_element_model_json = {}
        aligned_element_model_json['element_pair'] = [element_pair_model]
        aligned_element_model_json['identical_text'] = True
        aligned_element_model_json['provenance_ids'] = ['testString']
        aligned_element_model_json['significant_elements'] = True

        # Construct a model instance of AlignedElement by calling from_dict on the json representation
        aligned_element_model = AlignedElement.from_dict(aligned_element_model_json)
        assert aligned_element_model != False

        # Construct a model instance of AlignedElement by calling from_dict on the json representation
        aligned_element_model_dict = AlignedElement.from_dict(aligned_element_model_json).__dict__
        aligned_element_model2 = AlignedElement(**aligned_element_model_dict)

        # Verify the model instances are equivalent
        assert aligned_element_model == aligned_element_model2

        # Convert model instance back to dict and verify no loss of data
        aligned_element_model_json2 = aligned_element_model.to_dict()
        assert aligned_element_model_json2 == aligned_element_model_json

class TestModel_Attribute():
    """
    Test Class for Attribute
    """

    def test_attribute_serialization(self):
        """
        Test serialization/deserialization for Attribute
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a Attribute model
        attribute_model_json = {}
        attribute_model_json['type'] = 'Currency'
        attribute_model_json['text'] = 'testString'
        attribute_model_json['location'] = location_model

        # Construct a model instance of Attribute by calling from_dict on the json representation
        attribute_model = Attribute.from_dict(attribute_model_json)
        assert attribute_model != False

        # Construct a model instance of Attribute by calling from_dict on the json representation
        attribute_model_dict = Attribute.from_dict(attribute_model_json).__dict__
        attribute_model2 = Attribute(**attribute_model_dict)

        # Verify the model instances are equivalent
        assert attribute_model == attribute_model2

        # Convert model instance back to dict and verify no loss of data
        attribute_model_json2 = attribute_model.to_dict()
        assert attribute_model_json2 == attribute_model_json

class TestModel_BatchStatus():
    """
    Test Class for BatchStatus
    """

    def test_batch_status_serialization(self):
        """
        Test serialization/deserialization for BatchStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        doc_counts_model = {} # DocCounts
        doc_counts_model['total'] = 38
        doc_counts_model['pending'] = 38
        doc_counts_model['successful'] = 38
        doc_counts_model['failed'] = 38

        # Construct a json representation of a BatchStatus model
        batch_status_model_json = {}
        batch_status_model_json['function'] = 'element_classification'
        batch_status_model_json['input_bucket_location'] = 'testString'
        batch_status_model_json['input_bucket_name'] = 'testString'
        batch_status_model_json['output_bucket_location'] = 'testString'
        batch_status_model_json['output_bucket_name'] = 'testString'
        batch_status_model_json['batch_id'] = 'testString'
        batch_status_model_json['document_counts'] = doc_counts_model
        batch_status_model_json['status'] = 'testString'
        batch_status_model_json['created'] = "2019-01-01T12:00:00Z"
        batch_status_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of BatchStatus by calling from_dict on the json representation
        batch_status_model = BatchStatus.from_dict(batch_status_model_json)
        assert batch_status_model != False

        # Construct a model instance of BatchStatus by calling from_dict on the json representation
        batch_status_model_dict = BatchStatus.from_dict(batch_status_model_json).__dict__
        batch_status_model2 = BatchStatus(**batch_status_model_dict)

        # Verify the model instances are equivalent
        assert batch_status_model == batch_status_model2

        # Convert model instance back to dict and verify no loss of data
        batch_status_model_json2 = batch_status_model.to_dict()
        assert batch_status_model_json2 == batch_status_model_json

class TestModel_Batches():
    """
    Test Class for Batches
    """

    def test_batches_serialization(self):
        """
        Test serialization/deserialization for Batches
        """

        # Construct dict forms of any model objects needed in order to build this model.

        doc_counts_model = {} # DocCounts
        doc_counts_model['total'] = 38
        doc_counts_model['pending'] = 38
        doc_counts_model['successful'] = 38
        doc_counts_model['failed'] = 38

        batch_status_model = {} # BatchStatus
        batch_status_model['function'] = 'element_classification'
        batch_status_model['input_bucket_location'] = 'testString'
        batch_status_model['input_bucket_name'] = 'testString'
        batch_status_model['output_bucket_location'] = 'testString'
        batch_status_model['output_bucket_name'] = 'testString'
        batch_status_model['batch_id'] = 'testString'
        batch_status_model['document_counts'] = doc_counts_model
        batch_status_model['status'] = 'testString'
        batch_status_model['created'] = "2019-01-01T12:00:00Z"
        batch_status_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a Batches model
        batches_model_json = {}
        batches_model_json['batches'] = [batch_status_model]

        # Construct a model instance of Batches by calling from_dict on the json representation
        batches_model = Batches.from_dict(batches_model_json)
        assert batches_model != False

        # Construct a model instance of Batches by calling from_dict on the json representation
        batches_model_dict = Batches.from_dict(batches_model_json).__dict__
        batches_model2 = Batches(**batches_model_dict)

        # Verify the model instances are equivalent
        assert batches_model == batches_model2

        # Convert model instance back to dict and verify no loss of data
        batches_model_json2 = batches_model.to_dict()
        assert batches_model_json2 == batches_model_json

class TestModel_BodyCells():
    """
    Test Class for BodyCells
    """

    def test_body_cells_serialization(self):
        """
        Test serialization/deserialization for BodyCells
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        # Construct a json representation of a BodyCells model
        body_cells_model_json = {}
        body_cells_model_json['cell_id'] = 'testString'
        body_cells_model_json['location'] = location_model
        body_cells_model_json['text'] = 'testString'
        body_cells_model_json['row_index_begin'] = 26
        body_cells_model_json['row_index_end'] = 26
        body_cells_model_json['column_index_begin'] = 26
        body_cells_model_json['column_index_end'] = 26
        body_cells_model_json['row_header_ids'] = ['testString']
        body_cells_model_json['row_header_texts'] = ['testString']
        body_cells_model_json['row_header_texts_normalized'] = ['testString']
        body_cells_model_json['column_header_ids'] = ['testString']
        body_cells_model_json['column_header_texts'] = ['testString']
        body_cells_model_json['column_header_texts_normalized'] = ['testString']
        body_cells_model_json['attributes'] = [attribute_model]

        # Construct a model instance of BodyCells by calling from_dict on the json representation
        body_cells_model = BodyCells.from_dict(body_cells_model_json)
        assert body_cells_model != False

        # Construct a model instance of BodyCells by calling from_dict on the json representation
        body_cells_model_dict = BodyCells.from_dict(body_cells_model_json).__dict__
        body_cells_model2 = BodyCells(**body_cells_model_dict)

        # Verify the model instances are equivalent
        assert body_cells_model == body_cells_model2

        # Convert model instance back to dict and verify no loss of data
        body_cells_model_json2 = body_cells_model.to_dict()
        assert body_cells_model_json2 == body_cells_model_json

class TestModel_Category():
    """
    Test Class for Category
    """

    def test_category_serialization(self):
        """
        Test serialization/deserialization for Category
        """

        # Construct a json representation of a Category model
        category_model_json = {}
        category_model_json['label'] = 'Amendments'
        category_model_json['provenance_ids'] = ['testString']
        category_model_json['modification'] = 'added'

        # Construct a model instance of Category by calling from_dict on the json representation
        category_model = Category.from_dict(category_model_json)
        assert category_model != False

        # Construct a model instance of Category by calling from_dict on the json representation
        category_model_dict = Category.from_dict(category_model_json).__dict__
        category_model2 = Category(**category_model_dict)

        # Verify the model instances are equivalent
        assert category_model == category_model2

        # Convert model instance back to dict and verify no loss of data
        category_model_json2 = category_model.to_dict()
        assert category_model_json2 == category_model_json

class TestModel_CategoryComparison():
    """
    Test Class for CategoryComparison
    """

    def test_category_comparison_serialization(self):
        """
        Test serialization/deserialization for CategoryComparison
        """

        # Construct a json representation of a CategoryComparison model
        category_comparison_model_json = {}
        category_comparison_model_json['label'] = 'Amendments'

        # Construct a model instance of CategoryComparison by calling from_dict on the json representation
        category_comparison_model = CategoryComparison.from_dict(category_comparison_model_json)
        assert category_comparison_model != False

        # Construct a model instance of CategoryComparison by calling from_dict on the json representation
        category_comparison_model_dict = CategoryComparison.from_dict(category_comparison_model_json).__dict__
        category_comparison_model2 = CategoryComparison(**category_comparison_model_dict)

        # Verify the model instances are equivalent
        assert category_comparison_model == category_comparison_model2

        # Convert model instance back to dict and verify no loss of data
        category_comparison_model_json2 = category_comparison_model.to_dict()
        assert category_comparison_model_json2 == category_comparison_model_json

class TestModel_ClassifyReturn():
    """
    Test Class for ClassifyReturn
    """

    def test_classify_return_serialization(self):
        """
        Test serialization/deserialization for ClassifyReturn
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_model = {} # Document
        document_model['title'] = 'IBM DC QDRO Guidelines'
        document_model['html'] = '<?xml version=\'1.0\' encoding=\'UTF-8\' standalone=\'yes\'?><html>\n<head>\n ...'
        document_model['hash'] = '91edc2ff254d29f7a4922635ad47276a'
        document_model['label'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 6958
        location_model['end'] = 7171

        label_model = {} # Label
        label_model['nature'] = 'Obligation'
        label_model['party'] = 'You'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['Nlu0ogWAEGms4vjhhzpMv3iXhm8b8fBqMBNtT/bXH8JI=', 'Pqjd5I+s/Fdpx2NbIwCRMtyPLV8n1Hq+wINPGAr/PNtcRCSdxR9P7RLf1/eXPKQYI']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        element_model = {} # Element
        element_model['location'] = location_model
        element_model['text'] = 'In the following sections, you will find the Plan\'s processing guidelines for determining the qualification of an order and some discussion of plan features and issues that should be considered in drafting a QDRO.'
        element_model['types'] = [type_label_model]
        element_model['categories'] = [category_model]
        element_model['attributes'] = [attribute_model]

        effective_dates_model = {} # EffectiveDates
        effective_dates_model['confidence_level'] = 'High'
        effective_dates_model['text'] = 'testString'
        effective_dates_model['text_normalized'] = 'testString'
        effective_dates_model['provenance_ids'] = ['testString']
        effective_dates_model['location'] = location_model

        interpretation_model = {} # Interpretation
        interpretation_model['value'] = 'testString'
        interpretation_model['numeric_value'] = 72.5
        interpretation_model['unit'] = 'testString'

        contract_amts_model = {} # ContractAmts
        contract_amts_model['confidence_level'] = 'High'
        contract_amts_model['text'] = 'testString'
        contract_amts_model['text_normalized'] = 'testString'
        contract_amts_model['interpretation'] = interpretation_model
        contract_amts_model['provenance_ids'] = ['testString']
        contract_amts_model['location'] = location_model

        termination_dates_model = {} # TerminationDates
        termination_dates_model['confidence_level'] = 'High'
        termination_dates_model['text'] = 'testString'
        termination_dates_model['text_normalized'] = 'testString'
        termination_dates_model['provenance_ids'] = ['testString']
        termination_dates_model['location'] = location_model

        contract_types_model = {} # ContractTypes
        contract_types_model['confidence_level'] = 'High'
        contract_types_model['text'] = 'testString'
        contract_types_model['provenance_ids'] = ['testString']
        contract_types_model['location'] = location_model

        contract_terms_model = {} # ContractTerms
        contract_terms_model['confidence_level'] = 'High'
        contract_terms_model['text'] = 'testString'
        contract_terms_model['text_normalized'] = 'testString'
        contract_terms_model['interpretation'] = interpretation_model
        contract_terms_model['provenance_ids'] = ['testString']
        contract_terms_model['location'] = location_model

        payment_terms_model = {} # PaymentTerms
        payment_terms_model['confidence_level'] = 'High'
        payment_terms_model['text'] = 'testString'
        payment_terms_model['text_normalized'] = 'testString'
        payment_terms_model['interpretation'] = interpretation_model
        payment_terms_model['provenance_ids'] = ['testString']
        payment_terms_model['location'] = location_model

        contract_currencies_model = {} # ContractCurrencies
        contract_currencies_model['confidence_level'] = 'High'
        contract_currencies_model['text'] = 'testString'
        contract_currencies_model['text_normalized'] = 'testString'
        contract_currencies_model['provenance_ids'] = ['testString']
        contract_currencies_model['location'] = location_model

        section_title_model = {} # SectionTitle
        section_title_model['text'] = 'Buyer will pay Supplier certain amounts for the Developed Works and other Services and Deliverables as described below: '
        section_title_model['location'] = location_model

        table_title_model = {} # TableTitle
        table_title_model['location'] = location_model
        table_title_model['text'] = 'Roles and responsibilities'

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = { 'foo': 'bar' }
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        row_headers_model = {} # RowHeaders
        row_headers_model['cell_id'] = 'testString'
        row_headers_model['location'] = location_model
        row_headers_model['text'] = 'testString'
        row_headers_model['text_normalized'] = 'testString'
        row_headers_model['row_index_begin'] = 26
        row_headers_model['row_index_end'] = 26
        row_headers_model['column_index_begin'] = 26
        row_headers_model['column_index_end'] = 26

        column_headers_model = {} # ColumnHeaders
        column_headers_model['cell_id'] = 'colHeader-23489-23496'
        column_headers_model['location'] = { 'foo': 'bar' }
        column_headers_model['text'] = 'Res Ref'
        column_headers_model['text_normalized'] = 'Res Ref'
        column_headers_model['row_index_begin'] = 0
        column_headers_model['row_index_end'] = 0
        column_headers_model['column_index_begin'] = 0
        column_headers_model['column_index_end'] = 0

        body_cells_model = {} # BodyCells
        body_cells_model['cell_id'] = 'bodyCell-24768-24777'
        body_cells_model['location'] = location_model
        body_cells_model['text'] = 'RBS-RES01'
        body_cells_model['row_index_begin'] = 1
        body_cells_model['row_index_end'] = 1
        body_cells_model['column_index_begin'] = 0
        body_cells_model['column_index_end'] = 0
        body_cells_model['row_header_ids'] = []
        body_cells_model['row_header_texts'] = []
        body_cells_model['row_header_texts_normalized'] = []
        body_cells_model['column_header_ids'] = ['colHeader-23489-23496']
        body_cells_model['column_header_texts'] = ['Res Ref']
        body_cells_model['column_header_texts_normalized'] = ['Res Ref']
        body_cells_model['attributes'] = [attribute_model]

        contexts_model = {} # Contexts
        contexts_model['text'] = 'testString'
        contexts_model['location'] = location_model

        key_model = {} # Key
        key_model['cell_id'] = 'testString'
        key_model['location'] = location_model
        key_model['text'] = 'testString'

        value_model = {} # Value
        value_model['cell_id'] = 'testString'
        value_model['location'] = location_model
        value_model['text'] = 'testString'

        key_value_pair_model = {} # KeyValuePair
        key_value_pair_model['key'] = key_model
        key_value_pair_model['value'] = [value_model]

        tables_model = {} # Tables
        tables_model['location'] = location_model
        tables_model['text'] = 'Res Ref Role Type Estimated Days Rate (per da y) Estimated Total RBS-RES01 CRM Developer 1 (Junior Technical Consultant) 55 £600 £33,000 RBS-RES02 CRM Developer 2 (Junior Technical Consultant) 77 £600 £46,200 RBS-RES03 Specialist Tester (Test Lead) 65 £550 £35,750    Totals     £114,950 '
        tables_model['section_title'] = section_title_model
        tables_model['title'] = table_title_model
        tables_model['table_headers'] = [table_headers_model]
        tables_model['row_headers'] = [row_headers_model]
        tables_model['column_headers'] = [column_headers_model]
        tables_model['body_cells'] = [body_cells_model]
        tables_model['contexts'] = [contexts_model]
        tables_model['key_value_pairs'] = [key_value_pair_model]

        element_locations_model = {} # ElementLocations
        element_locations_model['begin'] = 4174
        element_locations_model['end'] = 4277

        section_titles_model = {} # SectionTitles
        section_titles_model['text'] = '1.0 Scope of Work Summary'
        section_titles_model['location'] = location_model
        section_titles_model['level'] = 1
        section_titles_model['element_locations'] = [element_locations_model]

        leading_sentence_model = {} # LeadingSentence
        leading_sentence_model['text'] = 'testString'
        leading_sentence_model['location'] = location_model
        leading_sentence_model['element_locations'] = [element_locations_model]

        paragraphs_model = {} # Paragraphs
        paragraphs_model['location'] = location_model

        doc_structure_model = {} # DocStructure
        doc_structure_model['section_titles'] = [section_titles_model]
        doc_structure_model['leading_sentences'] = [leading_sentence_model]
        doc_structure_model['paragraphs'] = [paragraphs_model]

        address_model = {} # Address
        address_model['text'] = 'testString'
        address_model['location'] = location_model

        contact_model = {} # Contact
        contact_model['name'] = 'testString'
        contact_model['role'] = 'testString'

        mention_model = {} # Mention
        mention_model['text'] = 'testString'
        mention_model['location'] = location_model

        parties_model = {} # Parties
        parties_model['party'] = 'IBM'
        parties_model['role'] = 'Unknown'
        parties_model['importance'] = 'Primary'
        parties_model['addresses'] = [address_model]
        parties_model['contacts'] = [contact_model]
        parties_model['mentions'] = [mention_model]

        # Construct a json representation of a ClassifyReturn model
        classify_return_model_json = {}
        classify_return_model_json['document'] = document_model
        classify_return_model_json['model_id'] = 'testString'
        classify_return_model_json['model_version'] = 'testString'
        classify_return_model_json['elements'] = [element_model]
        classify_return_model_json['effective_dates'] = [effective_dates_model]
        classify_return_model_json['contract_amounts'] = [contract_amts_model]
        classify_return_model_json['termination_dates'] = [termination_dates_model]
        classify_return_model_json['contract_types'] = [contract_types_model]
        classify_return_model_json['contract_terms'] = [contract_terms_model]
        classify_return_model_json['payment_terms'] = [payment_terms_model]
        classify_return_model_json['contract_currencies'] = [contract_currencies_model]
        classify_return_model_json['tables'] = [tables_model]
        classify_return_model_json['document_structure'] = doc_structure_model
        classify_return_model_json['parties'] = [parties_model]

        # Construct a model instance of ClassifyReturn by calling from_dict on the json representation
        classify_return_model = ClassifyReturn.from_dict(classify_return_model_json)
        assert classify_return_model != False

        # Construct a model instance of ClassifyReturn by calling from_dict on the json representation
        classify_return_model_dict = ClassifyReturn.from_dict(classify_return_model_json).__dict__
        classify_return_model2 = ClassifyReturn(**classify_return_model_dict)

        # Verify the model instances are equivalent
        assert classify_return_model == classify_return_model2

        # Convert model instance back to dict and verify no loss of data
        classify_return_model_json2 = classify_return_model.to_dict()
        assert classify_return_model_json2 == classify_return_model_json

class TestModel_ColumnHeaders():
    """
    Test Class for ColumnHeaders
    """

    def test_column_headers_serialization(self):
        """
        Test serialization/deserialization for ColumnHeaders
        """

        # Construct a json representation of a ColumnHeaders model
        column_headers_model_json = {}
        column_headers_model_json['cell_id'] = 'testString'
        column_headers_model_json['location'] = { 'foo': 'bar' }
        column_headers_model_json['text'] = 'testString'
        column_headers_model_json['text_normalized'] = 'testString'
        column_headers_model_json['row_index_begin'] = 26
        column_headers_model_json['row_index_end'] = 26
        column_headers_model_json['column_index_begin'] = 26
        column_headers_model_json['column_index_end'] = 26

        # Construct a model instance of ColumnHeaders by calling from_dict on the json representation
        column_headers_model = ColumnHeaders.from_dict(column_headers_model_json)
        assert column_headers_model != False

        # Construct a model instance of ColumnHeaders by calling from_dict on the json representation
        column_headers_model_dict = ColumnHeaders.from_dict(column_headers_model_json).__dict__
        column_headers_model2 = ColumnHeaders(**column_headers_model_dict)

        # Verify the model instances are equivalent
        assert column_headers_model == column_headers_model2

        # Convert model instance back to dict and verify no loss of data
        column_headers_model_json2 = column_headers_model.to_dict()
        assert column_headers_model_json2 == column_headers_model_json

class TestModel_CompareReturn():
    """
    Test Class for CompareReturn
    """

    def test_compare_return_serialization(self):
        """
        Test serialization/deserialization for CompareReturn
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_model = {} # Document
        document_model['title'] = '31235_000156459017003570_kodk-ex1013_296.pdf'
        document_model['html'] = '<html><head>...'
        document_model['hash'] = '0d9589556c16fca21c64ce9c8b10d065'
        document_model['label'] = 'file_1'

        location_model = {} # Location
        location_model['begin'] = 5690
        location_model['end'] = 5865

        label_model = {} # Label
        label_model['nature'] = 'Exclusion'
        label_model['party'] = 'You'

        type_label_comparison_model = {} # TypeLabelComparison
        type_label_comparison_model['label'] = label_model

        category_comparison_model = {} # CategoryComparison
        category_comparison_model['label'] = 'Amendments'

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        element_pair_model = {} # ElementPair
        element_pair_model['document_label'] = 'file_1'
        element_pair_model['text'] = 'You will not have the rights of a Ishki shareholder with respect to the shares issued to you in payment of your RSUs until the shares are actually issued and delivered to you.'
        element_pair_model['location'] = location_model
        element_pair_model['types'] = [type_label_comparison_model]
        element_pair_model['categories'] = [category_comparison_model]
        element_pair_model['attributes'] = [attribute_model]

        aligned_element_model = {} # AlignedElement
        aligned_element_model['element_pair'] = [element_pair_model]
        aligned_element_model['identical_text'] = True
        aligned_element_model['provenance_ids'] = ['1mSG/96z1wY4De35LAExJzhCo2t0DfvbYnTl+vbavjY=']
        aligned_element_model['significant_elements'] = True

        unaligned_element_model = {} # UnalignedElement
        unaligned_element_model['document_label'] = 'file_1'
        unaligned_element_model['location'] = location_model
        unaligned_element_model['text'] = 'The RSUs (at the time of vesting or otherwise) will be includible as compensation for pension.'
        unaligned_element_model['types'] = [type_label_comparison_model]
        unaligned_element_model['categories'] = [category_comparison_model]
        unaligned_element_model['attributes'] = [attribute_model]

        # Construct a json representation of a CompareReturn model
        compare_return_model_json = {}
        compare_return_model_json['model_id'] = 'testString'
        compare_return_model_json['model_version'] = 'testString'
        compare_return_model_json['documents'] = [document_model]
        compare_return_model_json['aligned_elements'] = [aligned_element_model]
        compare_return_model_json['unaligned_elements'] = [unaligned_element_model]

        # Construct a model instance of CompareReturn by calling from_dict on the json representation
        compare_return_model = CompareReturn.from_dict(compare_return_model_json)
        assert compare_return_model != False

        # Construct a model instance of CompareReturn by calling from_dict on the json representation
        compare_return_model_dict = CompareReturn.from_dict(compare_return_model_json).__dict__
        compare_return_model2 = CompareReturn(**compare_return_model_dict)

        # Verify the model instances are equivalent
        assert compare_return_model == compare_return_model2

        # Convert model instance back to dict and verify no loss of data
        compare_return_model_json2 = compare_return_model.to_dict()
        assert compare_return_model_json2 == compare_return_model_json

class TestModel_Contact():
    """
    Test Class for Contact
    """

    def test_contact_serialization(self):
        """
        Test serialization/deserialization for Contact
        """

        # Construct a json representation of a Contact model
        contact_model_json = {}
        contact_model_json['name'] = 'testString'
        contact_model_json['role'] = 'testString'

        # Construct a model instance of Contact by calling from_dict on the json representation
        contact_model = Contact.from_dict(contact_model_json)
        assert contact_model != False

        # Construct a model instance of Contact by calling from_dict on the json representation
        contact_model_dict = Contact.from_dict(contact_model_json).__dict__
        contact_model2 = Contact(**contact_model_dict)

        # Verify the model instances are equivalent
        assert contact_model == contact_model2

        # Convert model instance back to dict and verify no loss of data
        contact_model_json2 = contact_model.to_dict()
        assert contact_model_json2 == contact_model_json

class TestModel_Contexts():
    """
    Test Class for Contexts
    """

    def test_contexts_serialization(self):
        """
        Test serialization/deserialization for Contexts
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a Contexts model
        contexts_model_json = {}
        contexts_model_json['text'] = 'testString'
        contexts_model_json['location'] = location_model

        # Construct a model instance of Contexts by calling from_dict on the json representation
        contexts_model = Contexts.from_dict(contexts_model_json)
        assert contexts_model != False

        # Construct a model instance of Contexts by calling from_dict on the json representation
        contexts_model_dict = Contexts.from_dict(contexts_model_json).__dict__
        contexts_model2 = Contexts(**contexts_model_dict)

        # Verify the model instances are equivalent
        assert contexts_model == contexts_model2

        # Convert model instance back to dict and verify no loss of data
        contexts_model_json2 = contexts_model.to_dict()
        assert contexts_model_json2 == contexts_model_json

class TestModel_ContractAmts():
    """
    Test Class for ContractAmts
    """

    def test_contract_amts_serialization(self):
        """
        Test serialization/deserialization for ContractAmts
        """

        # Construct dict forms of any model objects needed in order to build this model.

        interpretation_model = {} # Interpretation
        interpretation_model['value'] = 'testString'
        interpretation_model['numeric_value'] = 72.5
        interpretation_model['unit'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a ContractAmts model
        contract_amts_model_json = {}
        contract_amts_model_json['confidence_level'] = 'High'
        contract_amts_model_json['text'] = 'testString'
        contract_amts_model_json['text_normalized'] = 'testString'
        contract_amts_model_json['interpretation'] = interpretation_model
        contract_amts_model_json['provenance_ids'] = ['testString']
        contract_amts_model_json['location'] = location_model

        # Construct a model instance of ContractAmts by calling from_dict on the json representation
        contract_amts_model = ContractAmts.from_dict(contract_amts_model_json)
        assert contract_amts_model != False

        # Construct a model instance of ContractAmts by calling from_dict on the json representation
        contract_amts_model_dict = ContractAmts.from_dict(contract_amts_model_json).__dict__
        contract_amts_model2 = ContractAmts(**contract_amts_model_dict)

        # Verify the model instances are equivalent
        assert contract_amts_model == contract_amts_model2

        # Convert model instance back to dict and verify no loss of data
        contract_amts_model_json2 = contract_amts_model.to_dict()
        assert contract_amts_model_json2 == contract_amts_model_json

class TestModel_ContractCurrencies():
    """
    Test Class for ContractCurrencies
    """

    def test_contract_currencies_serialization(self):
        """
        Test serialization/deserialization for ContractCurrencies
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a ContractCurrencies model
        contract_currencies_model_json = {}
        contract_currencies_model_json['confidence_level'] = 'High'
        contract_currencies_model_json['text'] = 'testString'
        contract_currencies_model_json['text_normalized'] = 'testString'
        contract_currencies_model_json['provenance_ids'] = ['testString']
        contract_currencies_model_json['location'] = location_model

        # Construct a model instance of ContractCurrencies by calling from_dict on the json representation
        contract_currencies_model = ContractCurrencies.from_dict(contract_currencies_model_json)
        assert contract_currencies_model != False

        # Construct a model instance of ContractCurrencies by calling from_dict on the json representation
        contract_currencies_model_dict = ContractCurrencies.from_dict(contract_currencies_model_json).__dict__
        contract_currencies_model2 = ContractCurrencies(**contract_currencies_model_dict)

        # Verify the model instances are equivalent
        assert contract_currencies_model == contract_currencies_model2

        # Convert model instance back to dict and verify no loss of data
        contract_currencies_model_json2 = contract_currencies_model.to_dict()
        assert contract_currencies_model_json2 == contract_currencies_model_json

class TestModel_ContractTerms():
    """
    Test Class for ContractTerms
    """

    def test_contract_terms_serialization(self):
        """
        Test serialization/deserialization for ContractTerms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        interpretation_model = {} # Interpretation
        interpretation_model['value'] = 'testString'
        interpretation_model['numeric_value'] = 72.5
        interpretation_model['unit'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a ContractTerms model
        contract_terms_model_json = {}
        contract_terms_model_json['confidence_level'] = 'High'
        contract_terms_model_json['text'] = 'testString'
        contract_terms_model_json['text_normalized'] = 'testString'
        contract_terms_model_json['interpretation'] = interpretation_model
        contract_terms_model_json['provenance_ids'] = ['testString']
        contract_terms_model_json['location'] = location_model

        # Construct a model instance of ContractTerms by calling from_dict on the json representation
        contract_terms_model = ContractTerms.from_dict(contract_terms_model_json)
        assert contract_terms_model != False

        # Construct a model instance of ContractTerms by calling from_dict on the json representation
        contract_terms_model_dict = ContractTerms.from_dict(contract_terms_model_json).__dict__
        contract_terms_model2 = ContractTerms(**contract_terms_model_dict)

        # Verify the model instances are equivalent
        assert contract_terms_model == contract_terms_model2

        # Convert model instance back to dict and verify no loss of data
        contract_terms_model_json2 = contract_terms_model.to_dict()
        assert contract_terms_model_json2 == contract_terms_model_json

class TestModel_ContractTypes():
    """
    Test Class for ContractTypes
    """

    def test_contract_types_serialization(self):
        """
        Test serialization/deserialization for ContractTypes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a ContractTypes model
        contract_types_model_json = {}
        contract_types_model_json['confidence_level'] = 'High'
        contract_types_model_json['text'] = 'testString'
        contract_types_model_json['provenance_ids'] = ['testString']
        contract_types_model_json['location'] = location_model

        # Construct a model instance of ContractTypes by calling from_dict on the json representation
        contract_types_model = ContractTypes.from_dict(contract_types_model_json)
        assert contract_types_model != False

        # Construct a model instance of ContractTypes by calling from_dict on the json representation
        contract_types_model_dict = ContractTypes.from_dict(contract_types_model_json).__dict__
        contract_types_model2 = ContractTypes(**contract_types_model_dict)

        # Verify the model instances are equivalent
        assert contract_types_model == contract_types_model2

        # Convert model instance back to dict and verify no loss of data
        contract_types_model_json2 = contract_types_model.to_dict()
        assert contract_types_model_json2 == contract_types_model_json

class TestModel_DocCounts():
    """
    Test Class for DocCounts
    """

    def test_doc_counts_serialization(self):
        """
        Test serialization/deserialization for DocCounts
        """

        # Construct a json representation of a DocCounts model
        doc_counts_model_json = {}
        doc_counts_model_json['total'] = 38
        doc_counts_model_json['pending'] = 38
        doc_counts_model_json['successful'] = 38
        doc_counts_model_json['failed'] = 38

        # Construct a model instance of DocCounts by calling from_dict on the json representation
        doc_counts_model = DocCounts.from_dict(doc_counts_model_json)
        assert doc_counts_model != False

        # Construct a model instance of DocCounts by calling from_dict on the json representation
        doc_counts_model_dict = DocCounts.from_dict(doc_counts_model_json).__dict__
        doc_counts_model2 = DocCounts(**doc_counts_model_dict)

        # Verify the model instances are equivalent
        assert doc_counts_model == doc_counts_model2

        # Convert model instance back to dict and verify no loss of data
        doc_counts_model_json2 = doc_counts_model.to_dict()
        assert doc_counts_model_json2 == doc_counts_model_json

class TestModel_DocInfo():
    """
    Test Class for DocInfo
    """

    def test_doc_info_serialization(self):
        """
        Test serialization/deserialization for DocInfo
        """

        # Construct a json representation of a DocInfo model
        doc_info_model_json = {}
        doc_info_model_json['html'] = 'testString'
        doc_info_model_json['title'] = 'testString'
        doc_info_model_json['hash'] = 'testString'

        # Construct a model instance of DocInfo by calling from_dict on the json representation
        doc_info_model = DocInfo.from_dict(doc_info_model_json)
        assert doc_info_model != False

        # Construct a model instance of DocInfo by calling from_dict on the json representation
        doc_info_model_dict = DocInfo.from_dict(doc_info_model_json).__dict__
        doc_info_model2 = DocInfo(**doc_info_model_dict)

        # Verify the model instances are equivalent
        assert doc_info_model == doc_info_model2

        # Convert model instance back to dict and verify no loss of data
        doc_info_model_json2 = doc_info_model.to_dict()
        assert doc_info_model_json2 == doc_info_model_json

class TestModel_DocStructure():
    """
    Test Class for DocStructure
    """

    def test_doc_structure_serialization(self):
        """
        Test serialization/deserialization for DocStructure
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        element_locations_model = {} # ElementLocations
        element_locations_model['begin'] = 38
        element_locations_model['end'] = 38

        section_titles_model = {} # SectionTitles
        section_titles_model['text'] = 'testString'
        section_titles_model['location'] = location_model
        section_titles_model['level'] = 38
        section_titles_model['element_locations'] = [element_locations_model]

        leading_sentence_model = {} # LeadingSentence
        leading_sentence_model['text'] = 'testString'
        leading_sentence_model['location'] = location_model
        leading_sentence_model['element_locations'] = [element_locations_model]

        paragraphs_model = {} # Paragraphs
        paragraphs_model['location'] = location_model

        # Construct a json representation of a DocStructure model
        doc_structure_model_json = {}
        doc_structure_model_json['section_titles'] = [section_titles_model]
        doc_structure_model_json['leading_sentences'] = [leading_sentence_model]
        doc_structure_model_json['paragraphs'] = [paragraphs_model]

        # Construct a model instance of DocStructure by calling from_dict on the json representation
        doc_structure_model = DocStructure.from_dict(doc_structure_model_json)
        assert doc_structure_model != False

        # Construct a model instance of DocStructure by calling from_dict on the json representation
        doc_structure_model_dict = DocStructure.from_dict(doc_structure_model_json).__dict__
        doc_structure_model2 = DocStructure(**doc_structure_model_dict)

        # Verify the model instances are equivalent
        assert doc_structure_model == doc_structure_model2

        # Convert model instance back to dict and verify no loss of data
        doc_structure_model_json2 = doc_structure_model.to_dict()
        assert doc_structure_model_json2 == doc_structure_model_json

class TestModel_Document():
    """
    Test Class for Document
    """

    def test_document_serialization(self):
        """
        Test serialization/deserialization for Document
        """

        # Construct a json representation of a Document model
        document_model_json = {}
        document_model_json['title'] = 'testString'
        document_model_json['html'] = 'testString'
        document_model_json['hash'] = 'testString'
        document_model_json['label'] = 'testString'

        # Construct a model instance of Document by calling from_dict on the json representation
        document_model = Document.from_dict(document_model_json)
        assert document_model != False

        # Construct a model instance of Document by calling from_dict on the json representation
        document_model_dict = Document.from_dict(document_model_json).__dict__
        document_model2 = Document(**document_model_dict)

        # Verify the model instances are equivalent
        assert document_model == document_model2

        # Convert model instance back to dict and verify no loss of data
        document_model_json2 = document_model.to_dict()
        assert document_model_json2 == document_model_json

class TestModel_EffectiveDates():
    """
    Test Class for EffectiveDates
    """

    def test_effective_dates_serialization(self):
        """
        Test serialization/deserialization for EffectiveDates
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a EffectiveDates model
        effective_dates_model_json = {}
        effective_dates_model_json['confidence_level'] = 'High'
        effective_dates_model_json['text'] = 'testString'
        effective_dates_model_json['text_normalized'] = 'testString'
        effective_dates_model_json['provenance_ids'] = ['testString']
        effective_dates_model_json['location'] = location_model

        # Construct a model instance of EffectiveDates by calling from_dict on the json representation
        effective_dates_model = EffectiveDates.from_dict(effective_dates_model_json)
        assert effective_dates_model != False

        # Construct a model instance of EffectiveDates by calling from_dict on the json representation
        effective_dates_model_dict = EffectiveDates.from_dict(effective_dates_model_json).__dict__
        effective_dates_model2 = EffectiveDates(**effective_dates_model_dict)

        # Verify the model instances are equivalent
        assert effective_dates_model == effective_dates_model2

        # Convert model instance back to dict and verify no loss of data
        effective_dates_model_json2 = effective_dates_model.to_dict()
        assert effective_dates_model_json2 == effective_dates_model_json

class TestModel_Element():
    """
    Test Class for Element
    """

    def test_element_serialization(self):
        """
        Test serialization/deserialization for Element
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        # Construct a json representation of a Element model
        element_model_json = {}
        element_model_json['location'] = location_model
        element_model_json['text'] = 'testString'
        element_model_json['types'] = [type_label_model]
        element_model_json['categories'] = [category_model]
        element_model_json['attributes'] = [attribute_model]

        # Construct a model instance of Element by calling from_dict on the json representation
        element_model = Element.from_dict(element_model_json)
        assert element_model != False

        # Construct a model instance of Element by calling from_dict on the json representation
        element_model_dict = Element.from_dict(element_model_json).__dict__
        element_model2 = Element(**element_model_dict)

        # Verify the model instances are equivalent
        assert element_model == element_model2

        # Convert model instance back to dict and verify no loss of data
        element_model_json2 = element_model.to_dict()
        assert element_model_json2 == element_model_json

class TestModel_ElementLocations():
    """
    Test Class for ElementLocations
    """

    def test_element_locations_serialization(self):
        """
        Test serialization/deserialization for ElementLocations
        """

        # Construct a json representation of a ElementLocations model
        element_locations_model_json = {}
        element_locations_model_json['begin'] = 38
        element_locations_model_json['end'] = 38

        # Construct a model instance of ElementLocations by calling from_dict on the json representation
        element_locations_model = ElementLocations.from_dict(element_locations_model_json)
        assert element_locations_model != False

        # Construct a model instance of ElementLocations by calling from_dict on the json representation
        element_locations_model_dict = ElementLocations.from_dict(element_locations_model_json).__dict__
        element_locations_model2 = ElementLocations(**element_locations_model_dict)

        # Verify the model instances are equivalent
        assert element_locations_model == element_locations_model2

        # Convert model instance back to dict and verify no loss of data
        element_locations_model_json2 = element_locations_model.to_dict()
        assert element_locations_model_json2 == element_locations_model_json

class TestModel_ElementPair():
    """
    Test Class for ElementPair
    """

    def test_element_pair_serialization(self):
        """
        Test serialization/deserialization for ElementPair
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_comparison_model = {} # TypeLabelComparison
        type_label_comparison_model['label'] = label_model

        category_comparison_model = {} # CategoryComparison
        category_comparison_model['label'] = 'Amendments'

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        # Construct a json representation of a ElementPair model
        element_pair_model_json = {}
        element_pair_model_json['document_label'] = 'testString'
        element_pair_model_json['text'] = 'testString'
        element_pair_model_json['location'] = location_model
        element_pair_model_json['types'] = [type_label_comparison_model]
        element_pair_model_json['categories'] = [category_comparison_model]
        element_pair_model_json['attributes'] = [attribute_model]

        # Construct a model instance of ElementPair by calling from_dict on the json representation
        element_pair_model = ElementPair.from_dict(element_pair_model_json)
        assert element_pair_model != False

        # Construct a model instance of ElementPair by calling from_dict on the json representation
        element_pair_model_dict = ElementPair.from_dict(element_pair_model_json).__dict__
        element_pair_model2 = ElementPair(**element_pair_model_dict)

        # Verify the model instances are equivalent
        assert element_pair_model == element_pair_model2

        # Convert model instance back to dict and verify no loss of data
        element_pair_model_json2 = element_pair_model.to_dict()
        assert element_pair_model_json2 == element_pair_model_json

class TestModel_FeedbackDataInput():
    """
    Test Class for FeedbackDataInput
    """

    def test_feedback_data_input_serialization(self):
        """
        Test serialization/deserialization for FeedbackDataInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        short_doc_model = {} # ShortDoc
        short_doc_model['title'] = 'testString'
        short_doc_model['hash'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        original_labels_in_model = {} # OriginalLabelsIn
        original_labels_in_model['types'] = [type_label_model]
        original_labels_in_model['categories'] = [category_model]

        updated_labels_in_model = {} # UpdatedLabelsIn
        updated_labels_in_model['types'] = [type_label_model]
        updated_labels_in_model['categories'] = [category_model]

        # Construct a json representation of a FeedbackDataInput model
        feedback_data_input_model_json = {}
        feedback_data_input_model_json['feedback_type'] = 'testString'
        feedback_data_input_model_json['document'] = short_doc_model
        feedback_data_input_model_json['model_id'] = 'testString'
        feedback_data_input_model_json['model_version'] = 'testString'
        feedback_data_input_model_json['location'] = location_model
        feedback_data_input_model_json['text'] = 'testString'
        feedback_data_input_model_json['original_labels'] = original_labels_in_model
        feedback_data_input_model_json['updated_labels'] = updated_labels_in_model

        # Construct a model instance of FeedbackDataInput by calling from_dict on the json representation
        feedback_data_input_model = FeedbackDataInput.from_dict(feedback_data_input_model_json)
        assert feedback_data_input_model != False

        # Construct a model instance of FeedbackDataInput by calling from_dict on the json representation
        feedback_data_input_model_dict = FeedbackDataInput.from_dict(feedback_data_input_model_json).__dict__
        feedback_data_input_model2 = FeedbackDataInput(**feedback_data_input_model_dict)

        # Verify the model instances are equivalent
        assert feedback_data_input_model == feedback_data_input_model2

        # Convert model instance back to dict and verify no loss of data
        feedback_data_input_model_json2 = feedback_data_input_model.to_dict()
        assert feedback_data_input_model_json2 == feedback_data_input_model_json

class TestModel_FeedbackDataOutput():
    """
    Test Class for FeedbackDataOutput
    """

    def test_feedback_data_output_serialization(self):
        """
        Test serialization/deserialization for FeedbackDataOutput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        short_doc_model = {} # ShortDoc
        short_doc_model['title'] = 'testString'
        short_doc_model['hash'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        original_labels_out_model = {} # OriginalLabelsOut
        original_labels_out_model['types'] = [type_label_model]
        original_labels_out_model['categories'] = [category_model]

        updated_labels_out_model = {} # UpdatedLabelsOut
        updated_labels_out_model['types'] = [type_label_model]
        updated_labels_out_model['categories'] = [category_model]

        pagination_model = {} # Pagination
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 26

        # Construct a json representation of a FeedbackDataOutput model
        feedback_data_output_model_json = {}
        feedback_data_output_model_json['feedback_type'] = 'testString'
        feedback_data_output_model_json['document'] = short_doc_model
        feedback_data_output_model_json['model_id'] = 'testString'
        feedback_data_output_model_json['model_version'] = 'testString'
        feedback_data_output_model_json['location'] = location_model
        feedback_data_output_model_json['text'] = 'testString'
        feedback_data_output_model_json['original_labels'] = original_labels_out_model
        feedback_data_output_model_json['updated_labels'] = updated_labels_out_model
        feedback_data_output_model_json['pagination'] = pagination_model

        # Construct a model instance of FeedbackDataOutput by calling from_dict on the json representation
        feedback_data_output_model = FeedbackDataOutput.from_dict(feedback_data_output_model_json)
        assert feedback_data_output_model != False

        # Construct a model instance of FeedbackDataOutput by calling from_dict on the json representation
        feedback_data_output_model_dict = FeedbackDataOutput.from_dict(feedback_data_output_model_json).__dict__
        feedback_data_output_model2 = FeedbackDataOutput(**feedback_data_output_model_dict)

        # Verify the model instances are equivalent
        assert feedback_data_output_model == feedback_data_output_model2

        # Convert model instance back to dict and verify no loss of data
        feedback_data_output_model_json2 = feedback_data_output_model.to_dict()
        assert feedback_data_output_model_json2 == feedback_data_output_model_json

class TestModel_FeedbackDeleted():
    """
    Test Class for FeedbackDeleted
    """

    def test_feedback_deleted_serialization(self):
        """
        Test serialization/deserialization for FeedbackDeleted
        """

        # Construct a json representation of a FeedbackDeleted model
        feedback_deleted_model_json = {}
        feedback_deleted_model_json['status'] = 38
        feedback_deleted_model_json['message'] = 'testString'

        # Construct a model instance of FeedbackDeleted by calling from_dict on the json representation
        feedback_deleted_model = FeedbackDeleted.from_dict(feedback_deleted_model_json)
        assert feedback_deleted_model != False

        # Construct a model instance of FeedbackDeleted by calling from_dict on the json representation
        feedback_deleted_model_dict = FeedbackDeleted.from_dict(feedback_deleted_model_json).__dict__
        feedback_deleted_model2 = FeedbackDeleted(**feedback_deleted_model_dict)

        # Verify the model instances are equivalent
        assert feedback_deleted_model == feedback_deleted_model2

        # Convert model instance back to dict and verify no loss of data
        feedback_deleted_model_json2 = feedback_deleted_model.to_dict()
        assert feedback_deleted_model_json2 == feedback_deleted_model_json

class TestModel_FeedbackList():
    """
    Test Class for FeedbackList
    """

    def test_feedback_list_serialization(self):
        """
        Test serialization/deserialization for FeedbackList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        short_doc_model = {} # ShortDoc
        short_doc_model['title'] = 'Legal Approval SOW'
        short_doc_model['hash'] = 'dcd82f59c6bb1a289a514b611d531191'

        location_model = {} # Location
        location_model['begin'] = 214
        location_model['end'] = 237

        label_model = {} # Label
        label_model['nature'] = 'Obligation'
        label_model['party'] = 'IBM'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['85f5981a-ba91-44f5-9efa-0bd22e64b7bc', 'ce0480a1-5ef1-4c3e-9861-3743b5610795']
        type_label_model['modification'] = 'unchanged'

        category_model = {} # Category
        category_model['label'] = 'Responsibilities'
        category_model['provenance_ids'] = []
        category_model['modification'] = 'unchanged'

        original_labels_out_model = {} # OriginalLabelsOut
        original_labels_out_model['types'] = [type_label_model]
        original_labels_out_model['categories'] = [category_model]

        updated_labels_out_model = {} # UpdatedLabelsOut
        updated_labels_out_model['types'] = [type_label_model]
        updated_labels_out_model['categories'] = [category_model]

        pagination_model = {} # Pagination
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 26

        feedback_data_output_model = {} # FeedbackDataOutput
        feedback_data_output_model['feedback_type'] = 'element_classification'
        feedback_data_output_model['document'] = short_doc_model
        feedback_data_output_model['model_id'] = 'contracts'
        feedback_data_output_model['model_version'] = '10.00'
        feedback_data_output_model['location'] = location_model
        feedback_data_output_model['text'] = '1. IBM will provide a Senior Managing Consultant / expert resource, for up to 80 hours, to assist Florida Power & Light (FPL) with the creation of an IT infrastructure unit cost model for existing infrastructure.'
        feedback_data_output_model['original_labels'] = original_labels_out_model
        feedback_data_output_model['updated_labels'] = updated_labels_out_model
        feedback_data_output_model['pagination'] = pagination_model

        get_feedback_model = {} # GetFeedback
        get_feedback_model['feedback_id'] = '9730b437-cb86-4d40-9a84-ff6948bb3dd1'
        get_feedback_model['created'] = "2018-07-03T15:16:05Z"
        get_feedback_model['comment'] = 'testString'
        get_feedback_model['feedback_data'] = feedback_data_output_model

        # Construct a json representation of a FeedbackList model
        feedback_list_model_json = {}
        feedback_list_model_json['feedback'] = [get_feedback_model]

        # Construct a model instance of FeedbackList by calling from_dict on the json representation
        feedback_list_model = FeedbackList.from_dict(feedback_list_model_json)
        assert feedback_list_model != False

        # Construct a model instance of FeedbackList by calling from_dict on the json representation
        feedback_list_model_dict = FeedbackList.from_dict(feedback_list_model_json).__dict__
        feedback_list_model2 = FeedbackList(**feedback_list_model_dict)

        # Verify the model instances are equivalent
        assert feedback_list_model == feedback_list_model2

        # Convert model instance back to dict and verify no loss of data
        feedback_list_model_json2 = feedback_list_model.to_dict()
        assert feedback_list_model_json2 == feedback_list_model_json

class TestModel_FeedbackReturn():
    """
    Test Class for FeedbackReturn
    """

    def test_feedback_return_serialization(self):
        """
        Test serialization/deserialization for FeedbackReturn
        """

        # Construct dict forms of any model objects needed in order to build this model.

        short_doc_model = {} # ShortDoc
        short_doc_model['title'] = 'testString'
        short_doc_model['hash'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        original_labels_out_model = {} # OriginalLabelsOut
        original_labels_out_model['types'] = [type_label_model]
        original_labels_out_model['categories'] = [category_model]

        updated_labels_out_model = {} # UpdatedLabelsOut
        updated_labels_out_model['types'] = [type_label_model]
        updated_labels_out_model['categories'] = [category_model]

        pagination_model = {} # Pagination
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 26

        feedback_data_output_model = {} # FeedbackDataOutput
        feedback_data_output_model['feedback_type'] = 'testString'
        feedback_data_output_model['document'] = short_doc_model
        feedback_data_output_model['model_id'] = 'testString'
        feedback_data_output_model['model_version'] = 'testString'
        feedback_data_output_model['location'] = location_model
        feedback_data_output_model['text'] = 'testString'
        feedback_data_output_model['original_labels'] = original_labels_out_model
        feedback_data_output_model['updated_labels'] = updated_labels_out_model
        feedback_data_output_model['pagination'] = pagination_model

        # Construct a json representation of a FeedbackReturn model
        feedback_return_model_json = {}
        feedback_return_model_json['feedback_id'] = 'testString'
        feedback_return_model_json['user_id'] = 'testString'
        feedback_return_model_json['comment'] = 'testString'
        feedback_return_model_json['created'] = "2019-01-01T12:00:00Z"
        feedback_return_model_json['feedback_data'] = feedback_data_output_model

        # Construct a model instance of FeedbackReturn by calling from_dict on the json representation
        feedback_return_model = FeedbackReturn.from_dict(feedback_return_model_json)
        assert feedback_return_model != False

        # Construct a model instance of FeedbackReturn by calling from_dict on the json representation
        feedback_return_model_dict = FeedbackReturn.from_dict(feedback_return_model_json).__dict__
        feedback_return_model2 = FeedbackReturn(**feedback_return_model_dict)

        # Verify the model instances are equivalent
        assert feedback_return_model == feedback_return_model2

        # Convert model instance back to dict and verify no loss of data
        feedback_return_model_json2 = feedback_return_model.to_dict()
        assert feedback_return_model_json2 == feedback_return_model_json

class TestModel_GetFeedback():
    """
    Test Class for GetFeedback
    """

    def test_get_feedback_serialization(self):
        """
        Test serialization/deserialization for GetFeedback
        """

        # Construct dict forms of any model objects needed in order to build this model.

        short_doc_model = {} # ShortDoc
        short_doc_model['title'] = 'Legal Approval SOW'
        short_doc_model['hash'] = '4492935afd3673e04082591d163ad68b'

        location_model = {} # Location
        location_model['begin'] = 214
        location_model['end'] = 237

        label_model = {} # Label
        label_model['nature'] = 'Obligation'
        label_model['party'] = 'IBM'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['85f5981a-ba91-44f5-9efa-0bd22e64b7bc', 'ce0480a1-5ef1-4c3e-9861-3743b5610795']
        type_label_model['modification'] = 'unchanged'

        category_model = {} # Category
        category_model['label'] = 'obligation'
        category_model['provenance_ids'] = ['85f5981a-ba91-44f5-9efa-0bd22e64b7bc', 'ce0480a1-5ef1-4c3e-9861-3743b5610795']
        category_model['modification'] = 'removed'

        original_labels_out_model = {} # OriginalLabelsOut
        original_labels_out_model['types'] = [type_label_model]
        original_labels_out_model['categories'] = [category_model]

        updated_labels_out_model = {} # UpdatedLabelsOut
        updated_labels_out_model['types'] = [type_label_model]
        updated_labels_out_model['categories'] = [category_model]

        pagination_model = {} # Pagination
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 26

        feedback_data_output_model = {} # FeedbackDataOutput
        feedback_data_output_model['feedback_type'] = 'element_classification'
        feedback_data_output_model['document'] = short_doc_model
        feedback_data_output_model['model_id'] = 'contracts'
        feedback_data_output_model['model_version'] = '10.00'
        feedback_data_output_model['location'] = location_model
        feedback_data_output_model['text'] = '1. IBM will provide a Senior Managing Consultant / expert resource, for up to 80 hours, to assist Florida Power & Light (FPL) with the creation of an IT infrastructure unit cost model for existing infrastructure.'
        feedback_data_output_model['original_labels'] = original_labels_out_model
        feedback_data_output_model['updated_labels'] = updated_labels_out_model
        feedback_data_output_model['pagination'] = pagination_model

        # Construct a json representation of a GetFeedback model
        get_feedback_model_json = {}
        get_feedback_model_json['feedback_id'] = 'testString'
        get_feedback_model_json['created'] = "2019-01-01T12:00:00Z"
        get_feedback_model_json['comment'] = 'testString'
        get_feedback_model_json['feedback_data'] = feedback_data_output_model

        # Construct a model instance of GetFeedback by calling from_dict on the json representation
        get_feedback_model = GetFeedback.from_dict(get_feedback_model_json)
        assert get_feedback_model != False

        # Construct a model instance of GetFeedback by calling from_dict on the json representation
        get_feedback_model_dict = GetFeedback.from_dict(get_feedback_model_json).__dict__
        get_feedback_model2 = GetFeedback(**get_feedback_model_dict)

        # Verify the model instances are equivalent
        assert get_feedback_model == get_feedback_model2

        # Convert model instance back to dict and verify no loss of data
        get_feedback_model_json2 = get_feedback_model.to_dict()
        assert get_feedback_model_json2 == get_feedback_model_json

class TestModel_HTMLReturn():
    """
    Test Class for HTMLReturn
    """

    def test_html_return_serialization(self):
        """
        Test serialization/deserialization for HTMLReturn
        """

        # Construct a json representation of a HTMLReturn model
        html_return_model_json = {}
        html_return_model_json['num_pages'] = 'testString'
        html_return_model_json['author'] = 'testString'
        html_return_model_json['publication_date'] = 'testString'
        html_return_model_json['title'] = 'testString'
        html_return_model_json['html'] = 'testString'

        # Construct a model instance of HTMLReturn by calling from_dict on the json representation
        html_return_model = HTMLReturn.from_dict(html_return_model_json)
        assert html_return_model != False

        # Construct a model instance of HTMLReturn by calling from_dict on the json representation
        html_return_model_dict = HTMLReturn.from_dict(html_return_model_json).__dict__
        html_return_model2 = HTMLReturn(**html_return_model_dict)

        # Verify the model instances are equivalent
        assert html_return_model == html_return_model2

        # Convert model instance back to dict and verify no loss of data
        html_return_model_json2 = html_return_model.to_dict()
        assert html_return_model_json2 == html_return_model_json

class TestModel_Interpretation():
    """
    Test Class for Interpretation
    """

    def test_interpretation_serialization(self):
        """
        Test serialization/deserialization for Interpretation
        """

        # Construct a json representation of a Interpretation model
        interpretation_model_json = {}
        interpretation_model_json['value'] = 'testString'
        interpretation_model_json['numeric_value'] = 72.5
        interpretation_model_json['unit'] = 'testString'

        # Construct a model instance of Interpretation by calling from_dict on the json representation
        interpretation_model = Interpretation.from_dict(interpretation_model_json)
        assert interpretation_model != False

        # Construct a model instance of Interpretation by calling from_dict on the json representation
        interpretation_model_dict = Interpretation.from_dict(interpretation_model_json).__dict__
        interpretation_model2 = Interpretation(**interpretation_model_dict)

        # Verify the model instances are equivalent
        assert interpretation_model == interpretation_model2

        # Convert model instance back to dict and verify no loss of data
        interpretation_model_json2 = interpretation_model.to_dict()
        assert interpretation_model_json2 == interpretation_model_json

class TestModel_Key():
    """
    Test Class for Key
    """

    def test_key_serialization(self):
        """
        Test serialization/deserialization for Key
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a Key model
        key_model_json = {}
        key_model_json['cell_id'] = 'testString'
        key_model_json['location'] = location_model
        key_model_json['text'] = 'testString'

        # Construct a model instance of Key by calling from_dict on the json representation
        key_model = Key.from_dict(key_model_json)
        assert key_model != False

        # Construct a model instance of Key by calling from_dict on the json representation
        key_model_dict = Key.from_dict(key_model_json).__dict__
        key_model2 = Key(**key_model_dict)

        # Verify the model instances are equivalent
        assert key_model == key_model2

        # Convert model instance back to dict and verify no loss of data
        key_model_json2 = key_model.to_dict()
        assert key_model_json2 == key_model_json

class TestModel_KeyValuePair():
    """
    Test Class for KeyValuePair
    """

    def test_key_value_pair_serialization(self):
        """
        Test serialization/deserialization for KeyValuePair
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        key_model = {} # Key
        key_model['cell_id'] = 'testString'
        key_model['location'] = location_model
        key_model['text'] = 'testString'

        value_model = {} # Value
        value_model['cell_id'] = 'testString'
        value_model['location'] = location_model
        value_model['text'] = 'testString'

        # Construct a json representation of a KeyValuePair model
        key_value_pair_model_json = {}
        key_value_pair_model_json['key'] = key_model
        key_value_pair_model_json['value'] = [value_model]

        # Construct a model instance of KeyValuePair by calling from_dict on the json representation
        key_value_pair_model = KeyValuePair.from_dict(key_value_pair_model_json)
        assert key_value_pair_model != False

        # Construct a model instance of KeyValuePair by calling from_dict on the json representation
        key_value_pair_model_dict = KeyValuePair.from_dict(key_value_pair_model_json).__dict__
        key_value_pair_model2 = KeyValuePair(**key_value_pair_model_dict)

        # Verify the model instances are equivalent
        assert key_value_pair_model == key_value_pair_model2

        # Convert model instance back to dict and verify no loss of data
        key_value_pair_model_json2 = key_value_pair_model.to_dict()
        assert key_value_pair_model_json2 == key_value_pair_model_json

class TestModel_Label():
    """
    Test Class for Label
    """

    def test_label_serialization(self):
        """
        Test serialization/deserialization for Label
        """

        # Construct a json representation of a Label model
        label_model_json = {}
        label_model_json['nature'] = 'testString'
        label_model_json['party'] = 'testString'

        # Construct a model instance of Label by calling from_dict on the json representation
        label_model = Label.from_dict(label_model_json)
        assert label_model != False

        # Construct a model instance of Label by calling from_dict on the json representation
        label_model_dict = Label.from_dict(label_model_json).__dict__
        label_model2 = Label(**label_model_dict)

        # Verify the model instances are equivalent
        assert label_model == label_model2

        # Convert model instance back to dict and verify no loss of data
        label_model_json2 = label_model.to_dict()
        assert label_model_json2 == label_model_json

class TestModel_LeadingSentence():
    """
    Test Class for LeadingSentence
    """

    def test_leading_sentence_serialization(self):
        """
        Test serialization/deserialization for LeadingSentence
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        element_locations_model = {} # ElementLocations
        element_locations_model['begin'] = 38
        element_locations_model['end'] = 38

        # Construct a json representation of a LeadingSentence model
        leading_sentence_model_json = {}
        leading_sentence_model_json['text'] = 'testString'
        leading_sentence_model_json['location'] = location_model
        leading_sentence_model_json['element_locations'] = [element_locations_model]

        # Construct a model instance of LeadingSentence by calling from_dict on the json representation
        leading_sentence_model = LeadingSentence.from_dict(leading_sentence_model_json)
        assert leading_sentence_model != False

        # Construct a model instance of LeadingSentence by calling from_dict on the json representation
        leading_sentence_model_dict = LeadingSentence.from_dict(leading_sentence_model_json).__dict__
        leading_sentence_model2 = LeadingSentence(**leading_sentence_model_dict)

        # Verify the model instances are equivalent
        assert leading_sentence_model == leading_sentence_model2

        # Convert model instance back to dict and verify no loss of data
        leading_sentence_model_json2 = leading_sentence_model.to_dict()
        assert leading_sentence_model_json2 == leading_sentence_model_json

class TestModel_Location():
    """
    Test Class for Location
    """

    def test_location_serialization(self):
        """
        Test serialization/deserialization for Location
        """

        # Construct a json representation of a Location model
        location_model_json = {}
        location_model_json['begin'] = 26
        location_model_json['end'] = 26

        # Construct a model instance of Location by calling from_dict on the json representation
        location_model = Location.from_dict(location_model_json)
        assert location_model != False

        # Construct a model instance of Location by calling from_dict on the json representation
        location_model_dict = Location.from_dict(location_model_json).__dict__
        location_model2 = Location(**location_model_dict)

        # Verify the model instances are equivalent
        assert location_model == location_model2

        # Convert model instance back to dict and verify no loss of data
        location_model_json2 = location_model.to_dict()
        assert location_model_json2 == location_model_json

class TestModel_Mention():
    """
    Test Class for Mention
    """

    def test_mention_serialization(self):
        """
        Test serialization/deserialization for Mention
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a Mention model
        mention_model_json = {}
        mention_model_json['text'] = 'testString'
        mention_model_json['location'] = location_model

        # Construct a model instance of Mention by calling from_dict on the json representation
        mention_model = Mention.from_dict(mention_model_json)
        assert mention_model != False

        # Construct a model instance of Mention by calling from_dict on the json representation
        mention_model_dict = Mention.from_dict(mention_model_json).__dict__
        mention_model2 = Mention(**mention_model_dict)

        # Verify the model instances are equivalent
        assert mention_model == mention_model2

        # Convert model instance back to dict and verify no loss of data
        mention_model_json2 = mention_model.to_dict()
        assert mention_model_json2 == mention_model_json

class TestModel_OriginalLabelsIn():
    """
    Test Class for OriginalLabelsIn
    """

    def test_original_labels_in_serialization(self):
        """
        Test serialization/deserialization for OriginalLabelsIn
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        # Construct a json representation of a OriginalLabelsIn model
        original_labels_in_model_json = {}
        original_labels_in_model_json['types'] = [type_label_model]
        original_labels_in_model_json['categories'] = [category_model]

        # Construct a model instance of OriginalLabelsIn by calling from_dict on the json representation
        original_labels_in_model = OriginalLabelsIn.from_dict(original_labels_in_model_json)
        assert original_labels_in_model != False

        # Construct a model instance of OriginalLabelsIn by calling from_dict on the json representation
        original_labels_in_model_dict = OriginalLabelsIn.from_dict(original_labels_in_model_json).__dict__
        original_labels_in_model2 = OriginalLabelsIn(**original_labels_in_model_dict)

        # Verify the model instances are equivalent
        assert original_labels_in_model == original_labels_in_model2

        # Convert model instance back to dict and verify no loss of data
        original_labels_in_model_json2 = original_labels_in_model.to_dict()
        assert original_labels_in_model_json2 == original_labels_in_model_json

class TestModel_OriginalLabelsOut():
    """
    Test Class for OriginalLabelsOut
    """

    def test_original_labels_out_serialization(self):
        """
        Test serialization/deserialization for OriginalLabelsOut
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        # Construct a json representation of a OriginalLabelsOut model
        original_labels_out_model_json = {}
        original_labels_out_model_json['types'] = [type_label_model]
        original_labels_out_model_json['categories'] = [category_model]

        # Construct a model instance of OriginalLabelsOut by calling from_dict on the json representation
        original_labels_out_model = OriginalLabelsOut.from_dict(original_labels_out_model_json)
        assert original_labels_out_model != False

        # Construct a model instance of OriginalLabelsOut by calling from_dict on the json representation
        original_labels_out_model_dict = OriginalLabelsOut.from_dict(original_labels_out_model_json).__dict__
        original_labels_out_model2 = OriginalLabelsOut(**original_labels_out_model_dict)

        # Verify the model instances are equivalent
        assert original_labels_out_model == original_labels_out_model2

        # Convert model instance back to dict and verify no loss of data
        original_labels_out_model_json2 = original_labels_out_model.to_dict()
        assert original_labels_out_model_json2 == original_labels_out_model_json

class TestModel_Pagination():
    """
    Test Class for Pagination
    """

    def test_pagination_serialization(self):
        """
        Test serialization/deserialization for Pagination
        """

        # Construct a json representation of a Pagination model
        pagination_model_json = {}
        pagination_model_json['refresh_cursor'] = 'testString'
        pagination_model_json['next_cursor'] = 'testString'
        pagination_model_json['refresh_url'] = 'testString'
        pagination_model_json['next_url'] = 'testString'
        pagination_model_json['total'] = 26

        # Construct a model instance of Pagination by calling from_dict on the json representation
        pagination_model = Pagination.from_dict(pagination_model_json)
        assert pagination_model != False

        # Construct a model instance of Pagination by calling from_dict on the json representation
        pagination_model_dict = Pagination.from_dict(pagination_model_json).__dict__
        pagination_model2 = Pagination(**pagination_model_dict)

        # Verify the model instances are equivalent
        assert pagination_model == pagination_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_model_json2 = pagination_model.to_dict()
        assert pagination_model_json2 == pagination_model_json

class TestModel_Paragraphs():
    """
    Test Class for Paragraphs
    """

    def test_paragraphs_serialization(self):
        """
        Test serialization/deserialization for Paragraphs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a Paragraphs model
        paragraphs_model_json = {}
        paragraphs_model_json['location'] = location_model

        # Construct a model instance of Paragraphs by calling from_dict on the json representation
        paragraphs_model = Paragraphs.from_dict(paragraphs_model_json)
        assert paragraphs_model != False

        # Construct a model instance of Paragraphs by calling from_dict on the json representation
        paragraphs_model_dict = Paragraphs.from_dict(paragraphs_model_json).__dict__
        paragraphs_model2 = Paragraphs(**paragraphs_model_dict)

        # Verify the model instances are equivalent
        assert paragraphs_model == paragraphs_model2

        # Convert model instance back to dict and verify no loss of data
        paragraphs_model_json2 = paragraphs_model.to_dict()
        assert paragraphs_model_json2 == paragraphs_model_json

class TestModel_Parties():
    """
    Test Class for Parties
    """

    def test_parties_serialization(self):
        """
        Test serialization/deserialization for Parties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        address_model = {} # Address
        address_model['text'] = 'testString'
        address_model['location'] = location_model

        contact_model = {} # Contact
        contact_model['name'] = 'testString'
        contact_model['role'] = 'testString'

        mention_model = {} # Mention
        mention_model['text'] = 'testString'
        mention_model['location'] = location_model

        # Construct a json representation of a Parties model
        parties_model_json = {}
        parties_model_json['party'] = 'testString'
        parties_model_json['role'] = 'testString'
        parties_model_json['importance'] = 'Primary'
        parties_model_json['addresses'] = [address_model]
        parties_model_json['contacts'] = [contact_model]
        parties_model_json['mentions'] = [mention_model]

        # Construct a model instance of Parties by calling from_dict on the json representation
        parties_model = Parties.from_dict(parties_model_json)
        assert parties_model != False

        # Construct a model instance of Parties by calling from_dict on the json representation
        parties_model_dict = Parties.from_dict(parties_model_json).__dict__
        parties_model2 = Parties(**parties_model_dict)

        # Verify the model instances are equivalent
        assert parties_model == parties_model2

        # Convert model instance back to dict and verify no loss of data
        parties_model_json2 = parties_model.to_dict()
        assert parties_model_json2 == parties_model_json

class TestModel_PaymentTerms():
    """
    Test Class for PaymentTerms
    """

    def test_payment_terms_serialization(self):
        """
        Test serialization/deserialization for PaymentTerms
        """

        # Construct dict forms of any model objects needed in order to build this model.

        interpretation_model = {} # Interpretation
        interpretation_model['value'] = 'testString'
        interpretation_model['numeric_value'] = 72.5
        interpretation_model['unit'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a PaymentTerms model
        payment_terms_model_json = {}
        payment_terms_model_json['confidence_level'] = 'High'
        payment_terms_model_json['text'] = 'testString'
        payment_terms_model_json['text_normalized'] = 'testString'
        payment_terms_model_json['interpretation'] = interpretation_model
        payment_terms_model_json['provenance_ids'] = ['testString']
        payment_terms_model_json['location'] = location_model

        # Construct a model instance of PaymentTerms by calling from_dict on the json representation
        payment_terms_model = PaymentTerms.from_dict(payment_terms_model_json)
        assert payment_terms_model != False

        # Construct a model instance of PaymentTerms by calling from_dict on the json representation
        payment_terms_model_dict = PaymentTerms.from_dict(payment_terms_model_json).__dict__
        payment_terms_model2 = PaymentTerms(**payment_terms_model_dict)

        # Verify the model instances are equivalent
        assert payment_terms_model == payment_terms_model2

        # Convert model instance back to dict and verify no loss of data
        payment_terms_model_json2 = payment_terms_model.to_dict()
        assert payment_terms_model_json2 == payment_terms_model_json

class TestModel_RowHeaders():
    """
    Test Class for RowHeaders
    """

    def test_row_headers_serialization(self):
        """
        Test serialization/deserialization for RowHeaders
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a RowHeaders model
        row_headers_model_json = {}
        row_headers_model_json['cell_id'] = 'testString'
        row_headers_model_json['location'] = location_model
        row_headers_model_json['text'] = 'testString'
        row_headers_model_json['text_normalized'] = 'testString'
        row_headers_model_json['row_index_begin'] = 26
        row_headers_model_json['row_index_end'] = 26
        row_headers_model_json['column_index_begin'] = 26
        row_headers_model_json['column_index_end'] = 26

        # Construct a model instance of RowHeaders by calling from_dict on the json representation
        row_headers_model = RowHeaders.from_dict(row_headers_model_json)
        assert row_headers_model != False

        # Construct a model instance of RowHeaders by calling from_dict on the json representation
        row_headers_model_dict = RowHeaders.from_dict(row_headers_model_json).__dict__
        row_headers_model2 = RowHeaders(**row_headers_model_dict)

        # Verify the model instances are equivalent
        assert row_headers_model == row_headers_model2

        # Convert model instance back to dict and verify no loss of data
        row_headers_model_json2 = row_headers_model.to_dict()
        assert row_headers_model_json2 == row_headers_model_json

class TestModel_SectionTitle():
    """
    Test Class for SectionTitle
    """

    def test_section_title_serialization(self):
        """
        Test serialization/deserialization for SectionTitle
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a SectionTitle model
        section_title_model_json = {}
        section_title_model_json['text'] = 'testString'
        section_title_model_json['location'] = location_model

        # Construct a model instance of SectionTitle by calling from_dict on the json representation
        section_title_model = SectionTitle.from_dict(section_title_model_json)
        assert section_title_model != False

        # Construct a model instance of SectionTitle by calling from_dict on the json representation
        section_title_model_dict = SectionTitle.from_dict(section_title_model_json).__dict__
        section_title_model2 = SectionTitle(**section_title_model_dict)

        # Verify the model instances are equivalent
        assert section_title_model == section_title_model2

        # Convert model instance back to dict and verify no loss of data
        section_title_model_json2 = section_title_model.to_dict()
        assert section_title_model_json2 == section_title_model_json

class TestModel_SectionTitles():
    """
    Test Class for SectionTitles
    """

    def test_section_titles_serialization(self):
        """
        Test serialization/deserialization for SectionTitles
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        element_locations_model = {} # ElementLocations
        element_locations_model['begin'] = 38
        element_locations_model['end'] = 38

        # Construct a json representation of a SectionTitles model
        section_titles_model_json = {}
        section_titles_model_json['text'] = 'testString'
        section_titles_model_json['location'] = location_model
        section_titles_model_json['level'] = 38
        section_titles_model_json['element_locations'] = [element_locations_model]

        # Construct a model instance of SectionTitles by calling from_dict on the json representation
        section_titles_model = SectionTitles.from_dict(section_titles_model_json)
        assert section_titles_model != False

        # Construct a model instance of SectionTitles by calling from_dict on the json representation
        section_titles_model_dict = SectionTitles.from_dict(section_titles_model_json).__dict__
        section_titles_model2 = SectionTitles(**section_titles_model_dict)

        # Verify the model instances are equivalent
        assert section_titles_model == section_titles_model2

        # Convert model instance back to dict and verify no loss of data
        section_titles_model_json2 = section_titles_model.to_dict()
        assert section_titles_model_json2 == section_titles_model_json

class TestModel_ShortDoc():
    """
    Test Class for ShortDoc
    """

    def test_short_doc_serialization(self):
        """
        Test serialization/deserialization for ShortDoc
        """

        # Construct a json representation of a ShortDoc model
        short_doc_model_json = {}
        short_doc_model_json['title'] = 'testString'
        short_doc_model_json['hash'] = 'testString'

        # Construct a model instance of ShortDoc by calling from_dict on the json representation
        short_doc_model = ShortDoc.from_dict(short_doc_model_json)
        assert short_doc_model != False

        # Construct a model instance of ShortDoc by calling from_dict on the json representation
        short_doc_model_dict = ShortDoc.from_dict(short_doc_model_json).__dict__
        short_doc_model2 = ShortDoc(**short_doc_model_dict)

        # Verify the model instances are equivalent
        assert short_doc_model == short_doc_model2

        # Convert model instance back to dict and verify no loss of data
        short_doc_model_json2 = short_doc_model.to_dict()
        assert short_doc_model_json2 == short_doc_model_json

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

class TestModel_TableReturn():
    """
    Test Class for TableReturn
    """

    def test_table_return_serialization(self):
        """
        Test serialization/deserialization for TableReturn
        """

        # Construct dict forms of any model objects needed in order to build this model.

        doc_info_model = {} # DocInfo
        doc_info_model['html'] = 'testString'
        doc_info_model['title'] = 'testString'
        doc_info_model['hash'] = 'testString'

        location_model = {} # Location
        location_model['begin'] = 872
        location_model['end'] = 5879

        section_title_model = {} # SectionTitle
        section_title_model['text'] = 'testString'
        section_title_model['location'] = location_model

        table_title_model = {} # TableTitle
        table_title_model['location'] = location_model
        table_title_model['text'] = 'testString'

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'tableHeader-872-873'
        table_headers_model['location'] = { 'foo': 'bar' }
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 0
        table_headers_model['row_index_end'] = 0
        table_headers_model['column_index_begin'] = 0
        table_headers_model['column_index_end'] = 0

        row_headers_model = {} # RowHeaders
        row_headers_model['cell_id'] = 'rowHeader-2244-2262'
        row_headers_model['location'] = location_model
        row_headers_model['text'] = 'Statutory tax rate'
        row_headers_model['text_normalized'] = 'Statutory tax rate'
        row_headers_model['row_index_begin'] = 2
        row_headers_model['row_index_end'] = 2
        row_headers_model['column_index_begin'] = 0
        row_headers_model['column_index_end'] = 0

        column_headers_model = {} # ColumnHeaders
        column_headers_model['cell_id'] = 'colHeader-1050-1082'
        column_headers_model['location'] = { 'foo': 'bar' }
        column_headers_model['text'] = 'Three months ended September 30,'
        column_headers_model['text_normalized'] = 'Three months ended September 30,'
        column_headers_model['row_index_begin'] = 0
        column_headers_model['row_index_end'] = 0
        column_headers_model['column_index_begin'] = 1
        column_headers_model['column_index_end'] = 2

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        body_cells_model = {} # BodyCells
        body_cells_model['cell_id'] = 'bodyCell-2450-2455'
        body_cells_model['location'] = location_model
        body_cells_model['text'] = '35.0%'
        body_cells_model['row_index_begin'] = 2
        body_cells_model['row_index_end'] = 2
        body_cells_model['column_index_begin'] = 1
        body_cells_model['column_index_end'] = 1
        body_cells_model['row_header_ids'] = ['rowHeader-2244-2262']
        body_cells_model['row_header_texts'] = ['Statutory tax rate']
        body_cells_model['row_header_texts_normalized'] = ['Statutory tax rate']
        body_cells_model['column_header_ids'] = ['colHeader-1050-1082', 'colHeader-1544-1548']
        body_cells_model['column_header_texts'] = ['Three months ended September 30, ', '2005']
        body_cells_model['column_header_texts_normalized'] = ['Three months ended September 30, ', 'Year 1']
        body_cells_model['attributes'] = [attribute_model]

        contexts_model = {} # Contexts
        contexts_model['text'] = 'testString'
        contexts_model['location'] = location_model

        key_model = {} # Key
        key_model['cell_id'] = 'testString'
        key_model['location'] = location_model
        key_model['text'] = 'testString'

        value_model = {} # Value
        value_model['cell_id'] = 'testString'
        value_model['location'] = location_model
        value_model['text'] = 'testString'

        key_value_pair_model = {} # KeyValuePair
        key_value_pair_model['key'] = key_model
        key_value_pair_model['value'] = [value_model]

        tables_model = {} # Tables
        tables_model['location'] = location_model
        tables_model['text'] = '...'
        tables_model['section_title'] = section_title_model
        tables_model['title'] = table_title_model
        tables_model['table_headers'] = [table_headers_model]
        tables_model['row_headers'] = [row_headers_model]
        tables_model['column_headers'] = [column_headers_model]
        tables_model['body_cells'] = [body_cells_model]
        tables_model['contexts'] = [contexts_model]
        tables_model['key_value_pairs'] = [key_value_pair_model]

        # Construct a json representation of a TableReturn model
        table_return_model_json = {}
        table_return_model_json['document'] = doc_info_model
        table_return_model_json['model_id'] = 'testString'
        table_return_model_json['model_version'] = 'testString'
        table_return_model_json['tables'] = [tables_model]

        # Construct a model instance of TableReturn by calling from_dict on the json representation
        table_return_model = TableReturn.from_dict(table_return_model_json)
        assert table_return_model != False

        # Construct a model instance of TableReturn by calling from_dict on the json representation
        table_return_model_dict = TableReturn.from_dict(table_return_model_json).__dict__
        table_return_model2 = TableReturn(**table_return_model_dict)

        # Verify the model instances are equivalent
        assert table_return_model == table_return_model2

        # Convert model instance back to dict and verify no loss of data
        table_return_model_json2 = table_return_model.to_dict()
        assert table_return_model_json2 == table_return_model_json

class TestModel_TableTitle():
    """
    Test Class for TableTitle
    """

    def test_table_title_serialization(self):
        """
        Test serialization/deserialization for TableTitle
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a TableTitle model
        table_title_model_json = {}
        table_title_model_json['location'] = location_model
        table_title_model_json['text'] = 'testString'

        # Construct a model instance of TableTitle by calling from_dict on the json representation
        table_title_model = TableTitle.from_dict(table_title_model_json)
        assert table_title_model != False

        # Construct a model instance of TableTitle by calling from_dict on the json representation
        table_title_model_dict = TableTitle.from_dict(table_title_model_json).__dict__
        table_title_model2 = TableTitle(**table_title_model_dict)

        # Verify the model instances are equivalent
        assert table_title_model == table_title_model2

        # Convert model instance back to dict and verify no loss of data
        table_title_model_json2 = table_title_model.to_dict()
        assert table_title_model_json2 == table_title_model_json

class TestModel_Tables():
    """
    Test Class for Tables
    """

    def test_tables_serialization(self):
        """
        Test serialization/deserialization for Tables
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        section_title_model = {} # SectionTitle
        section_title_model['text'] = 'testString'
        section_title_model['location'] = location_model

        table_title_model = {} # TableTitle
        table_title_model['location'] = location_model
        table_title_model['text'] = 'testString'

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = { 'foo': 'bar' }
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        row_headers_model = {} # RowHeaders
        row_headers_model['cell_id'] = 'testString'
        row_headers_model['location'] = location_model
        row_headers_model['text'] = 'testString'
        row_headers_model['text_normalized'] = 'testString'
        row_headers_model['row_index_begin'] = 26
        row_headers_model['row_index_end'] = 26
        row_headers_model['column_index_begin'] = 26
        row_headers_model['column_index_end'] = 26

        column_headers_model = {} # ColumnHeaders
        column_headers_model['cell_id'] = 'testString'
        column_headers_model['location'] = { 'foo': 'bar' }
        column_headers_model['text'] = 'testString'
        column_headers_model['text_normalized'] = 'testString'
        column_headers_model['row_index_begin'] = 26
        column_headers_model['row_index_end'] = 26
        column_headers_model['column_index_begin'] = 26
        column_headers_model['column_index_end'] = 26

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        body_cells_model = {} # BodyCells
        body_cells_model['cell_id'] = 'testString'
        body_cells_model['location'] = location_model
        body_cells_model['text'] = 'testString'
        body_cells_model['row_index_begin'] = 26
        body_cells_model['row_index_end'] = 26
        body_cells_model['column_index_begin'] = 26
        body_cells_model['column_index_end'] = 26
        body_cells_model['row_header_ids'] = ['testString']
        body_cells_model['row_header_texts'] = ['testString']
        body_cells_model['row_header_texts_normalized'] = ['testString']
        body_cells_model['column_header_ids'] = ['testString']
        body_cells_model['column_header_texts'] = ['testString']
        body_cells_model['column_header_texts_normalized'] = ['testString']
        body_cells_model['attributes'] = [attribute_model]

        contexts_model = {} # Contexts
        contexts_model['text'] = 'testString'
        contexts_model['location'] = location_model

        key_model = {} # Key
        key_model['cell_id'] = 'testString'
        key_model['location'] = location_model
        key_model['text'] = 'testString'

        value_model = {} # Value
        value_model['cell_id'] = 'testString'
        value_model['location'] = location_model
        value_model['text'] = 'testString'

        key_value_pair_model = {} # KeyValuePair
        key_value_pair_model['key'] = key_model
        key_value_pair_model['value'] = [value_model]

        # Construct a json representation of a Tables model
        tables_model_json = {}
        tables_model_json['location'] = location_model
        tables_model_json['text'] = 'testString'
        tables_model_json['section_title'] = section_title_model
        tables_model_json['title'] = table_title_model
        tables_model_json['table_headers'] = [table_headers_model]
        tables_model_json['row_headers'] = [row_headers_model]
        tables_model_json['column_headers'] = [column_headers_model]
        tables_model_json['body_cells'] = [body_cells_model]
        tables_model_json['contexts'] = [contexts_model]
        tables_model_json['key_value_pairs'] = [key_value_pair_model]

        # Construct a model instance of Tables by calling from_dict on the json representation
        tables_model = Tables.from_dict(tables_model_json)
        assert tables_model != False

        # Construct a model instance of Tables by calling from_dict on the json representation
        tables_model_dict = Tables.from_dict(tables_model_json).__dict__
        tables_model2 = Tables(**tables_model_dict)

        # Verify the model instances are equivalent
        assert tables_model == tables_model2

        # Convert model instance back to dict and verify no loss of data
        tables_model_json2 = tables_model.to_dict()
        assert tables_model_json2 == tables_model_json

class TestModel_TerminationDates():
    """
    Test Class for TerminationDates
    """

    def test_termination_dates_serialization(self):
        """
        Test serialization/deserialization for TerminationDates
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a TerminationDates model
        termination_dates_model_json = {}
        termination_dates_model_json['confidence_level'] = 'High'
        termination_dates_model_json['text'] = 'testString'
        termination_dates_model_json['text_normalized'] = 'testString'
        termination_dates_model_json['provenance_ids'] = ['testString']
        termination_dates_model_json['location'] = location_model

        # Construct a model instance of TerminationDates by calling from_dict on the json representation
        termination_dates_model = TerminationDates.from_dict(termination_dates_model_json)
        assert termination_dates_model != False

        # Construct a model instance of TerminationDates by calling from_dict on the json representation
        termination_dates_model_dict = TerminationDates.from_dict(termination_dates_model_json).__dict__
        termination_dates_model2 = TerminationDates(**termination_dates_model_dict)

        # Verify the model instances are equivalent
        assert termination_dates_model == termination_dates_model2

        # Convert model instance back to dict and verify no loss of data
        termination_dates_model_json2 = termination_dates_model.to_dict()
        assert termination_dates_model_json2 == termination_dates_model_json

class TestModel_TypeLabel():
    """
    Test Class for TypeLabel
    """

    def test_type_label_serialization(self):
        """
        Test serialization/deserialization for TypeLabel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        # Construct a json representation of a TypeLabel model
        type_label_model_json = {}
        type_label_model_json['label'] = label_model
        type_label_model_json['provenance_ids'] = ['testString']
        type_label_model_json['modification'] = 'added'

        # Construct a model instance of TypeLabel by calling from_dict on the json representation
        type_label_model = TypeLabel.from_dict(type_label_model_json)
        assert type_label_model != False

        # Construct a model instance of TypeLabel by calling from_dict on the json representation
        type_label_model_dict = TypeLabel.from_dict(type_label_model_json).__dict__
        type_label_model2 = TypeLabel(**type_label_model_dict)

        # Verify the model instances are equivalent
        assert type_label_model == type_label_model2

        # Convert model instance back to dict and verify no loss of data
        type_label_model_json2 = type_label_model.to_dict()
        assert type_label_model_json2 == type_label_model_json

class TestModel_TypeLabelComparison():
    """
    Test Class for TypeLabelComparison
    """

    def test_type_label_comparison_serialization(self):
        """
        Test serialization/deserialization for TypeLabelComparison
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        # Construct a json representation of a TypeLabelComparison model
        type_label_comparison_model_json = {}
        type_label_comparison_model_json['label'] = label_model

        # Construct a model instance of TypeLabelComparison by calling from_dict on the json representation
        type_label_comparison_model = TypeLabelComparison.from_dict(type_label_comparison_model_json)
        assert type_label_comparison_model != False

        # Construct a model instance of TypeLabelComparison by calling from_dict on the json representation
        type_label_comparison_model_dict = TypeLabelComparison.from_dict(type_label_comparison_model_json).__dict__
        type_label_comparison_model2 = TypeLabelComparison(**type_label_comparison_model_dict)

        # Verify the model instances are equivalent
        assert type_label_comparison_model == type_label_comparison_model2

        # Convert model instance back to dict and verify no loss of data
        type_label_comparison_model_json2 = type_label_comparison_model.to_dict()
        assert type_label_comparison_model_json2 == type_label_comparison_model_json

class TestModel_UnalignedElement():
    """
    Test Class for UnalignedElement
    """

    def test_unaligned_element_serialization(self):
        """
        Test serialization/deserialization for UnalignedElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_comparison_model = {} # TypeLabelComparison
        type_label_comparison_model['label'] = label_model

        category_comparison_model = {} # CategoryComparison
        category_comparison_model['label'] = 'Amendments'

        attribute_model = {} # Attribute
        attribute_model['type'] = 'Currency'
        attribute_model['text'] = 'testString'
        attribute_model['location'] = location_model

        # Construct a json representation of a UnalignedElement model
        unaligned_element_model_json = {}
        unaligned_element_model_json['document_label'] = 'testString'
        unaligned_element_model_json['location'] = location_model
        unaligned_element_model_json['text'] = 'testString'
        unaligned_element_model_json['types'] = [type_label_comparison_model]
        unaligned_element_model_json['categories'] = [category_comparison_model]
        unaligned_element_model_json['attributes'] = [attribute_model]

        # Construct a model instance of UnalignedElement by calling from_dict on the json representation
        unaligned_element_model = UnalignedElement.from_dict(unaligned_element_model_json)
        assert unaligned_element_model != False

        # Construct a model instance of UnalignedElement by calling from_dict on the json representation
        unaligned_element_model_dict = UnalignedElement.from_dict(unaligned_element_model_json).__dict__
        unaligned_element_model2 = UnalignedElement(**unaligned_element_model_dict)

        # Verify the model instances are equivalent
        assert unaligned_element_model == unaligned_element_model2

        # Convert model instance back to dict and verify no loss of data
        unaligned_element_model_json2 = unaligned_element_model.to_dict()
        assert unaligned_element_model_json2 == unaligned_element_model_json

class TestModel_UpdatedLabelsIn():
    """
    Test Class for UpdatedLabelsIn
    """

    def test_updated_labels_in_serialization(self):
        """
        Test serialization/deserialization for UpdatedLabelsIn
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        # Construct a json representation of a UpdatedLabelsIn model
        updated_labels_in_model_json = {}
        updated_labels_in_model_json['types'] = [type_label_model]
        updated_labels_in_model_json['categories'] = [category_model]

        # Construct a model instance of UpdatedLabelsIn by calling from_dict on the json representation
        updated_labels_in_model = UpdatedLabelsIn.from_dict(updated_labels_in_model_json)
        assert updated_labels_in_model != False

        # Construct a model instance of UpdatedLabelsIn by calling from_dict on the json representation
        updated_labels_in_model_dict = UpdatedLabelsIn.from_dict(updated_labels_in_model_json).__dict__
        updated_labels_in_model2 = UpdatedLabelsIn(**updated_labels_in_model_dict)

        # Verify the model instances are equivalent
        assert updated_labels_in_model == updated_labels_in_model2

        # Convert model instance back to dict and verify no loss of data
        updated_labels_in_model_json2 = updated_labels_in_model.to_dict()
        assert updated_labels_in_model_json2 == updated_labels_in_model_json

class TestModel_UpdatedLabelsOut():
    """
    Test Class for UpdatedLabelsOut
    """

    def test_updated_labels_out_serialization(self):
        """
        Test serialization/deserialization for UpdatedLabelsOut
        """

        # Construct dict forms of any model objects needed in order to build this model.

        label_model = {} # Label
        label_model['nature'] = 'testString'
        label_model['party'] = 'testString'

        type_label_model = {} # TypeLabel
        type_label_model['label'] = label_model
        type_label_model['provenance_ids'] = ['testString']
        type_label_model['modification'] = 'added'

        category_model = {} # Category
        category_model['label'] = 'Amendments'
        category_model['provenance_ids'] = ['testString']
        category_model['modification'] = 'added'

        # Construct a json representation of a UpdatedLabelsOut model
        updated_labels_out_model_json = {}
        updated_labels_out_model_json['types'] = [type_label_model]
        updated_labels_out_model_json['categories'] = [category_model]

        # Construct a model instance of UpdatedLabelsOut by calling from_dict on the json representation
        updated_labels_out_model = UpdatedLabelsOut.from_dict(updated_labels_out_model_json)
        assert updated_labels_out_model != False

        # Construct a model instance of UpdatedLabelsOut by calling from_dict on the json representation
        updated_labels_out_model_dict = UpdatedLabelsOut.from_dict(updated_labels_out_model_json).__dict__
        updated_labels_out_model2 = UpdatedLabelsOut(**updated_labels_out_model_dict)

        # Verify the model instances are equivalent
        assert updated_labels_out_model == updated_labels_out_model2

        # Convert model instance back to dict and verify no loss of data
        updated_labels_out_model_json2 = updated_labels_out_model.to_dict()
        assert updated_labels_out_model_json2 == updated_labels_out_model_json

class TestModel_Value():
    """
    Test Class for Value
    """

    def test_value_serialization(self):
        """
        Test serialization/deserialization for Value
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['begin'] = 26
        location_model['end'] = 26

        # Construct a json representation of a Value model
        value_model_json = {}
        value_model_json['cell_id'] = 'testString'
        value_model_json['location'] = location_model
        value_model_json['text'] = 'testString'

        # Construct a model instance of Value by calling from_dict on the json representation
        value_model = Value.from_dict(value_model_json)
        assert value_model != False

        # Construct a model instance of Value by calling from_dict on the json representation
        value_model_dict = Value.from_dict(value_model_json).__dict__
        value_model2 = Value(**value_model_dict)

        # Verify the model instances are equivalent
        assert value_model == value_model2

        # Convert model instance back to dict and verify no loss of data
        value_model_json2 = value_model.to_dict()
        assert value_model_json2 == value_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
