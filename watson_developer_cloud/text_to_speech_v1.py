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
The IBM Watson Text to Speech service provides an API that uses IBM's speech-synthesis
capabilities to synthesize text into natural-sounding speech in a variety of languages,
dialects, and voices. The service supports at least one male or female voice, sometimes
both, for each language. The audio is streamed back to the client with minimal delay.

For more information about the service and its various interfaces, see [About Text to
Speech](https://console.bluemix.net/docs/services/text-to-speech/index.html).
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService
from .utils import deprecated

##############################################################################
# Service
##############################################################################


class TextToSpeechV1(WatsonService):
    """The Text to Speech V1 service."""

    default_url = 'https://stream.watsonplatform.net/text-to-speech/api'

    def __init__(self,
                 url=default_url,
                 username=None,
                 password=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
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
            vcap_services_name='text_to_speech',
            url=url,
            username=username,
            password=password,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)

    #########################
    # Voices
    #########################

    def get_voice(self, voice, customization_id=None, **kwargs):
        """
        Retrieves a specific voice available for speech synthesis.

        :param str voice: The voice for which information is to be returned.
        :param str customization_id: The GUID of a custom voice model for which information is to be returned. You must make the request with service credentials created for the instance of the service that owns the custom model. Omit the parameter to see information about the specified voice with no customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Voice` response.
        :rtype: dict
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
        Retrieves a list of all voices available for use with the service. The information
        includes the name, language, gender, and other details about the voice.

        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Voices` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/voices'
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    @deprecated('Use list_voices() instead')
    def voices(self):
        return self.list_voices()

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
        Streaming speech synthesis of the text in the body parameter. Synthesizes text to spoken audio, returning the synthesized audio stream as an array of bytes.

        :param str text: The text to synthesize.
        :param str accept: The type of the response: audio/basic, audio/flac, audio/l16;rate=nnnn, audio/ogg, audio/ogg;codecs=opus, audio/ogg;codecs=vorbis, audio/mp3, audio/mpeg, audio/mulaw;rate=nnnn, audio/wav, audio/webm, audio/webm;codecs=opus, or audio/webm;codecs=vorbis.
        :param str voice: The voice to use for synthesis.
        :param str customization_id: The GUID of a custom voice model to use for the synthesis. If a custom voice model is specified, it is guaranteed to work only if it matches the language of the indicated voice. You must make the request with service credentials created for the instance of the service that owns the custom model. Omit the parameter to use the specified voice with no customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `Response <Response>` object representing the response.
        :rtype: requests.models.Response
        """
        if text is None:
            raise ValueError('text must be provided')
        headers = {'Accept': accept}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'voice': voice,
            'customization_id': customization_id
        }
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
        Gets the pronunciation for a word.

        Returns the phonetic pronunciation for the word specified by the `text` parameter.
        You can request the pronunciation for a specific format. You can also request the
        pronunciation for a specific voice to see the default translation for the language
        of that voice or for a specific custom voice model to see the translation for that
        voice model.   **Note:** This method is currently a beta release.

        :param str text: The word for which the pronunciation is requested.
        :param str voice: A voice that specifies the language in which the pronunciation is to be returned. All voices for the same language (for example, `en-US`) return the same translation.
        :param str format: The phoneme format in which to return the pronunciation. Omit the parameter to obtain the pronunciation in the default format.
        :param str customization_id: The GUID of a custom voice model for which the pronunciation is to be returned. The language of a specified custom model must match the language of the specified voice. If the word is not defined in the specified custom model, the service returns the default translation for the custom model's language. You must make the request with service credentials created for the instance of the service that owns the custom model. Omit the parameter to see the translation for the specified voice with no customization.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Pronunciation` response.
        :rtype: dict
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

    @deprecated('Use get_pronunciation() instead')
    def pronunciation(self, text, voice=None, pronunciation_format='ipa'):
        return self.get_pronunciation(text, voice, pronunciation_format)

    #########################
    # Custom models
    #########################

    def create_voice_model(self,
                           name,
                           language=None,
                           description=None,
                           **kwargs):
        """
        Creates a new empty custom voice model. The model is owned by the instance of the
        service whose credentials are used to create it.   **Note:** This method is
        currently a beta release.

        :param str name: The name of the new custom voice model.
        :param str language: The language of the new custom voice model. Omit the parameter to use the the default language, `en-US`.
        :param str description: A description of the new custom voice model. Specifying a description is recommended.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `VoiceModel` response.
        :rtype: dict
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

    @deprecated('Use create_voice_model() instead.')
    def create_customization(self, name, language=None, description=None):
        return self.create_voice_model(name, language, description)

    def delete_voice_model(self, customization_id, **kwargs):
        """
        Deletes the custom voice model with the specified `customization_id`. You must use
        credentials for the instance of the service that owns a model to delete it.
        **Note:** This method is currently a beta release.

        :param str customization_id: The GUID of the custom voice model.
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

    @deprecated('Use delete_voice_model() instead.')
    def delete_customization(self, customization_id):
        return self.delete_voice_model(customization_id)

    def get_voice_model(self, customization_id, **kwargs):
        """
        Queries the contents of a custom voice model.

        Lists all information about the custom voice model with the specified
        `customization_id`. In addition to metadata such as the name and description of
        the voice model, the output includes the words in the model and their translations
        as defined in the model. To see just the metadata for a voice model, use the `GET
        /v1/customizations` method. You must use credentials for the instance of the
        service that owns a model to list information about it.   **Note:** This method is
        currently a beta release.

        :param str customization_id: The GUID of the custom voice model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `VoiceModel` response.
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

    @deprecated('Use get_voice_model instead.')
    def get_customization(self, customization_id):
        return self.get_voice_model(customization_id)

    def list_voice_models(self, language=None, **kwargs):
        """
        Lists metadata such as the name and description for the custom voice models that
        you own. Use the `language` query parameter to list the voice models that you own
        for the specified language only. Omit the parameter to see all voice models that
        you own for all languages. To see the words in addition to the metadata for a
        specific voice model, use the `GET /v1/customizations/{customization_id}` method.
        You must use credentials for the instance of the service that owns a model to list
        information about it.   **Note:** This method is currently a beta release.

        :param str language: The language for which custom voice models that are owned by the requesting service credentials are to be returned. Omit the parameter to see all custom voice models that are owned by the requester.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `VoiceModels` response.
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

    @deprecated('Use list_voice_models() instead.')
    def customizations(self, language=None):
        return self.list_voice_models(language)

    def update_voice_model(self,
                           customization_id,
                           name=None,
                           description=None,
                           words=None,
                           **kwargs):
        """
        Updates information and words for a custom voice model.

        Updates information for the custom voice model with the specified
        `customization_id`. You can update the metadata such as the name and description
        of the voice model. You can also update the words in the model and their
        translations. Adding a new translation for a word that already exists in a custom
        model overwrites the word's existing translation. A custom model can contain no
        more than 20,000 entries. You must use credentials for the instance of the service
        that owns a model to update it.   **Note:** This method is currently a beta
        release.

        :param str customization_id: The GUID of the custom voice model.
        :param str name: A new name for the custom voice model.
        :param str description: A new description for the custom voice model.
        :param list[Word] words: An array of `Word` objects that provides the words and their translations that are to be added or updated for the custom voice model. Pass an empty array to make no additions or updates.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return None

    @deprecated('Use update_voice_model() instead')
    def update_customization(self, customization_id, name=None,
                             description=None, words=None):
        return self.update_voice_model(customization_id, name, description, words)

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
        Adds a word to a custom voice model.

        Adds a single word and its translation to the custom voice model with the
        specified `customization_id`. Adding a new translation for a word that already
        exists in a custom model overwrites the word's existing translation. A custom
        model can contain no more than 20,000 entries. You must use credentials for the
        instance of the service that owns a model to add a word to it.   **Note:** This
        method is currently a beta release.

        :param str customization_id: The GUID of the custom voice model.
        :param str word: The word that is to be added or updated for the custom voice model.
        :param str translation: The phonetic or sounds-like translation for the word. A phonetic translation is based on the SSML format for representing the phonetic string of a word either as an IPA translation or as an IBM SPR translation. A sounds-like is one or more words that, when combined, sound like the word.
        :param str part_of_speech: **Japanese only.** The part of speech for the word. The service uses the value to produce the correct intonation for the word. You can create only a single entry, with or without a single part of speech, for any word; you cannot create multiple entries with different parts of speech for the same word. For more information, see [Working with Japanese entries](https://console.bluemix.net/docs/services/text-to-speech/custom-rules.html#jaNotes).
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        self.request(
            method='PUT',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return None

    @deprecated('Use add_word() instead.')
    def set_customization_word(self, customization_id, word, translation):
        return self.add_word(customization_id, word, translation)

    def add_words(self, customization_id, words, **kwargs):
        """
        Adds one or more words to a custom voice model.

        Adds one or more words and their translations to the custom voice model with the
        specified `customization_id`. Adding a new translation for a word that already
        exists in a custom model overwrites the word's existing translation. A custom
        model can contain no more than 20,000 entries. You must use credentials for the
        instance of the service that owns a model to add words to it.   **Note:** This
        method is currently a beta release.

        :param str customization_id: The GUID of the custom voice model.
        :param list[Word] words: **When adding words to a custom voice model,** an array of `Word` objects that provides one or more words that are to be added or updated for the custom voice model and the translation for each specified word. **When listing words from a custom voice model,** an array of `Word` objects that lists the words and their translations from the custom voice model. The words are listed in alphabetical order, with uppercase letters listed before lowercase letters. The array is empty if the custom model contains no words.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return None

    @deprecated('Use add_words() instead.')
    def add_customization_words(self, customization_id, words):
        return self.add_words(customization_id, words)

    def delete_word(self, customization_id, word, **kwargs):
        """
        Deletes a word from a custom voice model.

        Deletes a single word from the custom voice model with the specified
        `customization_id`. You must use credentials for the instance of the service that
        owns a model to delete it.   **Note:** This method is currently a beta release.

        :param str customization_id: The GUID of the custom voice model.
        :param str word: The word that is to be deleted from the custom voice model.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
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
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    @deprecated('Use delete_word() instead.')
    def delete_customization_word(self, customization_id, word):
        return self.delete_word(customization_id, word)

    def get_word(self, customization_id, word, **kwargs):
        """
        Queries details about a word in a custom voice model.

        Returns the translation for a single word from the custom model with the specified
        `customization_id`. The output shows the translation as it is defined in the
        model. You must use credentials for the instance of the service that owns a model
        to query information about its words.   **Note:** This method is currently a beta
        release.

        :param str customization_id: The GUID of the custom voice model.
        :param str word: The word that is to be queried from the custom voice model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Translation` response.
        :rtype: dict
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

    @deprecated('Use get_word() instead.')
    def get_customization_word(self, customization_id, word):
        return self.get_word(customization_id, word)

    def list_words(self, customization_id, **kwargs):
        """
        Queries details about the words in a custom voice model.

        Lists all of the words and their translations for the custom voice model with the
        specified `customization_id`. The output shows the translations as they are
        defined in the model. You must use credentials for the instance of the service
        that owns a model to query information about its words.   **Note:** This method is
        currently a beta release.

        :param str customization_id: The GUID of the custom voice model.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Words` response.
        :rtype: dict
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

    @deprecated('Use list_words() instead.')
    def get_customization_words(self, customization_id):
        return self.list_words(customization_id)


##############################################################################
# Models
##############################################################################


class Pronunciation(object):
    """
    Pronunciation.

    :attr str pronunciation: The pronunciation of the requested text in the specified voice and format.
    """

    def __init__(self, pronunciation):
        """
        Initialize a Pronunciation object.

        :param str pronunciation: The pronunciation of the requested text in the specified voice and format.
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
    SupportedFeatures.

    :attr bool custom_pronunciation: If `true`, the voice can be customized; if `false`, the voice cannot be customized. (Same as `customizable`.).
    :attr bool voice_transformation: If `true`, the voice can be transformed by using the SSML &lt;voice-transformation&gt; element; if `false`, the voice cannot be transformed.
    """

    def __init__(self, custom_pronunciation, voice_transformation):
        """
        Initialize a SupportedFeatures object.

        :param bool custom_pronunciation: If `true`, the voice can be customized; if `false`, the voice cannot be customized. (Same as `customizable`.).
        :param bool voice_transformation: If `true`, the voice can be transformed by using the SSML &lt;voice-transformation&gt; element; if `false`, the voice cannot be transformed.
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
        if hasattr(self, 'custom_pronunciation') and self.custom_pronunciation is not None:
            _dict['custom_pronunciation'] = self.custom_pronunciation
        if hasattr(self, 'voice_transformation') and self.voice_transformation is not None:
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

    :attr str translation: The phonetic or sounds-like translation for the word. A phonetic translation is based on the SSML format for representing the phonetic string of a word either as an IPA translation or as an IBM SPR translation. A sounds-like is one or more words that, when combined, sound like the word.
    :attr str part_of_speech: (optional) **Japanese only.** The part of speech for the word. The service uses the value to produce the correct intonation for the word. You can create only a single entry, with or without a single part of speech, for any word; you cannot create multiple entries with different parts of speech for the same word. For more information, see [Working with Japanese entries](https://console.bluemix.net/docs/services/text-to-speech/custom-rules.html#jaNotes).
    """

    def __init__(self, translation, part_of_speech=None):
        """
        Initialize a Translation object.

        :param str translation: The phonetic or sounds-like translation for the word. A phonetic translation is based on the SSML format for representing the phonetic string of a word either as an IPA translation or as an IBM SPR translation. A sounds-like is one or more words that, when combined, sound like the word.
        :param str part_of_speech: (optional) **Japanese only.** The part of speech for the word. The service uses the value to produce the correct intonation for the word. You can create only a single entry, with or without a single part of speech, for any word; you cannot create multiple entries with different parts of speech for the same word. For more information, see [Working with Japanese entries](https://console.bluemix.net/docs/services/text-to-speech/custom-rules.html#jaNotes).
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
    :attr str name: The name of the voice. Use this as the voice identifier in all requests.
    :attr str language: The language and region of the voice (for example, `en-US`).
    :attr str description: A textual description of the voice.
    :attr bool customizable: If `true`, the voice can be customized; if `false`, the voice cannot be customized. (Same as `custom_pronunciation`; maintained for backward compatibility.).
    :attr SupportedFeatures supported_features: Describes the additional service features supported with the voice.
    :attr VoiceModel customization: (optional) Returns information about a specified custom voice model. **Note:** This field is returned only when you list information about a specific voice and specify the GUID of a custom voice model that is based on that voice.
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
        :param str name: The name of the voice. Use this as the voice identifier in all requests.
        :param str language: The language and region of the voice (for example, `en-US`).
        :param str description: A textual description of the voice.
        :param bool customizable: If `true`, the voice can be customized; if `false`, the voice cannot be customized. (Same as `custom_pronunciation`; maintained for backward compatibility.).
        :param SupportedFeatures supported_features: Describes the additional service features supported with the voice.
        :param VoiceModel customization: (optional) Returns information about a specified custom voice model. **Note:** This field is returned only when you list information about a specific voice and specify the GUID of a custom voice model that is based on that voice.
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

    :attr str customization_id: The customization ID (GUID) of the custom voice model. **Note:** When you create a new custom voice model, the service returns only the GUID of the new custom model; it does not return the other fields of this object.
    :attr str name: (optional) The name of the custom voice model.
    :attr str language: (optional) The language identifier of the custom voice model (for example, `en-US`).
    :attr str owner: (optional) The GUID of the service credentials for the instance of the service that owns the custom voice model.
    :attr str created: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom voice model was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str last_modified: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom voice model was last modified. Equals `created` when a new voice model is first added but has yet to be updated. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
    :attr str description: (optional) The description of the custom voice model.
    :attr list[Word] words: (optional) An array of `Word` objects that lists the words and their translations from the custom voice model. The words are listed in alphabetical order, with uppercase letters listed before lowercase letters. The array is empty if the custom model contains no words. **Note:** This field is returned only when you list information about a specific custom voice model.
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

        :param str customization_id: The customization ID (GUID) of the custom voice model. **Note:** When you create a new custom voice model, the service returns only the GUID of the new custom model; it does not return the other fields of this object.
        :param str name: (optional) The name of the custom voice model.
        :param str language: (optional) The language identifier of the custom voice model (for example, `en-US`).
        :param str owner: (optional) The GUID of the service credentials for the instance of the service that owns the custom voice model.
        :param str created: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom voice model was created. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str last_modified: (optional) The date and time in Coordinated Universal Time (UTC) at which the custom voice model was last modified. Equals `created` when a new voice model is first added but has yet to be updated. The value is provided in full ISO 8601 format (`YYYY-MM-DDThh:mm:ss.sTZD`).
        :param str description: (optional) The description of the custom voice model.
        :param list[Word] words: (optional) An array of `Word` objects that lists the words and their translations from the custom voice model. The words are listed in alphabetical order, with uppercase letters listed before lowercase letters. The array is empty if the custom model contains no words. **Note:** This field is returned only when you list information about a specific custom voice model.
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
            args['words'] = [Word._from_dict(x) for x in _dict.get('words')]
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

    :attr list[VoiceModel] customizations: An array of `VoiceModel` objects that provides information about each available custom voice model. The array is empty if the requesting service credentials own no custom voice models (if no language is specified) or own no custom voice models for the specified language.
    """

    def __init__(self, customizations):
        """
        Initialize a VoiceModels object.

        :param list[VoiceModel] customizations: An array of `VoiceModel` objects that provides information about each available custom voice model. The array is empty if the requesting service credentials own no custom voice models (if no language is specified) or own no custom voice models for the specified language.
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
    :attr str translation: The phonetic or sounds-like translation for the word. A phonetic translation is based on the SSML format for representing the phonetic string of a word either as an IPA or IBM SPR translation. A sounds-like translation consists of one or more words that, when combined, sound like the word.
    :attr str part_of_speech: (optional) **Japanese only.** The part of speech for the word. The service uses the value to produce the correct intonation for the word. You can create only a single entry, with or without a single part of speech, for any word; you cannot create multiple entries with different parts of speech for the same word. For more information, see [Working with Japanese entries](https://console.bluemix.net/docs/services/text-to-speech/custom-rules.html#jaNotes).
    """

    def __init__(self, word, translation, part_of_speech=None):
        """
        Initialize a Word object.

        :param str word: A word from the custom voice model.
        :param str translation: The phonetic or sounds-like translation for the word. A phonetic translation is based on the SSML format for representing the phonetic string of a word either as an IPA or IBM SPR translation. A sounds-like translation consists of one or more words that, when combined, sound like the word.
        :param str part_of_speech: (optional) **Japanese only.** The part of speech for the word. The service uses the value to produce the correct intonation for the word. You can create only a single entry, with or without a single part of speech, for any word; you cannot create multiple entries with different parts of speech for the same word. For more information, see [Working with Japanese entries](https://console.bluemix.net/docs/services/text-to-speech/custom-rules.html#jaNotes).
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

    :attr list[Word] words: **When adding words to a custom voice model,** an array of `Word` objects that provides one or more words that are to be added or updated for the custom voice model and the translation for each specified word. **When listing words from a custom voice model,** an array of `Word` objects that lists the words and their translations from the custom voice model. The words are listed in alphabetical order, with uppercase letters listed before lowercase letters. The array is empty if the custom model contains no words.
    """

    def __init__(self, words):
        """
        Initialize a Words object.

        :param list[Word] words: **When adding words to a custom voice model,** an array of `Word` objects that provides one or more words that are to be added or updated for the custom voice model and the translation for each specified word. **When listing words from a custom voice model,** an array of `Word` objects that lists the words and their translations from the custom voice model. The words are listed in alphabetical order, with uppercase letters listed before lowercase letters. The array is empty if the custom model contains no words.
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
