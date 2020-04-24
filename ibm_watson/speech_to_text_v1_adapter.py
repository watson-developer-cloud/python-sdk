# coding: utf-8

# (C) Copyright IBM Corp. 2018, 2020.
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

from ibm_watson.websocket import RecognizeCallback, RecognizeListener, AudioSource
from .speech_to_text_v1 import SpeechToTextV1
from urllib.parse import urlencode

BEARER = 'Bearer'


class SpeechToTextV1Adapter(SpeechToTextV1):

    def recognize_using_websocket(self,
                                  audio,
                                  content_type,
                                  recognize_callback,
                                  model=None,
                                  language_customization_id=None,
                                  acoustic_customization_id=None,
                                  customization_weight=None,
                                  base_model_version=None,
                                  inactivity_timeout=None,
                                  interim_results=None,
                                  keywords=None,
                                  keywords_threshold=None,
                                  max_alternatives=None,
                                  word_alternatives_threshold=None,
                                  word_confidence=None,
                                  timestamps=None,
                                  profanity_filter=None,
                                  smart_formatting=None,
                                  speaker_labels=None,
                                  http_proxy_host=None,
                                  http_proxy_port=None,
                                  customization_id=None,
                                  grammar_name=None,
                                  redaction=None,
                                  processing_metrics=None,
                                  processing_metrics_interval=None,
                                  audio_metrics=None,
                                  end_of_phrase_silence_time=None,
                                  split_transcript_at_phrase_end=None,
                                  speech_detector_sensitivity=None,
                                  background_audio_suppression=None,
                                  **kwargs):
        """
        Sends audio for speech recognition using web sockets.

        :param AudioSource audio: The audio to transcribe in the format specified by the
        `Content-Type` header.
        :param str content_type: The type of the input: audio/basic, audio/flac,
        audio/l16, audio/mp3, audio/mpeg, audio/mulaw, audio/ogg, audio/ogg;codecs=opus,
        audio/ogg;codecs=vorbis, audio/wav, audio/webm, audio/webm;codecs=opus, or
        audio/webm;codecs=vorbis.
        :param RecognizeCallback recognize_callback: The callback method for the websocket.
        :param str model: The identifier of the model that is to be used for the
        recognition request or, for the **Create a session** method, with the new session.
        :param str language_customization_id: The customization ID (GUID) of a custom
        language model that is to be used with the recognition request. The base model of
        the specified custom language model must match the model specified with the
        `model` parameter. You must make the request with service credentials created for
        the instance of the service that owns the custom model. By default, no custom
        language model is used. See [Custom
        models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#custom).
        **Note:** Use this parameter instead of the deprecated `customization_id`
        parameter.
        :param str acoustic_customization_id: The customization ID (GUID) of a custom
        acoustic model that is to be used with the recognition request or, for the
        **Create a session** method, with the new session. The base model of the specified
        custom acoustic model must match the model specified with the `model` parameter.
        You must make the request with service credentials created for the instance of the
        service that owns the custom model. By default, no custom acoustic model is used.
        :param float customization_weight: If you specify the customization ID (GUID) of a
        custom language model with the recognition request or, for sessions, with the
        **Create a session** method, the customization weight tells the service how much
        weight to give to words from the custom language model compared to those from the
        base model for the current request.
        Specify a value between 0.0 and 1.0. Unless a different customization weight was
        specified for the custom model when it was trained, the default value is 0.3. A
        customization weight that you specify overrides a weight that was specified when
        the custom model was trained.
        The default value yields the best performance in general. Assign a higher value if
        your audio makes frequent use of OOV words from the custom model. Use caution when
        setting the weight: a higher value can improve the accuracy of phrases from the
        custom model's domain, but it can negatively affect performance on non-domain
        phrases.
        :param str base_model_version: The version of the specified base model that is to
        be used with recognition request or, for the **Create a session** method, with the
        new session. Multiple versions of a base model can exist when a model is updated
        for internal improvements. The parameter is intended primarily for use with custom
        models that have been upgraded for a new base model. The default value depends on
        whether the parameter is used with or without a custom model. For more
        information, see [Base model
        version](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#version).
        :param int inactivity_timeout: The time in seconds after which, if only silence
        (no speech) is detected in submitted audio, the connection is closed with a 400
        error. Useful for stopping audio submission from a live microphone when a user
        simply walks away. Use `-1` for infinity.
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
        spotting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-output#keyword_spotting).
        :param float keywords_threshold: A confidence value that is the lower bound for
        spotting a keyword. A word is considered to match a keyword if its confidence is
        greater than or equal to the threshold. Specify a probability between 0 and 1
        inclusive. No keyword spotting is performed if you omit the parameter. If you
        specify a threshold, you must also specify one or more keywords.
        :param int max_alternatives: The maximum number of alternative transcripts to be
        returned. By default, a single transcription is returned.
        :param float word_alternatives_threshold: A confidence value that is the lower
        bound for identifying a hypothesis as a possible word alternative (also known as
        \"Confusion Networks\"). An alternative word is considered if its confidence is
        greater than or equal to the threshold. Specify a probability between 0 and 1
        inclusive. No alternative words are computed if you omit the parameter.
        :param bool word_confidence: If `true`, a confidence measure in the range of 0 to
        1 is returned for each word. By default, no word confidence measures are returned.
        :param bool timestamps: If `true`, time alignment is returned for each word. By
        default, no timestamps are returned.
        :param bool profanity_filter: If `true` (the default), filters profanity from all
        output except for keyword results by replacing inappropriate words with a series
        of asterisks. Set the parameter to `false` to return results with no censoring.
        Applies to US English transcription only.
        :param bool smart_formatting: If `true`, converts dates, times, series of digits
        and numbers, phone numbers, currency values, and internet addresses into more
        readable, conventional representations in the final transcript of a recognition
        request. For US English, also converts certain keyword strings to punctuation
        symbols. By default, no smart formatting is performed. Applies to US English and
        Spanish transcription only.
        :param bool speaker_labels: (optional) If `true`, the response includes
        labels that identify which words were spoken by which participants in a
        multi-person exchange. By default, the service returns no speaker labels.
        Setting `speaker_labels` to `true` forces the `timestamps` parameter to be
        `true`, regardless of whether you specify `false` for the parameter.
        **Note:** Applies to US English, German, Japanese, Korean, and Spanish
        (both broadband and narrowband models) and UK English (narrowband model)
        transcription only. To determine whether a language model supports speaker
        labels, you can also use the **Get a model** method and check that the
        attribute `speaker_labels` is set to `true`.
        See [Speaker
        labels](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-output#speaker_labels).
        :param str http_proxy_host: http proxy host name.
        :param str http_proxy_port: http proxy port. If not set, set to 80.
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
        [Grammars](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-output).
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
        redaction](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-output#redaction).
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
        :param float end_of_phrase_silence_time: (optional) If `true`, specifies
        the duration of the pause interval at which the service splits a transcript
        into multiple final results. If the service detects pauses or extended
        silence before it reaches the end of the audio stream, its response can
        include multiple final results. Silence indicates a point at which the
        speaker pauses between spoken words or phrases.
        Specify a value for the pause interval in the range of 0.0 to 120.0.
        * A value greater than 0 specifies the interval that the service is to use
        for speech recognition.
        * A value of 0 indicates that the service is to use the default interval.
        It is equivalent to omitting the parameter.
        The default pause interval for most languages is 0.8 seconds; the default
        for Chinese is 0.6 seconds.
        See [End of phrase silence
        time](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-output#silence_time).
        :param bool split_transcript_at_phrase_end: (optional) If `true`, directs
        the service to split the transcript into multiple final results based on
        semantic features of the input, for example, at the conclusion of
        meaningful phrases such as sentences. The service bases its understanding
        of semantic features on the base language model that you use with a
        request. Custom language models and grammars can also influence how and
        where the service splits a transcript. By default, the service splits
        transcripts based solely on the pause interval.
        See [Split transcript at phrase
        end](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-output#split_transcript).
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
        The values increase on a monotonic curve. See [Speech Activity
        Detection](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#detection).
        :param float background_audio_suppression: (optional) The level to which
        the service is to suppress background audio based on its volume to prevent
        it from being transcribed as speech. Use the parameter to suppress side
        conversations or background noise.
        Specify a value in the range of 0.0 to 1.0:
        * 0.0 (the default) provides no suppression (background audio suppression
        is disabled).
        * 0.5 provides a reasonable level of audio suppression for general usage.
        * 1.0 suppresses all audio (no audio is transcribed).
        The values increase on a monotonic curve. See [Speech Activity
        Detection](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-input#detection).
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `SpeechRecognitionResults` response.
        :rtype: dict
        """
        if audio is None:
            raise ValueError('audio must be provided')
        if not isinstance(audio, AudioSource):
            raise Exception(
                'audio is not of type AudioSource. Import the class from ibm_watson.websocket'
            )
        if content_type is None:
            raise ValueError('content_type must be provided')
        if recognize_callback is None:
            raise ValueError('recognize_callback must be provided')
        if not isinstance(recognize_callback, RecognizeCallback):
            raise Exception(
                'Callback is not a derived class of RecognizeCallback')

        request = {}

        headers = {}
        if self.default_headers is not None:
            headers = self.default_headers.copy()
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        request['headers'] = headers

        if self.authenticator:
            self.authenticator.authenticate(request)

        url = self.service_url.replace('https:', 'wss:')

        params = {
            'model': model,
            'customization_id': customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'base_model_version': base_model_version,
            'language_customization_id': language_customization_id
        }
        params = {k: v for k, v in params.items() if v is not None}
        url += '/v1/recognize?{0}'.format(urlencode(params))
        request['url'] = url

        options = {
            'customization_weight': customization_weight,
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
            'speaker_labels': speaker_labels,
            'grammar_name': grammar_name,
            'redaction': redaction,
            'processing_metrics': processing_metrics,
            'processing_metrics_interval': processing_metrics_interval,
            'audio_metrics': audio_metrics,
            'end_of_phrase_silence_time': end_of_phrase_silence_time,
            'split_transcript_at_phrase_end': split_transcript_at_phrase_end,
            'speech_detector_sensitivity': speech_detector_sensitivity,
            'background_audio_suppression': background_audio_suppression
        }
        options = {k: v for k, v in options.items() if v is not None}
        request['options'] = options

        RecognizeListener(audio, request.get('options'), recognize_callback,
                          request.get('url'), request.get('headers'),
                          http_proxy_host, http_proxy_port,
                          self.disable_ssl_verification)
