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
The IBM Watson&trade; Tone Analyzer service uses linguistic analysis to detect emotional
and language tones in written text. The service can analyze tone at both the document and
sentence levels. You can use the service to understand how your written communications are
perceived and then to improve the tone of your communications. Businesses can use the
service to learn the tone of their customers' communications and to respond to each
customer appropriately, or to understand and improve their customer conversations.
**Note:** Request logging is disabled for the Tone Analyzer service. The service neither
logs nor retains data from requests and responses, regardless of whether the
`X-Watson-Learning-Opt-Out` request header is set.
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class ToneAnalyzerV3(WatsonService):
    """The Tone Analyzer V3 service."""

    default_url = 'https://gateway.watsonplatform.net/tone-analyzer/api'

    def __init__(
            self,
            version,
            url=default_url,
            username=None,
            password=None,
            iam_apikey=None,
            iam_access_token=None,
            iam_url=None,
    ):
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

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway.watsonplatform.net/tone-analyzer/api").
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
            vcap_services_name='tone_analyzer',
            url=url,
            username=username,
            password=password,
            iam_apikey=iam_apikey,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)
        self.version = version

    #########################
    # Methods
    #########################

    def tone(self,
             tone_input,
             content_type,
             sentences=None,
             tones=None,
             content_language=None,
             accept_language=None,
             **kwargs):
        """
        Analyze general tone.

        Use the general purpose endpoint to analyze the tone of your input content. The
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

        :param ToneInput tone_input: JSON, plain text, or HTML input that contains the
        content to be analyzed. For JSON input, provide an object of type `ToneInput`.
        :param str content_type: The type of the input. A character encoding can be
        specified by including a `charset` parameter. For example,
        'text/plain;charset=utf-8'.
        :param bool sentences: Indicates whether the service is to return an analysis of
        each individual sentence in addition to its analysis of the full document. If
        `true` (the default), the service returns results for each sentence.
        :param list[str] tones: **`2017-09-21`:** Deprecated. The service continues to
        accept the parameter for backward-compatibility, but the parameter no longer
        affects the response.
        **`2016-05-19`:** A comma-separated list of tones for which the service is to
        return its analysis of the input; the indicated tones apply both to the full
        document and to individual sentences of the document. You can specify one or more
        of the valid values. Omit the parameter to request results for all three tones.
        :param str content_language: The language of the input text for the request:
        English or French. Regional variants are treated as their parent language; for
        example, `en-US` is interpreted as `en`. The input content must match the
        specified language. Do not submit content that contains both languages. You can
        use different languages for **Content-Language** and **Accept-Language**.
        * **`2017-09-21`:** Accepts `en` or `fr`.
        * **`2016-05-19`:** Accepts only `en`.
        :param str accept_language: The desired language of the response. For
        two-character arguments, regional variants are treated as their parent language;
        for example, `en-US` is interpreted as `en`. You can use different languages for
        **Content-Language** and **Accept-Language**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if tone_input is None:
            raise ValueError('tone_input must be provided')
        if content_type is None:
            raise ValueError('content_type must be provided')
        if isinstance(tone_input, ToneInput):
            tone_input = self._convert_model(tone_input, ToneInput)
        headers = {
            'Content-Type': content_type,
            'Content-Language': content_language,
            'Accept-Language': accept_language
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
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
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return response

    def tone_chat(self,
                  utterances,
                  content_language=None,
                  accept_language=None,
                  **kwargs):
        """
        Analyze customer engagement tone.

        Use the customer engagement endpoint to analyze the tone of customer service and
        customer support conversations. For each utterance of a conversation, the method
        reports the most prevalent subset of the following seven tones: sad, frustrated,
        satisfied, excited, polite, impolite, and sympathetic.
        If you submit more than 50 utterances, the service returns a warning for the
        overall content and analyzes only the first 50 utterances. If you submit a single
        utterance that contains more than 500 characters, the service returns an error for
        that utterance and does not analyze the utterance. The request fails if all
        utterances have more than 500 characters.
        Per the JSON specification, the default character encoding for JSON content is
        effectively always UTF-8.

        :param list[Utterance] utterances: An array of `Utterance` objects that provides
        the input content that the service is to analyze.
        :param str content_language: The language of the input text for the request:
        English or French. Regional variants are treated as their parent language; for
        example, `en-US` is interpreted as `en`. The input content must match the
        specified language. Do not submit content that contains both languages. You can
        use different languages for **Content-Language** and **Accept-Language**.
        * **`2017-09-21`:** Accepts `en` or `fr`.
        * **`2016-05-19`:** Accepts only `en`.
        :param str accept_language: The desired language of the response. For
        two-character arguments, regional variants are treated as their parent language;
        for example, `en-US` is interpreted as `en`. You can use different languages for
        **Content-Language** and **Accept-Language**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if utterances is None:
            raise ValueError('utterances must be provided')
        utterances = [self._convert_model(x, Utterance) for x in utterances]
        headers = {
            'Content-Language': content_language,
            'Accept-Language': accept_language
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'utterances': utterances}
        url = '/v3/tone_chat'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class DocumentAnalysis(object):
    """
    DocumentAnalysis.

    :attr list[ToneScore] tones: (optional) **`2017-09-21`:** An array of `ToneScore`
    objects that provides the results of the analysis for each qualifying tone of the
    document. The array includes results for any tone whose score is at least 0.5. The
    array is empty if no tone has a score that meets this threshold. **`2016-05-19`:** Not
    returned.
    :attr list[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not returned.
    **`2016-05-19`:** An array of `ToneCategory` objects that provides the results of the
    tone analysis for the full document of the input content. The service returns results
    only for the tones specified with the `tones` parameter of the request.
    :attr str warning: (optional) **`2017-09-21`:** A warning message if the overall
    content exceeds 128 KB or contains more than 1000 sentences. The service analyzes only
    the first 1000 sentences for document-level analysis and the first 100 sentences for
    sentence-level analysis. **`2016-05-19`:** Not returned.
    """

    def __init__(self, tones=None, tone_categories=None, warning=None):
        """
        Initialize a DocumentAnalysis object.

        :param list[ToneScore] tones: (optional) **`2017-09-21`:** An array of `ToneScore`
        objects that provides the results of the analysis for each qualifying tone of the
        document. The array includes results for any tone whose score is at least 0.5. The
        array is empty if no tone has a score that meets this threshold. **`2016-05-19`:**
        Not returned.
        :param list[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not
        returned. **`2016-05-19`:** An array of `ToneCategory` objects that provides the
        results of the tone analysis for the full document of the input content. The
        service returns results only for the tones specified with the `tones` parameter of
        the request.
        :param str warning: (optional) **`2017-09-21`:** A warning message if the overall
        content exceeds 128 KB or contains more than 1000 sentences. The service analyzes
        only the first 1000 sentences for document-level analysis and the first 100
        sentences for sentence-level analysis. **`2016-05-19`:** Not returned.
        """
        self.tones = tones
        self.tone_categories = tone_categories
        self.warning = warning

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentAnalysis object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this DocumentAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentenceAnalysis(object):
    """
    SentenceAnalysis.

    :attr int sentence_id: The unique identifier of a sentence of the input content. The
    first sentence has ID 0, and the ID of each subsequent sentence is incremented by one.
    :attr str text: The text of the input sentence.
    :attr list[ToneScore] tones: (optional) **`2017-09-21`:** An array of `ToneScore`
    objects that provides the results of the analysis for each qualifying tone of the
    sentence. The array includes results for any tone whose score is at least 0.5. The
    array is empty if no tone has a score that meets this threshold. **`2016-05-19`:** Not
    returned.
    :attr list[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not returned.
    **`2016-05-19`:** An array of `ToneCategory` objects that provides the results of the
    tone analysis for the sentence. The service returns results only for the tones
    specified with the `tones` parameter of the request.
    :attr int input_from: (optional) **`2017-09-21`:** Not returned. **`2016-05-19`:** The
    offset of the first character of the sentence in the overall input content.
    :attr int input_to: (optional) **`2017-09-21`:** Not returned. **`2016-05-19`:** The
    offset of the last character of the sentence in the overall input content.
    """

    def __init__(self,
                 sentence_id,
                 text,
                 tones=None,
                 tone_categories=None,
                 input_from=None,
                 input_to=None):
        """
        Initialize a SentenceAnalysis object.

        :param int sentence_id: The unique identifier of a sentence of the input content.
        The first sentence has ID 0, and the ID of each subsequent sentence is incremented
        by one.
        :param str text: The text of the input sentence.
        :param list[ToneScore] tones: (optional) **`2017-09-21`:** An array of `ToneScore`
        objects that provides the results of the analysis for each qualifying tone of the
        sentence. The array includes results for any tone whose score is at least 0.5. The
        array is empty if no tone has a score that meets this threshold. **`2016-05-19`:**
        Not returned.
        :param list[ToneCategory] tone_categories: (optional) **`2017-09-21`:** Not
        returned. **`2016-05-19`:** An array of `ToneCategory` objects that provides the
        results of the tone analysis for the sentence. The service returns results only
        for the tones specified with the `tones` parameter of the request.
        :param int input_from: (optional) **`2017-09-21`:** Not returned.
        **`2016-05-19`:** The offset of the first character of the sentence in the overall
        input content.
        :param int input_to: (optional) **`2017-09-21`:** Not returned. **`2016-05-19`:**
        The offset of the last character of the sentence in the overall input content.
        """
        self.sentence_id = sentence_id
        self.text = text
        self.tones = tones
        self.tone_categories = tone_categories
        self.input_from = input_from
        self.input_to = input_to

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentenceAnalysis object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this SentenceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneAnalysis(object):
    """
    ToneAnalysis.

    :attr DocumentAnalysis document_tone: An object of type `DocumentAnalysis` that
    provides the results of the analysis for the full input document.
    :attr list[SentenceAnalysis] sentences_tone: (optional) An array of `SentenceAnalysis`
    objects that provides the results of the analysis for the individual sentences of the
    input content. The service returns results only for the first 100 sentences of the
    input. The field is omitted if the `sentences` parameter of the request is set to
    `false`.
    """

    def __init__(self, document_tone, sentences_tone=None):
        """
        Initialize a ToneAnalysis object.

        :param DocumentAnalysis document_tone: An object of type `DocumentAnalysis` that
        provides the results of the analysis for the full input document.
        :param list[SentenceAnalysis] sentences_tone: (optional) An array of
        `SentenceAnalysis` objects that provides the results of the analysis for the
        individual sentences of the input content. The service returns results only for
        the first 100 sentences of the input. The field is omitted if the `sentences`
        parameter of the request is set to `false`.
        """
        self.document_tone = document_tone
        self.sentences_tone = sentences_tone

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneAnalysis object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document_tone') and self.document_tone is not None:
            _dict['document_tone'] = self.document_tone._to_dict()
        if hasattr(self, 'sentences_tone') and self.sentences_tone is not None:
            _dict['sentences_tone'] = [
                x._to_dict() for x in self.sentences_tone
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this ToneAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneCategory(object):
    """
    ToneCategory.

    :attr list[ToneScore] tones: An array of `ToneScore` objects that provides the results
    for the tones of the category.
    :attr str category_id: The unique, non-localized identifier of the category for the
    results. The service can return results for the following category IDs:
    `emotion_tone`, `language_tone`, and `social_tone`.
    :attr str category_name: The user-visible, localized name of the category.
    """

    def __init__(self, tones, category_id, category_name):
        """
        Initialize a ToneCategory object.

        :param list[ToneScore] tones: An array of `ToneScore` objects that provides the
        results for the tones of the category.
        :param str category_id: The unique, non-localized identifier of the category for
        the results. The service can return results for the following category IDs:
        `emotion_tone`, `language_tone`, and `social_tone`.
        :param str category_name: The user-visible, localized name of the category.
        """
        self.tones = tones
        self.category_id = category_id
        self.category_name = category_name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneCategory object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tones') and self.tones is not None:
            _dict['tones'] = [x._to_dict() for x in self.tones]
        if hasattr(self, 'category_id') and self.category_id is not None:
            _dict['category_id'] = self.category_id
        if hasattr(self, 'category_name') and self.category_name is not None:
            _dict['category_name'] = self.category_name
        return _dict

    def __str__(self):
        """Return a `str` version of this ToneCategory object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneChatScore(object):
    """
    ToneChatScore.

    :attr float score: The score for the tone in the range of 0.5 to 1. A score greater
    than 0.75 indicates a high likelihood that the tone is perceived in the utterance.
    :attr str tone_id: The unique, non-localized identifier of the tone for the results.
    The service can return results for the following tone IDs: `sad`, `frustrated`,
    `satisfied`, `excited`, `polite`, `impolite`, and `sympathetic`. The service returns
    results only for tones whose scores meet a minimum threshold of 0.5.
    :attr str tone_name: The user-visible, localized name of the tone.
    """

    def __init__(self, score, tone_id, tone_name):
        """
        Initialize a ToneChatScore object.

        :param float score: The score for the tone in the range of 0.5 to 1. A score
        greater than 0.75 indicates a high likelihood that the tone is perceived in the
        utterance.
        :param str tone_id: The unique, non-localized identifier of the tone for the
        results. The service can return results for the following tone IDs: `sad`,
        `frustrated`, `satisfied`, `excited`, `polite`, `impolite`, and `sympathetic`. The
        service returns results only for tones whose scores meet a minimum threshold of
        0.5.
        :param str tone_name: The user-visible, localized name of the tone.
        """
        self.score = score
        self.tone_id = tone_id
        self.tone_name = tone_name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneChatScore object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'tone_id') and self.tone_id is not None:
            _dict['tone_id'] = self.tone_id
        if hasattr(self, 'tone_name') and self.tone_name is not None:
            _dict['tone_name'] = self.tone_name
        return _dict

    def __str__(self):
        """Return a `str` version of this ToneChatScore object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneInput(object):
    """
    ToneInput.

    :attr str text: The input content that the service is to analyze.
    """

    def __init__(self, text):
        """
        Initialize a ToneInput object.

        :param str text: The input content that the service is to analyze.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneInput object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in ToneInput JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this ToneInput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToneScore(object):
    """
    ToneScore.

    :attr float score: The score for the tone.
    * **`2017-09-21`:** The score that is returned lies in the range of 0.5 to 1. A score
    greater than 0.75 indicates a high likelihood that the tone is perceived in the
    content.
    * **`2016-05-19`:** The score that is returned lies in the range of 0 to 1. A score
    less than 0.5 indicates that the tone is unlikely to be perceived in the content; a
    score greater than 0.75 indicates a high likelihood that the tone is perceived.
    :attr str tone_id: The unique, non-localized identifier of the tone.
    * **`2017-09-21`:** The service can return results for the following tone IDs:
    `anger`, `fear`, `joy`, and `sadness` (emotional tones); `analytical`, `confident`,
    and `tentative` (language tones). The service returns results only for tones whose
    scores meet a minimum threshold of 0.5.
    * **`2016-05-19`:** The service can return results for the following tone IDs of the
    different categories: for the `emotion` category: `anger`, `disgust`, `fear`, `joy`,
    and `sadness`; for the `language` category: `analytical`, `confident`, and
    `tentative`; for the `social` category: `openness_big5`, `conscientiousness_big5`,
    `extraversion_big5`, `agreeableness_big5`, and `emotional_range_big5`. The service
    returns scores for all tones of a category, regardless of their values.
    :attr str tone_name: The user-visible, localized name of the tone.
    """

    def __init__(self, score, tone_id, tone_name):
        """
        Initialize a ToneScore object.

        :param float score: The score for the tone.
        * **`2017-09-21`:** The score that is returned lies in the range of 0.5 to 1. A
        score greater than 0.75 indicates a high likelihood that the tone is perceived in
        the content.
        * **`2016-05-19`:** The score that is returned lies in the range of 0 to 1. A
        score less than 0.5 indicates that the tone is unlikely to be perceived in the
        content; a score greater than 0.75 indicates a high likelihood that the tone is
        perceived.
        :param str tone_id: The unique, non-localized identifier of the tone.
        * **`2017-09-21`:** The service can return results for the following tone IDs:
        `anger`, `fear`, `joy`, and `sadness` (emotional tones); `analytical`,
        `confident`, and `tentative` (language tones). The service returns results only
        for tones whose scores meet a minimum threshold of 0.5.
        * **`2016-05-19`:** The service can return results for the following tone IDs of
        the different categories: for the `emotion` category: `anger`, `disgust`, `fear`,
        `joy`, and `sadness`; for the `language` category: `analytical`, `confident`, and
        `tentative`; for the `social` category: `openness_big5`, `conscientiousness_big5`,
        `extraversion_big5`, `agreeableness_big5`, and `emotional_range_big5`. The service
        returns scores for all tones of a category, regardless of their values.
        :param str tone_name: The user-visible, localized name of the tone.
        """
        self.score = score
        self.tone_id = tone_id
        self.tone_name = tone_name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneScore object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'tone_id') and self.tone_id is not None:
            _dict['tone_id'] = self.tone_id
        if hasattr(self, 'tone_name') and self.tone_name is not None:
            _dict['tone_name'] = self.tone_name
        return _dict

    def __str__(self):
        """Return a `str` version of this ToneScore object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Utterance(object):
    """
    Utterance.

    :attr str text: An utterance contributed by a user in the conversation that is to be
    analyzed. The utterance can contain multiple sentences.
    :attr str user: (optional) A string that identifies the user who contributed the
    utterance specified by the `text` parameter.
    """

    def __init__(self, text, user=None):
        """
        Initialize a Utterance object.

        :param str text: An utterance contributed by a user in the conversation that is to
        be analyzed. The utterance can contain multiple sentences.
        :param str user: (optional) A string that identifies the user who contributed the
        utterance specified by the `text` parameter.
        """
        self.text = text
        self.user = user

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Utterance object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in Utterance JSON')
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        return _dict

    def __str__(self):
        """Return a `str` version of this Utterance object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UtteranceAnalyses(object):
    """
    UtteranceAnalyses.

    :attr list[UtteranceAnalysis] utterances_tone: An array of `UtteranceAnalysis` objects
    that provides the results for each utterance of the input.
    :attr str warning: (optional) **`2017-09-21`:** A warning message if the content
    contains more than 50 utterances. The service analyzes only the first 50 utterances.
    **`2016-05-19`:** Not returned.
    """

    def __init__(self, utterances_tone, warning=None):
        """
        Initialize a UtteranceAnalyses object.

        :param list[UtteranceAnalysis] utterances_tone: An array of `UtteranceAnalysis`
        objects that provides the results for each utterance of the input.
        :param str warning: (optional) **`2017-09-21`:** A warning message if the content
        contains more than 50 utterances. The service analyzes only the first 50
        utterances. **`2016-05-19`:** Not returned.
        """
        self.utterances_tone = utterances_tone
        self.warning = warning

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UtteranceAnalyses object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this UtteranceAnalyses object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UtteranceAnalysis(object):
    """
    UtteranceAnalysis.

    :attr int utterance_id: The unique identifier of the utterance. The first utterance
    has ID 0, and the ID of each subsequent utterance is incremented by one.
    :attr str utterance_text: The text of the utterance.
    :attr list[ToneChatScore] tones: An array of `ToneChatScore` objects that provides
    results for the most prevalent tones of the utterance. The array includes results for
    any tone whose score is at least 0.5. The array is empty if no tone has a score that
    meets this threshold.
    :attr str error: (optional) **`2017-09-21`:** An error message if the utterance
    contains more than 500 characters. The service does not analyze the utterance.
    **`2016-05-19`:** Not returned.
    """

    def __init__(self, utterance_id, utterance_text, tones, error=None):
        """
        Initialize a UtteranceAnalysis object.

        :param int utterance_id: The unique identifier of the utterance. The first
        utterance has ID 0, and the ID of each subsequent utterance is incremented by one.
        :param str utterance_text: The text of the utterance.
        :param list[ToneChatScore] tones: An array of `ToneChatScore` objects that
        provides results for the most prevalent tones of the utterance. The array includes
        results for any tone whose score is at least 0.5. The array is empty if no tone
        has a score that meets this threshold.
        :param str error: (optional) **`2017-09-21`:** An error message if the utterance
        contains more than 500 characters. The service does not analyze the utterance.
        **`2016-05-19`:** Not returned.
        """
        self.utterance_id = utterance_id
        self.utterance_text = utterance_text
        self.tones = tones
        self.error = error

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UtteranceAnalysis object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this UtteranceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
