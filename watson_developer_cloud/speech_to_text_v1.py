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
### Service Overview
 The service transcribes speech from various languages and audio formats to text with low
latency. The service supports transcription of the following languages: Brazilian
Portuguese, French, Japanese, Mandarin Chinese, Modern Standard Arabic, Spanish, UK
English, and US English. For most languages, the service supports two sampling rates,
broadband and narrowband.
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService, _remove_null_values
from .utils import deprecated
from watson_developer_cloud.websocket import RecognizeCallback, RecognizeListener
import base64
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

##############################################################################
# Service
##############################################################################


class SpeechToTextV1(WatsonService):
    """The Speech to Text V1 service."""

    default_url = 'https://stream.watsonplatform.net/speech-to-text/api'

    def __init__(self,
                 url=default_url,
                 username=None,
                 password=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
        """
        Construct a new client for the Speech to Text service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://stream.watsonplatform.net/speech-to-text/api").
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
            vcap_services_name='speech_to_text',
            url=url,
            username=username,
            password=password,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)

    #########################
    # Models
    #########################

    def get_model(self, model_id, **kwargs):
        """
        Retrieves information about the model.

        Returns information about a single specified language model that is available for
        use with the service. The information includes the name of the model and its
        minimum sampling rate in Hertz, among other things.

        :param str model_id: The identifier of the desired model in the form of its `name` from the output of **Get models**.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `SpeechModel` response.
        :rtype: dict
        """
        if model_id is None:
            raise ValueError('model_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/models/{0}'.format(*self._encode_path_vars(model_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def list_models(self, **kwargs):
        """
        Retrieves the models available for the service.

        Returns a list of all language models that are available for use with the service.
        The information includes the name of the model and its minimum sampling rate in
        Hertz, among other things.

        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `SpeechModels` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/models'
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    @deprecated('Use list_models instead.')
    def models(self):
        return self.list_models()

    #########################
    # Sessionless
    #########################

    def recognize(self,
                  model=None,
                  customization_id=None,
                  acoustic_customization_id=None,
                  customization_weight=None,
                  version=None,
                  audio=None,
                  content_type=None,
                  inactivity_timeout=None,
                  keywords=None,
                  keywords_threshold=None,
                  max_alternatives=None,
                  word_alternatives_threshold=None,
                  word_confidence=None,
                  timestamps=None,
                  profanity_filter=None,
                  smart_formatting=None,
                  speaker_labels=None,
                  **kwargs):
        """
        Sends audio for speech recognition in sessionless mode.

        :param str model: The identifier of the model that is to be used for the recognition request.
        :param str customization_id: The GUID of a custom language model that is to be used with the request. The base model of the specified custom language model must match the model specified with the `model` parameter. You must make the request with service credentials created for the instance of the service that owns the custom model. By default, no custom language model is used.
        :param str acoustic_customization_id: The GUID of a custom acoustic model that is to be used with the request. The base model of the specified custom acoustic model must match the model specified with the `model` parameter. You must make the request with service credentials created for the instance of the service that owns the custom model. By default, no custom acoustic model is used.
        :param float customization_weight: NON-MULTIPART ONLY: If you specify a customization ID with the request, you can use the customization weight to tell the service how much weight to give to words from the custom language model compared to those from the base model for speech recognition.   Specify a value between 0.0 and 1.0. Unless a different customization weight was specified for the custom model when it was trained, the default value is 0.3. A customization weight that you specify overrides a weight that was specified when the custom model was trained.   The default value yields the best performance in general. Assign a higher value if your audio makes frequent use of OOV words from the custom model. Use caution when setting the weight: a higher value can improve the accuracy of phrases from the custom model's domain, but it can negatively affect performance on non-domain phrases.
        :param str version: The version of the specified base `model` that is to be used for speech recognition. Multiple versions of a base model can exist when a model is updated for internal improvements. The parameter is intended primarily for use with custom models that have been upgraded for a new base model. The default value depends on whether the parameter is used with or without a custom model. For more information, see [Base model version](https://console.bluemix.net/docs/services/speech-to-text/input.html#version).
        :param str audio: NON-MULTIPART ONLY: Audio to transcribe in the format specified by the `Content-Type` header. **Required for a non-multipart request.**.
        :param str content_type: The type of the input: audio/basic, audio/flac, audio/l16, audio/mp3, audio/mpeg, audio/mulaw, audio/ogg, audio/ogg;codecs=opus, audio/ogg;codecs=vorbis, audio/wav, audio/webm, audio/webm;codecs=opus, audio/webm;codecs=vorbis, or multipart/form-data.
        :param int inactivity_timeout: NON-MULTIPART ONLY: The time in seconds after which, if only silence (no speech) is detected in submitted audio, the connection is closed with a 400 error. Useful for stopping audio submission from a live microphone when a user simply walks away. Use `-1` for infinity.
        :param list[str] keywords: NON-MULTIPART ONLY: Array of keyword strings to spot in the audio. Each keyword string can include one or more tokens. Keywords are spotted only in the final hypothesis, not in interim results. If you specify any keywords, you must also specify a keywords threshold. You can spot a maximum of 1000 keywords. Omit the parameter or specify an empty array if you do not need to spot keywords.
        :param float keywords_threshold: NON-MULTIPART ONLY: Confidence value that is the lower bound for spotting a keyword. A word is considered to match a keyword if its confidence is greater than or equal to the threshold. Specify a probability between 0 and 1 inclusive. No keyword spotting is performed if you omit the parameter. If you specify a threshold, you must also specify one or more keywords.
        :param int max_alternatives: NON-MULTIPART ONLY: Maximum number of alternative transcripts to be returned. By default, a single transcription is returned.
        :param float word_alternatives_threshold: NON-MULTIPART ONLY: Confidence value that is the lower bound for identifying a hypothesis as a possible word alternative (also known as \"Confusion Networks\"). An alternative word is considered if its confidence is greater than or equal to the threshold. Specify a probability between 0 and 1 inclusive. No alternative words are computed if you omit the parameter.
        :param bool word_confidence: NON-MULTIPART ONLY: If `true`, confidence measure per word is returned.
        :param bool timestamps: NON-MULTIPART ONLY: If `true`, time alignment for each word is returned.
        :param bool profanity_filter: NON-MULTIPART ONLY: If `true` (the default), filters profanity from all output except for keyword results by replacing inappropriate words with a series of asterisks. Set the parameter to `false` to return results with no censoring. Applies to US English transcription only.
        :param bool smart_formatting: NON-MULTIPART ONLY: If `true`, converts dates, times, series of digits and numbers, phone numbers, currency values, and Internet addresses into more readable, conventional representations in the final transcript of a recognition request. If `false` (the default), no formatting is performed. Applies to US English transcription only.
        :param bool speaker_labels: NON-MULTIPART ONLY: Indicates whether labels that identify which words were spoken by which participants in a multi-person exchange are to be included in the response. The default is `false`; no speaker labels are returned. Setting `speaker_labels` to `true` forces the `timestamps` parameter to be `true`, regardless of whether you specify `false` for the parameter.   To determine whether a language model supports speaker labels, use the **Get models** method and check that the attribute `speaker_labels` is set to `true`. You can also refer to [Speaker labels](https://console.bluemix.net/docs/services/speech-to-text/output.html#speaker_labels).
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `SpeechRecognitionResults` response.
        :rtype: dict
        """
        headers = {'Content-Type': content_type}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'model': model,
            'customization_id': customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'customization_weight': customization_weight,
            'version': version,
            'base_model_version': version,
            'inactivity_timeout': inactivity_timeout,
            'keywords': self._convert_list(keywords),
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'speaker_labels': speaker_labels
        }
        data = audio
        url = '/v1/recognize'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return response

    def recognize_with_websocket(self,
                                 audio=None,
                                 content_type='audio/l16; rate=44100',
                                 model='en-US_BroadbandModel',
                                 recognize_callback=None,
                                 customization_id=None,
                                 acoustic_customization_id=None,
                                 customization_weight=None,
                                 version=None,
                                 inactivity_timeout=None,
                                 interim_results=True,
                                 keywords=None,
                                 keywords_threshold=None,
                                 max_alternatives=1,
                                 word_alternatives_threshold=None,
                                 word_confidence=False,
                                 timestamps=False,
                                 profanity_filter=None,
                                 smart_formatting=False,
                                 speaker_labels=None,
                                 **kwargs):
        """
        Sends audio for speech recognition using web sockets.

        :param str audio: Audio to transcribe in the format specified by the `Content-Type` header.
        :param str content_type: The type of the input: audio/basic, audio/flac, audio/l16, audio/mp3, audio/mpeg, audio/mulaw, audio/ogg, audio/ogg;codecs=opus, audio/ogg;codecs=vorbis, audio/wav, audio/webm, audio/webm;codecs=opus, audio/webm;codecs=vorbis, or multipart/form-data.
        :param str model: The identifier of the model to be used for the recognition request.
        :param RecognizeCallback recognize_callback: The instance handling events returned from the service.
        :param str customization_id: The GUID of a custom language model that is to be used with the request. The base model of the specified custom language model must match the model specified with the `model` parameter. You must make the request with service credentials created for the instance of the service that owns the custom model. By default, no custom language model is used.
        :param str acoustic_customization_id: The GUID of a custom acoustic model that is to be used with the request. The base model of the specified custom acoustic model must match the model specified with the `model` parameter. You must make the request with service credentials created for the instance of the service that owns the custom model. By default, no custom acoustic model is used.
        :param float customization_weight: If you specify a `customization_id` with the request, you can use the `customization_weight` parameter to tell the service how much weight to give to words from the custom language model compared to those from the base model for speech recognition.   Specify a value between 0.0 and 1.0. Unless a different customization weight was specified for the custom model when it was trained, the default value is 0.3. A customization weight that you specify overrides a weight that was specified when the custom model was trained.   The default value yields the best performance in general. Assign a higher value if your audio makes frequent use of OOV words from the custom model. Use caution when setting the weight: a higher value can improve the accuracy of phrases from the custom model's domain, but it can negatively affect performance on non-domain phrases.
        :param str version: The version of the specified base `model` that is to be used for speech recognition. Multiple versions of a base model can exist when a model is updated for internal improvements. The parameter is intended primarily for use with custom models that have been upgraded for a new base model. The default value depends on whether the parameter is used with or without a custom model. For more information, see [Base model version](https://console.bluemix.net/docs/services/speech-to-text/input.html#version).
        :param int inactivity_timeout: The time in seconds after which, if only silence (no speech) is detected in submitted audio, the connection is closed with a 400 error. Useful for stopping audio submission from a live microphone when a user simply walks away. Use `-1` for infinity.
        :param bool interim_results: Send back non-final previews of each "sentence" as it is being processed. These results are ignored in text mode.
        :param list[str] keywords: Array of keyword strings to spot in the audio. Each keyword string can include one or more tokens. Keywords are spotted only in the final hypothesis, not in interim results. If you specify any keywords, you must also specify a keywords threshold. Omit the parameter or specify an empty array if you do not need to spot keywords.
        :param float keywords_threshold: Confidence value that is the lower bound for spotting a keyword. A word is considered to match a keyword if its confidence is greater than or equal to the threshold. Specify a probability between 0 and 1 inclusive. No keyword spotting is performed if you omit the parameter. If you specify a threshold, you must also specify one or more keywords.
        :param int max_alternatives: Maximum number of alternative transcripts to be returned. By default, a single transcription is returned.
        :param float word_alternatives_threshold: Confidence value that is the lower bound for identifying a hypothesis as a possible word alternative (also known as \"Confusion Networks\"). An alternative word is considered if its confidence is greater than or equal to the threshold. Specify a probability between 0 and 1 inclusive. No alternative words are computed if you omit the parameter.
        :param bool word_confidence: If `true`, confidence measure per word is returned.
        :param bool timestamps: If `true`, time alignment for each word is returned.
        :param bool profanity_filter: If `true` (the default), filters profanity from all output except for keyword results by replacing inappropriate words with a series of asterisks. Set the parameter to `false` to return results with no censoring. Applies to US English transcription only.
        :param bool smart_formatting: If `true`, converts dates, times, series of digits and numbers, phone numbers, currency values, and Internet addresses into more readable, conventional representations in the final transcript of a recognition request. If `false` (the default), no formatting is performed. Applies to US English transcription only.
        :param bool speaker_labels: Indicates whether labels that identify which words were spoken by which participants in a multi-person exchange are to be included in the response. The default is `false`; no speaker labels are returned. Setting `speaker_labels` to `true` forces the `timestamps` parameter to be `true`, regardless of whether you specify `false` for the parameter.   To determine whether a language model supports speaker labels, use the `GET /v1/models` method and check that the attribute `speaker_labels` is set to `true`. You can also refer to [Speaker labels](https://console.bluemix.net/docs/services/speech-to-text/output.html#speaker_labels).
        :param dict headers: A `dict` containing the request headers
        :return:
        """
        if audio is None:
            raise ValueError('Audio must be provided')
        if recognize_callback is None:
            raise ValueError('Recognize callback must be provided')
        if not isinstance(recognize_callback, RecognizeCallback):
            raise Exception(
                'Callback is not a derived class of RecognizeCallback')

        headers = {}
        if self.default_headers is not None:
            headers = self.default_headers.copy()
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        authstring = "{0}:{1}".format(self.username, self.password)
        base64_authorization = base64.b64encode(authstring.encode('utf-8')).decode('utf-8')
        headers['Authorization'] = 'Basic {0}'.format(base64_authorization)

        url = self.url.replace('https:', 'wss:')
        params = {
            'model': model,
            'customization_id': customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'customization_weight': customization_weight,
            'version': version
        }
        params = _remove_null_values(params)
        url = url + '/v1/recognize?{0}'.format(urlencode(params))

        options = {
            'content_type': content_type,
            'inactivity_timeout': inactivity_timeout,
            'interim_results': interim_results,
            'keywords': keywords,
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'speaker_labels': speaker_labels
        }
        options = _remove_null_values(options)

        RecognizeListener(audio, options, recognize_callback, url, headers)

    #########################
    # Asynchronous
    #########################

    def check_job(self, id, **kwargs):
        """
        Checks the status of the specified asynchronous job.

        :param str id: The ID of the job whose status is to be checked.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `RecognitionJob` response.
        :rtype: dict
        """
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/recognitions/{0}'.format(*self._encode_path_vars(id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def check_jobs(self, **kwargs):
        """
        Checks the status of all asynchronous jobs.

        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `RecognitionJobs` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/recognitions'
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def create_job(self,
                   audio,
                   content_type,
                   model=None,
                   callback_url=None,
                   events=None,
                   user_token=None,
                   results_ttl=None,
                   customization_id=None,
                   acoustic_customization_id=None,
                   customization_weight=None,
                   version=None,
                   inactivity_timeout=None,
                   keywords=None,
                   keywords_threshold=None,
                   max_alternatives=None,
                   word_alternatives_threshold=None,
                   word_confidence=None,
                   timestamps=None,
                   profanity_filter=None,
                   smart_formatting=None,
                   speaker_labels=None,
                   **kwargs):
        """
        Creates a job for an asynchronous recognition request.

        :param str audio: Audio to transcribe in the format specified by the `Content-Type` header.
        :param str content_type: The type of the input: audio/basic, audio/flac, audio/l16, audio/mp3, audio/mpeg, audio/mulaw, audio/ogg, audio/ogg;codecs=opus, audio/ogg;codecs=vorbis, audio/wav, audio/webm, audio/webm;codecs=opus, or audio/webm;codecs=vorbis.
        :param str model: The identifier of the model that is to be used for the recognition request.
        :param str callback_url: A URL to which callback notifications are to be sent. The URL must already be successfully white-listed by using the **Register a callback** method. Omit the parameter to poll the service for job completion and results. You can include the same callback URL with any number of job creation requests. Use the `user_token` parameter to specify a unique user-specified string with each job to differentiate the callback notifications for the jobs.
        :param str events: If the job includes a callback URL, a comma-separated list of notification events to which to subscribe. Valid events are: `recognitions.started` generates a callback notification when the service begins to process the job. `recognitions.completed` generates a callback notification when the job is complete; you must use the **Check a job** method to retrieve the results before they time out or are deleted. `recognitions.completed_with_results` generates a callback notification when the job is complete; the notification includes the results of the request. `recognitions.failed` generates a callback notification if the service experiences an error while processing the job. Omit the parameter to subscribe to the default events: `recognitions.started`, `recognitions.completed`, and `recognitions.failed`. The `recognitions.completed` and `recognitions.completed_with_results` events are incompatible; you can specify only of the two events. If the job does not include a callback URL, omit the parameter.
        :param str user_token: If the job includes a callback URL, a user-specified string that the service is to include with each callback notification for the job; the token allows the user to maintain an internal mapping between jobs and notification events. If the job does not include a callback URL, omit the parameter.
        :param int results_ttl: The number of minutes for which the results are to be available after the job has finished. If not delivered via a callback, the results must be retrieved within this time. Omit the parameter to use a time to live of one week. The parameter is valid with or without a callback URL.
        :param str customization_id: The GUID of a custom language model that is to be used with the request. The base model of the specified custom language model must match the model specified with the `model` parameter. You must make the request with service credentials created for the instance of the service that owns the custom model. By default, no custom language model is used.
        :param str acoustic_customization_id: The GUID of a custom acoustic model that is to be used with the request. The base model of the specified custom acoustic model must match the model specified with the `model` parameter. You must make the request with service credentials created for the instance of the service that owns the custom model. By default, no custom acoustic model is used.
        :param float customization_weight: If you specify a customization ID with the request, you can use the customization weight to tell the service how much weight to give to words from the custom language model compared to those from the base model for speech recognition.   Specify a value between 0.0 and 1.0. Unless a different customization weight was specified for the custom model when it was trained, the default value is 0.3. A customization weight that you specify overrides a weight that was specified when the custom model was trained.   The default value yields the best performance in general. Assign a higher value if your audio makes frequent use of OOV words from the custom model. Use caution when setting the weight: a higher value can improve the accuracy of phrases from the custom model's domain, but it can negatively affect  performance on non-domain phrases.
        :param str version: The version of the specified base `model` that is to be used with the request. Multiple versions of a base model can exist when a model is updated for internal improvements. The parameter is intended primarily for use with custom models that have been upgraded for a new base model. The default value depends on whether the parameter is used with or without a custom model. For more information, see [Base model version](https://console.bluemix.net/docs/services/speech-to-text/input.html#version).
        :param int inactivity_timeout: The time in seconds after which, if only silence (no speech) is detected in submitted audio, the connection is closed with a 400 error. Useful for stopping audio submission from a live microphone when a user simply walks away. Use `-1` for infinity.
        :param list[str] keywords: Array of keyword strings to spot in the audio. Each keyword string can include one or more tokens. Keywords are spotted only in the final hypothesis, not in interim results. If you specify any keywords, you must also specify a keywords threshold. You can spot a maximum of 1000 keywords. Omit the parameter or specify an empty array if you do not need to spot keywords.
        :param float keywords_threshold: Confidence value that is the lower bound for spotting a keyword. A word is considered to match a keyword if its confidence is greater than or equal to the threshold. Specify a probability between 0 and 1 inclusive. No keyword spotting is performed if you omit the parameter. If you specify a threshold, you must also specify one or more keywords.
        :param int max_alternatives: Maximum number of alternative transcripts to be returned. By default, a single transcription is returned.
        :param float word_alternatives_threshold: Confidence value that is the lower bound for identifying a hypothesis as a possible word alternative (also known as \"Confusion Networks\"). An alternative word is considered if its confidence is greater than or equal to the threshold. Specify a probability between 0 and 1 inclusive. No alternative words are computed if you omit the parameter.
        :param bool word_confidence: If `true`, confidence measure per word is returned.
        :param bool timestamps: If `true`, time alignment for each word is returned.
        :param bool profanity_filter: If `true` (the default), filters profanity from all output except for keyword results by replacing inappropriate words with a series of asterisks. Set the parameter to `false` to return results with no censoring. Applies to US English transcription only.
        :param bool smart_formatting: If `true`, converts dates, times, series of digits and numbers, phone numbers, currency values, and Internet addresses into more readable, conventional representations in the final transcript of a recognition request. If `false` (the default), no formatting is performed. Applies to US English transcription only.
        :param bool speaker_labels: Indicates whether labels that identify which words were spoken by which participants in a multi-person exchange are to be included in the response. The default is `false`; no speaker labels are returned. Setting `speaker_labels` to `true` forces the `timestamps` parameter to be `true`, regardless of whether you specify `false` for the parameter.   To determine whether a language model supports speaker labels, use the **Get models** method and check that the attribute `speaker_labels` is set to `true`. You can also refer to [Speaker labels](https://console.bluemix.net/docs/services/speech-to-text/output.html#speaker_labels).
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `RecognitionJob` response.
        :rtype: dict
        """
        if audio is None:
            raise ValueError('audio must be provided')
        if content_type is None:
            raise ValueError('content_type must be provided')
        headers = {'Content-Type': content_type}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'model': model,
            'callback_url': callback_url,
            'events': events,
            'user_token': user_token,
            'results_ttl': results_ttl,
            'customization_id': customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'customization_weight': customization_weight,
            'version': version,
            'base_model_version': version,
            'inactivity_timeout': inactivity_timeout,
            'keywords': self._convert_list(keywords),
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'speaker_labels': speaker_labels
        }
        data = audio
        url = '/v1/recognitions'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return response

    def delete_job(self, id, **kwargs):
        """
        Deletes the specified asynchronous job.

        Deletes the specified job. You cannot delete a job that the service is actively
        processing. Once you delete a job, its results are no longer available. The
        service automatically deletes a job and its results when the time to live for the
        results expires. You must submit the request with the service credentials of the
        user who created the job.

        :param str id: The ID of the job that is to be deleted.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/recognitions/{0}'.format(*self._encode_path_vars(id))
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    def register_callback(self, callback_url, user_secret=None, **kwargs):
        """
        Registers a callback URL for use with the asynchronous interface.

        :param str callback_url: An HTTP or HTTPS URL to which callback notifications are to be sent. To be white-listed, the URL must successfully echo the challenge string during URL verification. During verification, the client can also check the signature that the service sends in the `X-Callback-Signature` header to verify the origin of the request.
        :param str user_secret: A user-specified string that the service uses to generate the HMAC-SHA1 signature that it sends via the `X-Callback-Signature` header. The service includes the header during URL verification and with every notification sent to the callback URL. It calculates the signature over the payload of the notification. If you omit the parameter, the service does not send the header.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `RegisterStatus` response.
        :rtype: dict
        """
        if callback_url is None:
            raise ValueError('callback_url must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'callback_url': callback_url, 'user_secret': user_secret}
        url = '/v1/register_callback'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def unregister_callback(self, callback_url, **kwargs):
        """
        Removes the registration for an asynchronous callback URL.

        Unregisters a callback URL that was previously white-listed with a `POST
        register_callback` request for use with the asynchronous interface. Once
        unregistered, the URL can no longer be used with asynchronous recognition
        requests.

        :param str callback_url: The callback URL that is to be unregistered.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if callback_url is None:
            raise ValueError('callback_url must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'callback_url': callback_url}
        url = '/v1/unregister_callback'
        self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    #########################
    # Custom language models
    #########################

    def create_language_model(self,
                              name,
                              base_model_name,
                              dialect=None,
                              description=None,
                              **kwargs):
        """
        Creates a custom language model.

        Creates a new custom language model for a specified base model. The custom
        language model can be used only with the base model for which it is created. The
        model is owned by the instance of the service whose credentials are used to create
        it.

        :param str name: A user-defined name for the new custom language model. Use a name that is unique among all custom language models that you own. Use a localized name that matches the language of the custom model. Use a name that describes the domain of the custom model, such as `Medical custom model` or `Legal custom model`.
        :param str base_model_name: The name of the base language model that is to be customized by the new custom language model. The new custom model can be used only with the base model that it customizes. To determine whether a base model supports language model customization, request information about the base model and check that the attribute `custom_language_model` is set to `true`, or refer to [Language support for customization](https://console.bluemix.net/docs/services/speech-to-text/custom.html#languageSupport).
        :param str dialect: The dialect of the specified language that is to be used with the custom language model. The parameter is meaningful only for Spanish models, for which the service creates a custom language model that is suited for speech in one of the following dialects: * `es-ES` for Castilian Spanish (the default) * `es-LA` for Latin American Spanish * `es-US` for North American (Mexican) Spanish   A specified dialect must be valid for the base model. By default, the dialect matches the language of the base model; for example, `en-US` for either of the US English language models.
        :param str description: A description of the new custom language model. Use a localized description that matches the language of the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `LanguageModel` response.
        :rtype: dict
        """
        if name is None:
            raise ValueError('name must be provided')
        if base_model_name is None:
            raise ValueError('base_model_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        data = {
            'name': name,
            'base_model_name': base_model_name,
            'dialect': dialect,
            'description': description
        }
        url = '/v1/customizations'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return response

    @deprecated('Use create_language_model() instead.')
    def create_custom_model(self,
                            name,
                            description="",
                            base_model="en-US_BroadbandModel"):
        return self.create_language_model(
            name, base_model, description=description)

    def delete_language_model(self, customization_id, **kwargs):
        """
        Deletes a custom language model.

        Deletes an existing custom language model. The custom model cannot be deleted if
        another request, such as adding a corpus to the model, is currently being
        processed. You must use credentials for the instance of the service that owns a
        model to delete it.

        :param str customization_id: The GUID of the custom language model that is to be deleted. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    @deprecated('Use delete_language_model() instead.')
    def delete_custom_model(self, modelid):
        return self.delete_language_model(modelid)

    def get_language_model(self, customization_id, **kwargs):
        """
        Lists information about a custom language model.

        Lists information about a specified custom language model. You must use
        credentials for the instance of the service that owns a model to list information
        about it.

        :param str customization_id: The GUID of the custom language model for which information is to be returned. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `LanguageModel` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    @deprecated('Use get_language_model() instead.')
    def get_custom_model(self, modelid):
        return self.get_language_model(modelid)

    def list_language_models(self, language=None, **kwargs):
        """
        Lists information about all custom language models.

        Lists information about all custom language models that are owned by an instance
        of the service. Use the `language` parameter to see all custom language models for
        the specified language; omit the parameter to see all custom language models for
        all languages. You must use credentials for the instance of the service that owns
        a model to list information about it.

        :param str language: The identifier of the language for which custom language models are to be returned (for example, `en-US`). Omit the parameter to see all custom language models owned by the requesting service credentials.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `LanguageModels` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'language': language}
        url = '/v1/customizations'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    @deprecated('Use list_language_models() instead.')
    def list_custom_models(self):
        return self.list_language_models()

    def reset_language_model(self, customization_id, **kwargs):
        """
        Resets a custom language model.

        Resets a custom language model by removing all corpora and words from the model.
        Resetting a custom language model initializes the model to its state when it was
        first created. Metadata such as the name and language of the model are preserved,
        but the model's words resource is removed and must be re-created. You must use
        credentials for the instance of the service that owns a model to reset it.

        :param str customization_id: The GUID of the custom language model that is to be reset. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}/reset'.format(
            *self._encode_path_vars(customization_id))
        self.request(method='POST', url=url, headers=headers, accept_json=True)
        return None

    def train_language_model(self,
                             customization_id,
                             word_type_to_add=None,
                             customization_weight=None,
                             **kwargs):
        """
        Trains a custom language model.

        :param str customization_id: The GUID of the custom language model that is to be trained. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str word_type_to_add: The type of words from the custom language model's words resource on which to train the model: * `all` (the default) trains the model on all new words, regardless of whether they were extracted from corpora or were added or modified by the user. * `user` trains the model only on new words that were added or modified by the user; the model is not trained on new words extracted from corpora.
        :param float customization_weight: Specifies a customization weight for the custom language model. The customization weight tells the service how much weight to give to words from the custom language model compared to those from the base model for speech recognition. Specify a value between 0.0 and 1.0. The default value is 0.3.   The default value yields the best performance in general. Assign a higher value if your audio makes frequent use of OOV words from the custom model. Use caution when setting the weight: a higher value can improve the accuracy of phrases from the custom model's domain, but it can negatively affect performance on non-domain phrases.   The value that you assign is used for all recognition requests that use the model. You can override it for any recognition request by specifying a customization weight for that request.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'word_type_to_add': word_type_to_add,
            'customization_weight': customization_weight
        }
        url = '/v1/customizations/{0}/train'.format(
            *self._encode_path_vars(customization_id))
        self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    @deprecated('Use train_language_model() instead.')
    def train_custom_model(self,
                           customization_id,
                           customization_weight=None,
                           word_type=None):
        self.train_language_model(customization_id, word_type,
                                  customization_weight)

    def upgrade_language_model(self, customization_id, **kwargs):
        """
        Upgrades a custom language model.

        :param str customization_id: The GUID of the custom language model that is to be upgraded. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}/upgrade_model'.format(
            *self._encode_path_vars(customization_id))
        self.request(method='POST', url=url, headers=headers, accept_json=True)
        return None

    #########################
    # Custom corpora
    #########################

    def add_corpus(self,
                   customization_id,
                   corpus_name,
                   corpus_file,
                   allow_overwrite=None,
                   corpus_file_content_type=None,
                   corpus_filename=None,
                   **kwargs):
        """
        Adds a corpus text file to a custom language model.

        :param str customization_id: The GUID of the custom language model to which a corpus is to be added. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str corpus_name: The name of the corpus that is to be added to the custom language model. The name cannot contain spaces and cannot be the string `user`, which is reserved by the service to denote custom words added or modified by the user. Use a localized name that matches the language of the custom model.
        :param file corpus_file: A plain text file that contains the training data for the corpus. Encode the file in UTF-8 if it contains non-ASCII characters; the service assumes UTF-8 encoding if it encounters non-ASCII characters. With cURL, use the `--data-binary` option to upload the file for the request.
        :param bool allow_overwrite: Indicates whether the specified corpus is to overwrite an existing corpus with the same name. If a corpus with the same name already exists, the request fails unless `allow_overwrite` is set to `true`; by default, the parameter is `false`. The parameter has no effect if a corpus with the same name does not already exist.
        :param str corpus_file_content_type: The content type of corpus_file.
        :param str corpus_filename: The filename for corpus_file.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if corpus_name is None:
            raise ValueError('corpus_name must be provided')
        if corpus_file is None:
            raise ValueError('corpus_file must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'allow_overwrite': allow_overwrite}
        if not corpus_filename and hasattr(corpus_file, 'name'):
            corpus_filename = corpus_file.name
        mime_type = corpus_file_content_type or 'application/octet-stream'
        corpus_file_tuple = (corpus_filename, corpus_file, mime_type)
        url = '/v1/customizations/{0}/corpora/{1}'.format(
            *self._encode_path_vars(customization_id, corpus_name))
        self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={'corpus_file': corpus_file_tuple},
            accept_json=True)
        return None

    def delete_corpus(self, customization_id, corpus_name, **kwargs):
        """
        Deletes a corpus from a custom language model.

        :param str customization_id: The GUID of the custom language model from which a corpus is to be deleted. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str corpus_name: The name of the corpus that is to be deleted from the custom language model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if corpus_name is None:
            raise ValueError('corpus_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}/corpora/{1}'.format(
            *self._encode_path_vars(customization_id, corpus_name))
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    def get_corpus(self, customization_id, corpus_name, **kwargs):
        """
        Lists information about a corpus for a custom language model.

        Lists information about a corpus from a custom language model. The information
        includes the total number of words and out-of-vocabulary (OOV) words, name, and
        status of the corpus. You must use credentials for the instance of the service
        that owns a model to list its corpora.

        :param str customization_id: The GUID of the custom language model for which a corpus is to be listed. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str corpus_name: The name of the corpus about which information is to be listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Corpus` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if corpus_name is None:
            raise ValueError('corpus_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}/corpora/{1}'.format(
            *self._encode_path_vars(customization_id, corpus_name))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def list_corpora(self, customization_id, **kwargs):
        """
        Lists information about all corpora for a custom language model.

        Lists information about all corpora from a custom language model. The information
        includes the total number of words and out-of-vocabulary (OOV) words, name, and
        status of each corpus. You must use credentials for the instance of the service
        that owns a model to list its corpora.

        :param str customization_id: The GUID of the custom language model for which corpora are to be listed. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Corpora` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}/corpora'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # Custom words
    #########################

    def add_word(self,
                 customization_id,
                 word_name,
                 sounds_like=None,
                 display_as=None,
                 **kwargs):
        """
        Adds a custom word to a custom language model.

        :param str customization_id: The GUID of the custom language model to which a word is to be added. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str word_name: The custom word that is to be added to or updated in the custom model. Do not include spaces in the word. Use a - (dash) or _ (underscore) to connect the tokens of compound words.
        :param list[str] sounds_like: An array of sounds-like pronunciations for the custom word. Specify how words that are difficult to pronounce, foreign words, acronyms, and so on can be pronounced by users. For a word that is not in the service's base vocabulary, omit the parameter to have the service automatically generate a sounds-like pronunciation for the word. For a word that is in the service's base vocabulary, use the parameter to specify additional pronunciations for the word. You cannot override the default pronunciation of a word; pronunciations you add augment the pronunciation from the base vocabulary. A word can have at most five sounds-like pronunciations, and a pronunciation can include at most 40 characters not including spaces.
        :param str display_as: An alternative spelling for the custom word when it appears in a transcript. Use the parameter when you want the word to have a spelling that is different from its usual representation or from its spelling in corpora training data.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word_name is None:
            raise ValueError('word_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        data = {
            'word': word_name,
            'sounds_like': sounds_like,
            'display_as': display_as
        }
        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word_name))
        self.request(
            method='PUT',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return None

    @deprecated('Use add_word instead.')
    def add_custom_word(self, customization_id, custom_word):
        return self.add_word(customization_id, custom_word)

    def add_words(self, customization_id, words, **kwargs):
        """
        Adds one or more custom words to a custom language model.

        :param str customization_id: The GUID of the custom language model to which words are to be added. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param list[CustomWord] words: An array of objects that provides information about each custom word that is to be added to or updated in the custom language model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if words is None:
            raise ValueError('words must be provided')
        words = [self._convert_model(x, CustomWord) for x in words]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        data = {'words': words}
        url = '/v1/customizations/{0}/words'.format(
            *self._encode_path_vars(customization_id))
        self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return None

    @deprecated('Use add_words() instead.')
    def add_custom_words(self, customization_id, custom_words):
        return self.add_words(customization_id, custom_words)

    def delete_word(self, customization_id, word_name, **kwargs):
        """
        Deletes a custom word from a custom language model.

        :param str customization_id: The GUID of the custom language model from which a word is to be deleted. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str word_name: The custom word that is to be deleted from the custom language model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word_name is None:
            raise ValueError('word_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word_name))
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    @deprecated('Use delete_word() instead.')
    def delete_custom_word(self, customization_id, custom_word):
        return self.delete_word(customization_id, custom_word)

    def get_word(self, customization_id, word_name, **kwargs):
        """
        Lists a custom word from a custom language model.

        Lists information about a custom word from a custom language model. You must use
        credentials for the instance of the service that owns a model to query information
        about its words.

        :param str customization_id: The GUID of the custom language model from which a word is to be queried. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str word_name: The custom word that is to be queried from the custom language model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Word` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word_name is None:
            raise ValueError('word_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word_name))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    @deprecated('Use get_word() instead.')
    def get_custom_word(self, customization_id, custom_word):
        return self.get_word(customization_id, custom_word)

    def list_words(self, customization_id, word_type=None, sort=None, **kwargs):
        """
        Lists all custom words from a custom language model.

        Lists information about custom words from a custom language model. You can list
        all words from the custom model's words resource, only custom words that were
        added or modified by the user, or only out-of-vocabulary (OOV) words that were
        extracted from corpora. You can also indicate the order in which the service is to
        return words; by default, words are listed in ascending alphabetical order. You
        must use credentials for the instance of the service that owns a model to query
        information about its words.

        :param str customization_id: The GUID of the custom language model from which words are to be queried. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str word_type: The type of words to be listed from the custom language model's words resource: * `all` (the default) shows all words. * `user` shows only custom words that were added or modified by the user. * `corpora` shows only OOV that were extracted from corpora.
        :param str sort: Indicates the order in which the words are to be listed, `alphabetical` or by `count`. You can prepend an optional `+` or `-` to an argument to indicate whether the results are to be sorted in ascending or descending order. By default, words are sorted in ascending alphabetical order. For alphabetical ordering, the lexicographical precedence is numeric values, uppercase letters, and lowercase letters. For count ordering, values with the same count are ordered alphabetically. With cURL, URL encode the `+` symbol as `%2B`.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Words` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'word_type': word_type, 'sort': sort}
        url = '/v1/customizations/{0}/words'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_custom_words(self, customization_id, word_type=None, sort=None):
        return self.list_words(customization_id, word_type, sort)

    #########################
    # Custom acoustic models
    #########################

    def create_acoustic_model(self,
                              name,
                              base_model_name,
                              description=None,
                              **kwargs):
        """
        Creates a custom acoustic model.

        Creates a new custom acoustic model for a specified base model. The custom
        acoustic model can be used only with the base model for which it is created. The
        model is owned by the instance of the service whose credentials are used to create
        it.

        :param str name: A user-defined name for the new custom acoustic model. Use a name that is unique among all custom acoustic models that you own. Use a localized name that matches the language of the custom model. Use a name that describes the acoustic environment of the custom model, such as `Mobile custom model` or `Noisy car custom model`.
        :param str base_model_name: The name of the base language model that is to be customized by the new custom acoustic model. The new custom model can be used only with the base model that it customizes. To determine whether a base model supports acoustic model customization, refer to [Language support for customization](https://console.bluemix.net/docs/services/speech-to-text/custom.html#languageSupport).
        :param str description: A description of the new custom acoustic model. Use a localized description that matches the language of the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `AcousticModel` response.
        :rtype: dict
        """
        if name is None:
            raise ValueError('name must be provided')
        if base_model_name is None:
            raise ValueError('base_model_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        data = {
            'name': name,
            'base_model_name': base_model_name,
            'description': description
        }
        url = '/v1/acoustic_customizations'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return response

    def delete_acoustic_model(self, customization_id, **kwargs):
        """
        Deletes a custom acoustic model.

        Deletes an existing custom acoustic model. The custom model cannot be deleted if
        another request, such as adding an audio resource to the model, is currently being
        processed. You must use credentials for the instance of the service that owns a
        model to delete it.

        :param str customization_id: The GUID of the custom acoustic model that is to be deleted. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/acoustic_customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    def get_acoustic_model(self, customization_id, **kwargs):
        """
        Lists information about a custom acoustic model.

        Lists information about a specified custom acoustic model. You must use
        credentials for the instance of the service that owns a model to list information
        about it.

        :param str customization_id: The GUID of the custom acoustic model for which information is to be returned. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `AcousticModel` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/acoustic_customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def list_acoustic_models(self, language=None, **kwargs):
        """
        Lists information about all custom acoustic models.

        Lists information about all custom acoustic models that are owned by an instance
        of the service. Use the `language` parameter to see all custom acoustic models for
        the specified language; omit the parameter to see all custom acoustic models for
        all languages. You must use credentials for the instance of the service that owns
        a model to list information about it.

        :param str language: The identifier of the language for which custom acoustic models are to be returned (for example, `en-US`). Omit the parameter to see all custom acoustic models owned by the requesting service credentials.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `AcousticModels` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'language': language}
        url = '/v1/acoustic_customizations'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def reset_acoustic_model(self, customization_id, **kwargs):
        """
        Resets a custom acoustic model.

        Resets a custom acoustic model by removing all audio resources from the model.
        Resetting a custom acoustic model initializes the model to its state when it was
        first created. Metadata such as the name and language of the model are preserved,
        but the model's audio resources are removed and must be re-created. You must use
        credentials for the instance of the service that owns a model to reset it.

        :param str customization_id: The GUID of the custom acoustic model that is to be reset. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/acoustic_customizations/{0}/reset'.format(
            *self._encode_path_vars(customization_id))
        self.request(method='POST', url=url, headers=headers, accept_json=True)
        return None

    def train_acoustic_model(self,
                             customization_id,
                             custom_language_model_id=None,
                             **kwargs):
        """
        Trains a custom acoustic model.

        :param str customization_id: The GUID of the custom acoustic model that is to be trained. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str custom_language_model_id: The GUID of a custom language model that is to be used during training of the custom acoustic model. Specify a custom language model that has been trained with verbatim transcriptions of the audio resources or that contains words that are relevant to the contents of the audio resources.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'custom_language_model_id': custom_language_model_id}
        url = '/v1/acoustic_customizations/{0}/train'.format(
            *self._encode_path_vars(customization_id))
        self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def upgrade_acoustic_model(self,
                               customization_id,
                               custom_language_model_id=None,
                               **kwargs):
        """
        Upgrades a custom acoustic model.

        :param str customization_id: The GUID of the custom acoustic model that is to be upgraded. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str custom_language_model_id: If the custom acoustic model was trained with a custom language model, the GUID of that custom language model. The custom language model must be upgraded before the custom acoustic model can be upgraded.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'custom_language_model_id': custom_language_model_id}
        url = '/v1/acoustic_customizations/{0}/upgrade_model'.format(
            *self._encode_path_vars(customization_id))
        self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    #########################
    # Custom audio resources
    #########################

    def add_audio(self,
                  customization_id,
                  audio_name,
                  audio_resource,
                  content_type,
                  contained_content_type=None,
                  allow_overwrite=None,
                  **kwargs):
        """
        Adds an audio resource to a custom acoustic model.

        :param str customization_id: The GUID of the custom acoustic model to which an audio resource is to be added. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str audio_name: The name of the audio resource that is to be added to the custom acoustic model. The name cannot contain spaces. Use a localized name that matches the language of the custom model.
        :param list[str] audio_resource: The audio resource that is to be added to the custom acoustic model, an individual audio file or an archive file.
        :param str content_type: The type of the input: application/zip, application/gzip, audio/basic, audio/flac, audio/l16, audio/mp3, audio/mpeg, audio/mulaw, audio/ogg, audio/ogg;codecs=opus, audio/ogg;codecs=vorbis, audio/wav, audio/webm, audio/webm;codecs=opus, or audio/webm;codecs=vorbis.
        :param str contained_content_type: For an archive-type resource that contains audio files whose format is not `audio/wav`, specifies the format of the audio files. The header accepts all of the audio formats supported for use with speech recognition and with the `Content-Type` header, including the `rate`, `channels`, and `endianness` parameters that are used with some formats. For a complete list of supported audio formats, see [Audio formats](/docs/services/speech-to-text/input.html#formats).
        :param bool allow_overwrite: Indicates whether the specified audio resource is to overwrite an existing resource with the same name. If a resource with the same name already exists, the request fails unless `allow_overwrite` is set to `true`; by default, the parameter is `false`. The parameter has no effect if a resource with the same name does not already exist.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if audio_name is None:
            raise ValueError('audio_name must be provided')
        if audio_resource is None:
            raise ValueError('audio_resource must be provided')
        if content_type is None:
            raise ValueError('content_type must be provided')
        headers = {
            'Content-Type': content_type,
            'Contained-Content-Type': contained_content_type
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'allow_overwrite': allow_overwrite}
        data = audio_resource
        url = '/v1/acoustic_customizations/{0}/audio/{1}'.format(
            *self._encode_path_vars(customization_id, audio_name))
        self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return None

    def delete_audio(self, customization_id, audio_name, **kwargs):
        """
        Deletes an audio resource from a custom acoustic model.

        :param str customization_id: The GUID of the custom acoustic model from which an audio resource is to be deleted. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str audio_name: The name of the audio resource that is to be deleted from the custom acoustic model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if audio_name is None:
            raise ValueError('audio_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/acoustic_customizations/{0}/audio/{1}'.format(
            *self._encode_path_vars(customization_id, audio_name))
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    def get_audio(self, customization_id, audio_name, **kwargs):
        """
        Lists information about an audio resource for a custom acoustic model.

        :param str customization_id: The GUID of the custom acoustic model for which an audio resource is to be listed. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param str audio_name: The name of the audio resource about which information is to be listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `AudioListing` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if audio_name is None:
            raise ValueError('audio_name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/acoustic_customizations/{0}/audio/{1}'.format(
            *self._encode_path_vars(customization_id, audio_name))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def list_audio(self, customization_id, **kwargs):
        """
        Lists information about all audio resources for a custom acoustic model.

        Lists information about all audio resources from a custom acoustic model. The
        information includes the name of the resource and information about its audio
        data, such as its duration. It also includes the status of the audio resource,
        which is important for checking the service's analysis of the resource in response
        to a request to add it to the custom acoustic model. You must use credentials for
        the instance of the service that owns a model to list its audio resources.

        :param str customization_id: The GUID of the custom acoustic model for which audio resources are to be listed. You must make the request with service credentials created for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `AudioResources` response.
        :rtype: dict
        """
        if customization_id is None:
            raise ValueError('customization_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/acoustic_customizations/{0}/audio'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class AcousticModel(object):
    """
    AcousticModel.

    :attr str customization_id: The customization ID (GUID) of the custom acoustic model. **Note:** When you create a new custom acoustic model, the service returns only the GUID of the new model; it does not return the other fields of this object.
    :attr str created: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom acoustic model was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str language: (optional) The language identifier of the custom acoustic model (for example, `en-US`).
    :attr list[str] versions: (optional) A list of the available versions of the custom acoustic model. Each element of the array indicates a version of the base model with which the custom model can be used. Multiple versions exist only if the custom model has been upgraded; otherwise, only a single version is shown.
    :attr str owner: (optional) The GUID of the service credentials for the instance of the service that owns the custom acoustic model.
    :attr str name: (optional) The name of the custom acoustic model.
    :attr str description: (optional) The description of the custom acoustic model.
    :attr str base_model_name: (optional) The name of the language model for which the custom acoustic model was created.
    :attr str status: (optional) The current status of the custom acoustic model: * `pending` indicates that the model was created but is waiting either for training data to be added or for the service to finish analyzing added data. * `ready` indicates that the model contains data and is ready to be trained. * `training` indicates that the model is currently being trained. * `available` indicates that the model is trained and ready to use. * `upgrading` indicates that the model is currently being upgraded. * `failed` indicates that training of the model failed.
    :attr int progress: (optional) A percentage that indicates the progress of the custom acoustic model's current training. A value of `100` means that the model is fully trained. **Note:** The `progress` field does not currently reflect the progress of the training; the field changes from `0` to `100` when training is complete.
    :attr str warnings: (optional) If the request included unknown parameters, the following message: `Unexpected query parameter(s) ['parameters'] detected`, where `parameters` is a list that includes a quoted string for each unknown parameter.
    """

    def __init__(self,
                 customization_id,
                 created=None,
                 language=None,
                 versions=None,
                 owner=None,
                 name=None,
                 description=None,
                 base_model_name=None,
                 status=None,
                 progress=None,
                 warnings=None):
        """
        Initialize a AcousticModel object.

        :param str customization_id: The customization ID (GUID) of the custom acoustic model. **Note:** When you create a new custom acoustic model, the service returns only the GUID of the new model; it does not return the other fields of this object.
        :param str created: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom acoustic model was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str language: (optional) The language identifier of the custom acoustic model (for example, `en-US`).
        :param list[str] versions: (optional) A list of the available versions of the custom acoustic model. Each element of the array indicates a version of the base model with which the custom model can be used. Multiple versions exist only if the custom model has been upgraded; otherwise, only a single version is shown.
        :param str owner: (optional) The GUID of the service credentials for the instance of the service that owns the custom acoustic model.
        :param str name: (optional) The name of the custom acoustic model.
        :param str description: (optional) The description of the custom acoustic model.
        :param str base_model_name: (optional) The name of the language model for which the custom acoustic model was created.
        :param str status: (optional) The current status of the custom acoustic model: * `pending` indicates that the model was created but is waiting either for training data to be added or for the service to finish analyzing added data. * `ready` indicates that the model contains data and is ready to be trained. * `training` indicates that the model is currently being trained. * `available` indicates that the model is trained and ready to use. * `upgrading` indicates that the model is currently being upgraded. * `failed` indicates that training of the model failed.
        :param int progress: (optional) A percentage that indicates the progress of the custom acoustic model's current training. A value of `100` means that the model is fully trained. **Note:** The `progress` field does not currently reflect the progress of the training; the field changes from `0` to `100` when training is complete.
        :param str warnings: (optional) If the request included unknown parameters, the following message: `Unexpected query parameter(s) ['parameters'] detected`, where `parameters` is a list that includes a quoted string for each unknown parameter.
        """
        self.customization_id = customization_id
        self.created = created
        self.language = language
        self.versions = versions
        self.owner = owner
        self.name = name
        self.description = description
        self.base_model_name = base_model_name
        self.status = status
        self.progress = progress
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AcousticModel object from a json dictionary."""
        args = {}
        if 'customization_id' in _dict:
            args['customization_id'] = _dict.get('customization_id')
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in AcousticModel JSON'
            )
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'versions' in _dict:
            args['versions'] = _dict.get('versions')
        if 'owner' in _dict:
            args['owner'] = _dict.get('owner')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'base_model_name' in _dict:
            args['base_model_name'] = _dict.get('base_model_name')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'progress' in _dict:
            args['progress'] = _dict.get('progress')
        if 'warnings' in _dict:
            args['warnings'] = _dict.get('warnings')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'customization_id') and self.customization_id is not None:
            _dict['customization_id'] = self.customization_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'versions') and self.versions is not None:
            _dict['versions'] = self.versions
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self,
                   'base_model_name') and self.base_model_name is not None:
            _dict['base_model_name'] = self.base_model_name
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'progress') and self.progress is not None:
            _dict['progress'] = self.progress
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = self.warnings
        return _dict

    def __str__(self):
        """Return a `str` version of this AcousticModel object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AcousticModels(object):
    """
    AcousticModels.

    :attr list[AcousticModel] customizations: An array of objects that provides information about each available custom acoustic model. The array is empty if the requesting service credentials own no custom acoustic models (if no language is specified) or own no custom acoustic models for the specified language.
    """

    def __init__(self, customizations):
        """
        Initialize a AcousticModels object.

        :param list[AcousticModel] customizations: An array of objects that provides information about each available custom acoustic model. The array is empty if the requesting service credentials own no custom acoustic models (if no language is specified) or own no custom acoustic models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AcousticModels object from a json dictionary."""
        args = {}
        if 'customizations' in _dict:
            args['customizations'] = [
                AcousticModel._from_dict(x)
                for x in (_dict.get('customizations'))
            ]
        else:
            raise ValueError(
                'Required property \'customizations\' not present in AcousticModels JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'customizations') and self.customizations is not None:
            _dict['customizations'] = [
                x._to_dict() for x in self.customizations
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this AcousticModels object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioDetails(object):
    """
    AudioDetails.

    :attr str type: The type of the audio resource: * `audio` for an individual audio file * `archive` for an archive (**.zip** or **.tar.gz**) file that contains audio files.
    :attr str codec: (optional) **For an audio-type resource,** the codec in which the audio is encoded. Omitted for an archive-type resource.
    :attr int frequency: (optional) **For an audio-type resource,** the sampling rate of the audio in Hertz (samples per second). Omitted for an archive-type resource.
    :attr str compression: (optional) **For an archive-type resource,** the format of the compressed archive: * `zip` for a **.zip** file * `gzip` for a **.tar.gz** file   Omitted for an audio-type resource.
    """

    def __init__(self, type, codec=None, frequency=None, compression=None):
        """
        Initialize a AudioDetails object.

        :param str type: The type of the audio resource: * `audio` for an individual audio file * `archive` for an archive (**.zip** or **.tar.gz**) file that contains audio files.
        :param str codec: (optional) **For an audio-type resource,** the codec in which the audio is encoded. Omitted for an archive-type resource.
        :param int frequency: (optional) **For an audio-type resource,** the sampling rate of the audio in Hertz (samples per second). Omitted for an archive-type resource.
        :param str compression: (optional) **For an archive-type resource,** the format of the compressed archive: * `zip` for a **.zip** file * `gzip` for a **.tar.gz** file   Omitted for an audio-type resource.
        """
        self.type = type
        self.codec = codec
        self.frequency = frequency
        self.compression = compression

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioDetails object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in AudioDetails JSON')
        if 'codec' in _dict:
            args['codec'] = _dict.get('codec')
        if 'frequency' in _dict:
            args['frequency'] = _dict.get('frequency')
        if 'compression' in _dict:
            args['compression'] = _dict.get('compression')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'codec') and self.codec is not None:
            _dict['codec'] = self.codec
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        if hasattr(self, 'compression') and self.compression is not None:
            _dict['compression'] = self.compression
        return _dict

    def __str__(self):
        """Return a `str` version of this AudioDetails object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioListing(object):
    """
    AudioListing.

    :attr float duration: (optional) **For an audio-type resource,**  the total seconds of audio in the resource. Omitted for an archive-type resource.
    :attr str name: (optional) **For an audio-type resource,** the name of the resource. Omitted for an archive-type resource.
    :attr AudioDetails details: (optional) **For an audio-type resource,** an `AudioDetails` object that provides detailed information about the resource. The object is empty until the service finishes processing the audio. Omitted for an archive-type resource.
    :attr str status: (optional) **For an audio-type resource,** the status of the resource: * `ok` indicates that the service has successfully analyzed the audio data. The data can be used to train the custom model. * `being_processed` indicates that the service is still analyzing the audio data. The service cannot accept requests to add new audio resources or to train the custom model until its analysis is complete. * `invalid` indicates that the audio data is not valid for training the custom model (possibly because it has the wrong format or sampling rate, or because it is corrupted).   Omitted for an archive-type resource.
    :attr AudioResource container: (optional) **For an archive-type resource,** an object of type `AudioResource` that provides information about the resource. Omitted for an audio-type resource.
    :attr list[AudioResource] audio: (optional) **For an archive-type resource,** an array of `AudioResource` objects that provides information about the audio-type resources that are contained in the resource. Omitted for an audio-type resource.
    """

    def __init__(self,
                 duration=None,
                 name=None,
                 details=None,
                 status=None,
                 container=None,
                 audio=None):
        """
        Initialize a AudioListing object.

        :param float duration: (optional) **For an audio-type resource,**  the total seconds of audio in the resource. Omitted for an archive-type resource.
        :param str name: (optional) **For an audio-type resource,** the name of the resource. Omitted for an archive-type resource.
        :param AudioDetails details: (optional) **For an audio-type resource,** an `AudioDetails` object that provides detailed information about the resource. The object is empty until the service finishes processing the audio. Omitted for an archive-type resource.
        :param str status: (optional) **For an audio-type resource,** the status of the resource: * `ok` indicates that the service has successfully analyzed the audio data. The data can be used to train the custom model. * `being_processed` indicates that the service is still analyzing the audio data. The service cannot accept requests to add new audio resources or to train the custom model until its analysis is complete. * `invalid` indicates that the audio data is not valid for training the custom model (possibly because it has the wrong format or sampling rate, or because it is corrupted).   Omitted for an archive-type resource.
        :param AudioResource container: (optional) **For an archive-type resource,** an object of type `AudioResource` that provides information about the resource. Omitted for an audio-type resource.
        :param list[AudioResource] audio: (optional) **For an archive-type resource,** an array of `AudioResource` objects that provides information about the audio-type resources that are contained in the resource. Omitted for an audio-type resource.
        """
        self.duration = duration
        self.name = name
        self.details = details
        self.status = status
        self.container = container
        self.audio = audio

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioListing object from a json dictionary."""
        args = {}
        if 'duration' in _dict:
            args['duration'] = _dict.get('duration')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'details' in _dict:
            args['details'] = AudioDetails._from_dict(_dict.get('details'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'container' in _dict:
            args['container'] = AudioResource._from_dict(
                _dict.get('container'))
        if 'audio' in _dict:
            args['audio'] = [
                AudioResource._from_dict(x) for x in (_dict.get('audio'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'duration') and self.duration is not None:
            _dict['duration'] = self.duration
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'details') and self.details is not None:
            _dict['details'] = self.details._to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'container') and self.container is not None:
            _dict['container'] = self.container._to_dict()
        if hasattr(self, 'audio') and self.audio is not None:
            _dict['audio'] = [x._to_dict() for x in self.audio]
        return _dict

    def __str__(self):
        """Return a `str` version of this AudioListing object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioResource(object):
    """
    AudioResource.

    :attr float duration: The total seconds of audio in the audio resource.
    :attr str name: The name of the audio resource.
    :attr AudioDetails details: An `AudioDetails` object that provides detailed information about the audio resource. The object is empty until the service finishes processing the audio.
    :attr str status: The status of the audio resource: * `ok` indicates that the service has successfully analyzed the audio data. The data can be used to train the custom model. * `being_processed` indicates that the service is still analyzing the audio data. The service cannot accept requests to add new audio resources or to train the custom model until its analysis is complete. * `invalid` indicates that the audio data is not valid for training the custom model (possibly because it has the wrong format or sampling rate, or because it is corrupted). For an archive file, the entire archive is invalid if any of its audio files are invalid.
    """

    def __init__(self, duration, name, details, status):
        """
        Initialize a AudioResource object.

        :param float duration: The total seconds of audio in the audio resource.
        :param str name: The name of the audio resource.
        :param AudioDetails details: An `AudioDetails` object that provides detailed information about the audio resource. The object is empty until the service finishes processing the audio.
        :param str status: The status of the audio resource: * `ok` indicates that the service has successfully analyzed the audio data. The data can be used to train the custom model. * `being_processed` indicates that the service is still analyzing the audio data. The service cannot accept requests to add new audio resources or to train the custom model until its analysis is complete. * `invalid` indicates that the audio data is not valid for training the custom model (possibly because it has the wrong format or sampling rate, or because it is corrupted). For an archive file, the entire archive is invalid if any of its audio files are invalid.
        """
        self.duration = duration
        self.name = name
        self.details = details
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioResource object from a json dictionary."""
        args = {}
        if 'duration' in _dict:
            args['duration'] = _dict.get('duration')
        else:
            raise ValueError(
                'Required property \'duration\' not present in AudioResource JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in AudioResource JSON')
        if 'details' in _dict:
            args['details'] = AudioDetails._from_dict(_dict.get('details'))
        else:
            raise ValueError(
                'Required property \'details\' not present in AudioResource JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in AudioResource JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'duration') and self.duration is not None:
            _dict['duration'] = self.duration
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'details') and self.details is not None:
            _dict['details'] = self.details._to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def __str__(self):
        """Return a `str` version of this AudioResource object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioResources(object):
    """
    AudioResources.

    :attr float total_minutes_of_audio: The total minutes of accumulated audio summed over all of the valid audio resources for the custom acoustic model. You can use this value to determine whether the custom model has too little or too much audio to begin training.
    :attr list[AudioResource] audio: An array of `AudioResource` objects that provides information about the audio resources of the custom acoustic model. The array is empty if the custom model has no audio resources.
    """

    def __init__(self, total_minutes_of_audio, audio):
        """
        Initialize a AudioResources object.

        :param float total_minutes_of_audio: The total minutes of accumulated audio summed over all of the valid audio resources for the custom acoustic model. You can use this value to determine whether the custom model has too little or too much audio to begin training.
        :param list[AudioResource] audio: An array of `AudioResource` objects that provides information about the audio resources of the custom acoustic model. The array is empty if the custom model has no audio resources.
        """
        self.total_minutes_of_audio = total_minutes_of_audio
        self.audio = audio

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioResources object from a json dictionary."""
        args = {}
        if 'total_minutes_of_audio' in _dict:
            args['total_minutes_of_audio'] = _dict.get(
                'total_minutes_of_audio')
        else:
            raise ValueError(
                'Required property \'total_minutes_of_audio\' not present in AudioResources JSON'
            )
        if 'audio' in _dict:
            args['audio'] = [
                AudioResource._from_dict(x) for x in (_dict.get('audio'))
            ]
        else:
            raise ValueError(
                'Required property \'audio\' not present in AudioResources JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_minutes_of_audio') and self.total_minutes_of_audio is not None:
            _dict['total_minutes_of_audio'] = self.total_minutes_of_audio
        if hasattr(self, 'audio') and self.audio is not None:
            _dict['audio'] = [x._to_dict() for x in self.audio]
        return _dict

    def __str__(self):
        """Return a `str` version of this AudioResources object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Corpora(object):
    """
    Corpora.

    :attr list[Corpus] corpora: Information about corpora of the custom model. The array is empty if the custom model has no corpora.
    """

    def __init__(self, corpora):
        """
        Initialize a Corpora object.

        :param list[Corpus] corpora: Information about corpora of the custom model. The array is empty if the custom model has no corpora.
        """
        self.corpora = corpora

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Corpora object from a json dictionary."""
        args = {}
        if 'corpora' in _dict:
            args['corpora'] = [
                Corpus._from_dict(x) for x in (_dict.get('corpora'))
            ]
        else:
            raise ValueError(
                'Required property \'corpora\' not present in Corpora JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'corpora') and self.corpora is not None:
            _dict['corpora'] = [x._to_dict() for x in self.corpora]
        return _dict

    def __str__(self):
        """Return a `str` version of this Corpora object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Corpus(object):
    """
    Corpus.

    :attr str name: The name of the corpus.
    :attr int total_words: The total number of words in the corpus. The value is `0` while the corpus is being processed.
    :attr int out_of_vocabulary_words: The number of OOV words in the corpus. The value is `0` while the corpus is being processed.
    :attr str status: The status of the corpus: * `analyzed` indicates that the service has successfully analyzed the corpus; the custom model can be trained with data from the corpus. * `being_processed` indicates that the service is still analyzing the corpus; the service cannot accept requests to add new corpora or words, or to train the custom model. * `undetermined` indicates that the service encountered an error while processing the corpus.
    :attr str error: (optional) If the status of the corpus is `undetermined`, the following message: `Analysis of corpus 'name' failed. Please try adding the corpus again by setting the 'allow_overwrite' flag to 'true'`.
    """

    def __init__(self,
                 name,
                 total_words,
                 out_of_vocabulary_words,
                 status,
                 error=None):
        """
        Initialize a Corpus object.

        :param str name: The name of the corpus.
        :param int total_words: The total number of words in the corpus. The value is `0` while the corpus is being processed.
        :param int out_of_vocabulary_words: The number of OOV words in the corpus. The value is `0` while the corpus is being processed.
        :param str status: The status of the corpus: * `analyzed` indicates that the service has successfully analyzed the corpus; the custom model can be trained with data from the corpus. * `being_processed` indicates that the service is still analyzing the corpus; the service cannot accept requests to add new corpora or words, or to train the custom model. * `undetermined` indicates that the service encountered an error while processing the corpus.
        :param str error: (optional) If the status of the corpus is `undetermined`, the following message: `Analysis of corpus 'name' failed. Please try adding the corpus again by setting the 'allow_overwrite' flag to 'true'`.
        """
        self.name = name
        self.total_words = total_words
        self.out_of_vocabulary_words = out_of_vocabulary_words
        self.status = status
        self.error = error

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Corpus object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Corpus JSON')
        if 'total_words' in _dict:
            args['total_words'] = _dict.get('total_words')
        else:
            raise ValueError(
                'Required property \'total_words\' not present in Corpus JSON')
        if 'out_of_vocabulary_words' in _dict:
            args['out_of_vocabulary_words'] = _dict.get(
                'out_of_vocabulary_words')
        else:
            raise ValueError(
                'Required property \'out_of_vocabulary_words\' not present in Corpus JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in Corpus JSON')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'total_words') and self.total_words is not None:
            _dict['total_words'] = self.total_words
        if hasattr(self, 'out_of_vocabulary_words') and self.out_of_vocabulary_words is not None:
            _dict['out_of_vocabulary_words'] = self.out_of_vocabulary_words
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        return _dict

    def __str__(self):
        """Return a `str` version of this Corpus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CustomWord(object):
    """
    CustomWord.

    :attr str word: (optional) **When specifying an array of one or more words,** you must specify the custom word that is to be added to or updated in the custom model. Do not include spaces in the word. Use a - (dash) or _ (underscore) to connect the tokens of compound words. **When adding or updating a single word directly,** omit this field.
    :attr list[str] sounds_like: (optional) An array of sounds-like pronunciations for the custom word. Specify how words that are difficult to pronounce, foreign words, acronyms, and so on can be pronounced by users. For a word that is not in the service's base vocabulary, omit the parameter to have the service automatically generate a sounds-like pronunciation for the word. For a word that is in the service's base vocabulary, use the parameter to specify additional pronunciations for the word. You cannot override the default pronunciation of a word; pronunciations you add augment the pronunciation from the base vocabulary. A word can have at most five sounds-like pronunciations, and a pronunciation can include at most 40 characters not including spaces.
    :attr str display_as: (optional) An alternative spelling for the custom word when it appears in a transcript. Use the parameter when you want the word to have a spelling that is different from its usual representation or from its spelling in corpora training data.
    """

    def __init__(self, word=None, sounds_like=None, display_as=None):
        """
        Initialize a CustomWord object.

        :param str word: (optional) **When specifying an array of one or more words,** you must specify the custom word that is to be added to or updated in the custom model. Do not include spaces in the word. Use a - (dash) or _ (underscore) to connect the tokens of compound words. **When adding or updating a single word directly,** omit this field.
        :param list[str] sounds_like: (optional) An array of sounds-like pronunciations for the custom word. Specify how words that are difficult to pronounce, foreign words, acronyms, and so on can be pronounced by users. For a word that is not in the service's base vocabulary, omit the parameter to have the service automatically generate a sounds-like pronunciation for the word. For a word that is in the service's base vocabulary, use the parameter to specify additional pronunciations for the word. You cannot override the default pronunciation of a word; pronunciations you add augment the pronunciation from the base vocabulary. A word can have at most five sounds-like pronunciations, and a pronunciation can include at most 40 characters not including spaces.
        :param str display_as: (optional) An alternative spelling for the custom word when it appears in a transcript. Use the parameter when you want the word to have a spelling that is different from its usual representation or from its spelling in corpora training data.
        """
        self.word = word
        self.sounds_like = sounds_like
        self.display_as = display_as

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomWord object from a json dictionary."""
        args = {}
        if 'word' in _dict:
            args['word'] = _dict.get('word')
        if 'sounds_like' in _dict:
            args['sounds_like'] = _dict.get('sounds_like')
        if 'display_as' in _dict:
            args['display_as'] = _dict.get('display_as')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word
        if hasattr(self, 'sounds_like') and self.sounds_like is not None:
            _dict['sounds_like'] = self.sounds_like
        if hasattr(self, 'display_as') and self.display_as is not None:
            _dict['display_as'] = self.display_as
        return _dict

    def __str__(self):
        """Return a `str` version of this CustomWord object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordResult(object):
    """
    KeywordResult.

    :attr str normalized_text: A specified keyword normalized to the spoken phrase that matched in the audio input.
    :attr float start_time: The start time in seconds of the keyword match.
    :attr float end_time: The end time in seconds of the keyword match.
    :attr float confidence: A confidence score for the keyword match in the range of 0 to 1.
    """

    def __init__(self, normalized_text, start_time, end_time, confidence):
        """
        Initialize a KeywordResult object.

        :param str normalized_text: A specified keyword normalized to the spoken phrase that matched in the audio input.
        :param float start_time: The start time in seconds of the keyword match.
        :param float end_time: The end time in seconds of the keyword match.
        :param float confidence: A confidence score for the keyword match in the range of 0 to 1.
        """
        self.normalized_text = normalized_text
        self.start_time = start_time
        self.end_time = end_time
        self.confidence = confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordResult object from a json dictionary."""
        args = {}
        if 'normalized_text' in _dict:
            args['normalized_text'] = _dict.get('normalized_text')
        else:
            raise ValueError(
                'Required property \'normalized_text\' not present in KeywordResult JSON'
            )
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        else:
            raise ValueError(
                'Required property \'start_time\' not present in KeywordResult JSON'
            )
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        else:
            raise ValueError(
                'Required property \'end_time\' not present in KeywordResult JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        else:
            raise ValueError(
                'Required property \'confidence\' not present in KeywordResult JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'normalized_text') and self.normalized_text is not None:
            _dict['normalized_text'] = self.normalized_text
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def __str__(self):
        """Return a `str` version of this KeywordResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LanguageModel(object):
    """
    LanguageModel.

    :attr str customization_id: The customization ID (GUID) of the custom language model. **Note:** When you create a new custom language model, the service returns only the GUID of the new model; it does not return the other fields of this object.
    :attr str created: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom language model was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str language: (optional) The language identifier of the custom language model (for example, `en-US`).
    :attr str dialect: (optional) The dialect of the language for the custom language model. By default, the dialect matches the language of the base model; for example, `en-US` for either of the US English language models. For Spanish models, the field indicates the dialect for which the model was created: * `es-ES` for Castilian Spanish (the default) * `es-LA` for Latin American Spanish * `es-US` for North American (Mexican) Spanish.
    :attr list[str] versions: (optional) A list of the available versions of the custom language model. Each element of the array indicates a version of the base model with which the custom model can be used. Multiple versions exist only if the custom model has been upgraded; otherwise, only a single version is shown.
    :attr str owner: (optional) The GUID of the service credentials for the instance of the service that owns the custom language model.
    :attr str name: (optional) The name of the custom language model.
    :attr str description: (optional) The description of the custom language model.
    :attr str base_model_name: (optional) The name of the language model for which the custom language model was created.
    :attr str status: (optional) The current status of the custom language model: * `pending` indicates that the model was created but is waiting either for training data to be added or for the service to finish analyzing added data. * `ready` indicates that the model contains data and is ready to be trained. * `training` indicates that the model is currently being trained. * `available` indicates that the model is trained and ready to use. * `upgrading` indicates that the model is currently being upgraded. * `failed` indicates that training of the model failed.
    :attr int progress: (optional) A percentage that indicates the progress of the custom language model's current training. A value of `100` means that the model is fully trained. **Note:** The `progress` field does not currently reflect the progress of the training; the field changes from `0` to `100` when training is complete.
    :attr str warnings: (optional) If the request included unknown parameters, the following message: `Unexpected query parameter(s) ['parameters'] detected`, where `parameters` is a list that includes a quoted string for each unknown parameter.
    """

    def __init__(self,
                 customization_id,
                 created=None,
                 language=None,
                 dialect=None,
                 versions=None,
                 owner=None,
                 name=None,
                 description=None,
                 base_model_name=None,
                 status=None,
                 progress=None,
                 warnings=None):
        """
        Initialize a LanguageModel object.

        :param str customization_id: The customization ID (GUID) of the custom language model. **Note:** When you create a new custom language model, the service returns only the GUID of the new model; it does not return the other fields of this object.
        :param str created: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom language model was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str language: (optional) The language identifier of the custom language model (for example, `en-US`).
        :param str dialect: (optional) The dialect of the language for the custom language model. By default, the dialect matches the language of the base model; for example, `en-US` for either of the US English language models. For Spanish models, the field indicates the dialect for which the model was created: * `es-ES` for Castilian Spanish (the default) * `es-LA` for Latin American Spanish * `es-US` for North American (Mexican) Spanish.
        :param list[str] versions: (optional) A list of the available versions of the custom language model. Each element of the array indicates a version of the base model with which the custom model can be used. Multiple versions exist only if the custom model has been upgraded; otherwise, only a single version is shown.
        :param str owner: (optional) The GUID of the service credentials for the instance of the service that owns the custom language model.
        :param str name: (optional) The name of the custom language model.
        :param str description: (optional) The description of the custom language model.
        :param str base_model_name: (optional) The name of the language model for which the custom language model was created.
        :param str status: (optional) The current status of the custom language model: * `pending` indicates that the model was created but is waiting either for training data to be added or for the service to finish analyzing added data. * `ready` indicates that the model contains data and is ready to be trained. * `training` indicates that the model is currently being trained. * `available` indicates that the model is trained and ready to use. * `upgrading` indicates that the model is currently being upgraded. * `failed` indicates that training of the model failed.
        :param int progress: (optional) A percentage that indicates the progress of the custom language model's current training. A value of `100` means that the model is fully trained. **Note:** The `progress` field does not currently reflect the progress of the training; the field changes from `0` to `100` when training is complete.
        :param str warnings: (optional) If the request included unknown parameters, the following message: `Unexpected query parameter(s) ['parameters'] detected`, where `parameters` is a list that includes a quoted string for each unknown parameter.
        """
        self.customization_id = customization_id
        self.created = created
        self.language = language
        self.dialect = dialect
        self.versions = versions
        self.owner = owner
        self.name = name
        self.description = description
        self.base_model_name = base_model_name
        self.status = status
        self.progress = progress
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LanguageModel object from a json dictionary."""
        args = {}
        if 'customization_id' in _dict:
            args['customization_id'] = _dict.get('customization_id')
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in LanguageModel JSON'
            )
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'dialect' in _dict:
            args['dialect'] = _dict.get('dialect')
        if 'versions' in _dict:
            args['versions'] = _dict.get('versions')
        if 'owner' in _dict:
            args['owner'] = _dict.get('owner')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'base_model_name' in _dict:
            args['base_model_name'] = _dict.get('base_model_name')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'progress' in _dict:
            args['progress'] = _dict.get('progress')
        if 'warnings' in _dict:
            args['warnings'] = _dict.get('warnings')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'customization_id') and self.customization_id is not None:
            _dict['customization_id'] = self.customization_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'dialect') and self.dialect is not None:
            _dict['dialect'] = self.dialect
        if hasattr(self, 'versions') and self.versions is not None:
            _dict['versions'] = self.versions
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self,
                   'base_model_name') and self.base_model_name is not None:
            _dict['base_model_name'] = self.base_model_name
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'progress') and self.progress is not None:
            _dict['progress'] = self.progress
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = self.warnings
        return _dict

    def __str__(self):
        """Return a `str` version of this LanguageModel object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LanguageModels(object):
    """
    LanguageModels.

    :attr list[LanguageModel] customizations: An array of objects that provides information about each available custom language model. The array is empty if the requesting service credentials own no custom language models (if no language is specified) or own no custom language models for the specified language.
    """

    def __init__(self, customizations):
        """
        Initialize a LanguageModels object.

        :param list[LanguageModel] customizations: An array of objects that provides information about each available custom language model. The array is empty if the requesting service credentials own no custom language models (if no language is specified) or own no custom language models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LanguageModels object from a json dictionary."""
        args = {}
        if 'customizations' in _dict:
            args['customizations'] = [
                LanguageModel._from_dict(x)
                for x in (_dict.get('customizations'))
            ]
        else:
            raise ValueError(
                'Required property \'customizations\' not present in LanguageModels JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'customizations') and self.customizations is not None:
            _dict['customizations'] = [
                x._to_dict() for x in self.customizations
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this LanguageModels object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RecognitionJob(object):
    """
    RecognitionJob.

    :attr str id: The ID of the job.
    :attr str status: The current status of the job: * `waiting`: The service is preparing the job for processing. The service returns this status when the job is initially created or when it is waiting for capacity to process the job. The job remains in this state until the service has the capacity to begin processing it. * `processing`: The service is actively processing the job. * `completed`: The service has finished processing the job. If the job specified a callback URL and the event `recognitions.completed_with_results`, the service sent the results with the callback notification; otherwise, you must retrieve the results by checking the individual job. * `failed`: The job failed.
    :attr str created: The date and time in Coordinated Universal Time (UTC) at which the job was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str updated: (optional) The date and time in Coordinated Universal Time (UTC) at which the job was last updated by the service. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`). **Note:** This field is returned only when you list information about a specific or all existing jobs.
    :attr str url: (optional) The URL to use to request information about the job with the **Check a job** method. **Note:** This field is returned only when you create a new job.
    :attr str user_token: (optional) The user token associated with a job that was created with a callback URL and a user token. **Note:** This field can be returned only when you list information about all existing jobs.
    :attr list[SpeechRecognitionResults] results: (optional) If the status is `completed`, the results of the recognition request as an array that includes a single instance of a `SpeechRecognitionResults` object. **Note:** This field can be returned only when you list information about a specific existing job.
    :attr list[str] warnings: (optional) An array of warning messages about invalid parameters included with the request. Each warning includes a descriptive message and a list of invalid argument strings, for example, `"unexpected query parameter 'user_token', query parameter 'callback_url' was not specified"`. The request succeeds despite the warnings. **Note:** This field can be returned only when you create a new job.
    """

    def __init__(self,
                 id,
                 status,
                 created,
                 updated=None,
                 url=None,
                 user_token=None,
                 results=None,
                 warnings=None):
        """
        Initialize a RecognitionJob object.

        :param str id: The ID of the job.
        :param str status: The current status of the job: * `waiting`: The service is preparing the job for processing. The service returns this status when the job is initially created or when it is waiting for capacity to process the job. The job remains in this state until the service has the capacity to begin processing it. * `processing`: The service is actively processing the job. * `completed`: The service has finished processing the job. If the job specified a callback URL and the event `recognitions.completed_with_results`, the service sent the results with the callback notification; otherwise, you must retrieve the results by checking the individual job. * `failed`: The job failed.
        :param str created: The date and time in Coordinated Universal Time (UTC) at which the job was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str updated: (optional) The date and time in Coordinated Universal Time (UTC) at which the job was last updated by the service. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`). **Note:** This field is returned only when you list information about a specific or all existing jobs.
        :param str url: (optional) The URL to use to request information about the job with the **Check a job** method. **Note:** This field is returned only when you create a new job.
        :param str user_token: (optional) The user token associated with a job that was created with a callback URL and a user token. **Note:** This field can be returned only when you list information about all existing jobs.
        :param list[SpeechRecognitionResults] results: (optional) If the status is `completed`, the results of the recognition request as an array that includes a single instance of a `SpeechRecognitionResults` object. **Note:** This field can be returned only when you list information about a specific existing job.
        :param list[str] warnings: (optional) An array of warning messages about invalid parameters included with the request. Each warning includes a descriptive message and a list of invalid argument strings, for example, `"unexpected query parameter 'user_token', query parameter 'callback_url' was not specified"`. The request succeeds despite the warnings. **Note:** This field can be returned only when you create a new job.
        """
        self.id = id
        self.status = status
        self.created = created
        self.updated = updated
        self.url = url
        self.user_token = user_token
        self.results = results
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecognitionJob object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError(
                'Required property \'id\' not present in RecognitionJob JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in RecognitionJob JSON'
            )
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        else:
            raise ValueError(
                'Required property \'created\' not present in RecognitionJob JSON'
            )
        if 'updated' in _dict:
            args['updated'] = _dict.get('updated')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'user_token' in _dict:
            args['user_token'] = _dict.get('user_token')
        if 'results' in _dict:
            args['results'] = [
                SpeechRecognitionResults._from_dict(x)
                for x in (_dict.get('results'))
            ]
        if 'warnings' in _dict:
            args['warnings'] = _dict.get('warnings')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = self.updated
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'user_token') and self.user_token is not None:
            _dict['user_token'] = self.user_token
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = self.warnings
        return _dict

    def __str__(self):
        """Return a `str` version of this RecognitionJob object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RecognitionJobs(object):
    """
    RecognitionJobs.

    :attr list[RecognitionJob] recognitions: An array of objects that provides the status for each of the user's current jobs. The array is empty if the user has no current jobs.
    """

    def __init__(self, recognitions):
        """
        Initialize a RecognitionJobs object.

        :param list[RecognitionJob] recognitions: An array of objects that provides the status for each of the user's current jobs. The array is empty if the user has no current jobs.
        """
        self.recognitions = recognitions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecognitionJobs object from a json dictionary."""
        args = {}
        if 'recognitions' in _dict:
            args['recognitions'] = [
                RecognitionJob._from_dict(x)
                for x in (_dict.get('recognitions'))
            ]
        else:
            raise ValueError(
                'Required property \'recognitions\' not present in RecognitionJobs JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'recognitions') and self.recognitions is not None:
            _dict['recognitions'] = [x._to_dict() for x in self.recognitions]
        return _dict

    def __str__(self):
        """Return a `str` version of this RecognitionJobs object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RegisterStatus(object):
    """
    RegisterStatus.

    :attr str status: The current status of the job: * `created` if the callback URL was successfully white-listed as a result of the call. * `already created` if the URL was already white-listed.
    :attr str url: The callback URL that is successfully registered.
    """

    def __init__(self, status, url):
        """
        Initialize a RegisterStatus object.

        :param str status: The current status of the job: * `created` if the callback URL was successfully white-listed as a result of the call. * `already created` if the URL was already white-listed.
        :param str url: The callback URL that is successfully registered.
        """
        self.status = status
        self.url = url

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RegisterStatus object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in RegisterStatus JSON'
            )
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in RegisterStatus JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def __str__(self):
        """Return a `str` version of this RegisterStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeakerLabelsResult(object):
    """
    SpeakerLabelsResult.

    :attr float _from: The start time of a word from the transcript. The value matches the start time of a word from the `timestamps` array.
    :attr float to: The end time of a word from the transcript. The value matches the end time of a word from the `timestamps` array.
    :attr int speaker: The numeric identifier that the service assigns to a speaker from the audio. Speaker IDs begin at `0` initially but can evolve and change across interim results (if supported by the method) and between interim and final results as the service processes the audio. They are not guaranteed to be sequential, contiguous, or ordered.
    :attr float confidence: A score that indicates the service's confidence in its identification of the speaker in the range of 0 to 1.
    :attr bool final_results: An indication of whether the service might further change word and speaker-label results. A value of `true` means that the service guarantees not to send any further updates for the current or any preceding results; `false` means that the service might send further updates to the results.
    """

    def __init__(self, _from, to, speaker, confidence, final_results):
        """
        Initialize a SpeakerLabelsResult object.

        :param float _from: The start time of a word from the transcript. The value matches the start time of a word from the `timestamps` array.
        :param float to: The end time of a word from the transcript. The value matches the end time of a word from the `timestamps` array.
        :param int speaker: The numeric identifier that the service assigns to a speaker from the audio. Speaker IDs begin at `0` initially but can evolve and change across interim results (if supported by the method) and between interim and final results as the service processes the audio. They are not guaranteed to be sequential, contiguous, or ordered.
        :param float confidence: A score that indicates the service's confidence in its identification of the speaker in the range of 0 to 1.
        :param bool final_results: An indication of whether the service might further change word and speaker-label results. A value of `true` means that the service guarantees not to send any further updates for the current or any preceding results; `false` means that the service might send further updates to the results.
        """
        self._from = _from
        self.to = to
        self.speaker = speaker
        self.confidence = confidence
        self.final_results = final_results

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeakerLabelsResult object from a json dictionary."""
        args = {}
        if 'from' in _dict:
            args['_from'] = _dict.get('from')
        else:
            raise ValueError(
                'Required property \'from\' not present in SpeakerLabelsResult JSON'
            )
        if 'to' in _dict:
            args['to'] = _dict.get('to')
        else:
            raise ValueError(
                'Required property \'to\' not present in SpeakerLabelsResult JSON'
            )
        if 'speaker' in _dict:
            args['speaker'] = _dict.get('speaker')
        else:
            raise ValueError(
                'Required property \'speaker\' not present in SpeakerLabelsResult JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        else:
            raise ValueError(
                'Required property \'confidence\' not present in SpeakerLabelsResult JSON'
            )
        if 'final' in _dict or 'final_results' in _dict:
            args['final_results'] = _dict.get('final') or _dict.get('final_results')
        else:
            raise ValueError(
                'Required property \'final\' not present in SpeakerLabelsResult JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_from') and self._from is not None:
            _dict['from'] = self._from
        if hasattr(self, 'to') and self.to is not None:
            _dict['to'] = self.to
        if hasattr(self, 'speaker') and self.speaker is not None:
            _dict['speaker'] = self.speaker
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'final_results') and self.final_results is not None:
            _dict['final'] = self.final_results
        return _dict

    def __str__(self):
        """Return a `str` version of this SpeakerLabelsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechModel(object):
    """
    SpeechModel.

    :attr str name: The name of the model for use as an identifier in calls to the service (for example, `en-US_BroadbandModel`).
    :attr str language: The language identifier for the model (for example, `en-US`).
    :attr int rate: The sampling rate (minimum acceptable rate for audio) used by the model in Hertz.
    :attr str url: The URI for the model.
    :attr SupportedFeatures supported_features: Describes the additional service features supported with the model.
    :attr str description: Brief description of the model.
    :attr str sessions: (optional) The URI for the model for use with the **Create a session** method. (Returned only for requests for a single model with the **Get a model** method.).
    """

    def __init__(self,
                 name,
                 language,
                 rate,
                 url,
                 supported_features,
                 description,
                 sessions=None):
        """
        Initialize a SpeechModel object.

        :param str name: The name of the model for use as an identifier in calls to the service (for example, `en-US_BroadbandModel`).
        :param str language: The language identifier for the model (for example, `en-US`).
        :param int rate: The sampling rate (minimum acceptable rate for audio) used by the model in Hertz.
        :param str url: The URI for the model.
        :param SupportedFeatures supported_features: Describes the additional service features supported with the model.
        :param str description: Brief description of the model.
        :param str sessions: (optional) The URI for the model for use with the **Create a session** method. (Returned only for requests for a single model with the **Get a model** method.).
        """
        self.name = name
        self.language = language
        self.rate = rate
        self.url = url
        self.supported_features = supported_features
        self.description = description
        self.sessions = sessions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechModel object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in SpeechModel JSON')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in SpeechModel JSON'
            )
        if 'rate' in _dict:
            args['rate'] = _dict.get('rate')
        else:
            raise ValueError(
                'Required property \'rate\' not present in SpeechModel JSON')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in SpeechModel JSON')
        if 'supported_features' in _dict:
            args['supported_features'] = SupportedFeatures._from_dict(
                _dict.get('supported_features'))
        else:
            raise ValueError(
                'Required property \'supported_features\' not present in SpeechModel JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError(
                'Required property \'description\' not present in SpeechModel JSON'
            )
        if 'sessions' in _dict:
            args['sessions'] = _dict.get('sessions')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'rate') and self.rate is not None:
            _dict['rate'] = self.rate
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(
                self,
                'supported_features') and self.supported_features is not None:
            _dict['supported_features'] = self.supported_features._to_dict()
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'sessions') and self.sessions is not None:
            _dict['sessions'] = self.sessions
        return _dict

    def __str__(self):
        """Return a `str` version of this SpeechModel object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechModels(object):
    """
    SpeechModels.

    :attr list[SpeechModel] models: Information about each available model.
    """

    def __init__(self, models):
        """
        Initialize a SpeechModels object.

        :param list[SpeechModel] models: Information about each available model.
        """
        self.models = models

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechModels object from a json dictionary."""
        args = {}
        if 'models' in _dict:
            args['models'] = [
                SpeechModel._from_dict(x) for x in (_dict.get('models'))
            ]
        else:
            raise ValueError(
                'Required property \'models\' not present in SpeechModels JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            _dict['models'] = [x._to_dict() for x in self.models]
        return _dict

    def __str__(self):
        """Return a `str` version of this SpeechModels object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechRecognitionAlternative(object):
    """
    SpeechRecognitionAlternative.

    :attr str transcript: A transcription of the audio.
    :attr float confidence: (optional) A score that indicates the service's confidence in the transcript in the range of 0 to 1. Available only for the best alternative and only in results marked as final.
    :attr list[str] timestamps: (optional) Time alignments for each word from the transcript as a list of lists. Each inner list consists of three elements: the word followed by its start and end time in seconds. Example: `[["hello",0.0,1.2],["world",1.2,2.5]]`. Available only for the best alternative.
    :attr list[str] word_confidence: (optional) A confidence score for each word of the transcript as a list of lists. Each inner list consists of two elements: the word and its confidence score in the range of 0 to 1. Example: `[["hello",0.95],["world",0.866]]`. Available only for the best alternative and only in results marked as final.
    """

    def __init__(self,
                 transcript,
                 confidence=None,
                 timestamps=None,
                 word_confidence=None):
        """
        Initialize a SpeechRecognitionAlternative object.

        :param str transcript: A transcription of the audio.
        :param float confidence: (optional) A score that indicates the service's confidence in the transcript in the range of 0 to 1. Available only for the best alternative and only in results marked as final.
        :param list[str] timestamps: (optional) Time alignments for each word from the transcript as a list of lists. Each inner list consists of three elements: the word followed by its start and end time in seconds. Example: `[["hello",0.0,1.2],["world",1.2,2.5]]`. Available only for the best alternative.
        :param list[str] word_confidence: (optional) A confidence score for each word of the transcript as a list of lists. Each inner list consists of two elements: the word and its confidence score in the range of 0 to 1. Example: `[["hello",0.95],["world",0.866]]`. Available only for the best alternative and only in results marked as final.
        """
        self.transcript = transcript
        self.confidence = confidence
        self.timestamps = timestamps
        self.word_confidence = word_confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionAlternative object from a json dictionary."""
        args = {}
        if 'transcript' in _dict:
            args['transcript'] = _dict.get('transcript')
        else:
            raise ValueError(
                'Required property \'transcript\' not present in SpeechRecognitionAlternative JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'timestamps' in _dict:
            args['timestamps'] = _dict.get('timestamps')
        if 'word_confidence' in _dict:
            args['word_confidence'] = _dict.get('word_confidence')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'transcript') and self.transcript is not None:
            _dict['transcript'] = self.transcript
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'timestamps') and self.timestamps is not None:
            _dict['timestamps'] = self.timestamps
        if hasattr(self,
                   'word_confidence') and self.word_confidence is not None:
            _dict['word_confidence'] = self.word_confidence
        return _dict

    def __str__(self):
        """Return a `str` version of this SpeechRecognitionAlternative object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechRecognitionResult(object):
    """
    SpeechRecognitionResult.

    :attr bool final_results: An indication of whether the transcription results are final. If `true`, the results for this utterance are not updated further; no additional results are sent for a `result_index` once its results are indicated as final.
    :attr list[SpeechRecognitionAlternative] alternatives: An array of alternative transcripts. The `alternatives` array can include additional requested output such as word confidence or timestamps.
    :attr dict keywords_result: (optional) A dictionary (or associative array) whose keys are the strings specified for `keywords` if both that parameter and `keywords_threshold` are specified. A keyword for which no matches are found is omitted from the array. You can spot a maximum of 1000 keywords. The array is omitted if no keywords are found.
    :attr list[WordAlternativeResults] word_alternatives: (optional) An array of alternative hypotheses found for words of the input audio if a `word_alternatives_threshold` is specified.
    """

    def __init__(self,
                 final_results,
                 alternatives,
                 keywords_result=None,
                 word_alternatives=None):
        """
        Initialize a SpeechRecognitionResult object.

        :param bool final_results: An indication of whether the transcription results are final. If `true`, the results for this utterance are not updated further; no additional results are sent for a `result_index` once its results are indicated as final.
        :param list[SpeechRecognitionAlternative] alternatives: An array of alternative transcripts. The `alternatives` array can include additional requested output such as word confidence or timestamps.
        :param dict keywords_result: (optional) A dictionary (or associative array) whose keys are the strings specified for `keywords` if both that parameter and `keywords_threshold` are specified. A keyword for which no matches are found is omitted from the array. You can spot a maximum of 1000 keywords. The array is omitted if no keywords are found.
        :param list[WordAlternativeResults] word_alternatives: (optional) An array of alternative hypotheses found for words of the input audio if a `word_alternatives_threshold` is specified.
        """
        self.final_results = final_results
        self.alternatives = alternatives
        self.keywords_result = keywords_result
        self.word_alternatives = word_alternatives

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionResult object from a json dictionary."""
        args = {}
        if 'final' in _dict or 'final_results' in _dict:
            args['final_results'] = _dict.get('final') or _dict.get(
                'final_results')
        else:
            raise ValueError(
                'Required property \'final\' not present in SpeechRecognitionResult JSON'
            )
        if 'alternatives' in _dict:
            args['alternatives'] = [
                SpeechRecognitionAlternative._from_dict(x)
                for x in (_dict.get('alternatives'))
            ]
        else:
            raise ValueError(
                'Required property \'alternatives\' not present in SpeechRecognitionResult JSON'
            )
        if 'keywords_result' in _dict:
            args['keywords_result'] = _dict.get('keywords_result')
        if 'word_alternatives' in _dict:
            args['word_alternatives'] = [
                WordAlternativeResults._from_dict(x)
                for x in (_dict.get('word_alternatives'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'final_results') and self.final_results is not None:
            _dict['final'] = self.final_results
        if hasattr(self, 'alternatives') and self.alternatives is not None:
            _dict['alternatives'] = [x._to_dict() for x in self.alternatives]
        if hasattr(self,
                   'keywords_result') and self.keywords_result is not None:
            _dict['keywords_result'] = self.keywords_result
        if hasattr(self,
                   'word_alternatives') and self.word_alternatives is not None:
            _dict['word_alternatives'] = [
                x._to_dict() for x in self.word_alternatives
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this SpeechRecognitionResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechRecognitionResults(object):
    """
    SpeechRecognitionResults.

    :attr list[SpeechRecognitionResult] results: (optional) An array that can include interim and final results (interim results are returned only if supported by the method). Final results are guaranteed not to change; interim results might be replaced by further interim results and final results. The service periodically sends updates to the results list; the `result_index` is set to the lowest index in the array that has changed; it is incremented for new results.
    :attr int result_index: (optional) An index that indicates a change point in the `results` array. The service increments the index only for additional results that it sends for new audio for the same request.
    :attr list[SpeakerLabelsResult] speaker_labels: (optional) An array that identifies which words were spoken by which speakers in a multi-person exchange. Returned in the response only if `speaker_labels` is `true`. When interim results are also requested for methods that support them, it is possible for a `SpeechRecognitionResults` object to include only the `speaker_labels` field.
    :attr list[str] warnings: (optional) An array of warning messages associated with the request: * Warnings for invalid parameters or JSON fields can include a descriptive message and a list of invalid argument strings, for example, `"Unknown arguments:"` or `"Unknown url query arguments:"` followed by a list of the form `"invalid_arg_1, invalid_arg_2."` * The following warning is returned if the request passes a custom model that is based on an older version of a base model for which an updated version is available: `"Using previous version of base model, because your custom model has been built with it. Please note that this version will be supported only for a limited time. Consider updating your custom model to the new base model. If you do not do that you will be automatically switched to base model when you used the non-updated custom model."`  In both cases, the request succeeds despite the warnings.
    """

    def __init__(self,
                 results=None,
                 result_index=None,
                 speaker_labels=None,
                 warnings=None):
        """
        Initialize a SpeechRecognitionResults object.

        :param list[SpeechRecognitionResult] results: (optional) An array that can include interim and final results (interim results are returned only if supported by the method). Final results are guaranteed not to change; interim results might be replaced by further interim results and final results. The service periodically sends updates to the results list; the `result_index` is set to the lowest index in the array that has changed; it is incremented for new results.
        :param int result_index: (optional) An index that indicates a change point in the `results` array. The service increments the index only for additional results that it sends for new audio for the same request.
        :param list[SpeakerLabelsResult] speaker_labels: (optional) An array that identifies which words were spoken by which speakers in a multi-person exchange. Returned in the response only if `speaker_labels` is `true`. When interim results are also requested for methods that support them, it is possible for a `SpeechRecognitionResults` object to include only the `speaker_labels` field.
        :param list[str] warnings: (optional) An array of warning messages associated with the request: * Warnings for invalid parameters or JSON fields can include a descriptive message and a list of invalid argument strings, for example, `"Unknown arguments:"` or `"Unknown url query arguments:"` followed by a list of the form `"invalid_arg_1, invalid_arg_2."` * The following warning is returned if the request passes a custom model that is based on an older version of a base model for which an updated version is available: `"Using previous version of base model, because your custom model has been built with it. Please note that this version will be supported only for a limited time. Consider updating your custom model to the new base model. If you do not do that you will be automatically switched to base model when you used the non-updated custom model."`  In both cases, the request succeeds despite the warnings.
        """
        self.results = results
        self.result_index = result_index
        self.speaker_labels = speaker_labels
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionResults object from a json dictionary."""
        args = {}
        if 'results' in _dict:
            args['results'] = [
                SpeechRecognitionResult._from_dict(x)
                for x in (_dict.get('results'))
            ]
        if 'result_index' in _dict:
            args['result_index'] = _dict.get('result_index')
        if 'speaker_labels' in _dict:
            args['speaker_labels'] = [
                SpeakerLabelsResult._from_dict(x)
                for x in (_dict.get('speaker_labels'))
            ]
        if 'warnings' in _dict:
            args['warnings'] = _dict.get('warnings')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            _dict['results'] = [x._to_dict() for x in self.results]
        if hasattr(self, 'result_index') and self.result_index is not None:
            _dict['result_index'] = self.result_index
        if hasattr(self, 'speaker_labels') and self.speaker_labels is not None:
            _dict['speaker_labels'] = [
                x._to_dict() for x in self.speaker_labels
            ]
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = self.warnings
        return _dict

    def __str__(self):
        """Return a `str` version of this SpeechRecognitionResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SupportedFeatures(object):
    """
    SupportedFeatures.

    :attr bool custom_language_model: Indicates whether the customization interface can be used to create a custom language model based on the language model.
    :attr bool speaker_labels: Indicates whether the **speaker_labels** parameter can be used with the language model.
    """

    def __init__(self, custom_language_model, speaker_labels):
        """
        Initialize a SupportedFeatures object.

        :param bool custom_language_model: Indicates whether the customization interface can be used to create a custom language model based on the language model.
        :param bool speaker_labels: Indicates whether the **speaker_labels** parameter can be used with the language model.
        """
        self.custom_language_model = custom_language_model
        self.speaker_labels = speaker_labels

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SupportedFeatures object from a json dictionary."""
        args = {}
        if 'custom_language_model' in _dict:
            args['custom_language_model'] = _dict.get('custom_language_model')
        else:
            raise ValueError(
                'Required property \'custom_language_model\' not present in SupportedFeatures JSON'
            )
        if 'speaker_labels' in _dict:
            args['speaker_labels'] = _dict.get('speaker_labels')
        else:
            raise ValueError(
                'Required property \'speaker_labels\' not present in SupportedFeatures JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_language_model') and self.custom_language_model is not None:
            _dict['custom_language_model'] = self.custom_language_model
        if hasattr(self, 'speaker_labels') and self.speaker_labels is not None:
            _dict['speaker_labels'] = self.speaker_labels
        return _dict

    def __str__(self):
        """Return a `str` version of this SupportedFeatures object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Word(object):
    """
    Word.

    :attr str word: A word from the custom model's words resource. The spelling of the word is used to train the model.
    :attr list[str] sounds_like: An array of pronunciations for the word. The array can include the sounds-like pronunciation automatically generated by the service if none is provided for the word; the service adds this pronunciation when it finishes processing the word.
    :attr str display_as: The spelling of the word that the service uses to display the word in a transcript. The field contains an empty string if no display-as value is provided for the word, in which case the word is displayed as it is spelled.
    :attr int count: A sum of the number of times the word is found across all corpora. For example, if the word occurs five times in one corpus and seven times in another, its count is `12`. If you add a custom word to a model before it is added by any corpora, the count begins at `1`; if the word is added from a corpus first and later modified, the count reflects only the number of times it is found in corpora.
    :attr list[str] source: An array of sources that describes how the word was added to the custom model's words resource. For OOV words added from a corpus, includes the name of the corpus; if the word was added by multiple corpora, the names of all corpora are listed. If the word was modified or added by the user directly, the field includes the string `user`.
    :attr list[WordError] error: (optional) If the service discovered one or more problems that you need to correct for the word's definition, an array that describes each of the errors.
    """

    def __init__(self,
                 word,
                 sounds_like,
                 display_as,
                 count,
                 source,
                 error=None):
        """
        Initialize a Word object.

        :param str word: A word from the custom model's words resource. The spelling of the word is used to train the model.
        :param list[str] sounds_like: An array of pronunciations for the word. The array can include the sounds-like pronunciation automatically generated by the service if none is provided for the word; the service adds this pronunciation when it finishes processing the word.
        :param str display_as: The spelling of the word that the service uses to display the word in a transcript. The field contains an empty string if no display-as value is provided for the word, in which case the word is displayed as it is spelled.
        :param int count: A sum of the number of times the word is found across all corpora. For example, if the word occurs five times in one corpus and seven times in another, its count is `12`. If you add a custom word to a model before it is added by any corpora, the count begins at `1`; if the word is added from a corpus first and later modified, the count reflects only the number of times it is found in corpora.
        :param list[str] source: An array of sources that describes how the word was added to the custom model's words resource. For OOV words added from a corpus, includes the name of the corpus; if the word was added by multiple corpora, the names of all corpora are listed. If the word was modified or added by the user directly, the field includes the string `user`.
        :param list[WordError] error: (optional) If the service discovered one or more problems that you need to correct for the word's definition, an array that describes each of the errors.
        """
        self.word = word
        self.sounds_like = sounds_like
        self.display_as = display_as
        self.count = count
        self.source = source
        self.error = error

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Word object from a json dictionary."""
        args = {}
        if 'word' in _dict:
            args['word'] = _dict.get('word')
        else:
            raise ValueError(
                'Required property \'word\' not present in Word JSON')
        if 'sounds_like' in _dict:
            args['sounds_like'] = _dict.get('sounds_like')
        else:
            raise ValueError(
                'Required property \'sounds_like\' not present in Word JSON')
        if 'display_as' in _dict:
            args['display_as'] = _dict.get('display_as')
        else:
            raise ValueError(
                'Required property \'display_as\' not present in Word JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError(
                'Required property \'count\' not present in Word JSON')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        else:
            raise ValueError(
                'Required property \'source\' not present in Word JSON')
        if 'error' in _dict:
            args['error'] = [
                WordError._from_dict(x) for x in (_dict.get('error'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word
        if hasattr(self, 'sounds_like') and self.sounds_like is not None:
            _dict['sounds_like'] = self.sounds_like
        if hasattr(self, 'display_as') and self.display_as is not None:
            _dict['display_as'] = self.display_as
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = [x._to_dict() for x in self.error]
        return _dict

    def __str__(self):
        """Return a `str` version of this Word object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordAlternativeResult(object):
    """
    WordAlternativeResult.

    :attr float confidence: A confidence score for the word alternative hypothesis in the range of 0 to 1.
    :attr str word: An alternative hypothesis for a word from the input audio.
    """

    def __init__(self, confidence, word):
        """
        Initialize a WordAlternativeResult object.

        :param float confidence: A confidence score for the word alternative hypothesis in the range of 0 to 1.
        :param str word: An alternative hypothesis for a word from the input audio.
        """
        self.confidence = confidence
        self.word = word

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordAlternativeResult object from a json dictionary."""
        args = {}
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        else:
            raise ValueError(
                'Required property \'confidence\' not present in WordAlternativeResult JSON'
            )
        if 'word' in _dict:
            args['word'] = _dict.get('word')
        else:
            raise ValueError(
                'Required property \'word\' not present in WordAlternativeResult JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word
        return _dict

    def __str__(self):
        """Return a `str` version of this WordAlternativeResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordAlternativeResults(object):
    """
    WordAlternativeResults.

    :attr float start_time: The start time in seconds of the word from the input audio that corresponds to the word alternatives.
    :attr float end_time: The end time in seconds of the word from the input audio that corresponds to the word alternatives.
    :attr list[WordAlternativeResult] alternatives: An array of alternative hypotheses for a word from the input audio.
    """

    def __init__(self, start_time, end_time, alternatives):
        """
        Initialize a WordAlternativeResults object.

        :param float start_time: The start time in seconds of the word from the input audio that corresponds to the word alternatives.
        :param float end_time: The end time in seconds of the word from the input audio that corresponds to the word alternatives.
        :param list[WordAlternativeResult] alternatives: An array of alternative hypotheses for a word from the input audio.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.alternatives = alternatives

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordAlternativeResults object from a json dictionary."""
        args = {}
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        else:
            raise ValueError(
                'Required property \'start_time\' not present in WordAlternativeResults JSON'
            )
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        else:
            raise ValueError(
                'Required property \'end_time\' not present in WordAlternativeResults JSON'
            )
        if 'alternatives' in _dict:
            args['alternatives'] = [
                WordAlternativeResult._from_dict(x)
                for x in (_dict.get('alternatives'))
            ]
        else:
            raise ValueError(
                'Required property \'alternatives\' not present in WordAlternativeResults JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'alternatives') and self.alternatives is not None:
            _dict['alternatives'] = [x._to_dict() for x in self.alternatives]
        return _dict

    def __str__(self):
        """Return a `str` version of this WordAlternativeResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordError(object):
    """
    WordError.

    :attr str element: A key-value pair that describes an error associated with the definition of a word in the words resource. Each pair has the format `"element": "message"`, where `element` is the aspect of the definition that caused the problem and `message` describes the problem. The following example describes a problem with one of the word's sounds-like definitions: `"sounds_like_string": "Numbers are not allowed in sounds-like. You can try for example 'suggested_string'."` You must correct the error before you can train the model.
    """

    def __init__(self, element):
        """
        Initialize a WordError object.

        :param str element: A key-value pair that describes an error associated with the definition of a word in the words resource. Each pair has the format `"element": "message"`, where `element` is the aspect of the definition that caused the problem and `message` describes the problem. The following example describes a problem with one of the word's sounds-like definitions: `"sounds_like_string": "Numbers are not allowed in sounds-like. You can try for example 'suggested_string'."` You must correct the error before you can train the model.
        """
        self.element = element

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordError object from a json dictionary."""
        args = {}
        if 'element' in _dict:
            args['element'] = _dict.get('element')
        else:
            raise ValueError(
                'Required property \'element\' not present in WordError JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'element') and self.element is not None:
            _dict['element'] = self.element
        return _dict

    def __str__(self):
        """Return a `str` version of this WordError object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Words(object):
    """
    Words.

    :attr list[Word] words: Information about each word in the custom model's words resource. The array is empty if the custom model has no words.
    """

    def __init__(self, words):
        """
        Initialize a Words object.

        :param list[Word] words: Information about each word in the custom model's words resource. The array is empty if the custom model has no words.
        """
        self.words = words

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Words object from a json dictionary."""
        args = {}
        if 'words' in _dict:
            args['words'] = [Word._from_dict(x) for x in _dict.get('words')]
        else:
            raise ValueError(
                'Required property \'words\' not present in Words JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'words') and self.words is not None:
            _dict['words'] = [x._to_dict() for x in self.words]
        return _dict

    def __str__(self):
        """Return a `str` version of this Words object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
