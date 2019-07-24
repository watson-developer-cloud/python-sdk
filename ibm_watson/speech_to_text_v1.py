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
The IBM&reg; Speech to Text service provides APIs that use IBM's speech-recognition
capabilities to produce transcripts of spoken audio. The service can transcribe speech
from various languages and audio formats. In addition to basic transcription, the service
can produce detailed information about many different aspects of the audio. For most
languages, the service supports two sampling rates, broadband and narrowband. It returns
all JSON response content in the UTF-8 character set.
For speech recognition, the service supports synchronous and asynchronous HTTP
Representational State Transfer (REST) interfaces. It also supports a WebSocket interface
that provides a full-duplex, low-latency communication channel: Clients send requests and
audio to the service and receive results over a single connection asynchronously.
The service also offers two customization interfaces. Use language model customization to
expand the vocabulary of a base model with domain-specific terminology. Use acoustic model
customization to adapt a base model for the acoustic characteristics of your audio. For
language model customization, the service also supports grammars. A grammar is a formal
language specification that lets you restrict the phrases that the service can recognize.
Language model customization is generally available for production use with most supported
languages. Acoustic model customization is beta functionality that is available for all
supported languages.
"""

from __future__ import absolute_import

import json
from .common import get_sdk_headers
from ibm_cloud_sdk_core import BaseService

##############################################################################
# Service
##############################################################################


class SpeechToTextV1(BaseService):
    """The Speech to Text V1 service."""

    default_url = 'https://stream.watsonplatform.net/speech-to-text/api'

    def __init__(
            self,
            url=default_url,
            username=None,
            password=None,
            iam_apikey=None,
            iam_access_token=None,
            iam_url=None,
            iam_client_id=None,
            iam_client_secret=None,
            icp4d_access_token=None,
            icp4d_url=None,
            authentication_type=None,
    ):
        """
        Construct a new client for the Speech to Text service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://stream.watsonplatform.net/speech-to-text/api/speech-to-text/api").
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
            vcap_services_name='speech_to_text',
            url=url,
            username=username,
            password=password,
            iam_apikey=iam_apikey,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            iam_client_id=iam_client_id,
            iam_client_secret=iam_client_secret,
            use_vcap_services=True,
            display_name='Speech to Text',
            icp4d_access_token=icp4d_access_token,
            icp4d_url=icp4d_url,
            authentication_type=authentication_type)

    #########################
    # Models
    #########################

    def list_models(self, **kwargs):
        """
        List models.

        Lists all language models that are available for use with the service. The
        information includes the name of the model and its minimum sampling rate in Hertz,
        among other things.
        **See also:** [Languages and
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-models#models).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'list_models')
        headers.update(sdk_headers)

        url = '/v1/models'
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def get_model(self, model_id, **kwargs):
        """
        Get a model.

        Gets information for a single specified language model that is available for use
        with the service. The information includes the name of the model and its minimum
        sampling rate in Hertz, among other things.
        **See also:** [Languages and
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-models#models).

        :param str model_id: The identifier of the model in the form of its name from the
        output of the **Get a model** method.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if model_id is None:
            raise ValueError('model_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'get_model')
        headers.update(sdk_headers)

        url = '/v1/models/{0}'.format(*self._encode_path_vars(model_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # Synchronous
    #########################

    def recognize(self,
                  audio,
                  model=None,
                  language_customization_id=None,
                  acoustic_customization_id=None,
                  base_model_version=None,
                  customization_weight=None,
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
                  customization_id=None,
                  grammar_name=None,
                  redaction=None,
                  content_type=None,
                  audio_metrics=None,
                  **kwargs):
        """
        Recognize audio.

        Sends audio and returns transcription results for a recognition request. You can
        pass a maximum of 100 MB and a minimum of 100 bytes of audio with a request. The
        service automatically detects the endianness of the incoming audio and, for audio
        that includes multiple channels, downmixes the audio to one-channel mono during
        transcoding. The method returns only final results; to enable interim results, use
        the WebSocket API. (With the `curl` command, use the `--data-binary` option to
        upload the file for the request.)
        **See also:** [Making a basic HTTP
        request](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-http#HTTP-basic).
        ### Streaming mode
         For requests to transcribe live audio as it becomes available, you must set the
        `Transfer-Encoding` header to `chunked` to use streaming mode. In streaming mode,
        the service closes the connection (status code 408) if it does not receive at
        least 15 seconds of audio (including silence) in any 30-second period. The service
        also closes the connection (status code 400) if it detects no speech for
        `inactivity_timeout` seconds of streaming audio; use the `inactivity_timeout`
        parameter to change the default of 30 seconds.
        **See also:**
        * [Audio
        transmission](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#transmission)
        *
        [Timeouts](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#timeouts)
        ### Audio formats (content types)
         The service accepts audio in the following formats (MIME types).
        * For formats that are labeled **Required**, you must use the `Content-Type`
        header with the request to specify the format of the audio.
        * For all other formats, you can omit the `Content-Type` header or specify
        `application/octet-stream` with the header to have the service automatically
        detect the format of the audio. (With the `curl` command, you can specify either
        `\"Content-Type:\"` or `\"Content-Type: application/octet-stream\"`.)
        Where indicated, the format that you specify must include the sampling rate and
        can optionally include the number of channels and the endianness of the audio.
        * `audio/alaw` (**Required.** Specify the sampling rate (`rate`) of the audio.)
        * `audio/basic` (**Required.** Use only with narrowband models.)
        * `audio/flac`
        * `audio/g729` (Use only with narrowband models.)
        * `audio/l16` (**Required.** Specify the sampling rate (`rate`) and optionally the
        number of channels (`channels`) and endianness (`endianness`) of the audio.)
        * `audio/mp3`
        * `audio/mpeg`
        * `audio/mulaw` (**Required.** Specify the sampling rate (`rate`) of the audio.)
        * `audio/ogg` (The service automatically detects the codec of the input audio.)
        * `audio/ogg;codecs=opus`
        * `audio/ogg;codecs=vorbis`
        * `audio/wav` (Provide audio with a maximum of nine channels.)
        * `audio/webm` (The service automatically detects the codec of the input audio.)
        * `audio/webm;codecs=opus`
        * `audio/webm;codecs=vorbis`
        The sampling rate of the audio must match the sampling rate of the model for the
        recognition request: for broadband models, at least 16 kHz; for narrowband models,
        at least 8 kHz. If the sampling rate of the audio is higher than the minimum
        required rate, the service down-samples the audio to the appropriate rate. If the
        sampling rate of the audio is lower than the minimum required rate, the request
        fails.
         **See also:** [Audio
        formats](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-audio-formats#audio-formats).
        ### Multipart speech recognition
         **Note:** The Watson SDKs do not support multipart speech recognition.
        The HTTP `POST` method of the service also supports multipart speech recognition.
        With multipart requests, you pass all audio data as multipart form data. You
        specify some parameters as request headers and query parameters, but you pass JSON
        metadata as form data to control most aspects of the transcription. You can use
        multipart recognition to pass multiple audio files with a single request.
        Use the multipart approach with browsers for which JavaScript is disabled or when
        the parameters used with the request are greater than the 8 KB limit imposed by
        most HTTP servers and proxies. You can encounter this limit, for example, if you
        want to spot a very large number of keywords.
        **See also:** [Making a multipart HTTP
        request](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-http#HTTP-multi).

        :param file audio: The audio to transcribe.
        :param str model: The identifier of the model that is to be used for the
        recognition request. See [Languages and
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-models#models).
        :param str language_customization_id: The customization ID (GUID) of a custom
        language model that is to be used with the recognition request. The base model of
        the specified custom language model must match the model specified with the
        `model` parameter. You must make the request with credentials for the instance of
        the service that owns the custom model. By default, no custom language model is
        used. See [Custom
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#custom-input).
        **Note:** Use this parameter instead of the deprecated `customization_id`
        parameter.
        :param str acoustic_customization_id: The customization ID (GUID) of a custom
        acoustic model that is to be used with the recognition request. The base model of
        the specified custom acoustic model must match the model specified with the
        `model` parameter. You must make the request with credentials for the instance of
        the service that owns the custom model. By default, no custom acoustic model is
        used. See [Custom
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#custom-input).
        :param str base_model_version: The version of the specified base model that is to
        be used with the recognition request. Multiple versions of a base model can exist
        when a model is updated for internal improvements. The parameter is intended
        primarily for use with custom models that have been upgraded for a new base model.
        The default value depends on whether the parameter is used with or without a
        custom model. See [Base model
        version](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#version).
        :param float customization_weight: If you specify the customization ID (GUID) of a
        custom language model with the recognition request, the customization weight tells
        the service how much weight to give to words from the custom language model
        compared to those from the base model for the current request.
        Specify a value between 0.0 and 1.0. Unless a different customization weight was
        specified for the custom model when it was trained, the default value is 0.3. A
        customization weight that you specify overrides a weight that was specified when
        the custom model was trained.
        The default value yields the best performance in general. Assign a higher value if
        your audio makes frequent use of OOV words from the custom model. Use caution when
        setting the weight: a higher value can improve the accuracy of phrases from the
        custom model's domain, but it can negatively affect performance on non-domain
        phrases.
        See [Custom
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#custom-input).
        :param int inactivity_timeout: The time in seconds after which, if only silence
        (no speech) is detected in streaming audio, the connection is closed with a 400
        error. The parameter is useful for stopping audio submission from a live
        microphone when a user simply walks away. Use `-1` for infinity. See [Inactivity
        timeout](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#timeouts-inactivity).
        :param list[str] keywords: An array of keyword strings to spot in the audio. Each
        keyword string can include one or more string tokens. Keywords are spotted only in
        the final results, not in interim hypotheses. If you specify any keywords, you
        must also specify a keywords threshold. You can spot a maximum of 1000 keywords.
        Omit the parameter or specify an empty array if you do not need to spot keywords.
        See [Keyword
        spotting](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#keyword_spotting).
        :param float keywords_threshold: A confidence value that is the lower bound for
        spotting a keyword. A word is considered to match a keyword if its confidence is
        greater than or equal to the threshold. Specify a probability between 0.0 and 1.0.
        If you specify a threshold, you must also specify one or more keywords. The
        service performs no keyword spotting if you omit either parameter. See [Keyword
        spotting](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#keyword_spotting).
        :param int max_alternatives: The maximum number of alternative transcripts that
        the service is to return. By default, the service returns a single transcript. If
        you specify a value of `0`, the service uses the default value, `1`. See [Maximum
        alternatives](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#max_alternatives).
        :param float word_alternatives_threshold: A confidence value that is the lower
        bound for identifying a hypothesis as a possible word alternative (also known as
        \"Confusion Networks\"). An alternative word is considered if its confidence is
        greater than or equal to the threshold. Specify a probability between 0.0 and 1.0.
        By default, the service computes no alternative words. See [Word
        alternatives](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#word_alternatives).
        :param bool word_confidence: If `true`, the service returns a confidence measure
        in the range of 0.0 to 1.0 for each word. By default, the service returns no word
        confidence scores. See [Word
        confidence](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#word_confidence).
        :param bool timestamps: If `true`, the service returns time alignment for each
        word. By default, no timestamps are returned. See [Word
        timestamps](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#word_timestamps).
        :param bool profanity_filter: If `true`, the service filters profanity from all
        output except for keyword results by replacing inappropriate words with a series
        of asterisks. Set the parameter to `false` to return results with no censoring.
        Applies to US English transcription only. See [Profanity
        filtering](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#profanity_filter).
        :param bool smart_formatting: If `true`, the service converts dates, times, series
        of digits and numbers, phone numbers, currency values, and internet addresses into
        more readable, conventional representations in the final transcript of a
        recognition request. For US English, the service also converts certain keyword
        strings to punctuation symbols. By default, the service performs no smart
        formatting.
        **Note:** Applies to US English, Japanese, and Spanish transcription only.
        See [Smart
        formatting](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#smart_formatting).
        :param bool speaker_labels: If `true`, the response includes labels that identify
        which words were spoken by which participants in a multi-person exchange. By
        default, the service returns no speaker labels. Setting `speaker_labels` to `true`
        forces the `timestamps` parameter to be `true`, regardless of whether you specify
        `false` for the parameter.
        **Note:** Applies to US English, Japanese, and Spanish transcription only. To
        determine whether a language model supports speaker labels, you can also use the
        **Get a model** method and check that the attribute `speaker_labels` is set to
        `true`.
        See [Speaker
        labels](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#speaker_labels).
        :param str customization_id: **Deprecated.** Use the `language_customization_id`
        parameter to specify the customization ID (GUID) of a custom language model that
        is to be used with the recognition request. Do not specify both parameters with a
        request.
        :param str grammar_name: The name of a grammar that is to be used with the
        recognition request. If you specify a grammar, you must also use the
        `language_customization_id` parameter to specify the name of the custom language
        model for which the grammar is defined. The service recognizes only strings that
        are recognized by the specified grammar; it does not recognize other custom words
        from the model's words resource. See
        [Grammars](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#grammars-input).
        :param bool redaction: If `true`, the service redacts, or masks, numeric data from
        final transcripts. The feature redacts any number that has three or more
        consecutive digits by replacing each digit with an `X` character. It is intended
        to redact sensitive numeric data, such as credit card numbers. By default, the
        service performs no redaction.
        When you enable redaction, the service automatically enables smart formatting,
        regardless of whether you explicitly disable that feature. To ensure maximum
        security, the service also disables keyword spotting (ignores the `keywords` and
        `keywords_threshold` parameters) and returns only a single final transcript
        (forces the `max_alternatives` parameter to be `1`).
        **Note:** Applies to US English, Japanese, and Korean transcription only.
        See [Numeric
        redaction](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#redaction).
        :param bool audio_metrics: If `true`, requests detailed information about the
        signal characteristics of the input audio. The service returns audio metrics with
        the final transcription results. By default, the service returns no audio metrics.
        :param str content_type: The format (MIME type) of the audio. For more information
        about specifying an audio format, see **Audio formats (content types)** in the
        method description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if audio is None:
            raise ValueError('audio must be provided')

        headers = {'Content-Type': content_type}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'recognize')
        headers.update(sdk_headers)

        params = {
            'model': model,
            'language_customization_id': language_customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'base_model_version': base_model_version,
            'customization_weight': customization_weight,
            'inactivity_timeout': inactivity_timeout,
            'keywords': self._convert_list(keywords),
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'speaker_labels': speaker_labels,
            'customization_id': customization_id,
            'grammar_name': grammar_name,
            'redaction': redaction,
            'audio_metrics': audio_metrics
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

    #########################
    # Asynchronous
    #########################

    def register_callback(self, callback_url, user_secret=None, **kwargs):
        """
        Register a callback.

        Registers a callback URL with the service for use with subsequent asynchronous
        recognition requests. The service attempts to register, or white-list, the
        callback URL if it is not already registered by sending a `GET` request to the
        callback URL. The service passes a random alphanumeric challenge string via the
        `challenge_string` parameter of the request. The request includes an `Accept`
        header that specifies `text/plain` as the required response type.
        To be registered successfully, the callback URL must respond to the `GET` request
        from the service. The response must send status code 200 and must include the
        challenge string in its body. Set the `Content-Type` response header to
        `text/plain`. Upon receiving this response, the service responds to the original
        registration request with response code 201.
        The service sends only a single `GET` request to the callback URL. If the service
        does not receive a reply with a response code of 200 and a body that echoes the
        challenge string sent by the service within five seconds, it does not white-list
        the URL; it instead sends status code 400 in response to the **Register a
        callback** request. If the requested callback URL is already white-listed, the
        service responds to the initial registration request with response code 200.
        If you specify a user secret with the request, the service uses it as a key to
        calculate an HMAC-SHA1 signature of the challenge string in its response to the
        `POST` request. It sends this signature in the `X-Callback-Signature` header of
        its `GET` request to the URL during registration. It also uses the secret to
        calculate a signature over the payload of every callback notification that uses
        the URL. The signature provides authentication and data integrity for HTTP
        communications.
        After you successfully register a callback URL, you can use it with an indefinite
        number of recognition requests. You can register a maximum of 20 callback URLS in
        a one-hour span of time.
        **See also:** [Registering a callback
        URL](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-async#register).

        :param str callback_url: An HTTP or HTTPS URL to which callback notifications are
        to be sent. To be white-listed, the URL must successfully echo the challenge
        string during URL verification. During verification, the client can also check the
        signature that the service sends in the `X-Callback-Signature` header to verify
        the origin of the request.
        :param str user_secret: A user-specified string that the service uses to generate
        the HMAC-SHA1 signature that it sends via the `X-Callback-Signature` header. The
        service includes the header during URL verification and with every notification
        sent to the callback URL. It calculates the signature over the payload of the
        notification. If you omit the parameter, the service does not send the header.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if callback_url is None:
            raise ValueError('callback_url must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'register_callback')
        headers.update(sdk_headers)

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
        Unregister a callback.

        Unregisters a callback URL that was previously white-listed with a **Register a
        callback** request for use with the asynchronous interface. Once unregistered, the
        URL can no longer be used with asynchronous recognition requests.
        **See also:** [Unregistering a callback
        URL](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-async#unregister).

        :param str callback_url: The callback URL that is to be unregistered.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if callback_url is None:
            raise ValueError('callback_url must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'unregister_callback')
        headers.update(sdk_headers)

        params = {'callback_url': callback_url}

        url = '/v1/unregister_callback'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=False)
        return response

    def create_job(self,
                   audio,
                   model=None,
                   callback_url=None,
                   events=None,
                   user_token=None,
                   results_ttl=None,
                   language_customization_id=None,
                   acoustic_customization_id=None,
                   base_model_version=None,
                   customization_weight=None,
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
                   customization_id=None,
                   grammar_name=None,
                   redaction=None,
                   content_type=None,
                   processing_metrics=None,
                   processing_metrics_interval=None,
                   audio_metrics=None,
                   **kwargs):
        """
        Create a job.

        Creates a job for a new asynchronous recognition request. The job is owned by the
        instance of the service whose credentials are used to create it. How you learn the
        status and results of a job depends on the parameters you include with the job
        creation request:
        * By callback notification: Include the `callback_url` parameter to specify a URL
        to which the service is to send callback notifications when the status of the job
        changes. Optionally, you can also include the `events` and `user_token` parameters
        to subscribe to specific events and to specify a string that is to be included
        with each notification for the job.
        * By polling the service: Omit the `callback_url`, `events`, and `user_token`
        parameters. You must then use the **Check jobs** or **Check a job** methods to
        check the status of the job, using the latter to retrieve the results when the job
        is complete.
        The two approaches are not mutually exclusive. You can poll the service for job
        status or obtain results from the service manually even if you include a callback
        URL. In both cases, you can include the `results_ttl` parameter to specify how
        long the results are to remain available after the job is complete. Using the
        HTTPS **Check a job** method to retrieve results is more secure than receiving
        them via callback notification over HTTP because it provides confidentiality in
        addition to authentication and data integrity.
        The method supports the same basic parameters as other HTTP and WebSocket
        recognition requests. It also supports the following parameters specific to the
        asynchronous interface:
        * `callback_url`
        * `events`
        * `user_token`
        * `results_ttl`
        You can pass a maximum of 1 GB and a minimum of 100 bytes of audio with a request.
        The service automatically detects the endianness of the incoming audio and, for
        audio that includes multiple channels, downmixes the audio to one-channel mono
        during transcoding. The method returns only final results; to enable interim
        results, use the WebSocket API. (With the `curl` command, use the `--data-binary`
        option to upload the file for the request.)
        **See also:** [Creating a
        job](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-async#create).
        ### Streaming mode
         For requests to transcribe live audio as it becomes available, you must set the
        `Transfer-Encoding` header to `chunked` to use streaming mode. In streaming mode,
        the service closes the connection (status code 408) if it does not receive at
        least 15 seconds of audio (including silence) in any 30-second period. The service
        also closes the connection (status code 400) if it detects no speech for
        `inactivity_timeout` seconds of streaming audio; use the `inactivity_timeout`
        parameter to change the default of 30 seconds.
        **See also:**
        * [Audio
        transmission](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#transmission)
        *
        [Timeouts](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#timeouts)
        ### Audio formats (content types)
         The service accepts audio in the following formats (MIME types).
        * For formats that are labeled **Required**, you must use the `Content-Type`
        header with the request to specify the format of the audio.
        * For all other formats, you can omit the `Content-Type` header or specify
        `application/octet-stream` with the header to have the service automatically
        detect the format of the audio. (With the `curl` command, you can specify either
        `\"Content-Type:\"` or `\"Content-Type: application/octet-stream\"`.)
        Where indicated, the format that you specify must include the sampling rate and
        can optionally include the number of channels and the endianness of the audio.
        * `audio/alaw` (**Required.** Specify the sampling rate (`rate`) of the audio.)
        * `audio/basic` (**Required.** Use only with narrowband models.)
        * `audio/flac`
        * `audio/g729` (Use only with narrowband models.)
        * `audio/l16` (**Required.** Specify the sampling rate (`rate`) and optionally the
        number of channels (`channels`) and endianness (`endianness`) of the audio.)
        * `audio/mp3`
        * `audio/mpeg`
        * `audio/mulaw` (**Required.** Specify the sampling rate (`rate`) of the audio.)
        * `audio/ogg` (The service automatically detects the codec of the input audio.)
        * `audio/ogg;codecs=opus`
        * `audio/ogg;codecs=vorbis`
        * `audio/wav` (Provide audio with a maximum of nine channels.)
        * `audio/webm` (The service automatically detects the codec of the input audio.)
        * `audio/webm;codecs=opus`
        * `audio/webm;codecs=vorbis`
        The sampling rate of the audio must match the sampling rate of the model for the
        recognition request: for broadband models, at least 16 kHz; for narrowband models,
        at least 8 kHz. If the sampling rate of the audio is higher than the minimum
        required rate, the service down-samples the audio to the appropriate rate. If the
        sampling rate of the audio is lower than the minimum required rate, the request
        fails.
         **See also:** [Audio
        formats](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-audio-formats#audio-formats).

        :param file audio: The audio to transcribe.
        :param str model: The identifier of the model that is to be used for the
        recognition request. See [Languages and
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-models#models).
        :param str callback_url: A URL to which callback notifications are to be sent. The
        URL must already be successfully white-listed by using the **Register a callback**
        method. You can include the same callback URL with any number of job creation
        requests. Omit the parameter to poll the service for job completion and results.
        Use the `user_token` parameter to specify a unique user-specified string with each
        job to differentiate the callback notifications for the jobs.
        :param str events: If the job includes a callback URL, a comma-separated list of
        notification events to which to subscribe. Valid events are
        * `recognitions.started` generates a callback notification when the service begins
        to process the job.
        * `recognitions.completed` generates a callback notification when the job is
        complete. You must use the **Check a job** method to retrieve the results before
        they time out or are deleted.
        * `recognitions.completed_with_results` generates a callback notification when the
        job is complete. The notification includes the results of the request.
        * `recognitions.failed` generates a callback notification if the service
        experiences an error while processing the job.
        The `recognitions.completed` and `recognitions.completed_with_results` events are
        incompatible. You can specify only of the two events.
        If the job includes a callback URL, omit the parameter to subscribe to the default
        events: `recognitions.started`, `recognitions.completed`, and
        `recognitions.failed`. If the job does not include a callback URL, omit the
        parameter.
        :param str user_token: If the job includes a callback URL, a user-specified string
        that the service is to include with each callback notification for the job; the
        token allows the user to maintain an internal mapping between jobs and
        notification events. If the job does not include a callback URL, omit the
        parameter.
        :param int results_ttl: The number of minutes for which the results are to be
        available after the job has finished. If not delivered via a callback, the results
        must be retrieved within this time. Omit the parameter to use a time to live of
        one week. The parameter is valid with or without a callback URL.
        :param str language_customization_id: The customization ID (GUID) of a custom
        language model that is to be used with the recognition request. The base model of
        the specified custom language model must match the model specified with the
        `model` parameter. You must make the request with credentials for the instance of
        the service that owns the custom model. By default, no custom language model is
        used. See [Custom
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#custom-input).
        **Note:** Use this parameter instead of the deprecated `customization_id`
        parameter.
        :param str acoustic_customization_id: The customization ID (GUID) of a custom
        acoustic model that is to be used with the recognition request. The base model of
        the specified custom acoustic model must match the model specified with the
        `model` parameter. You must make the request with credentials for the instance of
        the service that owns the custom model. By default, no custom acoustic model is
        used. See [Custom
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#custom-input).
        :param str base_model_version: The version of the specified base model that is to
        be used with the recognition request. Multiple versions of a base model can exist
        when a model is updated for internal improvements. The parameter is intended
        primarily for use with custom models that have been upgraded for a new base model.
        The default value depends on whether the parameter is used with or without a
        custom model. See [Base model
        version](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#version).
        :param float customization_weight: If you specify the customization ID (GUID) of a
        custom language model with the recognition request, the customization weight tells
        the service how much weight to give to words from the custom language model
        compared to those from the base model for the current request.
        Specify a value between 0.0 and 1.0. Unless a different customization weight was
        specified for the custom model when it was trained, the default value is 0.3. A
        customization weight that you specify overrides a weight that was specified when
        the custom model was trained.
        The default value yields the best performance in general. Assign a higher value if
        your audio makes frequent use of OOV words from the custom model. Use caution when
        setting the weight: a higher value can improve the accuracy of phrases from the
        custom model's domain, but it can negatively affect performance on non-domain
        phrases.
        See [Custom
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#custom-input).
        :param int inactivity_timeout: The time in seconds after which, if only silence
        (no speech) is detected in streaming audio, the connection is closed with a 400
        error. The parameter is useful for stopping audio submission from a live
        microphone when a user simply walks away. Use `-1` for infinity. See [Inactivity
        timeout](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#timeouts-inactivity).
        :param list[str] keywords: An array of keyword strings to spot in the audio. Each
        keyword string can include one or more string tokens. Keywords are spotted only in
        the final results, not in interim hypotheses. If you specify any keywords, you
        must also specify a keywords threshold. You can spot a maximum of 1000 keywords.
        Omit the parameter or specify an empty array if you do not need to spot keywords.
        See [Keyword
        spotting](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#keyword_spotting).
        :param float keywords_threshold: A confidence value that is the lower bound for
        spotting a keyword. A word is considered to match a keyword if its confidence is
        greater than or equal to the threshold. Specify a probability between 0.0 and 1.0.
        If you specify a threshold, you must also specify one or more keywords. The
        service performs no keyword spotting if you omit either parameter. See [Keyword
        spotting](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#keyword_spotting).
        :param int max_alternatives: The maximum number of alternative transcripts that
        the service is to return. By default, the service returns a single transcript. If
        you specify a value of `0`, the service uses the default value, `1`. See [Maximum
        alternatives](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#max_alternatives).
        :param float word_alternatives_threshold: A confidence value that is the lower
        bound for identifying a hypothesis as a possible word alternative (also known as
        \"Confusion Networks\"). An alternative word is considered if its confidence is
        greater than or equal to the threshold. Specify a probability between 0.0 and 1.0.
        By default, the service computes no alternative words. See [Word
        alternatives](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#word_alternatives).
        :param bool word_confidence: If `true`, the service returns a confidence measure
        in the range of 0.0 to 1.0 for each word. By default, the service returns no word
        confidence scores. See [Word
        confidence](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#word_confidence).
        :param bool timestamps: If `true`, the service returns time alignment for each
        word. By default, no timestamps are returned. See [Word
        timestamps](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#word_timestamps).
        :param bool profanity_filter: If `true`, the service filters profanity from all
        output except for keyword results by replacing inappropriate words with a series
        of asterisks. Set the parameter to `false` to return results with no censoring.
        Applies to US English transcription only. See [Profanity
        filtering](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#profanity_filter).
        :param bool smart_formatting: If `true`, the service converts dates, times, series
        of digits and numbers, phone numbers, currency values, and internet addresses into
        more readable, conventional representations in the final transcript of a
        recognition request. For US English, the service also converts certain keyword
        strings to punctuation symbols. By default, the service performs no smart
        formatting.
        **Note:** Applies to US English, Japanese, and Spanish transcription only.
        See [Smart
        formatting](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#smart_formatting).
        :param bool speaker_labels: If `true`, the response includes labels that identify
        which words were spoken by which participants in a multi-person exchange. By
        default, the service returns no speaker labels. Setting `speaker_labels` to `true`
        forces the `timestamps` parameter to be `true`, regardless of whether you specify
        `false` for the parameter.
        **Note:** Applies to US English, Japanese, and Spanish transcription only. To
        determine whether a language model supports speaker labels, you can also use the
        **Get a model** method and check that the attribute `speaker_labels` is set to
        `true`.
        See [Speaker
        labels](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#speaker_labels).
        :param str customization_id: **Deprecated.** Use the `language_customization_id`
        parameter to specify the customization ID (GUID) of a custom language model that
        is to be used with the recognition request. Do not specify both parameters with a
        request.
        :param str grammar_name: The name of a grammar that is to be used with the
        recognition request. If you specify a grammar, you must also use the
        `language_customization_id` parameter to specify the name of the custom language
        model for which the grammar is defined. The service recognizes only strings that
        are recognized by the specified grammar; it does not recognize other custom words
        from the model's words resource. See
        [Grammars](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-input#grammars-input).
        :param bool redaction: If `true`, the service redacts, or masks, numeric data from
        final transcripts. The feature redacts any number that has three or more
        consecutive digits by replacing each digit with an `X` character. It is intended
        to redact sensitive numeric data, such as credit card numbers. By default, the
        service performs no redaction.
        When you enable redaction, the service automatically enables smart formatting,
        regardless of whether you explicitly disable that feature. To ensure maximum
        security, the service also disables keyword spotting (ignores the `keywords` and
        `keywords_threshold` parameters) and returns only a single final transcript
        (forces the `max_alternatives` parameter to be `1`).
        **Note:** Applies to US English, Japanese, and Korean transcription only.
        See [Numeric
        redaction](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-output#redaction).
        :param bool processing_metrics: If `true`, requests processing metrics about the
        service's transcription of the input audio. The service returns processing metrics
        at the interval specified by the `processing_metrics_interval` parameter. It also
        returns processing metrics for transcription events, for example, for final and
        interim results. By default, the service returns no processing metrics.
        :param float processing_metrics_interval: Specifies the interval in real
        wall-clock seconds at which the service is to return processing metrics. The
        parameter is ignored unless the `processing_metrics` parameter is set to `true`.
        The parameter accepts a minimum value of 0.1 seconds. The level of precision is
        not restricted, so you can specify values such as 0.25 and 0.125.
        The service does not impose a maximum value. If you want to receive processing
        metrics only for transcription events instead of at periodic intervals, set the
        value to a large number. If the value is larger than the duration of the audio,
        the service returns processing metrics only for transcription events.
        :param bool audio_metrics: If `true`, requests detailed information about the
        signal characteristics of the input audio. The service returns audio metrics with
        the final transcription results. By default, the service returns no audio metrics.
        :param str content_type: The format (MIME type) of the audio. For more information
        about specifying an audio format, see **Audio formats (content types)** in the
        method description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if audio is None:
            raise ValueError('audio must be provided')

        headers = {'Content-Type': content_type}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'create_job')
        headers.update(sdk_headers)

        params = {
            'model': model,
            'callback_url': callback_url,
            'events': events,
            'user_token': user_token,
            'results_ttl': results_ttl,
            'language_customization_id': language_customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'base_model_version': base_model_version,
            'customization_weight': customization_weight,
            'inactivity_timeout': inactivity_timeout,
            'keywords': self._convert_list(keywords),
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'speaker_labels': speaker_labels,
            'customization_id': customization_id,
            'grammar_name': grammar_name,
            'redaction': redaction,
            'processing_metrics': processing_metrics,
            'processing_metrics_interval': processing_metrics_interval,
            'audio_metrics': audio_metrics
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

    def check_jobs(self, **kwargs):
        """
        Check jobs.

        Returns the ID and status of the latest 100 outstanding jobs associated with the
        credentials with which it is called. The method also returns the creation and
        update times of each job, and, if a job was created with a callback URL and a user
        token, the user token for the job. To obtain the results for a job whose status is
        `completed` or not one of the latest 100 outstanding jobs, use the **Check a job**
        method. A job and its results remain available until you delete them with the
        **Delete a job** method or until the job's time to live expires, whichever comes
        first.
        **See also:** [Checking the status of the latest
        jobs](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-async#jobs).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'check_jobs')
        headers.update(sdk_headers)

        url = '/v1/recognitions'
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def check_job(self, id, **kwargs):
        """
        Check a job.

        Returns information about the specified job. The response always includes the
        status of the job and its creation and update times. If the status is `completed`,
        the response includes the results of the recognition request. You must use
        credentials for the instance of the service that owns a job to list information
        about it.
        You can use the method to retrieve the results of any job, regardless of whether
        it was submitted with a callback URL and the `recognitions.completed_with_results`
        event, and you can retrieve the results multiple times for as long as they remain
        available. Use the **Check jobs** method to request information about the most
        recent jobs associated with the calling credentials.
        **See also:** [Checking the status and retrieving the results of a
        job](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-async#job).

        :param str id: The identifier of the asynchronous job that is to be used for the
        request. You must make the request with credentials for the instance of the
        service that owns the job.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'check_job')
        headers.update(sdk_headers)

        url = '/v1/recognitions/{0}'.format(*self._encode_path_vars(id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def delete_job(self, id, **kwargs):
        """
        Delete a job.

        Deletes the specified job. You cannot delete a job that the service is actively
        processing. Once you delete a job, its results are no longer available. The
        service automatically deletes a job and its results when the time to live for the
        results expires. You must use credentials for the instance of the service that
        owns a job to delete it.
        **See also:** [Deleting a
        job](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-async#delete-async).

        :param str id: The identifier of the asynchronous job that is to be used for the
        request. You must make the request with credentials for the instance of the
        service that owns the job.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'delete_job')
        headers.update(sdk_headers)

        url = '/v1/recognitions/{0}'.format(*self._encode_path_vars(id))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=False)
        return response

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
        Create a custom language model.

        Creates a new custom language model for a specified base model. The custom
        language model can be used only with the base model for which it is created. The
        model is owned by the instance of the service whose credentials are used to create
        it.
        **See also:** [Create a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-languageCreate#createModel-language).

        :param str name: A user-defined name for the new custom language model. Use a name
        that is unique among all custom language models that you own. Use a localized name
        that matches the language of the custom model. Use a name that describes the
        domain of the custom model, such as `Medical custom model` or `Legal custom
        model`.
        :param str base_model_name: The name of the base language model that is to be
        customized by the new custom language model. The new custom model can be used only
        with the base model that it customizes.
        To determine whether a base model supports language model customization, use the
        **Get a model** method and check that the attribute `custom_language_model` is set
        to `true`. You can also refer to [Language support for
        customization](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-customization#languageSupport).
        :param str dialect: The dialect of the specified language that is to be used with
        the custom language model. The parameter is meaningful only for Spanish models,
        for which the service creates a custom language model that is suited for speech in
        one of the following dialects:
        * `es-ES` for Castilian Spanish (the default)
        * `es-LA` for Latin American Spanish
        * `es-US` for North American (Mexican) Spanish
        A specified dialect must be valid for the base model. By default, the dialect
        matches the language of the base model; for example, `en-US` for either of the US
        English language models.
        :param str description: A description of the new custom language model. Use a
        localized description that matches the language of the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')
        if base_model_name is None:
            raise ValueError('base_model_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'create_language_model')
        headers.update(sdk_headers)

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

    def list_language_models(self, language=None, **kwargs):
        """
        List custom language models.

        Lists information about all custom language models that are owned by an instance
        of the service. Use the `language` parameter to see all custom language models for
        the specified language. Omit the parameter to see all custom language models for
        all languages. You must use credentials for the instance of the service that owns
        a model to list information about it.
        **See also:** [Listing custom language
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageLanguageModels#listModels-language).

        :param str language: The identifier of the language for which custom language or
        custom acoustic models are to be returned (for example, `en-US`). Omit the
        parameter to see all custom language or custom acoustic models that are owned by
        the requesting credentials.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'list_language_models')
        headers.update(sdk_headers)

        params = {'language': language}

        url = '/v1/customizations'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_language_model(self, customization_id, **kwargs):
        """
        Get a custom language model.

        Gets information about a specified custom language model. You must use credentials
        for the instance of the service that owns a model to list information about it.
        **See also:** [Listing custom language
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageLanguageModels#listModels-language).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'get_language_model')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def delete_language_model(self, customization_id, **kwargs):
        """
        Delete a custom language model.

        Deletes an existing custom language model. The custom model cannot be deleted if
        another request, such as adding a corpus or grammar to the model, is currently
        being processed. You must use credentials for the instance of the service that
        owns a model to delete it.
        **See also:** [Deleting a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageLanguageModels#deleteModel-language).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'delete_language_model')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    def train_language_model(self,
                             customization_id,
                             word_type_to_add=None,
                             customization_weight=None,
                             **kwargs):
        """
        Train a custom language model.

        Initiates the training of a custom language model with new resources such as
        corpora, grammars, and custom words. After adding, modifying, or deleting
        resources for a custom language model, use this method to begin the actual
        training of the model on the latest data. You can specify whether the custom
        language model is to be trained with all words from its words resource or only
        with words that were added or modified by the user directly. You must use
        credentials for the instance of the service that owns a model to train it.
        The training method is asynchronous. It can take on the order of minutes to
        complete depending on the amount of data on which the service is being trained and
        the current load on the service. The method returns an HTTP 200 response code to
        indicate that the training process has begun.
        You can monitor the status of the training by using the **Get a custom language
        model** method to poll the model's status. Use a loop to check the status every 10
        seconds. The method returns a `LanguageModel` object that includes `status` and
        `progress` fields. A status of `available` means that the custom model is trained
        and ready to use. The service cannot accept subsequent training requests or
        requests to add new resources until the existing request completes.
        **See also:** [Train the custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-languageCreate#trainModel-language).
        ### Training failures
         Training can fail to start for the following reasons:
        * The service is currently handling another request for the custom model, such as
        another training request or a request to add a corpus or grammar to the model.
        * No training data have been added to the custom model.
        * The custom model contains one or more invalid corpora, grammars, or words (for
        example, a custom word has an invalid sounds-like pronunciation). You can correct
        the invalid resources or set the `strict` parameter to `false` to exclude the
        invalid resources from the training. The model must contain at least one valid
        resource for training to succeed.

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str word_type_to_add: The type of words from the custom language model's
        words resource on which to train the model:
        * `all` (the default) trains the model on all new words, regardless of whether
        they were extracted from corpora or grammars or were added or modified by the
        user.
        * `user` trains the model only on new words that were added or modified by the
        user directly. The model is not trained on new words extracted from corpora or
        grammars.
        :param float customization_weight: Specifies a customization weight for the custom
        language model. The customization weight tells the service how much weight to give
        to words from the custom language model compared to those from the base model for
        speech recognition. Specify a value between 0.0 and 1.0; the default is 0.3.
        The default value yields the best performance in general. Assign a higher value if
        your audio makes frequent use of OOV words from the custom model. Use caution when
        setting the weight: a higher value can improve the accuracy of phrases from the
        custom model's domain, but it can negatively affect performance on non-domain
        phrases.
        The value that you assign is used for all recognition requests that use the model.
        You can override it for any recognition request by specifying a customization
        weight for that request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'train_language_model')
        headers.update(sdk_headers)

        params = {
            'word_type_to_add': word_type_to_add,
            'customization_weight': customization_weight
        }

        url = '/v1/customizations/{0}/train'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def reset_language_model(self, customization_id, **kwargs):
        """
        Reset a custom language model.

        Resets a custom language model by removing all corpora, grammars, and words from
        the model. Resetting a custom language model initializes the model to its state
        when it was first created. Metadata such as the name and language of the model are
        preserved, but the model's words resource is removed and must be re-created. You
        must use credentials for the instance of the service that owns a model to reset
        it.
        **See also:** [Resetting a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageLanguageModels#resetModel-language).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'reset_language_model')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/reset'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST', url=url, headers=headers, accept_json=True)
        return response

    def upgrade_language_model(self, customization_id, **kwargs):
        """
        Upgrade a custom language model.

        Initiates the upgrade of a custom language model to the latest version of its base
        language model. The upgrade method is asynchronous. It can take on the order of
        minutes to complete depending on the amount of data in the custom model and the
        current load on the service. A custom model must be in the `ready` or `available`
        state to be upgraded. You must use credentials for the instance of the service
        that owns a model to upgrade it.
        The method returns an HTTP 200 response code to indicate that the upgrade process
        has begun successfully. You can monitor the status of the upgrade by using the
        **Get a custom language model** method to poll the model's status. The method
        returns a `LanguageModel` object that includes `status` and `progress` fields. Use
        a loop to check the status every 10 seconds. While it is being upgraded, the
        custom model has the status `upgrading`. When the upgrade is complete, the model
        resumes the status that it had prior to upgrade. The service cannot accept
        subsequent requests for the model until the upgrade completes.
        **See also:** [Upgrading a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-customUpgrade#upgradeLanguage).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'upgrade_language_model')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/upgrade_model'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # Custom corpora
    #########################

    def list_corpora(self, customization_id, **kwargs):
        """
        List corpora.

        Lists information about all corpora from a custom language model. The information
        includes the total number of words and out-of-vocabulary (OOV) words, name, and
        status of each corpus. You must use credentials for the instance of the service
        that owns a model to list its corpora.
        **See also:** [Listing corpora for a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageCorpora#listCorpora).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'list_corpora')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/corpora'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def add_corpus(self,
                   customization_id,
                   corpus_name,
                   corpus_file,
                   allow_overwrite=None,
                   **kwargs):
        """
        Add a corpus.

        Adds a single corpus text file of new training data to a custom language model.
        Use multiple requests to submit multiple corpus text files. You must use
        credentials for the instance of the service that owns a model to add a corpus to
        it. Adding a corpus does not affect the custom language model until you train the
        model for the new data by using the **Train a custom language model** method.
        Submit a plain text file that contains sample sentences from the domain of
        interest to enable the service to extract words in context. The more sentences you
        add that represent the context in which speakers use words from the domain, the
        better the service's recognition accuracy.
        The call returns an HTTP 201 response code if the corpus is valid. The service
        then asynchronously processes the contents of the corpus and automatically
        extracts new words that it finds. This can take on the order of a minute or two to
        complete depending on the total number of words and the number of new words in the
        corpus, as well as the current load on the service. You cannot submit requests to
        add additional resources to the custom model or to train the model until the
        service's analysis of the corpus for the current request completes. Use the **List
        a corpus** method to check the status of the analysis.
        The service auto-populates the model's words resource with words from the corpus
        that are not found in its base vocabulary. These are referred to as
        out-of-vocabulary (OOV) words. You can use the **List custom words** method to
        examine the words resource. You can use other words method to eliminate typos and
        modify how words are pronounced as needed.
        To add a corpus file that has the same name as an existing corpus, set the
        `allow_overwrite` parameter to `true`; otherwise, the request fails. Overwriting
        an existing corpus causes the service to process the corpus text file and extract
        OOV words anew. Before doing so, it removes any OOV words associated with the
        existing corpus from the model's words resource unless they were also added by
        another corpus or grammar, or they have been modified in some way with the **Add
        custom words** or **Add a custom word** method.
        The service limits the overall amount of data that you can add to a custom model
        to a maximum of 10 million total words from all sources combined. Also, you can
        add no more than 90 thousand custom (OOV) words to a model. This includes words
        that the service extracts from corpora and grammars, and words that you add
        directly.
        **See also:**
        * [Working with
        corpora](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-corporaWords#workingCorpora)
        * [Add a corpus to the custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-languageCreate#addCorpus).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str corpus_name: The name of the new corpus for the custom language model.
        Use a localized name that matches the language of the custom model and reflects
        the contents of the corpus.
        * Include a maximum of 128 characters in the name.
        * Do not use characters that need to be URL-encoded. For example, do not use
        spaces, slashes, backslashes, colons, ampersands, double quotes, plus signs,
        equals signs, questions marks, and so on in the name. (The service does not
        prevent the use of these characters. But because they must be URL-encoded wherever
        used, their use is strongly discouraged.)
        * Do not use the name of an existing corpus or grammar that is already defined for
        the custom model.
        * Do not use the name `user`, which is reserved by the service to denote custom
        words that are added or modified by the user.
        * Do not use the name `base_lm` or `default_lm`. Both names are reserved for
        future use by the service.
        :param file corpus_file: A plain text file that contains the training data for the
        corpus. Encode the file in UTF-8 if it contains non-ASCII characters; the service
        assumes UTF-8 encoding if it encounters non-ASCII characters.
        Make sure that you know the character encoding of the file. You must use that
        encoding when working with the words in the custom language model. For more
        information, see [Character
        encoding](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-corporaWords#charEncoding).
        With the `curl` command, use the `--data-binary` option to upload the file for the
        request.
        :param bool allow_overwrite: If `true`, the specified corpus overwrites an
        existing corpus with the same name. If `false`, the request fails if a corpus with
        the same name already exists. The parameter has no effect if a corpus with the
        same name does not already exist.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
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
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'add_corpus')
        headers.update(sdk_headers)

        params = {'allow_overwrite': allow_overwrite}

        form_data = {}
        form_data['corpus_file'] = (None, corpus_file, 'text/plain')

        url = '/v1/customizations/{0}/corpora/{1}'.format(
            *self._encode_path_vars(customization_id, corpus_name))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
            accept_json=True)
        return response

    def get_corpus(self, customization_id, corpus_name, **kwargs):
        """
        Get a corpus.

        Gets information about a corpus from a custom language model. The information
        includes the total number of words and out-of-vocabulary (OOV) words, name, and
        status of the corpus. You must use credentials for the instance of the service
        that owns a model to list its corpora.
        **See also:** [Listing corpora for a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageCorpora#listCorpora).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str corpus_name: The name of the corpus for the custom language model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if corpus_name is None:
            raise ValueError('corpus_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'get_corpus')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/corpora/{1}'.format(
            *self._encode_path_vars(customization_id, corpus_name))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def delete_corpus(self, customization_id, corpus_name, **kwargs):
        """
        Delete a corpus.

        Deletes an existing corpus from a custom language model. The service removes any
        out-of-vocabulary (OOV) words that are associated with the corpus from the custom
        model's words resource unless they were also added by another corpus or grammar,
        or they were modified in some way with the **Add custom words** or **Add a custom
        word** method. Removing a corpus does not affect the custom model until you train
        the model with the **Train a custom language model** method. You must use
        credentials for the instance of the service that owns a model to delete its
        corpora.
        **See also:** [Deleting a corpus from a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageCorpora#deleteCorpus).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str corpus_name: The name of the corpus for the custom language model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if corpus_name is None:
            raise ValueError('corpus_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'delete_corpus')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/corpora/{1}'.format(
            *self._encode_path_vars(customization_id, corpus_name))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # Custom words
    #########################

    def list_words(self, customization_id, word_type=None, sort=None, **kwargs):
        """
        List custom words.

        Lists information about custom words from a custom language model. You can list
        all words from the custom model's words resource, only custom words that were
        added or modified by the user, or only out-of-vocabulary (OOV) words that were
        extracted from corpora or are recognized by grammars. You can also indicate the
        order in which the service is to return words; by default, the service lists words
        in ascending alphabetical order. You must use credentials for the instance of the
        service that owns a model to list information about its words.
        **See also:** [Listing words from a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageWords#listWords).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str word_type: The type of words to be listed from the custom language
        model's words resource:
        * `all` (the default) shows all words.
        * `user` shows only custom words that were added or modified by the user directly.
        * `corpora` shows only OOV that were extracted from corpora.
        * `grammars` shows only OOV words that are recognized by grammars.
        :param str sort: Indicates the order in which the words are to be listed,
        `alphabetical` or by `count`. You can prepend an optional `+` or `-` to an
        argument to indicate whether the results are to be sorted in ascending or
        descending order. By default, words are sorted in ascending alphabetical order.
        For alphabetical ordering, the lexicographical precedence is numeric values,
        uppercase letters, and lowercase letters. For count ordering, values with the same
        count are ordered alphabetically. With the `curl` command, URL-encode the `+`
        symbol as `%2B`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'list_words')
        headers.update(sdk_headers)

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

    def add_words(self, customization_id, words, **kwargs):
        """
        Add custom words.

        Adds one or more custom words to a custom language model. The service populates
        the words resource for a custom model with out-of-vocabulary (OOV) words from each
        corpus or grammar that is added to the model. You can use this method to add
        additional words or to modify existing words in the words resource. The words
        resource for a model can contain a maximum of 90 thousand custom (OOV) words. This
        includes words that the service extracts from corpora and grammars and words that
        you add directly.
        You must use credentials for the instance of the service that owns a model to add
        or modify custom words for the model. Adding or modifying custom words does not
        affect the custom model until you train the model for the new data by using the
        **Train a custom language model** method.
        You add custom words by providing a `CustomWords` object, which is an array of
        `CustomWord` objects, one per word. You must use the object's `word` parameter to
        identify the word that is to be added. You can also provide one or both of the
        optional `sounds_like` and `display_as` fields for each word.
        * The `sounds_like` field provides an array of one or more pronunciations for the
        word. Use the parameter to specify how the word can be pronounced by users. Use
        the parameter for words that are difficult to pronounce, foreign words, acronyms,
        and so on. For example, you might specify that the word `IEEE` can sound like `i
        triple e`. You can specify a maximum of five sounds-like pronunciations for a
        word.
        * The `display_as` field provides a different way of spelling the word in a
        transcript. Use the parameter when you want the word to appear different from its
        usual representation or from its spelling in training data. For example, you might
        indicate that the word `IBM(trademark)` is to be displayed as `IBM&trade;`.
        If you add a custom word that already exists in the words resource for the custom
        model, the new definition overwrites the existing data for the word. If the
        service encounters an error with the input data, it returns a failure code and
        does not add any of the words to the words resource.
        The call returns an HTTP 201 response code if the input data is valid. It then
        asynchronously processes the words to add them to the model's words resource. The
        time that it takes for the analysis to complete depends on the number of new words
        that you add but is generally faster than adding a corpus or grammar.
        You can monitor the status of the request by using the **List a custom language
        model** method to poll the model's status. Use a loop to check the status every 10
        seconds. The method returns a `Customization` object that includes a `status`
        field. A status of `ready` means that the words have been added to the custom
        model. The service cannot accept requests to add new data or to train the model
        until the existing request completes.
        You can use the **List custom words** or **List a custom word** method to review
        the words that you add. Words with an invalid `sounds_like` field include an
        `error` field that describes the problem. You can use other words-related methods
        to correct errors, eliminate typos, and modify how words are pronounced as needed.
        **See also:**
        * [Working with custom
        words](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-corporaWords#workingWords)
        * [Add words to the custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-languageCreate#addWords).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param list[CustomWord] words: An array of `CustomWord` objects that provides
        information about each custom word that is to be added to or updated in the custom
        language model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if words is None:
            raise ValueError('words must be provided')
        words = [self._convert_model(x, CustomWord) for x in words]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'add_words')
        headers.update(sdk_headers)

        data = {'words': words}

        url = '/v1/customizations/{0}/words'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return response

    def add_word(self,
                 customization_id,
                 word_name,
                 word=None,
                 sounds_like=None,
                 display_as=None,
                 **kwargs):
        """
        Add a custom word.

        Adds a custom word to a custom language model. The service populates the words
        resource for a custom model with out-of-vocabulary (OOV) words from each corpus or
        grammar that is added to the model. You can use this method to add a word or to
        modify an existing word in the words resource. The words resource for a model can
        contain a maximum of 90 thousand custom (OOV) words. This includes words that the
        service extracts from corpora and grammars and words that you add directly.
        You must use credentials for the instance of the service that owns a model to add
        or modify a custom word for the model. Adding or modifying a custom word does not
        affect the custom model until you train the model for the new data by using the
        **Train a custom language model** method.
        Use the `word_name` parameter to specify the custom word that is to be added or
        modified. Use the `CustomWord` object to provide one or both of the optional
        `sounds_like` and `display_as` fields for the word.
        * The `sounds_like` field provides an array of one or more pronunciations for the
        word. Use the parameter to specify how the word can be pronounced by users. Use
        the parameter for words that are difficult to pronounce, foreign words, acronyms,
        and so on. For example, you might specify that the word `IEEE` can sound like `i
        triple e`. You can specify a maximum of five sounds-like pronunciations for a
        word.
        * The `display_as` field provides a different way of spelling the word in a
        transcript. Use the parameter when you want the word to appear different from its
        usual representation or from its spelling in training data. For example, you might
        indicate that the word `IBM(trademark)` is to be displayed as `IBM&trade;`.
        If you add a custom word that already exists in the words resource for the custom
        model, the new definition overwrites the existing data for the word. If the
        service encounters an error, it does not add the word to the words resource. Use
        the **List a custom word** method to review the word that you add.
        **See also:**
        * [Working with custom
        words](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-corporaWords#workingWords)
        * [Add words to the custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-languageCreate#addWords).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str word_name: The custom word that is to be added to or updated in the
        custom language model. Do not include spaces in the word. Use a `-` (dash) or `_`
        (underscore) to connect the tokens of compound words. URL-encode the word if it
        includes non-ASCII characters. For more information, see [Character
        encoding](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-corporaWords#charEncoding).
        :param str word: For the **Add custom words** method, you must specify the custom
        word that is to be added to or updated in the custom model. Do not include spaces
        in the word. Use a `-` (dash) or `_` (underscore) to connect the tokens of
        compound words.
        Omit this parameter for the **Add a custom word** method.
        :param list[str] sounds_like: An array of sounds-like pronunciations for the
        custom word. Specify how words that are difficult to pronounce, foreign words,
        acronyms, and so on can be pronounced by users.
        * For a word that is not in the service's base vocabulary, omit the parameter to
        have the service automatically generate a sounds-like pronunciation for the word.
        * For a word that is in the service's base vocabulary, use the parameter to
        specify additional pronunciations for the word. You cannot override the default
        pronunciation of a word; pronunciations you add augment the pronunciation from the
        base vocabulary.
        A word can have at most five sounds-like pronunciations. A pronunciation can
        include at most 40 characters not including spaces.
        :param str display_as: An alternative spelling for the custom word when it appears
        in a transcript. Use the parameter when you want the word to have a spelling that
        is different from its usual representation or from its spelling in corpora
        training data.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word_name is None:
            raise ValueError('word_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'add_word')
        headers.update(sdk_headers)

        data = {
            'word': word,
            'sounds_like': sounds_like,
            'display_as': display_as
        }

        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word_name))
        response = self.request(
            method='PUT', url=url, headers=headers, json=data, accept_json=True)
        return response

    def get_word(self, customization_id, word_name, **kwargs):
        """
        Get a custom word.

        Gets information about a custom word from a custom language model. You must use
        credentials for the instance of the service that owns a model to list information
        about its words.
        **See also:** [Listing words from a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageWords#listWords).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str word_name: The custom word that is to be read from the custom language
        model. URL-encode the word if it includes non-ASCII characters. For more
        information, see [Character
        encoding](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-corporaWords#charEncoding).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word_name is None:
            raise ValueError('word_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'get_word')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word_name))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def delete_word(self, customization_id, word_name, **kwargs):
        """
        Delete a custom word.

        Deletes a custom word from a custom language model. You can remove any word that
        you added to the custom model's words resource via any means. However, if the word
        also exists in the service's base vocabulary, the service removes only the custom
        pronunciation for the word; the word remains in the base vocabulary. Removing a
        custom word does not affect the custom model until you train the model with the
        **Train a custom language model** method. You must use credentials for the
        instance of the service that owns a model to delete its words.
        **See also:** [Deleting a word from a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageWords#deleteWord).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str word_name: The custom word that is to be deleted from the custom
        language model. URL-encode the word if it includes non-ASCII characters. For more
        information, see [Character
        encoding](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-corporaWords#charEncoding).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word_name is None:
            raise ValueError('word_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'delete_word')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word_name))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # Custom grammars
    #########################

    def list_grammars(self, customization_id, **kwargs):
        """
        List grammars.

        Lists information about all grammars from a custom language model. The information
        includes the total number of out-of-vocabulary (OOV) words, name, and status of
        each grammar. You must use credentials for the instance of the service that owns a
        model to list its grammars.
        **See also:** [Listing grammars from a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageGrammars#listGrammars).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'list_grammars')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/grammars'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def add_grammar(self,
                    customization_id,
                    grammar_name,
                    grammar_file,
                    content_type,
                    allow_overwrite=None,
                    **kwargs):
        """
        Add a grammar.

        Adds a single grammar file to a custom language model. Submit a plain text file in
        UTF-8 format that defines the grammar. Use multiple requests to submit multiple
        grammar files. You must use credentials for the instance of the service that owns
        a model to add a grammar to it. Adding a grammar does not affect the custom
        language model until you train the model for the new data by using the **Train a
        custom language model** method.
        The call returns an HTTP 201 response code if the grammar is valid. The service
        then asynchronously processes the contents of the grammar and automatically
        extracts new words that it finds. This can take a few seconds to complete
        depending on the size and complexity of the grammar, as well as the current load
        on the service. You cannot submit requests to add additional resources to the
        custom model or to train the model until the service's analysis of the grammar for
        the current request completes. Use the **Get a grammar** method to check the
        status of the analysis.
        The service populates the model's words resource with any word that is recognized
        by the grammar that is not found in the model's base vocabulary. These are
        referred to as out-of-vocabulary (OOV) words. You can use the **List custom
        words** method to examine the words resource and use other words-related methods
        to eliminate typos and modify how words are pronounced as needed.
        To add a grammar that has the same name as an existing grammar, set the
        `allow_overwrite` parameter to `true`; otherwise, the request fails. Overwriting
        an existing grammar causes the service to process the grammar file and extract OOV
        words anew. Before doing so, it removes any OOV words associated with the existing
        grammar from the model's words resource unless they were also added by another
        resource or they have been modified in some way with the **Add custom words** or
        **Add a custom word** method.
        The service limits the overall amount of data that you can add to a custom model
        to a maximum of 10 million total words from all sources combined. Also, you can
        add no more than 90 thousand OOV words to a model. This includes words that the
        service extracts from corpora and grammars and words that you add directly.
        **See also:**
        * [Understanding
        grammars](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-grammarUnderstand#grammarUnderstand)
        * [Add a grammar to the custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-grammarAdd#addGrammar).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str grammar_name: The name of the new grammar for the custom language
        model. Use a localized name that matches the language of the custom model and
        reflects the contents of the grammar.
        * Include a maximum of 128 characters in the name.
        * Do not use characters that need to be URL-encoded. For example, do not use
        spaces, slashes, backslashes, colons, ampersands, double quotes, plus signs,
        equals signs, questions marks, and so on in the name. (The service does not
        prevent the use of these characters. But because they must be URL-encoded wherever
        used, their use is strongly discouraged.)
        * Do not use the name of an existing grammar or corpus that is already defined for
        the custom model.
        * Do not use the name `user`, which is reserved by the service to denote custom
        words that are added or modified by the user.
        * Do not use the name `base_lm` or `default_lm`. Both names are reserved for
        future use by the service.
        :param str grammar_file: A plain text file that contains the grammar in the format
        specified by the `Content-Type` header. Encode the file in UTF-8 (ASCII is a
        subset of UTF-8). Using any other encoding can lead to issues when compiling the
        grammar or to unexpected results in decoding. The service ignores an encoding that
        is specified in the header of the grammar.
        With the `curl` command, use the `--data-binary` option to upload the file for the
        request.
        :param str content_type: The format (MIME type) of the grammar file:
        * `application/srgs` for Augmented Backus-Naur Form (ABNF), which uses a
        plain-text representation that is similar to traditional BNF grammars.
        * `application/srgs+xml` for XML Form, which uses XML elements to represent the
        grammar.
        :param bool allow_overwrite: If `true`, the specified grammar overwrites an
        existing grammar with the same name. If `false`, the request fails if a grammar
        with the same name already exists. The parameter has no effect if a grammar with
        the same name does not already exist.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if grammar_name is None:
            raise ValueError('grammar_name must be provided')
        if grammar_file is None:
            raise ValueError('grammar_file must be provided')
        if content_type is None:
            raise ValueError('content_type must be provided')

        headers = {'Content-Type': content_type}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'add_grammar')
        headers.update(sdk_headers)

        params = {'allow_overwrite': allow_overwrite}

        data = grammar_file

        url = '/v1/customizations/{0}/grammars/{1}'.format(
            *self._encode_path_vars(customization_id, grammar_name))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return response

    def get_grammar(self, customization_id, grammar_name, **kwargs):
        """
        Get a grammar.

        Gets information about a grammar from a custom language model. The information
        includes the total number of out-of-vocabulary (OOV) words, name, and status of
        the grammar. You must use credentials for the instance of the service that owns a
        model to list its grammars.
        **See also:** [Listing grammars from a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageGrammars#listGrammars).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str grammar_name: The name of the grammar for the custom language model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if grammar_name is None:
            raise ValueError('grammar_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'get_grammar')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/grammars/{1}'.format(
            *self._encode_path_vars(customization_id, grammar_name))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def delete_grammar(self, customization_id, grammar_name, **kwargs):
        """
        Delete a grammar.

        Deletes an existing grammar from a custom language model. The service removes any
        out-of-vocabulary (OOV) words associated with the grammar from the custom model's
        words resource unless they were also added by another resource or they were
        modified in some way with the **Add custom words** or **Add a custom word**
        method. Removing a grammar does not affect the custom model until you train the
        model with the **Train a custom language model** method. You must use credentials
        for the instance of the service that owns a model to delete its grammar.
        **See also:** [Deleting a grammar from a custom language
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageGrammars#deleteGrammar).

        :param str customization_id: The customization ID (GUID) of the custom language
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str grammar_name: The name of the grammar for the custom language model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if grammar_name is None:
            raise ValueError('grammar_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'delete_grammar')
        headers.update(sdk_headers)

        url = '/v1/customizations/{0}/grammars/{1}'.format(
            *self._encode_path_vars(customization_id, grammar_name))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # Custom acoustic models
    #########################

    def create_acoustic_model(self,
                              name,
                              base_model_name,
                              description=None,
                              **kwargs):
        """
        Create a custom acoustic model.

        Creates a new custom acoustic model for a specified base model. The custom
        acoustic model can be used only with the base model for which it is created. The
        model is owned by the instance of the service whose credentials are used to create
        it.
        **See also:** [Create a custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-acoustic#createModel-acoustic).

        :param str name: A user-defined name for the new custom acoustic model. Use a name
        that is unique among all custom acoustic models that you own. Use a localized name
        that matches the language of the custom model. Use a name that describes the
        acoustic environment of the custom model, such as `Mobile custom model` or `Noisy
        car custom model`.
        :param str base_model_name: The name of the base language model that is to be
        customized by the new custom acoustic model. The new custom model can be used only
        with the base model that it customizes.
        To determine whether a base model supports acoustic model customization, refer to
        [Language support for
        customization](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-customization#languageSupport).
        :param str description: A description of the new custom acoustic model. Use a
        localized description that matches the language of the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')
        if base_model_name is None:
            raise ValueError('base_model_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'create_acoustic_model')
        headers.update(sdk_headers)

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

    def list_acoustic_models(self, language=None, **kwargs):
        """
        List custom acoustic models.

        Lists information about all custom acoustic models that are owned by an instance
        of the service. Use the `language` parameter to see all custom acoustic models for
        the specified language. Omit the parameter to see all custom acoustic models for
        all languages. You must use credentials for the instance of the service that owns
        a model to list information about it.
        **See also:** [Listing custom acoustic
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageAcousticModels#listModels-acoustic).

        :param str language: The identifier of the language for which custom language or
        custom acoustic models are to be returned (for example, `en-US`). Omit the
        parameter to see all custom language or custom acoustic models that are owned by
        the requesting credentials.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'list_acoustic_models')
        headers.update(sdk_headers)

        params = {'language': language}

        url = '/v1/acoustic_customizations'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_acoustic_model(self, customization_id, **kwargs):
        """
        Get a custom acoustic model.

        Gets information about a specified custom acoustic model. You must use credentials
        for the instance of the service that owns a model to list information about it.
        **See also:** [Listing custom acoustic
        models](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageAcousticModels#listModels-acoustic).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'get_acoustic_model')
        headers.update(sdk_headers)

        url = '/v1/acoustic_customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def delete_acoustic_model(self, customization_id, **kwargs):
        """
        Delete a custom acoustic model.

        Deletes an existing custom acoustic model. The custom model cannot be deleted if
        another request, such as adding an audio resource to the model, is currently being
        processed. You must use credentials for the instance of the service that owns a
        model to delete it.
        **See also:** [Deleting a custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageAcousticModels#deleteModel-acoustic).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'delete_acoustic_model')
        headers.update(sdk_headers)

        url = '/v1/acoustic_customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    def train_acoustic_model(self,
                             customization_id,
                             custom_language_model_id=None,
                             **kwargs):
        """
        Train a custom acoustic model.

        Initiates the training of a custom acoustic model with new or changed audio
        resources. After adding or deleting audio resources for a custom acoustic model,
        use this method to begin the actual training of the model on the latest audio
        data. The custom acoustic model does not reflect its changed data until you train
        it. You must use credentials for the instance of the service that owns a model to
        train it.
        The training method is asynchronous. It can take on the order of minutes or hours
        to complete depending on the total amount of audio data on which the custom
        acoustic model is being trained and the current load on the service. Typically,
        training a custom acoustic model takes approximately two to four times the length
        of its audio data. The range of time depends on the model being trained and the
        nature of the audio, such as whether the audio is clean or noisy. The method
        returns an HTTP 200 response code to indicate that the training process has begun.
        You can monitor the status of the training by using the **Get a custom acoustic
        model** method to poll the model's status. Use a loop to check the status once a
        minute. The method returns an `AcousticModel` object that includes `status` and
        `progress` fields. A status of `available` indicates that the custom model is
        trained and ready to use. The service cannot train a model while it is handling
        another request for the model. The service cannot accept subsequent training
        requests, or requests to add new audio resources, until the existing training
        request completes.
        You can use the optional `custom_language_model_id` parameter to specify the GUID
        of a separately created custom language model that is to be used during training.
        Train with a custom language model if you have verbatim transcriptions of the
        audio files that you have added to the custom model or you have either corpora
        (text files) or a list of words that are relevant to the contents of the audio
        files. Both of the custom models must be based on the same version of the same
        base model for training to succeed.
        **See also:**
        * [Train the custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-acoustic#trainModel-acoustic)
        * [Using custom acoustic and custom language models
        together](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-useBoth#useBoth)
        ### Training failures
         Training can fail to start for the following reasons:
        * The service is currently handling another request for the custom model, such as
        another training request or a request to add audio resources to the model.
        * The custom model contains less than 10 minutes or more than 200 hours of audio
        data.
        * You passed an incompatible custom language model with the
        `custom_language_model_id` query parameter. Both custom models must be based on
        the same version of the same base model.
        * The custom model contains one or more invalid audio resources. You can correct
        the invalid audio resources or set the `strict` parameter to `false` to exclude
        the invalid resources from the training. The model must contain at least one valid
        resource for training to succeed.

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str custom_language_model_id: The customization ID (GUID) of a custom
        language model that is to be used during training of the custom acoustic model.
        Specify a custom language model that has been trained with verbatim transcriptions
        of the audio resources or that contains words that are relevant to the contents of
        the audio resources. The custom language model must be based on the same version
        of the same base model as the custom acoustic model. The credentials specified
        with the request must own both custom models.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'train_acoustic_model')
        headers.update(sdk_headers)

        params = {'custom_language_model_id': custom_language_model_id}

        url = '/v1/acoustic_customizations/{0}/train'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def reset_acoustic_model(self, customization_id, **kwargs):
        """
        Reset a custom acoustic model.

        Resets a custom acoustic model by removing all audio resources from the model.
        Resetting a custom acoustic model initializes the model to its state when it was
        first created. Metadata such as the name and language of the model are preserved,
        but the model's audio resources are removed and must be re-created. The service
        cannot reset a model while it is handling another request for the model. The
        service cannot accept subsequent requests for the model until the existing reset
        request completes. You must use credentials for the instance of the service that
        owns a model to reset it.
        **See also:** [Resetting a custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageAcousticModels#resetModel-acoustic).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'reset_acoustic_model')
        headers.update(sdk_headers)

        url = '/v1/acoustic_customizations/{0}/reset'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST', url=url, headers=headers, accept_json=True)
        return response

    def upgrade_acoustic_model(self,
                               customization_id,
                               custom_language_model_id=None,
                               force=None,
                               **kwargs):
        """
        Upgrade a custom acoustic model.

        Initiates the upgrade of a custom acoustic model to the latest version of its base
        language model. The upgrade method is asynchronous. It can take on the order of
        minutes or hours to complete depending on the amount of data in the custom model
        and the current load on the service; typically, upgrade takes approximately twice
        the length of the total audio contained in the custom model. A custom model must
        be in the `ready` or `available` state to be upgraded. You must use credentials
        for the instance of the service that owns a model to upgrade it.
        The method returns an HTTP 200 response code to indicate that the upgrade process
        has begun successfully. You can monitor the status of the upgrade by using the
        **Get a custom acoustic model** method to poll the model's status. The method
        returns an `AcousticModel` object that includes `status` and `progress` fields.
        Use a loop to check the status once a minute. While it is being upgraded, the
        custom model has the status `upgrading`. When the upgrade is complete, the model
        resumes the status that it had prior to upgrade. The service cannot upgrade a
        model while it is handling another request for the model. The service cannot
        accept subsequent requests for the model until the existing upgrade request
        completes.
        If the custom acoustic model was trained with a separately created custom language
        model, you must use the `custom_language_model_id` parameter to specify the GUID
        of that custom language model. The custom language model must be upgraded before
        the custom acoustic model can be upgraded. Omit the parameter if the custom
        acoustic model was not trained with a custom language model.
        **See also:** [Upgrading a custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-customUpgrade#upgradeAcoustic).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str custom_language_model_id: If the custom acoustic model was trained with
        a custom language model, the customization ID (GUID) of that custom language
        model. The custom language model must be upgraded before the custom acoustic model
        can be upgraded. The credentials specified with the request must own both custom
        models.
        :param bool force: If `true`, forces the upgrade of a custom acoustic model for
        which no input data has been modified since it was last trained. Use this
        parameter only to force the upgrade of a custom acoustic model that is trained
        with a custom language model, and only if you receive a 400 response code and the
        message `No input data modified since last training`. See [Upgrading a custom
        acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-customUpgrade#upgradeAcoustic).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'upgrade_acoustic_model')
        headers.update(sdk_headers)

        params = {
            'custom_language_model_id': custom_language_model_id,
            'force': force
        }

        url = '/v1/acoustic_customizations/{0}/upgrade_model'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    #########################
    # Custom audio resources
    #########################

    def list_audio(self, customization_id, **kwargs):
        """
        List audio resources.

        Lists information about all audio resources from a custom acoustic model. The
        information includes the name of the resource and information about its audio
        data, such as its duration. It also includes the status of the audio resource,
        which is important for checking the service's analysis of the resource in response
        to a request to add it to the custom acoustic model. You must use credentials for
        the instance of the service that owns a model to list its audio resources.
        **See also:** [Listing audio resources for a custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageAudio#listAudio).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'list_audio')
        headers.update(sdk_headers)

        url = '/v1/acoustic_customizations/{0}/audio'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def add_audio(self,
                  customization_id,
                  audio_name,
                  audio_resource,
                  contained_content_type=None,
                  allow_overwrite=None,
                  content_type=None,
                  **kwargs):
        """
        Add an audio resource.

        Adds an audio resource to a custom acoustic model. Add audio content that reflects
        the acoustic characteristics of the audio that you plan to transcribe. You must
        use credentials for the instance of the service that owns a model to add an audio
        resource to it. Adding audio data does not affect the custom acoustic model until
        you train the model for the new data by using the **Train a custom acoustic
        model** method.
        You can add individual audio files or an archive file that contains multiple audio
        files. Adding multiple audio files via a single archive file is significantly more
        efficient than adding each file individually. You can add audio resources in any
        format that the service supports for speech recognition.
        You can use this method to add any number of audio resources to a custom model by
        calling the method once for each audio or archive file. You can add multiple
        different audio resources at the same time. You must add a minimum of 10 minutes
        and a maximum of 200 hours of audio that includes speech, not just silence, to a
        custom acoustic model before you can train it. No audio resource, audio- or
        archive-type, can be larger than 100 MB. To add an audio resource that has the
        same name as an existing audio resource, set the `allow_overwrite` parameter to
        `true`; otherwise, the request fails.
        The method is asynchronous. It can take several seconds to complete depending on
        the duration of the audio and, in the case of an archive file, the total number of
        audio files being processed. The service returns a 201 response code if the audio
        is valid. It then asynchronously analyzes the contents of the audio file or files
        and automatically extracts information about the audio such as its length,
        sampling rate, and encoding. You cannot submit requests to train or upgrade the
        model until the service's analysis of all audio resources for current requests
        completes.
        To determine the status of the service's analysis of the audio, use the **Get an
        audio resource** method to poll the status of the audio. The method accepts the
        customization ID of the custom model and the name of the audio resource, and it
        returns the status of the resource. Use a loop to check the status of the audio
        every few seconds until it becomes `ok`.
        **See also:** [Add audio to the custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-acoustic#addAudio).
        ### Content types for audio-type resources
         You can add an individual audio file in any format that the service supports for
        speech recognition. For an audio-type resource, use the `Content-Type` parameter
        to specify the audio format (MIME type) of the audio file, including specifying
        the sampling rate, channels, and endianness where indicated.
        * `audio/alaw` (Specify the sampling rate (`rate`) of the audio.)
        * `audio/basic` (Use only with narrowband models.)
        * `audio/flac`
        * `audio/g729` (Use only with narrowband models.)
        * `audio/l16` (Specify the sampling rate (`rate`) and optionally the number of
        channels (`channels`) and endianness (`endianness`) of the audio.)
        * `audio/mp3`
        * `audio/mpeg`
        * `audio/mulaw` (Specify the sampling rate (`rate`) of the audio.)
        * `audio/ogg` (The service automatically detects the codec of the input audio.)
        * `audio/ogg;codecs=opus`
        * `audio/ogg;codecs=vorbis`
        * `audio/wav` (Provide audio with a maximum of nine channels.)
        * `audio/webm` (The service automatically detects the codec of the input audio.)
        * `audio/webm;codecs=opus`
        * `audio/webm;codecs=vorbis`
        The sampling rate of an audio file must match the sampling rate of the base model
        for the custom model: for broadband models, at least 16 kHz; for narrowband
        models, at least 8 kHz. If the sampling rate of the audio is higher than the
        minimum required rate, the service down-samples the audio to the appropriate rate.
        If the sampling rate of the audio is lower than the minimum required rate, the
        service labels the audio file as `invalid`.
         **See also:** [Audio
        formats](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-audio-formats#audio-formats).
        ### Content types for archive-type resources
         You can add an archive file (**.zip** or **.tar.gz** file) that contains audio
        files in any format that the service supports for speech recognition. For an
        archive-type resource, use the `Content-Type` parameter to specify the media type
        of the archive file:
        * `application/zip` for a **.zip** file
        * `application/gzip` for a **.tar.gz** file.
        When you add an archive-type resource, the `Contained-Content-Type` header is
        optional depending on the format of the files that you are adding:
        * For audio files of type `audio/alaw`, `audio/basic`, `audio/l16`, or
        `audio/mulaw`, you must use the `Contained-Content-Type` header to specify the
        format of the contained audio files. Include the `rate`, `channels`, and
        `endianness` parameters where necessary. In this case, all audio files contained
        in the archive file must have the same audio format.
        * For audio files of all other types, you can omit the `Contained-Content-Type`
        header. In this case, the audio files contained in the archive file can have any
        of the formats not listed in the previous bullet. The audio files do not need to
        have the same format.
        Do not use the `Contained-Content-Type` header when adding an audio-type resource.
        ### Naming restrictions for embedded audio files
         The name of an audio file that is contained in an archive-type resource can
        include a maximum of 128 characters. This includes the file extension and all
        elements of the name (for example, slashes).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str audio_name: The name of the new audio resource for the custom acoustic
        model. Use a localized name that matches the language of the custom model and
        reflects the contents of the resource.
        * Include a maximum of 128 characters in the name.
        * Do not use characters that need to be URL-encoded. For example, do not use
        spaces, slashes, backslashes, colons, ampersands, double quotes, plus signs,
        equals signs, questions marks, and so on in the name. (The service does not
        prevent the use of these characters. But because they must be URL-encoded wherever
        used, their use is strongly discouraged.)
        * Do not use the name of an audio resource that has already been added to the
        custom model.
        :param file audio_resource: The audio resource that is to be added to the custom
        acoustic model, an individual audio file or an archive file.
        With the `curl` command, use the `--data-binary` option to upload the file for the
        request.
        :param str contained_content_type: **For an archive-type resource,** specify the
        format of the audio files that are contained in the archive file if they are of
        type `audio/alaw`, `audio/basic`, `audio/l16`, or `audio/mulaw`. Include the
        `rate`, `channels`, and `endianness` parameters where necessary. In this case, all
        audio files that are contained in the archive file must be of the indicated type.
        For all other audio formats, you can omit the header. In this case, the audio
        files can be of multiple types as long as they are not of the types listed in the
        previous paragraph.
        The parameter accepts all of the audio formats that are supported for use with
        speech recognition. For more information, see **Content types for audio-type
        resources** in the method description.
        **For an audio-type resource,** omit the header.
        :param bool allow_overwrite: If `true`, the specified audio resource overwrites an
        existing audio resource with the same name. If `false`, the request fails if an
        audio resource with the same name already exists. The parameter has no effect if
        an audio resource with the same name does not already exist.
        :param str content_type: For an audio-type resource, the format (MIME type) of the
        audio. For more information, see **Content types for audio-type resources** in the
        method description.
        For an archive-type resource, the media type of the archive file. For more
        information, see **Content types for archive-type resources** in the method
        description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if audio_name is None:
            raise ValueError('audio_name must be provided')
        if audio_resource is None:
            raise ValueError('audio_resource must be provided')

        headers = {
            'Contained-Content-Type': contained_content_type,
            'Content-Type': content_type
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'add_audio')
        headers.update(sdk_headers)

        params = {'allow_overwrite': allow_overwrite}

        data = audio_resource

        url = '/v1/acoustic_customizations/{0}/audio/{1}'.format(
            *self._encode_path_vars(customization_id, audio_name))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return response

    def get_audio(self, customization_id, audio_name, **kwargs):
        """
        Get an audio resource.

        Gets information about an audio resource from a custom acoustic model. The method
        returns an `AudioListing` object whose fields depend on the type of audio resource
        that you specify with the method's `audio_name` parameter:
        * **For an audio-type resource,** the object's fields match those of an
        `AudioResource` object: `duration`, `name`, `details`, and `status`.
        * **For an archive-type resource,** the object includes a `container` field whose
        fields match those of an `AudioResource` object. It also includes an `audio`
        field, which contains an array of `AudioResource` objects that provides
        information about the audio files that are contained in the archive.
        The information includes the status of the specified audio resource. The status is
        important for checking the service's analysis of a resource that you add to the
        custom model.
        * For an audio-type resource, the `status` field is located in the `AudioListing`
        object.
        * For an archive-type resource, the `status` field is located in the
        `AudioResource` object that is returned in the `container` field.
        You must use credentials for the instance of the service that owns a model to list
        its audio resources.
        **See also:** [Listing audio resources for a custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageAudio#listAudio).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str audio_name: The name of the audio resource for the custom acoustic
        model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if audio_name is None:
            raise ValueError('audio_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'get_audio')
        headers.update(sdk_headers)

        url = '/v1/acoustic_customizations/{0}/audio/{1}'.format(
            *self._encode_path_vars(customization_id, audio_name))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def delete_audio(self, customization_id, audio_name, **kwargs):
        """
        Delete an audio resource.

        Deletes an existing audio resource from a custom acoustic model. Deleting an
        archive-type audio resource removes the entire archive of files. The service does
        not allow deletion of individual files from an archive resource.
        Removing an audio resource does not affect the custom model until you train the
        model on its updated data by using the **Train a custom acoustic model** method.
        You can delete an existing audio resource from a model while a different resource
        is being added to the model. You must use credentials for the instance of the
        service that owns a model to delete its audio resources.
        **See also:** [Deleting an audio resource from a custom acoustic
        model](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-manageAudio#deleteAudio).

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model that is to be used for the request. You must make the request with
        credentials for the instance of the service that owns the custom model.
        :param str audio_name: The name of the audio resource for the custom acoustic
        model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if audio_name is None:
            raise ValueError('audio_name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1', 'delete_audio')
        headers.update(sdk_headers)

        url = '/v1/acoustic_customizations/{0}/audio/{1}'.format(
            *self._encode_path_vars(customization_id, audio_name))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(self, customer_id, **kwargs):
        """
        Delete labeled data.

        Deletes all data that is associated with a specified customer ID. The method
        deletes all data for the customer ID, regardless of the method by which the
        information was added. The method has no effect if no data is associated with the
        customer ID. You must issue the request with credentials for the same instance of
        the service that was used to associate the customer ID with the data.
        You associate a customer ID with data by passing the `X-Watson-Metadata` header
        with a request that passes the data.
        **See also:** [Information
        security](https://cloud.ibm.com/docs/services/speech-to-text?topic=speech-to-text-information-security#information-security).

        :param str customer_id: The customer ID for which all data is to be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customer_id is None:
            raise ValueError('customer_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('speech_to_text', 'V1',
                                      'delete_user_data')
        headers.update(sdk_headers)

        params = {'customer_id': customer_id}

        url = '/v1/user_data'
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=False)
        return response


##############################################################################
# Models
##############################################################################


class AcousticModel(object):
    """
    Information about an existing custom acoustic model.

    :attr str customization_id: The customization ID (GUID) of the custom acoustic model.
    The **Create a custom acoustic model** method returns only this field of the object;
    it does not return the other fields.
    :attr str created: (optional) The date and time in Coordinated Universal Time (UTC) at
    which the custom acoustic model was created. The value is provided in full ISO 8601
    format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str updated: (optional) The date and time in Coordinated Universal Time (UTC) at
    which the custom acoustic model was last modified. The `created` and `updated` fields
    are equal when an acoustic model is first added but has yet to be updated. The value
    is provided in full ISO 8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
    :attr str language: (optional) The language identifier of the custom acoustic model
    (for example, `en-US`).
    :attr list[str] versions: (optional) A list of the available versions of the custom
    acoustic model. Each element of the array indicates a version of the base model with
    which the custom model can be used. Multiple versions exist only if the custom model
    has been upgraded; otherwise, only a single version is shown.
    :attr str owner: (optional) The GUID of the credentials for the instance of the
    service that owns the custom acoustic model.
    :attr str name: (optional) The name of the custom acoustic model.
    :attr str description: (optional) The description of the custom acoustic model.
    :attr str base_model_name: (optional) The name of the language model for which the
    custom acoustic model was created.
    :attr str status: (optional) The current status of the custom acoustic model:
    * `pending`: The model was created but is waiting either for valid training data to be
    added or for the service to finish analyzing added data.
    * `ready`: The model contains valid data and is ready to be trained. If the model
    contains a mix of valid and invalid resources, you need to set the `strict` parameter
    to `false` for the training to proceed.
    * `training`: The model is currently being trained.
    * `available`: The model is trained and ready to use.
    * `upgrading`: The model is currently being upgraded.
    * `failed`: Training of the model failed.
    :attr int progress: (optional) A percentage that indicates the progress of the custom
    acoustic model's current training. A value of `100` means that the model is fully
    trained. **Note:** The `progress` field does not currently reflect the progress of the
    training. The field changes from `0` to `100` when training is complete.
    :attr str warnings: (optional) If the request included unknown parameters, the
    following message: `Unexpected query parameter(s) ['parameters'] detected`, where
    `parameters` is a list that includes a quoted string for each unknown parameter.
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
                 warnings=None,
                 updated=None):
        """
        Initialize a AcousticModel object.

        :param str customization_id: The customization ID (GUID) of the custom acoustic
        model. The **Create a custom acoustic model** method returns only this field of
        the object; it does not return the other fields.
        :param str created: (optional) The date and time in Coordinated Universal Time
        (UTC) at which the custom acoustic model was created. The value is provided in
        full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str updated: (optional) The date and time in Coordinated Universal Time
        (UTC) at which the custom acoustic model was last modified. The `created` and
        `updated` fields are equal when an acoustic model is first added but has yet to be
        updated. The value is provided in full ISO 8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
        :param str language: (optional) The language identifier of the custom acoustic
        model (for example, `en-US`).
        :param list[str] versions: (optional) A list of the available versions of the
        custom acoustic model. Each element of the array indicates a version of the base
        model with which the custom model can be used. Multiple versions exist only if the
        custom model has been upgraded; otherwise, only a single version is shown.
        :param str owner: (optional) The GUID of the credentials for the instance of the
        service that owns the custom acoustic model.
        :param str name: (optional) The name of the custom acoustic model.
        :param str description: (optional) The description of the custom acoustic model.
        :param str base_model_name: (optional) The name of the language model for which
        the custom acoustic model was created.
        :param str status: (optional) The current status of the custom acoustic model:
        * `pending`: The model was created but is waiting either for valid training data
        to be added or for the service to finish analyzing added data.
        * `ready`: The model contains valid data and is ready to be trained. If the model
        contains a mix of valid and invalid resources, you need to set the `strict`
        parameter to `false` for the training to proceed.
        * `training`: The model is currently being trained.
        * `available`: The model is trained and ready to use.
        * `upgrading`: The model is currently being upgraded.
        * `failed`: Training of the model failed.
        :param int progress: (optional) A percentage that indicates the progress of the
        custom acoustic model's current training. A value of `100` means that the model is
        fully trained. **Note:** The `progress` field does not currently reflect the
        progress of the training. The field changes from `0` to `100` when training is
        complete.
        :param str warnings: (optional) If the request included unknown parameters, the
        following message: `Unexpected query parameter(s) ['parameters'] detected`, where
        `parameters` is a list that includes a quoted string for each unknown parameter.
        """
        self.customization_id = customization_id
        self.created = created
        self.updated = updated
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
        validKeys = [
            'customization_id', 'created', 'updated', 'language', 'versions',
            'owner', 'name', 'description', 'base_model_name', 'status',
            'progress', 'warnings'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AcousticModel: '
                + ', '.join(badKeys))
        if 'customization_id' in _dict:
            args['customization_id'] = _dict.get('customization_id')
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in AcousticModel JSON'
            )
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'updated' in _dict:
            args['updated'] = _dict.get('updated')
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
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = self.updated
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
    Information about existing custom acoustic models.

    :attr list[AcousticModel] customizations: An array of `AcousticModel` objects that
    provides information about each available custom acoustic model. The array is empty if
    the requesting credentials own no custom acoustic models (if no language is specified)
    or own no custom acoustic models for the specified language.
    """

    def __init__(self, customizations):
        """
        Initialize a AcousticModels object.

        :param list[AcousticModel] customizations: An array of `AcousticModel` objects
        that provides information about each available custom acoustic model. The array is
        empty if the requesting credentials own no custom acoustic models (if no language
        is specified) or own no custom acoustic models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AcousticModels object from a json dictionary."""
        args = {}
        validKeys = ['customizations']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AcousticModels: '
                + ', '.join(badKeys))
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
    Information about an audio resource from a custom acoustic model.

    :attr str type: (optional) The type of the audio resource:
    * `audio` for an individual audio file
    * `archive` for an archive (**.zip** or **.tar.gz**) file that contains audio files
    * `undetermined` for a resource that the service cannot validate (for example, if the
    user mistakenly passes a file that does not contain audio, such as a JPEG file).
    :attr str codec: (optional) **For an audio-type resource,** the codec in which the
    audio is encoded. Omitted for an archive-type resource.
    :attr int frequency: (optional) **For an audio-type resource,** the sampling rate of
    the audio in Hertz (samples per second). Omitted for an archive-type resource.
    :attr str compression: (optional) **For an archive-type resource,** the format of the
    compressed archive:
    * `zip` for a **.zip** file
    * `gzip` for a **.tar.gz** file
    Omitted for an audio-type resource.
    """

    def __init__(self, type=None, codec=None, frequency=None, compression=None):
        """
        Initialize a AudioDetails object.

        :param str type: (optional) The type of the audio resource:
        * `audio` for an individual audio file
        * `archive` for an archive (**.zip** or **.tar.gz**) file that contains audio
        files
        * `undetermined` for a resource that the service cannot validate (for example, if
        the user mistakenly passes a file that does not contain audio, such as a JPEG
        file).
        :param str codec: (optional) **For an audio-type resource,** the codec in which
        the audio is encoded. Omitted for an archive-type resource.
        :param int frequency: (optional) **For an audio-type resource,** the sampling rate
        of the audio in Hertz (samples per second). Omitted for an archive-type resource.
        :param str compression: (optional) **For an archive-type resource,** the format of
        the compressed archive:
        * `zip` for a **.zip** file
        * `gzip` for a **.tar.gz** file
        Omitted for an audio-type resource.
        """
        self.type = type
        self.codec = codec
        self.frequency = frequency
        self.compression = compression

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioDetails object from a json dictionary."""
        args = {}
        validKeys = ['type', 'codec', 'frequency', 'compression']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AudioDetails: '
                + ', '.join(badKeys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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
    Information about an audio resource from a custom acoustic model.

    :attr int duration: (optional) **For an audio-type resource,**  the total seconds of
    audio in the resource. Omitted for an archive-type resource.
    :attr str name: (optional) **For an audio-type resource,** the user-specified name of
    the resource. Omitted for an archive-type resource.
    :attr AudioDetails details: (optional) **For an audio-type resource,** an
    `AudioDetails` object that provides detailed information about the resource. The
    object is empty until the service finishes processing the audio. Omitted for an
    archive-type resource.
    :attr str status: (optional) **For an audio-type resource,** the status of the
    resource:
    * `ok`: The service successfully analyzed the audio data. The data can be used to
    train the custom model.
    * `being_processed`: The service is still analyzing the audio data. The service cannot
    accept requests to add new audio resources or to train the custom model until its
    analysis is complete.
    * `invalid`: The audio data is not valid for training the custom model (possibly
    because it has the wrong format or sampling rate, or because it is corrupted).
    Omitted for an archive-type resource.
    :attr AudioResource container: (optional) **For an archive-type resource,** an object
    of type `AudioResource` that provides information about the resource. Omitted for an
    audio-type resource.
    :attr list[AudioResource] audio: (optional) **For an archive-type resource,** an array
    of `AudioResource` objects that provides information about the audio-type resources
    that are contained in the resource. Omitted for an audio-type resource.
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

        :param int duration: (optional) **For an audio-type resource,**  the total seconds
        of audio in the resource. Omitted for an archive-type resource.
        :param str name: (optional) **For an audio-type resource,** the user-specified
        name of the resource. Omitted for an archive-type resource.
        :param AudioDetails details: (optional) **For an audio-type resource,** an
        `AudioDetails` object that provides detailed information about the resource. The
        object is empty until the service finishes processing the audio. Omitted for an
        archive-type resource.
        :param str status: (optional) **For an audio-type resource,** the status of the
        resource:
        * `ok`: The service successfully analyzed the audio data. The data can be used to
        train the custom model.
        * `being_processed`: The service is still analyzing the audio data. The service
        cannot accept requests to add new audio resources or to train the custom model
        until its analysis is complete.
        * `invalid`: The audio data is not valid for training the custom model (possibly
        because it has the wrong format or sampling rate, or because it is corrupted).
        Omitted for an archive-type resource.
        :param AudioResource container: (optional) **For an archive-type resource,** an
        object of type `AudioResource` that provides information about the resource.
        Omitted for an audio-type resource.
        :param list[AudioResource] audio: (optional) **For an archive-type resource,** an
        array of `AudioResource` objects that provides information about the audio-type
        resources that are contained in the resource. Omitted for an audio-type resource.
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
        validKeys = [
            'duration', 'name', 'details', 'status', 'container', 'audio'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AudioListing: '
                + ', '.join(badKeys))
        if 'duration' in _dict:
            args['duration'] = _dict.get('duration')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'details' in _dict:
            args['details'] = AudioDetails._from_dict(_dict.get('details'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'container' in _dict:
            args['container'] = AudioResource._from_dict(_dict.get('container'))
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


class AudioMetrics(object):
    """
    If audio metrics are requested, information about the signal characteristics of the
    input audio.

    :attr float sampling_interval: The interval in seconds (typically 0.1 seconds) at
    which the service calculated the audio metrics. In other words, how often the service
    calculated the metrics. A single unit in each histogram (see the
    `AudioMetricsHistogramBin` object) is calculated based on a `sampling_interval` length
    of audio.
    :attr AudioMetricsDetails accumulated: Detailed information about the signal
    characteristics of the input audio.
    """

    def __init__(self, sampling_interval, accumulated):
        """
        Initialize a AudioMetrics object.

        :param float sampling_interval: The interval in seconds (typically 0.1 seconds) at
        which the service calculated the audio metrics. In other words, how often the
        service calculated the metrics. A single unit in each histogram (see the
        `AudioMetricsHistogramBin` object) is calculated based on a `sampling_interval`
        length of audio.
        :param AudioMetricsDetails accumulated: Detailed information about the signal
        characteristics of the input audio.
        """
        self.sampling_interval = sampling_interval
        self.accumulated = accumulated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioMetrics object from a json dictionary."""
        args = {}
        validKeys = ['sampling_interval', 'accumulated']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AudioMetrics: '
                + ', '.join(badKeys))
        if 'sampling_interval' in _dict:
            args['sampling_interval'] = _dict.get('sampling_interval')
        else:
            raise ValueError(
                'Required property \'sampling_interval\' not present in AudioMetrics JSON'
            )
        if 'accumulated' in _dict:
            args['accumulated'] = AudioMetricsDetails._from_dict(
                _dict.get('accumulated'))
        else:
            raise ValueError(
                'Required property \'accumulated\' not present in AudioMetrics JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'sampling_interval') and self.sampling_interval is not None:
            _dict['sampling_interval'] = self.sampling_interval
        if hasattr(self, 'accumulated') and self.accumulated is not None:
            _dict['accumulated'] = self.accumulated._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this AudioMetrics object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioMetricsDetails(object):
    """
    Detailed information about the signal characteristics of the input audio.

    :attr bool final: If `true`, indicates the end of the audio stream, meaning that
    transcription is complete. Currently, the field is always `true`. The service returns
    metrics just once per audio stream. The results provide aggregated audio metrics that
    pertain to the complete audio stream.
    :attr float end_time: The end time in seconds of the block of audio to which the
    metrics apply.
    :attr float signal_to_noise_ratio: (optional) The signal-to-noise ratio (SNR) for the
    audio signal. The value indicates the ratio of speech to noise in the audio. A valid
    value lies in the range of 0 to 100 decibels (dB). The service omits the field if it
    cannot compute the SNR for the audio.
    :attr float speech_ratio: The ratio of speech to non-speech segments in the audio
    signal. The value lies in the range of 0.0 to 1.0.
    :attr float high_frequency_loss: The probability that the audio signal is missing the
    upper half of its frequency content.
    * A value close to 1.0 typically indicates artificially up-sampled audio, which
    negatively impacts the accuracy of the transcription results.
    * A value at or near 0.0 indicates that the audio signal is good and has a full
    spectrum.
    * A value around 0.5 means that detection of the frequency content is unreliable or
    not available.
    :attr list[AudioMetricsHistogramBin] direct_current_offset: An array of
    `AudioMetricsHistogramBin` objects that defines a histogram of the cumulative direct
    current (DC) component of the audio signal.
    :attr list[AudioMetricsHistogramBin] clipping_rate: An array of
    `AudioMetricsHistogramBin` objects that defines a histogram of the clipping rate for
    the audio segments. The clipping rate is defined as the fraction of samples in the
    segment that reach the maximum or minimum value that is offered by the audio
    quantization range. The service auto-detects either a 16-bit Pulse-Code
    Modulation(PCM) audio range (-32768 to +32767) or a unit range (-1.0 to +1.0). The
    clipping rate is between 0.0 and 1.0, with higher values indicating possible
    degradation of speech recognition.
    :attr list[AudioMetricsHistogramBin] speech_level: An array of
    `AudioMetricsHistogramBin` objects that defines a histogram of the signal level in
    segments of the audio that contain speech. The signal level is computed as the
    Root-Mean-Square (RMS) value in a decibel (dB) scale normalized to the range 0.0
    (minimum level) to 1.0 (maximum level).
    :attr list[AudioMetricsHistogramBin] non_speech_level: An array of
    `AudioMetricsHistogramBin` objects that defines a histogram of the signal level in
    segments of the audio that do not contain speech. The signal level is computed as the
    Root-Mean-Square (RMS) value in a decibel (dB) scale normalized to the range 0.0
    (minimum level) to 1.0 (maximum level).
    """

    def __init__(self,
                 final,
                 end_time,
                 speech_ratio,
                 high_frequency_loss,
                 direct_current_offset,
                 clipping_rate,
                 speech_level,
                 non_speech_level,
                 signal_to_noise_ratio=None):
        """
        Initialize a AudioMetricsDetails object.

        :param bool final: If `true`, indicates the end of the audio stream, meaning that
        transcription is complete. Currently, the field is always `true`. The service
        returns metrics just once per audio stream. The results provide aggregated audio
        metrics that pertain to the complete audio stream.
        :param float end_time: The end time in seconds of the block of audio to which the
        metrics apply.
        :param float speech_ratio: The ratio of speech to non-speech segments in the audio
        signal. The value lies in the range of 0.0 to 1.0.
        :param float high_frequency_loss: The probability that the audio signal is missing
        the upper half of its frequency content.
        * A value close to 1.0 typically indicates artificially up-sampled audio, which
        negatively impacts the accuracy of the transcription results.
        * A value at or near 0.0 indicates that the audio signal is good and has a full
        spectrum.
        * A value around 0.5 means that detection of the frequency content is unreliable
        or not available.
        :param list[AudioMetricsHistogramBin] direct_current_offset: An array of
        `AudioMetricsHistogramBin` objects that defines a histogram of the cumulative
        direct current (DC) component of the audio signal.
        :param list[AudioMetricsHistogramBin] clipping_rate: An array of
        `AudioMetricsHistogramBin` objects that defines a histogram of the clipping rate
        for the audio segments. The clipping rate is defined as the fraction of samples in
        the segment that reach the maximum or minimum value that is offered by the audio
        quantization range. The service auto-detects either a 16-bit Pulse-Code
        Modulation(PCM) audio range (-32768 to +32767) or a unit range (-1.0 to +1.0). The
        clipping rate is between 0.0 and 1.0, with higher values indicating possible
        degradation of speech recognition.
        :param list[AudioMetricsHistogramBin] speech_level: An array of
        `AudioMetricsHistogramBin` objects that defines a histogram of the signal level in
        segments of the audio that contain speech. The signal level is computed as the
        Root-Mean-Square (RMS) value in a decibel (dB) scale normalized to the range 0.0
        (minimum level) to 1.0 (maximum level).
        :param list[AudioMetricsHistogramBin] non_speech_level: An array of
        `AudioMetricsHistogramBin` objects that defines a histogram of the signal level in
        segments of the audio that do not contain speech. The signal level is computed as
        the Root-Mean-Square (RMS) value in a decibel (dB) scale normalized to the range
        0.0 (minimum level) to 1.0 (maximum level).
        :param float signal_to_noise_ratio: (optional) The signal-to-noise ratio (SNR) for
        the audio signal. The value indicates the ratio of speech to noise in the audio. A
        valid value lies in the range of 0 to 100 decibels (dB). The service omits the
        field if it cannot compute the SNR for the audio.
        """
        self.final = final
        self.end_time = end_time
        self.signal_to_noise_ratio = signal_to_noise_ratio
        self.speech_ratio = speech_ratio
        self.high_frequency_loss = high_frequency_loss
        self.direct_current_offset = direct_current_offset
        self.clipping_rate = clipping_rate
        self.speech_level = speech_level
        self.non_speech_level = non_speech_level

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioMetricsDetails object from a json dictionary."""
        args = {}
        validKeys = [
            'final', 'end_time', 'signal_to_noise_ratio', 'speech_ratio',
            'high_frequency_loss', 'direct_current_offset', 'clipping_rate',
            'speech_level', 'non_speech_level'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AudioMetricsDetails: '
                + ', '.join(badKeys))
        if 'final' in _dict:
            args['final'] = _dict.get('final')
        else:
            raise ValueError(
                'Required property \'final\' not present in AudioMetricsDetails JSON'
            )
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        else:
            raise ValueError(
                'Required property \'end_time\' not present in AudioMetricsDetails JSON'
            )
        if 'signal_to_noise_ratio' in _dict:
            args['signal_to_noise_ratio'] = _dict.get('signal_to_noise_ratio')
        if 'speech_ratio' in _dict:
            args['speech_ratio'] = _dict.get('speech_ratio')
        else:
            raise ValueError(
                'Required property \'speech_ratio\' not present in AudioMetricsDetails JSON'
            )
        if 'high_frequency_loss' in _dict:
            args['high_frequency_loss'] = _dict.get('high_frequency_loss')
        else:
            raise ValueError(
                'Required property \'high_frequency_loss\' not present in AudioMetricsDetails JSON'
            )
        if 'direct_current_offset' in _dict:
            args['direct_current_offset'] = [
                AudioMetricsHistogramBin._from_dict(x)
                for x in (_dict.get('direct_current_offset'))
            ]
        else:
            raise ValueError(
                'Required property \'direct_current_offset\' not present in AudioMetricsDetails JSON'
            )
        if 'clipping_rate' in _dict:
            args['clipping_rate'] = [
                AudioMetricsHistogramBin._from_dict(x)
                for x in (_dict.get('clipping_rate'))
            ]
        else:
            raise ValueError(
                'Required property \'clipping_rate\' not present in AudioMetricsDetails JSON'
            )
        if 'speech_level' in _dict:
            args['speech_level'] = [
                AudioMetricsHistogramBin._from_dict(x)
                for x in (_dict.get('speech_level'))
            ]
        else:
            raise ValueError(
                'Required property \'speech_level\' not present in AudioMetricsDetails JSON'
            )
        if 'non_speech_level' in _dict:
            args['non_speech_level'] = [
                AudioMetricsHistogramBin._from_dict(x)
                for x in (_dict.get('non_speech_level'))
            ]
        else:
            raise ValueError(
                'Required property \'non_speech_level\' not present in AudioMetricsDetails JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'final') and self.final is not None:
            _dict['final'] = self.final
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'signal_to_noise_ratio'
                  ) and self.signal_to_noise_ratio is not None:
            _dict['signal_to_noise_ratio'] = self.signal_to_noise_ratio
        if hasattr(self, 'speech_ratio') and self.speech_ratio is not None:
            _dict['speech_ratio'] = self.speech_ratio
        if hasattr(
                self,
                'high_frequency_loss') and self.high_frequency_loss is not None:
            _dict['high_frequency_loss'] = self.high_frequency_loss
        if hasattr(self, 'direct_current_offset'
                  ) and self.direct_current_offset is not None:
            _dict['direct_current_offset'] = [
                x._to_dict() for x in self.direct_current_offset
            ]
        if hasattr(self, 'clipping_rate') and self.clipping_rate is not None:
            _dict['clipping_rate'] = [x._to_dict() for x in self.clipping_rate]
        if hasattr(self, 'speech_level') and self.speech_level is not None:
            _dict['speech_level'] = [x._to_dict() for x in self.speech_level]
        if hasattr(self,
                   'non_speech_level') and self.non_speech_level is not None:
            _dict['non_speech_level'] = [
                x._to_dict() for x in self.non_speech_level
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this AudioMetricsDetails object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioMetricsHistogramBin(object):
    """
    A bin with defined boundaries that indicates the number of values in a range of signal
    characteristics for a histogram. The first and last bins of a histogram are the
    boundary bins. They cover the intervals between negative infinity and the first
    boundary, and between the last boundary and positive infinity, respectively.

    :attr float begin: The lower boundary of the bin in the histogram.
    :attr float end: The upper boundary of the bin in the histogram.
    :attr int count: The number of values in the bin of the histogram.
    """

    def __init__(self, begin, end, count):
        """
        Initialize a AudioMetricsHistogramBin object.

        :param float begin: The lower boundary of the bin in the histogram.
        :param float end: The upper boundary of the bin in the histogram.
        :param int count: The number of values in the bin of the histogram.
        """
        self.begin = begin
        self.end = end
        self.count = count

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioMetricsHistogramBin object from a json dictionary."""
        args = {}
        validKeys = ['begin', 'end', 'count']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AudioMetricsHistogramBin: '
                + ', '.join(badKeys))
        if 'begin' in _dict:
            args['begin'] = _dict.get('begin')
        else:
            raise ValueError(
                'Required property \'begin\' not present in AudioMetricsHistogramBin JSON'
            )
        if 'end' in _dict:
            args['end'] = _dict.get('end')
        else:
            raise ValueError(
                'Required property \'end\' not present in AudioMetricsHistogramBin JSON'
            )
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError(
                'Required property \'count\' not present in AudioMetricsHistogramBin JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def __str__(self):
        """Return a `str` version of this AudioMetricsHistogramBin object."""
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
    Information about an audio resource from a custom acoustic model.

    :attr int duration: The total seconds of audio in the audio resource.
    :attr str name: **For an archive-type resource,** the user-specified name of the
    resource.
    **For an audio-type resource,** the user-specified name of the resource or the name of
    the audio file that the user added for the resource. The value depends on the method
    that is called.
    :attr AudioDetails details: An `AudioDetails` object that provides detailed
    information about the audio resource. The object is empty until the service finishes
    processing the audio.
    :attr str status: The status of the audio resource:
    * `ok`: The service successfully analyzed the audio data. The data can be used to
    train the custom model.
    * `being_processed`: The service is still analyzing the audio data. The service cannot
    accept requests to add new audio resources or to train the custom model until its
    analysis is complete.
    * `invalid`: The audio data is not valid for training the custom model (possibly
    because it has the wrong format or sampling rate, or because it is corrupted). For an
    archive file, the entire archive is invalid if any of its audio files are invalid.
    """

    def __init__(self, duration, name, details, status):
        """
        Initialize a AudioResource object.

        :param int duration: The total seconds of audio in the audio resource.
        :param str name: **For an archive-type resource,** the user-specified name of the
        resource.
        **For an audio-type resource,** the user-specified name of the resource or the
        name of the audio file that the user added for the resource. The value depends on
        the method that is called.
        :param AudioDetails details: An `AudioDetails` object that provides detailed
        information about the audio resource. The object is empty until the service
        finishes processing the audio.
        :param str status: The status of the audio resource:
        * `ok`: The service successfully analyzed the audio data. The data can be used to
        train the custom model.
        * `being_processed`: The service is still analyzing the audio data. The service
        cannot accept requests to add new audio resources or to train the custom model
        until its analysis is complete.
        * `invalid`: The audio data is not valid for training the custom model (possibly
        because it has the wrong format or sampling rate, or because it is corrupted). For
        an archive file, the entire archive is invalid if any of its audio files are
        invalid.
        """
        self.duration = duration
        self.name = name
        self.details = details
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioResource object from a json dictionary."""
        args = {}
        validKeys = ['duration', 'name', 'details', 'status']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AudioResource: '
                + ', '.join(badKeys))
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
    Information about the audio resources from a custom acoustic model.

    :attr float total_minutes_of_audio: The total minutes of accumulated audio summed over
    all of the valid audio resources for the custom acoustic model. You can use this value
    to determine whether the custom model has too little or too much audio to begin
    training.
    :attr list[AudioResource] audio: An array of `AudioResource` objects that provides
    information about the audio resources of the custom acoustic model. The array is empty
    if the custom model has no audio resources.
    """

    def __init__(self, total_minutes_of_audio, audio):
        """
        Initialize a AudioResources object.

        :param float total_minutes_of_audio: The total minutes of accumulated audio summed
        over all of the valid audio resources for the custom acoustic model. You can use
        this value to determine whether the custom model has too little or too much audio
        to begin training.
        :param list[AudioResource] audio: An array of `AudioResource` objects that
        provides information about the audio resources of the custom acoustic model. The
        array is empty if the custom model has no audio resources.
        """
        self.total_minutes_of_audio = total_minutes_of_audio
        self.audio = audio

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioResources object from a json dictionary."""
        args = {}
        validKeys = ['total_minutes_of_audio', 'audio']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AudioResources: '
                + ', '.join(badKeys))
        if 'total_minutes_of_audio' in _dict:
            args['total_minutes_of_audio'] = _dict.get('total_minutes_of_audio')
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
        if hasattr(self, 'total_minutes_of_audio'
                  ) and self.total_minutes_of_audio is not None:
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
    Information about the corpora from a custom language model.

    :attr list[Corpus] corpora: An array of `Corpus` objects that provides information
    about the corpora for the custom model. The array is empty if the custom model has no
    corpora.
    """

    def __init__(self, corpora):
        """
        Initialize a Corpora object.

        :param list[Corpus] corpora: An array of `Corpus` objects that provides
        information about the corpora for the custom model. The array is empty if the
        custom model has no corpora.
        """
        self.corpora = corpora

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Corpora object from a json dictionary."""
        args = {}
        validKeys = ['corpora']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Corpora: ' +
                ', '.join(badKeys))
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
    Information about a corpus from a custom language model.

    :attr str name: The name of the corpus.
    :attr int total_words: The total number of words in the corpus. The value is `0` while
    the corpus is being processed.
    :attr int out_of_vocabulary_words: The number of OOV words in the corpus. The value is
    `0` while the corpus is being processed.
    :attr str status: The status of the corpus:
    * `analyzed`: The service successfully analyzed the corpus. The custom model can be
    trained with data from the corpus.
    * `being_processed`: The service is still analyzing the corpus. The service cannot
    accept requests to add new resources or to train the custom model.
    * `undetermined`: The service encountered an error while processing the corpus. The
    `error` field describes the failure.
    :attr str error: (optional) If the status of the corpus is `undetermined`, the
    following message: `Analysis of corpus 'name' failed. Please try adding the corpus
    again by setting the 'allow_overwrite' flag to 'true'`.
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
        :param int total_words: The total number of words in the corpus. The value is `0`
        while the corpus is being processed.
        :param int out_of_vocabulary_words: The number of OOV words in the corpus. The
        value is `0` while the corpus is being processed.
        :param str status: The status of the corpus:
        * `analyzed`: The service successfully analyzed the corpus. The custom model can
        be trained with data from the corpus.
        * `being_processed`: The service is still analyzing the corpus. The service cannot
        accept requests to add new resources or to train the custom model.
        * `undetermined`: The service encountered an error while processing the corpus.
        The `error` field describes the failure.
        :param str error: (optional) If the status of the corpus is `undetermined`, the
        following message: `Analysis of corpus 'name' failed. Please try adding the corpus
        again by setting the 'allow_overwrite' flag to 'true'`.
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
        validKeys = [
            'name', 'total_words', 'out_of_vocabulary_words', 'status', 'error'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Corpus: ' +
                ', '.join(badKeys))
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
        if hasattr(self, 'out_of_vocabulary_words'
                  ) and self.out_of_vocabulary_words is not None:
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
    Information about a word that is to be added to a custom language model.

    :attr str word: (optional) For the **Add custom words** method, you must specify the
    custom word that is to be added to or updated in the custom model. Do not include
    spaces in the word. Use a `-` (dash) or `_` (underscore) to connect the tokens of
    compound words.
    Omit this parameter for the **Add a custom word** method.
    :attr list[str] sounds_like: (optional) An array of sounds-like pronunciations for the
    custom word. Specify how words that are difficult to pronounce, foreign words,
    acronyms, and so on can be pronounced by users.
    * For a word that is not in the service's base vocabulary, omit the parameter to have
    the service automatically generate a sounds-like pronunciation for the word.
    * For a word that is in the service's base vocabulary, use the parameter to specify
    additional pronunciations for the word. You cannot override the default pronunciation
    of a word; pronunciations you add augment the pronunciation from the base vocabulary.
    A word can have at most five sounds-like pronunciations. A pronunciation can include
    at most 40 characters not including spaces.
    :attr str display_as: (optional) An alternative spelling for the custom word when it
    appears in a transcript. Use the parameter when you want the word to have a spelling
    that is different from its usual representation or from its spelling in corpora
    training data.
    """

    def __init__(self, word=None, sounds_like=None, display_as=None):
        """
        Initialize a CustomWord object.

        :param str word: (optional) For the **Add custom words** method, you must specify
        the custom word that is to be added to or updated in the custom model. Do not
        include spaces in the word. Use a `-` (dash) or `_` (underscore) to connect the
        tokens of compound words.
        Omit this parameter for the **Add a custom word** method.
        :param list[str] sounds_like: (optional) An array of sounds-like pronunciations
        for the custom word. Specify how words that are difficult to pronounce, foreign
        words, acronyms, and so on can be pronounced by users.
        * For a word that is not in the service's base vocabulary, omit the parameter to
        have the service automatically generate a sounds-like pronunciation for the word.
        * For a word that is in the service's base vocabulary, use the parameter to
        specify additional pronunciations for the word. You cannot override the default
        pronunciation of a word; pronunciations you add augment the pronunciation from the
        base vocabulary.
        A word can have at most five sounds-like pronunciations. A pronunciation can
        include at most 40 characters not including spaces.
        :param str display_as: (optional) An alternative spelling for the custom word when
        it appears in a transcript. Use the parameter when you want the word to have a
        spelling that is different from its usual representation or from its spelling in
        corpora training data.
        """
        self.word = word
        self.sounds_like = sounds_like
        self.display_as = display_as

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomWord object from a json dictionary."""
        args = {}
        validKeys = ['word', 'sounds_like', 'display_as']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CustomWord: '
                + ', '.join(badKeys))
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


class Grammar(object):
    """
    Information about a grammar from a custom language model.

    :attr str name: The name of the grammar.
    :attr int out_of_vocabulary_words: The number of OOV words in the grammar. The value
    is `0` while the grammar is being processed.
    :attr str status: The status of the grammar:
    * `analyzed`: The service successfully analyzed the grammar. The custom model can be
    trained with data from the grammar.
    * `being_processed`: The service is still analyzing the grammar. The service cannot
    accept requests to add new resources or to train the custom model.
    * `undetermined`: The service encountered an error while processing the grammar. The
    `error` field describes the failure.
    :attr str error: (optional) If the status of the grammar is `undetermined`, the
    following message: `Analysis of grammar '{grammar_name}' failed. Please try fixing the
    error or adding the grammar again by setting the 'allow_overwrite' flag to 'true'.`.
    """

    def __init__(self, name, out_of_vocabulary_words, status, error=None):
        """
        Initialize a Grammar object.

        :param str name: The name of the grammar.
        :param int out_of_vocabulary_words: The number of OOV words in the grammar. The
        value is `0` while the grammar is being processed.
        :param str status: The status of the grammar:
        * `analyzed`: The service successfully analyzed the grammar. The custom model can
        be trained with data from the grammar.
        * `being_processed`: The service is still analyzing the grammar. The service
        cannot accept requests to add new resources or to train the custom model.
        * `undetermined`: The service encountered an error while processing the grammar.
        The `error` field describes the failure.
        :param str error: (optional) If the status of the grammar is `undetermined`, the
        following message: `Analysis of grammar '{grammar_name}' failed. Please try fixing
        the error or adding the grammar again by setting the 'allow_overwrite' flag to
        'true'.`.
        """
        self.name = name
        self.out_of_vocabulary_words = out_of_vocabulary_words
        self.status = status
        self.error = error

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Grammar object from a json dictionary."""
        args = {}
        validKeys = ['name', 'out_of_vocabulary_words', 'status', 'error']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Grammar: ' +
                ', '.join(badKeys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Grammar JSON')
        if 'out_of_vocabulary_words' in _dict:
            args['out_of_vocabulary_words'] = _dict.get(
                'out_of_vocabulary_words')
        else:
            raise ValueError(
                'Required property \'out_of_vocabulary_words\' not present in Grammar JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in Grammar JSON')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'out_of_vocabulary_words'
                  ) and self.out_of_vocabulary_words is not None:
            _dict['out_of_vocabulary_words'] = self.out_of_vocabulary_words
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        return _dict

    def __str__(self):
        """Return a `str` version of this Grammar object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Grammars(object):
    """
    Information about the grammars from a custom language model.

    :attr list[Grammar] grammars: An array of `Grammar` objects that provides information
    about the grammars for the custom model. The array is empty if the custom model has no
    grammars.
    """

    def __init__(self, grammars):
        """
        Initialize a Grammars object.

        :param list[Grammar] grammars: An array of `Grammar` objects that provides
        information about the grammars for the custom model. The array is empty if the
        custom model has no grammars.
        """
        self.grammars = grammars

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Grammars object from a json dictionary."""
        args = {}
        validKeys = ['grammars']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Grammars: '
                + ', '.join(badKeys))
        if 'grammars' in _dict:
            args['grammars'] = [
                Grammar._from_dict(x) for x in (_dict.get('grammars'))
            ]
        else:
            raise ValueError(
                'Required property \'grammars\' not present in Grammars JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'grammars') and self.grammars is not None:
            _dict['grammars'] = [x._to_dict() for x in self.grammars]
        return _dict

    def __str__(self):
        """Return a `str` version of this Grammars object."""
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
    Information about a match for a keyword from speech recognition results.

    :attr str normalized_text: A specified keyword normalized to the spoken phrase that
    matched in the audio input.
    :attr float start_time: The start time in seconds of the keyword match.
    :attr float end_time: The end time in seconds of the keyword match.
    :attr float confidence: A confidence score for the keyword match in the range of 0.0
    to 1.0.
    """

    def __init__(self, normalized_text, start_time, end_time, confidence):
        """
        Initialize a KeywordResult object.

        :param str normalized_text: A specified keyword normalized to the spoken phrase
        that matched in the audio input.
        :param float start_time: The start time in seconds of the keyword match.
        :param float end_time: The end time in seconds of the keyword match.
        :param float confidence: A confidence score for the keyword match in the range of
        0.0 to 1.0.
        """
        self.normalized_text = normalized_text
        self.start_time = start_time
        self.end_time = end_time
        self.confidence = confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordResult object from a json dictionary."""
        args = {}
        validKeys = ['normalized_text', 'start_time', 'end_time', 'confidence']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class KeywordResult: '
                + ', '.join(badKeys))
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
    Information about an existing custom language model.

    :attr str customization_id: The customization ID (GUID) of the custom language model.
    The **Create a custom language model** method returns only this field of the object;
    it does not return the other fields.
    :attr str created: (optional) The date and time in Coordinated Universal Time (UTC) at
    which the custom language model was created. The value is provided in full ISO 8601
    format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str updated: (optional) The date and time in Coordinated Universal Time (UTC) at
    which the custom language model was last modified. The `created` and `updated` fields
    are equal when a language model is first added but has yet to be updated. The value is
    provided in full ISO 8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
    :attr str language: (optional) The language identifier of the custom language model
    (for example, `en-US`).
    :attr str dialect: (optional) The dialect of the language for the custom language
    model. By default, the dialect matches the language of the base model; for example,
    `en-US` for either of the US English language models. For Spanish models, the field
    indicates the dialect for which the model was created:
    * `es-ES` for Castilian Spanish (the default)
    * `es-LA` for Latin American Spanish
    * `es-US` for North American (Mexican) Spanish.
    :attr list[str] versions: (optional) A list of the available versions of the custom
    language model. Each element of the array indicates a version of the base model with
    which the custom model can be used. Multiple versions exist only if the custom model
    has been upgraded; otherwise, only a single version is shown.
    :attr str owner: (optional) The GUID of the credentials for the instance of the
    service that owns the custom language model.
    :attr str name: (optional) The name of the custom language model.
    :attr str description: (optional) The description of the custom language model.
    :attr str base_model_name: (optional) The name of the language model for which the
    custom language model was created.
    :attr str status: (optional) The current status of the custom language model:
    * `pending`: The model was created but is waiting either for valid training data to be
    added or for the service to finish analyzing added data.
    * `ready`: The model contains valid data and is ready to be trained. If the model
    contains a mix of valid and invalid resources, you need to set the `strict` parameter
    to `false` for the training to proceed.
    * `training`: The model is currently being trained.
    * `available`: The model is trained and ready to use.
    * `upgrading`: The model is currently being upgraded.
    * `failed`: Training of the model failed.
    :attr int progress: (optional) A percentage that indicates the progress of the custom
    language model's current training. A value of `100` means that the model is fully
    trained. **Note:** The `progress` field does not currently reflect the progress of the
    training. The field changes from `0` to `100` when training is complete.
    :attr str error: (optional) If an error occurred while adding a grammar file to the
    custom language model, a message that describes an `Internal Server Error` and
    includes the string `Cannot compile grammar`. The status of the custom model is not
    affected by the error, but the grammar cannot be used with the model.
    :attr str warnings: (optional) If the request included unknown parameters, the
    following message: `Unexpected query parameter(s) ['parameters'] detected`, where
    `parameters` is a list that includes a quoted string for each unknown parameter.
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
                 error=None,
                 warnings=None,
                 updated=None):
        """
        Initialize a LanguageModel object.

        :param str customization_id: The customization ID (GUID) of the custom language
        model. The **Create a custom language model** method returns only this field of
        the object; it does not return the other fields.
        :param str created: (optional) The date and time in Coordinated Universal Time
        (UTC) at which the custom language model was created. The value is provided in
        full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str updated: (optional) The date and time in Coordinated Universal Time
        (UTC) at which the custom language model was last modified. The `created` and
        `updated` fields are equal when a language model is first added but has yet to be
        updated. The value is provided in full ISO 8601 format (YYYY-MM-DDThh:mm:ss.sTZD).
        :param str language: (optional) The language identifier of the custom language
        model (for example, `en-US`).
        :param str dialect: (optional) The dialect of the language for the custom language
        model. By default, the dialect matches the language of the base model; for
        example, `en-US` for either of the US English language models. For Spanish models,
        the field indicates the dialect for which the model was created:
        * `es-ES` for Castilian Spanish (the default)
        * `es-LA` for Latin American Spanish
        * `es-US` for North American (Mexican) Spanish.
        :param list[str] versions: (optional) A list of the available versions of the
        custom language model. Each element of the array indicates a version of the base
        model with which the custom model can be used. Multiple versions exist only if the
        custom model has been upgraded; otherwise, only a single version is shown.
        :param str owner: (optional) The GUID of the credentials for the instance of the
        service that owns the custom language model.
        :param str name: (optional) The name of the custom language model.
        :param str description: (optional) The description of the custom language model.
        :param str base_model_name: (optional) The name of the language model for which
        the custom language model was created.
        :param str status: (optional) The current status of the custom language model:
        * `pending`: The model was created but is waiting either for valid training data
        to be added or for the service to finish analyzing added data.
        * `ready`: The model contains valid data and is ready to be trained. If the model
        contains a mix of valid and invalid resources, you need to set the `strict`
        parameter to `false` for the training to proceed.
        * `training`: The model is currently being trained.
        * `available`: The model is trained and ready to use.
        * `upgrading`: The model is currently being upgraded.
        * `failed`: Training of the model failed.
        :param int progress: (optional) A percentage that indicates the progress of the
        custom language model's current training. A value of `100` means that the model is
        fully trained. **Note:** The `progress` field does not currently reflect the
        progress of the training. The field changes from `0` to `100` when training is
        complete.
        :param str error: (optional) If an error occurred while adding a grammar file to
        the custom language model, a message that describes an `Internal Server Error` and
        includes the string `Cannot compile grammar`. The status of the custom model is
        not affected by the error, but the grammar cannot be used with the model.
        :param str warnings: (optional) If the request included unknown parameters, the
        following message: `Unexpected query parameter(s) ['parameters'] detected`, where
        `parameters` is a list that includes a quoted string for each unknown parameter.
        """
        self.customization_id = customization_id
        self.created = created
        self.updated = updated
        self.language = language
        self.dialect = dialect
        self.versions = versions
        self.owner = owner
        self.name = name
        self.description = description
        self.base_model_name = base_model_name
        self.status = status
        self.progress = progress
        self.error = error
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LanguageModel object from a json dictionary."""
        args = {}
        validKeys = [
            'customization_id', 'created', 'updated', 'language', 'dialect',
            'versions', 'owner', 'name', 'description', 'base_model_name',
            'status', 'progress', 'error', 'warnings'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LanguageModel: '
                + ', '.join(badKeys))
        if 'customization_id' in _dict:
            args['customization_id'] = _dict.get('customization_id')
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in LanguageModel JSON'
            )
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'updated' in _dict:
            args['updated'] = _dict.get('updated')
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
        if 'error' in _dict:
            args['error'] = _dict.get('error')
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
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = self.updated
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
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
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
    Information about existing custom language models.

    :attr list[LanguageModel] customizations: An array of `LanguageModel` objects that
    provides information about each available custom language model. The array is empty if
    the requesting credentials own no custom language models (if no language is specified)
    or own no custom language models for the specified language.
    """

    def __init__(self, customizations):
        """
        Initialize a LanguageModels object.

        :param list[LanguageModel] customizations: An array of `LanguageModel` objects
        that provides information about each available custom language model. The array is
        empty if the requesting credentials own no custom language models (if no language
        is specified) or own no custom language models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LanguageModels object from a json dictionary."""
        args = {}
        validKeys = ['customizations']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LanguageModels: '
                + ', '.join(badKeys))
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


class ProcessedAudio(object):
    """
    Detailed timing information about the service's processing of the input audio.

    :attr float received: The seconds of audio that the service has received as of this
    response. The value of the field is greater than the values of the `transcription` and
    `speaker_labels` fields during speech recognition processing, since the service first
    has to receive the audio before it can begin to process it. The final value can also
    be greater than the value of the `transcription` and `speaker_labels` fields by a
    fractional number of seconds.
    :attr float seen_by_engine: The seconds of audio that the service has passed to its
    speech-processing engine as of this response. The value of the field is greater than
    the values of the `transcription` and `speaker_labels` fields during speech
    recognition processing. The `received` and `seen_by_engine` fields have identical
    values when the service has finished processing all audio. This final value can be
    greater than the value of the `transcription` and `speaker_labels` fields by a
    fractional number of seconds.
    :attr float transcription: The seconds of audio that the service has processed for
    speech recognition as of this response.
    :attr float speaker_labels: (optional) If speaker labels are requested, the seconds of
    audio that the service has processed to determine speaker labels as of this response.
    This value often trails the value of the `transcription` field during speech
    recognition processing. The `transcription` and `speaker_labels` fields have identical
    values when the service has finished processing all audio.
    """

    def __init__(self,
                 received,
                 seen_by_engine,
                 transcription,
                 speaker_labels=None):
        """
        Initialize a ProcessedAudio object.

        :param float received: The seconds of audio that the service has received as of
        this response. The value of the field is greater than the values of the
        `transcription` and `speaker_labels` fields during speech recognition processing,
        since the service first has to receive the audio before it can begin to process
        it. The final value can also be greater than the value of the `transcription` and
        `speaker_labels` fields by a fractional number of seconds.
        :param float seen_by_engine: The seconds of audio that the service has passed to
        its speech-processing engine as of this response. The value of the field is
        greater than the values of the `transcription` and `speaker_labels` fields during
        speech recognition processing. The `received` and `seen_by_engine` fields have
        identical values when the service has finished processing all audio. This final
        value can be greater than the value of the `transcription` and `speaker_labels`
        fields by a fractional number of seconds.
        :param float transcription: The seconds of audio that the service has processed
        for speech recognition as of this response.
        :param float speaker_labels: (optional) If speaker labels are requested, the
        seconds of audio that the service has processed to determine speaker labels as of
        this response. This value often trails the value of the `transcription` field
        during speech recognition processing. The `transcription` and `speaker_labels`
        fields have identical values when the service has finished processing all audio.
        """
        self.received = received
        self.seen_by_engine = seen_by_engine
        self.transcription = transcription
        self.speaker_labels = speaker_labels

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProcessedAudio object from a json dictionary."""
        args = {}
        validKeys = [
            'received', 'seen_by_engine', 'transcription', 'speaker_labels'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ProcessedAudio: '
                + ', '.join(badKeys))
        if 'received' in _dict:
            args['received'] = _dict.get('received')
        else:
            raise ValueError(
                'Required property \'received\' not present in ProcessedAudio JSON'
            )
        if 'seen_by_engine' in _dict:
            args['seen_by_engine'] = _dict.get('seen_by_engine')
        else:
            raise ValueError(
                'Required property \'seen_by_engine\' not present in ProcessedAudio JSON'
            )
        if 'transcription' in _dict:
            args['transcription'] = _dict.get('transcription')
        else:
            raise ValueError(
                'Required property \'transcription\' not present in ProcessedAudio JSON'
            )
        if 'speaker_labels' in _dict:
            args['speaker_labels'] = _dict.get('speaker_labels')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'received') and self.received is not None:
            _dict['received'] = self.received
        if hasattr(self, 'seen_by_engine') and self.seen_by_engine is not None:
            _dict['seen_by_engine'] = self.seen_by_engine
        if hasattr(self, 'transcription') and self.transcription is not None:
            _dict['transcription'] = self.transcription
        if hasattr(self, 'speaker_labels') and self.speaker_labels is not None:
            _dict['speaker_labels'] = self.speaker_labels
        return _dict

    def __str__(self):
        """Return a `str` version of this ProcessedAudio object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProcessingMetrics(object):
    """
    If processing metrics are requested, information about the service's processing of the
    input audio. Processing metrics are not available with the synchronous **Recognize
    audio** method.

    :attr ProcessedAudio processed_audio: Detailed timing information about the service's
    processing of the input audio.
    :attr float wall_clock_since_first_byte_received: The amount of real time in seconds
    that has passed since the service received the first byte of input audio. Values in
    this field are generally multiples of the specified metrics interval, with two
    differences:
    * Values might not reflect exact intervals (for instance, 0.25, 0.5, and so on).
    Actual values might be 0.27, 0.52, and so on, depending on when the service receives
    and processes audio.
    * The service also returns values for transcription events if you set the
    `interim_results` parameter to `true`. The service returns both processing metrics and
    transcription results when such events occur.
    :attr bool periodic: An indication of whether the metrics apply to a periodic interval
    or a transcription event:
    * `true` means that the response was triggered by a specified processing interval. The
    information contains processing metrics only.
    * `false` means that the response was triggered by a transcription event. The
    information contains processing metrics plus transcription results.
    Use the field to identify why the service generated the response and to filter
    different results if necessary.
    """

    def __init__(self, processed_audio, wall_clock_since_first_byte_received,
                 periodic):
        """
        Initialize a ProcessingMetrics object.

        :param ProcessedAudio processed_audio: Detailed timing information about the
        service's processing of the input audio.
        :param float wall_clock_since_first_byte_received: The amount of real time in
        seconds that has passed since the service received the first byte of input audio.
        Values in this field are generally multiples of the specified metrics interval,
        with two differences:
        * Values might not reflect exact intervals (for instance, 0.25, 0.5, and so on).
        Actual values might be 0.27, 0.52, and so on, depending on when the service
        receives and processes audio.
        * The service also returns values for transcription events if you set the
        `interim_results` parameter to `true`. The service returns both processing metrics
        and transcription results when such events occur.
        :param bool periodic: An indication of whether the metrics apply to a periodic
        interval or a transcription event:
        * `true` means that the response was triggered by a specified processing interval.
        The information contains processing metrics only.
        * `false` means that the response was triggered by a transcription event. The
        information contains processing metrics plus transcription results.
        Use the field to identify why the service generated the response and to filter
        different results if necessary.
        """
        self.processed_audio = processed_audio
        self.wall_clock_since_first_byte_received = wall_clock_since_first_byte_received
        self.periodic = periodic

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProcessingMetrics object from a json dictionary."""
        args = {}
        validKeys = [
            'processed_audio', 'wall_clock_since_first_byte_received',
            'periodic'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ProcessingMetrics: '
                + ', '.join(badKeys))
        if 'processed_audio' in _dict:
            args['processed_audio'] = ProcessedAudio._from_dict(
                _dict.get('processed_audio'))
        else:
            raise ValueError(
                'Required property \'processed_audio\' not present in ProcessingMetrics JSON'
            )
        if 'wall_clock_since_first_byte_received' in _dict:
            args['wall_clock_since_first_byte_received'] = _dict.get(
                'wall_clock_since_first_byte_received')
        else:
            raise ValueError(
                'Required property \'wall_clock_since_first_byte_received\' not present in ProcessingMetrics JSON'
            )
        if 'periodic' in _dict:
            args['periodic'] = _dict.get('periodic')
        else:
            raise ValueError(
                'Required property \'periodic\' not present in ProcessingMetrics JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'processed_audio') and self.processed_audio is not None:
            _dict['processed_audio'] = self.processed_audio._to_dict()
        if hasattr(self, 'wall_clock_since_first_byte_received'
                  ) and self.wall_clock_since_first_byte_received is not None:
            _dict[
                'wall_clock_since_first_byte_received'] = self.wall_clock_since_first_byte_received
        if hasattr(self, 'periodic') and self.periodic is not None:
            _dict['periodic'] = self.periodic
        return _dict

    def __str__(self):
        """Return a `str` version of this ProcessingMetrics object."""
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
    Information about a current asynchronous speech recognition job.

    :attr str id: The ID of the asynchronous job.
    :attr str status: The current status of the job:
    * `waiting`: The service is preparing the job for processing. The service returns this
    status when the job is initially created or when it is waiting for capacity to process
    the job. The job remains in this state until the service has the capacity to begin
    processing it.
    * `processing`: The service is actively processing the job.
    * `completed`: The service has finished processing the job. If the job specified a
    callback URL and the event `recognitions.completed_with_results`, the service sent the
    results with the callback notification. Otherwise, you must retrieve the results by
    checking the individual job.
    * `failed`: The job failed.
    :attr str created: The date and time in Coordinated Universal Time (UTC) at which the
    job was created. The value is provided in full ISO 8601 format
    (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str updated: (optional) The date and time in Coordinated Universal Time (UTC) at
    which the job was last updated by the service. The value is provided in full ISO 8601
    format (`YYYY-MM-DDThh:mm:ss.sTZD`). This field is returned only by the **Check jobs**
    and **Check a job** methods.
    :attr str url: (optional) The URL to use to request information about the job with the
    **Check a job** method. This field is returned only by the **Create a job** method.
    :attr str user_token: (optional) The user token associated with a job that was created
    with a callback URL and a user token. This field can be returned only by the **Check
    jobs** method.
    :attr list[SpeechRecognitionResults] results: (optional) If the status is `completed`,
    the results of the recognition request as an array that includes a single instance of
    a `SpeechRecognitionResults` object. This field is returned only by the **Check a
    job** method.
    :attr list[str] warnings: (optional) An array of warning messages about invalid
    parameters included with the request. Each warning includes a descriptive message and
    a list of invalid argument strings, for example, `"unexpected query parameter
    'user_token', query parameter 'callback_url' was not specified"`. The request succeeds
    despite the warnings. This field can be returned only by the **Create a job** method.
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

        :param str id: The ID of the asynchronous job.
        :param str status: The current status of the job:
        * `waiting`: The service is preparing the job for processing. The service returns
        this status when the job is initially created or when it is waiting for capacity
        to process the job. The job remains in this state until the service has the
        capacity to begin processing it.
        * `processing`: The service is actively processing the job.
        * `completed`: The service has finished processing the job. If the job specified a
        callback URL and the event `recognitions.completed_with_results`, the service sent
        the results with the callback notification. Otherwise, you must retrieve the
        results by checking the individual job.
        * `failed`: The job failed.
        :param str created: The date and time in Coordinated Universal Time (UTC) at which
        the job was created. The value is provided in full ISO 8601 format
        (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str updated: (optional) The date and time in Coordinated Universal Time
        (UTC) at which the job was last updated by the service. The value is provided in
        full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`). This field is returned only by
        the **Check jobs** and **Check a job** methods.
        :param str url: (optional) The URL to use to request information about the job
        with the **Check a job** method. This field is returned only by the **Create a
        job** method.
        :param str user_token: (optional) The user token associated with a job that was
        created with a callback URL and a user token. This field can be returned only by
        the **Check jobs** method.
        :param list[SpeechRecognitionResults] results: (optional) If the status is
        `completed`, the results of the recognition request as an array that includes a
        single instance of a `SpeechRecognitionResults` object. This field is returned
        only by the **Check a job** method.
        :param list[str] warnings: (optional) An array of warning messages about invalid
        parameters included with the request. Each warning includes a descriptive message
        and a list of invalid argument strings, for example, `"unexpected query parameter
        'user_token', query parameter 'callback_url' was not specified"`. The request
        succeeds despite the warnings. This field can be returned only by the **Create a
        job** method.
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
        validKeys = [
            'id', 'status', 'created', 'updated', 'url', 'user_token',
            'results', 'warnings'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RecognitionJob: '
                + ', '.join(badKeys))
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
    Information about current asynchronous speech recognition jobs.

    :attr list[RecognitionJob] recognitions: An array of `RecognitionJob` objects that
    provides the status for each of the user's current jobs. The array is empty if the
    user has no current jobs.
    """

    def __init__(self, recognitions):
        """
        Initialize a RecognitionJobs object.

        :param list[RecognitionJob] recognitions: An array of `RecognitionJob` objects
        that provides the status for each of the user's current jobs. The array is empty
        if the user has no current jobs.
        """
        self.recognitions = recognitions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecognitionJobs object from a json dictionary."""
        args = {}
        validKeys = ['recognitions']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RecognitionJobs: '
                + ', '.join(badKeys))
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
    Information about a request to register a callback for asynchronous speech
    recognition.

    :attr str status: The current status of the job:
    * `created`: The service successfully white-listed the callback URL as a result of the
    call.
    * `already created`: The URL was already white-listed.
    :attr str url: The callback URL that is successfully registered.
    """

    def __init__(self, status, url):
        """
        Initialize a RegisterStatus object.

        :param str status: The current status of the job:
        * `created`: The service successfully white-listed the callback URL as a result of
        the call.
        * `already created`: The URL was already white-listed.
        :param str url: The callback URL that is successfully registered.
        """
        self.status = status
        self.url = url

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RegisterStatus object from a json dictionary."""
        args = {}
        validKeys = ['status', 'url']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RegisterStatus: '
                + ', '.join(badKeys))
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
    Information about the speakers from speech recognition results.

    :attr float from_: The start time of a word from the transcript. The value matches the
    start time of a word from the `timestamps` array.
    :attr float to: The end time of a word from the transcript. The value matches the end
    time of a word from the `timestamps` array.
    :attr int speaker: The numeric identifier that the service assigns to a speaker from
    the audio. Speaker IDs begin at `0` initially but can evolve and change across interim
    results (if supported by the method) and between interim and final results as the
    service processes the audio. They are not guaranteed to be sequential, contiguous, or
    ordered.
    :attr float confidence: A score that indicates the service's confidence in its
    identification of the speaker in the range of 0.0 to 1.0.
    :attr bool final_results: An indication of whether the service might further change
    word and speaker-label results. A value of `true` means that the service guarantees
    not to send any further updates for the current or any preceding results; `false`
    means that the service might send further updates to the results.
    """

    def __init__(self, from_, to, speaker, confidence, final_results):
        """
        Initialize a SpeakerLabelsResult object.

        :param float from_: The start time of a word from the transcript. The value
        matches the start time of a word from the `timestamps` array.
        :param float to: The end time of a word from the transcript. The value matches the
        end time of a word from the `timestamps` array.
        :param int speaker: The numeric identifier that the service assigns to a speaker
        from the audio. Speaker IDs begin at `0` initially but can evolve and change
        across interim results (if supported by the method) and between interim and final
        results as the service processes the audio. They are not guaranteed to be
        sequential, contiguous, or ordered.
        :param float confidence: A score that indicates the service's confidence in its
        identification of the speaker in the range of 0.0 to 1.0.
        :param bool final_results: An indication of whether the service might further
        change word and speaker-label results. A value of `true` means that the service
        guarantees not to send any further updates for the current or any preceding
        results; `false` means that the service might send further updates to the results.
        """
        self.from_ = from_
        self.to = to
        self.speaker = speaker
        self.confidence = confidence
        self.final_results = final_results

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeakerLabelsResult object from a json dictionary."""
        args = {}
        validKeys = [
            'from_', 'from', 'to', 'speaker', 'confidence', 'final_results',
            'final'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SpeakerLabelsResult: '
                + ', '.join(badKeys))
        if 'from' in _dict:
            args['from_'] = _dict.get('from')
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
            args['final_results'] = _dict.get('final') or _dict.get(
                'final_results')
        else:
            raise ValueError(
                'Required property \'final\' not present in SpeakerLabelsResult JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'from_') and self.from_ is not None:
            _dict['from'] = self.from_
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
    Information about an available language model.

    :attr str name: The name of the model for use as an identifier in calls to the service
    (for example, `en-US_BroadbandModel`).
    :attr str language: The language identifier of the model (for example, `en-US`).
    :attr int rate: The sampling rate (minimum acceptable rate for audio) used by the
    model in Hertz.
    :attr str url: The URI for the model.
    :attr SupportedFeatures supported_features: Additional service features that are
    supported with the model.
    :attr str description: A brief description of the model.
    """

    def __init__(self, name, language, rate, url, supported_features,
                 description):
        """
        Initialize a SpeechModel object.

        :param str name: The name of the model for use as an identifier in calls to the
        service (for example, `en-US_BroadbandModel`).
        :param str language: The language identifier of the model (for example, `en-US`).
        :param int rate: The sampling rate (minimum acceptable rate for audio) used by the
        model in Hertz.
        :param str url: The URI for the model.
        :param SupportedFeatures supported_features: Additional service features that are
        supported with the model.
        :param str description: A brief description of the model.
        """
        self.name = name
        self.language = language
        self.rate = rate
        self.url = url
        self.supported_features = supported_features
        self.description = description

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechModel object from a json dictionary."""
        args = {}
        validKeys = [
            'name', 'language', 'rate', 'url', 'supported_features',
            'description'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SpeechModel: '
                + ', '.join(badKeys))
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
    Information about the available language models.

    :attr list[SpeechModel] models: An array of `SpeechModel` objects that provides
    information about each available model.
    """

    def __init__(self, models):
        """
        Initialize a SpeechModels object.

        :param list[SpeechModel] models: An array of `SpeechModel` objects that provides
        information about each available model.
        """
        self.models = models

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechModels object from a json dictionary."""
        args = {}
        validKeys = ['models']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SpeechModels: '
                + ', '.join(badKeys))
        if 'models' in _dict:
            args['models'] = [
                SpeechModel._from_dict(x) for x in (_dict.get('models'))
            ]
        else:
            raise ValueError(
                'Required property \'models\' not present in SpeechModels JSON')
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
    An alternative transcript from speech recognition results.

    :attr str transcript: A transcription of the audio.
    :attr float confidence: (optional) A score that indicates the service's confidence in
    the transcript in the range of 0.0 to 1.0. A confidence score is returned only for the
    best alternative and only with results marked as final.
    :attr list[str] timestamps: (optional) Time alignments for each word from the
    transcript as a list of lists. Each inner list consists of three elements: the word
    followed by its start and end time in seconds, for example:
    `[["hello",0.0,1.2],["world",1.2,2.5]]`. Timestamps are returned only for the best
    alternative.
    :attr list[str] word_confidence: (optional) A confidence score for each word of the
    transcript as a list of lists. Each inner list consists of two elements: the word and
    its confidence score in the range of 0.0 to 1.0, for example:
    `[["hello",0.95],["world",0.866]]`. Confidence scores are returned only for the best
    alternative and only with results marked as final.
    """

    def __init__(self,
                 transcript,
                 confidence=None,
                 timestamps=None,
                 word_confidence=None):
        """
        Initialize a SpeechRecognitionAlternative object.

        :param str transcript: A transcription of the audio.
        :param float confidence: (optional) A score that indicates the service's
        confidence in the transcript in the range of 0.0 to 1.0. A confidence score is
        returned only for the best alternative and only with results marked as final.
        :param list[str] timestamps: (optional) Time alignments for each word from the
        transcript as a list of lists. Each inner list consists of three elements: the
        word followed by its start and end time in seconds, for example:
        `[["hello",0.0,1.2],["world",1.2,2.5]]`. Timestamps are returned only for the best
        alternative.
        :param list[str] word_confidence: (optional) A confidence score for each word of
        the transcript as a list of lists. Each inner list consists of two elements: the
        word and its confidence score in the range of 0.0 to 1.0, for example:
        `[["hello",0.95],["world",0.866]]`. Confidence scores are returned only for the
        best alternative and only with results marked as final.
        """
        self.transcript = transcript
        self.confidence = confidence
        self.timestamps = timestamps
        self.word_confidence = word_confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionAlternative object from a json dictionary."""
        args = {}
        validKeys = [
            'transcript', 'confidence', 'timestamps', 'word_confidence'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SpeechRecognitionAlternative: '
                + ', '.join(badKeys))
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
    Component results for a speech recognition request.

    :attr bool final_results: An indication of whether the transcription results are
    final. If `true`, the results for this utterance are not updated further; no
    additional results are sent for a `result_index` once its results are indicated as
    final.
    :attr list[SpeechRecognitionAlternative] alternatives: An array of alternative
    transcripts. The `alternatives` array can include additional requested output such as
    word confidence or timestamps.
    :attr dict keywords_result: (optional) A dictionary (or associative array) whose keys
    are the strings specified for `keywords` if both that parameter and
    `keywords_threshold` are specified. The value for each key is an array of matches
    spotted in the audio for that keyword. Each match is described by a `KeywordResult`
    object. A keyword for which no matches are found is omitted from the dictionary. The
    dictionary is omitted entirely if no matches are found for any keywords.
    :attr list[WordAlternativeResults] word_alternatives: (optional) An array of
    alternative hypotheses found for words of the input audio if a
    `word_alternatives_threshold` is specified.
    """

    def __init__(self,
                 final_results,
                 alternatives,
                 keywords_result=None,
                 word_alternatives=None):
        """
        Initialize a SpeechRecognitionResult object.

        :param bool final_results: An indication of whether the transcription results are
        final. If `true`, the results for this utterance are not updated further; no
        additional results are sent for a `result_index` once its results are indicated as
        final.
        :param list[SpeechRecognitionAlternative] alternatives: An array of alternative
        transcripts. The `alternatives` array can include additional requested output such
        as word confidence or timestamps.
        :param dict keywords_result: (optional) A dictionary (or associative array) whose
        keys are the strings specified for `keywords` if both that parameter and
        `keywords_threshold` are specified. The value for each key is an array of matches
        spotted in the audio for that keyword. Each match is described by a
        `KeywordResult` object. A keyword for which no matches are found is omitted from
        the dictionary. The dictionary is omitted entirely if no matches are found for any
        keywords.
        :param list[WordAlternativeResults] word_alternatives: (optional) An array of
        alternative hypotheses found for words of the input audio if a
        `word_alternatives_threshold` is specified.
        """
        self.final_results = final_results
        self.alternatives = alternatives
        self.keywords_result = keywords_result
        self.word_alternatives = word_alternatives

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionResult object from a json dictionary."""
        args = {}
        validKeys = [
            'final_results', 'final', 'alternatives', 'keywords_result',
            'word_alternatives'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SpeechRecognitionResult: '
                + ', '.join(badKeys))
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
    The complete results for a speech recognition request.

    :attr list[SpeechRecognitionResult] results: (optional) An array of
    `SpeechRecognitionResult` objects that can include interim and final results (interim
    results are returned only if supported by the method). Final results are guaranteed
    not to change; interim results might be replaced by further interim results and final
    results. The service periodically sends updates to the results list; the
    `result_index` is set to the lowest index in the array that has changed; it is
    incremented for new results.
    :attr int result_index: (optional) An index that indicates a change point in the
    `results` array. The service increments the index only for additional results that it
    sends for new audio for the same request.
    :attr list[SpeakerLabelsResult] speaker_labels: (optional) An array of
    `SpeakerLabelsResult` objects that identifies which words were spoken by which
    speakers in a multi-person exchange. The array is returned only if the
    `speaker_labels` parameter is `true`. When interim results are also requested for
    methods that support them, it is possible for a `SpeechRecognitionResults` object to
    include only the `speaker_labels` field.
    :attr ProcessingMetrics processing_metrics: (optional) If processing metrics are
    requested, information about the service's processing of the input audio. Processing
    metrics are not available with the synchronous **Recognize audio** method.
    :attr AudioMetrics audio_metrics: (optional) If audio metrics are requested,
    information about the signal characteristics of the input audio.
    :attr list[str] warnings: (optional) An array of warning messages associated with the
    request:
    * Warnings for invalid parameters or fields can include a descriptive message and a
    list of invalid argument strings, for example, `"Unknown arguments:"` or `"Unknown url
    query arguments:"` followed by a list of the form `"{invalid_arg_1},
    {invalid_arg_2}."`
    * The following warning is returned if the request passes a custom model that is based
    on an older version of a base model for which an updated version is available: `"Using
    previous version of base model, because your custom model has been built with it.
    Please note that this version will be supported only for a limited time. Consider
    updating your custom model to the new base model. If you do not do that you will be
    automatically switched to base model when you used the non-updated custom model."`
    In both cases, the request succeeds despite the warnings.
    """

    def __init__(self,
                 results=None,
                 result_index=None,
                 speaker_labels=None,
                 audio_metrics=None,
                 warnings=None,
                 processing_metrics=None):
        """
        Initialize a SpeechRecognitionResults object.

        :param list[SpeechRecognitionResult] results: (optional) An array of
        `SpeechRecognitionResult` objects that can include interim and final results
        (interim results are returned only if supported by the method). Final results are
        guaranteed not to change; interim results might be replaced by further interim
        results and final results. The service periodically sends updates to the results
        list; the `result_index` is set to the lowest index in the array that has changed;
        it is incremented for new results.
        :param int result_index: (optional) An index that indicates a change point in the
        `results` array. The service increments the index only for additional results that
        it sends for new audio for the same request.
        :param list[SpeakerLabelsResult] speaker_labels: (optional) An array of
        `SpeakerLabelsResult` objects that identifies which words were spoken by which
        speakers in a multi-person exchange. The array is returned only if the
        `speaker_labels` parameter is `true`. When interim results are also requested for
        methods that support them, it is possible for a `SpeechRecognitionResults` object
        to include only the `speaker_labels` field.
        :param ProcessingMetrics processing_metrics: (optional) If processing metrics are
        requested, information about the service's processing of the input audio.
        Processing metrics are not available with the synchronous **Recognize audio**
        method.
        :param AudioMetrics audio_metrics: (optional) If audio metrics are requested,
        information about the signal characteristics of the input audio.
        :param list[str] warnings: (optional) An array of warning messages associated with
        the request:
        * Warnings for invalid parameters or fields can include a descriptive message and
        a list of invalid argument strings, for example, `"Unknown arguments:"` or
        `"Unknown url query arguments:"` followed by a list of the form `"{invalid_arg_1},
        {invalid_arg_2}."`
        * The following warning is returned if the request passes a custom model that is
        based on an older version of a base model for which an updated version is
        available: `"Using previous version of base model, because your custom model has
        been built with it. Please note that this version will be supported only for a
        limited time. Consider updating your custom model to the new base model. If you do
        not do that you will be automatically switched to base model when you used the
        non-updated custom model."`
        In both cases, the request succeeds despite the warnings.
        """
        self.results = results
        self.result_index = result_index
        self.speaker_labels = speaker_labels
        self.processing_metrics = processing_metrics
        self.audio_metrics = audio_metrics
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionResults object from a json dictionary."""
        args = {}
        validKeys = [
            'results', 'result_index', 'speaker_labels', 'processing_metrics',
            'audio_metrics', 'warnings'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SpeechRecognitionResults: '
                + ', '.join(badKeys))
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
        if 'processing_metrics' in _dict:
            args['processing_metrics'] = ProcessingMetrics._from_dict(
                _dict.get('processing_metrics'))
        if 'audio_metrics' in _dict:
            args['audio_metrics'] = AudioMetrics._from_dict(
                _dict.get('audio_metrics'))
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
        if hasattr(
                self,
                'processing_metrics') and self.processing_metrics is not None:
            _dict['processing_metrics'] = self.processing_metrics._to_dict()
        if hasattr(self, 'audio_metrics') and self.audio_metrics is not None:
            _dict['audio_metrics'] = self.audio_metrics._to_dict()
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
    Additional service features that are supported with the model.

    :attr bool custom_language_model: Indicates whether the customization interface can be
    used to create a custom language model based on the language model.
    :attr bool speaker_labels: Indicates whether the `speaker_labels` parameter can be
    used with the language model.
    """

    def __init__(self, custom_language_model, speaker_labels):
        """
        Initialize a SupportedFeatures object.

        :param bool custom_language_model: Indicates whether the customization interface
        can be used to create a custom language model based on the language model.
        :param bool speaker_labels: Indicates whether the `speaker_labels` parameter can
        be used with the language model.
        """
        self.custom_language_model = custom_language_model
        self.speaker_labels = speaker_labels

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SupportedFeatures object from a json dictionary."""
        args = {}
        validKeys = ['custom_language_model', 'speaker_labels']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SupportedFeatures: '
                + ', '.join(badKeys))
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
        if hasattr(self, 'custom_language_model'
                  ) and self.custom_language_model is not None:
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


class TrainingResponse(object):
    """
    The response from training of a custom language or custom acoustic model.

    :attr list[TrainingWarning] warnings: (optional) An array of `TrainingWarning` objects
    that lists any invalid resources contained in the custom model. For custom language
    models, invalid resources are grouped and identified by type of resource. The method
    can return warnings only if the `strict` parameter is set to `false`.
    """

    def __init__(self, warnings=None):
        """
        Initialize a TrainingResponse object.

        :param list[TrainingWarning] warnings: (optional) An array of `TrainingWarning`
        objects that lists any invalid resources contained in the custom model. For custom
        language models, invalid resources are grouped and identified by type of resource.
        The method can return warnings only if the `strict` parameter is set to `false`.
        """
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingResponse object from a json dictionary."""
        args = {}
        validKeys = ['warnings']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingResponse: '
                + ', '.join(badKeys))
        if 'warnings' in _dict:
            args['warnings'] = [
                TrainingWarning._from_dict(x) for x in (_dict.get('warnings'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = [x._to_dict() for x in self.warnings]
        return _dict

    def __str__(self):
        """Return a `str` version of this TrainingResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingWarning(object):
    """
    A warning from training of a custom language or custom acoustic model.

    :attr str code: An identifier for the type of invalid resources listed in the
    `description` field.
    :attr str message: A warning message that lists the invalid resources that are
    excluded from the custom model's training. The message has the following format:
    `Analysis of the following {resource_type} has not completed successfully:
    [{resource_names}]. They will be excluded from custom {model_type} model training.`.
    """

    def __init__(self, code, message):
        """
        Initialize a TrainingWarning object.

        :param str code: An identifier for the type of invalid resources listed in the
        `description` field.
        :param str message: A warning message that lists the invalid resources that are
        excluded from the custom model's training. The message has the following format:
        `Analysis of the following {resource_type} has not completed successfully:
        [{resource_names}]. They will be excluded from custom {model_type} model
        training.`.
        """
        self.code = code
        self.message = message

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingWarning object from a json dictionary."""
        args = {}
        validKeys = ['code', 'message']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingWarning: '
                + ', '.join(badKeys))
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError(
                'Required property \'code\' not present in TrainingWarning JSON'
            )
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError(
                'Required property \'message\' not present in TrainingWarning JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def __str__(self):
        """Return a `str` version of this TrainingWarning object."""
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
    Information about a word from a custom language model.

    :attr str word: A word from the custom model's words resource. The spelling of the
    word is used to train the model.
    :attr list[str] sounds_like: An array of pronunciations for the word. The array can
    include the sounds-like pronunciation automatically generated by the service if none
    is provided for the word; the service adds this pronunciation when it finishes
    processing the word.
    :attr str display_as: The spelling of the word that the service uses to display the
    word in a transcript. The field contains an empty string if no display-as value is
    provided for the word, in which case the word is displayed as it is spelled.
    :attr int count: A sum of the number of times the word is found across all corpora.
    For example, if the word occurs five times in one corpus and seven times in another,
    its count is `12`. If you add a custom word to a model before it is added by any
    corpora, the count begins at `1`; if the word is added from a corpus first and later
    modified, the count reflects only the number of times it is found in corpora.
    :attr list[str] source: An array of sources that describes how the word was added to
    the custom model's words resource. For OOV words added from a corpus, includes the
    name of the corpus; if the word was added by multiple corpora, the names of all
    corpora are listed. If the word was modified or added by the user directly, the field
    includes the string `user`.
    :attr list[WordError] error: (optional) If the service discovered one or more problems
    that you need to correct for the word's definition, an array that describes each of
    the errors.
    """

    def __init__(self, word, sounds_like, display_as, count, source,
                 error=None):
        """
        Initialize a Word object.

        :param str word: A word from the custom model's words resource. The spelling of
        the word is used to train the model.
        :param list[str] sounds_like: An array of pronunciations for the word. The array
        can include the sounds-like pronunciation automatically generated by the service
        if none is provided for the word; the service adds this pronunciation when it
        finishes processing the word.
        :param str display_as: The spelling of the word that the service uses to display
        the word in a transcript. The field contains an empty string if no display-as
        value is provided for the word, in which case the word is displayed as it is
        spelled.
        :param int count: A sum of the number of times the word is found across all
        corpora. For example, if the word occurs five times in one corpus and seven times
        in another, its count is `12`. If you add a custom word to a model before it is
        added by any corpora, the count begins at `1`; if the word is added from a corpus
        first and later modified, the count reflects only the number of times it is found
        in corpora.
        :param list[str] source: An array of sources that describes how the word was added
        to the custom model's words resource. For OOV words added from a corpus, includes
        the name of the corpus; if the word was added by multiple corpora, the names of
        all corpora are listed. If the word was modified or added by the user directly,
        the field includes the string `user`.
        :param list[WordError] error: (optional) If the service discovered one or more
        problems that you need to correct for the word's definition, an array that
        describes each of the errors.
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
        validKeys = [
            'word', 'sounds_like', 'display_as', 'count', 'source', 'error'
        ]
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Word: ' +
                ', '.join(badKeys))
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
    An alternative hypothesis for a word from speech recognition results.

    :attr float confidence: A confidence score for the word alternative hypothesis in the
    range of 0.0 to 1.0.
    :attr str word: An alternative hypothesis for a word from the input audio.
    """

    def __init__(self, confidence, word):
        """
        Initialize a WordAlternativeResult object.

        :param float confidence: A confidence score for the word alternative hypothesis in
        the range of 0.0 to 1.0.
        :param str word: An alternative hypothesis for a word from the input audio.
        """
        self.confidence = confidence
        self.word = word

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordAlternativeResult object from a json dictionary."""
        args = {}
        validKeys = ['confidence', 'word']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WordAlternativeResult: '
                + ', '.join(badKeys))
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
    Information about alternative hypotheses for words from speech recognition results.

    :attr float start_time: The start time in seconds of the word from the input audio
    that corresponds to the word alternatives.
    :attr float end_time: The end time in seconds of the word from the input audio that
    corresponds to the word alternatives.
    :attr list[WordAlternativeResult] alternatives: An array of alternative hypotheses for
    a word from the input audio.
    """

    def __init__(self, start_time, end_time, alternatives):
        """
        Initialize a WordAlternativeResults object.

        :param float start_time: The start time in seconds of the word from the input
        audio that corresponds to the word alternatives.
        :param float end_time: The end time in seconds of the word from the input audio
        that corresponds to the word alternatives.
        :param list[WordAlternativeResult] alternatives: An array of alternative
        hypotheses for a word from the input audio.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.alternatives = alternatives

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordAlternativeResults object from a json dictionary."""
        args = {}
        validKeys = ['start_time', 'end_time', 'alternatives']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WordAlternativeResults: '
                + ', '.join(badKeys))
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
    An error associated with a word from a custom language model.

    :attr str element: A key-value pair that describes an error associated with the
    definition of a word in the words resource. The pair has the format `"element":
    "message"`, where `element` is the aspect of the definition that caused the problem
    and `message` describes the problem. The following example describes a problem with
    one of the word's sounds-like definitions: `"{sounds_like_string}": "Numbers are not
    allowed in sounds-like. You can try for example '{suggested_string}'."`.
    """

    def __init__(self, element):
        """
        Initialize a WordError object.

        :param str element: A key-value pair that describes an error associated with the
        definition of a word in the words resource. The pair has the format `"element":
        "message"`, where `element` is the aspect of the definition that caused the
        problem and `message` describes the problem. The following example describes a
        problem with one of the word's sounds-like definitions: `"{sounds_like_string}":
        "Numbers are not allowed in sounds-like. You can try for example
        '{suggested_string}'."`.
        """
        self.element = element

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordError object from a json dictionary."""
        args = {}
        validKeys = ['element']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WordError: '
                + ', '.join(badKeys))
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
    Information about the words from a custom language model.

    :attr list[Word] words: An array of `Word` objects that provides information about
    each word in the custom model's words resource. The array is empty if the custom model
    has no words.
    """

    def __init__(self, words):
        """
        Initialize a Words object.

        :param list[Word] words: An array of `Word` objects that provides information
        about each word in the custom model's words resource. The array is empty if the
        custom model has no words.
        """
        self.words = words

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Words object from a json dictionary."""
        args = {}
        validKeys = ['words']
        badKeys = set(_dict.keys()) - set(validKeys)
        if badKeys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Words: ' +
                ', '.join(badKeys))
        if 'words' in _dict:
            args['words'] = [Word._from_dict(x) for x in (_dict.get('words'))]
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
