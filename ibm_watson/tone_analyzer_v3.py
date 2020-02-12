# coding: utf-8

# (C) Copyright IBM Corp. 2016, 2020.
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
The IBM Watson&trade; Tone Analyzer service uses linguistic analysis to detect emotional
and language tones in written text. The service can analyze tone at both the document and
sentence levels. You can use the service to understand how your written communications are
perceived and then to improve the tone of your communications. Businesses can use the
service to learn the tone of their customers' communications and to respond to each
customer appropriately, or to understand and improve their customer conversations.
**Note:** Request logging is disabled for the Tone Analyzer service. Regardless of whether
you set the `X-Watson-Learning-Opt-Out` request header, the service does not log or retain
data from requests and responses.
"""

import json
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from .common import get_sdk_headers
from enum import Enum
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import DetailedResponse
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from typing import Dict
from typing import List

##############################################################################
# Service
##############################################################################


class ToneAnalyzerV3(BaseService):
    """The Tone Analyzer V3 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    DEFAULT_SERVICE_NAME = 'tone_analyzer'

    def __init__(
            self,
            version: str,
            authenticator: Authenticator = None,
            service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Tone Analyzer service.

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

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if not authenticator:
            authenticator = get_authenticator_from_environment(service_name)
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator,
                             disable_ssl_verification=False)
        self.version = version
        self.configure_service(service_name)

    #########################
    # Methods
    #########################

    def tone(self,
             tone_input: object,
             *,
             content_type: str = None,
             sentences: bool = None,
             tones: List[str] = None,
             content_language: str = None,
             accept_language: str = None,
             **kwargs) -> 'DetailedResponse':
        """
        Analyze general tone.

        Use the general-purpose endpoint to analyze the tone of your input content. The
        service analyzes the content for emotional and language tones. The method always
        analyzes the tone of the full document; by default, it also analyzes the tone of
        each individual sentence of the content.
        You can submit no more than 128 KB of total input content and no more than 1000
        individual sentences in JSON, plain text, or HTML format. The service analyzes the
        first 1000 sentences for document-level analysis and only the first 100 sentences
        for sentence-level analysis.
        Per the JSON specification, the default character encoding for JSON content is
        effectively always UTF-8; per the HTTP specification, the default encoding for
        plain text and HTML is ISO-8859-1 (effectively, the ASCII character set). When
        specifying a content type of plain text or HTML, include the `charset` parameter
        to indicate the character encoding of the input text; for example: `Content-Type:
        text/plain;charset=utf-8`. For `text/html`, the service removes HTML tags and
        analyzes only the textual content.
        **See also:** [Using the general-purpose
        endpoint](https://cloud.ibm.com/docs/tone-analyzer?topic=tone-analyzer-utgpe#utgpe).

        :param ToneInput tone_input: JSON, plain text, or HTML input that contains
               the content to be analyzed. For JSON input, provide an object of type
               `ToneInput`.
        :param str content_type: (optional) The type of the input. A character
               encoding can be specified by including a `charset` parameter. For example,
               'text/plain;charset=utf-8'.
        :param bool sentences: (optional) Indicates whether the service is to
               return an analysis of each individual sentence in addition to its analysis
               of the full document. If `true` (the default), the service returns results
               for each sentence.
        :param List[str] tones: (optional) **`2017-09-21`:** Deprecated. The
               service continues to accept the parameter for backward-compatibility, but
               the parameter no longer affects the response.
               **`2016-05-19`:** A comma-separated list of tones for which the service is
               to return its analysis of the input; the indicated tones apply both to the
               full document and to individual sentences of the document. You can specify
               one or more of the valid values. Omit the parameter to request results for
               all three tones.
        :param str content_language: (optional) The language of the input text for
               the request: English or French. Regional variants are treated as their
               parent language; for example, `en-US` is interpreted as `en`. The input
               content must match the specified language. Do not submit content that
               contains both languages. You can use different languages for
               **Content-Language** and **Accept-Language**.
               * **`2017-09-21`:** Accepts `en` or `fr`.
               * **`2016-05-19`:** Accepts only `en`.
        :param str accept_language: (optional) The desired language of the
               response. For two-character arguments, regional variants are treated as
               their parent language; for example, `en-US` is interpreted as `en`. You can
               use different languages for **Content-Language** and **Accept-Language**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if tone_input is None:
            raise ValueError('tone_input must be provided')
        if isinstance(tone_input, ToneInput):
            tone_input = self._convert_model(tone_input)

        headers = {
            'Content-Type': content_type,
            'Content-Language': content_language,
            'Accept-Language': accept_language
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='tone')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'sentences': sentences,
            'tones': self._convert_list(tones)
        }

        if content_type == 'application/json' and isinstance(tone_input, dict):
            data = json.dumps(tone_input)
        else:
            data = tone_input

        url = '/v3/tone'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def tone_chat(self,
                  utterances: List['Utterance'],
                  *,
                  content_language: str = None,
                  accept_language: str = None,
                  **kwargs) -> 'DetailedResponse':
        """
        Analyze customer-engagement tone.

        Use the customer-engagement endpoint to analyze the tone of customer service and
        customer support conversations. For each utterance of a conversation, the method
        reports the most prevalent subset of the following seven tones: sad, frustrated,
        satisfied, excited, polite, impolite, and sympathetic.
        If you submit more than 50 utterances, the service returns a warning for the
        overall content and analyzes only the first 50 utterances. If you submit a single
        utterance that contains more than 500 characters, the service returns an error for
        that utterance and does not analyze the utterance. The request fails if all
        utterances have more than 500 characters. Per the JSON specification, the default
        character encoding for JSON content is effectively always UTF-8.
        **See also:** [Using the customer-engagement
        endpoint](https://cloud.ibm.com/docs/tone-analyzer?topic=tone-analyzer-utco#utco).

        :param List[Utterance] utterances: An array of `Utterance` objects that
               provides the input content that the service is to analyze.
        :param str content_language: (optional) The language of the input text for
               the request: English or French. Regional variants are treated as their
               parent language; for example, `en-US` is interpreted as `en`. The input
               content must match the specified language. Do not submit content that
               contains both languages. You can use different languages for
               **Content-Language** and **Accept-Language**.
               * **`2017-09-21`:** Accepts `en` or `fr`.
               * **`2016-05-19`:** Accepts only `en`.
        :param str accept_language: (optional) The desired language of the
               response. For two-character arguments, regional variants are treated as
               their parent language; for example, `en-US` is interpreted as `en`. You can
               use different languages for **Content-Language** and **Accept-Language**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if utterances is None:
            raise ValueError('utterances must be provided')
        utterances = [self._convert_model(x) for x in utterances]

        headers = {
            'Content-Language': content_language,
            'Accept-Language': accept_language
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='tone_chat')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'utterances': utterances}

        url = '/v3/tone_chat'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


class ToneEnums(object):

    class ContentType(Enum):
        """
        The type of the input. A character encoding can be specified by including a
        `charset` parameter. For example, 'text/plain;charset=utf-8'.
        """
        APPLICATION_JSON = 'application/json'
        TEXT_PLAIN = 'text/plain'
        TEXT_HTML = 'text/html'

    class Tones(Enum):
        """
        **`2017-09-21`:** Deprecated. The service continues to accept the parameter for
        backward-compatibility, but the parameter no longer affects the response.
        **`2016-05-19`:** A comma-separated list of tones for which the service is to
        return its analysis of the input; the indicated tones apply both to the full
        document and to individual sentences of the document. You can specify one or more
        of the valid values. Omit the parameter to request results for all three tones.
        """
        EMOTION = 'emotion'
        LANGUAGE = 'language'
        SOCIAL = 'social'

    class ContentLanguage(Enum):
        """
        The language of the input text for the request: English or French. Regional
        variants are treated as their parent language; for example, `en-US` is interpreted
        as `en`. The input content must match the specified language. Do not submit
        content that contains both languages. You can use different languages for
        **Content-Language** and **Accept-Language**.
        * **`2017-09-21`:** Accepts `en` or `fr`.
        * **`2016-05-19`:** Accepts only `en`.
        """
        EN = 'en'
        FR = 'fr'

    class AcceptLanguage(Enum):
        """
        The desired language of the response. For two-character arguments, regional
        variants are treated as their parent language; for example, `en-US` is interpreted
        as `en`. You can use different languages for **Content-Language** and
        **Accept-Language**.
        """
        AR = 'ar'
        DE = 'de'
        EN = 'en'
        ES = 'es'
        FR = 'fr'
        IT = 'it'
        JA = 'ja'
        KO = 'ko'
        PT_BR = 'pt-br'
        ZH_CN = 'zh-cn'
        ZH_TW = 'zh-tw'


class ToneChatEnums(object):

    class ContentLanguage(Enum):
        """
        The language of the input text for the request: English or French. Regional
        variants are treated as their parent language; for example, `en-US` is interpreted
        as `en`. The input content must match the specified language. Do not submit
        content that contains both languages. You can use different languages for
        **Content-Language** and **Accept-Language**.
        * **`2017-09-21`:** Accepts `en` or `fr`.
        * **`2016-05-19`:** Accepts only `en`.
        """
        EN = 'en'
        FR = 'fr'

    class AcceptLanguage(Enum):
        """
        The desired language of the response. For two-character arguments, regional
        variants are treated as their parent language; for example, `en-US` is interpreted
        as `en`. You can use different languages for **Content-Language** and
        **Accept-Language**.
        """
        AR = 'ar'
        DE = 'de'
        EN = 'en'
        ES = 'es'
        FR = 'fr'
        IT = 'it'
        JA = 'ja'
        KO = 'ko'
        PT_BR = 'pt-br'
        ZH_CN = 'zh-cn'
        ZH_TW = 'zh-tw'


##############################################################################
# Models
##############################################################################


class DocumentAnalysis():
    """
    The results of the analysis for the full input content.

    :attr List[ToneScore] tones: (optional) **`2017-09-21`:** An array of
          `ToneScore` objects that provides the results of the analysis for each
          qualifying tone of the document. The array includes results for any tone whose
          score is at least 0.5. The array is empty if no tone has a score that meets this
          threshold. **`2016-05-19`:** Not returned.
    :attr List[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not
          returned. **`2016-05-19`:** An array of `ToneCategory` objects that provides the
          results of the tone analysis for the full document of the input content. The
          service returns results only for the tones specified with the `tones` parameter
          of the request.
    :attr str warning: (optional) **`2017-09-21`:** A warning message if the overall
          content exceeds 128 KB or contains more than 1000 sentences. The service
          analyzes only the first 1000 sentences for document-level analysis and the first
          100 sentences for sentence-level analysis. **`2016-05-19`:** Not returned.
    """

    def __init__(self,
                 *,
                 tones: List['ToneScore'] = None,
                 tone_categories: List['ToneCategory'] = None,
                 warning: str = None) -> None:
        """
        Initialize a DocumentAnalysis object.

        :param List[ToneScore] tones: (optional) **`2017-09-21`:** An array of
               `ToneScore` objects that provides the results of the analysis for each
               qualifying tone of the document. The array includes results for any tone
               whose score is at least 0.5. The array is empty if no tone has a score that
               meets this threshold. **`2016-05-19`:** Not returned.
        :param List[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not
               returned. **`2016-05-19`:** An array of `ToneCategory` objects that
               provides the results of the tone analysis for the full document of the
               input content. The service returns results only for the tones specified
               with the `tones` parameter of the request.
        :param str warning: (optional) **`2017-09-21`:** A warning message if the
               overall content exceeds 128 KB or contains more than 1000 sentences. The
               service analyzes only the first 1000 sentences for document-level analysis
               and the first 100 sentences for sentence-level analysis. **`2016-05-19`:**
               Not returned.
        """
        self.tones = tones
        self.tone_categories = tone_categories
        self.warning = warning

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentAnalysis':
        """Initialize a DocumentAnalysis object from a json dictionary."""
        args = {}
        valid_keys = ['tones', 'tone_categories', 'warning']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentAnalysis: '
                + ', '.join(bad_keys))
        if 'tones' in _dict:
            args['tones'] = [
                ToneScore._from_dict(x) for x in (_dict.get('tones'))
            ]
        if 'tone_categories' in _dict:
            args['tone_categories'] = [
                ToneCategory._from_dict(x)
                for x in (_dict.get('tone_categories'))
            ]
        if 'warning' in _dict:
            args['warning'] = _dict.get('warning')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentAnalysis object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tones') and self.tones is not None:
            _dict['tones'] = [x._to_dict() for x in self.tones]
        if hasattr(self,
                   'tone_categories') and self.tone_categories is not None:
            _dict['tone_categories'] = [
                x._to_dict() for x in self.tone_categories
            ]
        if hasattr(self, 'warning') and self.warning is not None:
            _dict['warning'] = self.warning
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocumentAnalysis') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentAnalysis') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentenceAnalysis():
    """
    The results of the analysis for the individual sentences of the input content.

    :attr int sentence_id: The unique identifier of a sentence of the input content.
          The first sentence has ID 0, and the ID of each subsequent sentence is
          incremented by one.
    :attr str text: The text of the input sentence.
    :attr List[ToneScore] tones: (optional) **`2017-09-21`:** An array of
          `ToneScore` objects that provides the results of the analysis for each
          qualifying tone of the sentence. The array includes results for any tone whose
          score is at least 0.5. The array is empty if no tone has a score that meets this
          threshold. **`2016-05-19`:** Not returned.
    :attr List[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not
          returned. **`2016-05-19`:** An array of `ToneCategory` objects that provides the
          results of the tone analysis for the sentence. The service returns results only
          for the tones specified with the `tones` parameter of the request.
    :attr int input_from: (optional) **`2017-09-21`:** Not returned.
          **`2016-05-19`:** The offset of the first character of the sentence in the
          overall input content.
    :attr int input_to: (optional) **`2017-09-21`:** Not returned. **`2016-05-19`:**
          The offset of the last character of the sentence in the overall input content.
    """

    def __init__(self,
                 sentence_id: int,
                 text: str,
                 *,
                 tones: List['ToneScore'] = None,
                 tone_categories: List['ToneCategory'] = None,
                 input_from: int = None,
                 input_to: int = None) -> None:
        """
        Initialize a SentenceAnalysis object.

        :param int sentence_id: The unique identifier of a sentence of the input
               content. The first sentence has ID 0, and the ID of each subsequent
               sentence is incremented by one.
        :param str text: The text of the input sentence.
        :param List[ToneScore] tones: (optional) **`2017-09-21`:** An array of
               `ToneScore` objects that provides the results of the analysis for each
               qualifying tone of the sentence. The array includes results for any tone
               whose score is at least 0.5. The array is empty if no tone has a score that
               meets this threshold. **`2016-05-19`:** Not returned.
        :param List[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not
               returned. **`2016-05-19`:** An array of `ToneCategory` objects that
               provides the results of the tone analysis for the sentence. The service
               returns results only for the tones specified with the `tones` parameter of
               the request.
        :param int input_from: (optional) **`2017-09-21`:** Not returned.
               **`2016-05-19`:** The offset of the first character of the sentence in the
               overall input content.
        :param int input_to: (optional) **`2017-09-21`:** Not returned.
               **`2016-05-19`:** The offset of the last character of the sentence in the
               overall input content.
        """
        self.sentence_id = sentence_id
        self.text = text
        self.tones = tones
        self.tone_categories = tone_categories
        self.input_from = input_from
        self.input_to = input_to

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SentenceAnalysis':
        """Initialize a SentenceAnalysis object from a json dictionary."""
        args = {}
        valid_keys = [
            'sentence_id', 'text', 'tones', 'tone_categories', 'input_from',
            'input_to'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SentenceAnalysis: '
                + ', '.join(bad_keys))
        if 'sentence_id' in _dict:
            args['sentence_id'] = _dict.get('sentence_id')
        else:
            raise ValueError(
                'Required property \'sentence_id\' not present in SentenceAnalysis JSON'
            )
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in SentenceAnalysis JSON'
            )
        if 'tones' in _dict:
            args['tones'] = [
                ToneScore._from_dict(x) for x in (_dict.get('tones'))
            ]
        if 'tone_categories' in _dict:
            args['tone_categories'] = [
                ToneCategory._from_dict(x)
                for x in (_dict.get('tone_categories'))
            ]
        if 'input_from' in _dict:
            args['input_from'] = _dict.get('input_from')
        if 'input_to' in _dict:
            args['input_to'] = _dict.get('input_to')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentenceAnalysis object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sentence_id') and self.sentence_id is not None:
            _dict['sentence_id'] = self.sentence_id
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'tones') and self.tones is not None:
            _dict['tones'] = [x._to_dict() for x in self.tones]
        if hasattr(self,
                   'tone_categories') and self.tone_categories is not None:
            _dict['tone_categories'] = [
                x._to_dict() for x in self.tone_categories
            ]
        if hasattr(self, 'input_from') and self.input_from is not None:
            _dict['input_from'] = self.input_from
        if hasattr(self, 'input_to') and self.input_to is not None:
            _dict['input_to'] = self.input_to
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SentenceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SentenceAnalysis') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SentenceAnalysis') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneAnalysis():
    """
    The tone analysis results for the input from the general-purpose endpoint.

    :attr DocumentAnalysis document_tone: The results of the analysis for the full
          input content.
    :attr List[SentenceAnalysis] sentences_tone: (optional) An array of
          `SentenceAnalysis` objects that provides the results of the analysis for the
          individual sentences of the input content. The service returns results only for
          the first 100 sentences of the input. The field is omitted if the `sentences`
          parameter of the request is set to `false`.
    """

    def __init__(self,
                 document_tone: 'DocumentAnalysis',
                 *,
                 sentences_tone: List['SentenceAnalysis'] = None) -> None:
        """
        Initialize a ToneAnalysis object.

        :param DocumentAnalysis document_tone: The results of the analysis for the
               full input content.
        :param List[SentenceAnalysis] sentences_tone: (optional) An array of
               `SentenceAnalysis` objects that provides the results of the analysis for
               the individual sentences of the input content. The service returns results
               only for the first 100 sentences of the input. The field is omitted if the
               `sentences` parameter of the request is set to `false`.
        """
        self.document_tone = document_tone
        self.sentences_tone = sentences_tone

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToneAnalysis':
        """Initialize a ToneAnalysis object from a json dictionary."""
        args = {}
        valid_keys = ['document_tone', 'sentences_tone']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ToneAnalysis: '
                + ', '.join(bad_keys))
        if 'document_tone' in _dict:
            args['document_tone'] = DocumentAnalysis._from_dict(
                _dict.get('document_tone'))
        else:
            raise ValueError(
                'Required property \'document_tone\' not present in ToneAnalysis JSON'
            )
        if 'sentences_tone' in _dict:
            args['sentences_tone'] = [
                SentenceAnalysis._from_dict(x)
                for x in (_dict.get('sentences_tone'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneAnalysis object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_tone') and self.document_tone is not None:
            _dict['document_tone'] = self.document_tone._to_dict()
        if hasattr(self, 'sentences_tone') and self.sentences_tone is not None:
            _dict['sentences_tone'] = [
                x._to_dict() for x in self.sentences_tone
            ]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToneAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ToneAnalysis') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToneAnalysis') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneCategory():
    """
    The category for a tone from the input content.

    :attr List[ToneScore] tones: An array of `ToneScore` objects that provides the
          results for the tones of the category.
    :attr str category_id: The unique, non-localized identifier of the category for
          the results. The service can return results for the following category IDs:
          `emotion_tone`, `language_tone`, and `social_tone`.
    :attr str category_name: The user-visible, localized name of the category.
    """

    def __init__(self, tones: List['ToneScore'], category_id: str,
                 category_name: str) -> None:
        """
        Initialize a ToneCategory object.

        :param List[ToneScore] tones: An array of `ToneScore` objects that provides
               the results for the tones of the category.
        :param str category_id: The unique, non-localized identifier of the
               category for the results. The service can return results for the following
               category IDs: `emotion_tone`, `language_tone`, and `social_tone`.
        :param str category_name: The user-visible, localized name of the category.
        """
        self.tones = tones
        self.category_id = category_id
        self.category_name = category_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToneCategory':
        """Initialize a ToneCategory object from a json dictionary."""
        args = {}
        valid_keys = ['tones', 'category_id', 'category_name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ToneCategory: '
                + ', '.join(bad_keys))
        if 'tones' in _dict:
            args['tones'] = [
                ToneScore._from_dict(x) for x in (_dict.get('tones'))
            ]
        else:
            raise ValueError(
                'Required property \'tones\' not present in ToneCategory JSON')
        if 'category_id' in _dict:
            args['category_id'] = _dict.get('category_id')
        else:
            raise ValueError(
                'Required property \'category_id\' not present in ToneCategory JSON'
            )
        if 'category_name' in _dict:
            args['category_name'] = _dict.get('category_name')
        else:
            raise ValueError(
                'Required property \'category_name\' not present in ToneCategory JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneCategory object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tones') and self.tones is not None:
            _dict['tones'] = [x._to_dict() for x in self.tones]
        if hasattr(self, 'category_id') and self.category_id is not None:
            _dict['category_id'] = self.category_id
        if hasattr(self, 'category_name') and self.category_name is not None:
            _dict['category_name'] = self.category_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToneCategory object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ToneCategory') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToneCategory') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneChatScore():
    """
    The score for an utterance from the input content.

    :attr float score: The score for the tone in the range of 0.5 to 1. A score
          greater than 0.75 indicates a high likelihood that the tone is perceived in the
          utterance.
    :attr str tone_id: The unique, non-localized identifier of the tone for the
          results. The service returns results only for tones whose scores meet a minimum
          threshold of 0.5.
    :attr str tone_name: The user-visible, localized name of the tone.
    """

    def __init__(self, score: float, tone_id: str, tone_name: str) -> None:
        """
        Initialize a ToneChatScore object.

        :param float score: The score for the tone in the range of 0.5 to 1. A
               score greater than 0.75 indicates a high likelihood that the tone is
               perceived in the utterance.
        :param str tone_id: The unique, non-localized identifier of the tone for
               the results. The service returns results only for tones whose scores meet a
               minimum threshold of 0.5.
        :param str tone_name: The user-visible, localized name of the tone.
        """
        self.score = score
        self.tone_id = tone_id
        self.tone_name = tone_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToneChatScore':
        """Initialize a ToneChatScore object from a json dictionary."""
        args = {}
        valid_keys = ['score', 'tone_id', 'tone_name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ToneChatScore: '
                + ', '.join(bad_keys))
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        else:
            raise ValueError(
                'Required property \'score\' not present in ToneChatScore JSON')
        if 'tone_id' in _dict:
            args['tone_id'] = _dict.get('tone_id')
        else:
            raise ValueError(
                'Required property \'tone_id\' not present in ToneChatScore JSON'
            )
        if 'tone_name' in _dict:
            args['tone_name'] = _dict.get('tone_name')
        else:
            raise ValueError(
                'Required property \'tone_name\' not present in ToneChatScore JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneChatScore object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'tone_id') and self.tone_id is not None:
            _dict['tone_id'] = self.tone_id
        if hasattr(self, 'tone_name') and self.tone_name is not None:
            _dict['tone_name'] = self.tone_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToneChatScore object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ToneChatScore') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToneChatScore') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ToneIdEnum(Enum):
        """
        The unique, non-localized identifier of the tone for the results. The service
        returns results only for tones whose scores meet a minimum threshold of 0.5.
        """
        EXCITED = "excited"
        FRUSTRATED = "frustrated"
        IMPOLITE = "impolite"
        POLITE = "polite"
        SAD = "sad"
        SATISFIED = "satisfied"
        SYMPATHETIC = "sympathetic"


class ToneInput():
    """
    Input for the general-purpose endpoint.

    :attr str text: The input content that the service is to analyze.
    """

    def __init__(self, text: str) -> None:
        """
        Initialize a ToneInput object.

        :param str text: The input content that the service is to analyze.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToneInput':
        """Initialize a ToneInput object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ToneInput: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in ToneInput JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToneInput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ToneInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToneInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneScore():
    """
    The score for a tone from the input content.

    :attr float score: The score for the tone.
          * **`2017-09-21`:** The score that is returned lies in the range of 0.5 to 1. A
          score greater than 0.75 indicates a high likelihood that the tone is perceived
          in the content.
          * **`2016-05-19`:** The score that is returned lies in the range of 0 to 1. A
          score less than 0.5 indicates that the tone is unlikely to be perceived in the
          content; a score greater than 0.75 indicates a high likelihood that the tone is
          perceived.
    :attr str tone_id: The unique, non-localized identifier of the tone.
          * **`2017-09-21`:** The service can return results for the following tone IDs:
          `anger`, `fear`, `joy`, and `sadness` (emotional tones); `analytical`,
          `confident`, and `tentative` (language tones). The service returns results only
          for tones whose scores meet a minimum threshold of 0.5.
          * **`2016-05-19`:** The service can return results for the following tone IDs of
          the different categories: for the `emotion` category: `anger`, `disgust`,
          `fear`, `joy`, and `sadness`; for the `language` category: `analytical`,
          `confident`, and `tentative`; for the `social` category: `openness_big5`,
          `conscientiousness_big5`, `extraversion_big5`, `agreeableness_big5`, and
          `emotional_range_big5`. The service returns scores for all tones of a category,
          regardless of their values.
    :attr str tone_name: The user-visible, localized name of the tone.
    """

    def __init__(self, score: float, tone_id: str, tone_name: str) -> None:
        """
        Initialize a ToneScore object.

        :param float score: The score for the tone.
               * **`2017-09-21`:** The score that is returned lies in the range of 0.5 to
               1. A score greater than 0.75 indicates a high likelihood that the tone is
               perceived in the content.
               * **`2016-05-19`:** The score that is returned lies in the range of 0 to 1.
               A score less than 0.5 indicates that the tone is unlikely to be perceived
               in the content; a score greater than 0.75 indicates a high likelihood that
               the tone is perceived.
        :param str tone_id: The unique, non-localized identifier of the tone.
               * **`2017-09-21`:** The service can return results for the following tone
               IDs: `anger`, `fear`, `joy`, and `sadness` (emotional tones); `analytical`,
               `confident`, and `tentative` (language tones). The service returns results
               only for tones whose scores meet a minimum threshold of 0.5.
               * **`2016-05-19`:** The service can return results for the following tone
               IDs of the different categories: for the `emotion` category: `anger`,
               `disgust`, `fear`, `joy`, and `sadness`; for the `language` category:
               `analytical`, `confident`, and `tentative`; for the `social` category:
               `openness_big5`, `conscientiousness_big5`, `extraversion_big5`,
               `agreeableness_big5`, and `emotional_range_big5`. The service returns
               scores for all tones of a category, regardless of their values.
        :param str tone_name: The user-visible, localized name of the tone.
        """
        self.score = score
        self.tone_id = tone_id
        self.tone_name = tone_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToneScore':
        """Initialize a ToneScore object from a json dictionary."""
        args = {}
        valid_keys = ['score', 'tone_id', 'tone_name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ToneScore: '
                + ', '.join(bad_keys))
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        else:
            raise ValueError(
                'Required property \'score\' not present in ToneScore JSON')
        if 'tone_id' in _dict:
            args['tone_id'] = _dict.get('tone_id')
        else:
            raise ValueError(
                'Required property \'tone_id\' not present in ToneScore JSON')
        if 'tone_name' in _dict:
            args['tone_name'] = _dict.get('tone_name')
        else:
            raise ValueError(
                'Required property \'tone_name\' not present in ToneScore JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneScore object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'tone_id') and self.tone_id is not None:
            _dict['tone_id'] = self.tone_id
        if hasattr(self, 'tone_name') and self.tone_name is not None:
            _dict['tone_name'] = self.tone_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToneScore object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ToneScore') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToneScore') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Utterance():
    """
    An utterance for the input of the general-purpose endpoint.

    :attr str text: An utterance contributed by a user in the conversation that is
          to be analyzed. The utterance can contain multiple sentences.
    :attr str user: (optional) A string that identifies the user who contributed the
          utterance specified by the `text` parameter.
    """

    def __init__(self, text: str, *, user: str = None) -> None:
        """
        Initialize a Utterance object.

        :param str text: An utterance contributed by a user in the conversation
               that is to be analyzed. The utterance can contain multiple sentences.
        :param str user: (optional) A string that identifies the user who
               contributed the utterance specified by the `text` parameter.
        """
        self.text = text
        self.user = user

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Utterance':
        """Initialize a Utterance object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'user']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Utterance: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in Utterance JSON')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Utterance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Utterance object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Utterance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Utterance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UtteranceAnalyses():
    """
    The results of the analysis for the utterances of the input content.

    :attr List[UtteranceAnalysis] utterances_tone: An array of `UtteranceAnalysis`
          objects that provides the results for each utterance of the input.
    :attr str warning: (optional) **`2017-09-21`:** A warning message if the content
          contains more than 50 utterances. The service analyzes only the first 50
          utterances. **`2016-05-19`:** Not returned.
    """

    def __init__(self,
                 utterances_tone: List['UtteranceAnalysis'],
                 *,
                 warning: str = None) -> None:
        """
        Initialize a UtteranceAnalyses object.

        :param List[UtteranceAnalysis] utterances_tone: An array of
               `UtteranceAnalysis` objects that provides the results for each utterance of
               the input.
        :param str warning: (optional) **`2017-09-21`:** A warning message if the
               content contains more than 50 utterances. The service analyzes only the
               first 50 utterances. **`2016-05-19`:** Not returned.
        """
        self.utterances_tone = utterances_tone
        self.warning = warning

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UtteranceAnalyses':
        """Initialize a UtteranceAnalyses object from a json dictionary."""
        args = {}
        valid_keys = ['utterances_tone', 'warning']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UtteranceAnalyses: '
                + ', '.join(bad_keys))
        if 'utterances_tone' in _dict:
            args['utterances_tone'] = [
                UtteranceAnalysis._from_dict(x)
                for x in (_dict.get('utterances_tone'))
            ]
        else:
            raise ValueError(
                'Required property \'utterances_tone\' not present in UtteranceAnalyses JSON'
            )
        if 'warning' in _dict:
            args['warning'] = _dict.get('warning')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UtteranceAnalyses object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'utterances_tone') and self.utterances_tone is not None:
            _dict['utterances_tone'] = [
                x._to_dict() for x in self.utterances_tone
            ]
        if hasattr(self, 'warning') and self.warning is not None:
            _dict['warning'] = self.warning
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UtteranceAnalyses object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'UtteranceAnalyses') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UtteranceAnalyses') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UtteranceAnalysis():
    """
    The results of the analysis for an utterance of the input content.

    :attr int utterance_id: The unique identifier of the utterance. The first
          utterance has ID 0, and the ID of each subsequent utterance is incremented by
          one.
    :attr str utterance_text: The text of the utterance.
    :attr List[ToneChatScore] tones: An array of `ToneChatScore` objects that
          provides results for the most prevalent tones of the utterance. The array
          includes results for any tone whose score is at least 0.5. The array is empty if
          no tone has a score that meets this threshold.
    :attr str error: (optional) **`2017-09-21`:** An error message if the utterance
          contains more than 500 characters. The service does not analyze the utterance.
          **`2016-05-19`:** Not returned.
    """

    def __init__(self,
                 utterance_id: int,
                 utterance_text: str,
                 tones: List['ToneChatScore'],
                 *,
                 error: str = None) -> None:
        """
        Initialize a UtteranceAnalysis object.

        :param int utterance_id: The unique identifier of the utterance. The first
               utterance has ID 0, and the ID of each subsequent utterance is incremented
               by one.
        :param str utterance_text: The text of the utterance.
        :param List[ToneChatScore] tones: An array of `ToneChatScore` objects that
               provides results for the most prevalent tones of the utterance. The array
               includes results for any tone whose score is at least 0.5. The array is
               empty if no tone has a score that meets this threshold.
        :param str error: (optional) **`2017-09-21`:** An error message if the
               utterance contains more than 500 characters. The service does not analyze
               the utterance. **`2016-05-19`:** Not returned.
        """
        self.utterance_id = utterance_id
        self.utterance_text = utterance_text
        self.tones = tones
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UtteranceAnalysis':
        """Initialize a UtteranceAnalysis object from a json dictionary."""
        args = {}
        valid_keys = ['utterance_id', 'utterance_text', 'tones', 'error']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UtteranceAnalysis: '
                + ', '.join(bad_keys))
        if 'utterance_id' in _dict:
            args['utterance_id'] = _dict.get('utterance_id')
        else:
            raise ValueError(
                'Required property \'utterance_id\' not present in UtteranceAnalysis JSON'
            )
        if 'utterance_text' in _dict:
            args['utterance_text'] = _dict.get('utterance_text')
        else:
            raise ValueError(
                'Required property \'utterance_text\' not present in UtteranceAnalysis JSON'
            )
        if 'tones' in _dict:
            args['tones'] = [
                ToneChatScore._from_dict(x) for x in (_dict.get('tones'))
            ]
        else:
            raise ValueError(
                'Required property \'tones\' not present in UtteranceAnalysis JSON'
            )
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UtteranceAnalysis object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'utterance_id') and self.utterance_id is not None:
            _dict['utterance_id'] = self.utterance_id
        if hasattr(self, 'utterance_text') and self.utterance_text is not None:
            _dict['utterance_text'] = self.utterance_text
        if hasattr(self, 'tones') and self.tones is not None:
            _dict['tones'] = [x._to_dict() for x in self.tones]
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UtteranceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'UtteranceAnalysis') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UtteranceAnalysis') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
