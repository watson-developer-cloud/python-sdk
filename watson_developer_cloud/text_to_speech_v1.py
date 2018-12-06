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
The IBM&reg; Text to Speech service provides APIs that use IBM's speech-synthesis
capabilities to synthesize text into natural-sounding speech in a variety of languages,
dialects, and voices. The service supports at least one male or female voice, sometimes
both, for each language. The audio is streamed back to the client with minimal delay.
For speech synthesis, the service supports a synchronous HTTP Representational State
Transfer (REST) interface. It also supports a WebSocket interface that provides both plain
text and SSML input, including the SSML &lt;mark&gt; element and word timings. SSML is an
XML-based markup language that provides text annotation for speech-synthesis applications.
The service also offers a customization interface. You can use the interface to define
sounds-like or phonetic translations for words. A sounds-like translation consists of one
or more words that, when combined, sound like the word. A phonetic translation is based on
the SSML phoneme format for representing a word. You can specify a phonetic translation in
standard International Phonetic Alphabet (IPA) representation or in the proprietary IBM
Symbolic Phonetic Representation (SPR).
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class TextToSpeechV1(WatsonService):
    """The Text to Speech V1 service."""

    default_url = 'https://stream.watsonplatform.net/text-to-speech/api'

    def __init__(
            self,
            url=default_url,
            username=None,
            password=None,
            iam_apikey=None,
            iam_access_token=None,
            iam_url=None,
    ):
        """
        Construct a new client for the Text to Speech service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://stream.watsonplatform.net/text-to-speech/api").
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

        :param str iam_apikey: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.bluemix.net/identity/token'.
        """

        WatsonService.__init__(
            self,
            vcap_services_name='text_to_speech',
            url=url,
            username=username,
            password=password,
            iam_apikey=iam_apikey,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)

    #########################
    # Voices
    #########################

    def get_voice(self, voice, customization_id=None, **kwargs):
        """
        Get a voice.

        Gets information about the specified voice. The information includes the name,
        language, gender, and other details about the voice. Specify a customization ID to
        obtain information for that custom voice model of the specified voice. To list
        information about all available voices, use the **List voices** method.
        **See also:** [Specifying a
        voice](/docs/services/text-to-speech/http.html#voices).

        :param str voice: The voice for which information is to be returned.
        :param str customization_id: The customization ID (GUID) of a custom voice model
        for which information is to be returned. You must make the request with service
        credentials created for the instance of the service that owns the custom model.
        Omit the parameter to see information about the specified voice with no
        customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if voice is None:
            raise ValueError('voice must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {'customization_id': customization_id}

        url = '/v1/voices/{0}'.format(*self._encode_path_vars(voice))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_voices(self, **kwargs):
        """
        List voices.

        Lists all voices available for use with the service. The information includes the
        name, language, gender, and other details about the voice. To see information
        about a specific voice, use the **Get a voice** method.
        **See also:** [Specifying a
        voice](/docs/services/text-to-speech/http.html#voices).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/voices'
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    #########################
    # Synthesis
    #########################

    def synthesize(self,
                   text,
                   accept=None,
                   voice=None,
                   customization_id=None,
                   **kwargs):
        """
        Synthesize audio.

        Synthesizes text to audio that is spoken in the specified voice. The service bases
        its understanding of the language for the input text on the specified voice. Use a
        voice that matches the language of the input text.
        The service returns the synthesized audio stream as an array of bytes. You can
        pass a maximum of 5 KB of text to the service.
        **See also:** [Synthesizing text to
        audio](/docs/services/text-to-speech/http.html#synthesize).
        ### Audio formats (accept types)
         The service can return audio in the following formats (MIME types).
        * Where indicated, you can optionally specify the sampling rate (`rate`) of the
        audio. You must specify a sampling rate for the `audio/l16` and `audio/mulaw`
        formats. A specified sampling rate must lie in the range of 8 kHz to 192 kHz.
        * For the `audio/l16` format, you can optionally specify the endianness
        (`endianness`) of the audio: `endianness=big-endian` or
        `endianness=little-endian`.
        Use the `Accept` header or the `accept` parameter to specify the requested format
        of the response audio. If you omit an audio format altogether, the service returns
        the audio in Ogg format with the Opus codec (`audio/ogg;codecs=opus`). The service
        always returns single-channel audio.
        * `audio/basic`
          The service returns audio with a sampling rate of 8000 Hz.
        * `audio/flac`
          You can optionally specify the `rate` of the audio. The default sampling rate is
        22,050 Hz.
        * `audio/l16`
          You must specify the `rate` of the audio. You can optionally specify the
        `endianness` of the audio. The default endianness is `little-endian`.
        * `audio/mp3`
          You can optionally specify the `rate` of the audio. The default sampling rate is
        22,050 Hz.
        * `audio/mpeg`
          You can optionally specify the `rate` of the audio. The default sampling rate is
        22,050 Hz.
        * `audio/mulaw`
          You must specify the `rate` of the audio.
        * `audio/ogg`
          The service returns the audio in the `vorbis` codec. You can optionally specify
        the `rate` of the audio. The default sampling rate is 22,050 Hz.
        * `audio/ogg;codecs=opus`
          You can optionally specify the `rate` of the audio. The default sampling rate is
        22,050 Hz.
        * `audio/ogg;codecs=vorbis`
          You can optionally specify the `rate` of the audio. The default sampling rate is
        22,050 Hz.
        * `audio/wav`
          You can optionally specify the `rate` of the audio. The default sampling rate is
        22,050 Hz.
        * `audio/webm`
          The service returns the audio in the `opus` codec. The service returns audio
        with a sampling rate of 48,000 Hz.
        * `audio/webm;codecs=opus`
          The service returns audio with a sampling rate of 48,000 Hz.
        * `audio/webm;codecs=vorbis`
          You can optionally specify the `rate` of the audio. The default sampling rate is
        22,050 Hz.
        For more information about specifying an audio format, including additional
        details about some of the formats, see [Specifying an audio
        format](/docs/services/text-to-speech/http.html#format).
        ### Warning messages
         If a request includes invalid query parameters, the service returns a `Warnings`
        response header that provides messages about the invalid parameters. The warning
        includes a descriptive message and a list of invalid argument strings. For
        example, a message such as `\"Unknown arguments:\"` or `\"Unknown url query
        arguments:\"` followed by a list of the form `\"{invalid_arg_1},
        {invalid_arg_2}.\"` The request succeeds despite the warnings.

        :param str text: The text to synthesize.
        :param str accept: The requested format (MIME type) of the audio. You can use the
        `Accept` header or the `accept` parameter to specify the audio format. For more
        information about specifying an audio format, see **Audio formats (accept types)**
        in the method description.
        Default: `audio/ogg;codecs=opus`.
        :param str voice: The voice to use for synthesis.
        :param str customization_id: The customization ID (GUID) of a custom voice model
        to use for the synthesis. If a custom voice model is specified, it is guaranteed
        to work only if it matches the language of the indicated voice. You must make the
        request with service credentials created for the instance of the service that owns
        the custom model. Omit the parameter to use the specified voice with no
        customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if text is None:
            raise ValueError('text must be provided')

        headers = {'Accept': accept}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {'voice': voice, 'customization_id': customization_id}

        data = {'text': text}

        url = '/v1/synthesize'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=False)
        return response

    #########################
    # Pronunciation
    #########################

    def get_pronunciation(self,
                          text,
                          voice=None,
                          format=None,
                          customization_id=None,
                          **kwargs):
        """
        Get pronunciation.

        Gets the phonetic pronunciation for the specified word. You can request the
        pronunciation for a specific format. You can also request the pronunciation for a
        specific voice to see the default translation for the language of that voice or
        for a specific custom voice model to see the translation for that voice model.
        **Note:** This method is currently a beta release.
        **See also:** [Querying a word from a
        language](/docs/services/text-to-speech/custom-entries.html#cuWordsQueryLanguage).

        :param str text: The word for which the pronunciation is requested.
        :param str voice: A voice that specifies the language in which the pronunciation
        is to be returned. All voices for the same language (for example, `en-US`) return
        the same translation.
        :param str format: The phoneme format in which to return the pronunciation. Omit
        the parameter to obtain the pronunciation in the default format.
        :param str customization_id: The customization ID (GUID) of a custom voice model
        for which the pronunciation is to be returned. The language of a specified custom
        model must match the language of the specified voice. If the word is not defined
        in the specified custom model, the service returns the default translation for the
        custom model's language. You must make the request with service credentials
        created for the instance of the service that owns the custom model. Omit the
        parameter to see the translation for the specified voice with no customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {
            'text': text,
            'voice': voice,
            'format': format,
            'customization_id': customization_id
        }

        url = '/v1/pronunciation'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    #########################
    # Custom models
    #########################

    def create_voice_model(self,
                           name,
                           language=None,
                           description=None,
                           **kwargs):
        """
        Create a custom model.

        Creates a new empty custom voice model. You must specify a name for the new custom
        model. You can optionally specify the language and a description for the new
        model. The model is owned by the instance of the service whose credentials are
        used to create it.
        **Note:** This method is currently a beta release.
        **See also:** [Creating a custom
        model](/docs/services/text-to-speech/custom-models.html#cuModelsCreate).

        :param str name: The name of the new custom voice model.
        :param str language: The language of the new custom voice model. Omit the
        parameter to use the the default language, `en-US`.
        :param str description: A description of the new custom voice model. Specifying a
        description is recommended.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        data = {'name': name, 'language': language, 'description': description}

        url = '/v1/customizations'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return response

    def delete_voice_model(self, customization_id, **kwargs):
        """
        Delete a custom model.

        Deletes the specified custom voice model. You must use credentials for the
        instance of the service that owns a model to delete it.
        **Note:** This method is currently a beta release.
        **See also:** [Deleting a custom
        model](/docs/services/text-to-speech/custom-models.html#cuModelsDelete).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    def get_voice_model(self, customization_id, **kwargs):
        """
        Get a custom model.

        Gets all information about a specified custom voice model. In addition to metadata
        such as the name and description of the voice model, the output includes the words
        and their translations as defined in the model. To see just the metadata for a
        voice model, use the **List custom models** method.
        **Note:** This method is currently a beta release.
        **See also:** [Querying a custom
        model](/docs/services/text-to-speech/custom-models.html#cuModelsQuery).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
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

    def list_voice_models(self, language=None, **kwargs):
        """
        List custom models.

        Lists metadata such as the name and description for all custom voice models that
        are owned by an instance of the service. Specify a language to list the voice
        models for that language only. To see the words in addition to the metadata for a
        specific voice model, use the **List a custom model** method. You must use
        credentials for the instance of the service that owns a model to list information
        about it.
        **Note:** This method is currently a beta release.
        **See also:** [Querying all custom
        models](/docs/services/text-to-speech/custom-models.html#cuModelsQueryAll).

        :param str language: The language for which custom voice models that are owned by
        the requesting service credentials are to be returned. Omit the parameter to see
        all custom voice models that are owned by the requester.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
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

    def update_voice_model(self,
                           customization_id,
                           name=None,
                           description=None,
                           words=None,
                           **kwargs):
        """
        Update a custom model.

        Updates information for the specified custom voice model. You can update metadata
        such as the name and description of the voice model. You can also update the words
        in the model and their translations. Adding a new translation for a word that
        already exists in a custom model overwrites the word's existing translation. A
        custom model can contain no more than 20,000 entries. You must use credentials for
        the instance of the service that owns a model to update it.
        You can define sounds-like or phonetic translations for words. A sounds-like
        translation consists of one or more words that, when combined, sound like the
        word. Phonetic translations are based on the SSML phoneme format for representing
        a word. You can specify them in standard International Phonetic Alphabet (IPA)
        representation
          <code>&lt;phoneme alphabet=\"ipa\"
        ph=\"t&#601;m&#712;&#593;to\"&gt;&lt;/phoneme&gt;</code>
          or in the proprietary IBM Symbolic Phonetic Representation (SPR)
          <code>&lt;phoneme alphabet=\"ibm\"
        ph=\"1gAstroEntxrYFXs\"&gt;&lt;/phoneme&gt;</code>
        **Note:** This method is currently a beta release.
        **See also:**
        * [Updating a custom
        model](/docs/services/text-to-speech/custom-models.html#cuModelsUpdate)
        * [Adding words to a Japanese custom
        model](/docs/services/text-to-speech/custom-entries.html#cuJapaneseAdd)
        * [Understanding customization](/docs/services/text-to-speech/custom-intro.html).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param str name: A new name for the custom voice model.
        :param str description: A new description for the custom voice model.
        :param list[Word] words: An array of `Word` objects that provides the words and
        their translations that are to be added or updated for the custom voice model.
        Pass an empty array to make no additions or updates.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if words is not None:
            words = [self._convert_model(x, Word) for x in words]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        data = {'name': name, 'description': description, 'words': words}

        url = '/v1/customizations/{0}'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return response

    #########################
    # Custom words
    #########################

    def add_word(self,
                 customization_id,
                 word,
                 translation,
                 part_of_speech=None,
                 **kwargs):
        """
        Add a custom word.

        Adds a single word and its translation to the specified custom voice model. Adding
        a new translation for a word that already exists in a custom model overwrites the
        word's existing translation. A custom model can contain no more than 20,000
        entries. You must use credentials for the instance of the service that owns a
        model to add a word to it.
        You can define sounds-like or phonetic translations for words. A sounds-like
        translation consists of one or more words that, when combined, sound like the
        word. Phonetic translations are based on the SSML phoneme format for representing
        a word. You can specify them in standard International Phonetic Alphabet (IPA)
        representation
          <code>&lt;phoneme alphabet=\"ipa\"
        ph=\"t&#601;m&#712;&#593;to\"&gt;&lt;/phoneme&gt;</code>
          or in the proprietary IBM Symbolic Phonetic Representation (SPR)
          <code>&lt;phoneme alphabet=\"ibm\"
        ph=\"1gAstroEntxrYFXs\"&gt;&lt;/phoneme&gt;</code>
        **Note:** This method is currently a beta release.
        **See also:**
        * [Adding a single word to a custom
        model](/docs/services/text-to-speech/custom-entries.html#cuWordAdd)
        * [Adding words to a Japanese custom
        model](/docs/services/text-to-speech/custom-entries.html#cuJapaneseAdd)
        * [Understanding customization](/docs/services/text-to-speech/custom-intro.html).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param str word: The word that is to be added or updated for the custom voice
        model.
        :param str translation: The phonetic or sounds-like translation for the word. A
        phonetic translation is based on the SSML format for representing the phonetic
        string of a word either as an IPA translation or as an IBM SPR translation. A
        sounds-like is one or more words that, when combined, sound like the word.
        :param str part_of_speech: **Japanese only.** The part of speech for the word. The
        service uses the value to produce the correct intonation for the word. You can
        create only a single entry, with or without a single part of speech, for any word;
        you cannot create multiple entries with different parts of speech for the same
        word. For more information, see [Working with Japanese
        entries](/docs/services/text-to-speech/custom-rules.html#jaNotes).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word is None:
            raise ValueError('word must be provided')
        if translation is None:
            raise ValueError('translation must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        data = {'translation': translation, 'part_of_speech': part_of_speech}

        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word))
        response = self.request(
            method='PUT', url=url, headers=headers, json=data, accept_json=True)
        return response

    def add_words(self, customization_id, words, **kwargs):
        """
        Add custom words.

        Adds one or more words and their translations to the specified custom voice model.
        Adding a new translation for a word that already exists in a custom model
        overwrites the word's existing translation. A custom model can contain no more
        than 20,000 entries. You must use credentials for the instance of the service that
        owns a model to add words to it.
        You can define sounds-like or phonetic translations for words. A sounds-like
        translation consists of one or more words that, when combined, sound like the
        word. Phonetic translations are based on the SSML phoneme format for representing
        a word. You can specify them in standard International Phonetic Alphabet (IPA)
        representation
          <code>&lt;phoneme alphabet=\"ipa\"
        ph=\"t&#601;m&#712;&#593;to\"&gt;&lt;/phoneme&gt;</code>
          or in the proprietary IBM Symbolic Phonetic Representation (SPR)
          <code>&lt;phoneme alphabet=\"ibm\"
        ph=\"1gAstroEntxrYFXs\"&gt;&lt;/phoneme&gt;</code>
        **Note:** This method is currently a beta release.
        **See also:**
        * [Adding multiple words to a custom
        model](/docs/services/text-to-speech/custom-entries.html#cuWordsAdd)
        * [Adding words to a Japanese custom
        model](/docs/services/text-to-speech/custom-entries.html#cuJapaneseAdd)
        * [Understanding customization](/docs/services/text-to-speech/custom-intro.html).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param list[Word] words: The **Add custom words** method accepts an array of
        `Word` objects. Each object provides a word that is to be added or updated for the
        custom voice model and the word's translation.
        The **List custom words** method returns an array of `Word` objects. Each object
        shows a word and its translation from the custom voice model. The words are listed
        in alphabetical order, with uppercase letters listed before lowercase letters. The
        array is empty if the custom model contains no words.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if words is None:
            raise ValueError('words must be provided')
        words = [self._convert_model(x, Word) for x in words]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

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

    def delete_word(self, customization_id, word, **kwargs):
        """
        Delete a custom word.

        Deletes a single word from the specified custom voice model. You must use
        credentials for the instance of the service that owns a model to delete its words.
        **Note:** This method is currently a beta release.
        **See also:** [Deleting a word from a custom
        model](/docs/services/text-to-speech/custom-entries.html#cuWordDelete).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param str word: The word that is to be deleted from the custom voice model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word is None:
            raise ValueError('word must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word))
        response = self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return response

    def get_word(self, customization_id, word, **kwargs):
        """
        Get a custom word.

        Gets the translation for a single word from the specified custom model. The output
        shows the translation as it is defined in the model. You must use credentials for
        the instance of the service that owns a model to list its words.
        **Note:** This method is currently a beta release.
        **See also:** [Querying a single word from a custom
        model](/docs/services/text-to-speech/custom-entries.html#cuWordQueryModel).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param str word: The word that is to be queried from the custom voice model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')
        if word is None:
            raise ValueError('word must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/customizations/{0}/words/{1}'.format(
            *self._encode_path_vars(customization_id, word))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def list_words(self, customization_id, **kwargs):
        """
        List custom words.

        Lists all of the words and their translations for the specified custom voice
        model. The output shows the translations as they are defined in the model. You
        must use credentials for the instance of the service that owns a model to list its
        words.
        **Note:** This method is currently a beta release.
        **See also:** [Querying all words from a custom
        model](/docs/services/text-to-speech/custom-entries.html#cuWordsQueryModel).

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. You must make the request with service credentials created for the instance
        of the service that owns the custom model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customization_id is None:
            raise ValueError('customization_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/customizations/{0}/words'.format(
            *self._encode_path_vars(customization_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
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
        security](/docs/services/text-to-speech/information-security.html).

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

        params = {'customer_id': customer_id}

        url = '/v1/user_data'
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class Pronunciation(object):
    """
    Pronunciation.

    :attr str pronunciation: The pronunciation of the specified text in the requested
    voice and format. If a custom voice model is specified, the pronunciation also
    reflects that custom voice.
    """

    def __init__(self, pronunciation):
        """
        Initialize a Pronunciation object.

        :param str pronunciation: The pronunciation of the specified text in the requested
        voice and format. If a custom voice model is specified, the pronunciation also
        reflects that custom voice.
        """
        self.pronunciation = pronunciation

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pronunciation object from a json dictionary."""
        args = {}
        if 'pronunciation' in _dict:
            args['pronunciation'] = _dict.get('pronunciation')
        else:
            raise ValueError(
                'Required property \'pronunciation\' not present in Pronunciation JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pronunciation') and self.pronunciation is not None:
            _dict['pronunciation'] = self.pronunciation
        return _dict

    def __str__(self):
        """Return a `str` version of this Pronunciation object."""
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
    Describes the additional service features that are supported with the voice.

    :attr bool custom_pronunciation: If `true`, the voice can be customized; if `false`,
    the voice cannot be customized. (Same as `customizable`.).
    :attr bool voice_transformation: If `true`, the voice can be transformed by using the
    SSML &lt;voice-transformation&gt; element; if `false`, the voice cannot be
    transformed.
    """

    def __init__(self, custom_pronunciation, voice_transformation):
        """
        Initialize a SupportedFeatures object.

        :param bool custom_pronunciation: If `true`, the voice can be customized; if
        `false`, the voice cannot be customized. (Same as `customizable`.).
        :param bool voice_transformation: If `true`, the voice can be transformed by using
        the SSML &lt;voice-transformation&gt; element; if `false`, the voice cannot be
        transformed.
        """
        self.custom_pronunciation = custom_pronunciation
        self.voice_transformation = voice_transformation

    @classmethod
    def _from_dict(cls, _dict):
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_pronunciation'
                  ) and self.custom_pronunciation is not None:
            _dict['custom_pronunciation'] = self.custom_pronunciation
        if hasattr(self, 'voice_transformation'
                  ) and self.voice_transformation is not None:
            _dict['voice_transformation'] = self.voice_transformation
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


class Translation(object):
    """
    Translation.

    :attr str translation: The phonetic or sounds-like translation for the word. A
    phonetic translation is based on the SSML format for representing the phonetic string
    of a word either as an IPA translation or as an IBM SPR translation. A sounds-like is
    one or more words that, when combined, sound like the word.
    :attr str part_of_speech: (optional) **Japanese only.** The part of speech for the
    word. The service uses the value to produce the correct intonation for the word. You
    can create only a single entry, with or without a single part of speech, for any word;
    you cannot create multiple entries with different parts of speech for the same word.
    For more information, see [Working with Japanese
    entries](/docs/services/text-to-speech/custom-rules.html#jaNotes).
    """

    def __init__(self, translation, part_of_speech=None):
        """
        Initialize a Translation object.

        :param str translation: The phonetic or sounds-like translation for the word. A
        phonetic translation is based on the SSML format for representing the phonetic
        string of a word either as an IPA translation or as an IBM SPR translation. A
        sounds-like is one or more words that, when combined, sound like the word.
        :param str part_of_speech: (optional) **Japanese only.** The part of speech for
        the word. The service uses the value to produce the correct intonation for the
        word. You can create only a single entry, with or without a single part of speech,
        for any word; you cannot create multiple entries with different parts of speech
        for the same word. For more information, see [Working with Japanese
        entries](/docs/services/text-to-speech/custom-rules.html#jaNotes).
        """
        self.translation = translation
        self.part_of_speech = part_of_speech

    @classmethod
    def _from_dict(cls, _dict):
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'translation') and self.translation is not None:
            _dict['translation'] = self.translation
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
        return _dict

    def __str__(self):
        """Return a `str` version of this Translation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Voice(object):
    """
    Voice.

    :attr str url: The URI of the voice.
    :attr str gender: The gender of the voice: `male` or `female`.
    :attr str name: The name of the voice. Use this as the voice identifier in all
    requests.
    :attr str language: The language and region of the voice (for example, `en-US`).
    :attr str description: A textual description of the voice.
    :attr bool customizable: If `true`, the voice can be customized; if `false`, the voice
    cannot be customized. (Same as `custom_pronunciation`; maintained for backward
    compatibility.).
    :attr SupportedFeatures supported_features: Describes the additional service features
    that are supported with the voice.
    :attr VoiceModel customization: (optional) Returns information about a specified
    custom voice model. This field is returned only by the **Get a voice** method and only
    when you specify the customization ID of a custom voice model.
    """

    def __init__(self,
                 url,
                 gender,
                 name,
                 language,
                 description,
                 customizable,
                 supported_features,
                 customization=None):
        """
        Initialize a Voice object.

        :param str url: The URI of the voice.
        :param str gender: The gender of the voice: `male` or `female`.
        :param str name: The name of the voice. Use this as the voice identifier in all
        requests.
        :param str language: The language and region of the voice (for example, `en-US`).
        :param str description: A textual description of the voice.
        :param bool customizable: If `true`, the voice can be customized; if `false`, the
        voice cannot be customized. (Same as `custom_pronunciation`; maintained for
        backward compatibility.).
        :param SupportedFeatures supported_features: Describes the additional service
        features that are supported with the voice.
        :param VoiceModel customization: (optional) Returns information about a specified
        custom voice model. This field is returned only by the **Get a voice** method and
        only when you specify the customization ID of a custom voice model.
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
    def _from_dict(cls, _dict):
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
            args['supported_features'] = SupportedFeatures._from_dict(
                _dict.get('supported_features'))
        else:
            raise ValueError(
                'Required property \'supported_features\' not present in Voice JSON'
            )
        if 'customization' in _dict:
            args['customization'] = VoiceModel._from_dict(
                _dict.get('customization'))
        return cls(**args)

    def _to_dict(self):
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
            _dict['supported_features'] = self.supported_features._to_dict()
        if hasattr(self, 'customization') and self.customization is not None:
            _dict['customization'] = self.customization._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this Voice object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VoiceModel(object):
    """
    VoiceModel.

    :attr str customization_id: The customization ID (GUID) of the custom voice model. The
    **Create a custom model** method returns only this field. It does not not return the
    other fields of this object.
    :attr str name: (optional) The name of the custom voice model.
    :attr str language: (optional) The language identifier of the custom voice model (for
    example, `en-US`).
    :attr str owner: (optional) The GUID of the service credentials for the instance of
    the service that owns the custom voice model.
    :attr str created: (optional) The date and time in Coordinated Universal Time (UTC) at
    which the custom voice model was created. The value is provided in full ISO 8601
    format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str last_modified: (optional) The date and time in Coordinated Universal Time
    (UTC) at which the custom voice model was last modified. Equals `created` when a new
    voice model is first added but has yet to be updated. The value is provided in full
    ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str description: (optional) The description of the custom voice model.
    :attr list[Word] words: (optional) An array of `Word` objects that lists the words and
    their translations from the custom voice model. The words are listed in alphabetical
    order, with uppercase letters listed before lowercase letters. The array is empty if
    the custom model contains no words. This field is returned only by the **Get a voice**
    method and only when you specify the customization ID of a custom voice model.
    """

    def __init__(self,
                 customization_id,
                 name=None,
                 language=None,
                 owner=None,
                 created=None,
                 last_modified=None,
                 description=None,
                 words=None):
        """
        Initialize a VoiceModel object.

        :param str customization_id: The customization ID (GUID) of the custom voice
        model. The **Create a custom model** method returns only this field. It does not
        not return the other fields of this object.
        :param str name: (optional) The name of the custom voice model.
        :param str language: (optional) The language identifier of the custom voice model
        (for example, `en-US`).
        :param str owner: (optional) The GUID of the service credentials for the instance
        of the service that owns the custom voice model.
        :param str created: (optional) The date and time in Coordinated Universal Time
        (UTC) at which the custom voice model was created. The value is provided in full
        ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str last_modified: (optional) The date and time in Coordinated Universal
        Time (UTC) at which the custom voice model was last modified. Equals `created`
        when a new voice model is first added but has yet to be updated. The value is
        provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str description: (optional) The description of the custom voice model.
        :param list[Word] words: (optional) An array of `Word` objects that lists the
        words and their translations from the custom voice model. The words are listed in
        alphabetical order, with uppercase letters listed before lowercase letters. The
        array is empty if the custom model contains no words. This field is returned only
        by the **Get a voice** method and only when you specify the customization ID of a
        custom voice model.
        """
        self.customization_id = customization_id
        self.name = name
        self.language = language
        self.owner = owner
        self.created = created
        self.last_modified = last_modified
        self.description = description
        self.words = words

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VoiceModel object from a json dictionary."""
        args = {}
        if 'customization_id' in _dict:
            args['customization_id'] = _dict.get('customization_id')
        else:
            raise ValueError(
                'Required property \'customization_id\' not present in VoiceModel JSON'
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
            args['words'] = [Word._from_dict(x) for x in (_dict.get('words'))]
        return cls(**args)

    def _to_dict(self):
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
            _dict['words'] = [x._to_dict() for x in self.words]
        return _dict

    def __str__(self):
        """Return a `str` version of this VoiceModel object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class VoiceModels(object):
    """
    VoiceModels.

    :attr list[VoiceModel] customizations: An array of `VoiceModel` objects that provides
    information about each available custom voice model. The array is empty if the
    requesting service credentials own no custom voice models (if no language is
    specified) or own no custom voice models for the specified language.
    """

    def __init__(self, customizations):
        """
        Initialize a VoiceModels object.

        :param list[VoiceModel] customizations: An array of `VoiceModel` objects that
        provides information about each available custom voice model. The array is empty
        if the requesting service credentials own no custom voice models (if no language
        is specified) or own no custom voice models for the specified language.
        """
        self.customizations = customizations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a VoiceModels object from a json dictionary."""
        args = {}
        if 'customizations' in _dict:
            args['customizations'] = [
                VoiceModel._from_dict(x) for x in (_dict.get('customizations'))
            ]
        else:
            raise ValueError(
                'Required property \'customizations\' not present in VoiceModels JSON'
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
        """Return a `str` version of this VoiceModels object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Voices(object):
    """
    Voices.

    :attr list[Voice] voices: A list of available voices.
    """

    def __init__(self, voices):
        """
        Initialize a Voices object.

        :param list[Voice] voices: A list of available voices.
        """
        self.voices = voices

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Voices object from a json dictionary."""
        args = {}
        if 'voices' in _dict:
            args['voices'] = [
                Voice._from_dict(x) for x in (_dict.get('voices'))
            ]
        else:
            raise ValueError(
                'Required property \'voices\' not present in Voices JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'voices') and self.voices is not None:
            _dict['voices'] = [x._to_dict() for x in self.voices]
        return _dict

    def __str__(self):
        """Return a `str` version of this Voices object."""
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

    :attr str word: A word from the custom voice model.
    :attr str translation: The phonetic or sounds-like translation for the word. A
    phonetic translation is based on the SSML format for representing the phonetic string
    of a word either as an IPA or IBM SPR translation. A sounds-like translation consists
    of one or more words that, when combined, sound like the word.
    :attr str part_of_speech: (optional) **Japanese only.** The part of speech for the
    word. The service uses the value to produce the correct intonation for the word. You
    can create only a single entry, with or without a single part of speech, for any word;
    you cannot create multiple entries with different parts of speech for the same word.
    For more information, see [Working with Japanese
    entries](/docs/services/text-to-speech/custom-rules.html#jaNotes).
    """

    def __init__(self, word, translation, part_of_speech=None):
        """
        Initialize a Word object.

        :param str word: A word from the custom voice model.
        :param str translation: The phonetic or sounds-like translation for the word. A
        phonetic translation is based on the SSML format for representing the phonetic
        string of a word either as an IPA or IBM SPR translation. A sounds-like
        translation consists of one or more words that, when combined, sound like the
        word.
        :param str part_of_speech: (optional) **Japanese only.** The part of speech for
        the word. The service uses the value to produce the correct intonation for the
        word. You can create only a single entry, with or without a single part of speech,
        for any word; you cannot create multiple entries with different parts of speech
        for the same word. For more information, see [Working with Japanese
        entries](/docs/services/text-to-speech/custom-rules.html#jaNotes).
        """
        self.word = word
        self.translation = translation
        self.part_of_speech = part_of_speech

    @classmethod
    def _from_dict(cls, _dict):
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'word') and self.word is not None:
            _dict['word'] = self.word
        if hasattr(self, 'translation') and self.translation is not None:
            _dict['translation'] = self.translation
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
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


class Words(object):
    """
    Words.

    :attr list[Word] words: The **Add custom words** method accepts an array of `Word`
    objects. Each object provides a word that is to be added or updated for the custom
    voice model and the word's translation.
    The **List custom words** method returns an array of `Word` objects. Each object shows
    a word and its translation from the custom voice model. The words are listed in
    alphabetical order, with uppercase letters listed before lowercase letters. The array
    is empty if the custom model contains no words.
    """

    def __init__(self, words):
        """
        Initialize a Words object.

        :param list[Word] words: The **Add custom words** method accepts an array of
        `Word` objects. Each object provides a word that is to be added or updated for the
        custom voice model and the word's translation.
        The **List custom words** method returns an array of `Word` objects. Each object
        shows a word and its translation from the custom voice model. The words are listed
        in alphabetical order, with uppercase letters listed before lowercase letters. The
        array is empty if the custom model contains no words.
        """
        self.words = words

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Words object from a json dictionary."""
        args = {}
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
