# coding: utf-8

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
                                  grammar_name=None,
                                  redaction=None,
                                  processing_metrics=None,
                                  processing_metrics_interval=None,
                                  audio_metrics=None,
                                  end_of_phrase_silence_time=None,
                                  split_transcript_at_phrase_end=None,
                                  speech_detector_sensitivity=None,
                                  background_audio_suppression=None,
                                  low_latency=None,
                                  character_insertion_bias=None,
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
        :param str model: (optional) The identifier of the model that is to be used
               for the recognition request. (**Note:** The model `ar-AR_BroadbandModel` is
               deprecated; use `ar-MS_BroadbandModel` instead.) See [Languages and
               models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models)
               and [Next-generation languages and
               models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng).
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
               weight was specified for the custom model when it was trained, the default
               value is 0.3. A customization weight that you specify overrides a weight
               that was specified when the custom model was trained.
               The default value yields the best performance in general. Assign a higher
               value if your audio makes frequent use of OOV words from the custom model.
               Use caution when setting the weight: a higher value can improve the
               accuracy of phrases from the custom model's domain, but it can negatively
               affect performance on non-domain phrases.
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
               `false` to return results with no censoring. Applies to US English and
               Japanese transcription only. See [Profanity
               filtering](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#profanity-filtering).
        :param bool smart_formatting: (optional) If `true`, the service converts
               dates, times, series of digits and numbers, phone numbers, currency values,
               and internet addresses into more readable, conventional representations in
               the final transcript of a recognition request. For US English, the service
               also converts certain keyword strings to punctuation symbols. By default,
               the service performs no smart formatting.
               **Note:** Applies to US English, Japanese, and Spanish transcription only.
               See [Smart
               formatting](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#smart-formatting).
        :param bool speaker_labels: (optional) If `true`, the response includes
               labels that identify which words were spoken by which participants in a
               multi-person exchange. By default, the service returns no speaker labels.
               Setting `speaker_labels` to `true` forces the `timestamps` parameter to be
               `true`, regardless of whether you specify `false` for the parameter.
               * For previous-generation models, can be used for US English, Australian
               English, German, Japanese, Korean, and Spanish (both broadband and
               narrowband models) and UK English (narrowband model) transcription only.
               * For next-generation models, can be used for English (Australian, UK, and
               US), German, and Spanish transcription only.
               Restrictions and limitations apply to the use of speaker labels for both
               types of models. See [Speaker
               labels](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-speaker-labels).
        :param str http_proxy_host: http proxy host name.
        :param str http_proxy_port: http proxy port. If not set, set to 80.
        :param str grammar_name: (optional) The name of a grammar that is to be
               used with the recognition request. If you specify a grammar, you must also
               use the `language_customization_id` parameter to specify the name of the
               custom language model for which the grammar is defined. The service
               recognizes only strings that are recognized by the specified grammar; it
               does not recognize other custom words from the model's words resource. See
               [Using a grammar for speech
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
               **Note:** Applies to US English, Japanese, and Korean transcription only.
               See [Numeric
               redaction](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-formatting#numeric-redaction).
        :param bool audio_metrics: (optional) If `true`, requests detailed
               information about the signal characteristics of the input audio. The
               service returns audio metrics with the final transcription results. By
               default, the service returns no audio metrics.
               See [Audio
               metrics](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-metrics#audio-metrics).
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
               time](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#silence-time).
        :param bool split_transcript_at_phrase_end: (optional) If `true`, directs
               the service to split the transcript into multiple final results based on
               semantic features of the input, for example, at the conclusion of
               meaningful phrases such as sentences. The service bases its understanding
               of semantic features on the base language model that you use with a
               request. Custom language models and grammars can also influence how and
               where the service splits a transcript. By default, the service splits
               transcripts based solely on the pause interval.
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
               The values increase on a monotonic curve. See [Speech detector
               sensitivity](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-parameters-sensitivity).
        :param float background_audio_suppression: (optional) The level to which
               the service is to suppress background audio based on its volume to prevent
               it from being transcribed as speech. Use the parameter to suppress side
               conversations or background noise.
               Specify a value in the range of 0.0 to 1.0:
               * 0.0 (the default) provides no suppression (background audio suppression
               is disabled).
               * 0.5 provides a reasonable level of audio suppression for general usage.
               * 1.0 suppresses all audio (no audio is transcribed).
               The values increase on a monotonic curve. See [Background audio
               suppression](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-detection#detection-parameters-suppression).
        :param bool low_latency: (optional) If `true` for next-generation
               `Multimedia` and `Telephony` models that support low latency, directs the
               service to produce results even more quickly than it usually does.
               Next-generation models produce transcription results faster than
               previous-generation models. The `low_latency` parameter causes the models
               to produce results even more quickly, though the results might be less
               accurate when the parameter is used.
               **Note:** The parameter is beta functionality. It is not available for
               previous-generation `Broadband` and `Narrowband` models. It is available
               only for some next-generation models.
               * For a list of next-generation models that support low latency, see
               [Supported language
               models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-ng#models-ng-supported)
               for next-generation models.
               * For more information about the `low_latency` parameter, see [Low
               latency](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-interim#low-latency).
        :param float character_insertion_bias: (optional) For next-generation
               `Multimedia` and `Telephony` models, an indication of whether the service
               is biased to recognize shorter or longer strings of characters when
               developing transcription hypotheses. By default, the service is optimized
               for each individual model to balance its recognition of strings of
               different lengths. The model-specific bias is equivalent to 0.0.
               The value that you specify represents a change from a model's default bias.
               The allowable range of values is -1.0 to 1.0.
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
               The parameter is not available for previous-generation `Broadband` and
               `Narrowband` models.
               See [Character insertion
               bias](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-parsing#insertion-bias).
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
            'background_audio_suppression': background_audio_suppression,
            'low_latency': low_latency,
            'character_insertion_bias': character_insertion_bias
        }
        options = {k: v for k, v in options.items() if v is not None}
        request['options'] = options

        RecognizeListener(audio, request.get('options'), recognize_callback,
                          request.get('url'), request.get('headers'),
                          http_proxy_host, http_proxy_port,
                          self.disable_ssl_verification)
