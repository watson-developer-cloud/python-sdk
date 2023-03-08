# coding: utf-8

# (C) Copyright IBM Corp. 2015, 2023.
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

# IBM OpenAPI SDK Code Generator Version: 3.64.1-cee95189-20230124-211647
"""
The IBM Watson&trade; Text to Speech service provides APIs that use IBM's speech-synthesis
capabilities to synthesize text into natural-sounding speech in a variety of languages,
dialects, and voices. The service supports at least one male or female voice, sometimes
both, for each language. The audio is streamed back to the client with minimal delay.
For speech synthesis, the service supports a synchronous HTTP Representational State
Transfer (REST) interface and a WebSocket interface. Both interfaces support plain text
and SSML input. SSML is an XML-based markup language that provides text annotation for
speech-synthesis applications. The WebSocket interface also supports the SSML
<code>&lt;mark&gt;</code> element and word timings.
The service offers a customization interface that you can use to define sounds-like or
phonetic translations for words. A sounds-like translation consists of one or more words
that, when combined, sound like the word. A phonetic translation is based on the SSML
phoneme format for representing a word. You can specify a phonetic translation in standard
International Phonetic Alphabet (IPA) representation or in the proprietary IBM Symbolic
Phonetic Representation (SPR). For phonetic translation, the Arabic, Chinese, Dutch,
Australian English, Korean, and Swedish voices support only IPA, not SPR.
The service also offers a Tune by Example feature that lets you define custom prompts. You
can also define speaker models to improve the quality of your custom prompts. The service
support custom prompts only for US English custom models and voices.
Effective **31 March 2022**, all *neural voices* are deprecated. The deprecated voices
remain available to existing users until 31 March 2023, when they will be removed from the
service and the documentation. *No enhanced neural voices or expressive neural voices are
deprecated.*<br/><br/> For more information, see the [1 March 2023 service
update](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-release-notes#text-to-speech-1march2023)
in the release notes for {{site.data.keyword.texttospeechshort}} for
{{site.data.keyword.cloud_notm}}.{: deprecated}

API Version: 1.0.0
See: https://cloud.ibm.com/docs/text-to-speech
"""

from enum import Enum
from typing import BinaryIO, Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class TextToSpeechV1(BaseService):
    """The Text to Speech V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'text_to_speech'

    def __init__(
        self,
        authenticator: Authenticator = None,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Text to Speech service.

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
    # Voices
    #########################

    def list_voices(self, **kwargs) -> DetailedResponse:
        """
        List voices.

        Lists all voices available for use with the service. The information includes the
        name, language, gender, and other details about the voice. The ordering of the
        list of voices can change from call to call; do not rely on an alphabetized or
        static list of voices. To see information about a specific voice, use the [Get a
        voice](#getvoice).
        **Note:** Effective **31 March 2022**, all *neural voices* are deprecated. The
        deprecated voices remain available to existing users until 31 March 2023, when
        they will be removed from the service and the documentation. *No enhanced neural
        voices or expressive neural voices are deprecated.* For more information, see the
        [1 March 2023 service
        update](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-release-notes#text-to-speech-1march2023)
        in the release notes.
        **See also:** [Listing all
        voices](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices-list#list-all-voices).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Voices` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_voices')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/voices'
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def get_voice(self,
                  voice: str,
                  *,
                  customization_id: str = None,
                  **kwargs) -> DetailedResponse:
        """
        Get a voice.

        Gets information about the specified voice. The information includes the name,
        language, gender, and other details about the voice. Specify a customization ID to
        obtain information for a custom model that is defined for the language of the
        specified voice. To list information about all available voices, use the [List
        voices](#listvoices) method.
        **See also:** [Listing a specific
        voice](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices-list#list-specific-voice).
        **Note:** Effective **31 March 2022**, all *neural voices* are deprecated. The
        deprecated voices remain available to existing users until 31 March 2023, when
        they will be removed from the service and the documentation. *No enhanced neural
        voices or expressive neural voices are deprecated.* For more information, see the
        [1 March 2023 service
        update](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-release-notes#text-to-speech-1march2023)
        in the release notes.

        :param str voice: The voice for which information is to be returned.
        :param str customization_id: (optional) The customization ID (GUID) of a
               custom model for which information is to be returned. You must make the
               request with credentials for the instance of the service that owns the
               custom model. Omit the parameter to see information about the specified
               voice with no customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Voice` object
        """

        if not voice:
            raise ValueError('voice must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_voice')
        headers.update(sdk_headers)

        params = {
            'customization_id': customization_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['voice']
        path_param_values = self.encode_path_vars(voice)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/voices/{voice}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Synthesis
    #########################

    def synthesize(self,
                   text: str,
                   *,
                   accept: str = None,
                   voice: str = None,
                   customization_id: str = None,
                   spell_out_mode: str = None,
                   rate_percentage: int = None,
                   pitch_percentage: int = None,
                   **kwargs) -> DetailedResponse:
        """
        Synthesize audio.

        Synthesizes text to audio that is spoken in the specified voice. The service bases
        its understanding of the language for the input text on the specified voice. Use a
        voice that matches the language of the input text.
        The method accepts a maximum of 5 KB of input text in the body of the request, and
        8 KB for the URL and headers. The 5 KB limit includes any SSML tags that you
        specify. The service returns the synthesized audio stream as an array of bytes.
        **See also:** [The HTTP
        interface](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-usingHTTP#usingHTTP).
        **Note:** Effective **31 March 2022**, all *neural voices* are deprecated. The
        deprecated voices remain available to existing users until 31 March 2023, when
        they will be removed from the service and the documentation. *No enhanced neural
        voices or expressive neural voices are deprecated.* For more information, see the
        [1 March 2023 service
        update](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-release-notes#text-to-speech-1march2023)
        in the release notes.
        ### Audio formats (accept types)
         The service can return audio in the following formats (MIME types).
        * Where indicated, you can optionally specify the sampling rate (`rate`) of the
        audio. You must specify a sampling rate for the `audio/alaw`, `audio/l16`,  and
        `audio/mulaw` formats. A specified sampling rate must lie in the range of 8 kHz to
        192 kHz. Some formats restrict the sampling rate to certain values, as noted.
        * For the `audio/l16` format, you can optionally specify the endianness
        (`endianness`) of the audio: `endianness=big-endian` or
        `endianness=little-endian`.
        Use the `Accept` header or the `accept` parameter to specify the requested format
        of the response audio. If you omit an audio format altogether, the service returns
        the audio in Ogg format with the Opus codec (`audio/ogg;codecs=opus`). The service
        always returns single-channel audio.
        * `audio/alaw` - You must specify the `rate` of the audio.
        * `audio/basic` - The service returns audio with a sampling rate of 8000 Hz.
        * `audio/flac` - You can optionally specify the `rate` of the audio. The default
        sampling rate is 22,050 Hz.
        * `audio/l16` - You must specify the `rate` of the audio. You can optionally
        specify the `endianness` of the audio. The default endianness is `little-endian`.
        * `audio/mp3` - You can optionally specify the `rate` of the audio. The default
        sampling rate is 22,050 Hz.
        * `audio/mpeg` - You can optionally specify the `rate` of the audio. The default
        sampling rate is 22,050 Hz.
        * `audio/mulaw` - You must specify the `rate` of the audio.
        * `audio/ogg` - The service returns the audio in the `vorbis` codec. You can
        optionally specify the `rate` of the audio. The default sampling rate is 22,050
        Hz.
        * `audio/ogg;codecs=opus` - You can optionally specify the `rate` of the audio.
        Only the following values are valid sampling rates: `48000`, `24000`, `16000`,
        `12000`, or `8000`. If you specify a value other than one of these, the service
        returns an error. The default sampling rate is 48,000 Hz.
        * `audio/ogg;codecs=vorbis` - You can optionally specify the `rate` of the audio.
        The default sampling rate is 22,050 Hz.
        * `audio/wav` - You can optionally specify the `rate` of the audio. The default
        sampling rate is 22,050 Hz.
        * `audio/webm` - The service returns the audio in the `opus` codec. The service
        returns audio with a sampling rate of 48,000 Hz.
        * `audio/webm;codecs=opus` - The service returns audio with a sampling rate of
        48,000 Hz.
        * `audio/webm;codecs=vorbis` - You can optionally specify the `rate` of the audio.
        The default sampling rate is 22,050 Hz.
        For more information about specifying an audio format, including additional
        details about some of the formats, see [Using audio
        formats](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-audio-formats).
        **Note:** By default, the service returns audio in the Ogg audio format with the
        Opus codec (`audio/ogg;codecs=opus`). However, the Ogg audio format is not
        supported with the Safari browser. If you are using the service with the Safari
        browser, you must use the `Accept` request header or the `accept` query parameter
        specify a different format in which you want the service to return the audio.
        ### Warning messages
         If a request includes invalid query parameters, the service returns a `Warnings`
        response header that provides messages about the invalid parameters. The warning
        includes a descriptive message and a list of invalid argument strings. For
        example, a message such as `"Unknown arguments:"` or `"Unknown url query
        arguments:"` followed by a list of the form `"{invalid_arg_1}, {invalid_arg_2}."`
        The request succeeds despite the warnings.

        :param str text: The text to synthesize.
        :param str accept: (optional) The requested format (MIME type) of the
               audio. You can use the `Accept` header or the `accept` parameter to specify
               the audio format. For more information about specifying an audio format,
               see **Audio formats (accept types)** in the method description.
        :param str voice: (optional) The voice to use for speech synthesis. If you
               omit the `voice` parameter, the service uses the US English
               `en-US_MichaelV3Voice` by default.
               _For IBM Cloud Pak for Data,_ if you do not install the
               `en-US_MichaelV3Voice`, you must either specify a voice with the request or
               specify a new default voice for your installation of the service.
               **See also:**
               * [Languages and
               voices](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices)
               * [Using the default
               voice](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices-use#specify-voice-default).
        :param str customization_id: (optional) The customization ID (GUID) of a
               custom model to use for the synthesis. If a custom model is specified, it
               works only if it matches the language of the indicated voice. You must make
               the request with credentials for the instance of the service that owns the
               custom model. Omit the parameter to use the specified voice with no
               customization.
        :param str spell_out_mode: (optional) *For German voices,* indicates how
               the service is to spell out strings of individual letters. To indicate the
               pace of the spelling, specify one of the following values:
               * `default` - The service reads the characters at the rate at which it
               synthesizes speech for the request. You can also omit the parameter
               entirely to achieve the default behavior.
               * `singles` - The service reads the characters one at a time, with a brief
               pause between each character.
               * `pairs` - The service reads the characters two at a time, with a brief
               pause between each pair.
               * `triples` - The service reads the characters three at a time, with a
               brief pause between each triplet.
               For more information, see [Specifying how strings are spelled
               out](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-synthesis-params#params-spell-out-mode).
        :param int rate_percentage: (optional) The percentage change from the
               default speaking rate of the voice that is used for speech synthesis. Each
               voice has a default speaking rate that is optimized to represent a normal
               rate of speech. The parameter accepts an integer that represents the
               percentage change from the voice's default rate:
               * Specify a signed negative integer to reduce the speaking rate by that
               percentage. For example, -10 reduces the rate by ten percent.
               * Specify an unsigned or signed positive integer to increase the speaking
               rate by that percentage. For example, 10 and +10 increase the rate by ten
               percent.
               * Specify 0 or omit the parameter to get the default speaking rate for the
               voice.
               The parameter affects the rate for an entire request.
               For more information, see [Modifying the speaking
               rate](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-synthesis-params#params-rate-percentage).
        :param int pitch_percentage: (optional) The percentage change from the
               default speaking pitch of the voice that is used for speech synthesis. Each
               voice has a default speaking pitch that is optimized to represent a normal
               tone of voice. The parameter accepts an integer that represents the
               percentage change from the voice's default tone:
               * Specify a signed negative integer to lower the voice's pitch by that
               percentage. For example, -5 reduces the tone by five percent.
               * Specify an unsigned or signed positive integer to increase the voice's
               pitch by that percentage. For example, 5 and +5 increase the tone by five
               percent.
               * Specify 0 or omit the parameter to get the default speaking pitch for the
               voice.
               The parameter affects the pitch for an entire request.
               For more information, see [Modifying the speaking
               pitch](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-synthesis-params#params-pitch-percentage).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if text is None:
            raise ValueError('text must be provided')
        headers = {
            'Accept': accept,
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='synthesize')
        headers.update(sdk_headers)

        params = {
            'voice': voice,
            'customization_id': customization_id,
            'spell_out_mode': spell_out_mode,
            'rate_percentage': rate_percentage,
            'pitch_percentage': pitch_percentage,
        }

        data = {
            'text': text,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/v1/synthesize'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Pronunciation
    #########################

    def get_pronunciation(self,
                          text: str,
                          *,
                          voice: str = None,
                          format: str = None,
                          customization_id: str = None,
                          **kwargs) -> DetailedResponse:
        """
        Get pronunciation.

        Gets the phonetic pronunciation for the specified word. You can request the
        pronunciation for a specific format. You can also request the pronunciation for a
        specific voice to see the default translation for the language of that voice or
        for a specific custom model to see the translation for that model.
        **Note:** Effective **31 March 2022**, all *neural voices* are deprecated. The
        deprecated voices remain available to existing users until 31 March 2023, when
        they will be removed from the service and the documentation. *No enhanced neural
        voices or expressive neural voices are deprecated.* For more information, see the
        [1 March 2023 service
        update](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-release-notes#text-to-speech-1march2023)
        in the release notes.
        **See also:** [Querying a word from a
        language](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuWordsQueryLanguage).

        :param str text: The word for which the pronunciation is requested.
        :param str voice: (optional) A voice that specifies the language in which
               the pronunciation is to be returned. If you omit the `voice` parameter, the
               service uses the US English `en-US_MichaelV3Voice` by default. All voices
               for the same language (for example, `en-US`) return the same translation.
               _For IBM Cloud Pak for Data,_ if you do not install the
               `en-US_MichaelV3Voice`, you must either specify a voice with the request or
               specify a new default voice for your installation of the service.
               **See also:** [Using the default
               voice](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices-use#specify-voice-default).
        :param str format: (optional) The phoneme format in which to return the
               pronunciation. The Arabic, Chinese, Dutch, Australian English, and Korean
               languages support only IPA. Omit the parameter to obtain the pronunciation
               in the default format.
        :param str customization_id: (optional) The customization ID (GUID) of a
               custom model for which the pronunciation is to be returned. The language of
               a specified custom model must match the language of the specified voice. If
               the word is not defined in the specified custom model, the service returns
               the default translation for the custom model's language. You must make the
               request with credentials for the instance of the service that owns the
               custom model. Omit the parameter to see the translation for the specified
               voice with no customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Pronunciation` object
        """

        if not text:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_pronunciation')
        headers.update(sdk_headers)

        params = {
            'text': text,
            'voice': voice,
            'format': format,
            'customization_id': customization_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/pronunciation'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom models
    #########################

    def create_custom_model(self,
                            name: str,
                            *,
                            language: str = None,
                            description: str = None,
                            **kwargs) -> DetailedResponse:
        """
        Create a custom model.

        Creates a new empty custom model. You must specify a name for the new custom
        model. You can optionally specify the language and a description for the new
        model. The model is owned by the instance of the service whose credentials are
        used to create it.
        **See also:** [Creating a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customModels#cuModelsCreate).
        **Note:** Effective **31 March 2022**, all *neural voices* are deprecated. The
        deprecated voices remain available to existing users until 31 March 2023, when
        they will be removed from the service and the documentation. *No enhanced neural
        voices or expressive neural voices are deprecated.* For more information, see the
        [1 March 2023 service
        update](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-release-notes#text-to-speech-1march2023)
        in the release notes.

        :param str name: The name of the new custom model. Use a localized name
               that matches the language of the custom model. Use a name that describes
               the purpose of the custom model, such as `Medical custom model` or `Legal
               custom model`. Use a name that is unique among all custom models that you
               own.
               Include a maximum of 256 characters in the name. Do not use backslashes,
               slashes, colons, equal signs, ampersands, or question marks in the name.
        :param str language: (optional) The language of the new custom model. You
               create a custom model for a specific language, not for a specific voice. A
               custom model can be used with any voice for its specified language. Omit
               the parameter to use the the default language, `en-US`.
        :param str description: (optional) A recommended description of the new
               custom model. Use a localized description that matches the language of the
               custom model. Include a maximum of 128 characters in the description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomModel` object
        """

        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_custom_model')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'language': language,
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def list_custom_models(self,
                           *,
                           language: str = None,
                           **kwargs) -> DetailedResponse:
        """
        List custom models.

        Lists metadata such as the name and description for all custom models that are
        owned by an instance of the service. Specify a language to list the custom models
        for that language only. To see the words and prompts in addition to the metadata
        for a specific custom model, use the [Get a custom model](#getcustommodel) method.
        You must use credentials for the instance of the service that owns a model to list
        information about it.
        **See also:** [Querying all custom
        models](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customModels#cuModelsQueryAll).

        :param str language: (optional) The language for which custom models that
               are owned by the requesting credentials are to be returned. Omit the
               parameter to see all custom models that are owned by the requester.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomModels` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_custom_models')
        headers.update(sdk_headers)

        params = {
            'language': language,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/customizations'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_custom_model(self,
                            customization_id: str,
                            *,
                            name: str = None,
                            description: str = None,
                            words: List['Word'] = None,
                            **kwargs) -> DetailedResponse:
        """
        Update a custom model.

        Updates information for the specified custom model. You can update metadata such
        as the name and description of the model. You can also update the words in the
        model and their translations. Adding a new translation for a word that already
        exists in a custom model overwrites the word's existing translation. A custom
        model can contain no more than 20,000 entries. You must use credentials for the
        instance of the service that owns a model to update it.
        You can define sounds-like or phonetic translations for words. A sounds-like
        translation consists of one or more words that, when combined, sound like the
        word. Phonetic translations are based on the SSML phoneme format for representing
        a word. You can specify them in standard International Phonetic Alphabet (IPA)
        representation
          <code>&lt;phoneme alphabet="ipa"
        ph="t&#601;m&#712;&#593;to"&gt;&lt;/phoneme&gt;</code>
          or in the proprietary IBM Symbolic Phonetic Representation (SPR)
          <code>&lt;phoneme alphabet="ibm"
        ph="1gAstroEntxrYFXs"&gt;&lt;/phoneme&gt;</code>
        **See also:**
        * [Updating a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customModels#cuModelsUpdate)
        * [Adding words to a Japanese custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuJapaneseAdd)
        * [Understanding
        customization](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customIntro#customIntro).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param str name: (optional) A new name for the custom model.
        :param str description: (optional) A new description for the custom model.
        :param List[Word] words: (optional) An array of `Word` objects that
               provides the words and their translations that are to be added or updated
               for the custom model. Pass an empty array to make no additions or updates.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if words is not None:
            words = [convert_model(x) for x in words]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_custom_model')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
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
        url = '/v1/customizations/{customization_id}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_custom_model(self, customization_id: str,
                         **kwargs) -> DetailedResponse:
        """
        Get a custom model.

        Gets all information about a specified custom model. In addition to metadata such
        as the name and description of the custom model, the output includes the words and
        their translations that are defined for the model, as well as any prompts that are
        defined for the model. To see just the metadata for a model, use the [List custom
        models](#listcustommodels) method.
        **See also:** [Querying a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customModels#cuModelsQuery).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomModel` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_custom_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_custom_model(self, customization_id: str,
                            **kwargs) -> DetailedResponse:
        """
        Delete a custom model.

        Deletes the specified custom model. You must use credentials for the instance of
        the service that owns a model to delete it.
        **See also:** [Deleting a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customModels#cuModelsDelete).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_custom_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom words
    #########################

    def add_words(self, customization_id: str, words: List['Word'],
                  **kwargs) -> DetailedResponse:
        """
        Add custom words.

        Adds one or more words and their translations to the specified custom model.
        Adding a new translation for a word that already exists in a custom model
        overwrites the word's existing translation. A custom model can contain no more
        than 20,000 entries. You must use credentials for the instance of the service that
        owns a model to add words to it.
        You can define sounds-like or phonetic translations for words. A sounds-like
        translation consists of one or more words that, when combined, sound like the
        word. Phonetic translations are based on the SSML phoneme format for representing
        a word. You can specify them in standard International Phonetic Alphabet (IPA)
        representation
          <code>&lt;phoneme alphabet="ipa"
        ph="t&#601;m&#712;&#593;to"&gt;&lt;/phoneme&gt;</code>
          or in the proprietary IBM Symbolic Phonetic Representation (SPR)
          <code>&lt;phoneme alphabet="ibm"
        ph="1gAstroEntxrYFXs"&gt;&lt;/phoneme&gt;</code>
        **See also:**
        * [Adding multiple words to a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuWordsAdd)
        * [Adding words to a Japanese custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuJapaneseAdd)
        * [Understanding
        customization](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customIntro#customIntro).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param List[Word] words: The [Add custom words](#addwords) method accepts
               an array of `Word` objects. Each object provides a word that is to be added
               or updated for the custom model and the word's translation.
               The [List custom words](#listwords) method returns an array of `Word`
               objects. Each object shows a word and its translation from the custom
               model. The words are listed in alphabetical order, with uppercase letters
               listed before lowercase letters. The array is empty if the custom model
               contains no words.
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_words')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def list_words(self, customization_id: str, **kwargs) -> DetailedResponse:
        """
        List custom words.

        Lists all of the words and their translations for the specified custom model. The
        output shows the translations as they are defined in the model. You must use
        credentials for the instance of the service that owns a model to list its words.
        **See also:** [Querying all words from a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuWordsQueryModel).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Words` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_words')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def add_word(self,
                 customization_id: str,
                 word: str,
                 translation: str,
                 *,
                 part_of_speech: str = None,
                 **kwargs) -> DetailedResponse:
        """
        Add a custom word.

        Adds a single word and its translation to the specified custom model. Adding a new
        translation for a word that already exists in a custom model overwrites the word's
        existing translation. A custom model can contain no more than 20,000 entries. You
        must use credentials for the instance of the service that owns a model to add a
        word to it.
        You can define sounds-like or phonetic translations for words. A sounds-like
        translation consists of one or more words that, when combined, sound like the
        word. Phonetic translations are based on the SSML phoneme format for representing
        a word. You can specify them in standard International Phonetic Alphabet (IPA)
        representation
          <code>&lt;phoneme alphabet="ipa"
        ph="t&#601;m&#712;&#593;to"&gt;&lt;/phoneme&gt;</code>
          or in the proprietary IBM Symbolic Phonetic Representation (SPR)
          <code>&lt;phoneme alphabet="ibm"
        ph="1gAstroEntxrYFXs"&gt;&lt;/phoneme&gt;</code>
        **See also:**
        * [Adding a single word to a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuWordAdd)
        * [Adding words to a Japanese custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuJapaneseAdd)
        * [Understanding
        customization](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customIntro#customIntro).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param str word: The word that is to be added or updated for the custom
               model.
        :param str translation: The phonetic or sounds-like translation for the
               word. A phonetic translation is based on the SSML format for representing
               the phonetic string of a word either as an IPA translation or as an IBM SPR
               translation. The Arabic, Chinese, Dutch, Australian English, and Korean
               languages support only IPA. A sounds-like is one or more words that, when
               combined, sound like the word.
        :param str part_of_speech: (optional) **Japanese only.** The part of speech
               for the word. The service uses the value to produce the correct intonation
               for the word. You can create only a single entry, with or without a single
               part of speech, for any word; you cannot create multiple entries with
               different parts of speech for the same word. For more information, see
               [Working with Japanese
               entries](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-rules#jaNotes).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not word:
            raise ValueError('word must be provided')
        if translation is None:
            raise ValueError('translation must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_word')
        headers.update(sdk_headers)

        data = {
            'translation': translation,
            'part_of_speech': part_of_speech,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['customization_id', 'word']
        path_param_values = self.encode_path_vars(customization_id, word)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words/{word}'.format(
            **path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_word(self, customization_id: str, word: str,
                 **kwargs) -> DetailedResponse:
        """
        Get a custom word.

        Gets the translation for a single word from the specified custom model. The output
        shows the translation as it is defined in the model. You must use credentials for
        the instance of the service that owns a model to list its words.
        **See also:** [Querying a single word from a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuWordQueryModel).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param str word: The word that is to be queried from the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Translation` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not word:
            raise ValueError('word must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_word')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'word']
        path_param_values = self.encode_path_vars(customization_id, word)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words/{word}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_word(self, customization_id: str, word: str,
                    **kwargs) -> DetailedResponse:
        """
        Delete a custom word.

        Deletes a single word from the specified custom model. You must use credentials
        for the instance of the service that owns a model to delete its words.
        **See also:** [Deleting a word from a custom
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-customWords#cuWordDelete).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param str word: The word that is to be deleted from the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not word:
            raise ValueError('word must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_word')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['customization_id', 'word']
        path_param_values = self.encode_path_vars(customization_id, word)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/words/{word}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom prompts
    #########################

    def list_custom_prompts(self, customization_id: str,
                            **kwargs) -> DetailedResponse:
        """
        List custom prompts.

        Lists information about all custom prompts that are defined for a custom model.
        The information includes the prompt ID, prompt text, status, and optional speaker
        ID for each prompt of the custom model. You must use credentials for the instance
        of the service that owns the custom model. The same information about all of the
        prompts for a custom model is also provided by the [Get a custom
        model](#getcustommodel) method. That method provides complete details about a
        specified custom model, including its language, owner, custom words, and more.
        Custom prompts are supported only for use with US English custom models and
        voices.
        **See also:** [Listing custom
        prompts](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-custom-prompts#tbe-custom-prompts-list).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Prompts` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_custom_prompts')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id']
        path_param_values = self.encode_path_vars(customization_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/prompts'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def add_custom_prompt(self, customization_id: str, prompt_id: str,
                          metadata: 'PromptMetadata', file: BinaryIO,
                          **kwargs) -> DetailedResponse:
        """
        Add a custom prompt.

        Adds a custom prompt to a custom model. A prompt is defined by the text that is to
        be spoken, the audio for that text, a unique user-specified ID for the prompt, and
        an optional speaker ID. The information is used to generate prosodic data that is
        not visible to the user. This data is used by the service to produce the
        synthesized audio upon request. You must use credentials for the instance of the
        service that owns a custom model to add a prompt to it. You can add a maximum of
        1000 custom prompts to a single custom model.
        You are recommended to assign meaningful values for prompt IDs. For example, use
        `goodbye` to identify a prompt that speaks a farewell message. Prompt IDs must be
        unique within a given custom model. You cannot define two prompts with the same
        name for the same custom model. If you provide the ID of an existing prompt, the
        previously uploaded prompt is replaced by the new information. The existing prompt
        is reprocessed by using the new text and audio and, if provided, new speaker
        model, and the prosody data associated with the prompt is updated.
        The quality of a prompt is undefined if the language of a prompt does not match
        the language of its custom model. This is consistent with any text or SSML that is
        specified for a speech synthesis request. The service makes a best-effort attempt
        to render the specified text for the prompt; it does not validate that the
        language of the text matches the language of the model.
        Adding a prompt is an asynchronous operation. Although it accepts less audio than
        speaker enrollment, the service must align the audio with the provided text. The
        time that it takes to process a prompt depends on the prompt itself. The
        processing time for a reasonably sized prompt generally matches the length of the
        audio (for example, it takes 20 seconds to process a 20-second prompt).
        For shorter prompts, you can wait for a reasonable amount of time and then check
        the status of the prompt with the [Get a custom prompt](#getcustomprompt) method.
        For longer prompts, consider using that method to poll the service every few
        seconds to determine when the prompt becomes available. No prompt can be used for
        speech synthesis if it is in the `processing` or `failed` state. Only prompts that
        are in the `available` state can be used for speech synthesis.
        When it processes a request, the service attempts to align the text and the audio
        that are provided for the prompt. The text that is passed with a prompt must match
        the spoken audio as closely as possible. Optimally, the text and audio match
        exactly. The service does its best to align the specified text with the audio, and
        it can often compensate for mismatches between the two. But if the service cannot
        effectively align the text and the audio, possibly because the magnitude of
        mismatches between the two is too great, processing of the prompt fails.
        ### Evaluating a prompt
         Always listen to and evaluate a prompt to determine its quality before using it
        in production. To evaluate a prompt, include only the single prompt in a speech
        synthesis request by using the following SSML extension, in this case for a prompt
        whose ID is `goodbye`:
        `<ibm:prompt id="goodbye"/>`
        In some cases, you might need to rerecord and resubmit a prompt as many as five
        times to address the following possible problems:
        * The service might fail to detect a mismatch between the prompt’s text and audio.
        The longer the prompt, the greater the chance for misalignment between its text
        and audio. Therefore, multiple shorter prompts are preferable to a single long
        prompt.
        * The text of a prompt might include a word that the service does not recognize.
        In this case, you can create a custom word and pronunciation pair to tell the
        service how to pronounce the word. You must then re-create the prompt.
        * The quality of the input audio might be insufficient or the service’s processing
        of the audio might fail to detect the intended prosody. Submitting new audio for
        the prompt can correct these issues.
        If a prompt that is created without a speaker ID does not adequately reflect the
        intended prosody, enrolling the speaker and providing a speaker ID for the prompt
        is one recommended means of potentially improving the quality of the prompt. This
        is especially important for shorter prompts such as "good-bye" or "thank you,"
        where less audio data makes it more difficult to match the prosody of the speaker.
        Custom prompts are supported only for use with US English custom models and
        voices.
        **See also:**
        * [Add a custom
        prompt](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-create#tbe-create-add-prompt)
        * [Evaluate a custom
        prompt](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-create#tbe-create-evaluate-prompt)
        * [Rules for creating custom
        prompts](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-rules#tbe-rules-prompts).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param str prompt_id: The identifier of the prompt that is to be added to
               the custom model:
               * Include a maximum of 49 characters in the ID.
               * Include only alphanumeric characters and `_` (underscores) in the ID.
               * Do not include XML sensitive characters (double quotes, single quotes,
               ampersands, angle brackets, and slashes) in the ID.
               * To add a new prompt, the ID must be unique for the specified custom
               model. Otherwise, the new information for the prompt overwrites the
               existing prompt that has that ID.
        :param PromptMetadata metadata: Information about the prompt that is to be
               added to a custom model. The following example of a `PromptMetadata` object
               includes both the required prompt text and an optional speaker model ID:
               `{ "prompt_text": "Thank you and good-bye!", "speaker_id":
               "823068b2-ed4e-11ea-b6e0-7b6456aa95cc" }`.
        :param BinaryIO file: An audio file that speaks the text of the prompt with
               intonation and prosody that matches how you would like the prompt to be
               spoken.
               * The prompt audio must be in WAV format and must have a minimum sampling
               rate of 16 kHz. The service accepts audio with higher sampling rates. The
               service transcodes all audio to 16 kHz before processing it.
               * The length of the prompt audio is limited to 30 seconds.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Prompt` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not prompt_id:
            raise ValueError('prompt_id must be provided')
        if metadata is None:
            raise ValueError('metadata must be provided')
        if file is None:
            raise ValueError('file must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_custom_prompt')
        headers.update(sdk_headers)

        form_data = []
        form_data.append(
            ('metadata', (None, json.dumps(metadata), 'application/json')))
        form_data.append(('file', (None, file, 'audio/wav')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'prompt_id']
        path_param_values = self.encode_path_vars(customization_id, prompt_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/prompts/{prompt_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    def get_custom_prompt(self, customization_id: str, prompt_id: str,
                          **kwargs) -> DetailedResponse:
        """
        Get a custom prompt.

        Gets information about a specified custom prompt for a specified custom model. The
        information includes the prompt ID, prompt text, status, and optional speaker ID
        for each prompt of the custom model. You must use credentials for the instance of
        the service that owns the custom model. Custom prompts are supported only for use
        with US English custom models and voices.
        **See also:** [Listing custom
        prompts](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-custom-prompts#tbe-custom-prompts-list).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param str prompt_id: The identifier (name) of the prompt.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Prompt` object
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not prompt_id:
            raise ValueError('prompt_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_custom_prompt')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['customization_id', 'prompt_id']
        path_param_values = self.encode_path_vars(customization_id, prompt_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/prompts/{prompt_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_custom_prompt(self, customization_id: str, prompt_id: str,
                             **kwargs) -> DetailedResponse:
        """
        Delete a custom prompt.

        Deletes an existing custom prompt from a custom model. The service deletes the
        prompt with the specified ID. You must use credentials for the instance of the
        service that owns the custom model from which the prompt is to be deleted.
        **Caution:** Deleting a custom prompt elicits a 400 response code from synthesis
        requests that attempt to use the prompt. Make sure that you do not attempt to use
        a deleted prompt in a production application. Custom prompts are supported only
        for use with US English custom models and voices.
        **See also:** [Deleting a custom
        prompt](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-custom-prompts#tbe-custom-prompts-delete).

        :param str customization_id: The customization ID (GUID) of the custom
               model. You must make the request with credentials for the instance of the
               service that owns the custom model.
        :param str prompt_id: The identifier (name) of the prompt that is to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customization_id:
            raise ValueError('customization_id must be provided')
        if not prompt_id:
            raise ValueError('prompt_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_custom_prompt')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['customization_id', 'prompt_id']
        path_param_values = self.encode_path_vars(customization_id, prompt_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/customizations/{customization_id}/prompts/{prompt_id}'.format(
            **path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Speaker models
    #########################

    def list_speaker_models(self, **kwargs) -> DetailedResponse:
        """
        List speaker models.

        Lists information about all speaker models that are defined for a service
        instance. The information includes the speaker ID and speaker name of each defined
        speaker. You must use credentials for the instance of a service to list its
        speakers. Speaker models and the custom prompts with which they are used are
        supported only for use with US English custom models and voices.
        **See also:** [Listing speaker
        models](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-speaker-models#tbe-speaker-models-list).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Speakers` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_speaker_models')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/speakers'
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def create_speaker_model(self, speaker_name: str, audio: BinaryIO,
                             **kwargs) -> DetailedResponse:
        """
        Create a speaker model.

        Creates a new speaker model, which is an optional enrollment token for users who
        are to add prompts to custom models. A speaker model contains information about a
        user's voice. The service extracts this information from a WAV audio sample that
        you pass as the body of the request. Associating a speaker model with a prompt is
        optional, but the information that is extracted from the speaker model helps the
        service learn about the speaker's voice.
        A speaker model can make an appreciable difference in the quality of prompts,
        especially short prompts with relatively little audio, that are associated with
        that speaker. A speaker model can help the service produce a prompt with more
        confidence; the lack of a speaker model can potentially compromise the quality of
        a prompt.
        The gender of the speaker who creates a speaker model does not need to match the
        gender of a voice that is used with prompts that are associated with that speaker
        model. For example, a speaker model that is created by a male speaker can be
        associated with prompts that are spoken by female voices.
        You create a speaker model for a given instance of the service. The new speaker
        model is owned by the service instance whose credentials are used to create it.
        That same speaker can then be used to create prompts for all custom models within
        that service instance. No language is associated with a speaker model, but each
        custom model has a single specified language. You can add prompts only to US
        English models.
        You specify a name for the speaker when you create it. The name must be unique
        among all speaker names for the owning service instance. To re-create a speaker
        model for an existing speaker name, you must first delete the existing speaker
        model that has that name.
        Speaker enrollment is a synchronous operation. Although it accepts more audio data
        than a prompt, the process of adding a speaker is very fast. The service simply
        extracts information about the speaker’s voice from the audio. Unlike prompts,
        speaker models neither need nor accept a transcription of the audio. When the call
        returns, the audio is fully processed and the speaker enrollment is complete.
        The service returns a speaker ID with the request. A speaker ID is globally unique
        identifier (GUID) that you use to identify the speaker in subsequent requests to
        the service. Speaker models and the custom prompts with which they are used are
        supported only for use with US English custom models and voices.
        **See also:**
        * [Create a speaker
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-create#tbe-create-speaker-model)
        * [Rules for creating speaker
        models](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-rules#tbe-rules-speakers).

        :param str speaker_name: The name of the speaker that is to be added to the
               service instance.
               * Include a maximum of 49 characters in the name.
               * Include only alphanumeric characters and `_` (underscores) in the name.
               * Do not include XML sensitive characters (double quotes, single quotes,
               ampersands, angle brackets, and slashes) in the name.
               * Do not use the name of an existing speaker that is already defined for
               the service instance.
        :param BinaryIO audio: An enrollment audio file that contains a sample of
               the speaker’s voice.
               * The enrollment audio must be in WAV format and must have a minimum
               sampling rate of 16 kHz. The service accepts audio with higher sampling
               rates. It transcodes all audio to 16 kHz before processing it.
               * The length of the enrollment audio is limited to 1 minute. Speaking one
               or two paragraphs of text that include five to ten sentences is
               recommended.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SpeakerModel` object
        """

        if not speaker_name:
            raise ValueError('speaker_name must be provided')
        if audio is None:
            raise ValueError('audio must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_speaker_model')
        headers.update(sdk_headers)

        params = {
            'speaker_name': speaker_name,
        }

        data = audio
        headers['content-type'] = 'audio/wav'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/speakers'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def get_speaker_model(self, speaker_id: str, **kwargs) -> DetailedResponse:
        """
        Get a speaker model.

        Gets information about all prompts that are defined by a specified speaker for all
        custom models that are owned by a service instance. The information is grouped by
        the customization IDs of the custom models. For each custom model, the information
        lists information about each prompt that is defined for that custom model by the
        speaker. You must use credentials for the instance of the service that owns a
        speaker model to list its prompts. Speaker models and the custom prompts with
        which they are used are supported only for use with US English custom models and
        voices.
        **See also:** [Listing the custom prompts for a speaker
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-speaker-models#tbe-speaker-models-list-prompts).

        :param str speaker_id: The speaker ID (GUID) of the speaker model. You must
               make the request with service credentials for the instance of the service
               that owns the speaker model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SpeakerCustomModels` object
        """

        if not speaker_id:
            raise ValueError('speaker_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_speaker_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['speaker_id']
        path_param_values = self.encode_path_vars(speaker_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/speakers/{speaker_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request, **kwargs)
        return response

    def delete_speaker_model(self, speaker_id: str,
                             **kwargs) -> DetailedResponse:
        """
        Delete a speaker model.

        Deletes an existing speaker model from the service instance. The service deletes
        the enrolled speaker with the specified speaker ID. You must use credentials for
        the instance of the service that owns a speaker model to delete the speaker.
        Any prompts that are associated with the deleted speaker are not affected by the
        speaker's deletion. The prosodic data that defines the quality of a prompt is
        established when the prompt is created. A prompt is static and remains unaffected
        by deletion of its associated speaker. However, the prompt cannot be resubmitted
        or updated with its original speaker once that speaker is deleted. Speaker models
        and the custom prompts with which they are used are supported only for use with US
        English custom models and voices.
        **See also:** [Deleting a speaker
        model](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-tbe-speaker-models#tbe-speaker-models-delete).

        :param str speaker_id: The speaker ID (GUID) of the speaker model. You must
               make the request with service credentials for the instance of the service
               that owns the speaker model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not speaker_id:
            raise ValueError('speaker_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_speaker_model')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['speaker_id']
        path_param_values = self.encode_path_vars(speaker_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/speakers/{speaker_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(self, customer_id: str, **kwargs) -> DetailedResponse:
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
        all custom models and word/translation pairs, and all data related to speech
        synthesis requests.
        **See also:** [Information
        security](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-information-security#information-security).

        :param str customer_id: The customer ID for which all data is to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customer_id:
            raise ValueError('customer_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_user_data')
        headers.update(sdk_headers)

        params = {
            'customer_id': customer_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/v1/user_data'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


class GetVoiceEnums:
    """
    Enums for get_voice parameters.
    """

    class Voice(str, Enum):
        """
        The voice for which information is to be returned.
        """
        AR_MS_OMARVOICE = 'ar-MS_OmarVoice'
        CS_CZ_ALENAVOICE = 'cs-CZ_AlenaVoice'
        DE_DE_BIRGITV3VOICE = 'de-DE_BirgitV3Voice'
        DE_DE_DIETERV3VOICE = 'de-DE_DieterV3Voice'
        DE_DE_ERIKAV3VOICE = 'de-DE_ErikaV3Voice'
        EN_AU_CRAIGVOICE = 'en-AU_CraigVoice'
        EN_AU_HEIDIEXPRESSIVE = 'en-AU_HeidiExpressive'
        EN_AU_JACKEXPRESSIVE = 'en-AU_JackExpressive'
        EN_AU_MADISONVOICE = 'en-AU_MadisonVoice'
        EN_AU_STEVEVOICE = 'en-AU_SteveVoice'
        EN_GB_CHARLOTTEV3VOICE = 'en-GB_CharlotteV3Voice'
        EN_GB_JAMESV3VOICE = 'en-GB_JamesV3Voice'
        EN_GB_KATEV3VOICE = 'en-GB_KateV3Voice'
        EN_US_ALLISONEXPRESSIVE = 'en-US_AllisonExpressive'
        EN_US_ALLISONV3VOICE = 'en-US_AllisonV3Voice'
        EN_US_EMILYV3VOICE = 'en-US_EmilyV3Voice'
        EN_US_EMMAEXPRESSIVE = 'en-US_EmmaExpressive'
        EN_US_HENRYV3VOICE = 'en-US_HenryV3Voice'
        EN_US_KEVINV3VOICE = 'en-US_KevinV3Voice'
        EN_US_LISAEXPRESSIVE = 'en-US_LisaExpressive'
        EN_US_LISAV3VOICE = 'en-US_LisaV3Voice'
        EN_US_MICHAELEXPRESSIVE = 'en-US_MichaelExpressive'
        EN_US_MICHAELV3VOICE = 'en-US_MichaelV3Voice'
        EN_US_OLIVIAV3VOICE = 'en-US_OliviaV3Voice'
        ES_ES_ENRIQUEV3VOICE = 'es-ES_EnriqueV3Voice'
        ES_ES_LAURAV3VOICE = 'es-ES_LauraV3Voice'
        ES_LA_SOFIAV3VOICE = 'es-LA_SofiaV3Voice'
        ES_US_SOFIAV3VOICE = 'es-US_SofiaV3Voice'
        FR_CA_LOUISEV3VOICE = 'fr-CA_LouiseV3Voice'
        FR_FR_NICOLASV3VOICE = 'fr-FR_NicolasV3Voice'
        FR_FR_RENEEV3VOICE = 'fr-FR_ReneeV3Voice'
        IT_IT_FRANCESCAV3VOICE = 'it-IT_FrancescaV3Voice'
        JA_JP_EMIV3VOICE = 'ja-JP_EmiV3Voice'
        KO_KR_HYUNJUNVOICE = 'ko-KR_HyunjunVoice'
        KO_KR_JINV3VOICE = 'ko-KR_JinV3Voice'
        KO_KR_SIWOOVOICE = 'ko-KR_SiWooVoice'
        KO_KR_YOUNGMIVOICE = 'ko-KR_YoungmiVoice'
        KO_KR_YUNAVOICE = 'ko-KR_YunaVoice'
        NL_BE_ADELEVOICE = 'nl-BE_AdeleVoice'
        NL_BE_BRAMVOICE = 'nl-BE_BramVoice'
        NL_NL_EMMAVOICE = 'nl-NL_EmmaVoice'
        NL_NL_LIAMVOICE = 'nl-NL_LiamVoice'
        PT_BR_ISABELAV3VOICE = 'pt-BR_IsabelaV3Voice'
        SV_SE_INGRIDVOICE = 'sv-SE_IngridVoice'
        ZH_CN_LINAVOICE = 'zh-CN_LiNaVoice'
        ZH_CN_WANGWEIVOICE = 'zh-CN_WangWeiVoice'
        ZH_CN_ZHANGJINGVOICE = 'zh-CN_ZhangJingVoice'


class SynthesizeEnums:
    """
    Enums for synthesize parameters.
    """

    class Accept(str, Enum):
        """
        The requested format (MIME type) of the audio. You can use the `Accept` header or
        the `accept` parameter to specify the audio format. For more information about
        specifying an audio format, see **Audio formats (accept types)** in the method
        description.
        """
        AUDIO_ALAW = 'audio/alaw'
        AUDIO_BASIC = 'audio/basic'
        AUDIO_FLAC = 'audio/flac'
        AUDIO_L16 = 'audio/l16'
        AUDIO_OGG = 'audio/ogg'
        AUDIO_OGG_CODECS_OPUS = 'audio/ogg;codecs=opus'
        AUDIO_OGG_CODECS_VORBIS = 'audio/ogg;codecs=vorbis'
        AUDIO_MP3 = 'audio/mp3'
        AUDIO_MPEG = 'audio/mpeg'
        AUDIO_MULAW = 'audio/mulaw'
        AUDIO_WAV = 'audio/wav'
        AUDIO_WEBM = 'audio/webm'
        AUDIO_WEBM_CODECS_OPUS = 'audio/webm;codecs=opus'
        AUDIO_WEBM_CODECS_VORBIS = 'audio/webm;codecs=vorbis'

    class Voice(str, Enum):
        """
        The voice to use for speech synthesis. If you omit the `voice` parameter, the
        service uses the US English `en-US_MichaelV3Voice` by default.
        _For IBM Cloud Pak for Data,_ if you do not install the `en-US_MichaelV3Voice`,
        you must either specify a voice with the request or specify a new default voice
        for your installation of the service.
        **See also:**
        * [Languages and
        voices](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices)
        * [Using the default
        voice](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices-use#specify-voice-default).
        """
        AR_MS_OMARVOICE = 'ar-MS_OmarVoice'
        CS_CZ_ALENAVOICE = 'cs-CZ_AlenaVoice'
        DE_DE_BIRGITV3VOICE = 'de-DE_BirgitV3Voice'
        DE_DE_DIETERV3VOICE = 'de-DE_DieterV3Voice'
        DE_DE_ERIKAV3VOICE = 'de-DE_ErikaV3Voice'
        EN_AU_CRAIGVOICE = 'en-AU_CraigVoice'
        EN_AU_HEIDIEXPRESSIVE = 'en-AU_HeidiExpressive'
        EN_AU_JACKEXPRESSIVE = 'en-AU_JackExpressive'
        EN_AU_MADISONVOICE = 'en-AU_MadisonVoice'
        EN_AU_STEVEVOICE = 'en-AU_SteveVoice'
        EN_GB_CHARLOTTEV3VOICE = 'en-GB_CharlotteV3Voice'
        EN_GB_JAMESV3VOICE = 'en-GB_JamesV3Voice'
        EN_GB_KATEV3VOICE = 'en-GB_KateV3Voice'
        EN_US_ALLISONEXPRESSIVE = 'en-US_AllisonExpressive'
        EN_US_ALLISONV3VOICE = 'en-US_AllisonV3Voice'
        EN_US_EMILYV3VOICE = 'en-US_EmilyV3Voice'
        EN_US_EMMAEXPRESSIVE = 'en-US_EmmaExpressive'
        EN_US_HENRYV3VOICE = 'en-US_HenryV3Voice'
        EN_US_KEVINV3VOICE = 'en-US_KevinV3Voice'
        EN_US_LISAEXPRESSIVE = 'en-US_LisaExpressive'
        EN_US_LISAV3VOICE = 'en-US_LisaV3Voice'
        EN_US_MICHAELEXPRESSIVE = 'en-US_MichaelExpressive'
        EN_US_MICHAELV3VOICE = 'en-US_MichaelV3Voice'
        EN_US_OLIVIAV3VOICE = 'en-US_OliviaV3Voice'
        ES_ES_ENRIQUEV3VOICE = 'es-ES_EnriqueV3Voice'
        ES_ES_LAURAV3VOICE = 'es-ES_LauraV3Voice'
        ES_LA_SOFIAV3VOICE = 'es-LA_SofiaV3Voice'
        ES_US_SOFIAV3VOICE = 'es-US_SofiaV3Voice'
        FR_CA_LOUISEV3VOICE = 'fr-CA_LouiseV3Voice'
        FR_FR_NICOLASV3VOICE = 'fr-FR_NicolasV3Voice'
        FR_FR_RENEEV3VOICE = 'fr-FR_ReneeV3Voice'
        IT_IT_FRANCESCAV3VOICE = 'it-IT_FrancescaV3Voice'
        JA_JP_EMIV3VOICE = 'ja-JP_EmiV3Voice'
        KO_KR_HYUNJUNVOICE = 'ko-KR_HyunjunVoice'
        KO_KR_JINV3VOICE = 'ko-KR_JinV3Voice'
        KO_KR_SIWOOVOICE = 'ko-KR_SiWooVoice'
        KO_KR_YOUNGMIVOICE = 'ko-KR_YoungmiVoice'
        KO_KR_YUNAVOICE = 'ko-KR_YunaVoice'
        NL_BE_ADELEVOICE = 'nl-BE_AdeleVoice'
        NL_BE_BRAMVOICE = 'nl-BE_BramVoice'
        NL_NL_EMMAVOICE = 'nl-NL_EmmaVoice'
        NL_NL_LIAMVOICE = 'nl-NL_LiamVoice'
        PT_BR_ISABELAV3VOICE = 'pt-BR_IsabelaV3Voice'
        SV_SE_INGRIDVOICE = 'sv-SE_IngridVoice'
        ZH_CN_LINAVOICE = 'zh-CN_LiNaVoice'
        ZH_CN_WANGWEIVOICE = 'zh-CN_WangWeiVoice'
        ZH_CN_ZHANGJINGVOICE = 'zh-CN_ZhangJingVoice'

    class SpellOutMode(str, Enum):
        """
        *For German voices,* indicates how the service is to spell out strings of
        individual letters. To indicate the pace of the spelling, specify one of the
        following values:
        * `default` - The service reads the characters at the rate at which it synthesizes
        speech for the request. You can also omit the parameter entirely to achieve the
        default behavior.
        * `singles` - The service reads the characters one at a time, with a brief pause
        between each character.
        * `pairs` - The service reads the characters two at a time, with a brief pause
        between each pair.
        * `triples` - The service reads the characters three at a time, with a brief pause
        between each triplet.
        For more information, see [Specifying how strings are spelled
        out](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-synthesis-params#params-spell-out-mode).
        """
        DEFAULT = 'default'
        SINGLES = 'singles'
        PAIRS = 'pairs'
        TRIPLES = 'triples'


class GetPronunciationEnums:
    """
    Enums for get_pronunciation parameters.
    """

    class Voice(str, Enum):
        """
        A voice that specifies the language in which the pronunciation is to be returned.
        If you omit the `voice` parameter, the service uses the US English
        `en-US_MichaelV3Voice` by default. All voices for the same language (for example,
        `en-US`) return the same translation.
        _For IBM Cloud Pak for Data,_ if you do not install the `en-US_MichaelV3Voice`,
        you must either specify a voice with the request or specify a new default voice
        for your installation of the service.
        **See also:** [Using the default
        voice](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices-use#specify-voice-default).
        """
        AR_MS_OMARVOICE = 'ar-MS_OmarVoice'
        CS_CZ_ALENAVOICE = 'cs-CZ_AlenaVoice'
        DE_DE_BIRGITV3VOICE = 'de-DE_BirgitV3Voice'
        DE_DE_DIETERV3VOICE = 'de-DE_DieterV3Voice'
        DE_DE_ERIKAV3VOICE = 'de-DE_ErikaV3Voice'
        EN_AU_CRAIGVOICE = 'en-AU_CraigVoice'
        EN_AU_HEIDIEXPRESSIVE = 'en-AU_HeidiExpressive'
        EN_AU_JACKEXPRESSIVE = 'en-AU_JackExpressive'
        EN_AU_MADISONVOICE = 'en-AU_MadisonVoice'
        EN_AU_STEVEVOICE = 'en-AU_SteveVoice'
        EN_GB_CHARLOTTEV3VOICE = 'en-GB_CharlotteV3Voice'
        EN_GB_JAMESV3VOICE = 'en-GB_JamesV3Voice'
        EN_GB_KATEV3VOICE = 'en-GB_KateV3Voice'
        EN_US_ALLISONEXPRESSIVE = 'en-US_AllisonExpressive'
        EN_US_ALLISONV3VOICE = 'en-US_AllisonV3Voice'
        EN_US_EMILYV3VOICE = 'en-US_EmilyV3Voice'
        EN_US_EMMAEXPRESSIVE = 'en-US_EmmaExpressive'
        EN_US_HENRYV3VOICE = 'en-US_HenryV3Voice'
        EN_US_KEVINV3VOICE = 'en-US_KevinV3Voice'
        EN_US_LISAEXPRESSIVE = 'en-US_LisaExpressive'
        EN_US_LISAV3VOICE = 'en-US_LisaV3Voice'
        EN_US_MICHAELEXPRESSIVE = 'en-US_MichaelExpressive'
        EN_US_MICHAELV3VOICE = 'en-US_MichaelV3Voice'
        EN_US_OLIVIAV3VOICE = 'en-US_OliviaV3Voice'
        ES_ES_ENRIQUEV3VOICE = 'es-ES_EnriqueV3Voice'
        ES_ES_LAURAV3VOICE = 'es-ES_LauraV3Voice'
        ES_LA_SOFIAV3VOICE = 'es-LA_SofiaV3Voice'
        ES_US_SOFIAV3VOICE = 'es-US_SofiaV3Voice'
        FR_CA_LOUISEV3VOICE = 'fr-CA_LouiseV3Voice'
        FR_FR_NICOLASV3VOICE = 'fr-FR_NicolasV3Voice'
        FR_FR_RENEEV3VOICE = 'fr-FR_ReneeV3Voice'
        IT_IT_FRANCESCAV3VOICE = 'it-IT_FrancescaV3Voice'
        JA_JP_EMIV3VOICE = 'ja-JP_EmiV3Voice'
        KO_KR_HYUNJUNVOICE = 'ko-KR_HyunjunVoice'
        KO_KR_JINV3VOICE = 'ko-KR_JinV3Voice'
        KO_KR_SIWOOVOICE = 'ko-KR_SiWooVoice'
        KO_KR_YOUNGMIVOICE = 'ko-KR_YoungmiVoice'
        KO_KR_YUNAVOICE = 'ko-KR_YunaVoice'
        NL_BE_ADELEVOICE = 'nl-BE_AdeleVoice'
        NL_BE_BRAMVOICE = 'nl-BE_BramVoice'
        NL_NL_EMMAVOICE = 'nl-NL_EmmaVoice'
        NL_NL_LIAMVOICE = 'nl-NL_LiamVoice'
        PT_BR_ISABELAV3VOICE = 'pt-BR_IsabelaV3Voice'
        SV_SE_INGRIDVOICE = 'sv-SE_IngridVoice'
        ZH_CN_LINAVOICE = 'zh-CN_LiNaVoice'
        ZH_CN_WANGWEIVOICE = 'zh-CN_WangWeiVoice'
        ZH_CN_ZHANGJINGVOICE = 'zh-CN_ZhangJingVoice'

    class Format(str, Enum):
        """
        The phoneme format in which to return the pronunciation. The Arabic, Chinese,
        Dutch, Australian English, and Korean languages support only IPA. Omit the
        parameter to obtain the pronunciation in the default format.
        """
        IBM = 'ibm'
        IPA = 'ipa'


class ListCustomModelsEnums:
    """
    Enums for list_custom_models parameters.
    """

    class Language(str, Enum):
        """
        The language for which custom models that are owned by the requesting credentials
        are to be returned. Omit the parameter to see all custom models that are owned by
        the requester.
        """
        AR_MS = 'ar-MS'
        CS_CZ = 'cs-CZ'
        DE_DE = 'de-DE'
        EN_AU = 'en-AU'
        EN_GB = 'en-GB'
        EN_US = 'en-US'
        ES_ES = 'es-ES'
        ES_LA = 'es-LA'
        ES_US = 'es-US'
        FR_CA = 'fr-CA'
        FR_FR = 'fr-FR'
        IT_IT = 'it-IT'
        JA_JP = 'ja-JP'
        KO_KR = 'ko-KR'
        NL_BE = 'nl-BE'
        NL_NL = 'nl-NL'
        PT_BR = 'pt-BR'
        SV_SE = 'sv-SE'
        ZH_CN = 'zh-CN'


##############################################################################
# Models
##############################################################################


class CustomModel():
    """
    Information about an existing custom model.

    :attr str customization_id: The customization ID (GUID) of the custom model. The
          [Create a custom model](#createcustommodel) method returns only this field. It
          does not not return the other fields of this object.
    :attr str name: (optional) The name of the custom model.
    :attr str language: (optional) The language identifier of the custom model (for
          example, `en-US`).
    :attr str owner: (optional) The GUID of the credentials for the instance of the
          service that owns the custom model.
    :attr str created: (optional) The date and time in Coordinated Universal Time
          (UTC) at which the custom model was created. The value is provided in full ISO
          8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str last_modified: (optional) The date and time in Coordinated Universal
          Time (UTC) at which the custom model was last modified. The `created` and
          `updated` fields are equal when a model is first added but has yet to be
          updated. The value is provided in full ISO 8601 format
          (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str description: (optional) The description of the custom model.
    :attr List[Word] words: (optional) An array of `Word` objects that lists the
          words and their translations from the custom model. The words are listed in
          alphabetical order, with uppercase letters listed before lowercase letters. The
          array is empty if no words are defined for the custom model. This field is
          returned only by the [Get a custom model](#getcustommodel) method.
    :attr List[Prompt] prompts: (optional) An array of `Prompt` objects that
          provides information about the prompts that are defined for the specified custom
          model. The array is empty if no prompts are defined for the custom model. This
          field is returned only by the [Get a custom model](#getcustommodel) method.
    """

    def __init__(self,
                 customization_id: str,
                 *,
                 name: str = None,
                 language: str = None,
                 owner: str = None,
                 created: str = None,
                 last_modified: str = None,
                 description: str = None,
                 words: List['Word'] = None,
                 prompts: List['Prompt'] = None) -> None:
        """
        Initialize a CustomModel object.

        :param str customization_id: The customization ID (GUID) of the custom
               model. The [Create a custom model](#createcustommodel) method returns only
               this field. It does not not return the other fields of this object.
        :param str name: (optional) The name of the custom model.
        :param str language: (optional) The language identifier of the custom model
               (for example, `en-US`).
        :param str owner: (optional) The GUID of the credentials for the instance
               of the service that owns the custom model.
        :param str created: (optional) The date and time in Coordinated Universal
               Time (UTC) at which the custom model was created. The value is provided in
               full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str last_modified: (optional) The date and time in Coordinated
               Universal Time (UTC) at which the custom model was last modified. The
               `created` and `updated` fields are equal when a model is first added but
               has yet to be updated. The value is provided in full ISO 8601 format
               (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str description: (optional) The description of the custom model.
        :param List[Word] words: (optional) An array of `Word` objects that lists
               the words and their translations from the custom model. The words are
               listed in alphabetical order, with uppercase letters listed before
               lowercase letters. The array is empty if no words are defined for the
               custom model. This field is returned only by the [Get a custom
               model](#getcustommodel) method.
        :param List[Prompt] prompts: (optional) An array of `Prompt` objects that
               provides information about the prompts that are defined for the specified
               custom model. The array is empty if no prompts are defined for the custom
               model. This field is returned only by the [Get a custom
               model](#getcustommodel) method.
        """
        self.customization_id = customization_id
        self.name = name
        self.language = language
        self.owner = owner
        self.created = created
        self.last_modified = last_modified
        self.description = description
        self.words = words
        self.prompts = prompts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomModel':
        """Initialize a CustomModel object from a json dictionary."""
        args = {}
        if 'customization_id' in _dict:
            args['customization_id'] = _dict.get('customization_id')
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in CustomModel JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'owner' in _dict:
            args['owner'] = _dict.get('owner')
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'last_modified' in _dict:
            args['last_modified'] = _dict.get('last_modified')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'words' in _dict:
            args['words'] = [Word.from_dict(v) for v in _dict.get('words')]
        if 'prompts' in _dict:
            args['prompts'] = [
                Prompt.from_dict(v) for v in _dict.get('prompts')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'customization_id') and self.customization_id is not None:
            _dict['customization_id'] = self.customization_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'last_modified') and self.last_modified is not None:
            _dict['last_modified'] = self.last_modified
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'words') and self.words is not None:
            words_list = []
            for v in self.words:
                if isinstance(v, dict):
                    words_list.append(v)
                else:
                    words_list.append(v.to_dict())
            _dict['words'] = words_list
        if hasattr(self, 'prompts') and self.prompts is not None:
            prompts_list = []
            for v in self.prompts:
                if isinstance(v, dict):
                    prompts_list.append(v)
                else:
                    prompts_list.append(v.to_dict())
            _dict['prompts'] = prompts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CustomModels():
    """
    Information about existing custom models.

    :attr List[CustomModel] customizations: An array of `CustomModel` objects that
          provides information about each available custom model. The array is empty if
          the requesting credentials own no custom models (if no language is specified) or
          own no custom models for the specified language.
    """

    def __init__(self, customizations: List['CustomModel']) -> None:
        """
        Initialize a CustomModels object.

        :param List[CustomModel] customizations: An array of `CustomModel` objects
               that provides information about each available custom model. The array is
               empty if the requesting credentials own no custom models (if no language is
               specified) or own no custom models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomModels':
        """Initialize a CustomModels object from a json dictionary."""
        args = {}
        if 'customizations' in _dict:
            args['customizations'] = [
                CustomModel.from_dict(v) for v in _dict.get('customizations')
            ]
        else:
            raise ValueError(
                'Required property \'customizations\' not present in CustomModels JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomModels object from a json dictionary."""
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
        """Return a `str` version of this CustomModels object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomModels') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomModels') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Prompt():
    """
    Information about a custom prompt.

    :attr str prompt: The user-specified text of the prompt.
    :attr str prompt_id: The user-specified identifier (name) of the prompt.
    :attr str status: The status of the prompt:
          * `processing`: The service received the request to add the prompt and is
          analyzing the validity of the prompt.
          * `available`: The service successfully validated the prompt, which is now ready
          for use in a speech synthesis request.
          * `failed`: The service's validation of the prompt failed. The status of the
          prompt includes an `error` field that describes the reason for the failure.
    :attr str error: (optional) If the status of the prompt is `failed`, an error
          message that describes the reason for the failure. The field is omitted if no
          error occurred.
    :attr str speaker_id: (optional) The speaker ID (GUID) of the speaker for which
          the prompt was defined. The field is omitted if no speaker ID was specified.
    """

    def __init__(self,
                 prompt: str,
                 prompt_id: str,
                 status: str,
                 *,
                 error: str = None,
                 speaker_id: str = None) -> None:
        """
        Initialize a Prompt object.

        :param str prompt: The user-specified text of the prompt.
        :param str prompt_id: The user-specified identifier (name) of the prompt.
        :param str status: The status of the prompt:
               * `processing`: The service received the request to add the prompt and is
               analyzing the validity of the prompt.
               * `available`: The service successfully validated the prompt, which is now
               ready for use in a speech synthesis request.
               * `failed`: The service's validation of the prompt failed. The status of
               the prompt includes an `error` field that describes the reason for the
               failure.
        :param str error: (optional) If the status of the prompt is `failed`, an
               error message that describes the reason for the failure. The field is
               omitted if no error occurred.
        :param str speaker_id: (optional) The speaker ID (GUID) of the speaker for
               which the prompt was defined. The field is omitted if no speaker ID was
               specified.
        """
        self.prompt = prompt
        self.prompt_id = prompt_id
        self.status = status
        self.error = error
        self.speaker_id = speaker_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Prompt':
        """Initialize a Prompt object from a json dictionary."""
        args = {}
        if 'prompt' in _dict:
            args['prompt'] = _dict.get('prompt')
        else:
            raise ValueError(
                'Required property \'prompt\' not present in Prompt JSON')
        if 'prompt_id' in _dict:
            args['prompt_id'] = _dict.get('prompt_id')
        else:
            raise ValueError(
                'Required property \'prompt_id\' not present in Prompt JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in Prompt JSON')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        if 'speaker_id' in _dict:
            args['speaker_id'] = _dict.get('speaker_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Prompt object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'prompt') and self.prompt is not None:
            _dict['prompt'] = self.prompt
        if hasattr(self, 'prompt_id') and self.prompt_id is not None:
            _dict['prompt_id'] = self.prompt_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        if hasattr(self, 'speaker_id') and self.speaker_id is not None:
            _dict['speaker_id'] = self.speaker_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Prompt object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Prompt') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Prompt') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PromptMetadata():
    """
    Information about the prompt that is to be added to a custom model. The following
    example of a `PromptMetadata` object includes both the required prompt text and an
    optional speaker model ID:
    `{ "prompt_text": "Thank you and good-bye!", "speaker_id":
    "823068b2-ed4e-11ea-b6e0-7b6456aa95cc" }`.

    :attr str prompt_text: The required written text of the spoken prompt. The
          length of a prompt's text is limited to a few sentences. Speaking one or two
          sentences of text is the recommended limit. A prompt cannot contain more than
          1000 characters of text. Escape any XML control characters (double quotes,
          single quotes, ampersands, angle brackets, and slashes) that appear in the text
          of the prompt.
    :attr str speaker_id: (optional) The optional speaker ID (GUID) of a previously
          defined speaker model that is to be associated with the prompt.
    """

    def __init__(self, prompt_text: str, *, speaker_id: str = None) -> None:
        """
        Initialize a PromptMetadata object.

        :param str prompt_text: The required written text of the spoken prompt. The
               length of a prompt's text is limited to a few sentences. Speaking one or
               two sentences of text is the recommended limit. A prompt cannot contain
               more than 1000 characters of text. Escape any XML control characters
               (double quotes, single quotes, ampersands, angle brackets, and slashes)
               that appear in the text of the prompt.
        :param str speaker_id: (optional) The optional speaker ID (GUID) of a
               previously defined speaker model that is to be associated with the prompt.
        """
        self.prompt_text = prompt_text
        self.speaker_id = speaker_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PromptMetadata':
        """Initialize a PromptMetadata object from a json dictionary."""
        args = {}
        if 'prompt_text' in _dict:
            args['prompt_text'] = _dict.get('prompt_text')
        else:
            raise ValueError(
                'Required property \'prompt_text\' not present in PromptMetadata JSON'
            )
        if 'speaker_id' in _dict:
            args['speaker_id'] = _dict.get('speaker_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PromptMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'prompt_text') and self.prompt_text is not None:
            _dict['prompt_text'] = self.prompt_text
        if hasattr(self, 'speaker_id') and self.speaker_id is not None:
            _dict['speaker_id'] = self.speaker_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PromptMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PromptMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PromptMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Prompts():
    """
    Information about the custom prompts that are defined for a custom model.

    :attr List[Prompt] prompts: An array of `Prompt` objects that provides
          information about the prompts that are defined for the specified custom model.
          The array is empty if no prompts are defined for the custom model.
    """

    def __init__(self, prompts: List['Prompt']) -> None:
        """
        Initialize a Prompts object.

        :param List[Prompt] prompts: An array of `Prompt` objects that provides
               information about the prompts that are defined for the specified custom
               model. The array is empty if no prompts are defined for the custom model.
        """
        self.prompts = prompts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Prompts':
        """Initialize a Prompts object from a json dictionary."""
        args = {}
        if 'prompts' in _dict:
            args['prompts'] = [
                Prompt.from_dict(v) for v in _dict.get('prompts')
            ]
        else:
            raise ValueError(
                'Required property \'prompts\' not present in Prompts JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Prompts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'prompts') and self.prompts is not None:
            prompts_list = []
            for v in self.prompts:
                if isinstance(v, dict):
                    prompts_list.append(v)
                else:
                    prompts_list.append(v.to_dict())
            _dict['prompts'] = prompts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Prompts object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Prompts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Prompts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Pronunciation():
    """
    The pronunciation of the specified text.

    :attr str pronunciation: The pronunciation of the specified text in the
          requested voice and format. If a custom model is specified, the pronunciation
          also reflects that custom model.
    """

    def __init__(self, pronunciation: str) -> None:
        """
        Initialize a Pronunciation object.

        :param str pronunciation: The pronunciation of the specified text in the
               requested voice and format. If a custom model is specified, the
               pronunciation also reflects that custom model.
        """
        self.pronunciation = pronunciation

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pronunciation':
        """Initialize a Pronunciation object from a json dictionary."""
        args = {}
        if 'pronunciation' in _dict:
            args['pronunciation'] = _dict.get('pronunciation')
        else:
            raise ValueError(
                'Required property \'pronunciation\' not present in Pronunciation JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pronunciation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pronunciation') and self.pronunciation is not None:
            _dict['pronunciation'] = self.pronunciation
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pronunciation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Pronunciation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pronunciation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Speaker():
    """
    Information about a speaker model.

    :attr str speaker_id: The speaker ID (GUID) of the speaker.
    :attr str name: The user-defined name of the speaker.
    """

    def __init__(self, speaker_id: str, name: str) -> None:
        """
        Initialize a Speaker object.

        :param str speaker_id: The speaker ID (GUID) of the speaker.
        :param str name: The user-defined name of the speaker.
        """
        self.speaker_id = speaker_id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Speaker':
        """Initialize a Speaker object from a json dictionary."""
        args = {}
        if 'speaker_id' in _dict:
            args['speaker_id'] = _dict.get('speaker_id')
        else:
            raise ValueError(
                'Required property \'speaker_id\' not present in Speaker JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Speaker JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Speaker object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'speaker_id') and self.speaker_id is not None:
            _dict['speaker_id'] = self.speaker_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Speaker object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Speaker') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Speaker') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeakerCustomModel():
    """
    A custom models for which the speaker has defined prompts.

    :attr str customization_id: The customization ID (GUID) of a custom model for
          which the speaker has defined one or more prompts.
    :attr List[SpeakerPrompt] prompts: An array of `SpeakerPrompt` objects that
          provides information about each prompt that the user has defined for the custom
          model.
    """

    def __init__(self, customization_id: str,
                 prompts: List['SpeakerPrompt']) -> None:
        """
        Initialize a SpeakerCustomModel object.

        :param str customization_id: The customization ID (GUID) of a custom model
               for which the speaker has defined one or more prompts.
        :param List[SpeakerPrompt] prompts: An array of `SpeakerPrompt` objects
               that provides information about each prompt that the user has defined for
               the custom model.
        """
        self.customization_id = customization_id
        self.prompts = prompts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeakerCustomModel':
        """Initialize a SpeakerCustomModel object from a json dictionary."""
        args = {}
        if 'customization_id' in _dict:
            args['customization_id'] = _dict.get('customization_id')
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in SpeakerCustomModel JSON'
            )
        if 'prompts' in _dict:
            args['prompts'] = [
                SpeakerPrompt.from_dict(v) for v in _dict.get('prompts')
            ]
        else:
            raise ValueError(
                'Required property \'prompts\' not present in SpeakerCustomModel JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeakerCustomModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'customization_id') and self.customization_id is not None:
            _dict['customization_id'] = self.customization_id
        if hasattr(self, 'prompts') and self.prompts is not None:
            prompts_list = []
            for v in self.prompts:
                if isinstance(v, dict):
                    prompts_list.append(v)
                else:
                    prompts_list.append(v.to_dict())
            _dict['prompts'] = prompts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeakerCustomModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeakerCustomModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeakerCustomModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeakerCustomModels():
    """
    Custom models for which the speaker has defined prompts.

    :attr List[SpeakerCustomModel] customizations: An array of `SpeakerCustomModel`
          objects. Each object provides information about the prompts that are defined for
          a specified speaker in the custom models that are owned by a specified service
          instance. The array is empty if no prompts are defined for the speaker.
    """

    def __init__(self, customizations: List['SpeakerCustomModel']) -> None:
        """
        Initialize a SpeakerCustomModels object.

        :param List[SpeakerCustomModel] customizations: An array of
               `SpeakerCustomModel` objects. Each object provides information about the
               prompts that are defined for a specified speaker in the custom models that
               are owned by a specified service instance. The array is empty if no prompts
               are defined for the speaker.
        """
        self.customizations = customizations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeakerCustomModels':
        """Initialize a SpeakerCustomModels object from a json dictionary."""
        args = {}
        if 'customizations' in _dict:
            args['customizations'] = [
                SpeakerCustomModel.from_dict(v)
                for v in _dict.get('customizations')
            ]
        else:
            raise ValueError(
                'Required property \'customizations\' not present in SpeakerCustomModels JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeakerCustomModels object from a json dictionary."""
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
        """Return a `str` version of this SpeakerCustomModels object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeakerCustomModels') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeakerCustomModels') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeakerModel():
    """
    The speaker ID of the speaker model.

    :attr str speaker_id: The speaker ID (GUID) of the speaker model.
    """

    def __init__(self, speaker_id: str) -> None:
        """
        Initialize a SpeakerModel object.

        :param str speaker_id: The speaker ID (GUID) of the speaker model.
        """
        self.speaker_id = speaker_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeakerModel':
        """Initialize a SpeakerModel object from a json dictionary."""
        args = {}
        if 'speaker_id' in _dict:
            args['speaker_id'] = _dict.get('speaker_id')
        else:
            raise ValueError(
                'Required property \'speaker_id\' not present in SpeakerModel JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeakerModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'speaker_id') and self.speaker_id is not None:
            _dict['speaker_id'] = self.speaker_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeakerModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeakerModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeakerModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SpeakerPrompt():
    """
    A prompt that a speaker has defined for a custom model.

    :attr str prompt: The user-specified text of the prompt.
    :attr str prompt_id: The user-specified identifier (name) of the prompt.
    :attr str status: The status of the prompt:
          * `processing`: The service received the request to add the prompt and is
          analyzing the validity of the prompt.
          * `available`: The service successfully validated the prompt, which is now ready
          for use in a speech synthesis request.
          * `failed`: The service's validation of the prompt failed. The status of the
          prompt includes an `error` field that describes the reason for the failure.
    :attr str error: (optional) If the status of the prompt is `failed`, an error
          message that describes the reason for the failure. The field is omitted if no
          error occurred.
    """

    def __init__(self,
                 prompt: str,
                 prompt_id: str,
                 status: str,
                 *,
                 error: str = None) -> None:
        """
        Initialize a SpeakerPrompt object.

        :param str prompt: The user-specified text of the prompt.
        :param str prompt_id: The user-specified identifier (name) of the prompt.
        :param str status: The status of the prompt:
               * `processing`: The service received the request to add the prompt and is
               analyzing the validity of the prompt.
               * `available`: The service successfully validated the prompt, which is now
               ready for use in a speech synthesis request.
               * `failed`: The service's validation of the prompt failed. The status of
               the prompt includes an `error` field that describes the reason for the
               failure.
        :param str error: (optional) If the status of the prompt is `failed`, an
               error message that describes the reason for the failure. The field is
               omitted if no error occurred.
        """
        self.prompt = prompt
        self.prompt_id = prompt_id
        self.status = status
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SpeakerPrompt':
        """Initialize a SpeakerPrompt object from a json dictionary."""
        args = {}
        if 'prompt' in _dict:
            args['prompt'] = _dict.get('prompt')
        else:
            raise ValueError(
                'Required property \'prompt\' not present in SpeakerPrompt JSON'
            )
        if 'prompt_id' in _dict:
            args['prompt_id'] = _dict.get('prompt_id')
        else:
            raise ValueError(
                'Required property \'prompt_id\' not present in SpeakerPrompt JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in SpeakerPrompt JSON'
            )
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SpeakerPrompt object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'prompt') and self.prompt is not None:
            _dict['prompt'] = self.prompt
        if hasattr(self, 'prompt_id') and self.prompt_id is not None:
            _dict['prompt_id'] = self.prompt_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SpeakerPrompt object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SpeakerPrompt') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SpeakerPrompt') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Speakers():
    """
    Information about all speaker models for the service instance.

    :attr List[Speaker] speakers: An array of `Speaker` objects that provides
          information about the speakers for the service instance. The array is empty if
          the service instance has no speakers.
    """

    def __init__(self, speakers: List['Speaker']) -> None:
        """
        Initialize a Speakers object.

        :param List[Speaker] speakers: An array of `Speaker` objects that provides
               information about the speakers for the service instance. The array is empty
               if the service instance has no speakers.
        """
        self.speakers = speakers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Speakers':
        """Initialize a Speakers object from a json dictionary."""
        args = {}
        if 'speakers' in _dict:
            args['speakers'] = [
                Speaker.from_dict(v) for v in _dict.get('speakers')
            ]
        else:
            raise ValueError(
                'Required property \'speakers\' not present in Speakers JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Speakers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'speakers') and self.speakers is not None:
            speakers_list = []
            for v in self.speakers:
                if isinstance(v, dict):
                    speakers_list.append(v)
                else:
                    speakers_list.append(v.to_dict())
            _dict['speakers'] = speakers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Speakers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Speakers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Speakers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SupportedFeatures():
    """
    Additional service features that are supported with the voice.

    :attr bool custom_pronunciation: If `true`, the voice can be customized; if
          `false`, the voice cannot be customized. (Same as `customizable`.).
    :attr bool voice_transformation: If `true`, the voice can be transformed by
          using the SSML &lt;voice-transformation&gt; element; if `false`, the voice
          cannot be transformed. The feature was available only for the now-deprecated
          standard voices. You cannot use the feature with neural voices.
    """

    def __init__(self, custom_pronunciation: bool,
                 voice_transformation: bool) -> None:
        """
        Initialize a SupportedFeatures object.

        :param bool custom_pronunciation: If `true`, the voice can be customized;
               if `false`, the voice cannot be customized. (Same as `customizable`.).
        :param bool voice_transformation: If `true`, the voice can be transformed
               by using the SSML &lt;voice-transformation&gt; element; if `false`, the
               voice cannot be transformed. The feature was available only for the
               now-deprecated standard voices. You cannot use the feature with neural
               voices.
        """
        self.custom_pronunciation = custom_pronunciation
        self.voice_transformation = voice_transformation

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SupportedFeatures':
        """Initialize a SupportedFeatures object from a json dictionary."""
        args = {}
        if 'custom_pronunciation' in _dict:
            args['custom_pronunciation'] = _dict.get('custom_pronunciation')
        else:
            raise ValueError(
                'Required property \'custom_pronunciation\' not present in SupportedFeatures JSON'
            )
        if 'voice_transformation' in _dict:
            args['voice_transformation'] = _dict.get('voice_transformation')
        else:
            raise ValueError(
                'Required property \'voice_transformation\' not present in SupportedFeatures JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SupportedFeatures object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_pronunciation'
                  ) and self.custom_pronunciation is not None:
            _dict['custom_pronunciation'] = self.custom_pronunciation
        if hasattr(self, 'voice_transformation'
                  ) and self.voice_transformation is not None:
            _dict['voice_transformation'] = self.voice_transformation
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


class Translation():
    """
    Information about the translation for the specified text.

    :attr str translation: The phonetic or sounds-like translation for the word. A
          phonetic translation is based on the SSML format for representing the phonetic
          string of a word either as an IPA translation or as an IBM SPR translation. The
          Arabic, Chinese, Dutch, Australian English, and Korean languages support only
          IPA. A sounds-like is one or more words that, when combined, sound like the
          word.
    :attr str part_of_speech: (optional) **Japanese only.** The part of speech for
          the word. The service uses the value to produce the correct intonation for the
          word. You can create only a single entry, with or without a single part of
          speech, for any word; you cannot create multiple entries with different parts of
          speech for the same word. For more information, see [Working with Japanese
          entries](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-rules#jaNotes).
    """

    def __init__(self, translation: str, *, part_of_speech: str = None) -> None:
        """
        Initialize a Translation object.

        :param str translation: The phonetic or sounds-like translation for the
               word. A phonetic translation is based on the SSML format for representing
               the phonetic string of a word either as an IPA translation or as an IBM SPR
               translation. The Arabic, Chinese, Dutch, Australian English, and Korean
               languages support only IPA. A sounds-like is one or more words that, when
               combined, sound like the word.
        :param str part_of_speech: (optional) **Japanese only.** The part of speech
               for the word. The service uses the value to produce the correct intonation
               for the word. You can create only a single entry, with or without a single
               part of speech, for any word; you cannot create multiple entries with
               different parts of speech for the same word. For more information, see
               [Working with Japanese
               entries](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-rules#jaNotes).
        """
        self.translation = translation
        self.part_of_speech = part_of_speech

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Translation':
        """Initialize a Translation object from a json dictionary."""
        args = {}
        if 'translation' in _dict:
            args['translation'] = _dict.get('translation')
        else:
            raise ValueError(
                'Required property \'translation\' not present in Translation JSON'
            )
        if 'part_of_speech' in _dict:
            args['part_of_speech'] = _dict.get('part_of_speech')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Translation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'translation') and self.translation is not None:
            _dict['translation'] = self.translation
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Translation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Translation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Translation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PartOfSpeechEnum(str, Enum):
        """
        **Japanese only.** The part of speech for the word. The service uses the value to
        produce the correct intonation for the word. You can create only a single entry,
        with or without a single part of speech, for any word; you cannot create multiple
        entries with different parts of speech for the same word. For more information,
        see [Working with Japanese
        entries](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-rules#jaNotes).
        """
        DOSI = 'Dosi'
        FUKU = 'Fuku'
        GOBI = 'Gobi'
        HOKA = 'Hoka'
        JODO = 'Jodo'
        JOSI = 'Josi'
        KATO = 'Kato'
        KEDO = 'Kedo'
        KEYO = 'Keyo'
        KIGO = 'Kigo'
        KOYU = 'Koyu'
        MESI = 'Mesi'
        RETA = 'Reta'
        STBI = 'Stbi'
        STTO = 'Stto'
        STZO = 'Stzo'
        SUJI = 'Suji'


class Voice():
    """
    Information about an available voice.

    :attr str url: The URI of the voice.
    :attr str gender: The gender of the voice: `male` or `female`.
    :attr str name: The name of the voice. Use this as the voice identifier in all
          requests.
    :attr str language: The language and region of the voice (for example, `en-US`).
    :attr str description: A textual description of the voice.
    :attr bool customizable: If `true`, the voice can be customized; if `false`, the
          voice cannot be customized. (Same as `custom_pronunciation`; maintained for
          backward compatibility.).
    :attr SupportedFeatures supported_features: Additional service features that are
          supported with the voice.
    :attr CustomModel customization: (optional) Returns information about a
          specified custom model. This field is returned only by the [Get a
          voice](#getvoice) method and only when you specify the customization ID of a
          custom model.
    """

    def __init__(self,
                 url: str,
                 gender: str,
                 name: str,
                 language: str,
                 description: str,
                 customizable: bool,
                 supported_features: 'SupportedFeatures',
                 *,
                 customization: 'CustomModel' = None) -> None:
        """
        Initialize a Voice object.

        :param str url: The URI of the voice.
        :param str gender: The gender of the voice: `male` or `female`.
        :param str name: The name of the voice. Use this as the voice identifier in
               all requests.
        :param str language: The language and region of the voice (for example,
               `en-US`).
        :param str description: A textual description of the voice.
        :param bool customizable: If `true`, the voice can be customized; if
               `false`, the voice cannot be customized. (Same as `custom_pronunciation`;
               maintained for backward compatibility.).
        :param SupportedFeatures supported_features: Additional service features
               that are supported with the voice.
        :param CustomModel customization: (optional) Returns information about a
               specified custom model. This field is returned only by the [Get a
               voice](#getvoice) method and only when you specify the customization ID of
               a custom model.
        """
        self.url = url
        self.gender = gender
        self.name = name
        self.language = language
        self.description = description
        self.customizable = customizable
        self.supported_features = supported_features
        self.customization = customization

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Voice':
        """Initialize a Voice object from a json dictionary."""
        args = {}
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in Voice JSON')
        if 'gender' in _dict:
            args['gender'] = _dict.get('gender')
        else:
            raise ValueError(
                'Required property \'gender\' not present in Voice JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Voice JSON')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in Voice JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError(
                'Required property \'description\' not present in Voice JSON')
        if 'customizable' in _dict:
            args['customizable'] = _dict.get('customizable')
        else:
            raise ValueError(
                'Required property \'customizable\' not present in Voice JSON')
        if 'supported_features' in _dict:
            args['supported_features'] = SupportedFeatures.from_dict(
                _dict.get('supported_features'))
        else:
            raise ValueError(
                'Required property \'supported_features\' not present in Voice JSON'
            )
        if 'customization' in _dict:
            args['customization'] = CustomModel.from_dict(
                _dict.get('customization'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Voice object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'gender') and self.gender is not None:
            _dict['gender'] = self.gender
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'customizable') and self.customizable is not None:
            _dict['customizable'] = self.customizable
        if hasattr(
                self,
                'supported_features') and self.supported_features is not None:
            if isinstance(self.supported_features, dict):
                _dict['supported_features'] = self.supported_features
            else:
                _dict['supported_features'] = self.supported_features.to_dict()
        if hasattr(self, 'customization') and self.customization is not None:
            if isinstance(self.customization, dict):
                _dict['customization'] = self.customization
            else:
                _dict['customization'] = self.customization.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Voice object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Voice') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Voice') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Voices():
    """
    Information about all available voices.

    :attr List[Voice] voices: A list of available voices.
    """

    def __init__(self, voices: List['Voice']) -> None:
        """
        Initialize a Voices object.

        :param List[Voice] voices: A list of available voices.
        """
        self.voices = voices

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Voices':
        """Initialize a Voices object from a json dictionary."""
        args = {}
        if 'voices' in _dict:
            args['voices'] = [Voice.from_dict(v) for v in _dict.get('voices')]
        else:
            raise ValueError(
                'Required property \'voices\' not present in Voices JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Voices object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'voices') and self.voices is not None:
            voices_list = []
            for v in self.voices:
                if isinstance(v, dict):
                    voices_list.append(v)
                else:
                    voices_list.append(v.to_dict())
            _dict['voices'] = voices_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Voices object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Voices') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Voices') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Word():
    """
    Information about a word for the custom model.

    :attr str word: The word for the custom model. The maximum length of a word is
          49 characters.
    :attr str translation: The phonetic or sounds-like translation for the word. A
          phonetic translation is based on the SSML format for representing the phonetic
          string of a word either as an IPA or IBM SPR translation. The Arabic, Chinese,
          Dutch, Australian English, and Korean languages support only IPA. A sounds-like
          translation consists of one or more words that, when combined, sound like the
          word. The maximum length of a translation is 499 characters.
    :attr str part_of_speech: (optional) **Japanese only.** The part of speech for
          the word. The service uses the value to produce the correct intonation for the
          word. You can create only a single entry, with or without a single part of
          speech, for any word; you cannot create multiple entries with different parts of
          speech for the same word. For more information, see [Working with Japanese
          entries](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-rules#jaNotes).
    """

    def __init__(self,
                 word: str,
                 translation: str,
                 *,
                 part_of_speech: str = None) -> None:
        """
        Initialize a Word object.

        :param str word: The word for the custom model. The maximum length of a
               word is 49 characters.
        :param str translation: The phonetic or sounds-like translation for the
               word. A phonetic translation is based on the SSML format for representing
               the phonetic string of a word either as an IPA or IBM SPR translation. The
               Arabic, Chinese, Dutch, Australian English, and Korean languages support
               only IPA. A sounds-like translation consists of one or more words that,
               when combined, sound like the word. The maximum length of a translation is
               499 characters.
        :param str part_of_speech: (optional) **Japanese only.** The part of speech
               for the word. The service uses the value to produce the correct intonation
               for the word. You can create only a single entry, with or without a single
               part of speech, for any word; you cannot create multiple entries with
               different parts of speech for the same word. For more information, see
               [Working with Japanese
               entries](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-rules#jaNotes).
        """
        self.word = word
        self.translation = translation
        self.part_of_speech = part_of_speech

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Word':
        """Initialize a Word object from a json dictionary."""
        args = {}
        if 'word' in _dict:
            args['word'] = _dict.get('word')
        else:
            raise ValueError(
                'Required property \'word\' not present in Word JSON')
        if 'translation' in _dict:
            args['translation'] = _dict.get('translation')
        else:
            raise ValueError(
                'Required property \'translation\' not present in Word JSON')
        if 'part_of_speech' in _dict:
            args['part_of_speech'] = _dict.get('part_of_speech')
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
        if hasattr(self, 'translation') and self.translation is not None:
            _dict['translation'] = self.translation
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
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

    class PartOfSpeechEnum(str, Enum):
        """
        **Japanese only.** The part of speech for the word. The service uses the value to
        produce the correct intonation for the word. You can create only a single entry,
        with or without a single part of speech, for any word; you cannot create multiple
        entries with different parts of speech for the same word. For more information,
        see [Working with Japanese
        entries](https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-rules#jaNotes).
        """
        DOSI = 'Dosi'
        FUKU = 'Fuku'
        GOBI = 'Gobi'
        HOKA = 'Hoka'
        JODO = 'Jodo'
        JOSI = 'Josi'
        KATO = 'Kato'
        KEDO = 'Kedo'
        KEYO = 'Keyo'
        KIGO = 'Kigo'
        KOYU = 'Koyu'
        MESI = 'Mesi'
        RETA = 'Reta'
        STBI = 'Stbi'
        STTO = 'Stto'
        STZO = 'Stzo'
        SUJI = 'Suji'


class Words():
    """
    For the [Add custom words](#addwords) method, one or more words that are to be added
    or updated for the custom model and the translation for each specified word.
    For the [List custom words](#listwords) method, the words and their translations from
    the custom model.

    :attr List[Word] words: The [Add custom words](#addwords) method accepts an
          array of `Word` objects. Each object provides a word that is to be added or
          updated for the custom model and the word's translation.
          The [List custom words](#listwords) method returns an array of `Word` objects.
          Each object shows a word and its translation from the custom model. The words
          are listed in alphabetical order, with uppercase letters listed before lowercase
          letters. The array is empty if the custom model contains no words.
    """

    def __init__(self, words: List['Word']) -> None:
        """
        Initialize a Words object.

        :param List[Word] words: The [Add custom words](#addwords) method accepts
               an array of `Word` objects. Each object provides a word that is to be added
               or updated for the custom model and the word's translation.
               The [List custom words](#listwords) method returns an array of `Word`
               objects. Each object shows a word and its translation from the custom
               model. The words are listed in alphabetical order, with uppercase letters
               listed before lowercase letters. The array is empty if the custom model
               contains no words.
        """
        self.words = words

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Words':
        """Initialize a Words object from a json dictionary."""
        args = {}
        if 'words' in _dict:
            args['words'] = [Word.from_dict(v) for v in _dict.get('words')]
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
