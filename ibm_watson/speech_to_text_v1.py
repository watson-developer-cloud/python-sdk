# coding: utf-8

# (C) Copyright IBM Corp. 2015, 2024.
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

# IBM OpenAPI SDK Code Generator Version: 3.97.0-0e90eab1-20241120-170029
"""
The IBM Watson&trade; Speech to Text service provides APIs that use IBM's
speech-recognition capabilities to produce transcripts of spoken audio. The service can
transcribe speech from various languages and audio formats. In addition to basic
transcription, the service can produce detailed information about many different aspects
of the audio. It returns all JSON response content in the UTF-8 character set.
The service supports two types of models: previous-generation models that include the
terms `Broadband` and `Narrowband` in their names, and next-generation models that include
the terms `Multimedia` and `Telephony` in their names. Broadband and multimedia models
have minimum sampling rates of 16 kHz. Narrowband and telephony models have minimum
sampling rates of 8 kHz. The next-generation models offer high throughput and greater
transcription accuracy.
Effective **31 July 2023**, all previous-generation models will be removed from the
service and the documentation. Most previous-generation models were deprecated on 15 March
2022. You must migrate to the equivalent large speech model or next-generation model by 31
July 2023. For more information, see [Migrating to large speech
models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-migrate).{:
deprecated}
For speech recognition, the service supports synchronous and asynchronous HTTP
Representational State Transfer (REST) interfaces. It also supports a WebSocket interface
that provides a full-duplex, low-latency communication channel: Clients send requests and
audio to the service and receive results over a single connection asynchronously.
The service also offers two customization interfaces. Use language model customization to
expand the vocabulary of a base model with domain-specific terminology. Use acoustic model
customization to adapt a base model for the acoustic characteristics of your audio. For
language model customization, the service also supports grammars. A grammar is a formal
language specification that lets you restrict the phrases that the service can recognize.
Language model customization and grammars are available for most previous- and
next-generation models. Acoustic model customization is available for all
previous-generation models.

API Version: 1.0.0
See: https://cloud.ibm.com/docs/speech-to-text
"""

from enum import Enum
from typing import BinaryIO, Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class SpeechToTextV1(BaseService):
    """The Speech to Text V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'speech_to_text'

    def __init__(
        self,
        authenticator: Authenticator = None,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Speech to Text service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if not authenticator:
            authenticator = get_authenticator_from_environment(service_name)
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.configure_service(service_name)

    #########################
    # Models
    #########################

    def list_models(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List models.

        Lists all language models that are available for use with the service. The
        information includes the name of the model and its minimum sampling rate in Hertz,
        among other things. The ordering of the list of models can change from call to
        call; do not rely on an alphabetized or static list of models.
        **See also:** [Listing all
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-list#models-list-all).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SpeechModels` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_models',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/models'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_model(
        self,
        model_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a model.

        Gets information for a single specified language model that is available for use
        with the service. The information includes the name of the model and its minimum
        sampling rate in Hertz, among other things.
        **See also:** [Listing a specific
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-list#models-list-specific).

        :param str model_id: The identifier of the model in the form of its name
               from the output of the [List models](#listmodels) method.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SpeechModel` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Synchronous
    #########################

    def recognize(
        self,
        audio: BinaryIO,
        *,
        content_type: Optional[str] = None,
        model: Optional[str] = None,
        speech_begin_event: Optional[bool] = None,
        language_customization_id: Optional[str] = None,
        acoustic_customization_id: Optional[str] = None,
        base_model_version: Optional[str] = None,
        customization_weight: Optional[float] = None,
        inactivity_timeout: Optional[int] = None,
        keywords: Optional[List[str]] = None,
        keywords_threshold: Optional[float] = None,
        max_alternatives: Optional[int] = None,
        word_alternatives_threshold: Optional[float] = None,
        word_confidence: Optional[bool] = None,
        timestamps: Optional[bool] = None,
        profanity_filter: Optional[bool] = None,
        smart_formatting: Optional[bool] = None,
        smart_formatting_version: Optional[int] = None,
        speaker_labels: Optional[bool] = None,
        grammar_name: Optional[str] = None,
        redaction: Optional[bool] = None,
        audio_metrics: Optional[bool] = None,
        end_of_phrase_silence_time: Optional[float] = None,
        split_transcript_at_phrase_end: Optional[bool] = None,
        speech_detector_sensitivity: Optional[float] = None,
        background_audio_suppression: Optional[float] = None,
        low_latency: Optional[bool] = None,
        character_insertion_bias: Optional[float] = None,
        **kwargs,
    ) -> DetailedResponse:
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
        request](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-http#HTTP-basic).
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
        transmission](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#transmission)
        *
        [Timeouts](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#timeouts)
        ### Audio formats (content types)
         The service accepts audio in the following formats (MIME types).
        * For formats that are labeled **Required**, you must use the `Content-Type`
        header with the request to specify the format of the audio.
        * For all other formats, you can omit the `Content-Type` header or specify
        `application/octet-stream` with the header to have the service automatically
        detect the format of the audio. (With the `curl` command, you can specify either
        `"Content-Type:"` or `"Content-Type: application/octet-stream"`.)
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
         **See also:** [Supported audio
        formats](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-audio-formats).
        ### Large speech models and Next-generation models
         The service supports large speech models and next-generation `Multimedia` (16
        kHz) and `Telephony` (8 kHz) models for many languages. Large speech models and
        next-generation models have higher throughput than the service's previous
        generation of `Broadband` and `Narrowband` models. When you use large speech
        models and next-generation models, the service can return transcriptions more
        quickly and also provide noticeably better transcription accuracy.
        You specify a large speech model or next-generation model by using the `model`
        query parameter, as you do a previous-generation model. Only the next-generation
        models support the `low_latency` parameter, and all large speech models and
        next-generation models support the `character_insertion_bias` parameter. These
        parameters are not available with previous-generation models.
        Large speech models and next-generation models do not support all of the speech
        recognition parameters that are available for use with previous-generation models.
        Next-generation models do not support the following parameters:
        * `acoustic_customization_id`
        * `keywords` and `keywords_threshold`
        * `processing_metrics` and `processing_metrics_interval`
        * `word_alternatives_threshold`
        **Important:** Effective **31 July 2023**, all previous-generation models will be
        removed from the service and the documentation. Most previous-generation models
        were deprecated on 15 March 2022. You must migrate to the equivalent large speech
        model or next-generation model by 31 July 2023. For more information, see
        [Migrating to large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-migrate).
        **See also:**
        * [Large speech languages and
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-large-speech-languages)
        * [Supported features for large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-large-speech-languages#models-lsm-supported-features)
        * [Next-generation languages and
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng)
        * [Supported features for next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng#models-ng-features)
        ### Multipart speech recognition
         **Note:** The asynchronous HTTP interface, WebSocket interface, and Watson SDKs
        do not support multipart speech recognition.
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
        request](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-http#HTTP-multi).

        :param BinaryIO audio: The audio to transcribe.
        :param str content_type: (optional) The format (MIME type) of the audio.
               For more information about specifying an audio format, see **Audio formats
               (content types)** in the method description.
        :param str model: (optional) The model to use for speech recognition. If
               you omit the `model` parameter, the service uses the US English
               `en-US_BroadbandModel` by default.
               _For IBM Cloud Pak for Data,_ if you do not install the
               `en-US_BroadbandModel`, you must either specify a model with the request or
               specify a new default model for your installation of the service.
               **See also:**
               * [Using a model for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use)
               * [Using the default
               model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use#models-use-default).
        :param bool speech_begin_event: (optional) If `true`, the service returns a
               response object `SpeechActivity` which contains the time when a speech
               activity is detected in the stream. This can be used both in standard and
               low latency mode. This feature enables client applications to know that
               some words/speech has been detected and the service is in the process of
               decoding. This can be used in lieu of interim results in standard mode. See
               [Using speech recognition
               parameters](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-service-features#features-parameters).
        :param str language_customization_id: (optional) The customization ID
               (GUID) of a custom language model that is to be used with the recognition
               request. The base model of the specified custom language model must match
               the model specified with the `model` parameter. You must make the request
               with credentials for the instance of the service that owns the custom
               model. By default, no custom language model is used. See [Using a custom
               language model for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageUse).
               **Note:** Use this parameter instead of the deprecated `customization_id`
               parameter.
        :param str acoustic_customization_id: (optional) The customization ID
               (GUID) of a custom acoustic model that is to be used with the recognition
               request. The base model of the specified custom acoustic model must match
               the model specified with the `model` parameter. You must make the request
               with credentials for the instance of the service that owns the custom
               model. By default, no custom acoustic model is used. See [Using a custom
               acoustic model for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-acousticUse).
        :param str base_model_version: (optional) The version of the specified base
               model that is to be used with the recognition request. Multiple versions of
               a base model can exist when a model is updated for internal improvements.
               The parameter is intended primarily for use with custom models that have
               been upgraded for a new base model. The default value depends on whether
               the parameter is used with or without a custom model. See [Making speech
               recognition requests with upgraded custom
               models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade-use#custom-upgrade-use-recognition).
        :param float customization_weight: (optional) If you specify the
               customization ID (GUID) of a custom language model with the recognition
               request, the customization weight tells the service how much weight to give
               to words from the custom language model compared to those from the base
               model for the current request.
               Specify a value between 0.0 and 1.0. Unless a different customization
               weight was specified for the custom model when the model was trained, the
               default value is:
               * 0.5 for large speech models
               * 0.3 for previous-generation models
               * 0.2 for most next-generation models
               * 0.1 for next-generation English and Japanese models
               A customization weight that you specify overrides a weight that was
               specified when the custom model was trained. The default value yields the
               best performance in general. Assign a higher value if your audio makes
               frequent use of OOV words from the custom model. Use caution when setting
               the weight: a higher value can improve the accuracy of phrases from the
               custom model's domain, but it can negatively affect performance on
               non-domain phrases.
               See [Using customization
               weight](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageUse#weight).
        :param int inactivity_timeout: (optional) The time in seconds after which,
               if only silence (no speech) is detected in streaming audio, the connection
               is closed with a 400 error. The parameter is useful for stopping audio
               submission from a live microphone when a user simply walks away. Use `-1`
               for infinity. See [Inactivity
               timeout](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#timeouts-inactivity).
        :param List[str] keywords: (optional) An array of keyword strings to spot
               in the audio. Each keyword string can include one or more string tokens.
               Keywords are spotted only in the final results, not in interim hypotheses.
               If you specify any keywords, you must also specify a keywords threshold.
               Omit the parameter or specify an empty array if you do not need to spot
               keywords.
               You can spot a maximum of 1000 keywords with a single request. A single
               keyword can have a maximum length of 1024 characters, though the maximum
               effective length for double-byte languages might be shorter. Keywords are
               case-insensitive.
               See [Keyword
               spotting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-spotting#keyword-spotting).
        :param float keywords_threshold: (optional) A confidence value that is the
               lower bound for spotting a keyword. A word is considered to match a keyword
               if its confidence is greater than or equal to the threshold. Specify a
               probability between 0.0 and 1.0. If you specify a threshold, you must also
               specify one or more keywords. The service performs no keyword spotting if
               you omit either parameter. See [Keyword
               spotting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-spotting#keyword-spotting).
        :param int max_alternatives: (optional) The maximum number of alternative
               transcripts that the service is to return. By default, the service returns
               a single transcript. If you specify a value of `0`, the service uses the
               default value, `1`. See [Maximum
               alternatives](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metadata#max-alternatives).
        :param float word_alternatives_threshold: (optional) A confidence value
               that is the lower bound for identifying a hypothesis as a possible word
               alternative (also known as "Confusion Networks"). An alternative word is
               considered if its confidence is greater than or equal to the threshold.
               Specify a probability between 0.0 and 1.0. By default, the service computes
               no alternative words. See [Word
               alternatives](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-spotting#word-alternatives).
        :param bool word_confidence: (optional) If `true`, the service returns a
               confidence measure in the range of 0.0 to 1.0 for each word. By default,
               the service returns no word confidence scores. See [Word
               confidence](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metadata#word-confidence).
        :param bool timestamps: (optional) If `true`, the service returns time
               alignment for each word. By default, no timestamps are returned. See [Word
               timestamps](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metadata#word-timestamps).
        :param bool profanity_filter: (optional) If `true`, the service filters
               profanity from all output except for keyword results by replacing
               inappropriate words with a series of asterisks. Set the parameter to
               `false` to return results with no censoring.
               **Note:** The parameter can be used with US English and Japanese
               transcription only. See [Profanity
               filtering](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#profanity-filtering).
        :param bool smart_formatting: (optional) If `true`, the service converts
               dates, times, series of digits and numbers, phone numbers, currency values,
               and internet addresses into more readable, conventional representations in
               the final transcript of a recognition request. For US English, the service
               also converts certain keyword strings to punctuation symbols. By default,
               the service performs no smart formatting.
               **Note:** The parameter can be used with US English, Japanese, and Spanish
               (all dialects) transcription only.
               See [Smart
               formatting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#smart-formatting).
        :param int smart_formatting_version: (optional) Smart formatting version
               for large speech models and next-generation models is supported in US
               English, Brazilian Portuguese, French, German, Spanish and French Canadian
               languages.
        :param bool speaker_labels: (optional) If `true`, the response includes
               labels that identify which words were spoken by which participants in a
               multi-person exchange. By default, the service returns no speaker labels.
               Setting `speaker_labels` to `true` forces the `timestamps` parameter to be
               `true`, regardless of whether you specify `false` for the parameter.
               * _For previous-generation models,_ the parameter can be used with
               Australian English, US English, German, Japanese, Korean, and Spanish (both
               broadband and narrowband models) and UK English (narrowband model)
               transcription only.
               * _For large speech models and next-generation models,_ the parameter can
               be used with all available languages.
               See [Speaker
               labels](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-speaker-labels).
        :param str grammar_name: (optional) The name of a grammar that is to be
               used with the recognition request. If you specify a grammar, you must also
               use the `language_customization_id` parameter to specify the name of the
               custom language model for which the grammar is defined. The service
               recognizes only strings that are recognized by the specified grammar; it
               does not recognize other custom words from the model's words resource.
               See [Using a grammar for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-grammarUse).
        :param bool redaction: (optional) If `true`, the service redacts, or masks,
               numeric data from final transcripts. The feature redacts any number that
               has three or more consecutive digits by replacing each digit with an `X`
               character. It is intended to redact sensitive numeric data, such as credit
               card numbers. By default, the service performs no redaction.
               When you enable redaction, the service automatically enables smart
               formatting, regardless of whether you explicitly disable that feature. To
               ensure maximum security, the service also disables keyword spotting
               (ignores the `keywords` and `keywords_threshold` parameters) and returns
               only a single final transcript (forces the `max_alternatives` parameter to
               be `1`).
               **Note:** The parameter can be used with US English, Japanese, and Korean
               transcription only.
               See [Numeric
               redaction](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#numeric-redaction).
        :param bool audio_metrics: (optional) If `true`, requests detailed
               information about the signal characteristics of the input audio. The
               service returns audio metrics with the final transcription results. By
               default, the service returns no audio metrics.
               See [Audio
               metrics](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metrics#audio-metrics).
        :param float end_of_phrase_silence_time: (optional) Specifies the duration
               of the pause interval at which the service splits a transcript into
               multiple final results. If the service detects pauses or extended silence
               before it reaches the end of the audio stream, its response can include
               multiple final results. Silence indicates a point at which the speaker
               pauses between spoken words or phrases.
               Specify a value for the pause interval in the range of 0.0 to 120.0.
               * A value greater than 0 specifies the interval that the service is to use
               for speech recognition.
               * A value of 0 indicates that the service is to use the default interval.
               It is equivalent to omitting the parameter.
               The default pause interval for most languages is 0.8 seconds; the default
               for Chinese is 0.6 seconds.
               See [End of phrase silence
               time](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#silence-time).
        :param bool split_transcript_at_phrase_end: (optional) If `true`, directs
               the service to split the transcript into multiple final results based on
               semantic features of the input, for example, at the conclusion of
               meaningful phrases such as sentences. The service bases its understanding
               of semantic features on the base language model that you use with a
               request. Custom language models and grammars can also influence how and
               where the service splits a transcript.
               By default, the service splits transcripts based solely on the pause
               interval. If the parameters are used together on the same request,
               `end_of_phrase_silence_time` has precedence over
               `split_transcript_at_phrase_end`.
               See [Split transcript at phrase
               end](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#split-transcript).
        :param float speech_detector_sensitivity: (optional) The sensitivity of
               speech activity detection that the service is to perform. Use the parameter
               to suppress word insertions from music, coughing, and other non-speech
               events. The service biases the audio it passes for speech recognition by
               evaluating the input audio against prior models of speech and non-speech
               activity.
               Specify a value between 0.0 and 1.0:
               * 0.0 suppresses all audio (no speech is transcribed).
               * 0.5 (the default) provides a reasonable compromise for the level of
               sensitivity.
               * 1.0 suppresses no audio (speech detection sensitivity is disabled).
               The values increase on a monotonic curve. Specifying one or two decimal
               places of precision (for example, `0.55`) is typically more than
               sufficient.
               The parameter is supported with all large speech models, next-generation
               models and with most previous-generation models. See [Speech detector
               sensitivity](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-parameters-sensitivity)
               and [Language model
               support](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-support).
        :param float background_audio_suppression: (optional) The level to which
               the service is to suppress background audio based on its volume to prevent
               it from being transcribed as speech. Use the parameter to suppress side
               conversations or background noise.
               Specify a value in the range of 0.0 to 1.0:
               * 0.0 (the default) provides no suppression (background audio suppression
               is disabled).
               * 0.5 provides a reasonable level of audio suppression for general usage.
               * 1.0 suppresses all audio (no audio is transcribed).
               The values increase on a monotonic curve. Specifying one or two decimal
               places of precision (for example, `0.55`) is typically more than
               sufficient.
               The parameter is supported with all large speech models, next-generation
               models and with most previous-generation models. See [Background audio
               suppression](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-parameters-suppression)
               and [Language model
               support](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-support).
        :param bool low_latency: (optional) If `true` for next-generation
               `Multimedia` and `Telephony` models that support low latency, directs the
               service to produce results even more quickly than it usually does.
               Next-generation models produce transcription results faster than
               previous-generation models. The `low_latency` parameter causes the models
               to produce results even more quickly, though the results might be less
               accurate when the parameter is used.
               The parameter is not available for large speech models and
               previous-generation `Broadband` and `Narrowband` models. It is available
               for most next-generation models.
               * For a list of next-generation models that support low latency, see
               [Supported next-generation language
               models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng#models-ng-supported).
               * For more information about the `low_latency` parameter, see [Low
               latency](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-interim#low-latency).
        :param float character_insertion_bias: (optional) For large speech models
               and next-generation models, an indication of whether the service is biased
               to recognize shorter or longer strings of characters when developing
               transcription hypotheses. By default, the service is optimized to produce
               the best balance of strings of different lengths.
               The default bias is 0.0. The allowable range of values is -1.0 to 1.0.
               * Negative values bias the service to favor hypotheses with shorter strings
               of characters.
               * Positive values bias the service to favor hypotheses with longer strings
               of characters.
               As the value approaches -1.0 or 1.0, the impact of the parameter becomes
               more pronounced. To determine the most effective value for your scenario,
               start by setting the value of the parameter to a small increment, such as
               -0.1, -0.05, 0.05, or 0.1, and assess how the value impacts the
               transcription results. Then experiment with different values as necessary,
               adjusting the value by small increments.
               The parameter is not available for previous-generation models.
               See [Character insertion
               bias](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#insertion-bias).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SpeechRecognitionResults` object
        """

        if audio is None:
            raise ValueError('audio must be provided')
        headers = {
            'Content-Type': content_type,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='recognize',
        )
        headers.update(sdk_headers)

        params = {
            'model': model,
            'speech_begin_event': speech_begin_event,
            'language_customization_id': language_customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'base_model_version': base_model_version,
            'customization_weight': customization_weight,
            'inactivity_timeout': inactivity_timeout,
            'keywords': convert_list(keywords),
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'smart_formatting_version': smart_formatting_version,
            'speaker_labels': speaker_labels,
            'grammar_name': grammar_name,
            'redaction': redaction,
            'audio_metrics': audio_metrics,
            'end_of_phrase_silence_time': end_of_phrase_silence_time,
            'split_transcript_at_phrase_end': split_transcript_at_phrase_end,
            'speech_detector_sensitivity': speech_detector_sensitivity,
            'background_audio_suppression': background_audio_suppression,
            'low_latency': low_latency,
            'character_insertion_bias': character_insertion_bias,
        }

        data = audio

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/recognize'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Asynchronous
    #########################

    def register_callback(
        self,
        callback_url: str,
        *,
        user_secret: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Register a callback.

        Registers a callback URL with the service for use with subsequent asynchronous
        recognition requests. The service attempts to register, or allowlist, the callback
        URL if it is not already registered by sending a `GET` request to the callback
        URL. The service passes a random alphanumeric challenge string via the
        `challenge_string` parameter of the request. The request includes an `Accept`
        header that specifies `text/plain` as the required response type.
        To be registered successfully, the callback URL must respond to the `GET` request
        from the service. The response must send status code 200 and must include the
        challenge string in its body. Set the `Content-Type` response header to
        `text/plain`. Upon receiving this response, the service responds to the original
        registration request with response code 201.
        The service sends only a single `GET` request to the callback URL. If the service
        does not receive a reply with a response code of 200 and a body that echoes the
        challenge string sent by the service within five seconds, it does not allowlist
        the URL; it instead sends status code 400 in response to the request to register a
        callback. If the requested callback URL is already allowlisted, the service
        responds to the initial registration request with response code 200.
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
        URL](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-async#register).

        :param str callback_url: An HTTP or HTTPS URL to which callback
               notifications are to be sent. To be allowlisted, the URL must successfully
               echo the challenge string during URL verification. During verification, the
               client can also check the signature that the service sends in the
               `X-Callback-Signature` header to verify the origin of the request.
        :param str user_secret: (optional) A user-specified string that the service
               uses to generate the HMAC-SHA1 signature that it sends via the
               `X-Callback-Signature` header. The service includes the header during URL
               verification and with every notification sent to the callback URL. It
               calculates the signature over the payload of the notification. If you omit
               the parameter, the service does not send the header.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RegisterStatus` object
        """

        if not callback_url:
            raise ValueError('callback_url must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='register_callback',
        )
        headers.update(sdk_headers)

        params = {
            'callback_url': callback_url,
            'user_secret': user_secret,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/register_callback'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def unregister_callback(
        self,
        callback_url: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Unregister a callback.

        Unregisters a callback URL that was previously allowlisted with a [Register a
        callback](#registercallback) request for use with the asynchronous interface. Once
        unregistered, the URL can no longer be used with asynchronous recognition
        requests.
        **See also:** [Unregistering a callback
        URL](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-async#unregister).

        :param str callback_url: The callback URL that is to be unregistered.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not callback_url:
            raise ValueError('callback_url must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='unregister_callback',
        )
        headers.update(sdk_headers)

        params = {
            'callback_url': callback_url,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/v1/unregister_callback'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_job(
        self,
        audio: BinaryIO,
        *,
        content_type: Optional[str] = None,
        model: Optional[str] = None,
        callback_url: Optional[str] = None,
        events: Optional[str] = None,
        user_token: Optional[str] = None,
        results_ttl: Optional[int] = None,
        language_customization_id: Optional[str] = None,
        acoustic_customization_id: Optional[str] = None,
        base_model_version: Optional[str] = None,
        customization_weight: Optional[float] = None,
        inactivity_timeout: Optional[int] = None,
        keywords: Optional[List[str]] = None,
        keywords_threshold: Optional[float] = None,
        max_alternatives: Optional[int] = None,
        word_alternatives_threshold: Optional[float] = None,
        word_confidence: Optional[bool] = None,
        timestamps: Optional[bool] = None,
        profanity_filter: Optional[bool] = None,
        smart_formatting: Optional[bool] = None,
        smart_formatting_version: Optional[int] = None,
        speaker_labels: Optional[bool] = None,
        grammar_name: Optional[str] = None,
        redaction: Optional[bool] = None,
        processing_metrics: Optional[bool] = None,
        processing_metrics_interval: Optional[float] = None,
        audio_metrics: Optional[bool] = None,
        end_of_phrase_silence_time: Optional[float] = None,
        split_transcript_at_phrase_end: Optional[bool] = None,
        speech_detector_sensitivity: Optional[float] = None,
        background_audio_suppression: Optional[float] = None,
        low_latency: Optional[bool] = None,
        character_insertion_bias: Optional[float] = None,
        **kwargs,
    ) -> DetailedResponse:
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
        parameters. You must then use the [Check jobs](#checkjobs) or [Check a
        job](#checkjob) methods to check the status of the job, using the latter to
        retrieve the results when the job is complete.
        The two approaches are not mutually exclusive. You can poll the service for job
        status or obtain results from the service manually even if you include a callback
        URL. In both cases, you can include the `results_ttl` parameter to specify how
        long the results are to remain available after the job is complete. Using the
        HTTPS [Check a job](#checkjob) method to retrieve results is more secure than
        receiving them via callback notification over HTTP because it provides
        confidentiality in addition to authentication and data integrity.
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
        job](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-async#create).
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
        transmission](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#transmission)
        *
        [Timeouts](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#timeouts)
        ### Audio formats (content types)
         The service accepts audio in the following formats (MIME types).
        * For formats that are labeled **Required**, you must use the `Content-Type`
        header with the request to specify the format of the audio.
        * For all other formats, you can omit the `Content-Type` header or specify
        `application/octet-stream` with the header to have the service automatically
        detect the format of the audio. (With the `curl` command, you can specify either
        `"Content-Type:"` or `"Content-Type: application/octet-stream"`.)
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
         **See also:** [Supported audio
        formats](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-audio-formats).
        ### Large speech models and Next-generation models
         The service supports large speech models and next-generation `Multimedia` (16
        kHz) and `Telephony` (8 kHz) models for many languages. Large speech models and
        next-generation models have higher throughput than the service's previous
        generation of `Broadband` and `Narrowband` models. When you use large speech
        models and next-generation models, the service can return transcriptions more
        quickly and also provide noticeably better transcription accuracy.
        You specify a large speech model or next-generation model by using the `model`
        query parameter, as you do a previous-generation model. Only the next-generation
        models support the `low_latency` parameter, and all large speech models and
        next-generation models support the `character_insertion_bias` parameter. These
        parameters are not available with previous-generation models.
        Large speech models and next-generation models do not support all of the speech
        recognition parameters that are available for use with previous-generation models.
        Next-generation models do not support the following parameters:
        * `acoustic_customization_id`
        * `keywords` and `keywords_threshold`
        * `processing_metrics` and `processing_metrics_interval`
        * `word_alternatives_threshold`
        **Important:** Effective **31 July 2023**, all previous-generation models will be
        removed from the service and the documentation. Most previous-generation models
        were deprecated on 15 March 2022. You must migrate to the equivalent large speech
        model or next-generation model by 31 July 2023. For more information, see
        [Migrating to large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-migrate).
        **See also:**
        * [Large speech languages and
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-large-speech-languages)
        * [Supported features for large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-large-speech-languages#models-lsm-supported-features)
        * [Next-generation languages and
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng)
        * [Supported features for next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng#models-ng-features).

        :param BinaryIO audio: The audio to transcribe.
        :param str content_type: (optional) The format (MIME type) of the audio.
               For more information about specifying an audio format, see **Audio formats
               (content types)** in the method description.
        :param str model: (optional) The model to use for speech recognition. If
               you omit the `model` parameter, the service uses the US English
               `en-US_BroadbandModel` by default.
               _For IBM Cloud Pak for Data,_ if you do not install the
               `en-US_BroadbandModel`, you must either specify a model with the request or
               specify a new default model for your installation of the service.
               **See also:**
               * [Using a model for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use)
               * [Using the default
               model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use#models-use-default).
        :param str callback_url: (optional) A URL to which callback notifications
               are to be sent. The URL must already be successfully allowlisted by using
               the [Register a callback](#registercallback) method. You can include the
               same callback URL with any number of job creation requests. Omit the
               parameter to poll the service for job completion and results.
               Use the `user_token` parameter to specify a unique user-specified string
               with each job to differentiate the callback notifications for the jobs.
        :param str events: (optional) If the job includes a callback URL, a
               comma-separated list of notification events to which to subscribe. Valid
               events are
               * `recognitions.started` generates a callback notification when the service
               begins to process the job.
               * `recognitions.completed` generates a callback notification when the job
               is complete. You must use the [Check a job](#checkjob) method to retrieve
               the results before they time out or are deleted.
               * `recognitions.completed_with_results` generates a callback notification
               when the job is complete. The notification includes the results of the
               request.
               * `recognitions.failed` generates a callback notification if the service
               experiences an error while processing the job.
               The `recognitions.completed` and `recognitions.completed_with_results`
               events are incompatible. You can specify only of the two events.
               If the job includes a callback URL, omit the parameter to subscribe to the
               default events: `recognitions.started`, `recognitions.completed`, and
               `recognitions.failed`. If the job does not include a callback URL, omit the
               parameter.
        :param str user_token: (optional) If the job includes a callback URL, a
               user-specified string that the service is to include with each callback
               notification for the job; the token allows the user to maintain an internal
               mapping between jobs and notification events. If the job does not include a
               callback URL, omit the parameter.
        :param int results_ttl: (optional) The number of minutes for which the
               results are to be available after the job has finished. If not delivered
               via a callback, the results must be retrieved within this time. Omit the
               parameter to use a time to live of one week. The parameter is valid with or
               without a callback URL.
        :param str language_customization_id: (optional) The customization ID
               (GUID) of a custom language model that is to be used with the recognition
               request. The base model of the specified custom language model must match
               the model specified with the `model` parameter. You must make the request
               with credentials for the instance of the service that owns the custom
               model. By default, no custom language model is used. See [Using a custom
               language model for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageUse).
               **Note:** Use this parameter instead of the deprecated `customization_id`
               parameter.
        :param str acoustic_customization_id: (optional) The customization ID
               (GUID) of a custom acoustic model that is to be used with the recognition
               request. The base model of the specified custom acoustic model must match
               the model specified with the `model` parameter. You must make the request
               with credentials for the instance of the service that owns the custom
               model. By default, no custom acoustic model is used. See [Using a custom
               acoustic model for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-acousticUse).
        :param str base_model_version: (optional) The version of the specified base
               model that is to be used with the recognition request. Multiple versions of
               a base model can exist when a model is updated for internal improvements.
               The parameter is intended primarily for use with custom models that have
               been upgraded for a new base model. The default value depends on whether
               the parameter is used with or without a custom model. See [Making speech
               recognition requests with upgraded custom
               models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade-use#custom-upgrade-use-recognition).
        :param float customization_weight: (optional) If you specify the
               customization ID (GUID) of a custom language model with the recognition
               request, the customization weight tells the service how much weight to give
               to words from the custom language model compared to those from the base
               model for the current request.
               Specify a value between 0.0 and 1.0. Unless a different customization
               weight was specified for the custom model when the model was trained, the
               default value is:
               * 0.5 for large speech models
               * 0.3 for previous-generation models
               * 0.2 for most next-generation models
               * 0.1 for next-generation English and Japanese models
               A customization weight that you specify overrides a weight that was
               specified when the custom model was trained. The default value yields the
               best performance in general. Assign a higher value if your audio makes
               frequent use of OOV words from the custom model. Use caution when setting
               the weight: a higher value can improve the accuracy of phrases from the
               custom model's domain, but it can negatively affect performance on
               non-domain phrases.
               See [Using customization
               weight](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageUse#weight).
        :param int inactivity_timeout: (optional) The time in seconds after which,
               if only silence (no speech) is detected in streaming audio, the connection
               is closed with a 400 error. The parameter is useful for stopping audio
               submission from a live microphone when a user simply walks away. Use `-1`
               for infinity. See [Inactivity
               timeout](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#timeouts-inactivity).
        :param List[str] keywords: (optional) An array of keyword strings to spot
               in the audio. Each keyword string can include one or more string tokens.
               Keywords are spotted only in the final results, not in interim hypotheses.
               If you specify any keywords, you must also specify a keywords threshold.
               Omit the parameter or specify an empty array if you do not need to spot
               keywords.
               You can spot a maximum of 1000 keywords with a single request. A single
               keyword can have a maximum length of 1024 characters, though the maximum
               effective length for double-byte languages might be shorter. Keywords are
               case-insensitive.
               See [Keyword
               spotting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-spotting#keyword-spotting).
        :param float keywords_threshold: (optional) A confidence value that is the
               lower bound for spotting a keyword. A word is considered to match a keyword
               if its confidence is greater than or equal to the threshold. Specify a
               probability between 0.0 and 1.0. If you specify a threshold, you must also
               specify one or more keywords. The service performs no keyword spotting if
               you omit either parameter. See [Keyword
               spotting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-spotting#keyword-spotting).
        :param int max_alternatives: (optional) The maximum number of alternative
               transcripts that the service is to return. By default, the service returns
               a single transcript. If you specify a value of `0`, the service uses the
               default value, `1`. See [Maximum
               alternatives](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metadata#max-alternatives).
        :param float word_alternatives_threshold: (optional) A confidence value
               that is the lower bound for identifying a hypothesis as a possible word
               alternative (also known as "Confusion Networks"). An alternative word is
               considered if its confidence is greater than or equal to the threshold.
               Specify a probability between 0.0 and 1.0. By default, the service computes
               no alternative words. See [Word
               alternatives](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-spotting#word-alternatives).
        :param bool word_confidence: (optional) If `true`, the service returns a
               confidence measure in the range of 0.0 to 1.0 for each word. By default,
               the service returns no word confidence scores. See [Word
               confidence](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metadata#word-confidence).
        :param bool timestamps: (optional) If `true`, the service returns time
               alignment for each word. By default, no timestamps are returned. See [Word
               timestamps](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metadata#word-timestamps).
        :param bool profanity_filter: (optional) If `true`, the service filters
               profanity from all output except for keyword results by replacing
               inappropriate words with a series of asterisks. Set the parameter to
               `false` to return results with no censoring.
               **Note:** The parameter can be used with US English and Japanese
               transcription only. See [Profanity
               filtering](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#profanity-filtering).
        :param bool smart_formatting: (optional) If `true`, the service converts
               dates, times, series of digits and numbers, phone numbers, currency values,
               and internet addresses into more readable, conventional representations in
               the final transcript of a recognition request. For US English, the service
               also converts certain keyword strings to punctuation symbols. By default,
               the service performs no smart formatting.
               **Note:** The parameter can be used with US English, Japanese, and Spanish
               (all dialects) transcription only.
               See [Smart
               formatting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#smart-formatting).
        :param int smart_formatting_version: (optional) Smart formatting version
               for large speech models and next-generation models is supported in US
               English, Brazilian Portuguese, French, German, Spanish and French Canadian
               languages.
        :param bool speaker_labels: (optional) If `true`, the response includes
               labels that identify which words were spoken by which participants in a
               multi-person exchange. By default, the service returns no speaker labels.
               Setting `speaker_labels` to `true` forces the `timestamps` parameter to be
               `true`, regardless of whether you specify `false` for the parameter.
               * _For previous-generation models,_ the parameter can be used with
               Australian English, US English, German, Japanese, Korean, and Spanish (both
               broadband and narrowband models) and UK English (narrowband model)
               transcription only.
               * _For large speech models and next-generation models,_ the parameter can
               be used with all available languages.
               See [Speaker
               labels](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-speaker-labels).
        :param str grammar_name: (optional) The name of a grammar that is to be
               used with the recognition request. If you specify a grammar, you must also
               use the `language_customization_id` parameter to specify the name of the
               custom language model for which the grammar is defined. The service
               recognizes only strings that are recognized by the specified grammar; it
               does not recognize other custom words from the model's words resource.
               See [Using a grammar for speech
               recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-grammarUse).
        :param bool redaction: (optional) If `true`, the service redacts, or masks,
               numeric data from final transcripts. The feature redacts any number that
               has three or more consecutive digits by replacing each digit with an `X`
               character. It is intended to redact sensitive numeric data, such as credit
               card numbers. By default, the service performs no redaction.
               When you enable redaction, the service automatically enables smart
               formatting, regardless of whether you explicitly disable that feature. To
               ensure maximum security, the service also disables keyword spotting
               (ignores the `keywords` and `keywords_threshold` parameters) and returns
               only a single final transcript (forces the `max_alternatives` parameter to
               be `1`).
               **Note:** The parameter can be used with US English, Japanese, and Korean
               transcription only.
               See [Numeric
               redaction](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#numeric-redaction).
        :param bool processing_metrics: (optional) If `true`, requests processing
               metrics about the service's transcription of the input audio. The service
               returns processing metrics at the interval specified by the
               `processing_metrics_interval` parameter. It also returns processing metrics
               for transcription events, for example, for final and interim results. By
               default, the service returns no processing metrics.
               See [Processing
               metrics](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metrics#processing-metrics).
        :param float processing_metrics_interval: (optional) Specifies the interval
               in real wall-clock seconds at which the service is to return processing
               metrics. The parameter is ignored unless the `processing_metrics` parameter
               is set to `true`.
               The parameter accepts a minimum value of 0.1 seconds. The level of
               precision is not restricted, so you can specify values such as 0.25 and
               0.125.
               The service does not impose a maximum value. If you want to receive
               processing metrics only for transcription events instead of at periodic
               intervals, set the value to a large number. If the value is larger than the
               duration of the audio, the service returns processing metrics only for
               transcription events.
               See [Processing
               metrics](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metrics#processing-metrics).
        :param bool audio_metrics: (optional) If `true`, requests detailed
               information about the signal characteristics of the input audio. The
               service returns audio metrics with the final transcription results. By
               default, the service returns no audio metrics.
               See [Audio
               metrics](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metrics#audio-metrics).
        :param float end_of_phrase_silence_time: (optional) Specifies the duration
               of the pause interval at which the service splits a transcript into
               multiple final results. If the service detects pauses or extended silence
               before it reaches the end of the audio stream, its response can include
               multiple final results. Silence indicates a point at which the speaker
               pauses between spoken words or phrases.
               Specify a value for the pause interval in the range of 0.0 to 120.0.
               * A value greater than 0 specifies the interval that the service is to use
               for speech recognition.
               * A value of 0 indicates that the service is to use the default interval.
               It is equivalent to omitting the parameter.
               The default pause interval for most languages is 0.8 seconds; the default
               for Chinese is 0.6 seconds.
               See [End of phrase silence
               time](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#silence-time).
        :param bool split_transcript_at_phrase_end: (optional) If `true`, directs
               the service to split the transcript into multiple final results based on
               semantic features of the input, for example, at the conclusion of
               meaningful phrases such as sentences. The service bases its understanding
               of semantic features on the base language model that you use with a
               request. Custom language models and grammars can also influence how and
               where the service splits a transcript.
               By default, the service splits transcripts based solely on the pause
               interval. If the parameters are used together on the same request,
               `end_of_phrase_silence_time` has precedence over
               `split_transcript_at_phrase_end`.
               See [Split transcript at phrase
               end](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#split-transcript).
        :param float speech_detector_sensitivity: (optional) The sensitivity of
               speech activity detection that the service is to perform. Use the parameter
               to suppress word insertions from music, coughing, and other non-speech
               events. The service biases the audio it passes for speech recognition by
               evaluating the input audio against prior models of speech and non-speech
               activity.
               Specify a value between 0.0 and 1.0:
               * 0.0 suppresses all audio (no speech is transcribed).
               * 0.5 (the default) provides a reasonable compromise for the level of
               sensitivity.
               * 1.0 suppresses no audio (speech detection sensitivity is disabled).
               The values increase on a monotonic curve. Specifying one or two decimal
               places of precision (for example, `0.55`) is typically more than
               sufficient.
               The parameter is supported with all large speech models, next-generation
               models and with most previous-generation models. See [Speech detector
               sensitivity](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-parameters-sensitivity)
               and [Language model
               support](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-support).
        :param float background_audio_suppression: (optional) The level to which
               the service is to suppress background audio based on its volume to prevent
               it from being transcribed as speech. Use the parameter to suppress side
               conversations or background noise.
               Specify a value in the range of 0.0 to 1.0:
               * 0.0 (the default) provides no suppression (background audio suppression
               is disabled).
               * 0.5 provides a reasonable level of audio suppression for general usage.
               * 1.0 suppresses all audio (no audio is transcribed).
               The values increase on a monotonic curve. Specifying one or two decimal
               places of precision (for example, `0.55`) is typically more than
               sufficient.
               The parameter is supported with all large speech models, next-generation
               models and with most previous-generation models. See [Background audio
               suppression](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-parameters-suppression)
               and [Language model
               support](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-support).
        :param bool low_latency: (optional) If `true` for next-generation
               `Multimedia` and `Telephony` models that support low latency, directs the
               service to produce results even more quickly than it usually does.
               Next-generation models produce transcription results faster than
               previous-generation models. The `low_latency` parameter causes the models
               to produce results even more quickly, though the results might be less
               accurate when the parameter is used.
               The parameter is not available for large speech models and
               previous-generation `Broadband` and `Narrowband` models. It is available
               for most next-generation models.
               * For a list of next-generation models that support low latency, see
               [Supported next-generation language
               models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng#models-ng-supported).
               * For more information about the `low_latency` parameter, see [Low
               latency](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-interim#low-latency).
        :param float character_insertion_bias: (optional) For large speech models
               and next-generation models, an indication of whether the service is biased
               to recognize shorter or longer strings of characters when developing
               transcription hypotheses. By default, the service is optimized to produce
               the best balance of strings of different lengths.
               The default bias is 0.0. The allowable range of values is -1.0 to 1.0.
               * Negative values bias the service to favor hypotheses with shorter strings
               of characters.
               * Positive values bias the service to favor hypotheses with longer strings
               of characters.
               As the value approaches -1.0 or 1.0, the impact of the parameter becomes
               more pronounced. To determine the most effective value for your scenario,
               start by setting the value of the parameter to a small increment, such as
               -0.1, -0.05, 0.05, or 0.1, and assess how the value impacts the
               transcription results. Then experiment with different values as necessary,
               adjusting the value by small increments.
               The parameter is not available for previous-generation models.
               See [Character insertion
               bias](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#insertion-bias).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RecognitionJob` object
        """

        if audio is None:
            raise ValueError('audio must be provided')
        headers = {
            'Content-Type': content_type,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_job',
        )
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
            'keywords': convert_list(keywords),
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'smart_formatting_version': smart_formatting_version,
            'speaker_labels': speaker_labels,
            'grammar_name': grammar_name,
            'redaction': redaction,
            'processing_metrics': processing_metrics,
            'processing_metrics_interval': processing_metrics_interval,
            'audio_metrics': audio_metrics,
            'end_of_phrase_silence_time': end_of_phrase_silence_time,
            'split_transcript_at_phrase_end': split_transcript_at_phrase_end,
            'speech_detector_sensitivity': speech_detector_sensitivity,
            'background_audio_suppression': background_audio_suppression,
            'low_latency': low_latency,
            'character_insertion_bias': character_insertion_bias,
        }

        data = audio

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/recognitions'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def check_jobs(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Check jobs.

        Returns the ID and status of the latest 100 outstanding jobs associated with the
        credentials with which it is called. The method also returns the creation and
        update times of each job, and, if a job was created with a callback URL and a user
        token, the user token for the job. To obtain the results for a job whose status is
        `completed` or not one of the latest 100 outstanding jobs, use the [Check a
        job[(#checkjob) method. A job and its results remain available until you delete
        them with the [Delete a job](#deletejob) method or until the job's time to live
        expires, whichever comes first.
        **See also:** [Checking the status of the latest
        jobs](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-async#jobs).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RecognitionJobs` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='check_jobs',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/recognitions'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def check_job(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
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
        available. Use the [Check jobs](#checkjobs) method to request information about
        the most recent jobs associated with the calling credentials.
        **See also:** [Checking the status and retrieving the results of a
        job](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-async#job).

        :param str id: The identifier of the asynchronous job that is to be used
               for the request. You must make the request with credentials for the
               instance of the service that owns the job.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RecognitionJob` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='check_job',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/recognitions/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_job(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a job.

        Deletes the specified job. You cannot delete a job that the service is actively
        processing. Once you delete a job, its results are no longer available. The
        service automatically deletes a job and its results when the time to live for the
        results expires. You must use credentials for the instance of the service that
        owns a job to delete it.
        **See also:** [Deleting a
        job](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-async#delete-async).

        :param str id: The identifier of the asynchronous job that is to be used
               for the request. You must make the request with credentials for the
               instance of the service that owns the job.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_job',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/recognitions/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom language models
    #########################

    def create_language_model(
        self,
        name: str,
        base_model_name: str,
        *,
        dialect: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom language model.

        Creates a new custom language model for a specified base model. The custom
        language model can be used only with the base model for which it is created. The
        model is owned by the instance of the service whose credentials are used to create
        it.
        You can create a maximum of 1024 custom language models per owning credentials.
        The service returns an error if you attempt to create more than 1024 models. You
        do not lose any models, but you cannot create any more until your model count is
        below the limit.
        **Important:** Effective **31 July 2023**, all previous-generation models will be
        removed from the service and the documentation. Most previous-generation models
        were deprecated on 15 March 2022. You must migrate to the equivalent large speech
        model or next-generation model by 31 July 2023. For more information, see
        [Migrating to large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-migrate).
        **See also:**
        * [Create a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageCreate#createModel-language)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support)
        ### Large speech models and Next-generation models
         The service supports large speech models and next-generation `Multimedia` (16
        kHz) and `Telephony` (8 kHz) models for many languages. Large speech models and
        next-generation models have higher throughput than the service's previous
        generation of `Broadband` and `Narrowband` models. When you use large speech
        models and next-generation models, the service can return transcriptions more
        quickly and also provide noticeably better transcription accuracy.
        You specify a large speech model or next-generation model by using the `model`
        query parameter, as you do a previous-generation model. Only the next-generation
        models support the `low_latency` parameter, and all large speech models and
        next-generation models support the `character_insertion_bias` parameter. These
        parameters are not available with previous-generation models.
        Large speech models and next-generation models do not support all of the speech
        recognition parameters that are available for use with previous-generation models.
        Next-generation models do not support the following parameters:
        * `acoustic_customization_id`
        * `keywords` and `keywords_threshold`
        * `processing_metrics` and `processing_metrics_interval`
        * `word_alternatives_threshold`
        **Important:** Effective **31 July 2023**, all previous-generation models will be
        removed from the service and the documentation. Most previous-generation models
        were deprecated on 15 March 2022. You must migrate to the equivalent large speech
        model or next-generation model by 31 July 2023. For more information, see
        [Migrating to large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-migrate).
        **See also:**
        * [Large speech languages and
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-large-speech-languages)
        * [Supported features for large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-large-speech-languages#models-lsm-supported-features)
        * [Next-generation languages and
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng)
        * [Supported features for next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng#models-ng-features).

        :param str name: A user-defined name for the new custom language model. Use
               a localized name that matches the language of the custom model. Use a name
               that describes the domain of the custom model, such as `Medical custom
               model` or `Legal custom model`. Use a name that is unique among all custom
               language models that you own.
               Include a maximum of 256 characters in the name. Do not use backslashes,
               slashes, colons, equal signs, ampersands, or question marks in the name.
        :param str base_model_name: The name of the base language model that is to
               be customized by the new custom language model. The new custom model can be
               used only with the base model that it customizes.
               To determine whether a base model supports language model customization,
               use the [Get a model](#getmodel) method and check that the attribute
               `custom_language_model` is set to `true`. You can also refer to [Language
               support for
               customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).
        :param str dialect: (optional) The dialect of the specified language that
               is to be used with the custom language model. _For all languages, it is
               always safe to omit this field._ The service automatically uses the
               language identifier from the name of the base model. For example, the
               service automatically uses `en-US` for all US English models.
               If you specify the `dialect` for a new custom model, follow these
               guidelines. _For non-Spanish previous-generation models and for
               next-generation models,_ you must specify a value that matches the
               five-character language identifier from the name of the base model. _For
               Spanish previous-generation models,_ you must specify one of the following
               values:
               * `es-ES` for Castilian Spanish (`es-ES` models)
               * `es-LA` for Latin American Spanish (`es-AR`, `es-CL`, `es-CO`, and
               `es-PE` models)
               * `es-US` for Mexican (North American) Spanish (`es-MX` models)
               All values that you pass for the `dialect` field are case-insensitive.
        :param str description: (optional) A recommended description of the new
               custom language model. Use a localized description that matches the
               language of the custom model. Include a maximum of 128 characters in the
               description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LanguageModel` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if base_model_name is None:
            raise ValueError('base_model_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_language_model',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'base_model_name': base_model_name,
            'dialect': dialect,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/customizations'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_language_models(
        self,
        *,
        language: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List custom language models.

        Lists information about all custom language models that are owned by an instance
        of the service. Use the `language` parameter to see all custom language models for
        the specified language. Omit the parameter to see all custom language models for
        all languages. You must use credentials for the instance of the service that owns
        a model to list information about it.
        **See also:**
        * [Listing custom language
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageLanguageModels#listModels-language)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str language: (optional) The identifier of the language for which
               custom language or custom acoustic models are to be returned. Specify the
               five-character language identifier; for example, specify `en-US` to see all
               custom language or custom acoustic models that are based on US English
               models. Omit the parameter to see all custom language or custom acoustic
               models that are owned by the requesting credentials.
               To determine the languages for which customization is available, see
               [Language support for
               customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LanguageModels` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_language_models',
        )
        headers.update(sdk_headers)

        params = {
            'language': language,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/customizations'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_language_model(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a custom language model.

        Gets information about a specified custom language model. You must use credentials
        for the instance of the service that owns a model to list information about it.
        **See also:**
        * [Listing custom language
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageLanguageModels#listModels-language)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LanguageModel` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_language_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_language_model(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom language model.

        Deletes an existing custom language model. The custom model cannot be deleted if
        another request, such as adding a corpus or grammar to the model, is currently
        being processed. You must use credentials for the instance of the service that
        owns a model to delete it.
        **See also:**
        * [Deleting a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageLanguageModels#deleteModel-language)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_language_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def train_language_model(
        self,
        customization_id: str,
        *,
        word_type_to_add: Optional[str] = None,
        customization_weight: Optional[float] = None,
        strict: Optional[bool] = None,
        force: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
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
        You can monitor the status of the training by using the [Get a custom language
        model](#getlanguagemodel) method to poll the model's status. Use a loop to check
        the status every 10 seconds. If you added custom words directly to a custom model
        that is based on a next-generation model, allow for some minutes of extra training
        time for the model.
        The method returns a `LanguageModel` object that includes `status` and `progress`
        fields. A status of `available` means that the custom model is trained and ready
        to use. The service cannot accept subsequent training requests or requests to add
        new resources until the existing request completes.
        For custom models that are based on improved base language models, training also
        performs an automatic upgrade to a newer version of the base model. You do not
        need to use the [Upgrade a custom language model](#upgradelanguagemodel) method to
        perform the upgrade.
        **See also:**
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support)
        * [Train the custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageCreate#trainModel-language)
        * [Upgrading custom language models that are based on improved next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade#custom-upgrade-language-ng)
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

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str word_type_to_add: (optional) _For custom models that are based
               on previous-generation models_, the type of words from the custom language
               model's words resource on which to train the model:
               * `all` (the default) trains the model on all new words, regardless of
               whether they were extracted from corpora or grammars or were added or
               modified by the user.
               * `user` trains the model only on custom words that were added or modified
               by the user directly. The model is not trained on new words extracted from
               corpora or grammars.
               _For custom models that are based on large speech models and
               next-generation models_, the service ignores the `word_type_to_add`
               parameter. The words resource contains only custom words that the user adds
               or modifies directly, so the parameter is unnecessary.
        :param float customization_weight: (optional) Specifies a customization
               weight for the custom language model. The customization weight tells the
               service how much weight to give to words from the custom language model
               compared to those from the base model for speech recognition. Specify a
               value between 0.0 and 1.0. The default value is:
               * 0.5 for large speech models
               * 0.3 for previous-generation models
               * 0.2 for most next-generation models
               * 0.1 for next-generation English and Japanese models
               The default value yields the best performance in general. Assign a higher
               value if your audio makes frequent use of OOV words from the custom model.
               Use caution when setting the weight: a higher value can improve the
               accuracy of phrases from the custom model's domain, but it can negatively
               affect performance on non-domain phrases.
               The value that you assign is used for all recognition requests that use the
               model. You can override it for any recognition request by specifying a
               customization weight for that request.
               See [Using customization
               weight](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageUse#weight).
        :param bool strict: (optional) If `false`, allows training of the custom
               language model to proceed as long as the model contains at least one valid
               resource. The method returns an array of `TrainingWarning` objects that
               lists any invalid resources. By default (`true`), training of a custom
               language model fails (status code 400) if the model contains one or more
               invalid resources (corpus files, grammar files, or custom words).
        :param bool force: (optional) If `true`, forces the training of the custom
               language model regardless of whether it contains any changes (is in the
               `ready` or `available` state). By default (`false`), the model must be in
               the `ready` state to be trained. You can use the parameter to train and
               thus upgrade a custom model that is based on an improved next-generation
               model. *The parameter is available only for IBM Cloud, not for IBM Cloud
               Pak for Data.*
               See [Upgrading a custom language model based on an improved next-generation
               model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade#custom-upgrade-language-ng).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrainingResponse` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='train_language_model',
        )
        headers.update(sdk_headers)

        params = {
            'word_type_to_add': word_type_to_add,
            'customization_weight': customization_weight,
            'strict': strict,
            'force': force,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/train'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def reset_language_model(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Reset a custom language model.

        Resets a custom language model by removing all corpora, grammars, and words from
        the model. Resetting a custom language model initializes the model to its state
        when it was first created. Metadata such as the name and language of the model are
        preserved, but the model's words resource is removed and must be re-created. You
        must use credentials for the instance of the service that owns a model to reset
        it.
        **See also:**
        * [Resetting a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageLanguageModels#resetModel-language)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='reset_language_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/reset'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def upgrade_language_model(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
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
        [Get a custom language model](#getlanguagemodel) method to poll the model's
        status. The method returns a `LanguageModel` object that includes `status` and
        `progress` fields. Use a loop to check the status every 10 seconds.
        While it is being upgraded, the custom model has the status `upgrading`. When the
        upgrade is complete, the model resumes the status that it had prior to upgrade.
        The service cannot accept subsequent requests for the model until the upgrade
        completes.
        For custom models that are based on improved base language models, the [Train a
        custom language model](#trainlanguagemodel) method also performs an automatic
        upgrade to a newer version of the base model. You do not need to use the upgrade
        method.
        **See also:**
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support)
        * [Upgrading a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade#custom-upgrade-language)
        * [Upgrading custom language models that are based on improved next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade#custom-upgrade-language-ng).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='upgrade_language_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/upgrade_model'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom corpora
    #########################

    def list_corpora(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List corpora.

        Lists information about all corpora from a custom language model. The information
        includes the name, status, and total number of words for each corpus. _For custom
        models that are based on previous-generation models_, it also includes the number
        of out-of-vocabulary (OOV) words from the corpus. You must use credentials for the
        instance of the service that owns a model to list its corpora.
        **See also:** [Listing corpora for a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageCorpora#listCorpora).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Corpora` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_corpora',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/corpora'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def add_corpus(
        self,
        customization_id: str,
        corpus_name: str,
        corpus_file: BinaryIO,
        *,
        allow_overwrite: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add a corpus.

        Adds a single corpus text file of new training data to a custom language model.
        Use multiple requests to submit multiple corpus text files. You must use
        credentials for the instance of the service that owns a model to add a corpus to
        it. Adding a corpus does not affect the custom language model until you train the
        model for the new data by using the [Train a custom language
        model](#trainlanguagemodel) method.
        Submit a plain text file that contains sample sentences from the domain of
        interest to enable the service to parse the words in context. The more sentences
        you add that represent the context in which speakers use words from the domain,
        the better the service's recognition accuracy.
        The call returns an HTTP 201 response code if the corpus is valid. The service
        then asynchronously processes and automatically extracts data from the contents of
        the corpus. This operation can take on the order of minutes to complete depending
        on the current load on the service, the total number of words in the corpus, and,
        _for custom models that are based on previous-generation models_, the number of
        new (out-of-vocabulary) words in the corpus. You cannot submit requests to add
        additional resources to the custom model or to train the model until the service's
        analysis of the corpus for the current request completes. Use the [Get a
        corpus](#getcorpus) method to check the status of the analysis.
        _For custom models that are based on large speech models_, the service parses and
        extracts word sequences from one or multiple corpora files. The characters help
        the service learn and predict character sequences from audio.
        _For custom models that are based on previous-generation models_, the service
        auto-populates the model's words resource with words from the corpus that are not
        found in its base vocabulary. These words are referred to as out-of-vocabulary
        (OOV) words. After adding a corpus, you must validate the words resource to ensure
        that each OOV word's definition is complete and valid. You can use the [List
        custom words](#listwords) method to examine the words resource. You can use other
        words method to eliminate typos and modify how words are pronounced and displayed
        as needed.
        To add a corpus file that has the same name as an existing corpus, set the
        `allow_overwrite` parameter to `true`; otherwise, the request fails. Overwriting
        an existing corpus causes the service to process the corpus text file and extract
        its data anew. _For a custom model that is based on a previous-generation model_,
        the service first removes any OOV words that are associated with the existing
        corpus from the model's words resource unless they were also added by another
        corpus or grammar, or they have been modified in some way with the [Add custom
        words](#addwords) or [Add a custom word](#addword) method.
        The service limits the overall amount of data that you can add to a custom model
        to a maximum of 10 million total words from all sources combined. _For a custom
        model that is based on a previous-generation model_, you can add no more than 90
        thousand custom (OOV) words to a model. This includes words that the service
        extracts from corpora and grammars, and words that you add directly.
        **See also:**
        * [Add a corpus to the custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageCreate#addCorpus)
        * [Working with corpora for previous-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#workingCorpora)
        * [Working with corpora for large speech models and next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords-ng#workingCorpora-ng)
        * [Validating a words resource for previous-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#validateModel)
        * [Validating a words resource for large speech models and next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords-ng#validateModel-ng).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str corpus_name: The name of the new corpus for the custom language
               model. Use a localized name that matches the language of the custom model
               and reflects the contents of the corpus.
               * Include a maximum of 128 characters in the name.
               * Do not use characters that need to be URL-encoded. For example, do not
               use spaces, slashes, backslashes, colons, ampersands, double quotes, plus
               signs, equals signs, questions marks, and so on in the name. (The service
               does not prevent the use of these characters. But because they must be
               URL-encoded wherever used, their use is strongly discouraged.)
               * Do not use the name of an existing corpus or grammar that is already
               defined for the custom model.
               * Do not use the name `user`, which is reserved by the service to denote
               custom words that are added or modified by the user.
               * Do not use the name `base_lm` or `default_lm`. Both names are reserved
               for future use by the service.
        :param BinaryIO corpus_file: A plain text file that contains the training
               data for the corpus. Encode the file in UTF-8 if it contains non-ASCII
               characters; the service assumes UTF-8 encoding if it encounters non-ASCII
               characters.
               Make sure that you know the character encoding of the file. You must use
               that same encoding when working with the words in the custom language
               model. For more information, see [Character encoding for custom
               words](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageWords#charEncoding).
               With the `curl` command, use the `--data-binary` option to upload the file
               for the request.
        :param bool allow_overwrite: (optional) If `true`, the specified corpus
               overwrites an existing corpus with the same name. If `false`, the request
               fails if a corpus with the same name already exists. The parameter has no
               effect if a corpus with the same name does not already exist.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not corpus_name:
            raise ValueError('corpus_name must be provided')
        if corpus_file is None:
            raise ValueError('corpus_file must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='add_corpus',
        )
        headers.update(sdk_headers)

        params = {
            'allow_overwrite': allow_overwrite,
        }

        form_data = []
        form_data.append(('corpus_file', (None, corpus_file, 'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'corpus_name']
        path_param_values = self.encode_path_vars(customization_id, corpus_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/corpora/{corpus_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_corpus(
        self,
        customization_id: str,
        corpus_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a corpus.

        Gets information about a corpus from a custom language model. The information
        includes the name, status, and total number of words for the corpus. _For custom
        models that are based on previous-generation models_, it also includes the number
        of out-of-vocabulary (OOV) words from the corpus. You must use credentials for the
        instance of the service that owns a model to list its corpora.
        **See also:** [Listing corpora for a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageCorpora#listCorpora).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str corpus_name: The name of the corpus for the custom language
               model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Corpus` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not corpus_name:
            raise ValueError('corpus_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_corpus',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'corpus_name']
        path_param_values = self.encode_path_vars(customization_id, corpus_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/corpora/{corpus_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_corpus(
        self,
        customization_id: str,
        corpus_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a corpus.

        Deletes an existing corpus from a custom language model. Removing a corpus does
        not affect the custom model until you train the model with the [Train a custom
        language model](#trainlanguagemodel) method. You must use credentials for the
        instance of the service that owns a model to delete its corpora.
        _For custom models that are based on previous-generation models_, the service
        removes any out-of-vocabulary (OOV) words that are associated with the corpus from
        the custom model's words resource unless they were also added by another corpus or
        grammar, or they were modified in some way with the [Add custom words](#addwords)
        or [Add a custom word](#addword) method.
        **See also:** [Deleting a corpus from a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageCorpora#deleteCorpus).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str corpus_name: The name of the corpus for the custom language
               model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not corpus_name:
            raise ValueError('corpus_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_corpus',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'corpus_name']
        path_param_values = self.encode_path_vars(customization_id, corpus_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/corpora/{corpus_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom words
    #########################

    def list_words(
        self,
        customization_id: str,
        *,
        word_type: Optional[str] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List custom words.

        Lists information about custom words from a custom language model. You can list
        all words from the custom model's words resource, only custom words that were
        added or modified by the user, or, _for a custom model that is based on a
        previous-generation model_, only out-of-vocabulary (OOV) words that were extracted
        from corpora or are recognized by grammars. _For a custom model that is based on a
        next-generation model_, you can list all words or only those words that were added
        directly by a user, which return the same results.
        You can also indicate the order in which the service is to return words; by
        default, the service lists words in ascending alphabetical order. You must use
        credentials for the instance of the service that owns a model to list information
        about its words.
        **See also:** [Listing words from a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageWords#listWords).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str word_type: (optional) The type of words to be listed from the
               custom language model's words resource:
               * `all` (the default) shows all words.
               * `user` shows only custom words that were added or modified by the user
               directly.
               * `corpora` shows only OOV that were extracted from corpora.
               * `grammars` shows only OOV words that are recognized by grammars.
               _For a custom model that is based on a next-generation model_, only `all`
               and `user` apply. Both options return the same results. Words from other
               sources are not added to custom models that are based on next-generation
               models.
        :param str sort: (optional) Indicates the order in which the words are to
               be listed, `alphabetical` or by `count`. You can prepend an optional `+` or
               `-` to an argument to indicate whether the results are to be sorted in
               ascending or descending order. By default, words are sorted in ascending
               alphabetical order. For alphabetical ordering, the lexicographical
               precedence is numeric values, uppercase letters, and lowercase letters. For
               count ordering, values with the same count are ordered alphabetically. With
               the `curl` command, URL-encode the `+` symbol as `%2B`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Words` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_words',
        )
        headers.update(sdk_headers)

        params = {
            'word_type': word_type,
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def add_words(
        self,
        customization_id: str,
        words: List['CustomWord'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Add custom words.

        Adds one or more custom words to a custom language model. You can use this method
        to add words or to modify existing words in a custom model's words resource. _For
        custom models that are based on previous-generation models_, the service populates
        the words resource for a custom model with out-of-vocabulary (OOV) words from each
        corpus or grammar that is added to the model. You can use this method to modify
        OOV words in the model's words resource.
        _For a custom model that is based on a previous-generation model_, the words
        resource for a model can contain a maximum of 90 thousand custom (OOV) words. This
        includes words that the service extracts from corpora and grammars and words that
        you add directly.
        You must use credentials for the instance of the service that owns a model to add
        or modify custom words for the model. Adding or modifying custom words does not
        affect the custom model until you train the model for the new data by using the
        [Train a custom language model](#trainlanguagemodel) method.
        You add custom words by providing a `CustomWords` object, which is an array of
        `CustomWord` objects, one per word. Use the object's `word` parameter to identify
        the word that is to be added. You can also provide one or both of the optional
        `display_as` or `sounds_like` fields for each word.
        * The `display_as` field provides a different way of spelling the word in a
        transcript. Use the parameter when you want the word to appear different from its
        usual representation or from its spelling in training data. For example, you might
        indicate that the word `IBM` is to be displayed as `IBM&trade;`.
        * The `sounds_like` field provides an array of one or more pronunciations for the
        word. Use the parameter to specify how the word can be pronounced by users. Use
        the parameter for words that are difficult to pronounce, foreign words, acronyms,
        and so on. For example, you might specify that the word `IEEE` can sound like `I
        triple E`. You can specify a maximum of five sounds-like pronunciations for a
        word. _For a custom model that is based on a previous-generation model_, if you
        omit the `sounds_like` field, the service attempts to set the field to its
        pronunciation of the word. It cannot generate a pronunciation for all words, so
        you must review the word's definition to ensure that it is complete and valid.
        * The `mapping_only` field provides parameter for custom words. You can use the
        'mapping_only' key in custom words as a form of post processing. This key
        parameter has a boolean value to determine whether 'sounds_like' (for non-Japanese
        models) or word (for Japanese) is not used for the model fine-tuning, but for the
        replacement for 'display_as'. This feature helps you when you use custom words
        exclusively to map 'sounds_like' (or word) to 'display_as' value. When you use
        custom words solely for post-processing purposes that does not need fine-tuning.
        If you add a custom word that already exists in the words resource for the custom
        model, the new definition overwrites the existing data for the word. If the
        service encounters an error with the input data, it returns a failure code and
        does not add any of the words to the words resource.
        The call returns an HTTP 201 response code if the input data is valid. It then
        asynchronously processes the words to add them to the model's words resource. The
        time that it takes for the analysis to complete depends on the number of new words
        that you add but is generally faster than adding a corpus or grammar.
        You can monitor the status of the request by using the [Get a custom language
        model](#getlanguagemodel) method to poll the model's status. Use a loop to check
        the status every 10 seconds. The method returns a `Customization` object that
        includes a `status` field. A status of `ready` means that the words have been
        added to the custom model. The service cannot accept requests to add new data or
        to train the model until the existing request completes.
        You can use the [List custom words](#listwords) or [Get a custom word](#getword)
        method to review the words that you add. Words with an invalid `sounds_like` field
        include an `error` field that describes the problem. You can use other
        words-related methods to correct errors, eliminate typos, and modify how words are
        pronounced as needed.
        **See also:**
        * [Add words to the custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageCreate#addWords)
        * [Working with custom words for previous-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#workingWords)
        * [Working with custom words for large speech models and next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords-ng#workingWords-ng)
        * [Validating a words resource for previous-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#validateModel)
        * [Validating a words resource for large speech models and next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords-ng#validateModel-ng).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param List[CustomWord] words: An array of `CustomWord` objects that
               provides information about each custom word that is to be added to or
               updated in the custom language model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if words is None:
            raise ValueError('words must be provided')
        words = [convert_model(x) for x in words]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='add_words',
        )
        headers.update(sdk_headers)

        data = {
            'words': words,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def add_word(
        self,
        customization_id: str,
        word_name: str,
        *,
        word: Optional[str] = None,
        mapping_only: Optional[List[str]] = None,
        sounds_like: Optional[List[str]] = None,
        display_as: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add a custom word.

        Adds a custom word to a custom language model. You can use this method to add a
        word or to modify an existing word in the words resource. _For custom models that
        are based on previous-generation models_, the service populates the words resource
        for a custom model with out-of-vocabulary (OOV) words from each corpus or grammar
        that is added to the model. You can use this method to modify OOV words in the
        model's words resource.
        _For a custom model that is based on a previous-generation models_, the words
        resource for a model can contain a maximum of 90 thousand custom (OOV) words. This
        includes words that the service extracts from corpora and grammars and words that
        you add directly.
        You must use credentials for the instance of the service that owns a model to add
        or modify a custom word for the model. Adding or modifying a custom word does not
        affect the custom model until you train the model for the new data by using the
        [Train a custom language model](#trainlanguagemodel) method.
        Use the `word_name` parameter to specify the custom word that is to be added or
        modified. Use the `CustomWord` object to provide one or both of the optional
        `display_as` or `sounds_like` fields for the word.
        * The `display_as` field provides a different way of spelling the word in a
        transcript. Use the parameter when you want the word to appear different from its
        usual representation or from its spelling in training data. For example, you might
        indicate that the word `IBM` is to be displayed as `IBM&trade;`.
        * The `sounds_like` field provides an array of one or more pronunciations for the
        word. Use the parameter to specify how the word can be pronounced by users. Use
        the parameter for words that are difficult to pronounce, foreign words, acronyms,
        and so on. For example, you might specify that the word `IEEE` can sound like `i
        triple e`. You can specify a maximum of five sounds-like pronunciations for a
        word. _For custom models that are based on previous-generation models_, if you
        omit the `sounds_like` field, the service attempts to set the field to its
        pronunciation of the word. It cannot generate a pronunciation for all words, so
        you must review the word's definition to ensure that it is complete and valid.
        If you add a custom word that already exists in the words resource for the custom
        model, the new definition overwrites the existing data for the word. If the
        service encounters an error, it does not add the word to the words resource. Use
        the [Get a custom word](#getword) method to review the word that you add.
        **See also:**
        * [Add words to the custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-languageCreate#addWords)
        * [Working with custom words for previous-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#workingWords)
        * [Working with custom words for large speech models and next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords-ng#workingWords-ng)
        * [Validating a words resource for previous-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#validateModel)
        * [Validating a words resource for large speech models and next-generation
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords-ng#validateModel-ng).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str word_name: The custom word that is to be added to or updated in
               the custom language model. Do not use characters that need to be
               URL-encoded, for example, spaces, slashes, backslashes, colons, ampersands,
               double quotes, plus signs, equals signs, or question marks. Use a `-`
               (dash) or `_` (underscore) to connect the tokens of compound words.
               URL-encode the word if it includes non-ASCII characters. For more
               information, see [Character
               encoding](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#charEncoding).
        :param str word: (optional) For the [Add custom words](#addwords) method,
               you must specify the custom word that is to be added to or updated in the
               custom model. Do not use characters that need to be URL-encoded, for
               example, spaces, slashes, backslashes, colons, ampersands, double quotes,
               plus signs, equals signs, or question marks. Use a `-` (dash) or `_`
               (underscore) to connect the tokens of compound words. A Japanese custom
               word can include at most 25 characters, not including leading or trailing
               spaces.
               Omit this parameter for the [Add a custom word](#addword) method.
        :param List[str] mapping_only: (optional) Parameter for custom words. You
               can use the 'mapping_only' key in custom words as a form of post
               processing. This key parameter has a boolean value to determine whether
               'sounds_like' (for non-Japanese models) or word (for Japanese) is not used
               for the model fine-tuning, but for the replacement for 'display_as'. This
               feature helps you when you use custom words exclusively to map
               'sounds_like' (or word) to 'display_as' value. When you use custom words
               solely for post-processing purposes that does not need fine-tuning.
        :param List[str] sounds_like: (optional) As array of sounds-like
               pronunciations for the custom word. Specify how words that are difficult to
               pronounce, foreign words, acronyms, and so on can be pronounced by users.
               * _For custom models that are based on previous-generation models_, for a
               word that is not in the service's base vocabulary, omit the parameter to
               have the service automatically generate a sounds-like pronunciation for the
               word.
               * For a word that is in the service's base vocabulary, use the parameter to
               specify additional pronunciations for the word. You cannot override the
               default pronunciation of a word; pronunciations you add augment the
               pronunciation from the base vocabulary.
               A word can have at most five sounds-like pronunciations. A pronunciation
               can include at most 40 characters, not including leading or trailing
               spaces. A Japanese pronunciation can include at most 25 characters, not
               including leading or trailing spaces.
        :param str display_as: (optional) An alternative spelling for the custom
               word when it appears in a transcript. Use the parameter when you want the
               word to have a spelling that is different from its usual representation or
               from its spelling in corpora training data.
               _For custom models that are based on next-generation models_, the service
               uses the spelling of the word as the display-as value if you omit the
               field.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not word_name:
            raise ValueError('word_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='add_word',
        )
        headers.update(sdk_headers)

        data = {
            'word': word,
            'mapping_only': mapping_only,
            'sounds_like': sounds_like,
            'display_as': display_as,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'word_name']
        path_param_values = self.encode_path_vars(customization_id, word_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words/{word_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_word(
        self,
        customization_id: str,
        word_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a custom word.

        Gets information about a custom word from a custom language model. You must use
        credentials for the instance of the service that owns a model to list information
        about its words.
        **See also:** [Listing words from a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageWords#listWords).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str word_name: The custom word that is to be read from the custom
               language model. URL-encode the word if it includes non-ASCII characters.
               For more information, see [Character
               encoding](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#charEncoding).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Word` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not word_name:
            raise ValueError('word_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_word',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'word_name']
        path_param_values = self.encode_path_vars(customization_id, word_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words/{word_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_word(
        self,
        customization_id: str,
        word_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom word.

        Deletes a custom word from a custom language model. You can remove any word that
        you added to the custom model's words resource via any means. However, if the word
        also exists in the service's base vocabulary, the service removes the word only
        from the words resource; the word remains in the base vocabulary. Removing a
        custom word does not affect the custom model until you train the model with the
        [Train a custom language model](#trainlanguagemodel) method. You must use
        credentials for the instance of the service that owns a model to delete its words.
        **See also:** [Deleting a word from a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageWords#deleteWord).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str word_name: The custom word that is to be deleted from the custom
               language model. URL-encode the word if it includes non-ASCII characters.
               For more information, see [Character
               encoding](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-corporaWords#charEncoding).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not word_name:
            raise ValueError('word_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_word',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'word_name']
        path_param_values = self.encode_path_vars(customization_id, word_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words/{word_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom grammars
    #########################

    def list_grammars(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List grammars.

        Lists information about all grammars from a custom language model. For each
        grammar, the information includes the name, status, and (for grammars that are
        based on previous-generation models) the total number of out-of-vocabulary (OOV)
        words. You must use credentials for the instance of the service that owns a model
        to list its grammars.
        **See also:**
        * [Listing grammars from a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageGrammars#listGrammars)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Grammars` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_grammars',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/grammars'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def add_grammar(
        self,
        customization_id: str,
        grammar_name: str,
        grammar_file: BinaryIO,
        content_type: str,
        *,
        allow_overwrite: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add a grammar.

        Adds a single grammar file to a custom language model. Submit a plain text file in
        UTF-8 format that defines the grammar. Use multiple requests to submit multiple
        grammar files. You must use credentials for the instance of the service that owns
        a model to add a grammar to it. Adding a grammar does not affect the custom
        language model until you train the model for the new data by using the [Train a
        custom language model](#trainlanguagemodel) method.
        The call returns an HTTP 201 response code if the grammar is valid. The service
        then asynchronously processes the contents of the grammar and automatically
        extracts new words that it finds. This operation can take a few seconds or minutes
        to complete depending on the size and complexity of the grammar, as well as the
        current load on the service. You cannot submit requests to add additional
        resources to the custom model or to train the model until the service's analysis
        of the grammar for the current request completes. Use the [Get a
        grammar](#getgrammar) method to check the status of the analysis.
        _For grammars that are based on previous-generation models,_ the service populates
        the model's words resource with any word that is recognized by the grammar that is
        not found in the model's base vocabulary. These are referred to as
        out-of-vocabulary (OOV) words. You can use the [List custom words](#listwords)
        method to examine the words resource and use other words-related methods to
        eliminate typos and modify how words are pronounced as needed. _For grammars that
        are based on next-generation models,_ the service extracts no OOV words from the
        grammars.
        To add a grammar that has the same name as an existing grammar, set the
        `allow_overwrite` parameter to `true`; otherwise, the request fails. Overwriting
        an existing grammar causes the service to process the grammar file and extract OOV
        words anew. Before doing so, it removes any OOV words associated with the existing
        grammar from the model's words resource unless they were also added by another
        resource or they have been modified in some way with the [Add custom
        words](#addwords) or [Add a custom word](#addword) method.
        _For grammars that are based on previous-generation models,_ the service limits
        the overall amount of data that you can add to a custom model to a maximum of 10
        million total words from all sources combined. Also, you can add no more than 90
        thousand OOV words to a model. This includes words that the service extracts from
        corpora and grammars and words that you add directly.
        **See also:**
        * [Understanding
        grammars](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-grammarUnderstand#grammarUnderstand)
        * [Add a grammar to the custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-grammarAdd#addGrammar)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str grammar_name: The name of the new grammar for the custom
               language model. Use a localized name that matches the language of the
               custom model and reflects the contents of the grammar.
               * Include a maximum of 128 characters in the name.
               * Do not use characters that need to be URL-encoded. For example, do not
               use spaces, slashes, backslashes, colons, ampersands, double quotes, plus
               signs, equals signs, questions marks, and so on in the name. (The service
               does not prevent the use of these characters. But because they must be
               URL-encoded wherever used, their use is strongly discouraged.)
               * Do not use the name of an existing grammar or corpus that is already
               defined for the custom model.
               * Do not use the name `user`, which is reserved by the service to denote
               custom words that are added or modified by the user.
               * Do not use the name `base_lm` or `default_lm`. Both names are reserved
               for future use by the service.
        :param BinaryIO grammar_file: A plain text file that contains the grammar
               in the format specified by the `Content-Type` header. Encode the file in
               UTF-8 (ASCII is a subset of UTF-8). Using any other encoding can lead to
               issues when compiling the grammar or to unexpected results in decoding. The
               service ignores an encoding that is specified in the header of the grammar.
               With the `curl` command, use the `--data-binary` option to upload the file
               for the request.
        :param str content_type: The format (MIME type) of the grammar file:
               * `application/srgs` for Augmented Backus-Naur Form (ABNF), which uses a
               plain-text representation that is similar to traditional BNF grammars.
               * `application/srgs+xml` for XML Form, which uses XML elements to represent
               the grammar.
        :param bool allow_overwrite: (optional) If `true`, the specified grammar
               overwrites an existing grammar with the same name. If `false`, the request
               fails if a grammar with the same name already exists. The parameter has no
               effect if a grammar with the same name does not already exist.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not grammar_name:
            raise ValueError('grammar_name must be provided')
        if grammar_file is None:
            raise ValueError('grammar_file must be provided')
        if not content_type:
            raise ValueError('content_type must be provided')
        headers = {
            'Content-Type': content_type,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='add_grammar',
        )
        headers.update(sdk_headers)

        params = {
            'allow_overwrite': allow_overwrite,
        }

        data = grammar_file

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'grammar_name']
        path_param_values = self.encode_path_vars(customization_id,
                                                  grammar_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/grammars/{grammar_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_grammar(
        self,
        customization_id: str,
        grammar_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a grammar.

        Gets information about a grammar from a custom language model. For each grammar,
        the information includes the name, status, and (for grammars that are based on
        previous-generation models) the total number of out-of-vocabulary (OOV) words. You
        must use credentials for the instance of the service that owns a model to list its
        grammars.
        **See also:**
        * [Listing grammars from a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageGrammars#listGrammars)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str grammar_name: The name of the grammar for the custom language
               model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Grammar` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not grammar_name:
            raise ValueError('grammar_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_grammar',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'grammar_name']
        path_param_values = self.encode_path_vars(customization_id,
                                                  grammar_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/grammars/{grammar_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_grammar(
        self,
        customization_id: str,
        grammar_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a grammar.

        Deletes an existing grammar from a custom language model. _For grammars that are
        based on previous-generation models,_ the service removes any out-of-vocabulary
        (OOV) words associated with the grammar from the custom model's words resource
        unless they were also added by another resource or they were modified in some way
        with the [Add custom words](#addwords) or [Add a custom word](#addword) method.
        Removing a grammar does not affect the custom model until you train the model with
        the [Train a custom language model](#trainlanguagemodel) method. You must use
        credentials for the instance of the service that owns a model to delete its
        grammar.
        **See also:**
        * [Deleting a grammar from a custom language
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageGrammars#deleteGrammar)
        * [Language support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).

        :param str customization_id: The customization ID (GUID) of the custom
               language model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str grammar_name: The name of the grammar for the custom language
               model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not grammar_name:
            raise ValueError('grammar_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_grammar',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'grammar_name']
        path_param_values = self.encode_path_vars(customization_id,
                                                  grammar_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/grammars/{grammar_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom acoustic models
    #########################

    def create_acoustic_model(
        self,
        name: str,
        base_model_name: str,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom acoustic model.

        Creates a new custom acoustic model for a specified base model. The custom
        acoustic model can be used only with the base model for which it is created. The
        model is owned by the instance of the service whose credentials are used to create
        it.
        You can create a maximum of 1024 custom acoustic models per owning credentials.
        The service returns an error if you attempt to create more than 1024 models. You
        do not lose any models, but you cannot create any more until your model count is
        below the limit.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **Important:** Effective **31 July 2023**, all previous-generation models will be
        removed from the service and the documentation. Most previous-generation models
        were deprecated on 15 March 2022. You must migrate to the equivalent large speech
        model or next-generation model by 31 July 2023. For more information, see
        [Migrating to large speech
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-migrate).
        **See also:** [Create a custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-acoustic#createModel-acoustic).

        :param str name: A user-defined name for the new custom acoustic model. Use
               a localized name that matches the language of the custom model. Use a name
               that describes the acoustic environment of the custom model, such as
               `Mobile custom model` or `Noisy car custom model`. Use a name that is
               unique among all custom acoustic models that you own.
               Include a maximum of 256 characters in the name. Do not use backslashes,
               slashes, colons, equal signs, ampersands, or question marks in the name.
        :param str base_model_name: The name of the base language model that is to
               be customized by the new custom acoustic model. The new custom model can be
               used only with the base model that it customizes.
               To determine whether a base model supports acoustic model customization,
               refer to [Language support for
               customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).
        :param str description: (optional) A recommended description of the new
               custom acoustic model. Use a localized description that matches the
               language of the custom model. Include a maximum of 128 characters in the
               description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AcousticModel` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if base_model_name is None:
            raise ValueError('base_model_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_acoustic_model',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'base_model_name': base_model_name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/acoustic_customizations'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_acoustic_models(
        self,
        *,
        language: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List custom acoustic models.

        Lists information about all custom acoustic models that are owned by an instance
        of the service. Use the `language` parameter to see all custom acoustic models for
        the specified language. Omit the parameter to see all custom acoustic models for
        all languages. You must use credentials for the instance of the service that owns
        a model to list information about it.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Listing custom acoustic
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageAcousticModels#listModels-acoustic).

        :param str language: (optional) The identifier of the language for which
               custom language or custom acoustic models are to be returned. Specify the
               five-character language identifier; for example, specify `en-US` to see all
               custom language or custom acoustic models that are based on US English
               models. Omit the parameter to see all custom language or custom acoustic
               models that are owned by the requesting credentials.
               To determine the languages for which customization is available, see
               [Language support for
               customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AcousticModels` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_acoustic_models',
        )
        headers.update(sdk_headers)

        params = {
            'language': language,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/acoustic_customizations'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_acoustic_model(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a custom acoustic model.

        Gets information about a specified custom acoustic model. You must use credentials
        for the instance of the service that owns a model to list information about it.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Listing custom acoustic
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageAcousticModels#listModels-acoustic).

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AcousticModel` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_acoustic_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_acoustic_model(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom acoustic model.

        Deletes an existing custom acoustic model. The custom model cannot be deleted if
        another request, such as adding an audio resource to the model, is currently being
        processed. You must use credentials for the instance of the service that owns a
        model to delete it.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Deleting a custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageAcousticModels#deleteModel-acoustic).

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_acoustic_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def train_acoustic_model(
        self,
        customization_id: str,
        *,
        custom_language_model_id: Optional[str] = None,
        strict: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Train a custom acoustic model.

        Initiates the training of a custom acoustic model with new or changed audio
        resources. After adding or deleting audio resources for a custom acoustic model,
        use this method to begin the actual training of the model on the latest audio
        data. The custom acoustic model does not reflect its changed data until you train
        it. You must use credentials for the instance of the service that owns a model to
        train it.
        The training method is asynchronous. Training time depends on the cumulative
        amount of audio data that the custom acoustic model contains and the current load
        on the service. When you train or retrain a model, the service uses all of the
        model's audio data in the training. Training a custom acoustic model takes
        approximately as long as the length of its cumulative audio data. For example, it
        takes approximately 2 hours to train a model that contains a total of 2 hours of
        audio. The method returns an HTTP 200 response code to indicate that the training
        process has begun.
        You can monitor the status of the training by using the [Get a custom acoustic
        model](#getacousticmodel) method to poll the model's status. Use a loop to check
        the status once a minute. The method returns an `AcousticModel` object that
        includes `status` and `progress` fields. A status of `available` indicates that
        the custom model is trained and ready to use. The service cannot train a model
        while it is handling another request for the model. The service cannot accept
        subsequent training requests, or requests to add new audio resources, until the
        existing training request completes.
        You can use the optional `custom_language_model_id` parameter to specify the GUID
        of a separately created custom language model that is to be used during training.
        Train with a custom language model if you have verbatim transcriptions of the
        audio files that you have added to the custom model or you have either corpora
        (text files) or a list of words that are relevant to the contents of the audio
        files. For training to succeed, both of the custom models must be based on the
        same version of the same base model, and the custom language model must be fully
        trained and available.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:**
        * [Train the custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-acoustic#trainModel-acoustic)
        * [Using custom acoustic and custom language models
        together](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-useBoth#useBoth)
        ### Training failures
         Training can fail to start for the following reasons:
        * The service is currently handling another request for the custom model, such as
        another training request or a request to add audio resources to the model.
        * The custom model contains less than 10 minutes of audio that includes speech,
        not silence.
        * The custom model contains more than 50 hours of audio (for IBM Cloud) or more
        that 200 hours of audio (for IBM Cloud Pak for Data). **Note:** For IBM Cloud, the
        maximum hours of audio for a custom acoustic model was reduced from 200 to 50
        hours in August and September 2022. For more information, see [Maximum hours of
        audio](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-audioResources#audioMaximum).
        * You passed a custom language model with the `custom_language_model_id` query
        parameter that is not in the available state. A custom language model must be
        fully trained and available to be used to train a custom acoustic model.
        * You passed an incompatible custom language model with the
        `custom_language_model_id` query parameter. Both custom models must be based on
        the same version of the same base model.
        * The custom model contains one or more invalid audio resources. You can correct
        the invalid audio resources or set the `strict` parameter to `false` to exclude
        the invalid resources from the training. The model must contain at least one valid
        resource for training to succeed.

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str custom_language_model_id: (optional) The customization ID (GUID)
               of a custom language model that is to be used during training of the custom
               acoustic model. Specify a custom language model that has been trained with
               verbatim transcriptions of the audio resources or that contains words that
               are relevant to the contents of the audio resources. The custom language
               model must be based on the same version of the same base model as the
               custom acoustic model, and the custom language model must be fully trained
               and available. The credentials specified with the request must own both
               custom models.
        :param bool strict: (optional) If `false`, allows training of the custom
               acoustic model to proceed as long as the model contains at least one valid
               audio resource. The method returns an array of `TrainingWarning` objects
               that lists any invalid resources. By default (`true`), training of a custom
               acoustic model fails (status code 400) if the model contains one or more
               invalid audio resources.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrainingResponse` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='train_acoustic_model',
        )
        headers.update(sdk_headers)

        params = {
            'custom_language_model_id': custom_language_model_id,
            'strict': strict,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}/train'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def reset_acoustic_model(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
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
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Resetting a custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageAcousticModels#resetModel-acoustic).

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='reset_acoustic_model',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}/reset'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def upgrade_acoustic_model(
        self,
        customization_id: str,
        *,
        custom_language_model_id: Optional[str] = None,
        force: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
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
        [Get a custom acoustic model](#getacousticmodel) method to poll the model's
        status. The method returns an `AcousticModel` object that includes `status` and
        `progress` fields. Use a loop to check the status once a minute.
        While it is being upgraded, the custom model has the status `upgrading`. When the
        upgrade is complete, the model resumes the status that it had prior to upgrade.
        The service cannot upgrade a model while it is handling another request for the
        model. The service cannot accept subsequent requests for the model until the
        existing upgrade request completes.
        If the custom acoustic model was trained with a separately created custom language
        model, you must use the `custom_language_model_id` parameter to specify the GUID
        of that custom language model. The custom language model must be upgraded before
        the custom acoustic model can be upgraded. Omit the parameter if the custom
        acoustic model was not trained with a custom language model.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Upgrading a custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade#custom-upgrade-acoustic).

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str custom_language_model_id: (optional) If the custom acoustic
               model was trained with a custom language model, the customization ID (GUID)
               of that custom language model. The custom language model must be upgraded
               before the custom acoustic model can be upgraded. The custom language model
               must be fully trained and available. The credentials specified with the
               request must own both custom models.
        :param bool force: (optional) If `true`, forces the upgrade of a custom
               acoustic model for which no input data has been modified since it was last
               trained. Use this parameter only to force the upgrade of a custom acoustic
               model that is trained with a custom language model, and only if you receive
               a 400 response code and the message `No input data modified since last
               training`. See [Upgrading a custom acoustic
               model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-upgrade#custom-upgrade-acoustic).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='upgrade_acoustic_model',
        )
        headers.update(sdk_headers)

        params = {
            'custom_language_model_id': custom_language_model_id,
            'force': force,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}/upgrade_model'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom audio resources
    #########################

    def list_audio(
        self,
        customization_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List audio resources.

        Lists information about all audio resources from a custom acoustic model. The
        information includes the name of the resource and information about its audio
        data, such as its duration. It also includes the status of the audio resource,
        which is important for checking the service's analysis of the resource in response
        to a request to add it to the custom acoustic model. You must use credentials for
        the instance of the service that owns a model to list its audio resources.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Listing audio resources for a custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageAudio#listAudio).

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AudioResources` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_audio',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}/audio'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def add_audio(
        self,
        customization_id: str,
        audio_name: str,
        audio_resource: BinaryIO,
        *,
        content_type: Optional[str] = None,
        contained_content_type: Optional[str] = None,
        allow_overwrite: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add an audio resource.

        Adds an audio resource to a custom acoustic model. Add audio content that reflects
        the acoustic characteristics of the audio that you plan to transcribe. You must
        use credentials for the instance of the service that owns a model to add an audio
        resource to it. Adding audio data does not affect the custom acoustic model until
        you train the model for the new data by using the [Train a custom acoustic
        model](#trainacousticmodel) method.
        You can add individual audio files or an archive file that contains multiple audio
        files. Adding multiple audio files via a single archive file is significantly more
        efficient than adding each file individually. You can add audio resources in any
        format that the service supports for speech recognition.
        You can use this method to add any number of audio resources to a custom model by
        calling the method once for each audio or archive file. You can add multiple
        different audio resources at the same time. You must add a minimum of 10 minutes
        of audio that includes speech, not just silence, to a custom acoustic model before
        you can train it. No audio resource, audio- or archive-type, can be larger than
        100 MB. To add an audio resource that has the same name as an existing audio
        resource, set the `allow_overwrite` parameter to `true`; otherwise, the request
        fails. A custom model can contain no more than 50 hours of audio (for IBM Cloud)
        or 200 hours of audio (for IBM Cloud Pak for Data). **Note:** For IBM Cloud, the
        maximum hours of audio for a custom acoustic model was reduced from 200 to 50
        hours in August and September 2022. For more information, see [Maximum hours of
        audio](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-audioResources#audioMaximum).
        The method is asynchronous. It can take several seconds or minutes to complete
        depending on the duration of the audio and, in the case of an archive file, the
        total number of audio files being processed. The service returns a 201 response
        code if the audio is valid. It then asynchronously analyzes the contents of the
        audio file or files and automatically extracts information about the audio such as
        its length, sampling rate, and encoding. You cannot submit requests to train or
        upgrade the model until the service's analysis of all audio resources for current
        requests completes.
        To determine the status of the service's analysis of the audio, use the [Get an
        audio resource](#getaudio) method to poll the status of the audio. The method
        accepts the customization ID of the custom model and the name of the audio
        resource, and it returns the status of the resource. Use a loop to check the
        status of the audio every few seconds until it becomes `ok`.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Add audio to the custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-acoustic#addAudio).
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
         **See also:** [Supported audio
        formats](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-audio-formats).
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

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str audio_name: The name of the new audio resource for the custom
               acoustic model. Use a localized name that matches the language of the
               custom model and reflects the contents of the resource.
               * Include a maximum of 128 characters in the name.
               * Do not use characters that need to be URL-encoded. For example, do not
               use spaces, slashes, backslashes, colons, ampersands, double quotes, plus
               signs, equals signs, questions marks, and so on in the name. (The service
               does not prevent the use of these characters. But because they must be
               URL-encoded wherever used, their use is strongly discouraged.)
               * Do not use the name of an audio resource that has already been added to
               the custom model.
        :param BinaryIO audio_resource: The audio resource that is to be added to
               the custom acoustic model, an individual audio file or an archive file.
               With the `curl` command, use the `--data-binary` option to upload the file
               for the request.
        :param str content_type: (optional) For an audio-type resource, the format
               (MIME type) of the audio. For more information, see **Content types for
               audio-type resources** in the method description.
               For an archive-type resource, the media type of the archive file. For more
               information, see **Content types for archive-type resources** in the method
               description.
        :param str contained_content_type: (optional) _For an archive-type
               resource_, specify the format of the audio files that are contained in the
               archive file if they are of type `audio/alaw`, `audio/basic`, `audio/l16`,
               or `audio/mulaw`. Include the `rate`, `channels`, and `endianness`
               parameters where necessary. In this case, all audio files that are
               contained in the archive file must be of the indicated type.
               For all other audio formats, you can omit the header. In this case, the
               audio files can be of multiple types as long as they are not of the types
               listed in the previous paragraph.
               The parameter accepts all of the audio formats that are supported for use
               with speech recognition. For more information, see **Content types for
               audio-type resources** in the method description.
               _For an audio-type resource_, omit the header.
        :param bool allow_overwrite: (optional) If `true`, the specified audio
               resource overwrites an existing audio resource with the same name. If
               `false`, the request fails if an audio resource with the same name already
               exists. The parameter has no effect if an audio resource with the same name
               does not already exist.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not audio_name:
            raise ValueError('audio_name must be provided')
        if audio_resource is None:
            raise ValueError('audio_resource must be provided')
        headers = {
            'Content-Type': content_type,
            'Contained-Content-Type': contained_content_type,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='add_audio',
        )
        headers.update(sdk_headers)

        params = {
            'allow_overwrite': allow_overwrite,
        }

        data = audio_resource

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'audio_name']
        path_param_values = self.encode_path_vars(customization_id, audio_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}/audio/{audio_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_audio(
        self,
        customization_id: str,
        audio_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an audio resource.

        Gets information about an audio resource from a custom acoustic model. The method
        returns an `AudioListing` object whose fields depend on the type of audio resource
        that you specify with the method's `audio_name` parameter:
        * _For an audio-type resource_, the object's fields match those of an
        `AudioResource` object: `duration`, `name`, `details`, and `status`.
        * _For an archive-type resource_, the object includes a `container` field whose
        fields match those of an `AudioResource` object. It also includes an `audio`
        field, which contains an array of `AudioResource` objects that provides
        information about the audio files that are contained in the archive.
        The information includes the status of the specified audio resource. The status is
        important for checking the service's analysis of a resource that you add to the
        custom model.
        * _For an audio-type resource_, the `status` field is located in the
        `AudioListing` object.
        * _For an archive-type resource_, the `status` field is located in the
        `AudioResource` object that is returned in the `container` field.
        You must use credentials for the instance of the service that owns a model to list
        its audio resources.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Listing audio resources for a custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageAudio#listAudio).

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str audio_name: The name of the audio resource for the custom
               acoustic model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AudioListing` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not audio_name:
            raise ValueError('audio_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_audio',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'audio_name']
        path_param_values = self.encode_path_vars(customization_id, audio_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}/audio/{audio_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_audio(
        self,
        customization_id: str,
        audio_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an audio resource.

        Deletes an existing audio resource from a custom acoustic model. Deleting an
        archive-type audio resource removes the entire archive of files. The service does
        not allow deletion of individual files from an archive resource.
        Removing an audio resource does not affect the custom model until you train the
        model on its updated data by using the [Train a custom acoustic
        model](#trainacousticmodel) method. You can delete an existing audio resource from
        a model while a different resource is being added to the model. You must use
        credentials for the instance of the service that owns a model to delete its audio
        resources.
        **Note:** Acoustic model customization is supported only for use with
        previous-generation models. It is not supported for large speech models and
        next-generation models.
        **See also:** [Deleting an audio resource from a custom acoustic
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-manageAudio#deleteAudio).

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model that is to be used for the request. You must make the
               request with credentials for the instance of the service that owns the
               custom model.
        :param str audio_name: The name of the audio resource for the custom
               acoustic model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not audio_name:
            raise ValueError('audio_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_audio',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'audio_name']
        path_param_values = self.encode_path_vars(customization_id, audio_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/acoustic_customizations/{customization_id}/audio/{audio_name}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(
        self,
        customer_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete labeled data.

        Deletes all data that is associated with a specified customer ID. The method
        deletes all data for the customer ID, regardless of the method by which the
        information was added. The method has no effect if no data is associated with the
        customer ID. You must issue the request with credentials for the same instance of
        the service that was used to associate the customer ID with the data. You
        associate a customer ID with data by passing the `X-Watson-Metadata` header with a
        request that passes the data.
        **Note:** If you delete an instance of the service from the service console, all
        data associated with that service instance is automatically deleted. This includes
        all custom language models, corpora, grammars, and words; all custom acoustic
        models and audio resources; all registered endpoints for the asynchronous HTTP
        interface; and all data related to speech recognition requests.
        **See also:** [Information
        security](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-information-security#information-security).

        :param str customer_id: The customer ID for which all data is to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customer_id:
            raise ValueError('customer_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_user_data',
        )
        headers.update(sdk_headers)

        params = {
            'customer_id': customer_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/v1/user_data'
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response


class GetModelEnums:
    """
    Enums for get_model parameters.
    """

    class ModelId(str, Enum):
        """
        The identifier of the model in the form of its name from the output of the [List
        models](#listmodels) method.
        """

        AR_MS_BROADBANDMODEL = 'ar-MS_BroadbandModel'
        AR_MS_TELEPHONY = 'ar-MS_Telephony'
        CS_CZ_TELEPHONY = 'cs-CZ_Telephony'
        DE_DE_BROADBANDMODEL = 'de-DE_BroadbandModel'
        DE_DE_MULTIMEDIA = 'de-DE_Multimedia'
        DE_DE_NARROWBANDMODEL = 'de-DE_NarrowbandModel'
        DE_DE_TELEPHONY = 'de-DE_Telephony'
        EN_AU = 'en-AU'
        EN_AU_BROADBANDMODEL = 'en-AU_BroadbandModel'
        EN_AU_MULTIMEDIA = 'en-AU_Multimedia'
        EN_AU_NARROWBANDMODEL = 'en-AU_NarrowbandModel'
        EN_AU_TELEPHONY = 'en-AU_Telephony'
        EN_GB = 'en-GB'
        EN_GB_BROADBANDMODEL = 'en-GB_BroadbandModel'
        EN_GB_MULTIMEDIA = 'en-GB_Multimedia'
        EN_GB_NARROWBANDMODEL = 'en-GB_NarrowbandModel'
        EN_GB_TELEPHONY = 'en-GB_Telephony'
        EN_IN = 'en-IN'
        EN_IN_TELEPHONY = 'en-IN_Telephony'
        EN_US = 'en-US'
        EN_US_BROADBANDMODEL = 'en-US_BroadbandModel'
        EN_US_MULTIMEDIA = 'en-US_Multimedia'
        EN_US_NARROWBANDMODEL = 'en-US_NarrowbandModel'
        EN_US_SHORTFORM_NARROWBANDMODEL = 'en-US_ShortForm_NarrowbandModel'
        EN_US_TELEPHONY = 'en-US_Telephony'
        EN_WW_MEDICAL_TELEPHONY = 'en-WW_Medical_Telephony'
        ES_AR = 'es-AR'
        ES_AR_BROADBANDMODEL = 'es-AR_BroadbandModel'
        ES_AR_NARROWBANDMODEL = 'es-AR_NarrowbandModel'
        ES_CL = 'es-CL'
        ES_CL_BROADBANDMODEL = 'es-CL_BroadbandModel'
        ES_CL_NARROWBANDMODEL = 'es-CL_NarrowbandModel'
        ES_CO = 'es-CO'
        ES_CO_BROADBANDMODEL = 'es-CO_BroadbandModel'
        ES_CO_NARROWBANDMODEL = 'es-CO_NarrowbandModel'
        ES_ES = 'es-ES'
        ES_ES_BROADBANDMODEL = 'es-ES_BroadbandModel'
        ES_ES_NARROWBANDMODEL = 'es-ES_NarrowbandModel'
        ES_ES_MULTIMEDIA = 'es-ES_Multimedia'
        ES_ES_TELEPHONY = 'es-ES_Telephony'
        ES_LA_TELEPHONY = 'es-LA_Telephony'
        ES_MX = 'es-MX'
        ES_MX_BROADBANDMODEL = 'es-MX_BroadbandModel'
        ES_MX_NARROWBANDMODEL = 'es-MX_NarrowbandModel'
        ES_PE = 'es-PE'
        ES_PE_BROADBANDMODEL = 'es-PE_BroadbandModel'
        ES_PE_NARROWBANDMODEL = 'es-PE_NarrowbandModel'
        FR_CA = 'fr-CA'
        FR_CA_BROADBANDMODEL = 'fr-CA_BroadbandModel'
        FR_CA_MULTIMEDIA = 'fr-CA_Multimedia'
        FR_CA_NARROWBANDMODEL = 'fr-CA_NarrowbandModel'
        FR_CA_TELEPHONY = 'fr-CA_Telephony'
        FR_FR = 'fr-FR'
        FR_FR_BROADBANDMODEL = 'fr-FR_BroadbandModel'
        FR_FR_MULTIMEDIA = 'fr-FR_Multimedia'
        FR_FR_NARROWBANDMODEL = 'fr-FR_NarrowbandModel'
        FR_FR_TELEPHONY = 'fr-FR_Telephony'
        HI_IN_TELEPHONY = 'hi-IN_Telephony'
        IT_IT_BROADBANDMODEL = 'it-IT_BroadbandModel'
        IT_IT_NARROWBANDMODEL = 'it-IT_NarrowbandModel'
        IT_IT_MULTIMEDIA = 'it-IT_Multimedia'
        IT_IT_TELEPHONY = 'it-IT_Telephony'
        JA_JP = 'ja-JP'
        JA_JP_BROADBANDMODEL = 'ja-JP_BroadbandModel'
        JA_JP_MULTIMEDIA = 'ja-JP_Multimedia'
        JA_JP_NARROWBANDMODEL = 'ja-JP_NarrowbandModel'
        JA_JP_TELEPHONY = 'ja-JP_Telephony'
        KO_KR_BROADBANDMODEL = 'ko-KR_BroadbandModel'
        KO_KR_MULTIMEDIA = 'ko-KR_Multimedia'
        KO_KR_NARROWBANDMODEL = 'ko-KR_NarrowbandModel'
        KO_KR_TELEPHONY = 'ko-KR_Telephony'
        NL_BE_TELEPHONY = 'nl-BE_Telephony'
        NL_NL_BROADBANDMODEL = 'nl-NL_BroadbandModel'
        NL_NL_MULTIMEDIA = 'nl-NL_Multimedia'
        NL_NL_NARROWBANDMODEL = 'nl-NL_NarrowbandModel'
        NL_NL_TELEPHONY = 'nl-NL_Telephony'
        PT_BR = 'pt-BR'
        PT_BR_BROADBANDMODEL = 'pt-BR_BroadbandModel'
        PT_BR_MULTIMEDIA = 'pt-BR_Multimedia'
        PT_BR_NARROWBANDMODEL = 'pt-BR_NarrowbandModel'
        PT_BR_TELEPHONY = 'pt-BR_Telephony'
        SV_SE_TELEPHONY = 'sv-SE_Telephony'
        ZH_CN_BROADBANDMODEL = 'zh-CN_BroadbandModel'
        ZH_CN_NARROWBANDMODEL = 'zh-CN_NarrowbandModel'
        ZH_CN_TELEPHONY = 'zh-CN_Telephony'


class RecognizeEnums:
    """
    Enums for recognize parameters.
    """

    class ContentType(str, Enum):
        """
        The format (MIME type) of the audio. For more information about specifying an
        audio format, see **Audio formats (content types)** in the method description.
        """

        APPLICATION_OCTET_STREAM = 'application/octet-stream'
        AUDIO_ALAW = 'audio/alaw'
        AUDIO_BASIC = 'audio/basic'
        AUDIO_FLAC = 'audio/flac'
        AUDIO_G729 = 'audio/g729'
        AUDIO_L16 = 'audio/l16'
        AUDIO_MP3 = 'audio/mp3'
        AUDIO_MPEG = 'audio/mpeg'
        AUDIO_MULAW = 'audio/mulaw'
        AUDIO_OGG = 'audio/ogg'
        AUDIO_OGG_CODECS_OPUS = 'audio/ogg;codecs=opus'
        AUDIO_OGG_CODECS_VORBIS = 'audio/ogg;codecs=vorbis'
        AUDIO_WAV = 'audio/wav'
        AUDIO_WEBM = 'audio/webm'
        AUDIO_WEBM_CODECS_OPUS = 'audio/webm;codecs=opus'
        AUDIO_WEBM_CODECS_VORBIS = 'audio/webm;codecs=vorbis'

    class Model(str, Enum):
        """
        The model to use for speech recognition. If you omit the `model` parameter, the
        service uses the US English `en-US_BroadbandModel` by default.
        _For IBM Cloud Pak for Data,_ if you do not install the `en-US_BroadbandModel`,
        you must either specify a model with the request or specify a new default model
        for your installation of the service.
        **See also:**
        * [Using a model for speech
        recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use)
        * [Using the default
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use#models-use-default).
        """

        AR_MS_BROADBANDMODEL = 'ar-MS_BroadbandModel'
        AR_MS_TELEPHONY = 'ar-MS_Telephony'
        CS_CZ_TELEPHONY = 'cs-CZ_Telephony'
        DE_DE_BROADBANDMODEL = 'de-DE_BroadbandModel'
        DE_DE_MULTIMEDIA = 'de-DE_Multimedia'
        DE_DE_NARROWBANDMODEL = 'de-DE_NarrowbandModel'
        DE_DE_TELEPHONY = 'de-DE_Telephony'
        EN_AU = 'en-AU'
        EN_AU_BROADBANDMODEL = 'en-AU_BroadbandModel'
        EN_AU_MULTIMEDIA = 'en-AU_Multimedia'
        EN_AU_NARROWBANDMODEL = 'en-AU_NarrowbandModel'
        EN_AU_TELEPHONY = 'en-AU_Telephony'
        EN_IN = 'en-IN'
        EN_IN_TELEPHONY = 'en-IN_Telephony'
        EN_GB = 'en-GB'
        EN_GB_BROADBANDMODEL = 'en-GB_BroadbandModel'
        EN_GB_MULTIMEDIA = 'en-GB_Multimedia'
        EN_GB_NARROWBANDMODEL = 'en-GB_NarrowbandModel'
        EN_GB_TELEPHONY = 'en-GB_Telephony'
        EN_US = 'en-US'
        EN_US_BROADBANDMODEL = 'en-US_BroadbandModel'
        EN_US_MULTIMEDIA = 'en-US_Multimedia'
        EN_US_NARROWBANDMODEL = 'en-US_NarrowbandModel'
        EN_US_SHORTFORM_NARROWBANDMODEL = 'en-US_ShortForm_NarrowbandModel'
        EN_US_TELEPHONY = 'en-US_Telephony'
        EN_WW_MEDICAL_TELEPHONY = 'en-WW_Medical_Telephony'
        ES_AR = 'es-AR'
        ES_AR_BROADBANDMODEL = 'es-AR_BroadbandModel'
        ES_AR_NARROWBANDMODEL = 'es-AR_NarrowbandModel'
        ES_CL = 'es-CL'
        ES_CL_BROADBANDMODEL = 'es-CL_BroadbandModel'
        ES_CL_NARROWBANDMODEL = 'es-CL_NarrowbandModel'
        ES_CO = 'es-CO'
        ES_CO_BROADBANDMODEL = 'es-CO_BroadbandModel'
        ES_CO_NARROWBANDMODEL = 'es-CO_NarrowbandModel'
        ES_ES = 'es-ES'
        ES_ES_BROADBANDMODEL = 'es-ES_BroadbandModel'
        ES_ES_NARROWBANDMODEL = 'es-ES_NarrowbandModel'
        ES_ES_MULTIMEDIA = 'es-ES_Multimedia'
        ES_ES_TELEPHONY = 'es-ES_Telephony'
        ES_LA_TELEPHONY = 'es-LA_Telephony'
        ES_MX = 'es-MX'
        ES_MX_BROADBANDMODEL = 'es-MX_BroadbandModel'
        ES_MX_NARROWBANDMODEL = 'es-MX_NarrowbandModel'
        ES_PE = 'es-PE'
        ES_PE_BROADBANDMODEL = 'es-PE_BroadbandModel'
        ES_PE_NARROWBANDMODEL = 'es-PE_NarrowbandModel'
        FR_CA = 'fr-CA'
        FR_CA_BROADBANDMODEL = 'fr-CA_BroadbandModel'
        FR_CA_MULTIMEDIA = 'fr-CA_Multimedia'
        FR_CA_NARROWBANDMODEL = 'fr-CA_NarrowbandModel'
        FR_CA_TELEPHONY = 'fr-CA_Telephony'
        FR_FR = 'fr-FR'
        FR_FR_BROADBANDMODEL = 'fr-FR_BroadbandModel'
        FR_FR_MULTIMEDIA = 'fr-FR_Multimedia'
        FR_FR_NARROWBANDMODEL = 'fr-FR_NarrowbandModel'
        FR_FR_TELEPHONY = 'fr-FR_Telephony'
        HI_IN_TELEPHONY = 'hi-IN_Telephony'
        IT_IT_BROADBANDMODEL = 'it-IT_BroadbandModel'
        IT_IT_NARROWBANDMODEL = 'it-IT_NarrowbandModel'
        IT_IT_MULTIMEDIA = 'it-IT_Multimedia'
        IT_IT_TELEPHONY = 'it-IT_Telephony'
        JA_JP = 'ja-JP'
        JA_JP_BROADBANDMODEL = 'ja-JP_BroadbandModel'
        JA_JP_MULTIMEDIA = 'ja-JP_Multimedia'
        JA_JP_NARROWBANDMODEL = 'ja-JP_NarrowbandModel'
        JA_JP_TELEPHONY = 'ja-JP_Telephony'
        KO_KR_BROADBANDMODEL = 'ko-KR_BroadbandModel'
        KO_KR_MULTIMEDIA = 'ko-KR_Multimedia'
        KO_KR_NARROWBANDMODEL = 'ko-KR_NarrowbandModel'
        KO_KR_TELEPHONY = 'ko-KR_Telephony'
        NL_BE_TELEPHONY = 'nl-BE_Telephony'
        NL_NL_BROADBANDMODEL = 'nl-NL_BroadbandModel'
        NL_NL_MULTIMEDIA = 'nl-NL_Multimedia'
        NL_NL_NARROWBANDMODEL = 'nl-NL_NarrowbandModel'
        NL_NL_TELEPHONY = 'nl-NL_Telephony'
        PT_BR = 'pt-BR'
        PT_BR_BROADBANDMODEL = 'pt-BR_BroadbandModel'
        PT_BR_MULTIMEDIA = 'pt-BR_Multimedia'
        PT_BR_NARROWBANDMODEL = 'pt-BR_NarrowbandModel'
        PT_BR_TELEPHONY = 'pt-BR_Telephony'
        SV_SE_TELEPHONY = 'sv-SE_Telephony'
        ZH_CN_BROADBANDMODEL = 'zh-CN_BroadbandModel'
        ZH_CN_NARROWBANDMODEL = 'zh-CN_NarrowbandModel'
        ZH_CN_TELEPHONY = 'zh-CN_Telephony'


class CreateJobEnums:
    """
    Enums for create_job parameters.
    """

    class ContentType(str, Enum):
        """
        The format (MIME type) of the audio. For more information about specifying an
        audio format, see **Audio formats (content types)** in the method description.
        """

        APPLICATION_OCTET_STREAM = 'application/octet-stream'
        AUDIO_ALAW = 'audio/alaw'
        AUDIO_BASIC = 'audio/basic'
        AUDIO_FLAC = 'audio/flac'
        AUDIO_G729 = 'audio/g729'
        AUDIO_L16 = 'audio/l16'
        AUDIO_MP3 = 'audio/mp3'
        AUDIO_MPEG = 'audio/mpeg'
        AUDIO_MULAW = 'audio/mulaw'
        AUDIO_OGG = 'audio/ogg'
        AUDIO_OGG_CODECS_OPUS = 'audio/ogg;codecs=opus'
        AUDIO_OGG_CODECS_VORBIS = 'audio/ogg;codecs=vorbis'
        AUDIO_WAV = 'audio/wav'
        AUDIO_WEBM = 'audio/webm'
        AUDIO_WEBM_CODECS_OPUS = 'audio/webm;codecs=opus'
        AUDIO_WEBM_CODECS_VORBIS = 'audio/webm;codecs=vorbis'

    class Model(str, Enum):
        """
        The model to use for speech recognition. If you omit the `model` parameter, the
        service uses the US English `en-US_BroadbandModel` by default.
        _For IBM Cloud Pak for Data,_ if you do not install the `en-US_BroadbandModel`,
        you must either specify a model with the request or specify a new default model
        for your installation of the service.
        **See also:**
        * [Using a model for speech
        recognition](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use)
        * [Using the default
        model](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-use#models-use-default).
        """

        AR_MS_BROADBANDMODEL = 'ar-MS_BroadbandModel'
        AR_MS_TELEPHONY = 'ar-MS_Telephony'
        CS_CZ_TELEPHONY = 'cs-CZ_Telephony'
        DE_DE_BROADBANDMODEL = 'de-DE_BroadbandModel'
        DE_DE_MULTIMEDIA = 'de-DE_Multimedia'
        DE_DE_NARROWBANDMODEL = 'de-DE_NarrowbandModel'
        DE_DE_TELEPHONY = 'de-DE_Telephony'
        EN_AU = 'en-AU'
        EN_AU_BROADBANDMODEL = 'en-AU_BroadbandModel'
        EN_AU_MULTIMEDIA = 'en-AU_Multimedia'
        EN_AU_NARROWBANDMODEL = 'en-AU_NarrowbandModel'
        EN_AU_TELEPHONY = 'en-AU_Telephony'
        EN_IN = 'en-IN'
        EN_IN_TELEPHONY = 'en-IN_Telephony'
        EN_GB = 'en-GB'
        EN_GB_BROADBANDMODEL = 'en-GB_BroadbandModel'
        EN_GB_MULTIMEDIA = 'en-GB_Multimedia'
        EN_GB_NARROWBANDMODEL = 'en-GB_NarrowbandModel'
        EN_GB_TELEPHONY = 'en-GB_Telephony'
        EN_US = 'en-US'
        EN_US_BROADBANDMODEL = 'en-US_BroadbandModel'
        EN_US_MULTIMEDIA = 'en-US_Multimedia'
        EN_US_NARROWBANDMODEL = 'en-US_NarrowbandModel'
        EN_US_SHORTFORM_NARROWBANDMODEL = 'en-US_ShortForm_NarrowbandModel'
        EN_US_TELEPHONY = 'en-US_Telephony'
        EN_WW_MEDICAL_TELEPHONY = 'en-WW_Medical_Telephony'
        ES_AR = 'es-AR'
        ES_AR_BROADBANDMODEL = 'es-AR_BroadbandModel'
        ES_AR_NARROWBANDMODEL = 'es-AR_NarrowbandModel'
        ES_CL = 'es-CL'
        ES_CL_BROADBANDMODEL = 'es-CL_BroadbandModel'
        ES_CL_NARROWBANDMODEL = 'es-CL_NarrowbandModel'
        ES_CO = 'es-CO'
        ES_CO_BROADBANDMODEL = 'es-CO_BroadbandModel'
        ES_CO_NARROWBANDMODEL = 'es-CO_NarrowbandModel'
        ES_ES = 'es-ES'
        ES_ES_BROADBANDMODEL = 'es-ES_BroadbandModel'
        ES_ES_NARROWBANDMODEL = 'es-ES_NarrowbandModel'
        ES_ES_MULTIMEDIA = 'es-ES_Multimedia'
        ES_ES_TELEPHONY = 'es-ES_Telephony'
        ES_LA_TELEPHONY = 'es-LA_Telephony'
        ES_MX = 'es-MX'
        ES_MX_BROADBANDMODEL = 'es-MX_BroadbandModel'
        ES_MX_NARROWBANDMODEL = 'es-MX_NarrowbandModel'
        ES_PE = 'es-PE'
        ES_PE_BROADBANDMODEL = 'es-PE_BroadbandModel'
        ES_PE_NARROWBANDMODEL = 'es-PE_NarrowbandModel'
        FR_CA = 'fr-CA'
        FR_CA_BROADBANDMODEL = 'fr-CA_BroadbandModel'
        FR_CA_MULTIMEDIA = 'fr-CA_Multimedia'
        FR_CA_NARROWBANDMODEL = 'fr-CA_NarrowbandModel'
        FR_CA_TELEPHONY = 'fr-CA_Telephony'
        FR_FR = 'fr-FR'
        FR_FR_BROADBANDMODEL = 'fr-FR_BroadbandModel'
        FR_FR_MULTIMEDIA = 'fr-FR_Multimedia'
        FR_FR_NARROWBANDMODEL = 'fr-FR_NarrowbandModel'
        FR_FR_TELEPHONY = 'fr-FR_Telephony'
        HI_IN_TELEPHONY = 'hi-IN_Telephony'
        IT_IT_BROADBANDMODEL = 'it-IT_BroadbandModel'
        IT_IT_NARROWBANDMODEL = 'it-IT_NarrowbandModel'
        IT_IT_MULTIMEDIA = 'it-IT_Multimedia'
        IT_IT_TELEPHONY = 'it-IT_Telephony'
        JA_JP = 'ja-JP'
        JA_JP_BROADBANDMODEL = 'ja-JP_BroadbandModel'
        JA_JP_MULTIMEDIA = 'ja-JP_Multimedia'
        JA_JP_NARROWBANDMODEL = 'ja-JP_NarrowbandModel'
        JA_JP_TELEPHONY = 'ja-JP_Telephony'
        KO_KR_BROADBANDMODEL = 'ko-KR_BroadbandModel'
        KO_KR_MULTIMEDIA = 'ko-KR_Multimedia'
        KO_KR_NARROWBANDMODEL = 'ko-KR_NarrowbandModel'
        KO_KR_TELEPHONY = 'ko-KR_Telephony'
        NL_BE_TELEPHONY = 'nl-BE_Telephony'
        NL_NL_BROADBANDMODEL = 'nl-NL_BroadbandModel'
        NL_NL_MULTIMEDIA = 'nl-NL_Multimedia'
        NL_NL_NARROWBANDMODEL = 'nl-NL_NarrowbandModel'
        NL_NL_TELEPHONY = 'nl-NL_Telephony'
        PT_BR = 'pt-BR'
        PT_BR_BROADBANDMODEL = 'pt-BR_BroadbandModel'
        PT_BR_MULTIMEDIA = 'pt-BR_Multimedia'
        PT_BR_NARROWBANDMODEL = 'pt-BR_NarrowbandModel'
        PT_BR_TELEPHONY = 'pt-BR_Telephony'
        SV_SE_TELEPHONY = 'sv-SE_Telephony'
        ZH_CN_BROADBANDMODEL = 'zh-CN_BroadbandModel'
        ZH_CN_NARROWBANDMODEL = 'zh-CN_NarrowbandModel'
        ZH_CN_TELEPHONY = 'zh-CN_Telephony'

    class Events(str, Enum):
        """
        If the job includes a callback URL, a comma-separated list of notification events
        to which to subscribe. Valid events are
        * `recognitions.started` generates a callback notification when the service begins
        to process the job.
        * `recognitions.completed` generates a callback notification when the job is
        complete. You must use the [Check a job](#checkjob) method to retrieve the results
        before they time out or are deleted.
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
        """

        RECOGNITIONS_STARTED = 'recognitions.started'
        RECOGNITIONS_COMPLETED = 'recognitions.completed'
        RECOGNITIONS_COMPLETED_WITH_RESULTS = 'recognitions.completed_with_results'
        RECOGNITIONS_FAILED = 'recognitions.failed'


class ListLanguageModelsEnums:
    """
    Enums for list_language_models parameters.
    """

    class Language(str, Enum):
        """
        The identifier of the language for which custom language or custom acoustic models
        are to be returned. Specify the five-character language identifier; for example,
        specify `en-US` to see all custom language or custom acoustic models that are
        based on US English models. Omit the parameter to see all custom language or
        custom acoustic models that are owned by the requesting credentials.
        To determine the languages for which customization is available, see [Language
        support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).
        """

        AR_MS = 'ar-MS'
        CS_CZ = 'cs-CZ'
        DE_DE = 'de-DE'
        EN_AU = 'en-AU'
        EN_GB = 'en-GB'
        EN_IN = 'en-IN'
        EN_US = 'en-US'
        EN_WW = 'en-WW'
        ES_AR = 'es-AR'
        ES_CL = 'es-CL'
        ES_CO = 'es-CO'
        ES_ES = 'es-ES'
        ES_LA = 'es-LA'
        ES_MX = 'es-MX'
        ES_PE = 'es-PE'
        FR_CA = 'fr-CA'
        FR_FR = 'fr-FR'
        HI_IN = 'hi-IN'
        IT_IT = 'it-IT'
        JA_JP = 'ja-JP'
        KO_KR = 'ko-KR'
        NL_BE = 'nl-BE'
        NL_NL = 'nl-NL'
        PT_BR = 'pt-BR'
        SV_SE = 'sv-SE'
        ZH_CN = 'zh-CN'


class TrainLanguageModelEnums:
    """
    Enums for train_language_model parameters.
    """

    class WordTypeToAdd(str, Enum):
        """
        _For custom models that are based on previous-generation models_, the type of
        words from the custom language model's words resource on which to train the model:
        * `all` (the default) trains the model on all new words, regardless of whether
        they were extracted from corpora or grammars or were added or modified by the
        user.
        * `user` trains the model only on custom words that were added or modified by the
        user directly. The model is not trained on new words extracted from corpora or
        grammars.
        _For custom models that are based on large speech models and next-generation
        models_, the service ignores the `word_type_to_add` parameter. The words resource
        contains only custom words that the user adds or modifies directly, so the
        parameter is unnecessary.
        """

        ALL = 'all'
        USER = 'user'


class ListWordsEnums:
    """
    Enums for list_words parameters.
    """

    class WordType(str, Enum):
        """
        The type of words to be listed from the custom language model's words resource:
        * `all` (the default) shows all words.
        * `user` shows only custom words that were added or modified by the user directly.
        * `corpora` shows only OOV that were extracted from corpora.
        * `grammars` shows only OOV words that are recognized by grammars.
        _For a custom model that is based on a next-generation model_, only `all` and
        `user` apply. Both options return the same results. Words from other sources are
        not added to custom models that are based on next-generation models.
        """

        ALL = 'all'
        USER = 'user'
        CORPORA = 'corpora'
        GRAMMARS = 'grammars'

    class Sort(str, Enum):
        """
        Indicates the order in which the words are to be listed, `alphabetical` or by
        `count`. You can prepend an optional `+` or `-` to an argument to indicate whether
        the results are to be sorted in ascending or descending order. By default, words
        are sorted in ascending alphabetical order. For alphabetical ordering, the
        lexicographical precedence is numeric values, uppercase letters, and lowercase
        letters. For count ordering, values with the same count are ordered
        alphabetically. With the `curl` command, URL-encode the `+` symbol as `%2B`.
        """

        ALPHABETICAL = 'alphabetical'
        COUNT = 'count'


class AddGrammarEnums:
    """
    Enums for add_grammar parameters.
    """

    class ContentType(str, Enum):
        """
        The format (MIME type) of the grammar file:
        * `application/srgs` for Augmented Backus-Naur Form (ABNF), which uses a
        plain-text representation that is similar to traditional BNF grammars.
        * `application/srgs+xml` for XML Form, which uses XML elements to represent the
        grammar.
        """

        APPLICATION_SRGS = 'application/srgs'
        APPLICATION_SRGS_XML = 'application/srgs+xml'


class ListAcousticModelsEnums:
    """
    Enums for list_acoustic_models parameters.
    """

    class Language(str, Enum):
        """
        The identifier of the language for which custom language or custom acoustic models
        are to be returned. Specify the five-character language identifier; for example,
        specify `en-US` to see all custom language or custom acoustic models that are
        based on US English models. Omit the parameter to see all custom language or
        custom acoustic models that are owned by the requesting credentials.
        To determine the languages for which customization is available, see [Language
        support for
        customization](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-custom-support).
        """

        AR_MS = 'ar-MS'
        CS_CZ = 'cs-CZ'
        DE_DE = 'de-DE'
        EN_AU = 'en-AU'
        EN_GB = 'en-GB'
        EN_IN = 'en-IN'
        EN_US = 'en-US'
        EN_WW = 'en-WW'
        ES_AR = 'es-AR'
        ES_CL = 'es-CL'
        ES_CO = 'es-CO'
        ES_ES = 'es-ES'
        ES_LA = 'es-LA'
        ES_MX = 'es-MX'
        ES_PE = 'es-PE'
        FR_CA = 'fr-CA'
        FR_FR = 'fr-FR'
        HI_IN = 'hi-IN'
        IT_IT = 'it-IT'
        JA_JP = 'ja-JP'
        KO_KR = 'ko-KR'
        NL_BE = 'nl-BE'
        NL_NL = 'nl-NL'
        PT_BR = 'pt-BR'
        SV_SE = 'sv-SE'
        ZH_CN = 'zh-CN'


class AddAudioEnums:
    """
    Enums for add_audio parameters.
    """

    class ContentType(str, Enum):
        """
        For an audio-type resource, the format (MIME type) of the audio. For more
        information, see **Content types for audio-type resources** in the method
        description.
        For an archive-type resource, the media type of the archive file. For more
        information, see **Content types for archive-type resources** in the method
        description.
        """

        APPLICATION_ZIP = 'application/zip'
        APPLICATION_GZIP = 'application/gzip'
        AUDIO_ALAW = 'audio/alaw'
        AUDIO_BASIC = 'audio/basic'
        AUDIO_FLAC = 'audio/flac'
        AUDIO_G729 = 'audio/g729'
        AUDIO_L16 = 'audio/l16'
        AUDIO_MP3 = 'audio/mp3'
        AUDIO_MPEG = 'audio/mpeg'
        AUDIO_MULAW = 'audio/mulaw'
        AUDIO_OGG = 'audio/ogg'
        AUDIO_OGG_CODECS_OPUS = 'audio/ogg;codecs=opus'
        AUDIO_OGG_CODECS_VORBIS = 'audio/ogg;codecs=vorbis'
        AUDIO_WAV = 'audio/wav'
        AUDIO_WEBM = 'audio/webm'
        AUDIO_WEBM_CODECS_OPUS = 'audio/webm;codecs=opus'
        AUDIO_WEBM_CODECS_VORBIS = 'audio/webm;codecs=vorbis'

    class ContainedContentType(str, Enum):
        """
        _For an archive-type resource_, specify the format of the audio files that are
        contained in the archive file if they are of type `audio/alaw`, `audio/basic`,
        `audio/l16`, or `audio/mulaw`. Include the `rate`, `channels`, and `endianness`
        parameters where necessary. In this case, all audio files that are contained in
        the archive file must be of the indicated type.
        For all other audio formats, you can omit the header. In this case, the audio
        files can be of multiple types as long as they are not of the types listed in the
        previous paragraph.
        The parameter accepts all of the audio formats that are supported for use with
        speech recognition. For more information, see **Content types for audio-type
        resources** in the method description.
        _For an audio-type resource_, omit the header.
        """

        AUDIO_ALAW = 'audio/alaw'
        AUDIO_BASIC = 'audio/basic'
        AUDIO_FLAC = 'audio/flac'
        AUDIO_G729 = 'audio/g729'
        AUDIO_L16 = 'audio/l16'
        AUDIO_MP3 = 'audio/mp3'
        AUDIO_MPEG = 'audio/mpeg'
        AUDIO_MULAW = 'audio/mulaw'
        AUDIO_OGG = 'audio/ogg'
        AUDIO_OGG_CODECS_OPUS = 'audio/ogg;codecs=opus'
        AUDIO_OGG_CODECS_VORBIS = 'audio/ogg;codecs=vorbis'
        AUDIO_WAV = 'audio/wav'
        AUDIO_WEBM = 'audio/webm'
        AUDIO_WEBM_CODECS_OPUS = 'audio/webm;codecs=opus'
        AUDIO_WEBM_CODECS_VORBIS = 'audio/webm;codecs=vorbis'


##############################################################################
# Models
##############################################################################


class AcousticModel:
    """
    Information about an existing custom acoustic model.

    :param str customization_id: The customization ID (GUID) of the custom acoustic
          model. The [Create a custom acoustic model](#createacousticmodel) method returns
          only this field of the object; it does not return the other fields.
    :param str created: (optional) The date and time in Coordinated Universal Time
          (UTC) at which the custom acoustic model was created. The value is provided in
          full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :param str updated: (optional) The date and time in Coordinated Universal Time
          (UTC) at which the custom acoustic model was last modified. The `created` and
          `updated` fields are equal when an acoustic model is first added but has yet to
          be updated. The value is provided in full ISO 8601 format
          (YYYY-MM-DDThh:mm:ss.sTZD).
    :param str language: (optional) The language identifier of the custom acoustic
          model (for example, `en-US`).
    :param List[str] versions: (optional) A list of the available versions of the
          custom acoustic model. Each element of the array indicates a version of the base
          model with which the custom model can be used. Multiple versions exist only if
          the custom model has been upgraded to a new version of its base model.
          Otherwise, only a single version is shown.
    :param str owner: (optional) The GUID of the credentials for the instance of the
          service that owns the custom acoustic model.
    :param str name: (optional) The name of the custom acoustic model.
    :param str description: (optional) The description of the custom acoustic model.
    :param str base_model_name: (optional) The name of the language model for which
          the custom acoustic model was created.
    :param str status: (optional) The current status of the custom acoustic model:
          * `pending`: The model was created but is waiting either for valid training data
          to be added or for the service to finish analyzing added data.
          * `ready`: The model contains valid data and is ready to be trained. If the
          model contains a mix of valid and invalid resources, you need to set the
          `strict` parameter to `false` for the training to proceed.
          * `training`: The model is currently being trained.
          * `available`: The model is trained and ready to use.
          * `upgrading`: The model is currently being upgraded.
          * `failed`: Training of the model failed.
    :param int progress: (optional) A percentage that indicates the progress of the
          custom acoustic model's current training. A value of `100` means that the model
          is fully trained. **Note:** The `progress` field does not currently reflect the
          progress of the training. The field changes from `0` to `100` when training is
          complete.
    :param str warnings: (optional) If the request included unknown parameters, the
          following message: `Unexpected query parameter(s) ['parameters'] detected`,
          where `parameters` is a list that includes a quoted string for each unknown
          parameter.
    """

    def __init__(
        self,
        customization_id: str,
        *,
        created: Optional[str] = None,
        updated: Optional[str] = None,
        language: Optional[str] = None,
        versions: Optional[List[str]] = None,
        owner: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        base_model_name: Optional[str] = None,
        status: Optional[str] = None,
        progress: Optional[int] = None,
        warnings: Optional[str] = None,
    ) -> None:
        """
        Initialize a AcousticModel object.

        :param str customization_id: The customization ID (GUID) of the custom
               acoustic model. The [Create a custom acoustic model](#createacousticmodel)
               method returns only this field of the object; it does not return the other
               fields.
        :param str created: (optional) The date and time in Coordinated Universal
               Time (UTC) at which the custom acoustic model was created. The value is
               provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str updated: (optional) The date and time in Coordinated Universal
               Time (UTC) at which the custom acoustic model was last modified. The
               `created` and `updated` fields are equal when an acoustic model is first
               added but has yet to be updated. The value is provided in full ISO 8601
               format (YYYY-MM-DDThh:mm:ss.sTZD).
        :param str language: (optional) The language identifier of the custom
               acoustic model (for example, `en-US`).
        :param List[str] versions: (optional) A list of the available versions of
               the custom acoustic model. Each element of the array indicates a version of
               the base model with which the custom model can be used. Multiple versions
               exist only if the custom model has been upgraded to a new version of its
               base model. Otherwise, only a single version is shown.
        :param str owner: (optional) The GUID of the credentials for the instance
               of the service that owns the custom acoustic model.
        :param str name: (optional) The name of the custom acoustic model.
        :param str description: (optional) The description of the custom acoustic
               model.
        :param str base_model_name: (optional) The name of the language model for
               which the custom acoustic model was created.
        :param str status: (optional) The current status of the custom acoustic
               model:
               * `pending`: The model was created but is waiting either for valid training
               data to be added or for the service to finish analyzing added data.
               * `ready`: The model contains valid data and is ready to be trained. If the
               model contains a mix of valid and invalid resources, you need to set the
               `strict` parameter to `false` for the training to proceed.
               * `training`: The model is currently being trained.
               * `available`: The model is trained and ready to use.
               * `upgrading`: The model is currently being upgraded.
               * `failed`: Training of the model failed.
        :param int progress: (optional) A percentage that indicates the progress of
               the custom acoustic model's current training. A value of `100` means that
               the model is fully trained. **Note:** The `progress` field does not
               currently reflect the progress of the training. The field changes from `0`
               to `100` when training is complete.
        :param str warnings: (optional) If the request included unknown parameters,
               the following message: `Unexpected query parameter(s) ['parameters']
               detected`, where `parameters` is a list that includes a quoted string for
               each unknown parameter.
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
    def from_dict(cls, _dict: Dict) -> 'AcousticModel':
        """Initialize a AcousticModel object from a json dictionary."""
        args = {}
        if (customization_id := _dict.get('customization_id')) is not None:
            args['customization_id'] = customization_id
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in AcousticModel JSON'
            )
        if (created := _dict.get('created')) is not None:
            args['created'] = created
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = updated
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        if (versions := _dict.get('versions')) is not None:
            args['versions'] = versions
        if (owner := _dict.get('owner')) is not None:
            args['owner'] = owner
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (base_model_name := _dict.get('base_model_name')) is not None:
            args['base_model_name'] = base_model_name
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (progress := _dict.get('progress')) is not None:
            args['progress'] = progress
        if (warnings := _dict.get('warnings')) is not None:
            args['warnings'] = warnings
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AcousticModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AcousticModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AcousticModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AcousticModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the custom acoustic model:
        * `pending`: The model was created but is waiting either for valid training data
        to be added or for the service to finish analyzing added data.
        * `ready`: The model contains valid data and is ready to be trained. If the model
        contains a mix of valid and invalid resources, you need to set the `strict`
        parameter to `false` for the training to proceed.
        * `training`: The model is currently being trained.
        * `available`: The model is trained and ready to use.
        * `upgrading`: The model is currently being upgraded.
        * `failed`: Training of the model failed.
        """

        PENDING = 'pending'
        READY = 'ready'
        TRAINING = 'training'
        AVAILABLE = 'available'
        UPGRADING = 'upgrading'
        FAILED = 'failed'


class AcousticModels:
    """
    Information about existing custom acoustic models.

    :param List[AcousticModel] customizations: An array of `AcousticModel` objects
          that provides information about each available custom acoustic model. The array
          is empty if the requesting credentials own no custom acoustic models (if no
          language is specified) or own no custom acoustic models for the specified
          language.
    """

    def __init__(
        self,
        customizations: List['AcousticModel'],
    ) -> None:
        """
        Initialize a AcousticModels object.

        :param List[AcousticModel] customizations: An array of `AcousticModel`
               objects that provides information about each available custom acoustic
               model. The array is empty if the requesting credentials own no custom
               acoustic models (if no language is specified) or own no custom acoustic
               models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AcousticModels':
        """Initialize a AcousticModels object from a json dictionary."""
        args = {}
        if (customizations := _dict.get('customizations')) is not None:
            args['customizations'] = [
                AcousticModel.from_dict(v) for v in customizations
            ]
        else:
            raise ValueError(
                'Required property \'customizations\' not present in AcousticModels JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AcousticModels object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'customizations') and self.customizations is not None:
            customizations_list = []
            for v in self.customizations:
                if isinstance(v, dict):
                    customizations_list.append(v)
                else:
                    customizations_list.append(v.to_dict())
            _dict['customizations'] = customizations_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AcousticModels object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AcousticModels') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AcousticModels') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioDetails:
    """
    Information about an audio resource from a custom acoustic model.

    :param str type: (optional) The type of the audio resource:
          * `audio` for an individual audio file
          * `archive` for an archive (**.zip** or **.tar.gz**) file that contains audio
          files
          * `undetermined` for a resource that the service cannot validate (for example,
          if the user mistakenly passes a file that does not contain audio, such as a JPEG
          file).
    :param str codec: (optional) _For an audio-type resource_, the codec in which
          the audio is encoded. Omitted for an archive-type resource.
    :param int frequency: (optional) _For an audio-type resource_, the sampling rate
          of the audio in Hertz (samples per second). Omitted for an archive-type
          resource.
    :param str compression: (optional) _For an archive-type resource_, the format of
          the compressed archive:
          * `zip` for a **.zip** file
          * `gzip` for a **.tar.gz** file
          Omitted for an audio-type resource.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        codec: Optional[str] = None,
        frequency: Optional[int] = None,
        compression: Optional[str] = None,
    ) -> None:
        """
        Initialize a AudioDetails object.

        :param str type: (optional) The type of the audio resource:
               * `audio` for an individual audio file
               * `archive` for an archive (**.zip** or **.tar.gz**) file that contains
               audio files
               * `undetermined` for a resource that the service cannot validate (for
               example, if the user mistakenly passes a file that does not contain audio,
               such as a JPEG file).
        :param str codec: (optional) _For an audio-type resource_, the codec in
               which the audio is encoded. Omitted for an archive-type resource.
        :param int frequency: (optional) _For an audio-type resource_, the sampling
               rate of the audio in Hertz (samples per second). Omitted for an
               archive-type resource.
        :param str compression: (optional) _For an archive-type resource_, the
               format of the compressed archive:
               * `zip` for a **.zip** file
               * `gzip` for a **.tar.gz** file
               Omitted for an audio-type resource.
        """
        self.type = type
        self.codec = codec
        self.frequency = frequency
        self.compression = compression

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AudioDetails':
        """Initialize a AudioDetails object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (codec := _dict.get('codec')) is not None:
            args['codec'] = codec
        if (frequency := _dict.get('frequency')) is not None:
            args['frequency'] = frequency
        if (compression := _dict.get('compression')) is not None:
            args['compression'] = compression
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AudioDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AudioDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AudioDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of the audio resource:
        * `audio` for an individual audio file
        * `archive` for an archive (**.zip** or **.tar.gz**) file that contains audio
        files
        * `undetermined` for a resource that the service cannot validate (for example, if
        the user mistakenly passes a file that does not contain audio, such as a JPEG
        file).
        """

        AUDIO = 'audio'
        ARCHIVE = 'archive'
        UNDETERMINED = 'undetermined'

    class CompressionEnum(str, Enum):
        """
        _For an archive-type resource_, the format of the compressed archive:
        * `zip` for a **.zip** file
        * `gzip` for a **.tar.gz** file
        Omitted for an audio-type resource.
        """

        ZIP = 'zip'
        GZIP = 'gzip'


class AudioListing:
    """
    Information about an audio resource from a custom acoustic model.

    :param int duration: (optional) _For an audio-type resource_, the total seconds
          of audio in the resource. Omitted for an archive-type resource.
    :param str name: (optional) _For an audio-type resource_, the user-specified
          name of the resource. Omitted for an archive-type resource.
    :param AudioDetails details: (optional) _For an audio-type resource_, an
          `AudioDetails` object that provides detailed information about the resource. The
          object is empty until the service finishes processing the audio. Omitted for an
          archive-type resource.
    :param str status: (optional) _For an audio-type resource_, the status of the
          resource:
          * `ok`: The service successfully analyzed the audio data. The data can be used
          to train the custom model.
          * `being_processed`: The service is still analyzing the audio data. The service
          cannot accept requests to add new audio resources or to train the custom model
          until its analysis is complete.
          * `invalid`: The audio data is not valid for training the custom model (possibly
          because it has the wrong format or sampling rate, or because it is corrupted).
          Omitted for an archive-type resource.
    :param AudioResource container: (optional) _For an archive-type resource_, an
          object of type `AudioResource` that provides information about the resource.
          Omitted for an audio-type resource.
    :param List[AudioResource] audio: (optional) _For an archive-type resource_, an
          array of `AudioResource` objects that provides information about the audio-type
          resources that are contained in the resource. Omitted for an audio-type
          resource.
    """

    def __init__(
        self,
        *,
        duration: Optional[int] = None,
        name: Optional[str] = None,
        details: Optional['AudioDetails'] = None,
        status: Optional[str] = None,
        container: Optional['AudioResource'] = None,
        audio: Optional[List['AudioResource']] = None,
    ) -> None:
        """
        Initialize a AudioListing object.

        :param int duration: (optional) _For an audio-type resource_, the total
               seconds of audio in the resource. Omitted for an archive-type resource.
        :param str name: (optional) _For an audio-type resource_, the
               user-specified name of the resource. Omitted for an archive-type resource.
        :param AudioDetails details: (optional) _For an audio-type resource_, an
               `AudioDetails` object that provides detailed information about the
               resource. The object is empty until the service finishes processing the
               audio. Omitted for an archive-type resource.
        :param str status: (optional) _For an audio-type resource_, the status of
               the resource:
               * `ok`: The service successfully analyzed the audio data. The data can be
               used to train the custom model.
               * `being_processed`: The service is still analyzing the audio data. The
               service cannot accept requests to add new audio resources or to train the
               custom model until its analysis is complete.
               * `invalid`: The audio data is not valid for training the custom model
               (possibly because it has the wrong format or sampling rate, or because it
               is corrupted).
               Omitted for an archive-type resource.
        :param AudioResource container: (optional) _For an archive-type resource_,
               an object of type `AudioResource` that provides information about the
               resource. Omitted for an audio-type resource.
        :param List[AudioResource] audio: (optional) _For an archive-type
               resource_, an array of `AudioResource` objects that provides information
               about the audio-type resources that are contained in the resource. Omitted
               for an audio-type resource.
        """
        self.duration = duration
        self.name = name
        self.details = details
        self.status = status
        self.container = container
        self.audio = audio

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AudioListing':
        """Initialize a AudioListing object from a json dictionary."""
        args = {}
        if (duration := _dict.get('duration')) is not None:
            args['duration'] = duration
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (details := _dict.get('details')) is not None:
            args['details'] = AudioDetails.from_dict(details)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (container := _dict.get('container')) is not None:
            args['container'] = AudioResource.from_dict(container)
        if (audio := _dict.get('audio')) is not None:
            args['audio'] = [AudioResource.from_dict(v) for v in audio]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioListing object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'duration') and self.duration is not None:
            _dict['duration'] = self.duration
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'details') and self.details is not None:
            if isinstance(self.details, dict):
                _dict['details'] = self.details
            else:
                _dict['details'] = self.details.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'container') and self.container is not None:
            if isinstance(self.container, dict):
                _dict['container'] = self.container
            else:
                _dict['container'] = self.container.to_dict()
        if hasattr(self, 'audio') and self.audio is not None:
            audio_list = []
            for v in self.audio:
                if isinstance(v, dict):
                    audio_list.append(v)
                else:
                    audio_list.append(v.to_dict())
            _dict['audio'] = audio_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AudioListing object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AudioListing') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AudioListing') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        _For an audio-type resource_, the status of the resource:
        * `ok`: The service successfully analyzed the audio data. The data can be used to
        train the custom model.
        * `being_processed`: The service is still analyzing the audio data. The service
        cannot accept requests to add new audio resources or to train the custom model
        until its analysis is complete.
        * `invalid`: The audio data is not valid for training the custom model (possibly
        because it has the wrong format or sampling rate, or because it is corrupted).
        Omitted for an archive-type resource.
        """

        OK = 'ok'
        BEING_PROCESSED = 'being_processed'
        INVALID = 'invalid'


class AudioMetrics:
    """
    If audio metrics are requested, information about the signal characteristics of the
    input audio.

    :param float sampling_interval: The interval in seconds (typically 0.1 seconds)
          at which the service calculated the audio metrics. In other words, how often the
          service calculated the metrics. A single unit in each histogram (see the
          `AudioMetricsHistogramBin` object) is calculated based on a `sampling_interval`
          length of audio.
    :param AudioMetricsDetails accumulated: Detailed information about the signal
          characteristics of the input audio.
    """

    def __init__(
        self,
        sampling_interval: float,
        accumulated: 'AudioMetricsDetails',
    ) -> None:
        """
        Initialize a AudioMetrics object.

        :param float sampling_interval: The interval in seconds (typically 0.1
               seconds) at which the service calculated the audio metrics. In other words,
               how often the service calculated the metrics. A single unit in each
               histogram (see the `AudioMetricsHistogramBin` object) is calculated based
               on a `sampling_interval` length of audio.
        :param AudioMetricsDetails accumulated: Detailed information about the
               signal characteristics of the input audio.
        """
        self.sampling_interval = sampling_interval
        self.accumulated = accumulated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AudioMetrics':
        """Initialize a AudioMetrics object from a json dictionary."""
        args = {}
        if (sampling_interval := _dict.get('sampling_interval')) is not None:
            args['sampling_interval'] = sampling_interval
        else:
            raise ValueError(
                'Required property \'sampling_interval\' not present in AudioMetrics JSON'
            )
        if (accumulated := _dict.get('accumulated')) is not None:
            args['accumulated'] = AudioMetricsDetails.from_dict(accumulated)
        else:
            raise ValueError(
                'Required property \'accumulated\' not present in AudioMetrics JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioMetrics object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'sampling_interval') and self.sampling_interval is not None:
            _dict['sampling_interval'] = self.sampling_interval
        if hasattr(self, 'accumulated') and self.accumulated is not None:
            if isinstance(self.accumulated, dict):
                _dict['accumulated'] = self.accumulated
            else:
                _dict['accumulated'] = self.accumulated.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AudioMetrics object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AudioMetrics') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AudioMetrics') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioMetricsDetails:
    """
    Detailed information about the signal characteristics of the input audio.

    :param bool final: If `true`, indicates the end of the audio stream, meaning
          that transcription is complete. Currently, the field is always `true`. The
          service returns metrics just once per audio stream. The results provide
          aggregated audio metrics that pertain to the complete audio stream.
    :param float end_time: The end time in seconds of the block of audio to which
          the metrics apply.
    :param float signal_to_noise_ratio: (optional) The signal-to-noise ratio (SNR)
          for the audio signal. The value indicates the ratio of speech to noise in the
          audio. A valid value lies in the range of 0 to 100 decibels (dB). The service
          omits the field if it cannot compute the SNR for the audio.
    :param float speech_ratio: The ratio of speech to non-speech segments in the
          audio signal. The value lies in the range of 0.0 to 1.0.
    :param float high_frequency_loss: The probability that the audio signal is
          missing the upper half of its frequency content.
          * A value close to 1.0 typically indicates artificially up-sampled audio, which
          negatively impacts the accuracy of the transcription results.
          * A value at or near 0.0 indicates that the audio signal is good and has a full
          spectrum.
          * A value around 0.5 means that detection of the frequency content is unreliable
          or not available.
    :param List[AudioMetricsHistogramBin] direct_current_offset: An array of
          `AudioMetricsHistogramBin` objects that defines a histogram of the cumulative
          direct current (DC) component of the audio signal.
    :param List[AudioMetricsHistogramBin] clipping_rate: An array of
          `AudioMetricsHistogramBin` objects that defines a histogram of the clipping rate
          for the audio segments. The clipping rate is defined as the fraction of samples
          in the segment that reach the maximum or minimum value that is offered by the
          audio quantization range. The service auto-detects either a 16-bit Pulse-Code
          Modulation(PCM) audio range (-32768 to +32767) or a unit range (-1.0 to +1.0).
          The clipping rate is between 0.0 and 1.0, with higher values indicating possible
          degradation of speech recognition.
    :param List[AudioMetricsHistogramBin] speech_level: An array of
          `AudioMetricsHistogramBin` objects that defines a histogram of the signal level
          in segments of the audio that contain speech. The signal level is computed as
          the Root-Mean-Square (RMS) value in a decibel (dB) scale normalized to the range
          0.0 (minimum level) to 1.0 (maximum level).
    :param List[AudioMetricsHistogramBin] non_speech_level: An array of
          `AudioMetricsHistogramBin` objects that defines a histogram of the signal level
          in segments of the audio that do not contain speech. The signal level is
          computed as the Root-Mean-Square (RMS) value in a decibel (dB) scale normalized
          to the range 0.0 (minimum level) to 1.0 (maximum level).
    """

    def __init__(
        self,
        final: bool,
        end_time: float,
        speech_ratio: float,
        high_frequency_loss: float,
        direct_current_offset: List['AudioMetricsHistogramBin'],
        clipping_rate: List['AudioMetricsHistogramBin'],
        speech_level: List['AudioMetricsHistogramBin'],
        non_speech_level: List['AudioMetricsHistogramBin'],
        *,
        signal_to_noise_ratio: Optional[float] = None,
    ) -> None:
        """
        Initialize a AudioMetricsDetails object.

        :param bool final: If `true`, indicates the end of the audio stream,
               meaning that transcription is complete. Currently, the field is always
               `true`. The service returns metrics just once per audio stream. The results
               provide aggregated audio metrics that pertain to the complete audio stream.
        :param float end_time: The end time in seconds of the block of audio to
               which the metrics apply.
        :param float speech_ratio: The ratio of speech to non-speech segments in
               the audio signal. The value lies in the range of 0.0 to 1.0.
        :param float high_frequency_loss: The probability that the audio signal is
               missing the upper half of its frequency content.
               * A value close to 1.0 typically indicates artificially up-sampled audio,
               which negatively impacts the accuracy of the transcription results.
               * A value at or near 0.0 indicates that the audio signal is good and has a
               full spectrum.
               * A value around 0.5 means that detection of the frequency content is
               unreliable or not available.
        :param List[AudioMetricsHistogramBin] direct_current_offset: An array of
               `AudioMetricsHistogramBin` objects that defines a histogram of the
               cumulative direct current (DC) component of the audio signal.
        :param List[AudioMetricsHistogramBin] clipping_rate: An array of
               `AudioMetricsHistogramBin` objects that defines a histogram of the clipping
               rate for the audio segments. The clipping rate is defined as the fraction
               of samples in the segment that reach the maximum or minimum value that is
               offered by the audio quantization range. The service auto-detects either a
               16-bit Pulse-Code Modulation(PCM) audio range (-32768 to +32767) or a unit
               range (-1.0 to +1.0). The clipping rate is between 0.0 and 1.0, with higher
               values indicating possible degradation of speech recognition.
        :param List[AudioMetricsHistogramBin] speech_level: An array of
               `AudioMetricsHistogramBin` objects that defines a histogram of the signal
               level in segments of the audio that contain speech. The signal level is
               computed as the Root-Mean-Square (RMS) value in a decibel (dB) scale
               normalized to the range 0.0 (minimum level) to 1.0 (maximum level).
        :param List[AudioMetricsHistogramBin] non_speech_level: An array of
               `AudioMetricsHistogramBin` objects that defines a histogram of the signal
               level in segments of the audio that do not contain speech. The signal level
               is computed as the Root-Mean-Square (RMS) value in a decibel (dB) scale
               normalized to the range 0.0 (minimum level) to 1.0 (maximum level).
        :param float signal_to_noise_ratio: (optional) The signal-to-noise ratio
               (SNR) for the audio signal. The value indicates the ratio of speech to
               noise in the audio. A valid value lies in the range of 0 to 100 decibels
               (dB). The service omits the field if it cannot compute the SNR for the
               audio.
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
    def from_dict(cls, _dict: Dict) -> 'AudioMetricsDetails':
        """Initialize a AudioMetricsDetails object from a json dictionary."""
        args = {}
        if (final := _dict.get('final')) is not None:
            args['final'] = final
        else:
            raise ValueError(
                'Required property \'final\' not present in AudioMetricsDetails JSON'
            )
        if (end_time := _dict.get('end_time')) is not None:
            args['end_time'] = end_time
        else:
            raise ValueError(
                'Required property \'end_time\' not present in AudioMetricsDetails JSON'
            )
        if (signal_to_noise_ratio :=
                _dict.get('signal_to_noise_ratio')) is not None:
            args['signal_to_noise_ratio'] = signal_to_noise_ratio
        if (speech_ratio := _dict.get('speech_ratio')) is not None:
            args['speech_ratio'] = speech_ratio
        else:
            raise ValueError(
                'Required property \'speech_ratio\' not present in AudioMetricsDetails JSON'
            )
        if (high_frequency_loss :=
                _dict.get('high_frequency_loss')) is not None:
            args['high_frequency_loss'] = high_frequency_loss
        else:
            raise ValueError(
                'Required property \'high_frequency_loss\' not present in AudioMetricsDetails JSON'
            )
        if (direct_current_offset :=
                _dict.get('direct_current_offset')) is not None:
            args['direct_current_offset'] = [
                AudioMetricsHistogramBin.from_dict(v)
                for v in direct_current_offset
            ]
        else:
            raise ValueError(
                'Required property \'direct_current_offset\' not present in AudioMetricsDetails JSON'
            )
        if (clipping_rate := _dict.get('clipping_rate')) is not None:
            args['clipping_rate'] = [
                AudioMetricsHistogramBin.from_dict(v) for v in clipping_rate
            ]
        else:
            raise ValueError(
                'Required property \'clipping_rate\' not present in AudioMetricsDetails JSON'
            )
        if (speech_level := _dict.get('speech_level')) is not None:
            args['speech_level'] = [
                AudioMetricsHistogramBin.from_dict(v) for v in speech_level
            ]
        else:
            raise ValueError(
                'Required property \'speech_level\' not present in AudioMetricsDetails JSON'
            )
        if (non_speech_level := _dict.get('non_speech_level')) is not None:
            args['non_speech_level'] = [
                AudioMetricsHistogramBin.from_dict(v) for v in non_speech_level
            ]
        else:
            raise ValueError(
                'Required property \'non_speech_level\' not present in AudioMetricsDetails JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioMetricsDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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
            direct_current_offset_list = []
            for v in self.direct_current_offset:
                if isinstance(v, dict):
                    direct_current_offset_list.append(v)
                else:
                    direct_current_offset_list.append(v.to_dict())
            _dict['direct_current_offset'] = direct_current_offset_list
        if hasattr(self, 'clipping_rate') and self.clipping_rate is not None:
            clipping_rate_list = []
            for v in self.clipping_rate:
                if isinstance(v, dict):
                    clipping_rate_list.append(v)
                else:
                    clipping_rate_list.append(v.to_dict())
            _dict['clipping_rate'] = clipping_rate_list
        if hasattr(self, 'speech_level') and self.speech_level is not None:
            speech_level_list = []
            for v in self.speech_level:
                if isinstance(v, dict):
                    speech_level_list.append(v)
                else:
                    speech_level_list.append(v.to_dict())
            _dict['speech_level'] = speech_level_list
        if hasattr(self,
                   'non_speech_level') and self.non_speech_level is not None:
            non_speech_level_list = []
            for v in self.non_speech_level:
                if isinstance(v, dict):
                    non_speech_level_list.append(v)
                else:
                    non_speech_level_list.append(v.to_dict())
            _dict['non_speech_level'] = non_speech_level_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AudioMetricsDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AudioMetricsDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AudioMetricsDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioMetricsHistogramBin:
    """
    A bin with defined boundaries that indicates the number of values in a range of signal
    characteristics for a histogram. The first and last bins of a histogram are the
    boundary bins. They cover the intervals between negative infinity and the first
    boundary, and between the last boundary and positive infinity, respectively.

    :param float begin: The lower boundary of the bin in the histogram.
    :param float end: The upper boundary of the bin in the histogram.
    :param int count: The number of values in the bin of the histogram.
    """

    def __init__(
        self,
        begin: float,
        end: float,
        count: int,
    ) -> None:
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
    def from_dict(cls, _dict: Dict) -> 'AudioMetricsHistogramBin':
        """Initialize a AudioMetricsHistogramBin object from a json dictionary."""
        args = {}
        if (begin := _dict.get('begin')) is not None:
            args['begin'] = begin
        else:
            raise ValueError(
                'Required property \'begin\' not present in AudioMetricsHistogramBin JSON'
            )
        if (end := _dict.get('end')) is not None:
            args['end'] = end
        else:
            raise ValueError(
                'Required property \'end\' not present in AudioMetricsHistogramBin JSON'
            )
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        else:
            raise ValueError(
                'Required property \'count\' not present in AudioMetricsHistogramBin JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioMetricsHistogramBin object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'begin') and self.begin is not None:
            _dict['begin'] = self.begin
        if hasattr(self, 'end') and self.end is not None:
            _dict['end'] = self.end
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AudioMetricsHistogramBin object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AudioMetricsHistogramBin') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AudioMetricsHistogramBin') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AudioResource:
    """
    Information about an audio resource from a custom acoustic model.

    :param int duration: The total seconds of audio in the audio resource.
    :param str name: _For an archive-type resource_, the user-specified name of the
          resource.
          _For an audio-type resource_, the user-specified name of the resource or the
          name of the audio file that the user added for the resource. The value depends
          on the method that is called.
    :param AudioDetails details: An `AudioDetails` object that provides detailed
          information about the audio resource. The object is empty until the service
          finishes processing the audio.
    :param str status: The status of the audio resource:
          * `ok`: The service successfully analyzed the audio data. The data can be used
          to train the custom model.
          * `being_processed`: The service is still analyzing the audio data. The service
          cannot accept requests to add new audio resources or to train the custom model
          until its analysis is complete.
          * `invalid`: The audio data is not valid for training the custom model (possibly
          because it has the wrong format or sampling rate, or because it is corrupted).
          For an archive file, the entire archive is invalid if any of its audio files are
          invalid.
    """

    def __init__(
        self,
        duration: int,
        name: str,
        details: 'AudioDetails',
        status: str,
    ) -> None:
        """
        Initialize a AudioResource object.

        :param int duration: The total seconds of audio in the audio resource.
        :param str name: _For an archive-type resource_, the user-specified name of
               the resource.
               _For an audio-type resource_, the user-specified name of the resource or
               the name of the audio file that the user added for the resource. The value
               depends on the method that is called.
        :param AudioDetails details: An `AudioDetails` object that provides
               detailed information about the audio resource. The object is empty until
               the service finishes processing the audio.
        :param str status: The status of the audio resource:
               * `ok`: The service successfully analyzed the audio data. The data can be
               used to train the custom model.
               * `being_processed`: The service is still analyzing the audio data. The
               service cannot accept requests to add new audio resources or to train the
               custom model until its analysis is complete.
               * `invalid`: The audio data is not valid for training the custom model
               (possibly because it has the wrong format or sampling rate, or because it
               is corrupted). For an archive file, the entire archive is invalid if any of
               its audio files are invalid.
        """
        self.duration = duration
        self.name = name
        self.details = details
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AudioResource':
        """Initialize a AudioResource object from a json dictionary."""
        args = {}
        if (duration := _dict.get('duration')) is not None:
            args['duration'] = duration
        else:
            raise ValueError(
                'Required property \'duration\' not present in AudioResource JSON'
            )
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in AudioResource JSON')
        if (details := _dict.get('details')) is not None:
            args['details'] = AudioDetails.from_dict(details)
        else:
            raise ValueError(
                'Required property \'details\' not present in AudioResource JSON'
            )
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError(
                'Required property \'status\' not present in AudioResource JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'duration') and self.duration is not None:
            _dict['duration'] = self.duration
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'details') and self.details is not None:
            if isinstance(self.details, dict):
                _dict['details'] = self.details
            else:
                _dict['details'] = self.details.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AudioResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AudioResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AudioResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the audio resource:
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

        OK = 'ok'
        BEING_PROCESSED = 'being_processed'
        INVALID = 'invalid'


class AudioResources:
    """
    Information about the audio resources from a custom acoustic model.

    :param float total_minutes_of_audio: The total minutes of accumulated audio
          summed over all of the valid audio resources for the custom acoustic model. You
          can use this value to determine whether the custom model has too little or too
          much audio to begin training.
    :param List[AudioResource] audio: An array of `AudioResource` objects that
          provides information about the audio resources of the custom acoustic model. The
          array is empty if the custom model has no audio resources.
    """

    def __init__(
        self,
        total_minutes_of_audio: float,
        audio: List['AudioResource'],
    ) -> None:
        """
        Initialize a AudioResources object.

        :param float total_minutes_of_audio: The total minutes of accumulated audio
               summed over all of the valid audio resources for the custom acoustic model.
               You can use this value to determine whether the custom model has too little
               or too much audio to begin training.
        :param List[AudioResource] audio: An array of `AudioResource` objects that
               provides information about the audio resources of the custom acoustic
               model. The array is empty if the custom model has no audio resources.
        """
        self.total_minutes_of_audio = total_minutes_of_audio
        self.audio = audio

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AudioResources':
        """Initialize a AudioResources object from a json dictionary."""
        args = {}
        if (total_minutes_of_audio :=
                _dict.get('total_minutes_of_audio')) is not None:
            args['total_minutes_of_audio'] = total_minutes_of_audio
        else:
            raise ValueError(
                'Required property \'total_minutes_of_audio\' not present in AudioResources JSON'
            )
        if (audio := _dict.get('audio')) is not None:
            args['audio'] = [AudioResource.from_dict(v) for v in audio]
        else:
            raise ValueError(
                'Required property \'audio\' not present in AudioResources JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AudioResources object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_minutes_of_audio'
                  ) and self.total_minutes_of_audio is not None:
            _dict['total_minutes_of_audio'] = self.total_minutes_of_audio
        if hasattr(self, 'audio') and self.audio is not None:
            audio_list = []
            for v in self.audio:
                if isinstance(v, dict):
                    audio_list.append(v)
                else:
                    audio_list.append(v.to_dict())
            _dict['audio'] = audio_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AudioResources object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AudioResources') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AudioResources') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Corpora:
    """
    Information about the corpora from a custom language model.

    :param List[Corpus] corpora: An array of `Corpus` objects that provides
          information about the corpora for the custom model. The array is empty if the
          custom model has no corpora.
    """

    def __init__(
        self,
        corpora: List['Corpus'],
    ) -> None:
        """
        Initialize a Corpora object.

        :param List[Corpus] corpora: An array of `Corpus` objects that provides
               information about the corpora for the custom model. The array is empty if
               the custom model has no corpora.
        """
        self.corpora = corpora

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Corpora':
        """Initialize a Corpora object from a json dictionary."""
        args = {}
        if (corpora := _dict.get('corpora')) is not None:
            args['corpora'] = [Corpus.from_dict(v) for v in corpora]
        else:
            raise ValueError(
                'Required property \'corpora\' not present in Corpora JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Corpora object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'corpora') and self.corpora is not None:
            corpora_list = []
            for v in self.corpora:
                if isinstance(v, dict):
                    corpora_list.append(v)
                else:
                    corpora_list.append(v.to_dict())
            _dict['corpora'] = corpora_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Corpora object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Corpora') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Corpora') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Corpus:
    """
    Information about a corpus from a custom language model.

    :param str name: The name of the corpus.
    :param int total_words: The total number of words in the corpus. The value is
          `0` while the corpus is being processed.
    :param int out_of_vocabulary_words: _For custom models that are based on large
          speech models and previous-generation models_, the number of OOV words extracted
          from the corpus. The value is `0` while the corpus is being processed.
          _For custom models that are based on next-generation models_, no OOV words are
          extracted from corpora, so the value is always `0`.
    :param str status: The status of the corpus:
          * `analyzed`: The service successfully analyzed the corpus. The custom model can
          be trained with data from the corpus.
          * `being_processed`: The service is still analyzing the corpus. The service
          cannot accept requests to add new resources or to train the custom model.
          * `undetermined`: The service encountered an error while processing the corpus.
          The `error` field describes the failure.
    :param str error: (optional) If the status of the corpus is `undetermined`, the
          following message: `Analysis of corpus 'name' failed. Please try adding the
          corpus again by setting the 'allow_overwrite' flag to 'true'`.
    """

    def __init__(
        self,
        name: str,
        total_words: int,
        out_of_vocabulary_words: int,
        status: str,
        *,
        error: Optional[str] = None,
    ) -> None:
        """
        Initialize a Corpus object.

        :param str name: The name of the corpus.
        :param int total_words: The total number of words in the corpus. The value
               is `0` while the corpus is being processed.
        :param int out_of_vocabulary_words: _For custom models that are based on
               large speech models and previous-generation models_, the number of OOV
               words extracted from the corpus. The value is `0` while the corpus is being
               processed.
               _For custom models that are based on next-generation models_, no OOV words
               are extracted from corpora, so the value is always `0`.
        :param str status: The status of the corpus:
               * `analyzed`: The service successfully analyzed the corpus. The custom
               model can be trained with data from the corpus.
               * `being_processed`: The service is still analyzing the corpus. The service
               cannot accept requests to add new resources or to train the custom model.
               * `undetermined`: The service encountered an error while processing the
               corpus. The `error` field describes the failure.
        :param str error: (optional) If the status of the corpus is `undetermined`,
               the following message: `Analysis of corpus 'name' failed. Please try adding
               the corpus again by setting the 'allow_overwrite' flag to 'true'`.
        """
        self.name = name
        self.total_words = total_words
        self.out_of_vocabulary_words = out_of_vocabulary_words
        self.status = status
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Corpus':
        """Initialize a Corpus object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in Corpus JSON')
        if (total_words := _dict.get('total_words')) is not None:
            args['total_words'] = total_words
        else:
            raise ValueError(
                'Required property \'total_words\' not present in Corpus JSON')
        if (out_of_vocabulary_words :=
                _dict.get('out_of_vocabulary_words')) is not None:
            args['out_of_vocabulary_words'] = out_of_vocabulary_words
        else:
            raise ValueError(
                'Required property \'out_of_vocabulary_words\' not present in Corpus JSON'
            )
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError(
                'Required property \'status\' not present in Corpus JSON')
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Corpus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Corpus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Corpus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Corpus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the corpus:
        * `analyzed`: The service successfully analyzed the corpus. The custom model can
        be trained with data from the corpus.
        * `being_processed`: The service is still analyzing the corpus. The service cannot
        accept requests to add new resources or to train the custom model.
        * `undetermined`: The service encountered an error while processing the corpus.
        The `error` field describes the failure.
        """

        ANALYZED = 'analyzed'
        BEING_PROCESSED = 'being_processed'
        UNDETERMINED = 'undetermined'


class CustomWord:
    """
    Information about a word that is to be added to a custom language model.

    :param str word: (optional) For the [Add custom words](#addwords) method, you
          must specify the custom word that is to be added to or updated in the custom
          model. Do not use characters that need to be URL-encoded, for example, spaces,
          slashes, backslashes, colons, ampersands, double quotes, plus signs, equals
          signs, or question marks. Use a `-` (dash) or `_` (underscore) to connect the
          tokens of compound words. A Japanese custom word can include at most 25
          characters, not including leading or trailing spaces.
          Omit this parameter for the [Add a custom word](#addword) method.
    :param List[str] mapping_only: (optional) Parameter for custom words. You can
          use the 'mapping_only' key in custom words as a form of post processing. This
          key parameter has a boolean value to determine whether 'sounds_like' (for
          non-Japanese models) or word (for Japanese) is not used for the model
          fine-tuning, but for the replacement for 'display_as'. This feature helps you
          when you use custom words exclusively to map 'sounds_like' (or word) to
          'display_as' value. When you use custom words solely for post-processing
          purposes that does not need fine-tuning.
    :param List[str] sounds_like: (optional) As array of sounds-like pronunciations
          for the custom word. Specify how words that are difficult to pronounce, foreign
          words, acronyms, and so on can be pronounced by users.
          * _For custom models that are based on previous-generation models_, for a word
          that is not in the service's base vocabulary, omit the parameter to have the
          service automatically generate a sounds-like pronunciation for the word.
          * For a word that is in the service's base vocabulary, use the parameter to
          specify additional pronunciations for the word. You cannot override the default
          pronunciation of a word; pronunciations you add augment the pronunciation from
          the base vocabulary.
          A word can have at most five sounds-like pronunciations. A pronunciation can
          include at most 40 characters, not including leading or trailing spaces. A
          Japanese pronunciation can include at most 25 characters, not including leading
          or trailing spaces.
    :param str display_as: (optional) An alternative spelling for the custom word
          when it appears in a transcript. Use the parameter when you want the word to
          have a spelling that is different from its usual representation or from its
          spelling in corpora training data.
          _For custom models that are based on next-generation models_, the service uses
          the spelling of the word as the display-as value if you omit the field.
    """

    def __init__(
        self,
        *,
        word: Optional[str] = None,
        mapping_only: Optional[List[str]] = None,
        sounds_like: Optional[List[str]] = None,
        display_as: Optional[str] = None,
    ) -> None:
        """
        Initialize a CustomWord object.

        :param str word: (optional) For the [Add custom words](#addwords) method,
               you must specify the custom word that is to be added to or updated in the
               custom model. Do not use characters that need to be URL-encoded, for
               example, spaces, slashes, backslashes, colons, ampersands, double quotes,
               plus signs, equals signs, or question marks. Use a `-` (dash) or `_`
               (underscore) to connect the tokens of compound words. A Japanese custom
               word can include at most 25 characters, not including leading or trailing
               spaces.
               Omit this parameter for the [Add a custom word](#addword) method.
        :param List[str] mapping_only: (optional) Parameter for custom words. You
               can use the 'mapping_only' key in custom words as a form of post
               processing. This key parameter has a boolean value to determine whether
               'sounds_like' (for non-Japanese models) or word (for Japanese) is not used
               for the model fine-tuning, but for the replacement for 'display_as'. This
               feature helps you when you use custom words exclusively to map
               'sounds_like' (or word) to 'display_as' value. When you use custom words
               solely for post-processing purposes that does not need fine-tuning.
        :param List[str] sounds_like: (optional) As array of sounds-like
               pronunciations for the custom word. Specify how words that are difficult to
               pronounce, foreign words, acronyms, and so on can be pronounced by users.
               * _For custom models that are based on previous-generation models_, for a
               word that is not in the service's base vocabulary, omit the parameter to
               have the service automatically generate a sounds-like pronunciation for the
               word.
               * For a word that is in the service's base vocabulary, use the parameter to
               specify additional pronunciations for the word. You cannot override the
               default pronunciation of a word; pronunciations you add augment the
               pronunciation from the base vocabulary.
               A word can have at most five sounds-like pronunciations. A pronunciation
               can include at most 40 characters, not including leading or trailing
               spaces. A Japanese pronunciation can include at most 25 characters, not
               including leading or trailing spaces.
        :param str display_as: (optional) An alternative spelling for the custom
               word when it appears in a transcript. Use the parameter when you want the
               word to have a spelling that is different from its usual representation or
               from its spelling in corpora training data.
               _For custom models that are based on next-generation models_, the service
               uses the spelling of the word as the display-as value if you omit the
               field.
        """
        self.word = word
        self.mapping_only = mapping_only
        self.sounds_like = sounds_like
        self.display_as = display_as

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomWord':
        """Initialize a CustomWord object from a json dictionary."""
        args = {}
        if (word := _dict.get('word')) is not None:
            args['word'] = word
        if (mapping_only := _dict.get('mapping_only')) is not None:
            args['mapping_only'] = mapping_only
        if (sounds_like := _dict.get('sounds_like')) is not None:
            args['sounds_like'] = sounds_like
        if (display_as := _dict.get('display_as')) is not None:
            args['display_as'] = display_as
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomWord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word
        if hasattr(self, 'mapping_only') and self.mapping_only is not None:
            _dict['mapping_only'] = self.mapping_only
        if hasattr(self, 'sounds_like') and self.sounds_like is not None:
            _dict['sounds_like'] = self.sounds_like
        if hasattr(self, 'display_as') and self.display_as is not None:
            _dict['display_as'] = self.display_as
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomWord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomWord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomWord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Grammar:
    """
    Information about a grammar from a custom language model.

    :param str name: The name of the grammar.
    :param int out_of_vocabulary_words: _For custom models that are based on
          previous-generation models_, the number of OOV words extracted from the grammar.
          The value is `0` while the grammar is being processed.
          _For custom models that are based on next-generation models_, no OOV words are
          extracted from grammars, so the value is always `0`.
    :param str status: The status of the grammar:
          * `analyzed`: The service successfully analyzed the grammar. The custom model
          can be trained with data from the grammar.
          * `being_processed`: The service is still analyzing the grammar. The service
          cannot accept requests to add new resources or to train the custom model.
          * `undetermined`: The service encountered an error while processing the grammar.
          The `error` field describes the failure.
    :param str error: (optional) If the status of the grammar is `undetermined`, the
          following message: `Analysis of grammar '{grammar_name}' failed. Please try
          fixing the error or adding the grammar again by setting the 'allow_overwrite'
          flag to 'true'.`.
    """

    def __init__(
        self,
        name: str,
        out_of_vocabulary_words: int,
        status: str,
        *,
        error: Optional[str] = None,
    ) -> None:
        """
        Initialize a Grammar object.

        :param str name: The name of the grammar.
        :param int out_of_vocabulary_words: _For custom models that are based on
               previous-generation models_, the number of OOV words extracted from the
               grammar. The value is `0` while the grammar is being processed.
               _For custom models that are based on next-generation models_, no OOV words
               are extracted from grammars, so the value is always `0`.
        :param str status: The status of the grammar:
               * `analyzed`: The service successfully analyzed the grammar. The custom
               model can be trained with data from the grammar.
               * `being_processed`: The service is still analyzing the grammar. The
               service cannot accept requests to add new resources or to train the custom
               model.
               * `undetermined`: The service encountered an error while processing the
               grammar. The `error` field describes the failure.
        :param str error: (optional) If the status of the grammar is
               `undetermined`, the following message: `Analysis of grammar
               '{grammar_name}' failed. Please try fixing the error or adding the grammar
               again by setting the 'allow_overwrite' flag to 'true'.`.
        """
        self.name = name
        self.out_of_vocabulary_words = out_of_vocabulary_words
        self.status = status
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Grammar':
        """Initialize a Grammar object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in Grammar JSON')
        if (out_of_vocabulary_words :=
                _dict.get('out_of_vocabulary_words')) is not None:
            args['out_of_vocabulary_words'] = out_of_vocabulary_words
        else:
            raise ValueError(
                'Required property \'out_of_vocabulary_words\' not present in Grammar JSON'
            )
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError(
                'Required property \'status\' not present in Grammar JSON')
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Grammar object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Grammar object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Grammar') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Grammar') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the grammar:
        * `analyzed`: The service successfully analyzed the grammar. The custom model can
        be trained with data from the grammar.
        * `being_processed`: The service is still analyzing the grammar. The service
        cannot accept requests to add new resources or to train the custom model.
        * `undetermined`: The service encountered an error while processing the grammar.
        The `error` field describes the failure.
        """

        ANALYZED = 'analyzed'
        BEING_PROCESSED = 'being_processed'
        UNDETERMINED = 'undetermined'


class Grammars:
    """
    Information about the grammars from a custom language model.

    :param List[Grammar] grammars: An array of `Grammar` objects that provides
          information about the grammars for the custom model. The array is empty if the
          custom model has no grammars.
    """

    def __init__(
        self,
        grammars: List['Grammar'],
    ) -> None:
        """
        Initialize a Grammars object.

        :param List[Grammar] grammars: An array of `Grammar` objects that provides
               information about the grammars for the custom model. The array is empty if
               the custom model has no grammars.
        """
        self.grammars = grammars

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Grammars':
        """Initialize a Grammars object from a json dictionary."""
        args = {}
        if (grammars := _dict.get('grammars')) is not None:
            args['grammars'] = [Grammar.from_dict(v) for v in grammars]
        else:
            raise ValueError(
                'Required property \'grammars\' not present in Grammars JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Grammars object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'grammars') and self.grammars is not None:
            grammars_list = []
            for v in self.grammars:
                if isinstance(v, dict):
                    grammars_list.append(v)
                else:
                    grammars_list.append(v.to_dict())
            _dict['grammars'] = grammars_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Grammars object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Grammars') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Grammars') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordResult:
    """
    Information about a match for a keyword from speech recognition results.

    :param str normalized_text: A specified keyword normalized to the spoken phrase
          that matched in the audio input.
    :param float start_time: The start time in seconds of the keyword match.
    :param float end_time: The end time in seconds of the keyword match.
    :param float confidence: A confidence score for the keyword match in the range
          of 0.0 to 1.0.
    """

    def __init__(
        self,
        normalized_text: str,
        start_time: float,
        end_time: float,
        confidence: float,
    ) -> None:
        """
        Initialize a KeywordResult object.

        :param str normalized_text: A specified keyword normalized to the spoken
               phrase that matched in the audio input.
        :param float start_time: The start time in seconds of the keyword match.
        :param float end_time: The end time in seconds of the keyword match.
        :param float confidence: A confidence score for the keyword match in the
               range of 0.0 to 1.0.
        """
        self.normalized_text = normalized_text
        self.start_time = start_time
        self.end_time = end_time
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KeywordResult':
        """Initialize a KeywordResult object from a json dictionary."""
        args = {}
        if (normalized_text := _dict.get('normalized_text')) is not None:
            args['normalized_text'] = normalized_text
        else:
            raise ValueError(
                'Required property \'normalized_text\' not present in KeywordResult JSON'
            )
        if (start_time := _dict.get('start_time')) is not None:
            args['start_time'] = start_time
        else:
            raise ValueError(
                'Required property \'start_time\' not present in KeywordResult JSON'
            )
        if (end_time := _dict.get('end_time')) is not None:
            args['end_time'] = end_time
        else:
            raise ValueError(
                'Required property \'end_time\' not present in KeywordResult JSON'
            )
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        else:
            raise ValueError(
                'Required property \'confidence\' not present in KeywordResult JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KeywordResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'KeywordResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KeywordResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LanguageModel:
    """
    Information about an existing custom language model.

    :param str customization_id: The customization ID (GUID) of the custom language
          model. The [Create a custom language model](#createlanguagemodel) method returns
          only this field of the object; it does not return the other fields.
    :param str created: (optional) The date and time in Coordinated Universal Time
          (UTC) at which the custom language model was created. The value is provided in
          full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :param str updated: (optional) The date and time in Coordinated Universal Time
          (UTC) at which the custom language model was last modified. The `created` and
          `updated` fields are equal when a language model is first added but has yet to
          be updated. The value is provided in full ISO 8601 format
          (YYYY-MM-DDThh:mm:ss.sTZD).
    :param str language: (optional) The language identifier of the custom language
          model (for example, `en-US`). The value matches the five-character language
          identifier from the name of the base model for the custom model. This value
          might be different from the value of the `dialect` field.
    :param str dialect: (optional) The dialect of the language for the custom
          language model. _For custom models that are based on non-Spanish
          previous-generation models and on next-generation models,_ the field matches the
          language of the base model; for example, `en-US` for one of the US English
          models. _For custom models that are based on Spanish previous-generation
          models,_ the field indicates the dialect with which the model was created. The
          value can match the name of the base model or, if it was specified by the user,
          can be one of the following:
          * `es-ES` for Castilian Spanish (`es-ES` models)
          * `es-LA` for Latin American Spanish (`es-AR`, `es-CL`, `es-CO`, and `es-PE`
          models)
          * `es-US` for Mexican (North American) Spanish (`es-MX` models)
          Dialect values are case-insensitive.
    :param List[str] versions: (optional) A list of the available versions of the
          custom language model. Each element of the array indicates a version of the base
          model with which the custom model can be used. Multiple versions exist only if
          the custom model has been upgraded to a new version of its base model.
          Otherwise, only a single version is shown.
    :param str owner: (optional) The GUID of the credentials for the instance of the
          service that owns the custom language model.
    :param str name: (optional) The name of the custom language model.
    :param str description: (optional) The description of the custom language model.
    :param str base_model_name: (optional) The name of the language model for which
          the custom language model was created.
    :param str status: (optional) The current status of the custom language model:
          * `pending`: The model was created but is waiting either for valid training data
          to be added or for the service to finish analyzing added data.
          * `ready`: The model contains valid data and is ready to be trained. If the
          model contains a mix of valid and invalid resources, you need to set the
          `strict` parameter to `false` for the training to proceed.
          * `training`: The model is currently being trained.
          * `available`: The model is trained and ready to use.
          * `upgrading`: The model is currently being upgraded.
          * `failed`: Training of the model failed.
    :param int progress: (optional) A percentage that indicates the progress of the
          custom language model's current training. A value of `100` means that the model
          is fully trained. **Note:** The `progress` field does not currently reflect the
          progress of the training. The field changes from `0` to `100` when training is
          complete.
    :param str error: (optional) If an error occurred while adding a grammar file to
          the custom language model, a message that describes an `Internal Server Error`
          and includes the string `Cannot compile grammar`. The status of the custom model
          is not affected by the error, but the grammar cannot be used with the model.
    :param str warnings: (optional) If the request included unknown parameters, the
          following message: `Unexpected query parameter(s) ['parameters'] detected`,
          where `parameters` is a list that includes a quoted string for each unknown
          parameter.
    """

    def __init__(
        self,
        customization_id: str,
        *,
        created: Optional[str] = None,
        updated: Optional[str] = None,
        language: Optional[str] = None,
        dialect: Optional[str] = None,
        versions: Optional[List[str]] = None,
        owner: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        base_model_name: Optional[str] = None,
        status: Optional[str] = None,
        progress: Optional[int] = None,
        error: Optional[str] = None,
        warnings: Optional[str] = None,
    ) -> None:
        """
        Initialize a LanguageModel object.

        :param str customization_id: The customization ID (GUID) of the custom
               language model. The [Create a custom language model](#createlanguagemodel)
               method returns only this field of the object; it does not return the other
               fields.
        :param str created: (optional) The date and time in Coordinated Universal
               Time (UTC) at which the custom language model was created. The value is
               provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str updated: (optional) The date and time in Coordinated Universal
               Time (UTC) at which the custom language model was last modified. The
               `created` and `updated` fields are equal when a language model is first
               added but has yet to be updated. The value is provided in full ISO 8601
               format (YYYY-MM-DDThh:mm:ss.sTZD).
        :param str language: (optional) The language identifier of the custom
               language model (for example, `en-US`). The value matches the five-character
               language identifier from the name of the base model for the custom model.
               This value might be different from the value of the `dialect` field.
        :param str dialect: (optional) The dialect of the language for the custom
               language model. _For custom models that are based on non-Spanish
               previous-generation models and on next-generation models,_ the field
               matches the language of the base model; for example, `en-US` for one of the
               US English models. _For custom models that are based on Spanish
               previous-generation models,_ the field indicates the dialect with which the
               model was created. The value can match the name of the base model or, if it
               was specified by the user, can be one of the following:
               * `es-ES` for Castilian Spanish (`es-ES` models)
               * `es-LA` for Latin American Spanish (`es-AR`, `es-CL`, `es-CO`, and
               `es-PE` models)
               * `es-US` for Mexican (North American) Spanish (`es-MX` models)
               Dialect values are case-insensitive.
        :param List[str] versions: (optional) A list of the available versions of
               the custom language model. Each element of the array indicates a version of
               the base model with which the custom model can be used. Multiple versions
               exist only if the custom model has been upgraded to a new version of its
               base model. Otherwise, only a single version is shown.
        :param str owner: (optional) The GUID of the credentials for the instance
               of the service that owns the custom language model.
        :param str name: (optional) The name of the custom language model.
        :param str description: (optional) The description of the custom language
               model.
        :param str base_model_name: (optional) The name of the language model for
               which the custom language model was created.
        :param str status: (optional) The current status of the custom language
               model:
               * `pending`: The model was created but is waiting either for valid training
               data to be added or for the service to finish analyzing added data.
               * `ready`: The model contains valid data and is ready to be trained. If the
               model contains a mix of valid and invalid resources, you need to set the
               `strict` parameter to `false` for the training to proceed.
               * `training`: The model is currently being trained.
               * `available`: The model is trained and ready to use.
               * `upgrading`: The model is currently being upgraded.
               * `failed`: Training of the model failed.
        :param int progress: (optional) A percentage that indicates the progress of
               the custom language model's current training. A value of `100` means that
               the model is fully trained. **Note:** The `progress` field does not
               currently reflect the progress of the training. The field changes from `0`
               to `100` when training is complete.
        :param str error: (optional) If an error occurred while adding a grammar
               file to the custom language model, a message that describes an `Internal
               Server Error` and includes the string `Cannot compile grammar`. The status
               of the custom model is not affected by the error, but the grammar cannot be
               used with the model.
        :param str warnings: (optional) If the request included unknown parameters,
               the following message: `Unexpected query parameter(s) ['parameters']
               detected`, where `parameters` is a list that includes a quoted string for
               each unknown parameter.
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
    def from_dict(cls, _dict: Dict) -> 'LanguageModel':
        """Initialize a LanguageModel object from a json dictionary."""
        args = {}
        if (customization_id := _dict.get('customization_id')) is not None:
            args['customization_id'] = customization_id
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in LanguageModel JSON'
            )
        if (created := _dict.get('created')) is not None:
            args['created'] = created
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = updated
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        if (dialect := _dict.get('dialect')) is not None:
            args['dialect'] = dialect
        if (versions := _dict.get('versions')) is not None:
            args['versions'] = versions
        if (owner := _dict.get('owner')) is not None:
            args['owner'] = owner
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (base_model_name := _dict.get('base_model_name')) is not None:
            args['base_model_name'] = base_model_name
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (progress := _dict.get('progress')) is not None:
            args['progress'] = progress
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        if (warnings := _dict.get('warnings')) is not None:
            args['warnings'] = warnings
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LanguageModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LanguageModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LanguageModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LanguageModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the custom language model:
        * `pending`: The model was created but is waiting either for valid training data
        to be added or for the service to finish analyzing added data.
        * `ready`: The model contains valid data and is ready to be trained. If the model
        contains a mix of valid and invalid resources, you need to set the `strict`
        parameter to `false` for the training to proceed.
        * `training`: The model is currently being trained.
        * `available`: The model is trained and ready to use.
        * `upgrading`: The model is currently being upgraded.
        * `failed`: Training of the model failed.
        """

        PENDING = 'pending'
        READY = 'ready'
        TRAINING = 'training'
        AVAILABLE = 'available'
        UPGRADING = 'upgrading'
        FAILED = 'failed'


class LanguageModels:
    """
    Information about existing custom language models.

    :param List[LanguageModel] customizations: An array of `LanguageModel` objects
          that provides information about each available custom language model. The array
          is empty if the requesting credentials own no custom language models (if no
          language is specified) or own no custom language models for the specified
          language.
    """

    def __init__(
        self,
        customizations: List['LanguageModel'],
    ) -> None:
        """
        Initialize a LanguageModels object.

        :param List[LanguageModel] customizations: An array of `LanguageModel`
               objects that provides information about each available custom language
               model. The array is empty if the requesting credentials own no custom
               language models (if no language is specified) or own no custom language
               models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LanguageModels':
        """Initialize a LanguageModels object from a json dictionary."""
        args = {}
        if (customizations := _dict.get('customizations')) is not None:
            args['customizations'] = [
                LanguageModel.from_dict(v) for v in customizations
            ]
        else:
            raise ValueError(
                'Required property \'customizations\' not present in LanguageModels JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LanguageModels object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'customizations') and self.customizations is not None:
            customizations_list = []
            for v in self.customizations:
                if isinstance(v, dict):
                    customizations_list.append(v)
                else:
                    customizations_list.append(v.to_dict())
            _dict['customizations'] = customizations_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LanguageModels object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LanguageModels') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LanguageModels') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProcessedAudio:
    """
    Detailed timing information about the service's processing of the input audio.

    :param float received: The seconds of audio that the service has received as of
          this response. The value of the field is greater than the values of the
          `transcription` and `speaker_labels` fields during speech recognition
          processing, since the service first has to receive the audio before it can begin
          to process it. The final value can also be greater than the value of the
          `transcription` and `speaker_labels` fields by a fractional number of seconds.
    :param float seen_by_engine: The seconds of audio that the service has passed to
          its speech-processing engine as of this response. The value of the field is
          greater than the values of the `transcription` and `speaker_labels` fields
          during speech recognition processing. The `received` and `seen_by_engine` fields
          have identical values when the service has finished processing all audio. This
          final value can be greater than the value of the `transcription` and
          `speaker_labels` fields by a fractional number of seconds.
    :param float transcription: The seconds of audio that the service has processed
          for speech recognition as of this response.
    :param float speaker_labels: (optional) If speaker labels are requested, the
          seconds of audio that the service has processed to determine speaker labels as
          of this response. This value often trails the value of the `transcription` field
          during speech recognition processing. The `transcription` and `speaker_labels`
          fields have identical values when the service has finished processing all audio.
    """

    def __init__(
        self,
        received: float,
        seen_by_engine: float,
        transcription: float,
        *,
        speaker_labels: Optional[float] = None,
    ) -> None:
        """
        Initialize a ProcessedAudio object.

        :param float received: The seconds of audio that the service has received
               as of this response. The value of the field is greater than the values of
               the `transcription` and `speaker_labels` fields during speech recognition
               processing, since the service first has to receive the audio before it can
               begin to process it. The final value can also be greater than the value of
               the `transcription` and `speaker_labels` fields by a fractional number of
               seconds.
        :param float seen_by_engine: The seconds of audio that the service has
               passed to its speech-processing engine as of this response. The value of
               the field is greater than the values of the `transcription` and
               `speaker_labels` fields during speech recognition processing. The
               `received` and `seen_by_engine` fields have identical values when the
               service has finished processing all audio. This final value can be greater
               than the value of the `transcription` and `speaker_labels` fields by a
               fractional number of seconds.
        :param float transcription: The seconds of audio that the service has
               processed for speech recognition as of this response.
        :param float speaker_labels: (optional) If speaker labels are requested,
               the seconds of audio that the service has processed to determine speaker
               labels as of this response. This value often trails the value of the
               `transcription` field during speech recognition processing. The
               `transcription` and `speaker_labels` fields have identical values when the
               service has finished processing all audio.
        """
        self.received = received
        self.seen_by_engine = seen_by_engine
        self.transcription = transcription
        self.speaker_labels = speaker_labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProcessedAudio':
        """Initialize a ProcessedAudio object from a json dictionary."""
        args = {}
        if (received := _dict.get('received')) is not None:
            args['received'] = received
        else:
            raise ValueError(
                'Required property \'received\' not present in ProcessedAudio JSON'
            )
        if (seen_by_engine := _dict.get('seen_by_engine')) is not None:
            args['seen_by_engine'] = seen_by_engine
        else:
            raise ValueError(
                'Required property \'seen_by_engine\' not present in ProcessedAudio JSON'
            )
        if (transcription := _dict.get('transcription')) is not None:
            args['transcription'] = transcription
        else:
            raise ValueError(
                'Required property \'transcription\' not present in ProcessedAudio JSON'
            )
        if (speaker_labels := _dict.get('speaker_labels')) is not None:
            args['speaker_labels'] = speaker_labels
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProcessedAudio object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProcessedAudio object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProcessedAudio') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProcessedAudio') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProcessingMetrics:
    """
    If processing metrics are requested, information about the service's processing of the
    input audio. Processing metrics are not available with the synchronous [Recognize
    audio](#recognize) method.

    :param ProcessedAudio processed_audio: Detailed timing information about the
          service's processing of the input audio.
    :param float wall_clock_since_first_byte_received: The amount of real time in
          seconds that has passed since the service received the first byte of input
          audio. Values in this field are generally multiples of the specified metrics
          interval, with two differences:
          * Values might not reflect exact intervals (for instance, 0.25, 0.5, and so on).
          Actual values might be 0.27, 0.52, and so on, depending on when the service
          receives and processes audio.
          * The service also returns values for transcription events if you set the
          `interim_results` parameter to `true`. The service returns both processing
          metrics and transcription results when such events occur.
    :param bool periodic: An indication of whether the metrics apply to a periodic
          interval or a transcription event:
          * `true` means that the response was triggered by a specified processing
          interval. The information contains processing metrics only.
          * `false` means that the response was triggered by a transcription event. The
          information contains processing metrics plus transcription results.
          Use the field to identify why the service generated the response and to filter
          different results if necessary.
    """

    def __init__(
        self,
        processed_audio: 'ProcessedAudio',
        wall_clock_since_first_byte_received: float,
        periodic: bool,
    ) -> None:
        """
        Initialize a ProcessingMetrics object.

        :param ProcessedAudio processed_audio: Detailed timing information about
               the service's processing of the input audio.
        :param float wall_clock_since_first_byte_received: The amount of real time
               in seconds that has passed since the service received the first byte of
               input audio. Values in this field are generally multiples of the specified
               metrics interval, with two differences:
               * Values might not reflect exact intervals (for instance, 0.25, 0.5, and so
               on). Actual values might be 0.27, 0.52, and so on, depending on when the
               service receives and processes audio.
               * The service also returns values for transcription events if you set the
               `interim_results` parameter to `true`. The service returns both processing
               metrics and transcription results when such events occur.
        :param bool periodic: An indication of whether the metrics apply to a
               periodic interval or a transcription event:
               * `true` means that the response was triggered by a specified processing
               interval. The information contains processing metrics only.
               * `false` means that the response was triggered by a transcription event.
               The information contains processing metrics plus transcription results.
               Use the field to identify why the service generated the response and to
               filter different results if necessary.
        """
        self.processed_audio = processed_audio
        self.wall_clock_since_first_byte_received = wall_clock_since_first_byte_received
        self.periodic = periodic

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProcessingMetrics':
        """Initialize a ProcessingMetrics object from a json dictionary."""
        args = {}
        if (processed_audio := _dict.get('processed_audio')) is not None:
            args['processed_audio'] = ProcessedAudio.from_dict(processed_audio)
        else:
            raise ValueError(
                'Required property \'processed_audio\' not present in ProcessingMetrics JSON'
            )
        if (wall_clock_since_first_byte_received :=
                _dict.get('wall_clock_since_first_byte_received')) is not None:
            args[
                'wall_clock_since_first_byte_received'] = wall_clock_since_first_byte_received
        else:
            raise ValueError(
                'Required property \'wall_clock_since_first_byte_received\' not present in ProcessingMetrics JSON'
            )
        if (periodic := _dict.get('periodic')) is not None:
            args['periodic'] = periodic
        else:
            raise ValueError(
                'Required property \'periodic\' not present in ProcessingMetrics JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProcessingMetrics object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'processed_audio') and self.processed_audio is not None:
            if isinstance(self.processed_audio, dict):
                _dict['processed_audio'] = self.processed_audio
            else:
                _dict['processed_audio'] = self.processed_audio.to_dict()
        if hasattr(self, 'wall_clock_since_first_byte_received'
                  ) and self.wall_clock_since_first_byte_received is not None:
            _dict[
                'wall_clock_since_first_byte_received'] = self.wall_clock_since_first_byte_received
        if hasattr(self, 'periodic') and self.periodic is not None:
            _dict['periodic'] = self.periodic
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProcessingMetrics object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProcessingMetrics') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProcessingMetrics') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RecognitionJob:
    """
    Information about a current asynchronous speech recognition job.

    :param str id: The ID of the asynchronous job.
    :param str status: The current status of the job:
          * `waiting`: The service is preparing the job for processing. The service
          returns this status when the job is initially created or when it is waiting for
          capacity to process the job. The job remains in this state until the service has
          the capacity to begin processing it.
          * `processing`: The service is actively processing the job.
          * `completed`: The service has finished processing the job. If the job specified
          a callback URL and the event `recognitions.completed_with_results`, the service
          sent the results with the callback notification. Otherwise, you must retrieve
          the results by checking the individual job.
          * `failed`: The job failed.
    :param str created: The date and time in Coordinated Universal Time (UTC) at
          which the job was created. The value is provided in full ISO 8601 format
          (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :param str updated: (optional) The date and time in Coordinated Universal Time
          (UTC) at which the job was last updated by the service. The value is provided in
          full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`). This field is returned only
          by the [Check jobs](#checkjobs) and [Check a job[(#checkjob) methods.
    :param str url: (optional) The URL to use to request information about the job
          with the [Check a job](#checkjob) method. This field is returned only by the
          [Create a job](#createjob) method.
    :param str user_token: (optional) The user token associated with a job that was
          created with a callback URL and a user token. This field can be returned only by
          the [Check jobs](#checkjobs) method.
    :param List[SpeechRecognitionResults] results: (optional) If the status is
          `completed`, the results of the recognition request as an array that includes a
          single instance of a `SpeechRecognitionResults` object. This field is returned
          only by the [Check a job](#checkjob) method.
    :param List[str] warnings: (optional) An array of warning messages about invalid
          parameters included with the request. Each warning includes a descriptive
          message and a list of invalid argument strings, for example, `"unexpected query
          parameter 'user_token', query parameter 'callback_url' was not specified"`. The
          request succeeds despite the warnings. This field can be returned only by the
          [Create a job](#createjob) method. (If you use the `character_insertion_bias`
          parameter with a previous-generation model, the warning message refers to the
          parameter as `lambdaBias`.).
    """

    def __init__(
        self,
        id: str,
        status: str,
        created: str,
        *,
        updated: Optional[str] = None,
        url: Optional[str] = None,
        user_token: Optional[str] = None,
        results: Optional[List['SpeechRecognitionResults']] = None,
        warnings: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a RecognitionJob object.

        :param str id: The ID of the asynchronous job.
        :param str status: The current status of the job:
               * `waiting`: The service is preparing the job for processing. The service
               returns this status when the job is initially created or when it is waiting
               for capacity to process the job. The job remains in this state until the
               service has the capacity to begin processing it.
               * `processing`: The service is actively processing the job.
               * `completed`: The service has finished processing the job. If the job
               specified a callback URL and the event
               `recognitions.completed_with_results`, the service sent the results with
               the callback notification. Otherwise, you must retrieve the results by
               checking the individual job.
               * `failed`: The job failed.
        :param str created: The date and time in Coordinated Universal Time (UTC)
               at which the job was created. The value is provided in full ISO 8601 format
               (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str updated: (optional) The date and time in Coordinated Universal
               Time (UTC) at which the job was last updated by the service. The value is
               provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`). This field
               is returned only by the [Check jobs](#checkjobs) and [Check a
               job[(#checkjob) methods.
        :param str url: (optional) The URL to use to request information about the
               job with the [Check a job](#checkjob) method. This field is returned only
               by the [Create a job](#createjob) method.
        :param str user_token: (optional) The user token associated with a job that
               was created with a callback URL and a user token. This field can be
               returned only by the [Check jobs](#checkjobs) method.
        :param List[SpeechRecognitionResults] results: (optional) If the status is
               `completed`, the results of the recognition request as an array that
               includes a single instance of a `SpeechRecognitionResults` object. This
               field is returned only by the [Check a job](#checkjob) method.
        :param List[str] warnings: (optional) An array of warning messages about
               invalid parameters included with the request. Each warning includes a
               descriptive message and a list of invalid argument strings, for example,
               `"unexpected query parameter 'user_token', query parameter 'callback_url'
               was not specified"`. The request succeeds despite the warnings. This field
               can be returned only by the [Create a job](#createjob) method. (If you use
               the `character_insertion_bias` parameter with a previous-generation model,
               the warning message refers to the parameter as `lambdaBias`.).
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
    def from_dict(cls, _dict: Dict) -> 'RecognitionJob':
        """Initialize a RecognitionJob object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError(
                'Required property \'id\' not present in RecognitionJob JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError(
                'Required property \'status\' not present in RecognitionJob JSON'
            )
        if (created := _dict.get('created')) is not None:
            args['created'] = created
        else:
            raise ValueError(
                'Required property \'created\' not present in RecognitionJob JSON'
            )
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = updated
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        if (user_token := _dict.get('user_token')) is not None:
            args['user_token'] = user_token
        if (results := _dict.get('results')) is not None:
            args['results'] = [
                SpeechRecognitionResults.from_dict(v) for v in results
            ]
        if (warnings := _dict.get('warnings')) is not None:
            args['warnings'] = warnings
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecognitionJob object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = self.warnings
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecognitionJob object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecognitionJob') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecognitionJob') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the job:
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
        """

        WAITING = 'waiting'
        PROCESSING = 'processing'
        COMPLETED = 'completed'
        FAILED = 'failed'


class RecognitionJobs:
    """
    Information about current asynchronous speech recognition jobs.

    :param List[RecognitionJob] recognitions: An array of `RecognitionJob` objects
          that provides the status for each of the user's current jobs. The array is empty
          if the user has no current jobs.
    """

    def __init__(
        self,
        recognitions: List['RecognitionJob'],
    ) -> None:
        """
        Initialize a RecognitionJobs object.

        :param List[RecognitionJob] recognitions: An array of `RecognitionJob`
               objects that provides the status for each of the user's current jobs. The
               array is empty if the user has no current jobs.
        """
        self.recognitions = recognitions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecognitionJobs':
        """Initialize a RecognitionJobs object from a json dictionary."""
        args = {}
        if (recognitions := _dict.get('recognitions')) is not None:
            args['recognitions'] = [
                RecognitionJob.from_dict(v) for v in recognitions
            ]
        else:
            raise ValueError(
                'Required property \'recognitions\' not present in RecognitionJobs JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecognitionJobs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'recognitions') and self.recognitions is not None:
            recognitions_list = []
            for v in self.recognitions:
                if isinstance(v, dict):
                    recognitions_list.append(v)
                else:
                    recognitions_list.append(v.to_dict())
            _dict['recognitions'] = recognitions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecognitionJobs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecognitionJobs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecognitionJobs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RegisterStatus:
    """
    Information about a request to register a callback for asynchronous speech
    recognition.

    :param str status: The current status of the job:
          * `created`: The service successfully allowlisted the callback URL as a result
          of the call.
          * `already created`: The URL was already allowlisted.
    :param str url: The callback URL that is successfully registered.
    """

    def __init__(
        self,
        status: str,
        url: str,
    ) -> None:
        """
        Initialize a RegisterStatus object.

        :param str status: The current status of the job:
               * `created`: The service successfully allowlisted the callback URL as a
               result of the call.
               * `already created`: The URL was already allowlisted.
        :param str url: The callback URL that is successfully registered.
        """
        self.status = status
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RegisterStatus':
        """Initialize a RegisterStatus object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError(
                'Required property \'status\' not present in RegisterStatus JSON'
            )
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in RegisterStatus JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RegisterStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RegisterStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RegisterStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RegisterStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the job:
        * `created`: The service successfully allowlisted the callback URL as a result of
        the call.
        * `already created`: The URL was already allowlisted.
        """

        CREATED = 'created'
        ALREADY_CREATED = 'already created'


class SpeakerLabelsResult:
    """
    Information about the speakers from speech recognition results.

    :param float from_: The start time of a word from the transcript. The value
          matches the start time of a word from the `timestamps` array.
    :param float to: The end time of a word from the transcript. The value matches
          the end time of a word from the `timestamps` array.
    :param int speaker: The numeric identifier that the service assigns to a speaker
          from the audio. Speaker IDs begin at `0` initially but can evolve and change
          across interim results (if supported by the method) and between interim and
          final results as the service processes the audio. They are not guaranteed to be
          sequential, contiguous, or ordered.
    :param float confidence: A score that indicates the service's confidence in its
          identification of the speaker in the range of 0.0 to 1.0.
    :param bool final: An indication of whether the service might further change
          word and speaker-label results. A value of `true` means that the service
          guarantees not to send any further updates for the current or any preceding
          results; `false` means that the service might send further updates to the
          results.
    """

    def __init__(
        self,
        from_: float,
        to: float,
        speaker: int,
        confidence: float,
        final: bool,
    ) -> None:
        """
        Initialize a SpeakerLabelsResult object.

        :param float from_: The start time of a word from the transcript. The value
               matches the start time of a word from the `timestamps` array.
        :param float to: The end time of a word from the transcript. The value
               matches the end time of a word from the `timestamps` array.
        :param int speaker: The numeric identifier that the service assigns to a
               speaker from the audio. Speaker IDs begin at `0` initially but can evolve
               and change across interim results (if supported by the method) and between
               interim and final results as the service processes the audio. They are not
               guaranteed to be sequential, contiguous, or ordered.
        :param float confidence: A score that indicates the service's confidence in
               its identification of the speaker in the range of 0.0 to 1.0.
        :param bool final: An indication of whether the service might further
               change word and speaker-label results. A value of `true` means that the
               service guarantees not to send any further updates for the current or any
               preceding results; `false` means that the service might send further
               updates to the results.
        """
        self.from_ = from_
        self.to = to
        self.speaker = speaker
        self.confidence = confidence
        self.final = final

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeakerLabelsResult':
        """Initialize a SpeakerLabelsResult object from a json dictionary."""
        args = {}
        if (from_ := _dict.get('from')) is not None:
            args['from_'] = from_
        else:
            raise ValueError(
                'Required property \'from\' not present in SpeakerLabelsResult JSON'
            )
        if (to := _dict.get('to')) is not None:
            args['to'] = to
        else:
            raise ValueError(
                'Required property \'to\' not present in SpeakerLabelsResult JSON'
            )
        if (speaker := _dict.get('speaker')) is not None:
            args['speaker'] = speaker
        else:
            raise ValueError(
                'Required property \'speaker\' not present in SpeakerLabelsResult JSON'
            )
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        else:
            raise ValueError(
                'Required property \'confidence\' not present in SpeakerLabelsResult JSON'
            )
        if (final := _dict.get('final')) is not None:
            args['final'] = final
        else:
            raise ValueError(
                'Required property \'final\' not present in SpeakerLabelsResult JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeakerLabelsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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
        if hasattr(self, 'final') and self.final is not None:
            _dict['final'] = self.final
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeakerLabelsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeakerLabelsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeakerLabelsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechModel:
    """
    Information about an available language model.

    :param str name: The name of the model for use as an identifier in calls to the
          service (for example, `en-US_BroadbandModel`).
    :param str language: The language identifier of the model (for example,
          `en-US`).
    :param int rate: The sampling rate (minimum acceptable rate for audio) used by
          the model in Hertz.
    :param str url: The URI for the model.
    :param SupportedFeatures supported_features: Indicates whether select service
          features are supported with the model.
    :param str description: A brief description of the model.
    """

    def __init__(
        self,
        name: str,
        language: str,
        rate: int,
        url: str,
        supported_features: 'SupportedFeatures',
        description: str,
    ) -> None:
        """
        Initialize a SpeechModel object.

        :param str name: The name of the model for use as an identifier in calls to
               the service (for example, `en-US_BroadbandModel`).
        :param str language: The language identifier of the model (for example,
               `en-US`).
        :param int rate: The sampling rate (minimum acceptable rate for audio) used
               by the model in Hertz.
        :param str url: The URI for the model.
        :param SupportedFeatures supported_features: Indicates whether select
               service features are supported with the model.
        :param str description: A brief description of the model.
        """
        self.name = name
        self.language = language
        self.rate = rate
        self.url = url
        self.supported_features = supported_features
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeechModel':
        """Initialize a SpeechModel object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in SpeechModel JSON')
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in SpeechModel JSON'
            )
        if (rate := _dict.get('rate')) is not None:
            args['rate'] = rate
        else:
            raise ValueError(
                'Required property \'rate\' not present in SpeechModel JSON')
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in SpeechModel JSON')
        if (supported_features := _dict.get('supported_features')) is not None:
            args['supported_features'] = SupportedFeatures.from_dict(
                supported_features)
        else:
            raise ValueError(
                'Required property \'supported_features\' not present in SpeechModel JSON'
            )
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError(
                'Required property \'description\' not present in SpeechModel JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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
            if isinstance(self.supported_features, dict):
                _dict['supported_features'] = self.supported_features
            else:
                _dict['supported_features'] = self.supported_features.to_dict()
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeechModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeechModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeechModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechModels:
    """
    Information about the available language models.

    :param List[SpeechModel] models: An array of `SpeechModel` objects that provides
          information about each available model.
    """

    def __init__(
        self,
        models: List['SpeechModel'],
    ) -> None:
        """
        Initialize a SpeechModels object.

        :param List[SpeechModel] models: An array of `SpeechModel` objects that
               provides information about each available model.
        """
        self.models = models

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeechModels':
        """Initialize a SpeechModels object from a json dictionary."""
        args = {}
        if (models := _dict.get('models')) is not None:
            args['models'] = [SpeechModel.from_dict(v) for v in models]
        else:
            raise ValueError(
                'Required property \'models\' not present in SpeechModels JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechModels object from a json dictionary."""
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
        """Return a `str` version of this SpeechModels object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeechModels') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeechModels') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechRecognitionAlternative:
    """
    An alternative transcript from speech recognition results.

    :param str transcript: A transcription of the audio.
    :param float confidence: (optional) A score that indicates the service's
          confidence in the transcript in the range of 0.0 to 1.0. The service returns a
          confidence score only for the best alternative and only with results marked as
          final.
    :param List[str] timestamps: (optional) Time alignments for each word from the
          transcript as a list of lists. Each inner list consists of three elements: the
          word followed by its start and end time in seconds, for example:
          `[["hello",0.0,1.2],["world",1.2,2.5]]`. Timestamps are returned only for the
          best alternative.
    :param List[str] word_confidence: (optional) A confidence score for each word of
          the transcript as a list of lists. Each inner list consists of two elements: the
          word and its confidence score in the range of 0.0 to 1.0, for example:
          `[["hello",0.95],["world",0.86]]`. Confidence scores are returned only for the
          best alternative and only with results marked as final.
    """

    def __init__(
        self,
        transcript: str,
        *,
        confidence: Optional[float] = None,
        timestamps: Optional[List[str]] = None,
        word_confidence: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a SpeechRecognitionAlternative object.

        :param str transcript: A transcription of the audio.
        :param float confidence: (optional) A score that indicates the service's
               confidence in the transcript in the range of 0.0 to 1.0. The service
               returns a confidence score only for the best alternative and only with
               results marked as final.
        :param List[str] timestamps: (optional) Time alignments for each word from
               the transcript as a list of lists. Each inner list consists of three
               elements: the word followed by its start and end time in seconds, for
               example: `[["hello",0.0,1.2],["world",1.2,2.5]]`. Timestamps are returned
               only for the best alternative.
        :param List[str] word_confidence: (optional) A confidence score for each
               word of the transcript as a list of lists. Each inner list consists of two
               elements: the word and its confidence score in the range of 0.0 to 1.0, for
               example: `[["hello",0.95],["world",0.86]]`. Confidence scores are returned
               only for the best alternative and only with results marked as final.
        """
        self.transcript = transcript
        self.confidence = confidence
        self.timestamps = timestamps
        self.word_confidence = word_confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeechRecognitionAlternative':
        """Initialize a SpeechRecognitionAlternative object from a json dictionary."""
        args = {}
        if (transcript := _dict.get('transcript')) is not None:
            args['transcript'] = transcript
        else:
            raise ValueError(
                'Required property \'transcript\' not present in SpeechRecognitionAlternative JSON'
            )
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        if (timestamps := _dict.get('timestamps')) is not None:
            args['timestamps'] = timestamps
        if (word_confidence := _dict.get('word_confidence')) is not None:
            args['word_confidence'] = word_confidence
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionAlternative object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeechRecognitionAlternative object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeechRecognitionAlternative') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeechRecognitionAlternative') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeechRecognitionResult:
    """
    Component results for a speech recognition request.

    :param bool final: An indication of whether the transcription results are final:
          * If `true`, the results for this utterance are final. They are guaranteed not
          to be updated further.
          * If `false`, the results are interim. They can be updated with further interim
          results until final results are eventually sent.
          **Note:** Because `final` is a reserved word in Java and Swift, the field is
          renamed `xFinal` in Java and is escaped with back quotes in Swift.
    :param List[SpeechRecognitionAlternative] alternatives: An array of alternative
          transcripts. The `alternatives` array can include additional requested output
          such as word confidence or timestamps.
    :param dict keywords_result: (optional) A dictionary (or associative array)
          whose keys are the strings specified for `keywords` if both that parameter and
          `keywords_threshold` are specified. The value for each key is an array of
          matches spotted in the audio for that keyword. Each match is described by a
          `KeywordResult` object. A keyword for which no matches are found is omitted from
          the dictionary. The dictionary is omitted entirely if no matches are found for
          any keywords.
    :param List[WordAlternativeResults] word_alternatives: (optional) An array of
          alternative hypotheses found for words of the input audio if a
          `word_alternatives_threshold` is specified.
    :param str end_of_utterance: (optional) If the `split_transcript_at_phrase_end`
          parameter is `true`, describes the reason for the split:
          * `end_of_data` - The end of the input audio stream.
          * `full_stop` - A full semantic stop, such as for the conclusion of a
          grammatical sentence. The insertion of splits is influenced by the base language
          model and biased by custom language models and grammars.
          * `reset` - The amount of audio that is currently being processed exceeds the
          two-minute maximum. The service splits the transcript to avoid excessive memory
          use.
          * `silence` - A pause or silence that is at least as long as the pause interval.
    """

    def __init__(
        self,
        final: bool,
        alternatives: List['SpeechRecognitionAlternative'],
        *,
        keywords_result: Optional[dict] = None,
        word_alternatives: Optional[List['WordAlternativeResults']] = None,
        end_of_utterance: Optional[str] = None,
    ) -> None:
        """
        Initialize a SpeechRecognitionResult object.

        :param bool final: An indication of whether the transcription results are
               final:
               * If `true`, the results for this utterance are final. They are guaranteed
               not to be updated further.
               * If `false`, the results are interim. They can be updated with further
               interim results until final results are eventually sent.
               **Note:** Because `final` is a reserved word in Java and Swift, the field
               is renamed `xFinal` in Java and is escaped with back quotes in Swift.
        :param List[SpeechRecognitionAlternative] alternatives: An array of
               alternative transcripts. The `alternatives` array can include additional
               requested output such as word confidence or timestamps.
        :param dict keywords_result: (optional) A dictionary (or associative array)
               whose keys are the strings specified for `keywords` if both that parameter
               and `keywords_threshold` are specified. The value for each key is an array
               of matches spotted in the audio for that keyword. Each match is described
               by a `KeywordResult` object. A keyword for which no matches are found is
               omitted from the dictionary. The dictionary is omitted entirely if no
               matches are found for any keywords.
        :param List[WordAlternativeResults] word_alternatives: (optional) An array
               of alternative hypotheses found for words of the input audio if a
               `word_alternatives_threshold` is specified.
        :param str end_of_utterance: (optional) If the
               `split_transcript_at_phrase_end` parameter is `true`, describes the reason
               for the split:
               * `end_of_data` - The end of the input audio stream.
               * `full_stop` - A full semantic stop, such as for the conclusion of a
               grammatical sentence. The insertion of splits is influenced by the base
               language model and biased by custom language models and grammars.
               * `reset` - The amount of audio that is currently being processed exceeds
               the two-minute maximum. The service splits the transcript to avoid
               excessive memory use.
               * `silence` - A pause or silence that is at least as long as the pause
               interval.
        """
        self.final = final
        self.alternatives = alternatives
        self.keywords_result = keywords_result
        self.word_alternatives = word_alternatives
        self.end_of_utterance = end_of_utterance

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeechRecognitionResult':
        """Initialize a SpeechRecognitionResult object from a json dictionary."""
        args = {}
        if (final := _dict.get('final')) is not None:
            args['final'] = final
        else:
            raise ValueError(
                'Required property \'final\' not present in SpeechRecognitionResult JSON'
            )
        if (alternatives := _dict.get('alternatives')) is not None:
            args['alternatives'] = [
                SpeechRecognitionAlternative.from_dict(v) for v in alternatives
            ]
        else:
            raise ValueError(
                'Required property \'alternatives\' not present in SpeechRecognitionResult JSON'
            )
        if (keywords_result := _dict.get('keywords_result')) is not None:
            args['keywords_result'] = keywords_result
        if (word_alternatives := _dict.get('word_alternatives')) is not None:
            args['word_alternatives'] = [
                WordAlternativeResults.from_dict(v) for v in word_alternatives
            ]
        if (end_of_utterance := _dict.get('end_of_utterance')) is not None:
            args['end_of_utterance'] = end_of_utterance
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'final') and self.final is not None:
            _dict['final'] = self.final
        if hasattr(self, 'alternatives') and self.alternatives is not None:
            alternatives_list = []
            for v in self.alternatives:
                if isinstance(v, dict):
                    alternatives_list.append(v)
                else:
                    alternatives_list.append(v.to_dict())
            _dict['alternatives'] = alternatives_list
        if hasattr(self,
                   'keywords_result') and self.keywords_result is not None:
            _dict['keywords_result'] = self.keywords_result
        if hasattr(self,
                   'word_alternatives') and self.word_alternatives is not None:
            word_alternatives_list = []
            for v in self.word_alternatives:
                if isinstance(v, dict):
                    word_alternatives_list.append(v)
                else:
                    word_alternatives_list.append(v.to_dict())
            _dict['word_alternatives'] = word_alternatives_list
        if hasattr(self,
                   'end_of_utterance') and self.end_of_utterance is not None:
            _dict['end_of_utterance'] = self.end_of_utterance
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeechRecognitionResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeechRecognitionResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeechRecognitionResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class EndOfUtteranceEnum(str, Enum):
        """
        If the `split_transcript_at_phrase_end` parameter is `true`, describes the reason
        for the split:
        * `end_of_data` - The end of the input audio stream.
        * `full_stop` - A full semantic stop, such as for the conclusion of a grammatical
        sentence. The insertion of splits is influenced by the base language model and
        biased by custom language models and grammars.
        * `reset` - The amount of audio that is currently being processed exceeds the
        two-minute maximum. The service splits the transcript to avoid excessive memory
        use.
        * `silence` - A pause or silence that is at least as long as the pause interval.
        """

        END_OF_DATA = 'end_of_data'
        FULL_STOP = 'full_stop'
        RESET = 'reset'
        SILENCE = 'silence'


class SpeechRecognitionResults:
    """
    The complete results for a speech recognition request.

    :param List[SpeechRecognitionResult] results: (optional) An array of
          `SpeechRecognitionResult` objects that can include interim and final results
          (interim results are returned only if supported by the method). Final results
          are guaranteed not to change; interim results might be replaced by further
          interim results and eventually final results.
          For the HTTP interfaces, all results arrive at the same time. For the WebSocket
          interface, results can be sent as multiple separate responses. The service
          periodically sends updates to the results list. The `result_index` is
          incremented to the lowest index in the array that has changed for new results.
          For more information, see [Understanding speech recognition
          results](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-basic-response).
    :param int result_index: (optional) An index that indicates a change point in
          the `results` array. The service increments the index for additional results
          that it sends for new audio for the same request. All results with the same
          index are delivered at the same time. The same index can include multiple final
          results that are delivered with the same response.
    :param List[SpeakerLabelsResult] speaker_labels: (optional) An array of
          `SpeakerLabelsResult` objects that identifies which words were spoken by which
          speakers in a multi-person exchange. The array is returned only if the
          `speaker_labels` parameter is `true`. When interim results are also requested
          for methods that support them, it is possible for a `SpeechRecognitionResults`
          object to include only the `speaker_labels` field.
    :param ProcessingMetrics processing_metrics: (optional) If processing metrics
          are requested, information about the service's processing of the input audio.
          Processing metrics are not available with the synchronous [Recognize
          audio](#recognize) method.
    :param AudioMetrics audio_metrics: (optional) If audio metrics are requested,
          information about the signal characteristics of the input audio.
    :param List[str] warnings: (optional) An array of warning messages associated
          with the request:
          * Warnings for invalid parameters or fields can include a descriptive message
          and a list of invalid argument strings, for example, `"Unknown arguments:"` or
          `"Unknown url query arguments:"` followed by a list of the form
          `"{invalid_arg_1}, {invalid_arg_2}."` (If you use the `character_insertion_bias`
          parameter with a previous-generation model, the warning message refers to the
          parameter as `lambdaBias`.)
          * The following warning is returned if the request passes a custom model that is
          based on an older version of a base model for which an updated version is
          available: `"Using previous version of base model, because your custom model has
          been built with it. Please note that this version will be supported only for a
          limited time. Consider updating your custom model to the new base model. If you
          do not do that you will be automatically switched to base model when you used
          the non-updated custom model."`
          In both cases, the request succeeds despite the warnings.
    """

    def __init__(
        self,
        *,
        results: Optional[List['SpeechRecognitionResult']] = None,
        result_index: Optional[int] = None,
        speaker_labels: Optional[List['SpeakerLabelsResult']] = None,
        processing_metrics: Optional['ProcessingMetrics'] = None,
        audio_metrics: Optional['AudioMetrics'] = None,
        warnings: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a SpeechRecognitionResults object.

        :param List[SpeechRecognitionResult] results: (optional) An array of
               `SpeechRecognitionResult` objects that can include interim and final
               results (interim results are returned only if supported by the method).
               Final results are guaranteed not to change; interim results might be
               replaced by further interim results and eventually final results.
               For the HTTP interfaces, all results arrive at the same time. For the
               WebSocket interface, results can be sent as multiple separate responses.
               The service periodically sends updates to the results list. The
               `result_index` is incremented to the lowest index in the array that has
               changed for new results.
               For more information, see [Understanding speech recognition
               results](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-basic-response).
        :param int result_index: (optional) An index that indicates a change point
               in the `results` array. The service increments the index for additional
               results that it sends for new audio for the same request. All results with
               the same index are delivered at the same time. The same index can include
               multiple final results that are delivered with the same response.
        :param List[SpeakerLabelsResult] speaker_labels: (optional) An array of
               `SpeakerLabelsResult` objects that identifies which words were spoken by
               which speakers in a multi-person exchange. The array is returned only if
               the `speaker_labels` parameter is `true`. When interim results are also
               requested for methods that support them, it is possible for a
               `SpeechRecognitionResults` object to include only the `speaker_labels`
               field.
        :param ProcessingMetrics processing_metrics: (optional) If processing
               metrics are requested, information about the service's processing of the
               input audio. Processing metrics are not available with the synchronous
               [Recognize audio](#recognize) method.
        :param AudioMetrics audio_metrics: (optional) If audio metrics are
               requested, information about the signal characteristics of the input audio.
        :param List[str] warnings: (optional) An array of warning messages
               associated with the request:
               * Warnings for invalid parameters or fields can include a descriptive
               message and a list of invalid argument strings, for example, `"Unknown
               arguments:"` or `"Unknown url query arguments:"` followed by a list of the
               form `"{invalid_arg_1}, {invalid_arg_2}."` (If you use the
               `character_insertion_bias` parameter with a previous-generation model, the
               warning message refers to the parameter as `lambdaBias`.)
               * The following warning is returned if the request passes a custom model
               that is based on an older version of a base model for which an updated
               version is available: `"Using previous version of base model, because your
               custom model has been built with it. Please note that this version will be
               supported only for a limited time. Consider updating your custom model to
               the new base model. If you do not do that you will be automatically
               switched to base model when you used the non-updated custom model."`
               In both cases, the request succeeds despite the warnings.
        """
        self.results = results
        self.result_index = result_index
        self.speaker_labels = speaker_labels
        self.processing_metrics = processing_metrics
        self.audio_metrics = audio_metrics
        self.warnings = warnings

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeechRecognitionResults':
        """Initialize a SpeechRecognitionResults object from a json dictionary."""
        args = {}
        if (results := _dict.get('results')) is not None:
            args['results'] = [
                SpeechRecognitionResult.from_dict(v) for v in results
            ]
        if (result_index := _dict.get('result_index')) is not None:
            args['result_index'] = result_index
        if (speaker_labels := _dict.get('speaker_labels')) is not None:
            args['speaker_labels'] = [
                SpeakerLabelsResult.from_dict(v) for v in speaker_labels
            ]
        if (processing_metrics := _dict.get('processing_metrics')) is not None:
            args['processing_metrics'] = ProcessingMetrics.from_dict(
                processing_metrics)
        if (audio_metrics := _dict.get('audio_metrics')) is not None:
            args['audio_metrics'] = AudioMetrics.from_dict(audio_metrics)
        if (warnings := _dict.get('warnings')) is not None:
            args['warnings'] = warnings
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeechRecognitionResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'results') and self.results is not None:
            results_list = []
            for v in self.results:
                if isinstance(v, dict):
                    results_list.append(v)
                else:
                    results_list.append(v.to_dict())
            _dict['results'] = results_list
        if hasattr(self, 'result_index') and self.result_index is not None:
            _dict['result_index'] = self.result_index
        if hasattr(self, 'speaker_labels') and self.speaker_labels is not None:
            speaker_labels_list = []
            for v in self.speaker_labels:
                if isinstance(v, dict):
                    speaker_labels_list.append(v)
                else:
                    speaker_labels_list.append(v.to_dict())
            _dict['speaker_labels'] = speaker_labels_list
        if hasattr(
                self,
                'processing_metrics') and self.processing_metrics is not None:
            if isinstance(self.processing_metrics, dict):
                _dict['processing_metrics'] = self.processing_metrics
            else:
                _dict['processing_metrics'] = self.processing_metrics.to_dict()
        if hasattr(self, 'audio_metrics') and self.audio_metrics is not None:
            if isinstance(self.audio_metrics, dict):
                _dict['audio_metrics'] = self.audio_metrics
            else:
                _dict['audio_metrics'] = self.audio_metrics.to_dict()
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = self.warnings
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeechRecognitionResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeechRecognitionResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeechRecognitionResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SupportedFeatures:
    """
    Indicates whether select service features are supported with the model.

    :param bool custom_language_model: Indicates whether the customization interface
          can be used to create a custom language model based on the language model.
    :param bool custom_acoustic_model: Indicates whether the customization interface
          can be used to create a custom acoustic model based on the language model.
    :param bool speaker_labels: Indicates whether the `speaker_labels` parameter can
          be used with the language model.
          **Note:** The field returns `true` for all models. However, speaker labels are
          supported for use only with the following languages and models:
          * _For previous-generation models,_ the parameter can be used with Australian
          English, US English, German, Japanese, Korean, and Spanish (both broadband and
          narrowband models) and UK English (narrowband model) transcription only.
          * _For next-generation models,_ the parameter can be used with Czech, English
          (Australian, Indian, UK, and US), German, Japanese, Korean, and Spanish
          transcription only.
          Speaker labels are not supported for use with any other languages or models.
    :param bool low_latency: (optional) Indicates whether the `low_latency`
          parameter can be used with a next-generation language model. The field is
          returned only for next-generation models. Previous-generation models do not
          support the `low_latency` parameter.
    """

    def __init__(
        self,
        custom_language_model: bool,
        custom_acoustic_model: bool,
        speaker_labels: bool,
        *,
        low_latency: Optional[bool] = None,
    ) -> None:
        """
        Initialize a SupportedFeatures object.

        :param bool custom_language_model: Indicates whether the customization
               interface can be used to create a custom language model based on the
               language model.
        :param bool custom_acoustic_model: Indicates whether the customization
               interface can be used to create a custom acoustic model based on the
               language model.
        :param bool speaker_labels: Indicates whether the `speaker_labels`
               parameter can be used with the language model.
               **Note:** The field returns `true` for all models. However, speaker labels
               are supported for use only with the following languages and models:
               * _For previous-generation models,_ the parameter can be used with
               Australian English, US English, German, Japanese, Korean, and Spanish (both
               broadband and narrowband models) and UK English (narrowband model)
               transcription only.
               * _For next-generation models,_ the parameter can be used with Czech,
               English (Australian, Indian, UK, and US), German, Japanese, Korean, and
               Spanish transcription only.
               Speaker labels are not supported for use with any other languages or
               models.
        :param bool low_latency: (optional) Indicates whether the `low_latency`
               parameter can be used with a next-generation language model. The field is
               returned only for next-generation models. Previous-generation models do not
               support the `low_latency` parameter.
        """
        self.custom_language_model = custom_language_model
        self.custom_acoustic_model = custom_acoustic_model
        self.speaker_labels = speaker_labels
        self.low_latency = low_latency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SupportedFeatures':
        """Initialize a SupportedFeatures object from a json dictionary."""
        args = {}
        if (custom_language_model :=
                _dict.get('custom_language_model')) is not None:
            args['custom_language_model'] = custom_language_model
        else:
            raise ValueError(
                'Required property \'custom_language_model\' not present in SupportedFeatures JSON'
            )
        if (custom_acoustic_model :=
                _dict.get('custom_acoustic_model')) is not None:
            args['custom_acoustic_model'] = custom_acoustic_model
        else:
            raise ValueError(
                'Required property \'custom_acoustic_model\' not present in SupportedFeatures JSON'
            )
        if (speaker_labels := _dict.get('speaker_labels')) is not None:
            args['speaker_labels'] = speaker_labels
        else:
            raise ValueError(
                'Required property \'speaker_labels\' not present in SupportedFeatures JSON'
            )
        if (low_latency := _dict.get('low_latency')) is not None:
            args['low_latency'] = low_latency
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SupportedFeatures object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_language_model'
                  ) and self.custom_language_model is not None:
            _dict['custom_language_model'] = self.custom_language_model
        if hasattr(self, 'custom_acoustic_model'
                  ) and self.custom_acoustic_model is not None:
            _dict['custom_acoustic_model'] = self.custom_acoustic_model
        if hasattr(self, 'speaker_labels') and self.speaker_labels is not None:
            _dict['speaker_labels'] = self.speaker_labels
        if hasattr(self, 'low_latency') and self.low_latency is not None:
            _dict['low_latency'] = self.low_latency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SupportedFeatures object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SupportedFeatures') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SupportedFeatures') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingResponse:
    """
    The response from training of a custom language or custom acoustic model.

    :param List[TrainingWarning] warnings: (optional) An array of `TrainingWarning`
          objects that lists any invalid resources contained in the custom model. For
          custom language models, invalid resources are grouped and identified by type of
          resource. The method can return warnings only if the `strict` parameter is set
          to `false`.
    """

    def __init__(
        self,
        *,
        warnings: Optional[List['TrainingWarning']] = None,
    ) -> None:
        """
        Initialize a TrainingResponse object.

        :param List[TrainingWarning] warnings: (optional) An array of
               `TrainingWarning` objects that lists any invalid resources contained in the
               custom model. For custom language models, invalid resources are grouped and
               identified by type of resource. The method can return warnings only if the
               `strict` parameter is set to `false`.
        """
        self.warnings = warnings

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingResponse':
        """Initialize a TrainingResponse object from a json dictionary."""
        args = {}
        if (warnings := _dict.get('warnings')) is not None:
            args['warnings'] = [TrainingWarning.from_dict(v) for v in warnings]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'warnings') and self.warnings is not None:
            warnings_list = []
            for v in self.warnings:
                if isinstance(v, dict):
                    warnings_list.append(v)
                else:
                    warnings_list.append(v.to_dict())
            _dict['warnings'] = warnings_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrainingResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingWarning:
    """
    A warning from training of a custom language or custom acoustic model.

    :param str code: An identifier for the type of invalid resources listed in the
          `description` field.
    :param str message: A warning message that lists the invalid resources that are
          excluded from the custom model's training. The message has the following format:
          `Analysis of the following {resource_type} has not completed successfully:
          [{resource_names}]. They will be excluded from custom {model_type} model
          training.`.
    """

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:
        """
        Initialize a TrainingWarning object.

        :param str code: An identifier for the type of invalid resources listed in
               the `description` field.
        :param str message: A warning message that lists the invalid resources that
               are excluded from the custom model's training. The message has the
               following format: `Analysis of the following {resource_type} has not
               completed successfully: [{resource_names}]. They will be excluded from
               custom {model_type} model training.`.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingWarning':
        """Initialize a TrainingWarning object from a json dictionary."""
        args = {}
        if (code := _dict.get('code')) is not None:
            args['code'] = code
        else:
            raise ValueError(
                'Required property \'code\' not present in TrainingWarning JSON'
            )
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        else:
            raise ValueError(
                'Required property \'message\' not present in TrainingWarning JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingWarning object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingWarning object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrainingWarning') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingWarning') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CodeEnum(str, Enum):
        """
        An identifier for the type of invalid resources listed in the `description` field.
        """

        INVALID_AUDIO_FILES = 'invalid_audio_files'
        INVALID_CORPUS_FILES = 'invalid_corpus_files'
        INVALID_GRAMMAR_FILES = 'invalid_grammar_files'
        INVALID_WORDS = 'invalid_words'


class Word:
    """
    Information about a word from a custom language model.

    :param str word: A word from the custom model's words resource. The spelling of
          the word is used to train the model.
    :param List[str] mapping_only: (optional) (Optional) Parameter for custom words.
          You can use the 'mapping_only' key in custom words as a form of post processing.
          A boolean value that indicates whether the added word should be used to
          fine-tune the mode for selected next-gen models. This field appears in the
          response body only when it's 'For a custom model that is based on a
          previous-generation model', the mapping_only field is populated with the value
          set by the user, but would not be used.
    :param List[str] sounds_like: An array of as many as five pronunciations for the
          word.
          * _For a custom model that is based on a previous-generation model_, in addition
          to sounds-like pronunciations that were added by a user, the array can include a
          sounds-like pronunciation that is automatically generated by the service if none
          is provided when the word is added to the custom model.
          * _For a custom model that is based on a next-generation model_, the array can
          include only sounds-like pronunciations that were added by a user.
    :param str display_as: The spelling of the word that the service uses to display
          the word in a transcript.
          * _For a custom model that is based on a previous-generation model_, the field
          can contain an empty string if no display-as value is provided for a word that
          exists in the service's base vocabulary. In this case, the word is displayed as
          it is spelled.
          * _For a custom model that is based on a next-generation model_, the service
          uses the spelling of the word as the value of the display-as field when the word
          is added to the model.
    :param int count: _For a custom model that is based on a previous-generation
          model_, a sum of the number of times the word is found across all corpora and
          grammars. For example, if the word occurs five times in one corpus and seven
          times in another, its count is `12`. If you add a custom word to a model before
          it is added by any corpora or grammars, the count begins at `1`; if the word is
          added from a corpus or grammar first and later modified, the count reflects only
          the number of times it is found in corpora and grammars.
          _For a custom model that is based on a next-generation model_, the `count` field
          for any word is always `1`.
    :param List[str] source: An array of sources that describes how the word was
          added to the custom model's words resource.
          * _For a custom model that is based on previous-generation model,_ the field
          includes the name of each corpus and grammar from which the service extracted
          the word. For OOV that are added by multiple corpora or grammars, the names of
          all corpora and grammars are listed. If you modified or added the word directly,
          the field includes the string `user`.
          * _For a custom model that is based on a next-generation model,_ this field
          shows only `user` for custom words that were added directly to the custom model.
          Words from corpora and grammars are not added to the words resource for custom
          models that are based on next-generation models.
    :param List[WordError] error: (optional) If the service discovered one or more
          problems that you need to correct for the word's definition, an array that
          describes each of the errors.
    """

    def __init__(
        self,
        word: str,
        sounds_like: List[str],
        display_as: str,
        count: int,
        source: List[str],
        *,
        mapping_only: Optional[List[str]] = None,
        error: Optional[List['WordError']] = None,
    ) -> None:
        """
        Initialize a Word object.

        :param str word: A word from the custom model's words resource. The
               spelling of the word is used to train the model.
        :param List[str] sounds_like: An array of as many as five pronunciations
               for the word.
               * _For a custom model that is based on a previous-generation model_, in
               addition to sounds-like pronunciations that were added by a user, the array
               can include a sounds-like pronunciation that is automatically generated by
               the service if none is provided when the word is added to the custom model.
               * _For a custom model that is based on a next-generation model_, the array
               can include only sounds-like pronunciations that were added by a user.
        :param str display_as: The spelling of the word that the service uses to
               display the word in a transcript.
               * _For a custom model that is based on a previous-generation model_, the
               field can contain an empty string if no display-as value is provided for a
               word that exists in the service's base vocabulary. In this case, the word
               is displayed as it is spelled.
               * _For a custom model that is based on a next-generation model_, the
               service uses the spelling of the word as the value of the display-as field
               when the word is added to the model.
        :param int count: _For a custom model that is based on a
               previous-generation model_, a sum of the number of times the word is found
               across all corpora and grammars. For example, if the word occurs five times
               in one corpus and seven times in another, its count is `12`. If you add a
               custom word to a model before it is added by any corpora or grammars, the
               count begins at `1`; if the word is added from a corpus or grammar first
               and later modified, the count reflects only the number of times it is found
               in corpora and grammars.
               _For a custom model that is based on a next-generation model_, the `count`
               field for any word is always `1`.
        :param List[str] source: An array of sources that describes how the word
               was added to the custom model's words resource.
               * _For a custom model that is based on previous-generation model,_ the
               field includes the name of each corpus and grammar from which the service
               extracted the word. For OOV that are added by multiple corpora or grammars,
               the names of all corpora and grammars are listed. If you modified or added
               the word directly, the field includes the string `user`.
               * _For a custom model that is based on a next-generation model,_ this field
               shows only `user` for custom words that were added directly to the custom
               model. Words from corpora and grammars are not added to the words resource
               for custom models that are based on next-generation models.
        :param List[str] mapping_only: (optional) (Optional) Parameter for custom
               words. You can use the 'mapping_only' key in custom words as a form of post
               processing. A boolean value that indicates whether the added word should be
               used to fine-tune the mode for selected next-gen models. This field appears
               in the response body only when it's 'For a custom model that is based on a
               previous-generation model', the mapping_only field is populated with the
               value set by the user, but would not be used.
        :param List[WordError] error: (optional) If the service discovered one or
               more problems that you need to correct for the word's definition, an array
               that describes each of the errors.
        """
        self.word = word
        self.mapping_only = mapping_only
        self.sounds_like = sounds_like
        self.display_as = display_as
        self.count = count
        self.source = source
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Word':
        """Initialize a Word object from a json dictionary."""
        args = {}
        if (word := _dict.get('word')) is not None:
            args['word'] = word
        else:
            raise ValueError(
                'Required property \'word\' not present in Word JSON')
        if (mapping_only := _dict.get('mapping_only')) is not None:
            args['mapping_only'] = mapping_only
        if (sounds_like := _dict.get('sounds_like')) is not None:
            args['sounds_like'] = sounds_like
        else:
            raise ValueError(
                'Required property \'sounds_like\' not present in Word JSON')
        if (display_as := _dict.get('display_as')) is not None:
            args['display_as'] = display_as
        else:
            raise ValueError(
                'Required property \'display_as\' not present in Word JSON')
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        else:
            raise ValueError(
                'Required property \'count\' not present in Word JSON')
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in Word JSON')
        if (error := _dict.get('error')) is not None:
            args['error'] = [WordError.from_dict(v) for v in error]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Word object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word
        if hasattr(self, 'mapping_only') and self.mapping_only is not None:
            _dict['mapping_only'] = self.mapping_only
        if hasattr(self, 'sounds_like') and self.sounds_like is not None:
            _dict['sounds_like'] = self.sounds_like
        if hasattr(self, 'display_as') and self.display_as is not None:
            _dict['display_as'] = self.display_as
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'error') and self.error is not None:
            error_list = []
            for v in self.error:
                if isinstance(v, dict):
                    error_list.append(v)
                else:
                    error_list.append(v.to_dict())
            _dict['error'] = error_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Word object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Word') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Word') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordAlternativeResult:
    """
    An alternative hypothesis for a word from speech recognition results.

    :param float confidence: A confidence score for the word alternative hypothesis
          in the range of 0.0 to 1.0.
    :param str word: An alternative hypothesis for a word from the input audio.
    """

    def __init__(
        self,
        confidence: float,
        word: str,
    ) -> None:
        """
        Initialize a WordAlternativeResult object.

        :param float confidence: A confidence score for the word alternative
               hypothesis in the range of 0.0 to 1.0.
        :param str word: An alternative hypothesis for a word from the input audio.
        """
        self.confidence = confidence
        self.word = word

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WordAlternativeResult':
        """Initialize a WordAlternativeResult object from a json dictionary."""
        args = {}
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        else:
            raise ValueError(
                'Required property \'confidence\' not present in WordAlternativeResult JSON'
            )
        if (word := _dict.get('word')) is not None:
            args['word'] = word
        else:
            raise ValueError(
                'Required property \'word\' not present in WordAlternativeResult JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordAlternativeResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WordAlternativeResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WordAlternativeResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WordAlternativeResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordAlternativeResults:
    """
    Information about alternative hypotheses for words from speech recognition results.

    :param float start_time: The start time in seconds of the word from the input
          audio that corresponds to the word alternatives.
    :param float end_time: The end time in seconds of the word from the input audio
          that corresponds to the word alternatives.
    :param List[WordAlternativeResult] alternatives: An array of alternative
          hypotheses for a word from the input audio.
    """

    def __init__(
        self,
        start_time: float,
        end_time: float,
        alternatives: List['WordAlternativeResult'],
    ) -> None:
        """
        Initialize a WordAlternativeResults object.

        :param float start_time: The start time in seconds of the word from the
               input audio that corresponds to the word alternatives.
        :param float end_time: The end time in seconds of the word from the input
               audio that corresponds to the word alternatives.
        :param List[WordAlternativeResult] alternatives: An array of alternative
               hypotheses for a word from the input audio.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.alternatives = alternatives

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WordAlternativeResults':
        """Initialize a WordAlternativeResults object from a json dictionary."""
        args = {}
        if (start_time := _dict.get('start_time')) is not None:
            args['start_time'] = start_time
        else:
            raise ValueError(
                'Required property \'start_time\' not present in WordAlternativeResults JSON'
            )
        if (end_time := _dict.get('end_time')) is not None:
            args['end_time'] = end_time
        else:
            raise ValueError(
                'Required property \'end_time\' not present in WordAlternativeResults JSON'
            )
        if (alternatives := _dict.get('alternatives')) is not None:
            args['alternatives'] = [
                WordAlternativeResult.from_dict(v) for v in alternatives
            ]
        else:
            raise ValueError(
                'Required property \'alternatives\' not present in WordAlternativeResults JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordAlternativeResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'alternatives') and self.alternatives is not None:
            alternatives_list = []
            for v in self.alternatives:
                if isinstance(v, dict):
                    alternatives_list.append(v)
                else:
                    alternatives_list.append(v.to_dict())
            _dict['alternatives'] = alternatives_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WordAlternativeResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WordAlternativeResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WordAlternativeResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WordError:
    """
    An error associated with a word from a custom language model.

    :param str element: A key-value pair that describes an error associated with the
          definition of a word in the words resource. The pair has the format `"element":
          "message"`, where `element` is the aspect of the definition that caused the
          problem and `message` describes the problem. The following example describes a
          problem with one of the word's sounds-like definitions: `"{sounds_like_string}":
          "Numbers are not allowed in sounds-like. You can try for example
          '{suggested_string}'."`.
    """

    def __init__(
        self,
        element: str,
    ) -> None:
        """
        Initialize a WordError object.

        :param str element: A key-value pair that describes an error associated
               with the definition of a word in the words resource. The pair has the
               format `"element": "message"`, where `element` is the aspect of the
               definition that caused the problem and `message` describes the problem. The
               following example describes a problem with one of the word's sounds-like
               definitions: `"{sounds_like_string}": "Numbers are not allowed in
               sounds-like. You can try for example '{suggested_string}'."`.
        """
        self.element = element

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WordError':
        """Initialize a WordError object from a json dictionary."""
        args = {}
        if (element := _dict.get('element')) is not None:
            args['element'] = element
        else:
            raise ValueError(
                'Required property \'element\' not present in WordError JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WordError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'element') and self.element is not None:
            _dict['element'] = self.element
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WordError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WordError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WordError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Words:
    """
    Information about the words from a custom language model.

    :param List[Word] words: An array of `Word` objects that provides information
          about each word in the custom model's words resource. The array is empty if the
          custom model has no words.
    """

    def __init__(
        self,
        words: List['Word'],
    ) -> None:
        """
        Initialize a Words object.

        :param List[Word] words: An array of `Word` objects that provides
               information about each word in the custom model's words resource. The array
               is empty if the custom model has no words.
        """
        self.words = words

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Words':
        """Initialize a Words object from a json dictionary."""
        args = {}
        if (words := _dict.get('words')) is not None:
            args['words'] = [Word.from_dict(v) for v in words]
        else:
            raise ValueError(
                'Required property \'words\' not present in Words JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Words object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'words') and self.words is not None:
            words_list = []
            for v in self.words:
                if isinstance(v, dict):
                    words_list.append(v)
                else:
                    words_list.append(v.to_dict())
            _dict['words'] = words_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Words object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Words') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Words') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
