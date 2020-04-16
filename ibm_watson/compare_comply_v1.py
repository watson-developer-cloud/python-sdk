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
IBM Watson&trade; Compare and Comply analyzes governing documents to provide details about
critical aspects of the documents.
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
from typing import BinaryIO
from typing import Dict
from typing import List

##############################################################################
# Service
##############################################################################


class CompareComplyV1(BaseService):
    """The Compare Comply V1 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/compare-comply/api'
    DEFAULT_SERVICE_NAME = 'compare_comply'

    def __init__(
            self,
            version: str,
            authenticator: Authenticator = None,
            service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Compare Comply service.

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
    # HTML conversion
    #########################

    def convert_to_html(self,
                        file: BinaryIO,
                        *,
                        file_content_type: str = None,
                        model: str = None,
                        **kwargs) -> 'DetailedResponse':
        """
        Convert document to HTML.

        Converts a document to HTML.

        :param TextIO file: The document to convert.
        :param str file_content_type: (optional) The content type of file.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file is None:
            raise ValueError('file must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='convert_to_html')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        form_data = []
        form_data.append(('file', (None, file, file_content_type or
                                   'application/octet-stream')))

        url = '/v1/html_conversion'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    #########################
    # Element classification
    #########################

    def classify_elements(self,
                          file: BinaryIO,
                          *,
                          file_content_type: str = None,
                          model: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Classify the elements of a document.

        Analyzes the structural and semantic elements of a document.

        :param TextIO file: The document to classify.
        :param str file_content_type: (optional) The content type of file.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file is None:
            raise ValueError('file must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='classify_elements')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        form_data = []
        form_data.append(('file', (None, file, file_content_type or
                                   'application/octet-stream')))

        url = '/v1/element_classification'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    #########################
    # Tables
    #########################

    def extract_tables(self,
                       file: BinaryIO,
                       *,
                       file_content_type: str = None,
                       model: str = None,
                       **kwargs) -> 'DetailedResponse':
        """
        Extract a document's tables.

        Analyzes the tables in a document.

        :param TextIO file: The document on which to run table extraction.
        :param str file_content_type: (optional) The content type of file.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file is None:
            raise ValueError('file must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='extract_tables')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        form_data = []
        form_data.append(('file', (None, file, file_content_type or
                                   'application/octet-stream')))

        url = '/v1/tables'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    #########################
    # Comparison
    #########################

    def compare_documents(self,
                          file_1: BinaryIO,
                          file_2: BinaryIO,
                          *,
                          file_1_content_type: str = None,
                          file_2_content_type: str = None,
                          file_1_label: str = None,
                          file_2_label: str = None,
                          model: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Compare two documents.

        Compares two input documents. Documents must be in the same format.

        :param TextIO file_1: The first document to compare.
        :param TextIO file_2: The second document to compare.
        :param str file_1_content_type: (optional) The content type of file_1.
        :param str file_2_content_type: (optional) The content type of file_2.
        :param str file_1_label: (optional) A text label for the first document.
        :param str file_2_label: (optional) A text label for the second document.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file_1 is None:
            raise ValueError('file_1 must be provided')
        if file_2 is None:
            raise ValueError('file_2 must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='compare_documents')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'file_1_label': file_1_label,
            'file_2_label': file_2_label,
            'model': model
        }

        form_data = []
        form_data.append(('file_1', (None, file_1, file_1_content_type or
                                     'application/octet-stream')))
        form_data.append(('file_2', (None, file_2, file_2_content_type or
                                     'application/octet-stream')))

        url = '/v1/comparison'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    #########################
    # Feedback
    #########################

    def add_feedback(self,
                     feedback_data: 'FeedbackDataInput',
                     *,
                     user_id: str = None,
                     comment: str = None,
                     **kwargs) -> 'DetailedResponse':
        """
        Add feedback.

        Adds feedback in the form of _labels_ from a subject-matter expert (SME) to a
        governing document.
        **Important:** Feedback is not immediately incorporated into the training model,
        nor is it guaranteed to be incorporated at a later date. Instead, submitted
        feedback is used to suggest future updates to the training model.

        :param FeedbackDataInput feedback_data: Feedback data for submission.
        :param str user_id: (optional) An optional string identifying the user.
        :param str comment: (optional) An optional comment on or description of the
               feedback.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if feedback_data is None:
            raise ValueError('feedback_data must be provided')
        feedback_data = self._convert_model(feedback_data)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_feedback')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'feedback_data': feedback_data,
            'user_id': user_id,
            'comment': comment
        }

        url = '/v1/feedback'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def list_feedback(self,
                      *,
                      feedback_type: str = None,
                      before: date = None,
                      after: date = None,
                      document_title: str = None,
                      model_id: str = None,
                      model_version: str = None,
                      category_removed: str = None,
                      category_added: str = None,
                      category_not_changed: str = None,
                      type_removed: str = None,
                      type_added: str = None,
                      type_not_changed: str = None,
                      page_limit: int = None,
                      cursor: str = None,
                      sort: str = None,
                      include_total: bool = None,
                      **kwargs) -> 'DetailedResponse':
        """
        List the feedback in a document.

        Lists the feedback in a document.

        :param str feedback_type: (optional) An optional string that filters the
               output to include only feedback with the specified feedback type. The only
               permitted value is `element_classification`.
        :param date before: (optional) An optional string in the format
               `YYYY-MM-DD` that filters the output to include only feedback that was
               added before the specified date.
        :param date after: (optional) An optional string in the format `YYYY-MM-DD`
               that filters the output to include only feedback that was added after the
               specified date.
        :param str document_title: (optional) An optional string that filters the
               output to include only feedback from the document with the specified
               `document_title`.
        :param str model_id: (optional) An optional string that filters the output
               to include only feedback with the specified `model_id`. The only permitted
               value is `contracts`.
        :param str model_version: (optional) An optional string that filters the
               output to include only feedback with the specified `model_version`.
        :param str category_removed: (optional) An optional string in the form of a
               comma-separated list of categories. If it is specified, the service filters
               the output to include only feedback that has at least one category from the
               list removed.
        :param str category_added: (optional) An optional string in the form of a
               comma-separated list of categories. If this is specified, the service
               filters the output to include only feedback that has at least one category
               from the list added.
        :param str category_not_changed: (optional) An optional string in the form
               of a comma-separated list of categories. If this is specified, the service
               filters the output to include only feedback that has at least one category
               from the list unchanged.
        :param str type_removed: (optional) An optional string of comma-separated
               `nature`:`party` pairs. If this is specified, the service filters the
               output to include only feedback that has at least one `nature`:`party` pair
               from the list removed.
        :param str type_added: (optional) An optional string of comma-separated
               `nature`:`party` pairs. If this is specified, the service filters the
               output to include only feedback that has at least one `nature`:`party` pair
               from the list removed.
        :param str type_not_changed: (optional) An optional string of
               comma-separated `nature`:`party` pairs. If this is specified, the service
               filters the output to include only feedback that has at least one
               `nature`:`party` pair from the list unchanged.
        :param int page_limit: (optional) An optional integer specifying the number
               of documents that you want the service to return.
        :param str cursor: (optional) An optional string that returns the set of
               documents after the previous set. Use this parameter with the `page_limit`
               parameter.
        :param str sort: (optional) An optional comma-separated list of fields in
               the document to sort on. You can optionally specify the sort direction by
               prefixing the value of the field with `-` for descending order or `+` for
               ascending order (the default). Currently permitted sorting fields are
               `created`, `user_id`, and `document_title`.
        :param bool include_total: (optional) An optional boolean value. If
               specified as `true`, the `pagination` object in the output includes a value
               called `total` that gives the total count of feedback created.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_feedback')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'feedback_type': feedback_type,
            'before': before,
            'after': after,
            'document_title': document_title,
            'model_id': model_id,
            'model_version': model_version,
            'category_removed': category_removed,
            'category_added': category_added,
            'category_not_changed': category_not_changed,
            'type_removed': type_removed,
            'type_added': type_added,
            'type_not_changed': type_not_changed,
            'page_limit': page_limit,
            'cursor': cursor,
            'sort': sort,
            'include_total': include_total
        }

        url = '/v1/feedback'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_feedback(self,
                     feedback_id: str,
                     *,
                     model: str = None,
                     **kwargs) -> 'DetailedResponse':
        """
        Get a specified feedback entry.

        Gets a feedback entry with a specified `feedback_id`.

        :param str feedback_id: A string that specifies the feedback entry to be
               included in the output.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if feedback_id is None:
            raise ValueError('feedback_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_feedback')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        url = '/v1/feedback/{0}'.format(*self._encode_path_vars(feedback_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def delete_feedback(self,
                        feedback_id: str,
                        *,
                        model: str = None,
                        **kwargs) -> 'DetailedResponse':
        """
        Delete a specified feedback entry.

        Deletes a feedback entry with a specified `feedback_id`.

        :param str feedback_id: A string that specifies the feedback entry to be
               deleted from the document.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if feedback_id is None:
            raise ValueError('feedback_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_feedback')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        url = '/v1/feedback/{0}'.format(*self._encode_path_vars(feedback_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Batches
    #########################

    def create_batch(self,
                     function: str,
                     input_credentials_file: BinaryIO,
                     input_bucket_location: str,
                     input_bucket_name: str,
                     output_credentials_file: BinaryIO,
                     output_bucket_location: str,
                     output_bucket_name: str,
                     *,
                     model: str = None,
                     **kwargs) -> 'DetailedResponse':
        """
        Submit a batch-processing request.

        Run Compare and Comply methods over a collection of input documents.
        **Important:** Batch processing requires the use of the [IBM Cloud Object Storage
        service](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-about#about-ibm-cloud-object-storage).
        The use of IBM Cloud Object Storage with Compare and Comply is discussed at [Using
        batch
        processing](https://cloud.ibm.com/docs/compare-comply?topic=compare-comply-batching#before-you-batch).

        :param str function: The Compare and Comply method to run across the
               submitted input documents.
        :param TextIO input_credentials_file: A JSON file containing the input
               Cloud Object Storage credentials. At a minimum, the credentials must enable
               `READ` permissions on the bucket defined by the `input_bucket_name`
               parameter.
        :param str input_bucket_location: The geographical location of the Cloud
               Object Storage input bucket as listed on the **Endpoint** tab of your Cloud
               Object Storage instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
        :param str input_bucket_name: The name of the Cloud Object Storage input
               bucket.
        :param TextIO output_credentials_file: A JSON file that lists the Cloud
               Object Storage output credentials. At a minimum, the credentials must
               enable `READ` and `WRITE` permissions on the bucket defined by the
               `output_bucket_name` parameter.
        :param str output_bucket_location: The geographical location of the Cloud
               Object Storage output bucket as listed on the **Endpoint** tab of your
               Cloud Object Storage instance; for example, `us-geo`, `eu-geo`, or
               `ap-geo`.
        :param str output_bucket_name: The name of the Cloud Object Storage output
               bucket.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if function is None:
            raise ValueError('function must be provided')
        if input_credentials_file is None:
            raise ValueError('input_credentials_file must be provided')
        if input_bucket_location is None:
            raise ValueError('input_bucket_location must be provided')
        if input_bucket_name is None:
            raise ValueError('input_bucket_name must be provided')
        if output_credentials_file is None:
            raise ValueError('output_credentials_file must be provided')
        if output_bucket_location is None:
            raise ValueError('output_bucket_location must be provided')
        if output_bucket_name is None:
            raise ValueError('output_bucket_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_batch')
        headers.update(sdk_headers)

        params = {'version': self.version, 'function': function, 'model': model}

        form_data = []
        form_data.append(('input_credentials_file',
                          (None, input_credentials_file, 'application/json')))
        input_bucket_location = str(input_bucket_location)
        form_data.append(('input_bucket_location', (None, input_bucket_location,
                                                    'text/plain')))
        input_bucket_name = str(input_bucket_name)
        form_data.append(
            ('input_bucket_name', (None, input_bucket_name, 'text/plain')))
        form_data.append(('output_credentials_file',
                          (None, output_credentials_file, 'application/json')))
        output_bucket_location = str(output_bucket_location)
        form_data.append(('output_bucket_location',
                          (None, output_bucket_location, 'text/plain')))
        output_bucket_name = str(output_bucket_name)
        form_data.append(
            ('output_bucket_name', (None, output_bucket_name, 'text/plain')))

        url = '/v1/batches'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    def list_batches(self, **kwargs) -> 'DetailedResponse':
        """
        List submitted batch-processing jobs.

        Lists batch-processing jobs submitted by users.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_batches')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/batches'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_batch(self, batch_id: str, **kwargs) -> 'DetailedResponse':
        """
        Get information about a specific batch-processing job.

        Gets information about a batch-processing job with a specified ID.

        :param str batch_id: The ID of the batch-processing job whose information
               you want to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if batch_id is None:
            raise ValueError('batch_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_batch')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/batches/{0}'.format(*self._encode_path_vars(batch_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_batch(self,
                     batch_id: str,
                     action: str,
                     *,
                     model: str = None,
                     **kwargs) -> 'DetailedResponse':
        """
        Update a pending or active batch-processing job.

        Updates a pending or active batch-processing job. You can rescan the input bucket
        to check for new documents or cancel a job.

        :param str batch_id: The ID of the batch-processing job you want to update.
        :param str action: The action you want to perform on the specified
               batch-processing job.
        :param str model: (optional) The analysis model to be used by the service.
               For the **Element classification** and **Compare two documents** methods,
               the default is `contracts`. For the **Extract tables** method, the default
               is `tables`. These defaults apply to the standalone methods as well as to
               the methods' use in batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if batch_id is None:
            raise ValueError('batch_id must be provided')
        if action is None:
            raise ValueError('action must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_batch')
        headers.update(sdk_headers)

        params = {'version': self.version, 'action': action, 'model': model}

        url = '/v1/batches/{0}'.format(*self._encode_path_vars(batch_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class ConvertToHtmlEnums(object):

    class FileContentType(Enum):
        """
        The content type of file.
        """
        APPLICATION_PDF = 'application/pdf'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        IMAGE_BMP = 'image/bmp'
        IMAGE_GIF = 'image/gif'
        IMAGE_JPEG = 'image/jpeg'
        IMAGE_PNG = 'image/png'
        IMAGE_TIFF = 'image/tiff'
        TEXT_PLAIN = 'text/plain'

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


class ClassifyElementsEnums(object):

    class FileContentType(Enum):
        """
        The content type of file.
        """
        APPLICATION_PDF = 'application/pdf'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        IMAGE_BMP = 'image/bmp'
        IMAGE_GIF = 'image/gif'
        IMAGE_JPEG = 'image/jpeg'
        IMAGE_PNG = 'image/png'
        IMAGE_TIFF = 'image/tiff'

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


class ExtractTablesEnums(object):

    class FileContentType(Enum):
        """
        The content type of file.
        """
        APPLICATION_PDF = 'application/pdf'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        IMAGE_BMP = 'image/bmp'
        IMAGE_GIF = 'image/gif'
        IMAGE_JPEG = 'image/jpeg'
        IMAGE_PNG = 'image/png'
        IMAGE_TIFF = 'image/tiff'
        TEXT_PLAIN = 'text/plain'

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


class CompareDocumentsEnums(object):

    class File1ContentType(Enum):
        """
        The content type of file_1.
        """
        APPLICATION_PDF = 'application/pdf'
        APPLICATION_JSON = 'application/json'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        IMAGE_BMP = 'image/bmp'
        IMAGE_GIF = 'image/gif'
        IMAGE_JPEG = 'image/jpeg'
        IMAGE_PNG = 'image/png'
        IMAGE_TIFF = 'image/tiff'

    class File2ContentType(Enum):
        """
        The content type of file_2.
        """
        APPLICATION_PDF = 'application/pdf'
        APPLICATION_JSON = 'application/json'
        APPLICATION_MSWORD = 'application/msword'
        APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        IMAGE_BMP = 'image/bmp'
        IMAGE_GIF = 'image/gif'
        IMAGE_JPEG = 'image/jpeg'
        IMAGE_PNG = 'image/png'
        IMAGE_TIFF = 'image/tiff'

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


class GetFeedbackEnums(object):

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


class DeleteFeedbackEnums(object):

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


class CreateBatchEnums(object):

    class Function(Enum):
        """
        The Compare and Comply method to run across the submitted input documents.
        """
        HTML_CONVERSION = 'html_conversion'
        ELEMENT_CLASSIFICATION = 'element_classification'
        TABLES = 'tables'

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


class UpdateBatchEnums(object):

    class Action(Enum):
        """
        The action you want to perform on the specified batch-processing job.
        """
        RESCAN = 'rescan'
        CANCEL = 'cancel'

    class Model(Enum):
        """
        The analysis model to be used by the service. For the **Element classification**
        and **Compare two documents** methods, the default is `contracts`. For the
        **Extract tables** method, the default is `tables`. These defaults apply to the
        standalone methods as well as to the methods' use in batch-processing requests.
        """
        CONTRACTS = 'contracts'
        TABLES = 'tables'


##############################################################################
# Models
##############################################################################


class Address():
    """
    A party's address.

    :attr str text: (optional) A string listing the address.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a Address object.

        :param str text: (optional) A string listing the address.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Address':
        """Initialize a Address object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Address: ' +
                ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Address object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Address object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Address') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Address') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AlignedElement():
    """
    AlignedElement.

    :attr List[ElementPair] element_pair: (optional) Identifies two elements that
          semantically align between the compared documents.
    :attr bool identical_text: (optional) Specifies whether the aligned element is
          identical. Elements are considered identical despite minor differences such as
          leading punctuation, end-of-sentence punctuation, whitespace, the presence or
          absence of definite or indefinite articles, and others.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr bool significant_elements: (optional) Indicates that the elements aligned
          are contractual clauses of significance.
    """

    def __init__(self,
                 *,
                 element_pair: List['ElementPair'] = None,
                 identical_text: bool = None,
                 provenance_ids: List[str] = None,
                 significant_elements: bool = None) -> None:
        """
        Initialize a AlignedElement object.

        :param List[ElementPair] element_pair: (optional) Identifies two elements
               that semantically align between the compared documents.
        :param bool identical_text: (optional) Specifies whether the aligned
               element is identical. Elements are considered identical despite minor
               differences such as leading punctuation, end-of-sentence punctuation,
               whitespace, the presence or absence of definite or indefinite articles, and
               others.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param bool significant_elements: (optional) Indicates that the elements
               aligned are contractual clauses of significance.
        """
        self.element_pair = element_pair
        self.identical_text = identical_text
        self.provenance_ids = provenance_ids
        self.significant_elements = significant_elements

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlignedElement':
        """Initialize a AlignedElement object from a json dictionary."""
        args = {}
        valid_keys = [
            'element_pair', 'identical_text', 'provenance_ids',
            'significant_elements'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AlignedElement: '
                + ', '.join(bad_keys))
        if 'element_pair' in _dict:
            args['element_pair'] = [
                ElementPair._from_dict(x) for x in (_dict.get('element_pair'))
            ]
        if 'identical_text' in _dict:
            args['identical_text'] = _dict.get('identical_text')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'significant_elements' in _dict:
            args['significant_elements'] = _dict.get('significant_elements')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlignedElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'element_pair') and self.element_pair is not None:
            _dict['element_pair'] = [x._to_dict() for x in self.element_pair]
        if hasattr(self, 'identical_text') and self.identical_text is not None:
            _dict['identical_text'] = self.identical_text
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'significant_elements'
                  ) and self.significant_elements is not None:
            _dict['significant_elements'] = self.significant_elements
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AlignedElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'AlignedElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlignedElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Attribute():
    """
    List of document attributes.

    :attr str type: (optional) The type of attribute.
    :attr str text: (optional) The text associated with the attribute.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 text: str = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a Attribute object.

        :param str type: (optional) The type of attribute.
        :param str text: (optional) The text associated with the attribute.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.type = type
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Attribute':
        """Initialize a Attribute object from a json dictionary."""
        args = {}
        valid_keys = ['type', 'text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Attribute: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Attribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Attribute object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Attribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Attribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        The type of attribute.
        """
        CURRENCY = "Currency"
        DATETIME = "DateTime"
        DEFINEDTERM = "DefinedTerm"
        DURATION = "Duration"
        LOCATION = "Location"
        NUMBER = "Number"
        ORGANIZATION = "Organization"
        PERCENTAGE = "Percentage"
        PERSON = "Person"


class BatchStatus():
    """
    The batch-request status.

    :attr str function: (optional) The method to be run against the documents.
          Possible values are `html_conversion`, `element_classification`, and `tables`.
    :attr str input_bucket_location: (optional) The geographical location of the
          Cloud Object Storage input bucket as listed on the **Endpoint** tab of your COS
          instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
    :attr str input_bucket_name: (optional) The name of the Cloud Object Storage
          input bucket.
    :attr str output_bucket_location: (optional) The geographical location of the
          Cloud Object Storage output bucket as listed on the **Endpoint** tab of your COS
          instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
    :attr str output_bucket_name: (optional) The name of the Cloud Object Storage
          output bucket.
    :attr str batch_id: (optional) The unique identifier for the batch request.
    :attr DocCounts document_counts: (optional) Document counts.
    :attr str status: (optional) The status of the batch request.
    :attr datetime created: (optional) The creation time of the batch request.
    :attr datetime updated: (optional) The time of the most recent update to the
          batch request.
    """

    def __init__(self,
                 *,
                 function: str = None,
                 input_bucket_location: str = None,
                 input_bucket_name: str = None,
                 output_bucket_location: str = None,
                 output_bucket_name: str = None,
                 batch_id: str = None,
                 document_counts: 'DocCounts' = None,
                 status: str = None,
                 created: datetime = None,
                 updated: datetime = None) -> None:
        """
        Initialize a BatchStatus object.

        :param str function: (optional) The method to be run against the documents.
               Possible values are `html_conversion`, `element_classification`, and
               `tables`.
        :param str input_bucket_location: (optional) The geographical location of
               the Cloud Object Storage input bucket as listed on the **Endpoint** tab of
               your COS instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
        :param str input_bucket_name: (optional) The name of the Cloud Object
               Storage input bucket.
        :param str output_bucket_location: (optional) The geographical location of
               the Cloud Object Storage output bucket as listed on the **Endpoint** tab of
               your COS instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
        :param str output_bucket_name: (optional) The name of the Cloud Object
               Storage output bucket.
        :param str batch_id: (optional) The unique identifier for the batch
               request.
        :param DocCounts document_counts: (optional) Document counts.
        :param str status: (optional) The status of the batch request.
        :param datetime created: (optional) The creation time of the batch request.
        :param datetime updated: (optional) The time of the most recent update to
               the batch request.
        """
        self.function = function
        self.input_bucket_location = input_bucket_location
        self.input_bucket_name = input_bucket_name
        self.output_bucket_location = output_bucket_location
        self.output_bucket_name = output_bucket_name
        self.batch_id = batch_id
        self.document_counts = document_counts
        self.status = status
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BatchStatus':
        """Initialize a BatchStatus object from a json dictionary."""
        args = {}
        valid_keys = [
            'function', 'input_bucket_location', 'input_bucket_name',
            'output_bucket_location', 'output_bucket_name', 'batch_id',
            'document_counts', 'status', 'created', 'updated'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class BatchStatus: '
                + ', '.join(bad_keys))
        if 'function' in _dict:
            args['function'] = _dict.get('function')
        if 'input_bucket_location' in _dict:
            args['input_bucket_location'] = _dict.get('input_bucket_location')
        if 'input_bucket_name' in _dict:
            args['input_bucket_name'] = _dict.get('input_bucket_name')
        if 'output_bucket_location' in _dict:
            args['output_bucket_location'] = _dict.get('output_bucket_location')
        if 'output_bucket_name' in _dict:
            args['output_bucket_name'] = _dict.get('output_bucket_name')
        if 'batch_id' in _dict:
            args['batch_id'] = _dict.get('batch_id')
        if 'document_counts' in _dict:
            args['document_counts'] = DocCounts._from_dict(
                _dict.get('document_counts'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BatchStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'function') and self.function is not None:
            _dict['function'] = self.function
        if hasattr(self, 'input_bucket_location'
                  ) and self.input_bucket_location is not None:
            _dict['input_bucket_location'] = self.input_bucket_location
        if hasattr(self,
                   'input_bucket_name') and self.input_bucket_name is not None:
            _dict['input_bucket_name'] = self.input_bucket_name
        if hasattr(self, 'output_bucket_location'
                  ) and self.output_bucket_location is not None:
            _dict['output_bucket_location'] = self.output_bucket_location
        if hasattr(
                self,
                'output_bucket_name') and self.output_bucket_name is not None:
            _dict['output_bucket_name'] = self.output_bucket_name
        if hasattr(self, 'batch_id') and self.batch_id is not None:
            _dict['batch_id'] = self.batch_id
        if hasattr(self,
                   'document_counts') and self.document_counts is not None:
            _dict['document_counts'] = self.document_counts._to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BatchStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'BatchStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BatchStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class FunctionEnum(Enum):
        """
        The method to be run against the documents. Possible values are `html_conversion`,
        `element_classification`, and `tables`.
        """
        ELEMENT_CLASSIFICATION = "element_classification"
        HTML_CONVERSION = "html_conversion"
        TABLES = "tables"


class Batches():
    """
    The results of a successful **List Batches** request.

    :attr List[BatchStatus] batches: (optional) A list of the status of all batch
          requests.
    """

    def __init__(self, *, batches: List['BatchStatus'] = None) -> None:
        """
        Initialize a Batches object.

        :param List[BatchStatus] batches: (optional) A list of the status of all
               batch requests.
        """
        self.batches = batches

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Batches':
        """Initialize a Batches object from a json dictionary."""
        args = {}
        valid_keys = ['batches']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Batches: ' +
                ', '.join(bad_keys))
        if 'batches' in _dict:
            args['batches'] = [
                BatchStatus._from_dict(x) for x in (_dict.get('batches'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Batches object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'batches') and self.batches is not None:
            _dict['batches'] = [x._to_dict() for x in self.batches]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Batches object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Batches') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Batches') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BodyCells():
    """
    Cells that are not table header, column header, or row header cells.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
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
    :attr List[str] row_header_ids: (optional) An array that contains the `id` value
          of a row header that is applicable to this body cell.
    :attr List[str] row_header_texts: (optional) An array that contains the `text`
          value of a row header that is applicable to this body cell.
    :attr List[str] row_header_texts_normalized: (optional) If you provide
          customization input, the normalized version of the row header texts according to
          the customization; otherwise, the same value as `row_header_texts`.
    :attr List[str] column_header_ids: (optional) An array that contains the `id`
          value of a column header that is applicable to the current cell.
    :attr List[str] column_header_texts: (optional) An array that contains the
          `text` value of a column header that is applicable to the current cell.
    :attr List[str] column_header_texts_normalized: (optional) If you provide
          customization input, the normalized version of the column header texts according
          to the customization; otherwise, the same value as `column_header_texts`.
    :attr List[Attribute] attributes: (optional)
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: 'Location' = None,
                 text: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None,
                 row_header_ids: List[str] = None,
                 row_header_texts: List[str] = None,
                 row_header_texts_normalized: List[str] = None,
                 column_header_ids: List[str] = None,
                 column_header_texts: List[str] = None,
                 column_header_texts_normalized: List[str] = None,
                 attributes: List['Attribute'] = None) -> None:
        """
        Initialize a BodyCells object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
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
        :param List[str] row_header_ids: (optional) An array that contains the `id`
               value of a row header that is applicable to this body cell.
        :param List[str] row_header_texts: (optional) An array that contains the
               `text` value of a row header that is applicable to this body cell.
        :param List[str] row_header_texts_normalized: (optional) If you provide
               customization input, the normalized version of the row header texts
               according to the customization; otherwise, the same value as
               `row_header_texts`.
        :param List[str] column_header_ids: (optional) An array that contains the
               `id` value of a column header that is applicable to the current cell.
        :param List[str] column_header_texts: (optional) An array that contains the
               `text` value of a column header that is applicable to the current cell.
        :param List[str] column_header_texts_normalized: (optional) If you provide
               customization input, the normalized version of the column header texts
               according to the customization; otherwise, the same value as
               `column_header_texts`.
        :param List[Attribute] attributes: (optional)
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
    def from_dict(cls, _dict: Dict) -> 'BodyCells':
        """Initialize a BodyCells object from a json dictionary."""
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
                'Unrecognized keys detected in dictionary for class BodyCells: '
                + ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
            args['row_header_ids'] = _dict.get('row_header_ids')
        if 'row_header_texts' in _dict:
            args['row_header_texts'] = _dict.get('row_header_texts')
        if 'row_header_texts_normalized' in _dict:
            args['row_header_texts_normalized'] = _dict.get(
                'row_header_texts_normalized')
        if 'column_header_ids' in _dict:
            args['column_header_ids'] = _dict.get('column_header_ids')
        if 'column_header_texts' in _dict:
            args['column_header_texts'] = _dict.get('column_header_texts')
        if 'column_header_texts_normalized' in _dict:
            args['column_header_texts_normalized'] = _dict.get(
                'column_header_texts_normalized')
        if 'attributes' in _dict:
            args['attributes'] = [
                Attribute._from_dict(x) for x in (_dict.get('attributes'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BodyCells object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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
            _dict['row_header_ids'] = self.row_header_ids
        if hasattr(self,
                   'row_header_texts') and self.row_header_texts is not None:
            _dict['row_header_texts'] = self.row_header_texts
        if hasattr(self, 'row_header_texts_normalized'
                  ) and self.row_header_texts_normalized is not None:
            _dict[
                'row_header_texts_normalized'] = self.row_header_texts_normalized
        if hasattr(self,
                   'column_header_ids') and self.column_header_ids is not None:
            _dict['column_header_ids'] = self.column_header_ids
        if hasattr(
                self,
                'column_header_texts') and self.column_header_texts is not None:
            _dict['column_header_texts'] = self.column_header_texts
        if hasattr(self, 'column_header_texts_normalized'
                  ) and self.column_header_texts_normalized is not None:
            _dict[
                'column_header_texts_normalized'] = self.column_header_texts_normalized
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x._to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BodyCells object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'BodyCells') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BodyCells') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Category():
    """
    Information defining an element's subject matter.

    :attr str label: (optional) The category of the associated element.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    """

    def __init__(self,
                 *,
                 label: str = None,
                 provenance_ids: List[str] = None) -> None:
        """
        Initialize a Category object.

        :param str label: (optional) The category of the associated element.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        """
        self.label = label
        self.provenance_ids = provenance_ids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Category':
        """Initialize a Category object from a json dictionary."""
        args = {}
        valid_keys = ['label', 'provenance_ids']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Category: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Category object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Category object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Category') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Category') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LabelEnum(Enum):
        """
        The category of the associated element.
        """
        AMENDMENTS = "Amendments"
        ASSET_USE = "Asset Use"
        ASSIGNMENTS = "Assignments"
        AUDITS = "Audits"
        BUSINESS_CONTINUITY = "Business Continuity"
        COMMUNICATION = "Communication"
        CONFIDENTIALITY = "Confidentiality"
        DELIVERABLES = "Deliverables"
        DELIVERY = "Delivery"
        DISPUTE_RESOLUTION = "Dispute Resolution"
        FORCE_MAJEURE = "Force Majeure"
        INDEMNIFICATION = "Indemnification"
        INSURANCE = "Insurance"
        INTELLECTUAL_PROPERTY = "Intellectual Property"
        LIABILITY = "Liability"
        ORDER_OF_PRECEDENCE = "Order of Precedence"
        PAYMENT_TERMS_BILLING = "Payment Terms & Billing"
        PRICING_TAXES = "Pricing & Taxes"
        PRIVACY = "Privacy"
        RESPONSIBILITIES = "Responsibilities"
        SAFETY_AND_SECURITY = "Safety and Security"
        SCOPE_OF_WORK = "Scope of Work"
        SUBCONTRACTS = "Subcontracts"
        TERM_TERMINATION = "Term & Termination"
        WARRANTIES = "Warranties"


class CategoryComparison():
    """
    Information defining an element's subject matter.

    :attr str label: (optional) The category of the associated element.
    """

    def __init__(self, *, label: str = None) -> None:
        """
        Initialize a CategoryComparison object.

        :param str label: (optional) The category of the associated element.
        """
        self.label = label

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoryComparison':
        """Initialize a CategoryComparison object from a json dictionary."""
        args = {}
        valid_keys = ['label']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CategoryComparison: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoryComparison object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoryComparison object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CategoryComparison') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoryComparison') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LabelEnum(Enum):
        """
        The category of the associated element.
        """
        AMENDMENTS = "Amendments"
        ASSET_USE = "Asset Use"
        ASSIGNMENTS = "Assignments"
        AUDITS = "Audits"
        BUSINESS_CONTINUITY = "Business Continuity"
        COMMUNICATION = "Communication"
        CONFIDENTIALITY = "Confidentiality"
        DELIVERABLES = "Deliverables"
        DELIVERY = "Delivery"
        DISPUTE_RESOLUTION = "Dispute Resolution"
        FORCE_MAJEURE = "Force Majeure"
        INDEMNIFICATION = "Indemnification"
        INSURANCE = "Insurance"
        INTELLECTUAL_PROPERTY = "Intellectual Property"
        LIABILITY = "Liability"
        ORDER_OF_PRECEDENCE = "Order of Precedence"
        PAYMENT_TERMS_BILLING = "Payment Terms & Billing"
        PRICING_TAXES = "Pricing & Taxes"
        PRIVACY = "Privacy"
        RESPONSIBILITIES = "Responsibilities"
        SAFETY_AND_SECURITY = "Safety and Security"
        SCOPE_OF_WORK = "Scope of Work"
        SUBCONTRACTS = "Subcontracts"
        TERM_TERMINATION = "Term & Termination"
        WARRANTIES = "Warranties"


class ClassifyReturn():
    """
    The analysis of objects returned by the **Element classification** method.

    :attr Document document: (optional) Basic information about the input document.
    :attr str model_id: (optional) The analysis model used to classify the input
          document. For the **Element classification** method, the only valid value is
          `contracts`.
    :attr str model_version: (optional) The version of the analysis model identified
          by the value of the `model_id` key.
    :attr List[Element] elements: (optional) Document elements identified by the
          service.
    :attr List[EffectiveDates] effective_dates: (optional) The date or dates on
          which the document becomes effective.
    :attr List[ContractAmts] contract_amounts: (optional) The monetary amounts that
          identify the total amount of the contract that needs to be paid from one party
          to another.
    :attr List[TerminationDates] termination_dates: (optional) The dates on which
          the document is to be terminated.
    :attr List[ContractTypes] contract_types: (optional) The contract type as
          declared in the document.
    :attr List[ContractTerms] contract_terms: (optional) The durations of the
          contract.
    :attr List[PaymentTerms] payment_terms: (optional) The document's payment
          durations.
    :attr List[ContractCurrencies] contract_currencies: (optional) The contract
          currencies as declared in the document.
    :attr List[Tables] tables: (optional) Definition of tables identified in the
          input document.
    :attr DocStructure document_structure: (optional) The structure of the input
          document.
    :attr List[Parties] parties: (optional) Definitions of the parties identified in
          the input document.
    """

    def __init__(self,
                 *,
                 document: 'Document' = None,
                 model_id: str = None,
                 model_version: str = None,
                 elements: List['Element'] = None,
                 effective_dates: List['EffectiveDates'] = None,
                 contract_amounts: List['ContractAmts'] = None,
                 termination_dates: List['TerminationDates'] = None,
                 contract_types: List['ContractTypes'] = None,
                 contract_terms: List['ContractTerms'] = None,
                 payment_terms: List['PaymentTerms'] = None,
                 contract_currencies: List['ContractCurrencies'] = None,
                 tables: List['Tables'] = None,
                 document_structure: 'DocStructure' = None,
                 parties: List['Parties'] = None) -> None:
        """
        Initialize a ClassifyReturn object.

        :param Document document: (optional) Basic information about the input
               document.
        :param str model_id: (optional) The analysis model used to classify the
               input document. For the **Element classification** method, the only valid
               value is `contracts`.
        :param str model_version: (optional) The version of the analysis model
               identified by the value of the `model_id` key.
        :param List[Element] elements: (optional) Document elements identified by
               the service.
        :param List[EffectiveDates] effective_dates: (optional) The date or dates
               on which the document becomes effective.
        :param List[ContractAmts] contract_amounts: (optional) The monetary amounts
               that identify the total amount of the contract that needs to be paid from
               one party to another.
        :param List[TerminationDates] termination_dates: (optional) The dates on
               which the document is to be terminated.
        :param List[ContractTypes] contract_types: (optional) The contract type as
               declared in the document.
        :param List[ContractTerms] contract_terms: (optional) The durations of the
               contract.
        :param List[PaymentTerms] payment_terms: (optional) The document's payment
               durations.
        :param List[ContractCurrencies] contract_currencies: (optional) The
               contract currencies as declared in the document.
        :param List[Tables] tables: (optional) Definition of tables identified in
               the input document.
        :param DocStructure document_structure: (optional) The structure of the
               input document.
        :param List[Parties] parties: (optional) Definitions of the parties
               identified in the input document.
        """
        self.document = document
        self.model_id = model_id
        self.model_version = model_version
        self.elements = elements
        self.effective_dates = effective_dates
        self.contract_amounts = contract_amounts
        self.termination_dates = termination_dates
        self.contract_types = contract_types
        self.contract_terms = contract_terms
        self.payment_terms = payment_terms
        self.contract_currencies = contract_currencies
        self.tables = tables
        self.document_structure = document_structure
        self.parties = parties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifyReturn':
        """Initialize a ClassifyReturn object from a json dictionary."""
        args = {}
        valid_keys = [
            'document', 'model_id', 'model_version', 'elements',
            'effective_dates', 'contract_amounts', 'termination_dates',
            'contract_types', 'contract_terms', 'payment_terms',
            'contract_currencies', 'tables', 'document_structure', 'parties'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifyReturn: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = Document._from_dict(_dict.get('document'))
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'model_version' in _dict:
            args['model_version'] = _dict.get('model_version')
        if 'elements' in _dict:
            args['elements'] = [
                Element._from_dict(x) for x in (_dict.get('elements'))
            ]
        if 'effective_dates' in _dict:
            args['effective_dates'] = [
                EffectiveDates._from_dict(x)
                for x in (_dict.get('effective_dates'))
            ]
        if 'contract_amounts' in _dict:
            args['contract_amounts'] = [
                ContractAmts._from_dict(x)
                for x in (_dict.get('contract_amounts'))
            ]
        if 'termination_dates' in _dict:
            args['termination_dates'] = [
                TerminationDates._from_dict(x)
                for x in (_dict.get('termination_dates'))
            ]
        if 'contract_types' in _dict:
            args['contract_types'] = [
                ContractTypes._from_dict(x)
                for x in (_dict.get('contract_types'))
            ]
        if 'contract_terms' in _dict:
            args['contract_terms'] = [
                ContractTerms._from_dict(x)
                for x in (_dict.get('contract_terms'))
            ]
        if 'payment_terms' in _dict:
            args['payment_terms'] = [
                PaymentTerms._from_dict(x) for x in (_dict.get('payment_terms'))
            ]
        if 'contract_currencies' in _dict:
            args['contract_currencies'] = [
                ContractCurrencies._from_dict(x)
                for x in (_dict.get('contract_currencies'))
            ]
        if 'tables' in _dict:
            args['tables'] = [
                Tables._from_dict(x) for x in (_dict.get('tables'))
            ]
        if 'document_structure' in _dict:
            args['document_structure'] = DocStructure._from_dict(
                _dict.get('document_structure'))
        if 'parties' in _dict:
            args['parties'] = [
                Parties._from_dict(x) for x in (_dict.get('parties'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifyReturn object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'elements') and self.elements is not None:
            _dict['elements'] = [x._to_dict() for x in self.elements]
        if hasattr(self,
                   'effective_dates') and self.effective_dates is not None:
            _dict['effective_dates'] = [
                x._to_dict() for x in self.effective_dates
            ]
        if hasattr(self,
                   'contract_amounts') and self.contract_amounts is not None:
            _dict['contract_amounts'] = [
                x._to_dict() for x in self.contract_amounts
            ]
        if hasattr(self,
                   'termination_dates') and self.termination_dates is not None:
            _dict['termination_dates'] = [
                x._to_dict() for x in self.termination_dates
            ]
        if hasattr(self, 'contract_types') and self.contract_types is not None:
            _dict['contract_types'] = [
                x._to_dict() for x in self.contract_types
            ]
        if hasattr(self, 'contract_terms') and self.contract_terms is not None:
            _dict['contract_terms'] = [
                x._to_dict() for x in self.contract_terms
            ]
        if hasattr(self, 'payment_terms') and self.payment_terms is not None:
            _dict['payment_terms'] = [x._to_dict() for x in self.payment_terms]
        if hasattr(
                self,
                'contract_currencies') and self.contract_currencies is not None:
            _dict['contract_currencies'] = [
                x._to_dict() for x in self.contract_currencies
            ]
        if hasattr(self, 'tables') and self.tables is not None:
            _dict['tables'] = [x._to_dict() for x in self.tables]
        if hasattr(
                self,
                'document_structure') and self.document_structure is not None:
            _dict['document_structure'] = self.document_structure._to_dict()
        if hasattr(self, 'parties') and self.parties is not None:
            _dict['parties'] = [x._to_dict() for x in self.parties]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifyReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassifyReturn') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifyReturn') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ColumnHeaders():
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
                 cell_id: str = None,
                 location: object = None,
                 text: str = None,
                 text_normalized: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None) -> None:
        """
        Initialize a ColumnHeaders object.

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
    def from_dict(cls, _dict: Dict) -> 'ColumnHeaders':
        """Initialize a ColumnHeaders object from a json dictionary."""
        args = {}
        valid_keys = [
            'cell_id', 'location', 'text', 'text_normalized', 'row_index_begin',
            'row_index_end', 'column_index_begin', 'column_index_end'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ColumnHeaders: '
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ColumnHeaders object from a json dictionary."""
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
        """Return a `str` version of this ColumnHeaders object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ColumnHeaders') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ColumnHeaders') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CompareReturn():
    """
    The comparison of the two submitted documents.

    :attr str model_id: (optional) The analysis model used to compare the input
          documents. For the **Compare two documents** method, the only valid value is
          `contracts`.
    :attr str model_version: (optional) The version of the analysis model identified
          by the value of the `model_id` key.
    :attr List[Document] documents: (optional) Information about the documents being
          compared.
    :attr List[AlignedElement] aligned_elements: (optional) A list of pairs of
          elements that semantically align between the compared documents.
    :attr List[UnalignedElement] unaligned_elements: (optional) A list of elements
          that do not semantically align between the compared documents.
    """

    def __init__(self,
                 *,
                 model_id: str = None,
                 model_version: str = None,
                 documents: List['Document'] = None,
                 aligned_elements: List['AlignedElement'] = None,
                 unaligned_elements: List['UnalignedElement'] = None) -> None:
        """
        Initialize a CompareReturn object.

        :param str model_id: (optional) The analysis model used to compare the
               input documents. For the **Compare two documents** method, the only valid
               value is `contracts`.
        :param str model_version: (optional) The version of the analysis model
               identified by the value of the `model_id` key.
        :param List[Document] documents: (optional) Information about the documents
               being compared.
        :param List[AlignedElement] aligned_elements: (optional) A list of pairs of
               elements that semantically align between the compared documents.
        :param List[UnalignedElement] unaligned_elements: (optional) A list of
               elements that do not semantically align between the compared documents.
        """
        self.model_id = model_id
        self.model_version = model_version
        self.documents = documents
        self.aligned_elements = aligned_elements
        self.unaligned_elements = unaligned_elements

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CompareReturn':
        """Initialize a CompareReturn object from a json dictionary."""
        args = {}
        valid_keys = [
            'model_id', 'model_version', 'documents', 'aligned_elements',
            'unaligned_elements'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CompareReturn: '
                + ', '.join(bad_keys))
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'model_version' in _dict:
            args['model_version'] = _dict.get('model_version')
        if 'documents' in _dict:
            args['documents'] = [
                Document._from_dict(x) for x in (_dict.get('documents'))
            ]
        if 'aligned_elements' in _dict:
            args['aligned_elements'] = [
                AlignedElement._from_dict(x)
                for x in (_dict.get('aligned_elements'))
            ]
        if 'unaligned_elements' in _dict:
            args['unaligned_elements'] = [
                UnalignedElement._from_dict(x)
                for x in (_dict.get('unaligned_elements'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CompareReturn object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'documents') and self.documents is not None:
            _dict['documents'] = [x._to_dict() for x in self.documents]
        if hasattr(self,
                   'aligned_elements') and self.aligned_elements is not None:
            _dict['aligned_elements'] = [
                x._to_dict() for x in self.aligned_elements
            ]
        if hasattr(
                self,
                'unaligned_elements') and self.unaligned_elements is not None:
            _dict['unaligned_elements'] = [
                x._to_dict() for x in self.unaligned_elements
            ]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CompareReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CompareReturn') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CompareReturn') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Contact():
    """
    A contact.

    :attr str name: (optional) A string listing the name of the contact.
    :attr str role: (optional) A string listing the role of the contact.
    """

    def __init__(self, *, name: str = None, role: str = None) -> None:
        """
        Initialize a Contact object.

        :param str name: (optional) A string listing the name of the contact.
        :param str role: (optional) A string listing the role of the contact.
        """
        self.name = name
        self.role = role

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Contact':
        """Initialize a Contact object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'role']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Contact: ' +
                ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'role' in _dict:
            args['role'] = _dict.get('role')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Contact object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'role') and self.role is not None:
            _dict['role'] = self.role
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Contact object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Contact') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Contact') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Contexts():
    """
    Text that is related to the contents of the table and that precedes or follows the
    current table.

    :attr str text: (optional) The related text.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a Contexts object.

        :param str text: (optional) The related text.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Contexts':
        """Initialize a Contexts object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Contexts: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Contexts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Contexts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Contexts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Contexts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractAmts():
    """
    A monetary amount identified in the input document.

    :attr str confidence_level: (optional) The confidence level in the
          identification of the contract amount.
    :attr str text: (optional) The monetary amount.
    :attr str text_normalized: (optional) The normalized form of the amount, which
          is listed as a string. This element is optional; it is returned only if
          normalized text exists.
    :attr Interpretation interpretation: (optional) The details of the normalized
          text, if applicable. This element is optional; it is returned only if normalized
          text exists.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 confidence_level: str = None,
                 text: str = None,
                 text_normalized: str = None,
                 interpretation: 'Interpretation' = None,
                 provenance_ids: List[str] = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a ContractAmts object.

        :param str confidence_level: (optional) The confidence level in the
               identification of the contract amount.
        :param str text: (optional) The monetary amount.
        :param str text_normalized: (optional) The normalized form of the amount,
               which is listed as a string. This element is optional; it is returned only
               if normalized text exists.
        :param Interpretation interpretation: (optional) The details of the
               normalized text, if applicable. This element is optional; it is returned
               only if normalized text exists.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.interpretation = interpretation
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractAmts':
        """Initialize a ContractAmts object from a json dictionary."""
        args = {}
        valid_keys = [
            'confidence_level', 'text', 'text_normalized', 'interpretation',
            'provenance_ids', 'location'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractAmts: '
                + ', '.join(bad_keys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'interpretation' in _dict:
            args['interpretation'] = Interpretation._from_dict(
                _dict.get('interpretation'))
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractAmts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'confidence_level') and self.confidence_level is not None:
            _dict['confidence_level'] = self.confidence_level
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self, 'interpretation') and self.interpretation is not None:
            _dict['interpretation'] = self.interpretation._to_dict()
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractAmts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ContractAmts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractAmts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConfidenceLevelEnum(Enum):
        """
        The confidence level in the identification of the contract amount.
        """
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"


class ContractCurrencies():
    """
    The contract currencies that are declared in the document.

    :attr str confidence_level: (optional) The confidence level in the
          identification of the contract currency.
    :attr str text: (optional) The contract currency.
    :attr str text_normalized: (optional) The normalized form of the contract
          currency, which is listed as a string in
          [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) format. This
          element is optional; it is returned only if normalized text exists.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 confidence_level: str = None,
                 text: str = None,
                 text_normalized: str = None,
                 provenance_ids: List[str] = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a ContractCurrencies object.

        :param str confidence_level: (optional) The confidence level in the
               identification of the contract currency.
        :param str text: (optional) The contract currency.
        :param str text_normalized: (optional) The normalized form of the contract
               currency, which is listed as a string in
               [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) format. This
               element is optional; it is returned only if normalized text exists.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractCurrencies':
        """Initialize a ContractCurrencies object from a json dictionary."""
        args = {}
        valid_keys = [
            'confidence_level', 'text', 'text_normalized', 'provenance_ids',
            'location'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractCurrencies: '
                + ', '.join(bad_keys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractCurrencies object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'confidence_level') and self.confidence_level is not None:
            _dict['confidence_level'] = self.confidence_level
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractCurrencies object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ContractCurrencies') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractCurrencies') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConfidenceLevelEnum(Enum):
        """
        The confidence level in the identification of the contract currency.
        """
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"


class ContractTerms():
    """
    The duration or durations of the contract.

    :attr str confidence_level: (optional) The confidence level in the
          identification of the contract term.
    :attr str text: (optional) The contract term (duration).
    :attr str text_normalized: (optional) The normalized form of the contract term,
          which is listed as a string. This element is optional; it is returned only if
          normalized text exists.
    :attr Interpretation interpretation: (optional) The details of the normalized
          text, if applicable. This element is optional; it is returned only if normalized
          text exists.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 confidence_level: str = None,
                 text: str = None,
                 text_normalized: str = None,
                 interpretation: 'Interpretation' = None,
                 provenance_ids: List[str] = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a ContractTerms object.

        :param str confidence_level: (optional) The confidence level in the
               identification of the contract term.
        :param str text: (optional) The contract term (duration).
        :param str text_normalized: (optional) The normalized form of the contract
               term, which is listed as a string. This element is optional; it is returned
               only if normalized text exists.
        :param Interpretation interpretation: (optional) The details of the
               normalized text, if applicable. This element is optional; it is returned
               only if normalized text exists.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.interpretation = interpretation
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTerms':
        """Initialize a ContractTerms object from a json dictionary."""
        args = {}
        valid_keys = [
            'confidence_level', 'text', 'text_normalized', 'interpretation',
            'provenance_ids', 'location'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractTerms: '
                + ', '.join(bad_keys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'interpretation' in _dict:
            args['interpretation'] = Interpretation._from_dict(
                _dict.get('interpretation'))
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTerms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'confidence_level') and self.confidence_level is not None:
            _dict['confidence_level'] = self.confidence_level
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self, 'interpretation') and self.interpretation is not None:
            _dict['interpretation'] = self.interpretation._to_dict()
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTerms object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ContractTerms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTerms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConfidenceLevelEnum(Enum):
        """
        The confidence level in the identification of the contract term.
        """
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"


class ContractTypes():
    """
    The contract type identified in the input document.

    :attr str confidence_level: (optional) The confidence level in the
          identification of the contract type.
    :attr str text: (optional) The contract type.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 confidence_level: str = None,
                 text: str = None,
                 provenance_ids: List[str] = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a ContractTypes object.

        :param str confidence_level: (optional) The confidence level in the
               identification of the contract type.
        :param str text: (optional) The contract type.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContractTypes':
        """Initialize a ContractTypes object from a json dictionary."""
        args = {}
        valid_keys = ['confidence_level', 'text', 'provenance_ids', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractTypes: '
                + ', '.join(bad_keys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTypes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'confidence_level') and self.confidence_level is not None:
            _dict['confidence_level'] = self.confidence_level
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContractTypes object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ContractTypes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContractTypes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConfidenceLevelEnum(Enum):
        """
        The confidence level in the identification of the contract type.
        """
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"


class DocCounts():
    """
    Document counts.

    :attr int total: (optional) Total number of documents.
    :attr int pending: (optional) Number of pending documents.
    :attr int successful: (optional) Number of documents successfully processed.
    :attr int failed: (optional) Number of documents not successfully processed.
    """

    def __init__(self,
                 *,
                 total: int = None,
                 pending: int = None,
                 successful: int = None,
                 failed: int = None) -> None:
        """
        Initialize a DocCounts object.

        :param int total: (optional) Total number of documents.
        :param int pending: (optional) Number of pending documents.
        :param int successful: (optional) Number of documents successfully
               processed.
        :param int failed: (optional) Number of documents not successfully
               processed.
        """
        self.total = total
        self.pending = pending
        self.successful = successful
        self.failed = failed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocCounts':
        """Initialize a DocCounts object from a json dictionary."""
        args = {}
        valid_keys = ['total', 'pending', 'successful', 'failed']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocCounts: '
                + ', '.join(bad_keys))
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        if 'pending' in _dict:
            args['pending'] = _dict.get('pending')
        if 'successful' in _dict:
            args['successful'] = _dict.get('successful')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocCounts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        if hasattr(self, 'pending') and self.pending is not None:
            _dict['pending'] = self.pending
        if hasattr(self, 'successful') and self.successful is not None:
            _dict['successful'] = self.successful
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocCounts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocCounts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocCounts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocInfo():
    """
    Information about the parsed input document.

    :attr str html: (optional) The full text of the parsed document in HTML format.
    :attr str title: (optional) The title of the parsed document. If the service did
          not detect a title, the value of this element is `null`.
    :attr str hash: (optional) The MD5 hash of the input document.
    """

    def __init__(self,
                 *,
                 html: str = None,
                 title: str = None,
                 hash: str = None) -> None:
        """
        Initialize a DocInfo object.

        :param str html: (optional) The full text of the parsed document in HTML
               format.
        :param str title: (optional) The title of the parsed document. If the
               service did not detect a title, the value of this element is `null`.
        :param str hash: (optional) The MD5 hash of the input document.
        """
        self.html = html
        self.title = title
        self.hash = hash

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocInfo':
        """Initialize a DocInfo object from a json dictionary."""
        args = {}
        valid_keys = ['html', 'title', 'hash']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocInfo: ' +
                ', '.join(bad_keys))
        if 'html' in _dict:
            args['html'] = _dict.get('html')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'hash' in _dict:
            args['hash'] = _dict.get('hash')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'html') and self.html is not None:
            _dict['html'] = self.html
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'hash') and self.hash is not None:
            _dict['hash'] = self.hash
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocInfo object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocStructure():
    """
    The structure of the input document.

    :attr List[SectionTitles] section_titles: (optional) An array containing one
          object per section or subsection identified in the input document.
    :attr List[LeadingSentence] leading_sentences: (optional) An array containing
          one object per section or subsection, in parallel with the `section_titles`
          array, that details the leading sentences in the corresponding section or
          subsection.
    :attr List[Paragraphs] paragraphs: (optional) An array containing one object per
          paragraph, in parallel with the `section_titles` and `leading_sentences` arrays.
    """

    def __init__(self,
                 *,
                 section_titles: List['SectionTitles'] = None,
                 leading_sentences: List['LeadingSentence'] = None,
                 paragraphs: List['Paragraphs'] = None) -> None:
        """
        Initialize a DocStructure object.

        :param List[SectionTitles] section_titles: (optional) An array containing
               one object per section or subsection identified in the input document.
        :param List[LeadingSentence] leading_sentences: (optional) An array
               containing one object per section or subsection, in parallel with the
               `section_titles` array, that details the leading sentences in the
               corresponding section or subsection.
        :param List[Paragraphs] paragraphs: (optional) An array containing one
               object per paragraph, in parallel with the `section_titles` and
               `leading_sentences` arrays.
        """
        self.section_titles = section_titles
        self.leading_sentences = leading_sentences
        self.paragraphs = paragraphs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocStructure':
        """Initialize a DocStructure object from a json dictionary."""
        args = {}
        valid_keys = ['section_titles', 'leading_sentences', 'paragraphs']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocStructure: '
                + ', '.join(bad_keys))
        if 'section_titles' in _dict:
            args['section_titles'] = [
                SectionTitles._from_dict(x)
                for x in (_dict.get('section_titles'))
            ]
        if 'leading_sentences' in _dict:
            args['leading_sentences'] = [
                LeadingSentence._from_dict(x)
                for x in (_dict.get('leading_sentences'))
            ]
        if 'paragraphs' in _dict:
            args['paragraphs'] = [
                Paragraphs._from_dict(x) for x in (_dict.get('paragraphs'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocStructure object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'section_titles') and self.section_titles is not None:
            _dict['section_titles'] = [
                x._to_dict() for x in self.section_titles
            ]
        if hasattr(self,
                   'leading_sentences') and self.leading_sentences is not None:
            _dict['leading_sentences'] = [
                x._to_dict() for x in self.leading_sentences
            ]
        if hasattr(self, 'paragraphs') and self.paragraphs is not None:
            _dict['paragraphs'] = [x._to_dict() for x in self.paragraphs]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocStructure object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocStructure') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocStructure') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Document():
    """
    Basic information about the input document.

    :attr str title: (optional) Document title, if detected.
    :attr str html: (optional) The input document converted into HTML format.
    :attr str hash: (optional) The MD5 hash value of the input document.
    :attr str label: (optional) The label applied to the input document with the
          calling method's `file_1_label` or `file_2_label` value. This field is specified
          only in the output of the **Comparing two documents** method.
    """

    def __init__(self,
                 *,
                 title: str = None,
                 html: str = None,
                 hash: str = None,
                 label: str = None) -> None:
        """
        Initialize a Document object.

        :param str title: (optional) Document title, if detected.
        :param str html: (optional) The input document converted into HTML format.
        :param str hash: (optional) The MD5 hash value of the input document.
        :param str label: (optional) The label applied to the input document with
               the calling method's `file_1_label` or `file_2_label` value. This field is
               specified only in the output of the **Comparing two documents** method.
        """
        self.title = title
        self.html = html
        self.hash = hash
        self.label = label

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Document':
        """Initialize a Document object from a json dictionary."""
        args = {}
        valid_keys = ['title', 'html', 'hash', 'label']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Document: '
                + ', '.join(bad_keys))
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'html' in _dict:
            args['html'] = _dict.get('html')
        if 'hash' in _dict:
            args['hash'] = _dict.get('hash')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Document object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'html') and self.html is not None:
            _dict['html'] = self.html
        if hasattr(self, 'hash') and self.hash is not None:
            _dict['hash'] = self.hash
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Document object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Document') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Document') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EffectiveDates():
    """
    An effective date.

    :attr str confidence_level: (optional) The confidence level in the
          identification of the effective date.
    :attr str text: (optional) The effective date, listed as a string.
    :attr str text_normalized: (optional) The normalized form of the effective date,
          which is listed as a string. This element is optional; it is returned only if
          normalized text exists.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 confidence_level: str = None,
                 text: str = None,
                 text_normalized: str = None,
                 provenance_ids: List[str] = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a EffectiveDates object.

        :param str confidence_level: (optional) The confidence level in the
               identification of the effective date.
        :param str text: (optional) The effective date, listed as a string.
        :param str text_normalized: (optional) The normalized form of the effective
               date, which is listed as a string. This element is optional; it is returned
               only if normalized text exists.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EffectiveDates':
        """Initialize a EffectiveDates object from a json dictionary."""
        args = {}
        valid_keys = [
            'confidence_level', 'text', 'text_normalized', 'provenance_ids',
            'location'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EffectiveDates: '
                + ', '.join(bad_keys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EffectiveDates object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'confidence_level') and self.confidence_level is not None:
            _dict['confidence_level'] = self.confidence_level
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EffectiveDates object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EffectiveDates') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EffectiveDates') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConfidenceLevelEnum(Enum):
        """
        The confidence level in the identification of the effective date.
        """
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"


class Element():
    """
    A component part of the document.

    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr str text: (optional) The text of the element.
    :attr List[TypeLabel] types: (optional) Description of the action specified by
          the element  and whom it affects.
    :attr List[Category] categories: (optional) List of functional categories into
          which the element falls; in other words, the subject matter of the element.
    :attr List[Attribute] attributes: (optional) List of document attributes.
    """

    def __init__(self,
                 *,
                 location: 'Location' = None,
                 text: str = None,
                 types: List['TypeLabel'] = None,
                 categories: List['Category'] = None,
                 attributes: List['Attribute'] = None) -> None:
        """
        Initialize a Element object.

        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param str text: (optional) The text of the element.
        :param List[TypeLabel] types: (optional) Description of the action
               specified by the element  and whom it affects.
        :param List[Category] categories: (optional) List of functional categories
               into which the element falls; in other words, the subject matter of the
               element.
        :param List[Attribute] attributes: (optional) List of document attributes.
        """
        self.location = location
        self.text = text
        self.types = types
        self.categories = categories
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Element':
        """Initialize a Element object from a json dictionary."""
        args = {}
        valid_keys = ['location', 'text', 'types', 'categories', 'attributes']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Element: ' +
                ', '.join(bad_keys))
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'types' in _dict:
            args['types'] = [
                TypeLabel._from_dict(x) for x in (_dict.get('types'))
            ]
        if 'categories' in _dict:
            args['categories'] = [
                Category._from_dict(x) for x in (_dict.get('categories'))
            ]
        if 'attributes' in _dict:
            args['attributes'] = [
                Attribute._from_dict(x) for x in (_dict.get('attributes'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Element object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x._to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Element object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Element') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Element') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ElementLocations():
    """
    A list of `begin` and `end` indexes that indicate the locations of the elements in the
    input document.

    :attr int begin: (optional) An integer that indicates the starting position of
          the element in the input document.
    :attr int end: (optional) An integer that indicates the ending position of the
          element in the input document.
    """

    def __init__(self, *, begin: int = None, end: int = None) -> None:
        """
        Initialize a ElementLocations object.

        :param int begin: (optional) An integer that indicates the starting
               position of the element in the input document.
        :param int end: (optional) An integer that indicates the ending position of
               the element in the input document.
        """
        self.begin = begin
        self.end = end

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ElementLocations':
        """Initialize a ElementLocations object from a json dictionary."""
        args = {}
        valid_keys = ['begin', 'end']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ElementLocations: '
                + ', '.join(bad_keys))
        if 'begin' in _dict:
            args['begin'] = _dict.get('begin')
        if 'end' in _dict:
            args['end'] = _dict.get('end')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElementLocations object from a json dictionary."""
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
        """Return a `str` version of this ElementLocations object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ElementLocations') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ElementLocations') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ElementPair():
    """
    Details of semantically aligned elements.

    :attr str document_label: (optional) The label of the document (that is, the
          value of either the `file_1_label` or `file_2_label` parameters) in which the
          element occurs.
    :attr str text: (optional) The contents of the element.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr List[TypeLabelComparison] types: (optional) Description of the action
          specified by the element and whom it affects.
    :attr List[CategoryComparison] categories: (optional) List of functional
          categories into which the element falls; in other words, the subject matter of
          the element.
    :attr List[Attribute] attributes: (optional) List of document attributes.
    """

    def __init__(self,
                 *,
                 document_label: str = None,
                 text: str = None,
                 location: 'Location' = None,
                 types: List['TypeLabelComparison'] = None,
                 categories: List['CategoryComparison'] = None,
                 attributes: List['Attribute'] = None) -> None:
        """
        Initialize a ElementPair object.

        :param str document_label: (optional) The label of the document (that is,
               the value of either the `file_1_label` or `file_2_label` parameters) in
               which the element occurs.
        :param str text: (optional) The contents of the element.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param List[TypeLabelComparison] types: (optional) Description of the
               action specified by the element and whom it affects.
        :param List[CategoryComparison] categories: (optional) List of functional
               categories into which the element falls; in other words, the subject matter
               of the element.
        :param List[Attribute] attributes: (optional) List of document attributes.
        """
        self.document_label = document_label
        self.text = text
        self.location = location
        self.types = types
        self.categories = categories
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ElementPair':
        """Initialize a ElementPair object from a json dictionary."""
        args = {}
        valid_keys = [
            'document_label', 'text', 'location', 'types', 'categories',
            'attributes'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ElementPair: '
                + ', '.join(bad_keys))
        if 'document_label' in _dict:
            args['document_label'] = _dict.get('document_label')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'types' in _dict:
            args['types'] = [
                TypeLabelComparison._from_dict(x) for x in (_dict.get('types'))
            ]
        if 'categories' in _dict:
            args['categories'] = [
                CategoryComparison._from_dict(x)
                for x in (_dict.get('categories'))
            ]
        if 'attributes' in _dict:
            args['attributes'] = [
                Attribute._from_dict(x) for x in (_dict.get('attributes'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElementPair object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_label') and self.document_label is not None:
            _dict['document_label'] = self.document_label
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x._to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ElementPair object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ElementPair') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ElementPair') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackDataInput():
    """
    Feedback data for submission.

    :attr str feedback_type: The type of feedback. The only permitted value is
          `element_classification`.
    :attr ShortDoc document: (optional) Brief information about the input document.
    :attr str model_id: (optional) An optional string identifying the model ID. The
          only permitted value is `contracts`.
    :attr str model_version: (optional) An optional string identifying the version
          of the model used.
    :attr Location location: The numeric location of the identified element in the
          document, represented with two integers labeled `begin` and `end`.
    :attr str text: The text on which to submit feedback.
    :attr OriginalLabelsIn original_labels: The original labeling from the input
          document, without the submitted feedback.
    :attr UpdatedLabelsIn updated_labels: The updated labeling from the input
          document, accounting for the submitted feedback.
    """

    def __init__(self,
                 feedback_type: str,
                 location: 'Location',
                 text: str,
                 original_labels: 'OriginalLabelsIn',
                 updated_labels: 'UpdatedLabelsIn',
                 *,
                 document: 'ShortDoc' = None,
                 model_id: str = None,
                 model_version: str = None) -> None:
        """
        Initialize a FeedbackDataInput object.

        :param str feedback_type: The type of feedback. The only permitted value is
               `element_classification`.
        :param Location location: The numeric location of the identified element in
               the document, represented with two integers labeled `begin` and `end`.
        :param str text: The text on which to submit feedback.
        :param OriginalLabelsIn original_labels: The original labeling from the
               input document, without the submitted feedback.
        :param UpdatedLabelsIn updated_labels: The updated labeling from the input
               document, accounting for the submitted feedback.
        :param ShortDoc document: (optional) Brief information about the input
               document.
        :param str model_id: (optional) An optional string identifying the model
               ID. The only permitted value is `contracts`.
        :param str model_version: (optional) An optional string identifying the
               version of the model used.
        """
        self.feedback_type = feedback_type
        self.document = document
        self.model_id = model_id
        self.model_version = model_version
        self.location = location
        self.text = text
        self.original_labels = original_labels
        self.updated_labels = updated_labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeedbackDataInput':
        """Initialize a FeedbackDataInput object from a json dictionary."""
        args = {}
        valid_keys = [
            'feedback_type', 'document', 'model_id', 'model_version',
            'location', 'text', 'original_labels', 'updated_labels'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackDataInput: '
                + ', '.join(bad_keys))
        if 'feedback_type' in _dict:
            args['feedback_type'] = _dict.get('feedback_type')
        else:
            raise ValueError(
                'Required property \'feedback_type\' not present in FeedbackDataInput JSON'
            )
        if 'document' in _dict:
            args['document'] = ShortDoc._from_dict(_dict.get('document'))
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'model_version' in _dict:
            args['model_version'] = _dict.get('model_version')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        else:
            raise ValueError(
                'Required property \'location\' not present in FeedbackDataInput JSON'
            )
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in FeedbackDataInput JSON'
            )
        if 'original_labels' in _dict:
            args['original_labels'] = OriginalLabelsIn._from_dict(
                _dict.get('original_labels'))
        else:
            raise ValueError(
                'Required property \'original_labels\' not present in FeedbackDataInput JSON'
            )
        if 'updated_labels' in _dict:
            args['updated_labels'] = UpdatedLabelsIn._from_dict(
                _dict.get('updated_labels'))
        else:
            raise ValueError(
                'Required property \'updated_labels\' not present in FeedbackDataInput JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackDataInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'feedback_type') and self.feedback_type is not None:
            _dict['feedback_type'] = self.feedback_type
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'original_labels') and self.original_labels is not None:
            _dict['original_labels'] = self.original_labels._to_dict()
        if hasattr(self, 'updated_labels') and self.updated_labels is not None:
            _dict['updated_labels'] = self.updated_labels._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeedbackDataInput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FeedbackDataInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeedbackDataInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackDataOutput():
    """
    Information returned from the **Add Feedback** method.

    :attr str feedback_type: (optional) A string identifying the user adding the
          feedback. The only permitted value is `element_classification`.
    :attr ShortDoc document: (optional) Brief information about the input document.
    :attr str model_id: (optional) An optional string identifying the model ID. The
          only permitted value is `contracts`.
    :attr str model_version: (optional) An optional string identifying the version
          of the model used.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr str text: (optional) The text to which the feedback applies.
    :attr OriginalLabelsOut original_labels: (optional) The original labeling from
          the input document, without the submitted feedback.
    :attr UpdatedLabelsOut updated_labels: (optional) The updated labeling from the
          input document, accounting for the submitted feedback.
    :attr Pagination pagination: (optional) Pagination details, if required by the
          length of the output.
    """

    def __init__(self,
                 *,
                 feedback_type: str = None,
                 document: 'ShortDoc' = None,
                 model_id: str = None,
                 model_version: str = None,
                 location: 'Location' = None,
                 text: str = None,
                 original_labels: 'OriginalLabelsOut' = None,
                 updated_labels: 'UpdatedLabelsOut' = None,
                 pagination: 'Pagination' = None) -> None:
        """
        Initialize a FeedbackDataOutput object.

        :param str feedback_type: (optional) A string identifying the user adding
               the feedback. The only permitted value is `element_classification`.
        :param ShortDoc document: (optional) Brief information about the input
               document.
        :param str model_id: (optional) An optional string identifying the model
               ID. The only permitted value is `contracts`.
        :param str model_version: (optional) An optional string identifying the
               version of the model used.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param str text: (optional) The text to which the feedback applies.
        :param OriginalLabelsOut original_labels: (optional) The original labeling
               from the input document, without the submitted feedback.
        :param UpdatedLabelsOut updated_labels: (optional) The updated labeling
               from the input document, accounting for the submitted feedback.
        :param Pagination pagination: (optional) Pagination details, if required by
               the length of the output.
        """
        self.feedback_type = feedback_type
        self.document = document
        self.model_id = model_id
        self.model_version = model_version
        self.location = location
        self.text = text
        self.original_labels = original_labels
        self.updated_labels = updated_labels
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeedbackDataOutput':
        """Initialize a FeedbackDataOutput object from a json dictionary."""
        args = {}
        valid_keys = [
            'feedback_type', 'document', 'model_id', 'model_version',
            'location', 'text', 'original_labels', 'updated_labels',
            'pagination'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackDataOutput: '
                + ', '.join(bad_keys))
        if 'feedback_type' in _dict:
            args['feedback_type'] = _dict.get('feedback_type')
        if 'document' in _dict:
            args['document'] = ShortDoc._from_dict(_dict.get('document'))
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'model_version' in _dict:
            args['model_version'] = _dict.get('model_version')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'original_labels' in _dict:
            args['original_labels'] = OriginalLabelsOut._from_dict(
                _dict.get('original_labels'))
        if 'updated_labels' in _dict:
            args['updated_labels'] = UpdatedLabelsOut._from_dict(
                _dict.get('updated_labels'))
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackDataOutput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'feedback_type') and self.feedback_type is not None:
            _dict['feedback_type'] = self.feedback_type
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'original_labels') and self.original_labels is not None:
            _dict['original_labels'] = self.original_labels._to_dict()
        if hasattr(self, 'updated_labels') and self.updated_labels is not None:
            _dict['updated_labels'] = self.updated_labels._to_dict()
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeedbackDataOutput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FeedbackDataOutput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeedbackDataOutput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackDeleted():
    """
    The status and message of the deletion request.

    :attr int status: (optional) HTTP return code.
    :attr str message: (optional) Status message returned from the service.
    """

    def __init__(self, *, status: int = None, message: str = None) -> None:
        """
        Initialize a FeedbackDeleted object.

        :param int status: (optional) HTTP return code.
        :param str message: (optional) Status message returned from the service.
        """
        self.status = status
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeedbackDeleted':
        """Initialize a FeedbackDeleted object from a json dictionary."""
        args = {}
        valid_keys = ['status', 'message']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackDeleted: '
                + ', '.join(bad_keys))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackDeleted object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeedbackDeleted object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FeedbackDeleted') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeedbackDeleted') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackList():
    """
    The results of a successful **List Feedback** request for all feedback.

    :attr List[GetFeedback] feedback: (optional) A list of all feedback for the
          document.
    """

    def __init__(self, *, feedback: List['GetFeedback'] = None) -> None:
        """
        Initialize a FeedbackList object.

        :param List[GetFeedback] feedback: (optional) A list of all feedback for
               the document.
        """
        self.feedback = feedback

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeedbackList':
        """Initialize a FeedbackList object from a json dictionary."""
        args = {}
        valid_keys = ['feedback']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackList: '
                + ', '.join(bad_keys))
        if 'feedback' in _dict:
            args['feedback'] = [
                GetFeedback._from_dict(x) for x in (_dict.get('feedback'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'feedback') and self.feedback is not None:
            _dict['feedback'] = [x._to_dict() for x in self.feedback]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeedbackList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FeedbackList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeedbackList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackReturn():
    """
    Information about the document and the submitted feedback.

    :attr str feedback_id: (optional) The unique ID of the feedback object.
    :attr str user_id: (optional) An optional string identifying the person
          submitting feedback.
    :attr str comment: (optional) An optional comment from the person submitting the
          feedback.
    :attr datetime created: (optional) Timestamp listing the creation time of the
          feedback submission.
    :attr FeedbackDataOutput feedback_data: (optional) Information returned from the
          **Add Feedback** method.
    """

    def __init__(self,
                 *,
                 feedback_id: str = None,
                 user_id: str = None,
                 comment: str = None,
                 created: datetime = None,
                 feedback_data: 'FeedbackDataOutput' = None) -> None:
        """
        Initialize a FeedbackReturn object.

        :param str feedback_id: (optional) The unique ID of the feedback object.
        :param str user_id: (optional) An optional string identifying the person
               submitting feedback.
        :param str comment: (optional) An optional comment from the person
               submitting the feedback.
        :param datetime created: (optional) Timestamp listing the creation time of
               the feedback submission.
        :param FeedbackDataOutput feedback_data: (optional) Information returned
               from the **Add Feedback** method.
        """
        self.feedback_id = feedback_id
        self.user_id = user_id
        self.comment = comment
        self.created = created
        self.feedback_data = feedback_data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeedbackReturn':
        """Initialize a FeedbackReturn object from a json dictionary."""
        args = {}
        valid_keys = [
            'feedback_id', 'user_id', 'comment', 'created', 'feedback_data'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackReturn: '
                + ', '.join(bad_keys))
        if 'feedback_id' in _dict:
            args['feedback_id'] = _dict.get('feedback_id')
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        if 'comment' in _dict:
            args['comment'] = _dict.get('comment')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'feedback_data' in _dict:
            args['feedback_data'] = FeedbackDataOutput._from_dict(
                _dict.get('feedback_data'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackReturn object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'feedback_id') and self.feedback_id is not None:
            _dict['feedback_id'] = self.feedback_id
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['comment'] = self.comment
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'feedback_data') and self.feedback_data is not None:
            _dict['feedback_data'] = self.feedback_data._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeedbackReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FeedbackReturn') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeedbackReturn') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GetFeedback():
    """
    The results of a successful **Get Feedback** request for a single feedback entry.

    :attr str feedback_id: (optional) A string uniquely identifying the feedback
          entry.
    :attr datetime created: (optional) A timestamp identifying the creation time of
          the feedback entry.
    :attr str comment: (optional) A string containing the user's comment about the
          feedback entry.
    :attr FeedbackDataOutput feedback_data: (optional) Information returned from the
          **Add Feedback** method.
    """

    def __init__(self,
                 *,
                 feedback_id: str = None,
                 created: datetime = None,
                 comment: str = None,
                 feedback_data: 'FeedbackDataOutput' = None) -> None:
        """
        Initialize a GetFeedback object.

        :param str feedback_id: (optional) A string uniquely identifying the
               feedback entry.
        :param datetime created: (optional) A timestamp identifying the creation
               time of the feedback entry.
        :param str comment: (optional) A string containing the user's comment about
               the feedback entry.
        :param FeedbackDataOutput feedback_data: (optional) Information returned
               from the **Add Feedback** method.
        """
        self.feedback_id = feedback_id
        self.created = created
        self.comment = comment
        self.feedback_data = feedback_data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetFeedback':
        """Initialize a GetFeedback object from a json dictionary."""
        args = {}
        valid_keys = ['feedback_id', 'created', 'comment', 'feedback_data']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class GetFeedback: '
                + ', '.join(bad_keys))
        if 'feedback_id' in _dict:
            args['feedback_id'] = _dict.get('feedback_id')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'comment' in _dict:
            args['comment'] = _dict.get('comment')
        if 'feedback_data' in _dict:
            args['feedback_data'] = FeedbackDataOutput._from_dict(
                _dict.get('feedback_data'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetFeedback object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'feedback_id') and self.feedback_id is not None:
            _dict['feedback_id'] = self.feedback_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['comment'] = self.comment
        if hasattr(self, 'feedback_data') and self.feedback_data is not None:
            _dict['feedback_data'] = self.feedback_data._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetFeedback object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'GetFeedback') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetFeedback') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HTMLReturn():
    """
    The HTML converted from an input document.

    :attr str num_pages: (optional) The number of pages in the input document.
    :attr str author: (optional) The author of the input document, if identified.
    :attr str publication_date: (optional) The publication date of the input
          document, if identified.
    :attr str title: (optional) The title of the input document, if identified.
    :attr str html: (optional) The HTML version of the input document.
    """

    def __init__(self,
                 *,
                 num_pages: str = None,
                 author: str = None,
                 publication_date: str = None,
                 title: str = None,
                 html: str = None) -> None:
        """
        Initialize a HTMLReturn object.

        :param str num_pages: (optional) The number of pages in the input document.
        :param str author: (optional) The author of the input document, if
               identified.
        :param str publication_date: (optional) The publication date of the input
               document, if identified.
        :param str title: (optional) The title of the input document, if
               identified.
        :param str html: (optional) The HTML version of the input document.
        """
        self.num_pages = num_pages
        self.author = author
        self.publication_date = publication_date
        self.title = title
        self.html = html

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HTMLReturn':
        """Initialize a HTMLReturn object from a json dictionary."""
        args = {}
        valid_keys = [
            'num_pages', 'author', 'publication_date', 'title', 'html'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class HTMLReturn: '
                + ', '.join(bad_keys))
        if 'num_pages' in _dict:
            args['num_pages'] = _dict.get('num_pages')
        if 'author' in _dict:
            args['author'] = _dict.get('author')
        if 'publication_date' in _dict:
            args['publication_date'] = _dict.get('publication_date')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'html' in _dict:
            args['html'] = _dict.get('html')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HTMLReturn object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'num_pages') and self.num_pages is not None:
            _dict['num_pages'] = self.num_pages
        if hasattr(self, 'author') and self.author is not None:
            _dict['author'] = self.author
        if hasattr(self,
                   'publication_date') and self.publication_date is not None:
            _dict['publication_date'] = self.publication_date
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'html') and self.html is not None:
            _dict['html'] = self.html
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HTMLReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'HTMLReturn') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HTMLReturn') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Interpretation():
    """
    The details of the normalized text, if applicable. This element is optional; it is
    returned only if normalized text exists.

    :attr str value: (optional) The value that was located in the normalized text.
    :attr float numeric_value: (optional) An integer or float expressing the numeric
          value of the `value` key.
    :attr str unit: (optional) A string listing the unit of the value that was found
          in the normalized text.
          **Note:** The value of `unit` is the [ISO-4217 currency
          code](https://www.iso.org/iso-4217-currency-codes.html) identified for the
          currency amount (for example, `USD` or `EUR`). If the service cannot
          disambiguate a currency symbol (for example, `$` or `£`), the value of `unit`
          contains the ambiguous symbol as-is.
    """

    def __init__(self,
                 *,
                 value: str = None,
                 numeric_value: float = None,
                 unit: str = None) -> None:
        """
        Initialize a Interpretation object.

        :param str value: (optional) The value that was located in the normalized
               text.
        :param float numeric_value: (optional) An integer or float expressing the
               numeric value of the `value` key.
        :param str unit: (optional) A string listing the unit of the value that was
               found in the normalized text.
               **Note:** The value of `unit` is the [ISO-4217 currency
               code](https://www.iso.org/iso-4217-currency-codes.html) identified for the
               currency amount (for example, `USD` or `EUR`). If the service cannot
               disambiguate a currency symbol (for example, `$` or `£`), the value of
               `unit` contains the ambiguous symbol as-is.
        """
        self.value = value
        self.numeric_value = numeric_value
        self.unit = unit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Interpretation':
        """Initialize a Interpretation object from a json dictionary."""
        args = {}
        valid_keys = ['value', 'numeric_value', 'unit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Interpretation: '
                + ', '.join(bad_keys))
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'numeric_value' in _dict:
            args['numeric_value'] = _dict.get('numeric_value')
        if 'unit' in _dict:
            args['unit'] = _dict.get('unit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Interpretation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'numeric_value') and self.numeric_value is not None:
            _dict['numeric_value'] = self.numeric_value
        if hasattr(self, 'unit') and self.unit is not None:
            _dict['unit'] = self.unit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Interpretation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Interpretation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Interpretation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Key():
    """
    A key in a key-value pair.

    :attr str cell_id: (optional) The unique ID of the key in the table.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr str text: (optional) The text content of the table cell without HTML
          markup.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: 'Location' = None,
                 text: str = None) -> None:
        """
        Initialize a Key object.

        :param str cell_id: (optional) The unique ID of the key in the table.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param str text: (optional) The text content of the table cell without HTML
               markup.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Key':
        """Initialize a Key object from a json dictionary."""
        args = {}
        valid_keys = ['cell_id', 'location', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Key: ' +
                ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Key object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Key object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Key') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Key') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeyValuePair():
    """
    Key-value pairs detected across cell boundaries.

    :attr Key key: (optional) A key in a key-value pair.
    :attr List[Value] value: (optional) A list of values in a key-value pair.
    """

    def __init__(self,
                 *,
                 key: 'Key' = None,
                 value: List['Value'] = None) -> None:
        """
        Initialize a KeyValuePair object.

        :param Key key: (optional) A key in a key-value pair.
        :param List[Value] value: (optional) A list of values in a key-value pair.
        """
        self.key = key
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KeyValuePair':
        """Initialize a KeyValuePair object from a json dictionary."""
        args = {}
        valid_keys = ['key', 'value']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class KeyValuePair: '
                + ', '.join(bad_keys))
        if 'key' in _dict:
            args['key'] = Key._from_dict(_dict.get('key'))
        if 'value' in _dict:
            args['value'] = [Value._from_dict(x) for x in (_dict.get('value'))]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeyValuePair object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key._to_dict()
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = [x._to_dict() for x in self.value]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KeyValuePair object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'KeyValuePair') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KeyValuePair') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Label():
    """
    A pair of `nature` and `party` objects. The `nature` object identifies the effect of
    the element on the identified `party`, and the `party` object identifies the affected
    party.

    :attr str nature: The identified `nature` of the element.
    :attr str party: The identified `party` of the element.
    """

    def __init__(self, nature: str, party: str) -> None:
        """
        Initialize a Label object.

        :param str nature: The identified `nature` of the element.
        :param str party: The identified `party` of the element.
        """
        self.nature = nature
        self.party = party

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Label':
        """Initialize a Label object from a json dictionary."""
        args = {}
        valid_keys = ['nature', 'party']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Label: ' +
                ', '.join(bad_keys))
        if 'nature' in _dict:
            args['nature'] = _dict.get('nature')
        else:
            raise ValueError(
                'Required property \'nature\' not present in Label JSON')
        if 'party' in _dict:
            args['party'] = _dict.get('party')
        else:
            raise ValueError(
                'Required property \'party\' not present in Label JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Label object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'nature') and self.nature is not None:
            _dict['nature'] = self.nature
        if hasattr(self, 'party') and self.party is not None:
            _dict['party'] = self.party
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Label object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Label') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Label') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LeadingSentence():
    """
    The leading sentences in a section or subsection of the input document.

    :attr str text: (optional) The text of the leading sentence.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr List[ElementLocations] element_locations: (optional) An array of
          `location` objects that lists the locations of detected leading sentences.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: 'Location' = None,
                 element_locations: List['ElementLocations'] = None) -> None:
        """
        Initialize a LeadingSentence object.

        :param str text: (optional) The text of the leading sentence.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param List[ElementLocations] element_locations: (optional) An array of
               `location` objects that lists the locations of detected leading sentences.
        """
        self.text = text
        self.location = location
        self.element_locations = element_locations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LeadingSentence':
        """Initialize a LeadingSentence object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location', 'element_locations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LeadingSentence: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'element_locations' in _dict:
            args['element_locations'] = [
                ElementLocations._from_dict(x)
                for x in (_dict.get('element_locations'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LeadingSentence object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self,
                   'element_locations') and self.element_locations is not None:
            _dict['element_locations'] = [
                x._to_dict() for x in self.element_locations
            ]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LeadingSentence object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'LeadingSentence') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LeadingSentence') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Location():
    """
    The numeric location of the identified element in the document, represented with two
    integers labeled `begin` and `end`.

    :attr int begin: The element's `begin` index.
    :attr int end: The element's `end` index.
    """

    def __init__(self, begin: int, end: int) -> None:
        """
        Initialize a Location object.

        :param int begin: The element's `begin` index.
        :param int end: The element's `end` index.
        """
        self.begin = begin
        self.end = end

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Location':
        """Initialize a Location object from a json dictionary."""
        args = {}
        valid_keys = ['begin', 'end']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Location: '
                + ', '.join(bad_keys))
        if 'begin' in _dict:
            args['begin'] = _dict.get('begin')
        else:
            raise ValueError(
                'Required property \'begin\' not present in Location JSON')
        if 'end' in _dict:
            args['end'] = _dict.get('end')
        else:
            raise ValueError(
                'Required property \'end\' not present in Location JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Location object from a json dictionary."""
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
        """Return a `str` version of this Location object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Location') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Location') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Mention():
    """
    A mention of a party.

    :attr str text: (optional) The name of the party.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a Mention object.

        :param str text: (optional) The name of the party.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Mention':
        """Initialize a Mention object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Mention: ' +
                ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Mention object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Mention object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Mention') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Mention') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OriginalLabelsIn():
    """
    The original labeling from the input document, without the submitted feedback.

    :attr List[TypeLabel] types: Description of the action specified by the element
          and whom it affects.
    :attr List[Category] categories: List of functional categories into which the
          element falls; in other words, the subject matter of the element.
    """

    def __init__(self, types: List['TypeLabel'],
                 categories: List['Category']) -> None:
        """
        Initialize a OriginalLabelsIn object.

        :param List[TypeLabel] types: Description of the action specified by the
               element and whom it affects.
        :param List[Category] categories: List of functional categories into which
               the element falls; in other words, the subject matter of the element.
        """
        self.types = types
        self.categories = categories

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OriginalLabelsIn':
        """Initialize a OriginalLabelsIn object from a json dictionary."""
        args = {}
        valid_keys = ['types', 'categories']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class OriginalLabelsIn: '
                + ', '.join(bad_keys))
        if 'types' in _dict:
            args['types'] = [
                TypeLabel._from_dict(x) for x in (_dict.get('types'))
            ]
        else:
            raise ValueError(
                'Required property \'types\' not present in OriginalLabelsIn JSON'
            )
        if 'categories' in _dict:
            args['categories'] = [
                Category._from_dict(x) for x in (_dict.get('categories'))
            ]
        else:
            raise ValueError(
                'Required property \'categories\' not present in OriginalLabelsIn JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginalLabelsIn object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OriginalLabelsIn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'OriginalLabelsIn') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OriginalLabelsIn') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OriginalLabelsOut():
    """
    The original labeling from the input document, without the submitted feedback.

    :attr List[TypeLabel] types: (optional) Description of the action specified by
          the element and whom it affects.
    :attr List[Category] categories: (optional) List of functional categories into
          which the element falls; in other words, the subject matter of the element.
    :attr str modification: (optional) A string identifying the type of modification
          the feedback entry in the `updated_labels` array. Possible values are `added`,
          `not_changed`, and `removed`.
    """

    def __init__(self,
                 *,
                 types: List['TypeLabel'] = None,
                 categories: List['Category'] = None,
                 modification: str = None) -> None:
        """
        Initialize a OriginalLabelsOut object.

        :param List[TypeLabel] types: (optional) Description of the action
               specified by the element and whom it affects.
        :param List[Category] categories: (optional) List of functional categories
               into which the element falls; in other words, the subject matter of the
               element.
        :param str modification: (optional) A string identifying the type of
               modification the feedback entry in the `updated_labels` array. Possible
               values are `added`, `not_changed`, and `removed`.
        """
        self.types = types
        self.categories = categories
        self.modification = modification

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OriginalLabelsOut':
        """Initialize a OriginalLabelsOut object from a json dictionary."""
        args = {}
        valid_keys = ['types', 'categories', 'modification']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class OriginalLabelsOut: '
                + ', '.join(bad_keys))
        if 'types' in _dict:
            args['types'] = [
                TypeLabel._from_dict(x) for x in (_dict.get('types'))
            ]
        if 'categories' in _dict:
            args['categories'] = [
                Category._from_dict(x) for x in (_dict.get('categories'))
            ]
        if 'modification' in _dict:
            args['modification'] = _dict.get('modification')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginalLabelsOut object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'modification') and self.modification is not None:
            _dict['modification'] = self.modification
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OriginalLabelsOut object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'OriginalLabelsOut') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OriginalLabelsOut') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModificationEnum(Enum):
        """
        A string identifying the type of modification the feedback entry in the
        `updated_labels` array. Possible values are `added`, `not_changed`, and `removed`.
        """
        ADDED = "added"
        NOT_CHANGED = "not_changed"
        REMOVED = "removed"


class Pagination():
    """
    Pagination details, if required by the length of the output.

    :attr str refresh_cursor: (optional) A token identifying the current page of
          results.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    :attr str refresh_url: (optional) The URL that returns the current page of
          results.
    :attr str next_url: (optional) The URL that returns the next page of results.
    :attr int total: (optional) Reserved for future use.
    """

    def __init__(self,
                 *,
                 refresh_cursor: str = None,
                 next_cursor: str = None,
                 refresh_url: str = None,
                 next_url: str = None,
                 total: int = None) -> None:
        """
        Initialize a Pagination object.

        :param str refresh_cursor: (optional) A token identifying the current page
               of results.
        :param str next_cursor: (optional) A token identifying the next page of
               results.
        :param str refresh_url: (optional) The URL that returns the current page of
               results.
        :param str next_url: (optional) The URL that returns the next page of
               results.
        :param int total: (optional) Reserved for future use.
        """
        self.refresh_cursor = refresh_cursor
        self.next_cursor = next_cursor
        self.refresh_url = refresh_url
        self.next_url = next_url
        self.total = total

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pagination':
        """Initialize a Pagination object from a json dictionary."""
        args = {}
        valid_keys = [
            'refresh_cursor', 'next_cursor', 'refresh_url', 'next_url', 'total'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Pagination: '
                + ', '.join(bad_keys))
        if 'refresh_cursor' in _dict:
            args['refresh_cursor'] = _dict.get('refresh_cursor')
        if 'next_cursor' in _dict:
            args['next_cursor'] = _dict.get('next_cursor')
        if 'refresh_url' in _dict:
            args['refresh_url'] = _dict.get('refresh_url')
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pagination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'refresh_cursor') and self.refresh_cursor is not None:
            _dict['refresh_cursor'] = self.refresh_cursor
        if hasattr(self, 'next_cursor') and self.next_cursor is not None:
            _dict['next_cursor'] = self.next_cursor
        if hasattr(self, 'refresh_url') and self.refresh_url is not None:
            _dict['refresh_url'] = self.refresh_url
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pagination object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Pagination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pagination') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Paragraphs():
    """
    The locations of each paragraph in the input document.

    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self, *, location: 'Location' = None) -> None:
        """
        Initialize a Paragraphs object.

        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Paragraphs':
        """Initialize a Paragraphs object from a json dictionary."""
        args = {}
        valid_keys = ['location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Paragraphs: '
                + ', '.join(bad_keys))
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Paragraphs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Paragraphs object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Paragraphs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Paragraphs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Parties():
    """
    A party and its corresponding role, including address and contact information if
    identified.

    :attr str party: (optional) The normalized form of the party's name.
    :attr str role: (optional) A string identifying the party's role.
    :attr str importance: (optional) A string that identifies the importance of the
          party.
    :attr List[Address] addresses: (optional) A list of the party's address or
          addresses.
    :attr List[Contact] contacts: (optional) A list of the names and roles of
          contacts identified in the input document.
    :attr List[Mention] mentions: (optional) A list of the party's mentions in the
          input document.
    """

    def __init__(self,
                 *,
                 party: str = None,
                 role: str = None,
                 importance: str = None,
                 addresses: List['Address'] = None,
                 contacts: List['Contact'] = None,
                 mentions: List['Mention'] = None) -> None:
        """
        Initialize a Parties object.

        :param str party: (optional) The normalized form of the party's name.
        :param str role: (optional) A string identifying the party's role.
        :param str importance: (optional) A string that identifies the importance
               of the party.
        :param List[Address] addresses: (optional) A list of the party's address or
               addresses.
        :param List[Contact] contacts: (optional) A list of the names and roles of
               contacts identified in the input document.
        :param List[Mention] mentions: (optional) A list of the party's mentions in
               the input document.
        """
        self.party = party
        self.role = role
        self.importance = importance
        self.addresses = addresses
        self.contacts = contacts
        self.mentions = mentions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Parties':
        """Initialize a Parties object from a json dictionary."""
        args = {}
        valid_keys = [
            'party', 'role', 'importance', 'addresses', 'contacts', 'mentions'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Parties: ' +
                ', '.join(bad_keys))
        if 'party' in _dict:
            args['party'] = _dict.get('party')
        if 'role' in _dict:
            args['role'] = _dict.get('role')
        if 'importance' in _dict:
            args['importance'] = _dict.get('importance')
        if 'addresses' in _dict:
            args['addresses'] = [
                Address._from_dict(x) for x in (_dict.get('addresses'))
            ]
        if 'contacts' in _dict:
            args['contacts'] = [
                Contact._from_dict(x) for x in (_dict.get('contacts'))
            ]
        if 'mentions' in _dict:
            args['mentions'] = [
                Mention._from_dict(x) for x in (_dict.get('mentions'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Parties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'party') and self.party is not None:
            _dict['party'] = self.party
        if hasattr(self, 'role') and self.role is not None:
            _dict['role'] = self.role
        if hasattr(self, 'importance') and self.importance is not None:
            _dict['importance'] = self.importance
        if hasattr(self, 'addresses') and self.addresses is not None:
            _dict['addresses'] = [x._to_dict() for x in self.addresses]
        if hasattr(self, 'contacts') and self.contacts is not None:
            _dict['contacts'] = [x._to_dict() for x in self.contacts]
        if hasattr(self, 'mentions') and self.mentions is not None:
            _dict['mentions'] = [x._to_dict() for x in self.mentions]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Parties object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Parties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Parties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ImportanceEnum(Enum):
        """
        A string that identifies the importance of the party.
        """
        PRIMARY = "Primary"
        UNKNOWN = "Unknown"


class PaymentTerms():
    """
    The document's payment duration or durations.

    :attr str confidence_level: (optional) The confidence level in the
          identification of the payment term.
    :attr str text: (optional) The payment term (duration).
    :attr str text_normalized: (optional) The normalized form of the payment term,
          which is listed as a string. This element is optional; it is returned only if
          normalized text exists.
    :attr Interpretation interpretation: (optional) The details of the normalized
          text, if applicable. This element is optional; it is returned only if normalized
          text exists.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 confidence_level: str = None,
                 text: str = None,
                 text_normalized: str = None,
                 interpretation: 'Interpretation' = None,
                 provenance_ids: List[str] = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a PaymentTerms object.

        :param str confidence_level: (optional) The confidence level in the
               identification of the payment term.
        :param str text: (optional) The payment term (duration).
        :param str text_normalized: (optional) The normalized form of the payment
               term, which is listed as a string. This element is optional; it is returned
               only if normalized text exists.
        :param Interpretation interpretation: (optional) The details of the
               normalized text, if applicable. This element is optional; it is returned
               only if normalized text exists.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.interpretation = interpretation
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaymentTerms':
        """Initialize a PaymentTerms object from a json dictionary."""
        args = {}
        valid_keys = [
            'confidence_level', 'text', 'text_normalized', 'interpretation',
            'provenance_ids', 'location'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class PaymentTerms: '
                + ', '.join(bad_keys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'interpretation' in _dict:
            args['interpretation'] = Interpretation._from_dict(
                _dict.get('interpretation'))
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaymentTerms object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'confidence_level') and self.confidence_level is not None:
            _dict['confidence_level'] = self.confidence_level
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self, 'interpretation') and self.interpretation is not None:
            _dict['interpretation'] = self.interpretation._to_dict()
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PaymentTerms object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'PaymentTerms') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PaymentTerms') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConfidenceLevelEnum(Enum):
        """
        The confidence level in the identification of the payment term.
        """
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"


class RowHeaders():
    """
    Row-level cells, each applicable as a header to other cells in the same row as itself,
    of the current table.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
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
                 location: 'Location' = None,
                 text: str = None,
                 text_normalized: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None) -> None:
        """
        Initialize a RowHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current
               table.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
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
    def from_dict(cls, _dict: Dict) -> 'RowHeaders':
        """Initialize a RowHeaders object from a json dictionary."""
        args = {}
        valid_keys = [
            'cell_id', 'location', 'text', 'text_normalized', 'row_index_begin',
            'row_index_end', 'column_index_begin', 'column_index_end'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RowHeaders: '
                + ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Initialize a RowHeaders object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RowHeaders object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'RowHeaders') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RowHeaders') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SectionTitle():
    """
    The table's section title, if identified.

    :attr str text: (optional) The text of the section title, if identified.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a SectionTitle object.

        :param str text: (optional) The text of the section title, if identified.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SectionTitle':
        """Initialize a SectionTitle object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SectionTitle: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SectionTitle object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SectionTitle object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SectionTitle') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SectionTitle') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SectionTitles():
    """
    An array containing one object per section or subsection detected in the input
    document. Sections and subsections are not nested; instead, they are flattened out and
    can be placed back in order by using the `begin` and `end` values of the element and
    the `level` value of the section.

    :attr str text: (optional) The text of the section title, if identified.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr int level: (optional) An integer indicating the level at which the section
          is located in the input document. For example, `1` represents a top-level
          section, `2` represents a subsection within the level `1` section, and so forth.
    :attr List[ElementLocations] element_locations: (optional) An array of
          `location` objects that lists the locations of detected section titles.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: 'Location' = None,
                 level: int = None,
                 element_locations: List['ElementLocations'] = None) -> None:
        """
        Initialize a SectionTitles object.

        :param str text: (optional) The text of the section title, if identified.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param int level: (optional) An integer indicating the level at which the
               section is located in the input document. For example, `1` represents a
               top-level section, `2` represents a subsection within the level `1`
               section, and so forth.
        :param List[ElementLocations] element_locations: (optional) An array of
               `location` objects that lists the locations of detected section titles.
        """
        self.text = text
        self.location = location
        self.level = level
        self.element_locations = element_locations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SectionTitles':
        """Initialize a SectionTitles object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location', 'level', 'element_locations']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SectionTitles: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'level' in _dict:
            args['level'] = _dict.get('level')
        if 'element_locations' in _dict:
            args['element_locations'] = [
                ElementLocations._from_dict(x)
                for x in (_dict.get('element_locations'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SectionTitles object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self,
                   'element_locations') and self.element_locations is not None:
            _dict['element_locations'] = [
                x._to_dict() for x in self.element_locations
            ]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SectionTitles object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SectionTitles') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SectionTitles') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ShortDoc():
    """
    Brief information about the input document.

    :attr str title: (optional) The title of the input document, if identified.
    :attr str hash: (optional) The MD5 hash of the input document.
    """

    def __init__(self, *, title: str = None, hash: str = None) -> None:
        """
        Initialize a ShortDoc object.

        :param str title: (optional) The title of the input document, if
               identified.
        :param str hash: (optional) The MD5 hash of the input document.
        """
        self.title = title
        self.hash = hash

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ShortDoc':
        """Initialize a ShortDoc object from a json dictionary."""
        args = {}
        valid_keys = ['title', 'hash']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ShortDoc: '
                + ', '.join(bad_keys))
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'hash' in _dict:
            args['hash'] = _dict.get('hash')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ShortDoc object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'hash') and self.hash is not None:
            _dict['hash'] = self.hash
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ShortDoc object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ShortDoc') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ShortDoc') -> bool:
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
                 cell_id: str = None,
                 location: object = None,
                 text: str = None,
                 row_index_begin: int = None,
                 row_index_end: int = None,
                 column_index_begin: int = None,
                 column_index_end: int = None) -> None:
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
    def from_dict(cls, _dict: Dict) -> 'TableHeaders':
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
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TableHeaders') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableHeaders') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableReturn():
    """
    The analysis of the document's tables.

    :attr DocInfo document: (optional) Information about the parsed input document.
    :attr str model_id: (optional) The ID of the model used to extract the table
          contents. The value for table extraction is `tables`.
    :attr str model_version: (optional) The version of the `tables` model ID.
    :attr List[Tables] tables: (optional) Definitions of the tables identified in
          the input document.
    """

    def __init__(self,
                 *,
                 document: 'DocInfo' = None,
                 model_id: str = None,
                 model_version: str = None,
                 tables: List['Tables'] = None) -> None:
        """
        Initialize a TableReturn object.

        :param DocInfo document: (optional) Information about the parsed input
               document.
        :param str model_id: (optional) The ID of the model used to extract the
               table contents. The value for table extraction is `tables`.
        :param str model_version: (optional) The version of the `tables` model ID.
        :param List[Tables] tables: (optional) Definitions of the tables identified
               in the input document.
        """
        self.document = document
        self.model_id = model_id
        self.model_version = model_version
        self.tables = tables

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableReturn':
        """Initialize a TableReturn object from a json dictionary."""
        args = {}
        valid_keys = ['document', 'model_id', 'model_version', 'tables']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableReturn: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = DocInfo._from_dict(_dict.get('document'))
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'model_version' in _dict:
            args['model_version'] = _dict.get('model_version')
        if 'tables' in _dict:
            args['tables'] = [
                Tables._from_dict(x) for x in (_dict.get('tables'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableReturn object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'tables') and self.tables is not None:
            _dict['tables'] = [x._to_dict() for x in self.tables]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TableReturn') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableReturn') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableTitle():
    """
    If identified, the title or caption of the current table of the form `Table x.: ...`.
    Empty when no title is identified. When exposed, the `title` is also excluded from the
    `contexts` array of the same table.

    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr str text: (optional) The text of the identified table title or caption.
    """

    def __init__(self,
                 *,
                 location: 'Location' = None,
                 text: str = None) -> None:
        """
        Initialize a TableTitle object.

        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param str text: (optional) The text of the identified table title or
               caption.
        """
        self.location = location
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TableTitle':
        """Initialize a TableTitle object from a json dictionary."""
        args = {}
        valid_keys = ['location', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableTitle: '
                + ', '.join(bad_keys))
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableTitle object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TableTitle object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TableTitle') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TableTitle') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Tables():
    """
    The contents of the tables extracted from a document.

    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr str text: (optional) The textual contents of the current table from the
          input document without associated markup content.
    :attr SectionTitle section_title: (optional) The table's section title, if
          identified.
    :attr TableTitle title: (optional) If identified, the title or caption of the
          current table of the form `Table x.: ...`. Empty when no title is identified.
          When exposed, the `title` is also excluded from the `contexts` array of the same
          table.
    :attr List[TableHeaders] table_headers: (optional) An array of table-level cells
          that apply as headers to all the other cells in the current table.
    :attr List[RowHeaders] row_headers: (optional) An array of row-level cells, each
          applicable as a header to other cells in the same row as itself, of the current
          table.
    :attr List[ColumnHeaders] column_headers: (optional) An array of column-level
          cells, each applicable as a header to other cells in the same column as itself,
          of the current table.
    :attr List[BodyCells] body_cells: (optional) An array of cells that are neither
          table header nor column header nor row header cells, of the current table with
          corresponding row and column header associations.
    :attr List[Contexts] contexts: (optional) An array of objects that list text
          that is related to the table contents and that precedes or follows the current
          table.
    :attr List[KeyValuePair] key_value_pairs: (optional) An array of key-value pairs
          identified in the current table.
    """

    def __init__(self,
                 *,
                 location: 'Location' = None,
                 text: str = None,
                 section_title: 'SectionTitle' = None,
                 title: 'TableTitle' = None,
                 table_headers: List['TableHeaders'] = None,
                 row_headers: List['RowHeaders'] = None,
                 column_headers: List['ColumnHeaders'] = None,
                 body_cells: List['BodyCells'] = None,
                 contexts: List['Contexts'] = None,
                 key_value_pairs: List['KeyValuePair'] = None) -> None:
        """
        Initialize a Tables object.

        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param str text: (optional) The textual contents of the current table from
               the input document without associated markup content.
        :param SectionTitle section_title: (optional) The table's section title, if
               identified.
        :param TableTitle title: (optional) If identified, the title or caption of
               the current table of the form `Table x.: ...`. Empty when no title is
               identified. When exposed, the `title` is also excluded from the `contexts`
               array of the same table.
        :param List[TableHeaders] table_headers: (optional) An array of table-level
               cells that apply as headers to all the other cells in the current table.
        :param List[RowHeaders] row_headers: (optional) An array of row-level
               cells, each applicable as a header to other cells in the same row as
               itself, of the current table.
        :param List[ColumnHeaders] column_headers: (optional) An array of
               column-level cells, each applicable as a header to other cells in the same
               column as itself, of the current table.
        :param List[BodyCells] body_cells: (optional) An array of cells that are
               neither table header nor column header nor row header cells, of the current
               table with corresponding row and column header associations.
        :param List[Contexts] contexts: (optional) An array of objects that list
               text that is related to the table contents and that precedes or follows the
               current table.
        :param List[KeyValuePair] key_value_pairs: (optional) An array of key-value
               pairs identified in the current table.
        """
        self.location = location
        self.text = text
        self.section_title = section_title
        self.title = title
        self.table_headers = table_headers
        self.row_headers = row_headers
        self.column_headers = column_headers
        self.body_cells = body_cells
        self.contexts = contexts
        self.key_value_pairs = key_value_pairs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tables':
        """Initialize a Tables object from a json dictionary."""
        args = {}
        valid_keys = [
            'location', 'text', 'section_title', 'title', 'table_headers',
            'row_headers', 'column_headers', 'body_cells', 'contexts',
            'key_value_pairs'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Tables: ' +
                ', '.join(bad_keys))
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'section_title' in _dict:
            args['section_title'] = SectionTitle._from_dict(
                _dict.get('section_title'))
        if 'title' in _dict:
            args['title'] = TableTitle._from_dict(_dict.get('title'))
        if 'table_headers' in _dict:
            args['table_headers'] = [
                TableHeaders._from_dict(x) for x in (_dict.get('table_headers'))
            ]
        if 'row_headers' in _dict:
            args['row_headers'] = [
                RowHeaders._from_dict(x) for x in (_dict.get('row_headers'))
            ]
        if 'column_headers' in _dict:
            args['column_headers'] = [
                ColumnHeaders._from_dict(x)
                for x in (_dict.get('column_headers'))
            ]
        if 'body_cells' in _dict:
            args['body_cells'] = [
                BodyCells._from_dict(x) for x in (_dict.get('body_cells'))
            ]
        if 'contexts' in _dict:
            args['contexts'] = [
                Contexts._from_dict(x) for x in (_dict.get('contexts'))
            ]
        if 'key_value_pairs' in _dict:
            args['key_value_pairs'] = [
                KeyValuePair._from_dict(x)
                for x in (_dict.get('key_value_pairs'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tables object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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
        if hasattr(self, 'body_cells') and self.body_cells is not None:
            _dict['body_cells'] = [x._to_dict() for x in self.body_cells]
        if hasattr(self, 'contexts') and self.contexts is not None:
            _dict['contexts'] = [x._to_dict() for x in self.contexts]
        if hasattr(self,
                   'key_value_pairs') and self.key_value_pairs is not None:
            _dict['key_value_pairs'] = [
                x._to_dict() for x in self.key_value_pairs
            ]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tables object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Tables') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tables') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TerminationDates():
    """
    Termination dates identified in the input document.

    :attr str confidence_level: (optional) The confidence level in the
          identification of the termination date.
    :attr str text: (optional) The termination date.
    :attr str text_normalized: (optional) The normalized form of the termination
          date, which is listed as a string. This element is optional; it is returned only
          if normalized text exists.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    """

    def __init__(self,
                 *,
                 confidence_level: str = None,
                 text: str = None,
                 text_normalized: str = None,
                 provenance_ids: List[str] = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a TerminationDates object.

        :param str confidence_level: (optional) The confidence level in the
               identification of the termination date.
        :param str text: (optional) The termination date.
        :param str text_normalized: (optional) The normalized form of the
               termination date, which is listed as a string. This element is optional; it
               is returned only if normalized text exists.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TerminationDates':
        """Initialize a TerminationDates object from a json dictionary."""
        args = {}
        valid_keys = [
            'confidence_level', 'text', 'text_normalized', 'provenance_ids',
            'location'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TerminationDates: '
                + ', '.join(bad_keys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'text_normalized' in _dict:
            args['text_normalized'] = _dict.get('text_normalized')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TerminationDates object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'confidence_level') and self.confidence_level is not None:
            _dict['confidence_level'] = self.confidence_level
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self,
                   'text_normalized') and self.text_normalized is not None:
            _dict['text_normalized'] = self.text_normalized
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TerminationDates object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TerminationDates') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TerminationDates') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConfidenceLevelEnum(Enum):
        """
        The confidence level in the identification of the termination date.
        """
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"


class TypeLabel():
    """
    Identification of a specific type.

    :attr Label label: (optional) A pair of `nature` and `party` objects. The
          `nature` object identifies the effect of the element on the identified `party`,
          and the `party` object identifies the affected party.
    :attr List[str] provenance_ids: (optional) Hashed values that you can send to
          IBM to provide feedback or receive support.
    """

    def __init__(self,
                 *,
                 label: 'Label' = None,
                 provenance_ids: List[str] = None) -> None:
        """
        Initialize a TypeLabel object.

        :param Label label: (optional) A pair of `nature` and `party` objects. The
               `nature` object identifies the effect of the element on the identified
               `party`, and the `party` object identifies the affected party.
        :param List[str] provenance_ids: (optional) Hashed values that you can send
               to IBM to provide feedback or receive support.
        """
        self.label = label
        self.provenance_ids = provenance_ids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TypeLabel':
        """Initialize a TypeLabel object from a json dictionary."""
        args = {}
        valid_keys = ['label', 'provenance_ids']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TypeLabel: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = Label._from_dict(_dict.get('label'))
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TypeLabel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label._to_dict()
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TypeLabel object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TypeLabel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TypeLabel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TypeLabelComparison():
    """
    Identification of a specific type.

    :attr Label label: (optional) A pair of `nature` and `party` objects. The
          `nature` object identifies the effect of the element on the identified `party`,
          and the `party` object identifies the affected party.
    """

    def __init__(self, *, label: 'Label' = None) -> None:
        """
        Initialize a TypeLabelComparison object.

        :param Label label: (optional) A pair of `nature` and `party` objects. The
               `nature` object identifies the effect of the element on the identified
               `party`, and the `party` object identifies the affected party.
        """
        self.label = label

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TypeLabelComparison':
        """Initialize a TypeLabelComparison object from a json dictionary."""
        args = {}
        valid_keys = ['label']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TypeLabelComparison: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = Label._from_dict(_dict.get('label'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TypeLabelComparison object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TypeLabelComparison object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TypeLabelComparison') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TypeLabelComparison') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UnalignedElement():
    """
    Element that does not align semantically between two compared documents.

    :attr str document_label: (optional) The label assigned to the document by the
          value of the `file_1_label` or `file_2_label` parameters on the **Compare two
          documents** method.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr str text: (optional) The text of the element.
    :attr List[TypeLabelComparison] types: (optional) Description of the action
          specified by the element and whom it affects.
    :attr List[CategoryComparison] categories: (optional) List of functional
          categories into which the element falls; in other words, the subject matter of
          the element.
    :attr List[Attribute] attributes: (optional) List of document attributes.
    """

    def __init__(self,
                 *,
                 document_label: str = None,
                 location: 'Location' = None,
                 text: str = None,
                 types: List['TypeLabelComparison'] = None,
                 categories: List['CategoryComparison'] = None,
                 attributes: List['Attribute'] = None) -> None:
        """
        Initialize a UnalignedElement object.

        :param str document_label: (optional) The label assigned to the document by
               the value of the `file_1_label` or `file_2_label` parameters on the
               **Compare two documents** method.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param str text: (optional) The text of the element.
        :param List[TypeLabelComparison] types: (optional) Description of the
               action specified by the element and whom it affects.
        :param List[CategoryComparison] categories: (optional) List of functional
               categories into which the element falls; in other words, the subject matter
               of the element.
        :param List[Attribute] attributes: (optional) List of document attributes.
        """
        self.document_label = document_label
        self.location = location
        self.text = text
        self.types = types
        self.categories = categories
        self.attributes = attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UnalignedElement':
        """Initialize a UnalignedElement object from a json dictionary."""
        args = {}
        valid_keys = [
            'document_label', 'location', 'text', 'types', 'categories',
            'attributes'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UnalignedElement: '
                + ', '.join(bad_keys))
        if 'document_label' in _dict:
            args['document_label'] = _dict.get('document_label')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'types' in _dict:
            args['types'] = [
                TypeLabelComparison._from_dict(x) for x in (_dict.get('types'))
            ]
        if 'categories' in _dict:
            args['categories'] = [
                CategoryComparison._from_dict(x)
                for x in (_dict.get('categories'))
            ]
        if 'attributes' in _dict:
            args['attributes'] = [
                Attribute._from_dict(x) for x in (_dict.get('attributes'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UnalignedElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_label') and self.document_label is not None:
            _dict['document_label'] = self.document_label
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = [x._to_dict() for x in self.attributes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UnalignedElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'UnalignedElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UnalignedElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdatedLabelsIn():
    """
    The updated labeling from the input document, accounting for the submitted feedback.

    :attr List[TypeLabel] types: Description of the action specified by the element
          and whom it affects.
    :attr List[Category] categories: List of functional categories into which the
          element falls; in other words, the subject matter of the element.
    """

    def __init__(self, types: List['TypeLabel'],
                 categories: List['Category']) -> None:
        """
        Initialize a UpdatedLabelsIn object.

        :param List[TypeLabel] types: Description of the action specified by the
               element and whom it affects.
        :param List[Category] categories: List of functional categories into which
               the element falls; in other words, the subject matter of the element.
        """
        self.types = types
        self.categories = categories

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdatedLabelsIn':
        """Initialize a UpdatedLabelsIn object from a json dictionary."""
        args = {}
        valid_keys = ['types', 'categories']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UpdatedLabelsIn: '
                + ', '.join(bad_keys))
        if 'types' in _dict:
            args['types'] = [
                TypeLabel._from_dict(x) for x in (_dict.get('types'))
            ]
        else:
            raise ValueError(
                'Required property \'types\' not present in UpdatedLabelsIn JSON'
            )
        if 'categories' in _dict:
            args['categories'] = [
                Category._from_dict(x) for x in (_dict.get('categories'))
            ]
        else:
            raise ValueError(
                'Required property \'categories\' not present in UpdatedLabelsIn JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdatedLabelsIn object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdatedLabelsIn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'UpdatedLabelsIn') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdatedLabelsIn') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdatedLabelsOut():
    """
    The updated labeling from the input document, accounting for the submitted feedback.

    :attr List[TypeLabel] types: (optional) Description of the action specified by
          the element and whom it affects.
    :attr List[Category] categories: (optional) List of functional categories into
          which the element falls; in other words, the subject matter of the element.
    :attr str modification: (optional) The type of modification the feedback entry
          in the `updated_labels` array. Possible values are `added`, `not_changed`, and
          `removed`.
    """

    def __init__(self,
                 *,
                 types: List['TypeLabel'] = None,
                 categories: List['Category'] = None,
                 modification: str = None) -> None:
        """
        Initialize a UpdatedLabelsOut object.

        :param List[TypeLabel] types: (optional) Description of the action
               specified by the element and whom it affects.
        :param List[Category] categories: (optional) List of functional categories
               into which the element falls; in other words, the subject matter of the
               element.
        :param str modification: (optional) The type of modification the feedback
               entry in the `updated_labels` array. Possible values are `added`,
               `not_changed`, and `removed`.
        """
        self.types = types
        self.categories = categories
        self.modification = modification

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdatedLabelsOut':
        """Initialize a UpdatedLabelsOut object from a json dictionary."""
        args = {}
        valid_keys = ['types', 'categories', 'modification']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UpdatedLabelsOut: '
                + ', '.join(bad_keys))
        if 'types' in _dict:
            args['types'] = [
                TypeLabel._from_dict(x) for x in (_dict.get('types'))
            ]
        if 'categories' in _dict:
            args['categories'] = [
                Category._from_dict(x) for x in (_dict.get('categories'))
            ]
        if 'modification' in _dict:
            args['modification'] = _dict.get('modification')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdatedLabelsOut object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'modification') and self.modification is not None:
            _dict['modification'] = self.modification
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdatedLabelsOut object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'UpdatedLabelsOut') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdatedLabelsOut') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModificationEnum(Enum):
        """
        The type of modification the feedback entry in the `updated_labels` array.
        Possible values are `added`, `not_changed`, and `removed`.
        """
        ADDED = "added"
        NOT_CHANGED = "not_changed"
        REMOVED = "removed"


class Value():
    """
    A value in a key-value pair.

    :attr str cell_id: (optional) The unique ID of the value in the table.
    :attr Location location: (optional) The numeric location of the identified
          element in the document, represented with two integers labeled `begin` and
          `end`.
    :attr str text: (optional) The text content of the table cell without HTML
          markup.
    """

    def __init__(self,
                 *,
                 cell_id: str = None,
                 location: 'Location' = None,
                 text: str = None) -> None:
        """
        Initialize a Value object.

        :param str cell_id: (optional) The unique ID of the value in the table.
        :param Location location: (optional) The numeric location of the identified
               element in the document, represented with two integers labeled `begin` and
               `end`.
        :param str text: (optional) The text content of the table cell without HTML
               markup.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Value':
        """Initialize a Value object from a json dictionary."""
        args = {}
        valid_keys = ['cell_id', 'location', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Value: ' +
                ', '.join(bad_keys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Value object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cell_id') and self.cell_id is not None:
            _dict['cell_id'] = self.cell_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Value object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Value') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Value') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
