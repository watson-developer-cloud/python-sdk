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

from watson_developer_cloud.websocket import RecognizeCallback, RecognizeListener, AudioSource
from .speech_to_text_v1 import SpeechToTextV1
from .watson_service import _remove_null_values
import base64
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

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
        models](https://console.bluemix.net/docs/services/speech-to-text/input.html#custom).
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
        version](https://console.bluemix.net/docs/services/speech-to-text/input.html#version).
        :param int inactivity_timeout: The time in seconds after which, if only silence
        (no speech) is detected in submitted audio, the connection is closed with a 400
        error. Useful for stopping audio submission from a live microphone when a user
        simply walks away. Use `-1` for infinity.
        :param list[str] keywords: An array of keyword strings to spot in the audio. Each
        keyword string can include one or more tokens. Keywords are spotted only in the
        final hypothesis, not in interim results. If you specify any keywords, you must
        also specify a keywords threshold. You can spot a maximum of 1000 keywords. Omit
        the parameter or specify an empty array if you do not need to spot keywords.
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
        :param bool speaker_labels: If `true`, the response includes labels that identify
        which words were spoken by which participants in a multi-person exchange. By
        default, no speaker labels are returned. Setting `speaker_labels` to `true` forces
        the `timestamps` parameter to be `true`, regardless of whether you specify `false`
        for the parameter.
        To determine whether a language model supports speaker labels, use the **Get
        models** method and check that the attribute `speaker_labels` is set to `true`.
        You can also refer to [Speaker
        labels](https://console.bluemix.net/docs/services/speech-to-text/output.html#speaker_labels).
        :param str http_proxy_host: http proxy host name.
        :param str http_proxy_port: http proxy port. If not set, set to 80.
        :param str customization_id: **Deprecated.** Use the `language_customization_id`
        parameter to specify the customization ID (GUID) of a custom language model that
        is to be used with the recognition request. Do not specify both parameters with a
        request.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `SpeechRecognitionResults` response.
        :rtype: dict
        """
        if audio is None:
            raise ValueError('audio must be provided')
        if not isinstance(audio, AudioSource):
            raise Exception(
                'audio is not of type AudioSource. Import the class from watson_developer_cloud.websocket')
        if content_type is None:
            raise ValueError('content_type must be provided')
        if recognize_callback is None:
            raise ValueError('recognize_callback must be provided')
        if not isinstance(recognize_callback, RecognizeCallback):
            raise Exception(
                'Callback is not a derived class of RecognizeCallback')

        headers = {}
        if self.default_headers is not None:
            headers = self.default_headers.copy()
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        if self.token_manager:
            access_token = self.token_manager.get_token()
            headers['Authorization'] = '{0} {1}'.format(BEARER, access_token)
        else:
            authstring = "{0}:{1}".format(self.username, self.password)
            base64_authorization = base64.b64encode(authstring.encode('utf-8')).decode('utf-8')
            headers['Authorization'] = 'Basic {0}'.format(base64_authorization)

        url = self.url.replace('https:', 'wss:')
        params = {
            'model': model,
            'customization_id': customization_id,
            'acoustic_customization_id': acoustic_customization_id,
            'customization_weight': customization_weight,
            'base_model_version': base_model_version,
            'language_customization_id': language_customization_id,
        }
        params = _remove_null_values(params)
        url += '/v1/recognize?{0}'.format(urlencode(params))

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

        RecognizeListener(audio,
                          options,
                          recognize_callback,
                          url,
                          headers,
                          http_proxy_host,
                          http_proxy_port,
                          self.verify)
