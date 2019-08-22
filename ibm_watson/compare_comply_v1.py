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
IBM Watson&trade; Compare and Comply analyzes governing documents to provide details about
critical aspects of the documents.
"""

from __future__ import absolute_import

import json
from .common import get_sdk_headers
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime
from os.path import basename

##############################################################################
# Service
##############################################################################


class CompareComplyV1(BaseService):
    """The Compare Comply V1 service."""

    default_url = 'https://gateway.watsonplatform.net/compare-comply/api'

    def __init__(
            self,
            version,
            url=default_url,
            iam_apikey=None,
            iam_access_token=None,
            iam_url=None,
            iam_client_id=None,
            iam_client_secret=None,
            icp4d_access_token=None,
            icp4d_url=None,
            authentication_type=None,
            username=None,
            password=None,
    ):
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

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway.watsonplatform.net/compare-comply/api/compare-comply/api").
               The base url may differ between IBM Cloud regions.

        :param str username: The username used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of IBM Cloud. When running on
               IBM Cloud, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        :param str password: The password used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of IBM Cloud. When running on
               IBM Cloud, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        :param str iam_apikey: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.cloud.ibm.com/identity/token'.

        :param str iam_client_id: An optional client_id value to use when interacting with the IAM service.

        :param str iam_client_secret: An optional client_secret value to use when interacting with the IAM service.

        :param str icp4d_access_token:  A ICP4D(IBM Cloud Pak for Data) access token is
               fully managed by the application. Responsibility falls on the application to
               refresh the token, either before it expires or reactively upon receiving a 401
               from the service as any requests made with an expired token will fail.

        :param str icp4d_url: In order to use an SDK-managed token with ICP4D authentication, this
               URL must be passed in.

        :param str authentication_type: Specifies the authentication pattern to use. Values that it
               takes are basic, iam or icp4d.
        """

        BaseService.__init__(
            self,
            vcap_services_name='compare-comply',
            url=url,
            username=username,
            password=password,
            iam_apikey=iam_apikey,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            iam_client_id=iam_client_id,
            iam_client_secret=iam_client_secret,
            use_vcap_services=True,
            display_name='Compare Comply',
            icp4d_access_token=icp4d_access_token,
            icp4d_url=icp4d_url,
            authentication_type=authentication_type)
        self.version = version

    #########################
    # HTML conversion
    #########################

    def convert_to_html(self,
                        file,
                        filename=None,
                        file_content_type=None,
                        model=None,
                        **kwargs):
        """
        Convert document to HTML.

        Converts a document to HTML.

        :param file file: The document to convert.
        :param str filename: The filename for file.
        :param str file_content_type: The content type of file.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file is None:
            raise ValueError('file must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'convert_to_html')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        form_data = {}
        if not filename and hasattr(file, 'name'):
            filename = basename(file.name)
        if not filename:
            raise ValueError('filename must be provided')
        form_data['file'] = (filename, file, file_content_type or
                             'application/octet-stream')

        url = '/v1/html_conversion'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
            accept_json=True)
        return response

    #########################
    # Element classification
    #########################

    def classify_elements(self,
                          file,
                          file_content_type=None,
                          model=None,
                          **kwargs):
        """
        Classify the elements of a document.

        Analyzes the structural and semantic elements of a document.

        :param file file: The document to classify.
        :param str file_content_type: The content type of file.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file is None:
            raise ValueError('file must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1',
                                      'classify_elements')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        form_data = {}
        form_data['file'] = (None, file, file_content_type or
                             'application/octet-stream')

        url = '/v1/element_classification'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
            accept_json=True)
        return response

    #########################
    # Tables
    #########################

    def extract_tables(self, file, file_content_type=None, model=None,
                       **kwargs):
        """
        Extract a document's tables.

        Analyzes the tables in a document.

        :param file file: The document on which to run table extraction.
        :param str file_content_type: The content type of file.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if file is None:
            raise ValueError('file must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'extract_tables')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        form_data = {}
        form_data['file'] = (None, file, file_content_type or
                             'application/octet-stream')

        url = '/v1/tables'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
            accept_json=True)
        return response

    #########################
    # Comparison
    #########################

    def compare_documents(self,
                          file_1,
                          file_2,
                          file_1_content_type=None,
                          file_2_content_type=None,
                          file_1_label=None,
                          file_2_label=None,
                          model=None,
                          **kwargs):
        """
        Compare two documents.

        Compares two input documents. Documents must be in the same format.

        :param file file_1: The first document to compare.
        :param file file_2: The second document to compare.
        :param str file_1_content_type: The content type of file_1.
        :param str file_2_content_type: The content type of file_2.
        :param str file_1_label: A text label for the first document.
        :param str file_2_label: A text label for the second document.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
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
        sdk_headers = get_sdk_headers('compare-comply', 'V1',
                                      'compare_documents')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'file_1_label': file_1_label,
            'file_2_label': file_2_label,
            'model': model
        }

        form_data = {}
        form_data['file_1'] = (None, file_1, file_1_content_type or
                               'application/octet-stream')
        form_data['file_2'] = (None, file_2, file_2_content_type or
                               'application/octet-stream')

        url = '/v1/comparison'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
            accept_json=True)
        return response

    #########################
    # Feedback
    #########################

    def add_feedback(self, feedback_data, user_id=None, comment=None, **kwargs):
        """
        Add feedback.

        Adds feedback in the form of _labels_ from a subject-matter expert (SME) to a
        governing document.
        **Important:** Feedback is not immediately incorporated into the training model,
        nor is it guaranteed to be incorporated at a later date. Instead, submitted
        feedback is used to suggest future updates to the training model.

        :param FeedbackDataInput feedback_data: Feedback data for submission.
        :param str user_id: An optional string identifying the user.
        :param str comment: An optional comment on or description of the feedback.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if feedback_data is None:
            raise ValueError('feedback_data must be provided')
        feedback_data = self._convert_model(feedback_data, FeedbackDataInput)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'add_feedback')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'feedback_data': feedback_data,
            'user_id': user_id,
            'comment': comment
        }

        url = '/v1/feedback'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    def list_feedback(self,
                      feedback_type=None,
                      before=None,
                      after=None,
                      document_title=None,
                      model_id=None,
                      model_version=None,
                      category_removed=None,
                      category_added=None,
                      category_not_changed=None,
                      type_removed=None,
                      type_added=None,
                      type_not_changed=None,
                      page_limit=None,
                      cursor=None,
                      sort=None,
                      include_total=None,
                      **kwargs):
        """
        List the feedback in a document.

        Lists the feedback in a document.

        :param str feedback_type: An optional string that filters the output to include
        only feedback with the specified feedback type. The only permitted value is
        `element_classification`.
        :param date before: An optional string in the format `YYYY-MM-DD` that filters the
        output to include only feedback that was added before the specified date.
        :param date after: An optional string in the format `YYYY-MM-DD` that filters the
        output to include only feedback that was added after the specified date.
        :param str document_title: An optional string that filters the output to include
        only feedback from the document with the specified `document_title`.
        :param str model_id: An optional string that filters the output to include only
        feedback with the specified `model_id`. The only permitted value is `contracts`.
        :param str model_version: An optional string that filters the output to include
        only feedback with the specified `model_version`.
        :param str category_removed: An optional string in the form of a comma-separated
        list of categories. If it is specified, the service filters the output to include
        only feedback that has at least one category from the list removed.
        :param str category_added: An optional string in the form of a comma-separated
        list of categories. If this is specified, the service filters the output to
        include only feedback that has at least one category from the list added.
        :param str category_not_changed: An optional string in the form of a
        comma-separated list of categories. If this is specified, the service filters the
        output to include only feedback that has at least one category from the list
        unchanged.
        :param str type_removed: An optional string of comma-separated `nature`:`party`
        pairs. If this is specified, the service filters the output to include only
        feedback that has at least one `nature`:`party` pair from the list removed.
        :param str type_added: An optional string of comma-separated `nature`:`party`
        pairs. If this is specified, the service filters the output to include only
        feedback that has at least one `nature`:`party` pair from the list removed.
        :param str type_not_changed: An optional string of comma-separated
        `nature`:`party` pairs. If this is specified, the service filters the output to
        include only feedback that has at least one `nature`:`party` pair from the list
        unchanged.
        :param int page_limit: An optional integer specifying the number of documents that
        you want the service to return.
        :param str cursor: An optional string that returns the set of documents after the
        previous set. Use this parameter with the `page_limit` parameter.
        :param str sort: An optional comma-separated list of fields in the document to
        sort on. You can optionally specify the sort direction by prefixing the value of
        the field with `-` for descending order or `+` for ascending order (the default).
        Currently permitted sorting fields are `created`, `user_id`, and `document_title`.
        :param bool include_total: An optional boolean value. If specified as `true`, the
        `pagination` object in the output includes a value called `total` that gives the
        total count of feedback created.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'list_feedback')
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
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_feedback(self, feedback_id, model=None, **kwargs):
        """
        Get a specified feedback entry.

        Gets a feedback entry with a specified `feedback_id`.

        :param str feedback_id: A string that specifies the feedback entry to be included
        in the output.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if feedback_id is None:
            raise ValueError('feedback_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'get_feedback')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        url = '/v1/feedback/{0}'.format(*self._encode_path_vars(feedback_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def delete_feedback(self, feedback_id, model=None, **kwargs):
        """
        Delete a specified feedback entry.

        Deletes a feedback entry with a specified `feedback_id`.

        :param str feedback_id: A string that specifies the feedback entry to be deleted
        from the document.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if feedback_id is None:
            raise ValueError('feedback_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'delete_feedback')
        headers.update(sdk_headers)

        params = {'version': self.version, 'model': model}

        url = '/v1/feedback/{0}'.format(*self._encode_path_vars(feedback_id))
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    #########################
    # Batches
    #########################

    def create_batch(self,
                     function,
                     input_credentials_file,
                     input_bucket_location,
                     input_bucket_name,
                     output_credentials_file,
                     output_bucket_location,
                     output_bucket_name,
                     model=None,
                     **kwargs):
        """
        Submit a batch-processing request.

        Run Compare and Comply methods over a collection of input documents.
        **Important:** Batch processing requires the use of the [IBM Cloud Object Storage
        service](https://cloud.ibm.com/docs/services/cloud-object-storage?topic=cloud-object-storage-about#about-ibm-cloud-object-storage).
        The use of IBM Cloud Object Storage with Compare and Comply is discussed at [Using
        batch
        processing](https://cloud.ibm.com/docs/services/compare-comply?topic=compare-comply-batching#before-you-batch).

        :param str function: The Compare and Comply method to run across the submitted
        input documents.
        :param file input_credentials_file: A JSON file containing the input Cloud Object
        Storage credentials. At a minimum, the credentials must enable `READ` permissions
        on the bucket defined by the `input_bucket_name` parameter.
        :param str input_bucket_location: The geographical location of the Cloud Object
        Storage input bucket as listed on the **Endpoint** tab of your Cloud Object
        Storage instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
        :param str input_bucket_name: The name of the Cloud Object Storage input bucket.
        :param file output_credentials_file: A JSON file that lists the Cloud Object
        Storage output credentials. At a minimum, the credentials must enable `READ` and
        `WRITE` permissions on the bucket defined by the `output_bucket_name` parameter.
        :param str output_bucket_location: The geographical location of the Cloud Object
        Storage output bucket as listed on the **Endpoint** tab of your Cloud Object
        Storage instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
        :param str output_bucket_name: The name of the Cloud Object Storage output bucket.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
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
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'create_batch')
        headers.update(sdk_headers)

        params = {'version': self.version, 'function': function, 'model': model}

        form_data = {}
        form_data['input_credentials_file'] = (None, input_credentials_file,
                                               'application/json')
        form_data['input_bucket_location'] = (None, input_bucket_location,
                                              'text/plain')
        form_data['input_bucket_name'] = (None, input_bucket_name, 'text/plain')
        form_data['output_credentials_file'] = (None, output_credentials_file,
                                                'application/json')
        form_data['output_bucket_location'] = (None, output_bucket_location,
                                               'text/plain')
        form_data['output_bucket_name'] = (None, output_bucket_name,
                                           'text/plain')

        url = '/v1/batches'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
            accept_json=True)
        return response

    def list_batches(self, **kwargs):
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
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'list_batches')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/batches'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_batch(self, batch_id, **kwargs):
        """
        Get information about a specific batch-processing job.

        Gets information about a batch-processing job with a specified ID.

        :param str batch_id: The ID of the batch-processing job whose information you want
        to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if batch_id is None:
            raise ValueError('batch_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'get_batch')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/batches/{0}'.format(*self._encode_path_vars(batch_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_batch(self, batch_id, action, model=None, **kwargs):
        """
        Update a pending or active batch-processing job.

        Updates a pending or active batch-processing job. You can rescan the input bucket
        to check for new documents or cancel a job.

        :param str batch_id: The ID of the batch-processing job you want to update.
        :param str action: The action you want to perform on the specified
        batch-processing job.
        :param str model: The analysis model to be used by the service. For the **Element
        classification** and **Compare two documents** methods, the default is
        `contracts`. For the **Extract tables** method, the default is `tables`. These
        defaults apply to the standalone methods as well as to the methods' use in
        batch-processing requests.
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
        sdk_headers = get_sdk_headers('compare-comply', 'V1', 'update_batch')
        headers.update(sdk_headers)

        params = {'version': self.version, 'action': action, 'model': model}

        url = '/v1/batches/{0}'.format(*self._encode_path_vars(batch_id))
        response = self.request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class Address(object):
    """
    A party's address.

    :attr str text: (optional) A string listing the address.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self, text=None, location=None):
        """
        Initialize a Address object.

        :param str text: (optional) A string listing the address.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Address object from a json dictionary."""
        args = {}
        validKeys = ['text', 'location']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Address: ' +
                ', '.join(badKeys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Return a `str` version of this Address object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AlignedElement(object):
    """
    AlignedElement.

    :attr list[ElementPair] element_pair: (optional) Identifies two elements that
    semantically align between the compared documents.
    :attr bool identical_text: (optional) Specifies whether the aligned element is
    identical. Elements are considered identical despite minor differences such as leading
    punctuation, end-of-sentence punctuation, whitespace, the presence or absence of
    definite or indefinite articles, and others.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr bool significant_elements: (optional) Indicates that the elements aligned are
    contractual clauses of significance.
    """

    def __init__(self,
                 element_pair=None,
                 identical_text=None,
                 provenance_ids=None,
                 significant_elements=None):
        """
        Initialize a AlignedElement object.

        :param list[ElementPair] element_pair: (optional) Identifies two elements that
        semantically align between the compared documents.
        :param bool identical_text: (optional) Specifies whether the aligned element is
        identical. Elements are considered identical despite minor differences such as
        leading punctuation, end-of-sentence punctuation, whitespace, the presence or
        absence of definite or indefinite articles, and others.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param bool significant_elements: (optional) Indicates that the elements aligned
        are contractual clauses of significance.
        """
        self.element_pair = element_pair
        self.identical_text = identical_text
        self.provenance_ids = provenance_ids
        self.significant_elements = significant_elements

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlignedElement object from a json dictionary."""
        args = {}
        validKeys = [
            'element_pair', 'identical_text', 'provenance_ids',
            'significant_elements'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AlignedElement: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this AlignedElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Attribute(object):
    """
    List of document attributes.

    :attr str type: (optional) The type of attribute.
    :attr str text: (optional) The text associated with the attribute.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self, type=None, text=None, location=None):
        """
        Initialize a Attribute object.

        :param str type: (optional) The type of attribute.
        :param str text: (optional) The text associated with the attribute.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.type = type
        self.text = text
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Attribute object from a json dictionary."""
        args = {}
        validKeys = ['type', 'text', 'location']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Attribute: '
                + ', '.join(badKeys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Return a `str` version of this Attribute object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BatchStatus(object):
    """
    The batch-request status.

    :attr str function: (optional) The method to be run against the documents. Possible
    values are `html_conversion`, `element_classification`, and `tables`.
    :attr str input_bucket_location: (optional) The geographical location of the Cloud
    Object Storage input bucket as listed on the **Endpoint** tab of your COS instance;
    for example, `us-geo`, `eu-geo`, or `ap-geo`.
    :attr str input_bucket_name: (optional) The name of the Cloud Object Storage input
    bucket.
    :attr str output_bucket_location: (optional) The geographical location of the Cloud
    Object Storage output bucket as listed on the **Endpoint** tab of your COS instance;
    for example, `us-geo`, `eu-geo`, or `ap-geo`.
    :attr str output_bucket_name: (optional) The name of the Cloud Object Storage output
    bucket.
    :attr str batch_id: (optional) The unique identifier for the batch request.
    :attr DocCounts document_counts: (optional) Document counts.
    :attr str status: (optional) The status of the batch request.
    :attr datetime created: (optional) The creation time of the batch request.
    :attr datetime updated: (optional) The time of the most recent update to the batch
    request.
    """

    def __init__(self,
                 function=None,
                 input_bucket_location=None,
                 input_bucket_name=None,
                 output_bucket_location=None,
                 output_bucket_name=None,
                 batch_id=None,
                 document_counts=None,
                 status=None,
                 created=None,
                 updated=None):
        """
        Initialize a BatchStatus object.

        :param str function: (optional) The method to be run against the documents.
        Possible values are `html_conversion`, `element_classification`, and `tables`.
        :param str input_bucket_location: (optional) The geographical location of the
        Cloud Object Storage input bucket as listed on the **Endpoint** tab of your COS
        instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
        :param str input_bucket_name: (optional) The name of the Cloud Object Storage
        input bucket.
        :param str output_bucket_location: (optional) The geographical location of the
        Cloud Object Storage output bucket as listed on the **Endpoint** tab of your COS
        instance; for example, `us-geo`, `eu-geo`, or `ap-geo`.
        :param str output_bucket_name: (optional) The name of the Cloud Object Storage
        output bucket.
        :param str batch_id: (optional) The unique identifier for the batch request.
        :param DocCounts document_counts: (optional) Document counts.
        :param str status: (optional) The status of the batch request.
        :param datetime created: (optional) The creation time of the batch request.
        :param datetime updated: (optional) The time of the most recent update to the
        batch request.
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
    def _from_dict(cls, _dict):
        """Initialize a BatchStatus object from a json dictionary."""
        args = {}
        validKeys = [
            'function', 'input_bucket_location', 'input_bucket_name',
            'output_bucket_location', 'output_bucket_name', 'batch_id',
            'document_counts', 'status', 'created', 'updated'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class BatchStatus: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this BatchStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Batches(object):
    """
    The results of a successful **List Batches** request.

    :attr list[BatchStatus] batches: (optional) A list of the status of all batch
    requests.
    """

    def __init__(self, batches=None):
        """
        Initialize a Batches object.

        :param list[BatchStatus] batches: (optional) A list of the status of all batch
        requests.
        """
        self.batches = batches

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Batches object from a json dictionary."""
        args = {}
        validKeys = ['batches']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Batches: ' +
                ', '.join(badKeys))
        if 'batches' in _dict:
            args['batches'] = [
                BatchStatus._from_dict(x) for x in (_dict.get('batches'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'batches') and self.batches is not None:
            _dict['batches'] = [x._to_dict() for x in self.batches]
        return _dict

    def __str__(self):
        """Return a `str` version of this Batches object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BodyCells(object):
    """
    Cells that are not table header, column header, or row header cells.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The textual contents of this cell from the input document
    without associated markup content.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row` location
    in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row` location in
    the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's `column`
    location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
    location in the current table.
    :attr list[str] row_header_ids: (optional) An array that contains the `id` value of a
    row header that is applicable to this body cell.
    :attr list[str] row_header_texts: (optional) An array that contains the `text` value
    of a row header that is applicable to this body cell.
    :attr list[str] row_header_texts_normalized: (optional) If you provide customization
    input, the normalized version of the row header texts according to the customization;
    otherwise, the same value as `row_header_texts`.
    :attr list[str] column_header_ids: (optional) An array that contains the `id` value of
    a column header that is applicable to the current cell.
    :attr list[str] column_header_texts: (optional) An array that contains the `text`
    value of a column header that is applicable to the current cell.
    :attr list[str] column_header_texts_normalized: (optional) If you provide
    customization input, the normalized version of the column header texts according to
    the customization; otherwise, the same value as `column_header_texts`.
    :attr list[Attribute] attributes: (optional)
    """

    def __init__(self,
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
        Initialize a BodyCells object.

        :param str cell_id: (optional) The unique ID of the cell in the current table.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The textual contents of this cell from the input
        document without associated markup content.
        :param int row_index_begin: (optional) The `begin` index of this cell's `row`
        location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row` location
        in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
        `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's `column`
        location in the current table.
        :param list[str] row_header_ids: (optional) An array that contains the `id` value
        of a row header that is applicable to this body cell.
        :param list[str] row_header_texts: (optional) An array that contains the `text`
        value of a row header that is applicable to this body cell.
        :param list[str] row_header_texts_normalized: (optional) If you provide
        customization input, the normalized version of the row header texts according to
        the customization; otherwise, the same value as `row_header_texts`.
        :param list[str] column_header_ids: (optional) An array that contains the `id`
        value of a column header that is applicable to the current cell.
        :param list[str] column_header_texts: (optional) An array that contains the `text`
        value of a column header that is applicable to the current cell.
        :param list[str] column_header_texts_normalized: (optional) If you provide
        customization input, the normalized version of the column header texts according
        to the customization; otherwise, the same value as `column_header_texts`.
        :param list[Attribute] attributes: (optional)
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
        """Initialize a BodyCells object from a json dictionary."""
        args = {}
        validKeys = [
            'cell_id', 'location', 'text', 'row_index_begin', 'row_index_end',
            'column_index_begin', 'column_index_end', 'row_header_ids',
            'row_header_texts', 'row_header_texts_normalized',
            'column_header_ids', 'column_header_texts',
            'column_header_texts_normalized', 'attributes'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class BodyCells: '
                + ', '.join(badKeys))
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

    def __str__(self):
        """Return a `str` version of this BodyCells object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Category(object):
    """
    Information defining an element's subject matter.

    :attr str label: (optional) The category of the associated element.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    """

    def __init__(self, label=None, provenance_ids=None):
        """
        Initialize a Category object.

        :param str label: (optional) The category of the associated element.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        """
        self.label = label
        self.provenance_ids = provenance_ids

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Category object from a json dictionary."""
        args = {}
        validKeys = ['label', 'provenance_ids']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Category: '
                + ', '.join(badKeys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        return _dict

    def __str__(self):
        """Return a `str` version of this Category object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoryComparison(object):
    """
    Information defining an element's subject matter.

    :attr str label: (optional) The category of the associated element.
    """

    def __init__(self, label=None):
        """
        Initialize a CategoryComparison object.

        :param str label: (optional) The category of the associated element.
        """
        self.label = label

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoryComparison object from a json dictionary."""
        args = {}
        validKeys = ['label']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CategoryComparison: '
                + ', '.join(badKeys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        return _dict

    def __str__(self):
        """Return a `str` version of this CategoryComparison object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifyReturn(object):
    """
    The analysis of objects returned by the **Element classification** method.

    :attr Document document: (optional) Basic information about the input document.
    :attr str model_id: (optional) The analysis model used to classify the input document.
    For the **Element classification** method, the only valid value is `contracts`.
    :attr str model_version: (optional) The version of the analysis model identified by
    the value of the `model_id` key.
    :attr list[Element] elements: (optional) Document elements identified by the service.
    :attr list[EffectiveDates] effective_dates: (optional) The date or dates on which the
    document becomes effective.
    :attr list[ContractAmts] contract_amounts: (optional) The monetary amounts that
    identify the total amount of the contract that needs to be paid from one party to
    another.
    :attr list[TerminationDates] termination_dates: (optional) The dates on which the
    document is to be terminated.
    :attr list[ContractTypes] contract_types: (optional) The contract type as declared in
    the document.
    :attr list[ContractTerms] contract_terms: (optional) The durations of the contract.
    :attr list[PaymentTerms] payment_terms: (optional) The document's payment durations.
    :attr list[ContractCurrencies] contract_currencies: (optional) The contract currencies
    as declared in the document.
    :attr list[Tables] tables: (optional) Definition of tables identified in the input
    document.
    :attr DocStructure document_structure: (optional) The structure of the input document.
    :attr list[Parties] parties: (optional) Definitions of the parties identified in the
    input document.
    """

    def __init__(self,
                 document=None,
                 model_id=None,
                 model_version=None,
                 elements=None,
                 tables=None,
                 document_structure=None,
                 parties=None,
                 effective_dates=None,
                 contract_amounts=None,
                 termination_dates=None,
                 contract_types=None,
                 contract_terms=None,
                 payment_terms=None,
                 contract_currencies=None,
                ):
        """
        Initialize a ClassifyReturn object.

        :param Document document: (optional) Basic information about the input document.
        :param str model_id: (optional) The analysis model used to classify the input
        document. For the **Element classification** method, the only valid value is
        `contracts`.
        :param str model_version: (optional) The version of the analysis model identified
        by the value of the `model_id` key.
        :param list[Element] elements: (optional) Document elements identified by the
        service.
        :param list[EffectiveDates] effective_dates: (optional) The date or dates on which
        the document becomes effective.
        :param list[ContractAmts] contract_amounts: (optional) The monetary amounts that
        identify the total amount of the contract that needs to be paid from one party to
        another.
        :param list[TerminationDates] termination_dates: (optional) The dates on which the
        document is to be terminated.
        :param list[ContractTypes] contract_types: (optional) The contract type as
        declared in the document.
        :param list[ContractTerms] contract_terms: (optional) The durations of the
        contract.
        :param list[PaymentTerms] payment_terms: (optional) The document's payment
        durations.
        :param list[ContractCurrencies] contract_currencies: (optional) The contract
        currencies as declared in the document.
        :param list[Tables] tables: (optional) Definition of tables identified in the
        input document.
        :param DocStructure document_structure: (optional) The structure of the input
        document.
        :param list[Parties] parties: (optional) Definitions of the parties identified in
        the input document.
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
    def _from_dict(cls, _dict):
        """Initialize a ClassifyReturn object from a json dictionary."""
        args = {}
        validKeys = [
            'document', 'model_id', 'model_version', 'elements',
            'effective_dates', 'contract_amounts', 'termination_dates',
            'contract_types', 'contract_terms', 'payment_terms',
            'contract_currencies', 'tables', 'document_structure', 'parties'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifyReturn: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ClassifyReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ColumnHeaders(object):
    """
    Column-level cells, each applicable as a header to other cells in the same column as
    itself, of the current table.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr object location: (optional) The location of the column header cell in the
    current table as defined by its `begin` and `end` offsets, respectfully, in the input
    document.
    :attr str text: (optional) The textual contents of this cell from the input document
    without associated markup content.
    :attr str text_normalized: (optional) If you provide customization input, the
    normalized version of the cell text according to the customization; otherwise, the
    same value as `text`.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row` location
    in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row` location in
    the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's `column`
    location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
    location in the current table.
    """

    def __init__(self,
                 cell_id=None,
                 location=None,
                 text=None,
                 text_normalized=None,
                 row_index_begin=None,
                 row_index_end=None,
                 column_index_begin=None,
                 column_index_end=None):
        """
        Initialize a ColumnHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current table.
        :param object location: (optional) The location of the column header cell in the
        current table as defined by its `begin` and `end` offsets, respectfully, in the
        input document.
        :param str text: (optional) The textual contents of this cell from the input
        document without associated markup content.
        :param str text_normalized: (optional) If you provide customization input, the
        normalized version of the cell text according to the customization; otherwise, the
        same value as `text`.
        :param int row_index_begin: (optional) The `begin` index of this cell's `row`
        location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row` location
        in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
        `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's `column`
        location in the current table.
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
        """Initialize a ColumnHeaders object from a json dictionary."""
        args = {}
        validKeys = [
            'cell_id', 'location', 'text', 'text_normalized', 'row_index_begin',
            'row_index_end', 'column_index_begin', 'column_index_end'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ColumnHeaders: '
                + ', '.join(badKeys))
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
        """Return a `str` version of this ColumnHeaders object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CompareReturn(object):
    """
    The comparison of the two submitted documents.

    :attr str model_id: (optional) The analysis model used to compare the input documents.
    For the **Compare two documents** method, the only valid value is `contracts`.
    :attr str model_version: (optional) The version of the analysis model identified by
    the value of the `model_id` key.
    :attr list[Document] documents: (optional) Information about the documents being
    compared.
    :attr list[AlignedElement] aligned_elements: (optional) A list of pairs of elements
    that semantically align between the compared documents.
    :attr list[UnalignedElement] unaligned_elements: (optional) A list of elements that do
    not semantically align between the compared documents.
    """

    def __init__(self,
                 model_id=None,
                 model_version=None,
                 documents=None,
                 aligned_elements=None,
                 unaligned_elements=None):
        """
        Initialize a CompareReturn object.

        :param str model_id: (optional) The analysis model used to compare the input
        documents. For the **Compare two documents** method, the only valid value is
        `contracts`.
        :param str model_version: (optional) The version of the analysis model identified
        by the value of the `model_id` key.
        :param list[Document] documents: (optional) Information about the documents being
        compared.
        :param list[AlignedElement] aligned_elements: (optional) A list of pairs of
        elements that semantically align between the compared documents.
        :param list[UnalignedElement] unaligned_elements: (optional) A list of elements
        that do not semantically align between the compared documents.
        """
        self.model_id = model_id
        self.model_version = model_version
        self.documents = documents
        self.aligned_elements = aligned_elements
        self.unaligned_elements = unaligned_elements

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CompareReturn object from a json dictionary."""
        args = {}
        validKeys = [
            'model_id', 'model_version', 'documents', 'aligned_elements',
            'unaligned_elements'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CompareReturn: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this CompareReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Contact(object):
    """
    A contact.

    :attr str name: (optional) A string listing the name of the contact.
    :attr str role: (optional) A string listing the role of the contact.
    """

    def __init__(self, name=None, role=None):
        """
        Initialize a Contact object.

        :param str name: (optional) A string listing the name of the contact.
        :param str role: (optional) A string listing the role of the contact.
        """
        self.name = name
        self.role = role

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Contact object from a json dictionary."""
        args = {}
        validKeys = ['name', 'role']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Contact: ' +
                ', '.join(badKeys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'role' in _dict:
            args['role'] = _dict.get('role')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'role') and self.role is not None:
            _dict['role'] = self.role
        return _dict

    def __str__(self):
        """Return a `str` version of this Contact object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Contexts(object):
    """
    Text that is related to the contents of the table and that precedes or follows the
    current table.

    :attr str text: (optional) The related text.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self, text=None, location=None):
        """
        Initialize a Contexts object.

        :param str text: (optional) The related text.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Contexts object from a json dictionary."""
        args = {}
        validKeys = ['text', 'location']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Contexts: '
                + ', '.join(badKeys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Return a `str` version of this Contexts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractAmts(object):
    """
    A monetary amount identified in the input document.

    :attr str confidence_level: (optional) The confidence level in the identification of
    the contract amount.
    :attr str text: (optional) The monetary amount.
    :attr str text_normalized: (optional) The normalized form of the amount, which is
    listed as a string. This element is optional; it is returned only if normalized text
    exists.
    :attr Interpretation interpretation: (optional) The details of the normalized text, if
    applicable. This element is optional; it is returned only if normalized text exists.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self,
                 text=None,
                 confidence_level=None,
                 location=None,
                 text_normalized=None,
                 interpretation=None,
                 provenance_ids=None):
        """
        Initialize a ContractAmts object.

        :param str confidence_level: (optional) The confidence level in the identification
        of the contract amount.
        :param str text: (optional) The monetary amount.
        :param str text_normalized: (optional) The normalized form of the amount, which is
        listed as a string. This element is optional; it is returned only if normalized
        text exists.
        :param Interpretation interpretation: (optional) The details of the normalized
        text, if applicable. This element is optional; it is returned only if normalized
        text exists.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.interpretation = interpretation
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractAmts object from a json dictionary."""
        args = {}
        validKeys = [
            'confidence_level', 'text', 'text_normalized', 'interpretation',
            'provenance_ids', 'location'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractAmts: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ContractAmts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractCurrencies(object):
    """
    The contract currencies that are declared in the document.

    :attr str confidence_level: (optional) The confidence level in the identification of
    the contract currency.
    :attr str text: (optional) The contract currency.
    :attr str text_normalized: (optional) The normalized form of the contract currency,
    which is listed as a string in
    [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) format. This element is
    optional; it is returned only if normalized text exists.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self,
                 confidence_level=None,
                 text=None,
                 text_normalized=None,
                 provenance_ids=None,
                 location=None):
        """
        Initialize a ContractCurrencies object.

        :param str confidence_level: (optional) The confidence level in the identification
        of the contract currency.
        :param str text: (optional) The contract currency.
        :param str text_normalized: (optional) The normalized form of the contract
        currency, which is listed as a string in
        [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) format. This element
        is optional; it is returned only if normalized text exists.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractCurrencies object from a json dictionary."""
        args = {}
        validKeys = [
            'confidence_level', 'text', 'text_normalized', 'provenance_ids',
            'location'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractCurrencies: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ContractCurrencies object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTerms(object):
    """
    The duration or durations of the contract.

    :attr str confidence_level: (optional) The confidence level in the identification of
    the contract term.
    :attr str text: (optional) The contract term (duration).
    :attr str text_normalized: (optional) The normalized form of the contract term, which
    is listed as a string. This element is optional; it is returned only if normalized
    text exists.
    :attr Interpretation interpretation: (optional) The details of the normalized text, if
    applicable. This element is optional; it is returned only if normalized text exists.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self,
                 confidence_level=None,
                 text=None,
                 text_normalized=None,
                 interpretation=None,
                 provenance_ids=None,
                 location=None):
        """
        Initialize a ContractTerms object.

        :param str confidence_level: (optional) The confidence level in the identification
        of the contract term.
        :param str text: (optional) The contract term (duration).
        :param str text_normalized: (optional) The normalized form of the contract term,
        which is listed as a string. This element is optional; it is returned only if
        normalized text exists.
        :param Interpretation interpretation: (optional) The details of the normalized
        text, if applicable. This element is optional; it is returned only if normalized
        text exists.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.interpretation = interpretation
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTerms object from a json dictionary."""
        args = {}
        validKeys = [
            'confidence_level', 'text', 'text_normalized', 'interpretation',
            'provenance_ids', 'location'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractTerms: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ContractTerms object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContractTypes(object):
    """
    The contract type identified in the input document.

    :attr str confidence_level: (optional) The confidence level in the identification of
    the contract type.
    :attr str text: (optional) The contract type.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self,
                 confidence_level=None,
                 text=None,
                 provenance_ids=None,
                 location=None):
        """
        Initialize a ContractTypes object.

        :param str confidence_level: (optional) The confidence level in the identification
        of the contract type.
        :param str text: (optional) The contract type.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContractTypes object from a json dictionary."""
        args = {}
        validKeys = ['confidence_level', 'text', 'provenance_ids', 'location']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContractTypes: '
                + ', '.join(badKeys))
        if 'confidence_level' in _dict:
            args['confidence_level'] = _dict.get('confidence_level')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ContractTypes object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocCounts(object):
    """
    Document counts.

    :attr int total: (optional) Total number of documents.
    :attr int pending: (optional) Number of pending documents.
    :attr int successful: (optional) Number of documents successfully processed.
    :attr int failed: (optional) Number of documents not successfully processed.
    """

    def __init__(self, total=None, pending=None, successful=None, failed=None):
        """
        Initialize a DocCounts object.

        :param int total: (optional) Total number of documents.
        :param int pending: (optional) Number of pending documents.
        :param int successful: (optional) Number of documents successfully processed.
        :param int failed: (optional) Number of documents not successfully processed.
        """
        self.total = total
        self.pending = pending
        self.successful = successful
        self.failed = failed

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocCounts object from a json dictionary."""
        args = {}
        validKeys = ['total', 'pending', 'successful', 'failed']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocCounts: '
                + ', '.join(badKeys))
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        if 'pending' in _dict:
            args['pending'] = _dict.get('pending')
        if 'successful' in _dict:
            args['successful'] = _dict.get('successful')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this DocCounts object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocInfo(object):
    """
    Information about the parsed input document.

    :attr str html: (optional) The full text of the parsed document in HTML format.
    :attr str title: (optional) The title of the parsed document. If the service did not
    detect a title, the value of this element is `null`.
    :attr str hash: (optional) The MD5 hash of the input document.
    """

    def __init__(self, html=None, title=None, hash=None):
        """
        Initialize a DocInfo object.

        :param str html: (optional) The full text of the parsed document in HTML format.
        :param str title: (optional) The title of the parsed document. If the service did
        not detect a title, the value of this element is `null`.
        :param str hash: (optional) The MD5 hash of the input document.
        """
        self.html = html
        self.title = title
        self.hash = hash

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocInfo object from a json dictionary."""
        args = {}
        validKeys = ['html', 'title', 'hash']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocInfo: ' +
                ', '.join(badKeys))
        if 'html' in _dict:
            args['html'] = _dict.get('html')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'hash' in _dict:
            args['hash'] = _dict.get('hash')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'html') and self.html is not None:
            _dict['html'] = self.html
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'hash') and self.hash is not None:
            _dict['hash'] = self.hash
        return _dict

    def __str__(self):
        """Return a `str` version of this DocInfo object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocStructure(object):
    """
    The structure of the input document.

    :attr list[SectionTitles] section_titles: (optional) An array containing one object
    per section or subsection identified in the input document.
    :attr list[LeadingSentence] leading_sentences: (optional) An array containing one
    object per section or subsection, in parallel with the `section_titles` array, that
    details the leading sentences in the corresponding section or subsection.
    :attr list[Paragraphs] paragraphs: (optional) An array containing one object per
    paragraph, in parallel with the `section_titles` and `leading_sentences` arrays.
    """

    def __init__(self,
                 section_titles=None,
                 leading_sentences=None,
                 paragraphs=None):
        """
        Initialize a DocStructure object.

        :param list[SectionTitles] section_titles: (optional) An array containing one
        object per section or subsection identified in the input document.
        :param list[LeadingSentence] leading_sentences: (optional) An array containing one
        object per section or subsection, in parallel with the `section_titles` array,
        that details the leading sentences in the corresponding section or subsection.
        :param list[Paragraphs] paragraphs: (optional) An array containing one object per
        paragraph, in parallel with the `section_titles` and `leading_sentences` arrays.
        """
        self.section_titles = section_titles
        self.leading_sentences = leading_sentences
        self.paragraphs = paragraphs

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocStructure object from a json dictionary."""
        args = {}
        validKeys = ['section_titles', 'leading_sentences', 'paragraphs']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocStructure: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this DocStructure object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Document(object):
    """
    Basic information about the input document.

    :attr str title: (optional) Document title, if detected.
    :attr str html: (optional) The input document converted into HTML format.
    :attr str hash: (optional) The MD5 hash value of the input document.
    :attr str label: (optional) The label applied to the input document with the calling
    method's `file_1_label` or `file_2_label` value. This field is specified only in the
    output of the **Comparing two documents** method.
    """

    def __init__(self, title=None, html=None, hash=None, label=None):
        """
        Initialize a Document object.

        :param str title: (optional) Document title, if detected.
        :param str html: (optional) The input document converted into HTML format.
        :param str hash: (optional) The MD5 hash value of the input document.
        :param str label: (optional) The label applied to the input document with the
        calling method's `file_1_label` or `file_2_label` value. This field is specified
        only in the output of the **Comparing two documents** method.
        """
        self.title = title
        self.html = html
        self.hash = hash
        self.label = label

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Document object from a json dictionary."""
        args = {}
        validKeys = ['title', 'html', 'hash', 'label']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Document: '
                + ', '.join(badKeys))
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'html' in _dict:
            args['html'] = _dict.get('html')
        if 'hash' in _dict:
            args['hash'] = _dict.get('hash')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Document object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EffectiveDates(object):
    """
    An effective date.

    :attr str confidence_level: (optional) The confidence level in the identification of
    the effective date.
    :attr str text: (optional) The effective date, listed as a string.
    :attr str text_normalized: (optional) The normalized form of the effective date, which
    is listed as a string. This element is optional; it is returned only if normalized
    text exists.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self,
                 confidence_level=None,
                 text=None,
                 text_normalized=None,
                 provenance_ids=None,
                 location=None):
        """
        Initialize a EffectiveDates object.

        :param str confidence_level: (optional) The confidence level in the identification
        of the effective date.
        :param str text: (optional) The effective date, listed as a string.
        :param str text_normalized: (optional) The normalized form of the effective date,
        which is listed as a string. This element is optional; it is returned only if
        normalized text exists.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EffectiveDates object from a json dictionary."""
        args = {}
        validKeys = [
            'confidence_level', 'text', 'text_normalized', 'provenance_ids',
            'location'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EffectiveDates: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this EffectiveDates object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Element(object):
    """
    A component part of the document.

    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The text of the element.
    :attr list[TypeLabel] types: (optional) Description of the action specified by the
    element  and whom it affects.
    :attr list[Category] categories: (optional) List of functional categories into which
    the element falls; in other words, the subject matter of the element.
    :attr list[Attribute] attributes: (optional) List of document attributes.
    """

    def __init__(self,
                 location=None,
                 text=None,
                 types=None,
                 categories=None,
                 attributes=None):
        """
        Initialize a Element object.

        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The text of the element.
        :param list[TypeLabel] types: (optional) Description of the action specified by
        the element  and whom it affects.
        :param list[Category] categories: (optional) List of functional categories into
        which the element falls; in other words, the subject matter of the element.
        :param list[Attribute] attributes: (optional) List of document attributes.
        """
        self.location = location
        self.text = text
        self.types = types
        self.categories = categories
        self.attributes = attributes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Element object from a json dictionary."""
        args = {}
        validKeys = ['location', 'text', 'types', 'categories', 'attributes']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Element: ' +
                ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Element object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ElementLocations(object):
    """
    A list of `begin` and `end` indexes that indicate the locations of the elements in the
    input document.

    :attr int begin: (optional) An integer that indicates the starting position of the
    element in the input document.
    :attr int end: (optional) An integer that indicates the ending position of the element
    in the input document.
    """

    def __init__(self, begin=None, end=None):
        """
        Initialize a ElementLocations object.

        :param int begin: (optional) An integer that indicates the starting position of
        the element in the input document.
        :param int end: (optional) An integer that indicates the ending position of the
        element in the input document.
        """
        self.begin = begin
        self.end = end

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElementLocations object from a json dictionary."""
        args = {}
        validKeys = ['begin', 'end']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ElementLocations: '
                + ', '.join(badKeys))
        if 'begin' in _dict:
            args['begin'] = _dict.get('begin')
        if 'end' in _dict:
            args['end'] = _dict.get('end')
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
        """Return a `str` version of this ElementLocations object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ElementPair(object):
    """
    Details of semantically aligned elements.

    :attr str document_label: (optional) The label of the document (that is, the value of
    either the `file_1_label` or `file_2_label` parameters) in which the element occurs.
    :attr str text: (optional) The contents of the element.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr list[TypeLabelComparison] types: (optional) Description of the action specified
    by the element and whom it affects.
    :attr list[CategoryComparison] categories: (optional) List of functional categories
    into which the element falls; in other words, the subject matter of the element.
    :attr list[Attribute] attributes: (optional) List of document attributes.
    """

    def __init__(self,
                 document_label=None,
                 text=None,
                 location=None,
                 types=None,
                 categories=None,
                 attributes=None):
        """
        Initialize a ElementPair object.

        :param str document_label: (optional) The label of the document (that is, the
        value of either the `file_1_label` or `file_2_label` parameters) in which the
        element occurs.
        :param str text: (optional) The contents of the element.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param list[TypeLabelComparison] types: (optional) Description of the action
        specified by the element and whom it affects.
        :param list[CategoryComparison] categories: (optional) List of functional
        categories into which the element falls; in other words, the subject matter of the
        element.
        :param list[Attribute] attributes: (optional) List of document attributes.
        """
        self.document_label = document_label
        self.text = text
        self.location = location
        self.types = types
        self.categories = categories
        self.attributes = attributes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElementPair object from a json dictionary."""
        args = {}
        validKeys = [
            'document_label', 'text', 'location', 'types', 'categories',
            'attributes'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ElementPair: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ElementPair object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackDataInput(object):
    """
    Feedback data for submission.

    :attr str feedback_type: The type of feedback. The only permitted value is
    `element_classification`.
    :attr ShortDoc document: (optional) Brief information about the input document.
    :attr str model_id: (optional) An optional string identifying the model ID. The only
    permitted value is `contracts`.
    :attr str model_version: (optional) An optional string identifying the version of the
    model used.
    :attr Location location: The numeric location of the identified element in the
    document, represented with two integers labeled `begin` and `end`.
    :attr str text: The text on which to submit feedback.
    :attr OriginalLabelsIn original_labels: The original labeling from the input document,
    without the submitted feedback.
    :attr UpdatedLabelsIn updated_labels: The updated labeling from the input document,
    accounting for the submitted feedback.
    """

    def __init__(self,
                 feedback_type,
                 location,
                 text,
                 original_labels,
                 updated_labels,
                 document=None,
                 model_id=None,
                 model_version=None):
        """
        Initialize a FeedbackDataInput object.

        :param str feedback_type: The type of feedback. The only permitted value is
        `element_classification`.
        :param Location location: The numeric location of the identified element in the
        document, represented with two integers labeled `begin` and `end`.
        :param str text: The text on which to submit feedback.
        :param OriginalLabelsIn original_labels: The original labeling from the input
        document, without the submitted feedback.
        :param UpdatedLabelsIn updated_labels: The updated labeling from the input
        document, accounting for the submitted feedback.
        :param ShortDoc document: (optional) Brief information about the input document.
        :param str model_id: (optional) An optional string identifying the model ID. The
        only permitted value is `contracts`.
        :param str model_version: (optional) An optional string identifying the version of
        the model used.
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
    def _from_dict(cls, _dict):
        """Initialize a FeedbackDataInput object from a json dictionary."""
        args = {}
        validKeys = [
            'feedback_type', 'document', 'model_id', 'model_version',
            'location', 'text', 'original_labels', 'updated_labels'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackDataInput: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this FeedbackDataInput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackDataOutput(object):
    """
    Information returned from the **Add Feedback** method.

    :attr str feedback_type: (optional) A string identifying the user adding the feedback.
    The only permitted value is `element_classification`.
    :attr ShortDoc document: (optional) Brief information about the input document.
    :attr str model_id: (optional) An optional string identifying the model ID. The only
    permitted value is `contracts`.
    :attr str model_version: (optional) An optional string identifying the version of the
    model used.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The text to which the feedback applies.
    :attr OriginalLabelsOut original_labels: (optional) The original labeling from the
    input document, without the submitted feedback.
    :attr UpdatedLabelsOut updated_labels: (optional) The updated labeling from the input
    document, accounting for the submitted feedback.
    :attr Pagination pagination: (optional) Pagination details, if required by the length
    of the output.
    """

    def __init__(self,
                 feedback_type=None,
                 document=None,
                 model_id=None,
                 model_version=None,
                 location=None,
                 text=None,
                 original_labels=None,
                 updated_labels=None,
                 pagination=None):
        """
        Initialize a FeedbackDataOutput object.

        :param str feedback_type: (optional) A string identifying the user adding the
        feedback. The only permitted value is `element_classification`.
        :param ShortDoc document: (optional) Brief information about the input document.
        :param str model_id: (optional) An optional string identifying the model ID. The
        only permitted value is `contracts`.
        :param str model_version: (optional) An optional string identifying the version of
        the model used.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The text to which the feedback applies.
        :param OriginalLabelsOut original_labels: (optional) The original labeling from
        the input document, without the submitted feedback.
        :param UpdatedLabelsOut updated_labels: (optional) The updated labeling from the
        input document, accounting for the submitted feedback.
        :param Pagination pagination: (optional) Pagination details, if required by the
        length of the output.
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
    def _from_dict(cls, _dict):
        """Initialize a FeedbackDataOutput object from a json dictionary."""
        args = {}
        validKeys = [
            'feedback_type', 'document', 'model_id', 'model_version',
            'location', 'text', 'original_labels', 'updated_labels',
            'pagination'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackDataOutput: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this FeedbackDataOutput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackDeleted(object):
    """
    The status and message of the deletion request.

    :attr int status: (optional) HTTP return code.
    :attr str message: (optional) Status message returned from the service.
    """

    def __init__(self, status=None, message=None):
        """
        Initialize a FeedbackDeleted object.

        :param int status: (optional) HTTP return code.
        :param str message: (optional) Status message returned from the service.
        """
        self.status = status
        self.message = message

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackDeleted object from a json dictionary."""
        args = {}
        validKeys = ['status', 'message']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackDeleted: '
                + ', '.join(badKeys))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def __str__(self):
        """Return a `str` version of this FeedbackDeleted object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackList(object):
    """
    The results of a successful **List Feedback** request for all feedback.

    :attr list[GetFeedback] feedback: (optional) A list of all feedback for the document.
    """

    def __init__(self, feedback=None):
        """
        Initialize a FeedbackList object.

        :param list[GetFeedback] feedback: (optional) A list of all feedback for the
        document.
        """
        self.feedback = feedback

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackList object from a json dictionary."""
        args = {}
        validKeys = ['feedback']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackList: '
                + ', '.join(badKeys))
        if 'feedback' in _dict:
            args['feedback'] = [
                GetFeedback._from_dict(x) for x in (_dict.get('feedback'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'feedback') and self.feedback is not None:
            _dict['feedback'] = [x._to_dict() for x in self.feedback]
        return _dict

    def __str__(self):
        """Return a `str` version of this FeedbackList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeedbackReturn(object):
    """
    Information about the document and the submitted feedback.

    :attr str feedback_id: (optional) The unique ID of the feedback object.
    :attr str user_id: (optional) An optional string identifying the person submitting
    feedback.
    :attr str comment: (optional) An optional comment from the person submitting the
    feedback.
    :attr datetime created: (optional) Timestamp listing the creation time of the feedback
    submission.
    :attr FeedbackDataOutput feedback_data: (optional) Information returned from the **Add
    Feedback** method.
    """

    def __init__(self,
                 feedback_id=None,
                 user_id=None,
                 comment=None,
                 created=None,
                 feedback_data=None):
        """
        Initialize a FeedbackReturn object.

        :param str feedback_id: (optional) The unique ID of the feedback object.
        :param str user_id: (optional) An optional string identifying the person
        submitting feedback.
        :param str comment: (optional) An optional comment from the person submitting the
        feedback.
        :param datetime created: (optional) Timestamp listing the creation time of the
        feedback submission.
        :param FeedbackDataOutput feedback_data: (optional) Information returned from the
        **Add Feedback** method.
        """
        self.feedback_id = feedback_id
        self.user_id = user_id
        self.comment = comment
        self.created = created
        self.feedback_data = feedback_data

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeedbackReturn object from a json dictionary."""
        args = {}
        validKeys = [
            'feedback_id', 'user_id', 'comment', 'created', 'feedback_data'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeedbackReturn: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this FeedbackReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GetFeedback(object):
    """
    The results of a successful **Get Feedback** request for a single feedback entry.

    :attr str feedback_id: (optional) A string uniquely identifying the feedback entry.
    :attr datetime created: (optional) A timestamp identifying the creation time of the
    feedback entry.
    :attr str comment: (optional) A string containing the user's comment about the
    feedback entry.
    :attr FeedbackDataOutput feedback_data: (optional) Information returned from the **Add
    Feedback** method.
    """

    def __init__(self,
                 feedback_id=None,
                 created=None,
                 comment=None,
                 feedback_data=None):
        """
        Initialize a GetFeedback object.

        :param str feedback_id: (optional) A string uniquely identifying the feedback
        entry.
        :param datetime created: (optional) A timestamp identifying the creation time of
        the feedback entry.
        :param str comment: (optional) A string containing the user's comment about the
        feedback entry.
        :param FeedbackDataOutput feedback_data: (optional) Information returned from the
        **Add Feedback** method.
        """
        self.feedback_id = feedback_id
        self.created = created
        self.comment = comment
        self.feedback_data = feedback_data

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetFeedback object from a json dictionary."""
        args = {}
        validKeys = ['feedback_id', 'created', 'comment', 'feedback_data']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class GetFeedback: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this GetFeedback object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class HTMLReturn(object):
    """
    The HTML converted from an input document.

    :attr str num_pages: (optional) The number of pages in the input document.
    :attr str author: (optional) The author of the input document, if identified.
    :attr str publication_date: (optional) The publication date of the input document, if
    identified.
    :attr str title: (optional) The title of the input document, if identified.
    :attr str html: (optional) The HTML version of the input document.
    """

    def __init__(self,
                 num_pages=None,
                 author=None,
                 publication_date=None,
                 title=None,
                 html=None):
        """
        Initialize a HTMLReturn object.

        :param str num_pages: (optional) The number of pages in the input document.
        :param str author: (optional) The author of the input document, if identified.
        :param str publication_date: (optional) The publication date of the input
        document, if identified.
        :param str title: (optional) The title of the input document, if identified.
        :param str html: (optional) The HTML version of the input document.
        """
        self.num_pages = num_pages
        self.author = author
        self.publication_date = publication_date
        self.title = title
        self.html = html

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HTMLReturn object from a json dictionary."""
        args = {}
        validKeys = ['num_pages', 'author', 'publication_date', 'title', 'html']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class HTMLReturn: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this HTMLReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Interpretation(object):
    """
    The details of the normalized text, if applicable. This element is optional; it is
    returned only if normalized text exists.

    :attr str value: (optional) The value that was located in the normalized text.
    :attr float numeric_value: (optional) An integer or float expressing the numeric value
    of the `value` key.
    :attr str unit: (optional) A string listing the unit of the value that was found in
    the normalized text.
    **Note:** The value of `unit` is the [ISO-4217 currency
    code](https://www.iso.org/iso-4217-currency-codes.html) identified for the currency
    amount (for example, `USD` or `EUR`). If the service cannot disambiguate a currency
    symbol (for example, `$` or `£`), the value of `unit` contains the ambiguous symbol
    as-is.
    """

    def __init__(self, value=None, numeric_value=None, unit=None):
        """
        Initialize a Interpretation object.

        :param str value: (optional) The value that was located in the normalized text.
        :param float numeric_value: (optional) An integer or float expressing the numeric
        value of the `value` key.
        :param str unit: (optional) A string listing the unit of the value that was found
        in the normalized text.
        **Note:** The value of `unit` is the [ISO-4217 currency
        code](https://www.iso.org/iso-4217-currency-codes.html) identified for the
        currency amount (for example, `USD` or `EUR`). If the service cannot disambiguate
        a currency symbol (for example, `$` or `£`), the value of `unit` contains the
        ambiguous symbol as-is.
        """
        self.value = value
        self.numeric_value = numeric_value
        self.unit = unit

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Interpretation object from a json dictionary."""
        args = {}
        validKeys = ['value', 'numeric_value', 'unit']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Interpretation: '
                + ', '.join(badKeys))
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'numeric_value' in _dict:
            args['numeric_value'] = _dict.get('numeric_value')
        if 'unit' in _dict:
            args['unit'] = _dict.get('unit')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'numeric_value') and self.numeric_value is not None:
            _dict['numeric_value'] = self.numeric_value
        if hasattr(self, 'unit') and self.unit is not None:
            _dict['unit'] = self.unit
        return _dict

    def __str__(self):
        """Return a `str` version of this Interpretation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Key(object):
    """
    A key in a key-value pair.

    :attr str cell_id: (optional) The unique ID of the key in the table.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The text content of the table cell without HTML markup.
    """

    def __init__(self, cell_id=None, location=None, text=None):
        """
        Initialize a Key object.

        :param str cell_id: (optional) The unique ID of the key in the table.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The text content of the table cell without HTML
        markup.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Key object from a json dictionary."""
        args = {}
        validKeys = ['cell_id', 'location', 'text']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Key: ' +
                ', '.join(badKeys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Return a `str` version of this Key object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeyValuePair(object):
    """
    Key-value pairs detected across cell boundaries.

    :attr Key key: (optional) A key in a key-value pair.
    :attr list[Value] value: (optional) A list of values in a key-value pair.
    """

    def __init__(self, key=None, value=None):
        """
        Initialize a KeyValuePair object.

        :param Key key: (optional) A key in a key-value pair.
        :param list[Value] value: (optional) A list of values in a key-value pair.
        """
        self.key = key
        self.value = value

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeyValuePair object from a json dictionary."""
        args = {}
        validKeys = ['key', 'value']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class KeyValuePair: '
                + ', '.join(badKeys))
        if 'key' in _dict:
            args['key'] = Key._from_dict(_dict.get('key'))
        if 'value' in _dict:
            args['value'] = [Value._from_dict(x) for x in (_dict.get('value'))]
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
        """Return a `str` version of this KeyValuePair object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Label(object):
    """
    A pair of `nature` and `party` objects. The `nature` object identifies the effect of
    the element on the identified `party`, and the `party` object identifies the affected
    party.

    :attr str nature: The identified `nature` of the element.
    :attr str party: The identified `party` of the element.
    """

    def __init__(self, nature, party):
        """
        Initialize a Label object.

        :param str nature: The identified `nature` of the element.
        :param str party: The identified `party` of the element.
        """
        self.nature = nature
        self.party = party

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Label object from a json dictionary."""
        args = {}
        validKeys = ['nature', 'party']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Label: ' +
                ', '.join(badKeys))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'nature') and self.nature is not None:
            _dict['nature'] = self.nature
        if hasattr(self, 'party') and self.party is not None:
            _dict['party'] = self.party
        return _dict

    def __str__(self):
        """Return a `str` version of this Label object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LeadingSentence(object):
    """
    The leading sentences in a section or subsection of the input document.

    :attr str text: (optional) The text of the leading sentence.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr list[ElementLocations] element_locations: (optional) An array of `location`
    objects that lists the locations of detected leading sentences.
    """

    def __init__(self, text=None, location=None, element_locations=None):
        """
        Initialize a LeadingSentence object.

        :param str text: (optional) The text of the leading sentence.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param list[ElementLocations] element_locations: (optional) An array of `location`
        objects that lists the locations of detected leading sentences.
        """
        self.text = text
        self.location = location
        self.element_locations = element_locations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LeadingSentence object from a json dictionary."""
        args = {}
        validKeys = ['text', 'location', 'element_locations']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LeadingSentence: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this LeadingSentence object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Location(object):
    """
    The numeric location of the identified element in the document, represented with two
    integers labeled `begin` and `end`.

    :attr int begin: The element's `begin` index.
    :attr int end: The element's `end` index.
    """

    def __init__(self, begin, end):
        """
        Initialize a Location object.

        :param int begin: The element's `begin` index.
        :param int end: The element's `end` index.
        """
        self.begin = begin
        self.end = end

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Location object from a json dictionary."""
        args = {}
        validKeys = ['begin', 'end']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Location: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        return _dict

    def __str__(self):
        """Return a `str` version of this Location object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Mention(object):
    """
    A mention of a party.

    :attr str text: (optional) The name of the party.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self, text=None, location=None):
        """
        Initialize a Mention object.

        :param str text: (optional) The name of the party.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Mention object from a json dictionary."""
        args = {}
        validKeys = ['text', 'location']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Mention: ' +
                ', '.join(badKeys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Return a `str` version of this Mention object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OriginalLabelsIn(object):
    """
    The original labeling from the input document, without the submitted feedback.

    :attr list[TypeLabel] types: Description of the action specified by the element and
    whom it affects.
    :attr list[Category] categories: List of functional categories into which the element
    falls; in other words, the subject matter of the element.
    """

    def __init__(self, types, categories):
        """
        Initialize a OriginalLabelsIn object.

        :param list[TypeLabel] types: Description of the action specified by the element
        and whom it affects.
        :param list[Category] categories: List of functional categories into which the
        element falls; in other words, the subject matter of the element.
        """
        self.types = types
        self.categories = categories

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginalLabelsIn object from a json dictionary."""
        args = {}
        validKeys = ['types', 'categories']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class OriginalLabelsIn: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        return _dict

    def __str__(self):
        """Return a `str` version of this OriginalLabelsIn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OriginalLabelsOut(object):
    """
    The original labeling from the input document, without the submitted feedback.

    :attr list[TypeLabel] types: (optional) Description of the action specified by the
    element and whom it affects.
    :attr list[Category] categories: (optional) List of functional categories into which
    the element falls; in other words, the subject matter of the element.
    :attr str modification: (optional) A string identifying the type of modification the
    feedback entry in the `updated_labels` array. Possible values are `added`,
    `not_changed`, and `removed`.
    """

    def __init__(self, types=None, categories=None, modification=None):
        """
        Initialize a OriginalLabelsOut object.

        :param list[TypeLabel] types: (optional) Description of the action specified by
        the element and whom it affects.
        :param list[Category] categories: (optional) List of functional categories into
        which the element falls; in other words, the subject matter of the element.
        :param str modification: (optional) A string identifying the type of modification
        the feedback entry in the `updated_labels` array. Possible values are `added`,
        `not_changed`, and `removed`.
        """
        self.types = types
        self.categories = categories
        self.modification = modification

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginalLabelsOut object from a json dictionary."""
        args = {}
        validKeys = ['types', 'categories', 'modification']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class OriginalLabelsOut: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'modification') and self.modification is not None:
            _dict['modification'] = self.modification
        return _dict

    def __str__(self):
        """Return a `str` version of this OriginalLabelsOut object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Pagination(object):
    """
    Pagination details, if required by the length of the output.

    :attr str refresh_cursor: (optional) A token identifying the current page of results.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    :attr str refresh_url: (optional) The URL that returns the current page of results.
    :attr str next_url: (optional) The URL that returns the next page of results.
    :attr int total: (optional) Reserved for future use.
    """

    def __init__(self,
                 refresh_cursor=None,
                 next_cursor=None,
                 refresh_url=None,
                 next_url=None,
                 total=None):
        """
        Initialize a Pagination object.

        :param str refresh_cursor: (optional) A token identifying the current page of
        results.
        :param str next_cursor: (optional) A token identifying the next page of results.
        :param str refresh_url: (optional) The URL that returns the current page of
        results.
        :param str next_url: (optional) The URL that returns the next page of results.
        :param int total: (optional) Reserved for future use.
        """
        self.refresh_cursor = refresh_cursor
        self.next_cursor = next_cursor
        self.refresh_url = refresh_url
        self.next_url = next_url
        self.total = total

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pagination object from a json dictionary."""
        args = {}
        validKeys = [
            'refresh_cursor', 'next_cursor', 'refresh_url', 'next_url', 'total'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Pagination: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Pagination object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Paragraphs(object):
    """
    The locations of each paragraph in the input document.

    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self, location=None):
        """
        Initialize a Paragraphs object.

        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Paragraphs object from a json dictionary."""
        args = {}
        validKeys = ['location']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Paragraphs: '
                + ', '.join(badKeys))
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this Paragraphs object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Parties(object):
    """
    A party and its corresponding role, including address and contact information if
    identified.

    :attr str party: (optional) The normalized form of the party's name.
    :attr str role: (optional) A string identifying the party's role.
    :attr str importance: (optional) A string that identifies the importance of the party.
    :attr list[Address] addresses: (optional) A list of the party's address or addresses.
    :attr list[Contact] contacts: (optional) A list of the names and roles of contacts
    identified in the input document.
    :attr list[Mention] mentions: (optional) A list of the party's mentions in the input
    document.
    """

    def __init__(self,
                 party=None,
                 importance=None,
                 role=None,
                 addresses=None,
                 contacts=None,
                 mentions=None):
        """
        Initialize a Parties object.

        :param str party: (optional) The normalized form of the party's name.
        :param str role: (optional) A string identifying the party's role.
        :param str importance: (optional) A string that identifies the importance of the
        party.
        :param list[Address] addresses: (optional) A list of the party's address or
        addresses.
        :param list[Contact] contacts: (optional) A list of the names and roles of
        contacts identified in the input document.
        :param list[Mention] mentions: (optional) A list of the party's mentions in the
        input document.
        """
        self.party = party
        self.role = role
        self.importance = importance
        self.addresses = addresses
        self.contacts = contacts
        self.mentions = mentions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Parties object from a json dictionary."""
        args = {}
        validKeys = [
            'party', 'role', 'importance', 'addresses', 'contacts', 'mentions'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Parties: ' +
                ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Parties object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PaymentTerms(object):
    """
    The document's payment duration or durations.

    :attr str confidence_level: (optional) The confidence level in the identification of
    the payment term.
    :attr str text: (optional) The payment term (duration).
    :attr str text_normalized: (optional) The normalized form of the payment term, which
    is listed as a string. This element is optional; it is returned only if normalized
    text exists.
    :attr Interpretation interpretation: (optional) The details of the normalized text, if
    applicable. This element is optional; it is returned only if normalized text exists.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self,
                 confidence_level=None,
                 text=None,
                 text_normalized=None,
                 interpretation=None,
                 provenance_ids=None,
                 location=None):
        """
        Initialize a PaymentTerms object.

        :param str confidence_level: (optional) The confidence level in the identification
        of the payment term.
        :param str text: (optional) The payment term (duration).
        :param str text_normalized: (optional) The normalized form of the payment term,
        which is listed as a string. This element is optional; it is returned only if
        normalized text exists.
        :param Interpretation interpretation: (optional) The details of the normalized
        text, if applicable. This element is optional; it is returned only if normalized
        text exists.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.interpretation = interpretation
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaymentTerms object from a json dictionary."""
        args = {}
        validKeys = [
            'confidence_level', 'text', 'text_normalized', 'interpretation',
            'provenance_ids', 'location'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class PaymentTerms: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this PaymentTerms object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RowHeaders(object):
    """
    Row-level cells, each applicable as a header to other cells in the same row as itself,
    of the current table.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The textual contents of this cell from the input document
    without associated markup content.
    :attr str text_normalized: (optional) If you provide customization input, the
    normalized version of the cell text according to the customization; otherwise, the
    same value as `text`.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row` location
    in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row` location in
    the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's `column`
    location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
    location in the current table.
    """

    def __init__(self,
                 cell_id=None,
                 location=None,
                 text=None,
                 text_normalized=None,
                 row_index_begin=None,
                 row_index_end=None,
                 column_index_begin=None,
                 column_index_end=None):
        """
        Initialize a RowHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current table.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The textual contents of this cell from the input
        document without associated markup content.
        :param str text_normalized: (optional) If you provide customization input, the
        normalized version of the cell text according to the customization; otherwise, the
        same value as `text`.
        :param int row_index_begin: (optional) The `begin` index of this cell's `row`
        location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row` location
        in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
        `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's `column`
        location in the current table.
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
        """Initialize a RowHeaders object from a json dictionary."""
        args = {}
        validKeys = [
            'cell_id', 'location', 'text', 'text_normalized', 'row_index_begin',
            'row_index_end', 'column_index_begin', 'column_index_end'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RowHeaders: '
                + ', '.join(badKeys))
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
        """Return a `str` version of this RowHeaders object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SectionTitle(object):
    """
    The table's section title, if identified.

    :attr str text: (optional) The text of the section title, if identified.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self, text=None, location=None):
        """
        Initialize a SectionTitle object.

        :param str text: (optional) The text of the section title, if identified.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.text = text
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SectionTitle object from a json dictionary."""
        args = {}
        validKeys = ['text', 'location']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SectionTitle: '
                + ', '.join(badKeys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Return a `str` version of this SectionTitle object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SectionTitles(object):
    """
    An array containing one object per section or subsection detected in the input
    document. Sections and subsections are not nested; instead, they are flattened out and
    can be placed back in order by using the `begin` and `end` values of the element and
    the `level` value of the section.

    :attr str text: (optional) The text of the section title, if identified.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr int level: (optional) An integer indicating the level at which the section is
    located in the input document. For example, `1` represents a top-level section, `2`
    represents a subsection within the level `1` section, and so forth.
    :attr list[ElementLocations] element_locations: (optional) An array of `location`
    objects that lists the locations of detected section titles.
    """

    def __init__(self,
                 text=None,
                 location=None,
                 level=None,
                 element_locations=None):
        """
        Initialize a SectionTitles object.

        :param str text: (optional) The text of the section title, if identified.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param int level: (optional) An integer indicating the level at which the section
        is located in the input document. For example, `1` represents a top-level section,
        `2` represents a subsection within the level `1` section, and so forth.
        :param list[ElementLocations] element_locations: (optional) An array of `location`
        objects that lists the locations of detected section titles.
        """
        self.text = text
        self.location = location
        self.level = level
        self.element_locations = element_locations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SectionTitles object from a json dictionary."""
        args = {}
        validKeys = ['text', 'location', 'level', 'element_locations']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SectionTitles: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this SectionTitles object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ShortDoc(object):
    """
    Brief information about the input document.

    :attr str title: (optional) The title of the input document, if identified.
    :attr str hash: (optional) The MD5 hash of the input document.
    """

    def __init__(self, title=None, hash=None):
        """
        Initialize a ShortDoc object.

        :param str title: (optional) The title of the input document, if identified.
        :param str hash: (optional) The MD5 hash of the input document.
        """
        self.title = title
        self.hash = hash

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ShortDoc object from a json dictionary."""
        args = {}
        validKeys = ['title', 'hash']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ShortDoc: '
                + ', '.join(badKeys))
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'hash' in _dict:
            args['hash'] = _dict.get('hash')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'hash') and self.hash is not None:
            _dict['hash'] = self.hash
        return _dict

    def __str__(self):
        """Return a `str` version of this ShortDoc object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableHeaders(object):
    """
    The contents of the current table's header.

    :attr str cell_id: (optional) The unique ID of the cell in the current table.
    :attr object location: (optional) The location of the table header cell in the current
    table as defined by its `begin` and `end` offsets, respectfully, in the input
    document.
    :attr str text: (optional) The textual contents of the cell from the input document
    without associated markup content.
    :attr int row_index_begin: (optional) The `begin` index of this cell's `row` location
    in the current table.
    :attr int row_index_end: (optional) The `end` index of this cell's `row` location in
    the current table.
    :attr int column_index_begin: (optional) The `begin` index of this cell's `column`
    location in the current table.
    :attr int column_index_end: (optional) The `end` index of this cell's `column`
    location in the current table.
    """

    def __init__(self,
                 cell_id=None,
                 location=None,
                 text=None,
                 row_index_begin=None,
                 row_index_end=None,
                 column_index_begin=None,
                 column_index_end=None):
        """
        Initialize a TableHeaders object.

        :param str cell_id: (optional) The unique ID of the cell in the current table.
        :param object location: (optional) The location of the table header cell in the
        current table as defined by its `begin` and `end` offsets, respectfully, in the
        input document.
        :param str text: (optional) The textual contents of the cell from the input
        document without associated markup content.
        :param int row_index_begin: (optional) The `begin` index of this cell's `row`
        location in the current table.
        :param int row_index_end: (optional) The `end` index of this cell's `row` location
        in the current table.
        :param int column_index_begin: (optional) The `begin` index of this cell's
        `column` location in the current table.
        :param int column_index_end: (optional) The `end` index of this cell's `column`
        location in the current table.
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
        validKeys = [
            'cell_id', 'location', 'text', 'row_index_begin', 'row_index_end',
            'column_index_begin', 'column_index_end'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableHeaders: '
                + ', '.join(badKeys))
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


class TableReturn(object):
    """
    The analysis of the document's tables.

    :attr DocInfo document: (optional) Information about the parsed input document.
    :attr str model_id: (optional) The ID of the model used to extract the table contents.
    The value for table extraction is `tables`.
    :attr str model_version: (optional) The version of the `tables` model ID.
    :attr list[Tables] tables: (optional) Definitions of the tables identified in the
    input document.
    """

    def __init__(self,
                 document=None,
                 model_id=None,
                 model_version=None,
                 tables=None):
        """
        Initialize a TableReturn object.

        :param DocInfo document: (optional) Information about the parsed input document.
        :param str model_id: (optional) The ID of the model used to extract the table
        contents. The value for table extraction is `tables`.
        :param str model_version: (optional) The version of the `tables` model ID.
        :param list[Tables] tables: (optional) Definitions of the tables identified in the
        input document.
        """
        self.document = document
        self.model_id = model_id
        self.model_version = model_version
        self.tables = tables

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableReturn object from a json dictionary."""
        args = {}
        validKeys = ['document', 'model_id', 'model_version', 'tables']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableReturn: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this TableReturn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TableTitle(object):
    """
    If identified, the title or caption of the current table of the form `Table x.: ...`.
    Empty when no title is identified. When exposed, the `title` is also excluded from the
    `contexts` array of the same table.

    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The text of the identified table title or caption.
    """

    def __init__(self, location=None, text=None):
        """
        Initialize a TableTitle object.

        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The text of the identified table title or caption.
        """
        self.location = location
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TableTitle object from a json dictionary."""
        args = {}
        validKeys = ['location', 'text']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TableTitle: '
                + ', '.join(badKeys))
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this TableTitle object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Tables(object):
    """
    The contents of the tables extracted from a document.

    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The textual contents of the current table from the input
    document without associated markup content.
    :attr SectionTitle section_title: (optional) The table's section title, if identified.
    :attr TableTitle title: (optional) If identified, the title or caption of the current
    table of the form `Table x.: ...`. Empty when no title is identified. When exposed,
    the `title` is also excluded from the `contexts` array of the same table.
    :attr list[TableHeaders] table_headers: (optional) An array of table-level cells that
    apply as headers to all the other cells in the current table.
    :attr list[RowHeaders] row_headers: (optional) An array of row-level cells, each
    applicable as a header to other cells in the same row as itself, of the current table.
    :attr list[ColumnHeaders] column_headers: (optional) An array of column-level cells,
    each applicable as a header to other cells in the same column as itself, of the
    current table.
    :attr list[BodyCells] body_cells: (optional) An array of cells that are neither table
    header nor column header nor row header cells, of the current table with corresponding
    row and column header associations.
    :attr list[Contexts] contexts: (optional) An array of objects that list text that is
    related to the table contents and that precedes or follows the current table.
    :attr list[KeyValuePair] key_value_pairs: (optional) An array of key-value pairs
    identified in the current table.
    """

    def __init__(
            self,
            location=None,
            text=None,
            section_title=None,
            table_headers=None,
            row_headers=None,
            column_headers=None,
            key_value_pairs=None,
            body_cells=None,
            contexts=None,
            title=None):
        """
        Initialize a Tables object.

        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The textual contents of the current table from the
        input document without associated markup content.
        :param SectionTitle section_title: (optional) The table's section title, if
        identified.
        :param TableTitle title: (optional) If identified, the title or caption of the
        current table of the form `Table x.: ...`. Empty when no title is identified. When
        exposed, the `title` is also excluded from the `contexts` array of the same table.
        :param list[TableHeaders] table_headers: (optional) An array of table-level cells
        that apply as headers to all the other cells in the current table.
        :param list[RowHeaders] row_headers: (optional) An array of row-level cells, each
        applicable as a header to other cells in the same row as itself, of the current
        table.
        :param list[ColumnHeaders] column_headers: (optional) An array of column-level
        cells, each applicable as a header to other cells in the same column as itself, of
        the current table.
        :param list[BodyCells] body_cells: (optional) An array of cells that are neither
        table header nor column header nor row header cells, of the current table with
        corresponding row and column header associations.
        :param list[Contexts] contexts: (optional) An array of objects that list text that
        is related to the table contents and that precedes or follows the current table.
        :param list[KeyValuePair] key_value_pairs: (optional) An array of key-value pairs
        identified in the current table.
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
    def _from_dict(cls, _dict):
        """Initialize a Tables object from a json dictionary."""
        args = {}
        validKeys = [
            'location', 'text', 'section_title', 'title', 'table_headers',
            'row_headers', 'column_headers', 'body_cells', 'contexts',
            'key_value_pairs'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Tables: ' +
                ', '.join(badKeys))
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

    def __str__(self):
        """Return a `str` version of this Tables object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TerminationDates(object):
    """
    Termination dates identified in the input document.

    :attr str confidence_level: (optional) The confidence level in the identification of
    the termination date.
    :attr str text: (optional) The termination date.
    :attr str text_normalized: (optional) The normalized form of the termination date,
    which is listed as a string. This element is optional; it is returned only if
    normalized text exists.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    """

    def __init__(self,
                 confidence_level=None,
                 text=None,
                 text_normalized=None,
                 provenance_ids=None,
                 location=None):
        """
        Initialize a TerminationDates object.

        :param str confidence_level: (optional) The confidence level in the identification
        of the termination date.
        :param str text: (optional) The termination date.
        :param str text_normalized: (optional) The normalized form of the termination
        date, which is listed as a string. This element is optional; it is returned only
        if normalized text exists.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        """
        self.confidence_level = confidence_level
        self.text = text
        self.text_normalized = text_normalized
        self.provenance_ids = provenance_ids
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TerminationDates object from a json dictionary."""
        args = {}
        validKeys = [
            'confidence_level', 'text', 'text_normalized', 'provenance_ids',
            'location'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TerminationDates: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this TerminationDates object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TypeLabel(object):
    """
    Identification of a specific type.

    :attr Label label: (optional) A pair of `nature` and `party` objects. The `nature`
    object identifies the effect of the element on the identified `party`, and the `party`
    object identifies the affected party.
    :attr list[str] provenance_ids: (optional) Hashed values that you can send to IBM to
    provide feedback or receive support.
    """

    def __init__(self, label=None, provenance_ids=None):
        """
        Initialize a TypeLabel object.

        :param Label label: (optional) A pair of `nature` and `party` objects. The
        `nature` object identifies the effect of the element on the identified `party`,
        and the `party` object identifies the affected party.
        :param list[str] provenance_ids: (optional) Hashed values that you can send to IBM
        to provide feedback or receive support.
        """
        self.label = label
        self.provenance_ids = provenance_ids

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TypeLabel object from a json dictionary."""
        args = {}
        validKeys = ['label', 'provenance_ids']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TypeLabel: '
                + ', '.join(badKeys))
        if 'label' in _dict:
            args['label'] = Label._from_dict(_dict.get('label'))
        if 'provenance_ids' in _dict:
            args['provenance_ids'] = _dict.get('provenance_ids')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label._to_dict()
        if hasattr(self, 'provenance_ids') and self.provenance_ids is not None:
            _dict['provenance_ids'] = self.provenance_ids
        return _dict

    def __str__(self):
        """Return a `str` version of this TypeLabel object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TypeLabelComparison(object):
    """
    Identification of a specific type.

    :attr Label label: (optional) A pair of `nature` and `party` objects. The `nature`
    object identifies the effect of the element on the identified `party`, and the `party`
    object identifies the affected party.
    """

    def __init__(self, label=None):
        """
        Initialize a TypeLabelComparison object.

        :param Label label: (optional) A pair of `nature` and `party` objects. The
        `nature` object identifies the effect of the element on the identified `party`,
        and the `party` object identifies the affected party.
        """
        self.label = label

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TypeLabelComparison object from a json dictionary."""
        args = {}
        validKeys = ['label']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TypeLabelComparison: '
                + ', '.join(badKeys))
        if 'label' in _dict:
            args['label'] = Label._from_dict(_dict.get('label'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this TypeLabelComparison object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UnalignedElement(object):
    """
    Element that does not align semantically between two compared documents.

    :attr str document_label: (optional) The label assigned to the document by the value
    of the `file_1_label` or `file_2_label` parameters on the **Compare two documents**
    method.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The text of the element.
    :attr list[TypeLabelComparison] types: (optional) Description of the action specified
    by the element and whom it affects.
    :attr list[CategoryComparison] categories: (optional) List of functional categories
    into which the element falls; in other words, the subject matter of the element.
    :attr list[Attribute] attributes: (optional) List of document attributes.
    """

    def __init__(self,
                 document_label=None,
                 location=None,
                 text=None,
                 types=None,
                 categories=None,
                 attributes=None):
        """
        Initialize a UnalignedElement object.

        :param str document_label: (optional) The label assigned to the document by the
        value of the `file_1_label` or `file_2_label` parameters on the **Compare two
        documents** method.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The text of the element.
        :param list[TypeLabelComparison] types: (optional) Description of the action
        specified by the element and whom it affects.
        :param list[CategoryComparison] categories: (optional) List of functional
        categories into which the element falls; in other words, the subject matter of the
        element.
        :param list[Attribute] attributes: (optional) List of document attributes.
        """
        self.document_label = document_label
        self.location = location
        self.text = text
        self.types = types
        self.categories = categories
        self.attributes = attributes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UnalignedElement object from a json dictionary."""
        args = {}
        validKeys = [
            'document_label', 'location', 'text', 'types', 'categories',
            'attributes'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UnalignedElement: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this UnalignedElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdatedLabelsIn(object):
    """
    The updated labeling from the input document, accounting for the submitted feedback.

    :attr list[TypeLabel] types: Description of the action specified by the element and
    whom it affects.
    :attr list[Category] categories: List of functional categories into which the element
    falls; in other words, the subject matter of the element.
    """

    def __init__(self, types, categories):
        """
        Initialize a UpdatedLabelsIn object.

        :param list[TypeLabel] types: Description of the action specified by the element
        and whom it affects.
        :param list[Category] categories: List of functional categories into which the
        element falls; in other words, the subject matter of the element.
        """
        self.types = types
        self.categories = categories

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdatedLabelsIn object from a json dictionary."""
        args = {}
        validKeys = ['types', 'categories']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UpdatedLabelsIn: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        return _dict

    def __str__(self):
        """Return a `str` version of this UpdatedLabelsIn object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdatedLabelsOut(object):
    """
    The updated labeling from the input document, accounting for the submitted feedback.

    :attr list[TypeLabel] types: (optional) Description of the action specified by the
    element and whom it affects.
    :attr list[Category] categories: (optional) List of functional categories into which
    the element falls; in other words, the subject matter of the element.
    :attr str modification: (optional) The type of modification the feedback entry in the
    `updated_labels` array. Possible values are `added`, `not_changed`, and `removed`.
    """

    def __init__(self, types=None, categories=None, modification=None):
        """
        Initialize a UpdatedLabelsOut object.

        :param list[TypeLabel] types: (optional) Description of the action specified by
        the element and whom it affects.
        :param list[Category] categories: (optional) List of functional categories into
        which the element falls; in other words, the subject matter of the element.
        :param str modification: (optional) The type of modification the feedback entry in
        the `updated_labels` array. Possible values are `added`, `not_changed`, and
        `removed`.
        """
        self.types = types
        self.categories = categories
        self.modification = modification

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdatedLabelsOut object from a json dictionary."""
        args = {}
        validKeys = ['types', 'categories', 'modification']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UpdatedLabelsOut: '
                + ', '.join(badKeys))
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'types') and self.types is not None:
            _dict['types'] = [x._to_dict() for x in self.types]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'modification') and self.modification is not None:
            _dict['modification'] = self.modification
        return _dict

    def __str__(self):
        """Return a `str` version of this UpdatedLabelsOut object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Value(object):
    """
    A value in a key-value pair.

    :attr str cell_id: (optional) The unique ID of the value in the table.
    :attr Location location: (optional) The numeric location of the identified element in
    the document, represented with two integers labeled `begin` and `end`.
    :attr str text: (optional) The text content of the table cell without HTML markup.
    """

    def __init__(self, cell_id=None, location=None, text=None):
        """
        Initialize a Value object.

        :param str cell_id: (optional) The unique ID of the value in the table.
        :param Location location: (optional) The numeric location of the identified
        element in the document, represented with two integers labeled `begin` and `end`.
        :param str text: (optional) The text content of the table cell without HTML
        markup.
        """
        self.cell_id = cell_id
        self.location = location
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Value object from a json dictionary."""
        args = {}
        validKeys = ['cell_id', 'location', 'text']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Value: ' +
                ', '.join(badKeys))
        if 'cell_id' in _dict:
            args['cell_id'] = _dict.get('cell_id')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
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
        """Return a `str` version of this Value object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
