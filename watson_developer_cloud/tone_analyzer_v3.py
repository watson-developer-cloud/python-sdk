# coding: utf-8

# Copyright 2017 IBM All Rights Reserved.
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
### Service Overview The IBM Watson Tone Analyzer service uses linguistic analysis to detect emotional, social, and language tones in written text. The service can analyze tone at both the document and sentence levels. You can use the service to understand how your written communications are perceived and then to improve the tone of your communications. Businesses can use the service to learn the tone of their customers' communications and to respond to each customer appropriately, or to understand and improve their customer conversations. ### API Usage The following information provides details about using the service to analyze tone: * **The tone method:** The service offers `GET` and `POST /v3/tone` methods that use the general purpose endpoint to analyze the tone of input content. The methods accept a maximum of 128 KB of content in JSON, plain text, or HTML format. * **The tone_chat method:** The service offers a `POST /v3/tone_chat` method that uses the customer engagement endpoint to analyze the tone of customer service and customer support conversations. The method accepts a maximum of 128 KB of content in JSON format. * **Authentication:** You authenticate to the service by using your service credentials. You can use your credentials to authenticate via a proxy server that resides in Bluemix, or you can use your credentials to obtain a token and contact the service directly. See [Service credentials for Watson services](https://console.bluemix.net/docs/services/watson/getting-started-credentials.html) and [Tokens for authentication](https://console.bluemix.net/docs/services/watson/getting-started-tokens.html). * **Request Logging:** By default, all Watson services log requests and their results. Data is collected only to improve the Watson services. If you do not want to share your data, set the header parameter `X-Watson-Learning-Opt-Out` to `true` for each request. Data is collected for any request that omits this header. See [Controlling request logging for Watson services](https://console.bluemix.net/docs/services/watson/getting-started-logging.html).   For more information about the service, see [About Tone Analyzer](https://console.bluemix.net/docs/services/tone-analyzer/index.html).
"""

import json
from .watson_developer_cloud_service import WatsonDeveloperCloudService

##############################################################################
# Service
##############################################################################


class ToneAnalyzerV3(WatsonDeveloperCloudService):
    """Client for the Tone Analyzer service."""

    default_url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    latest_version = ''

    def __init__(self,
                 version,
                 url=default_url,
                 username=None,
                 password=None,
                 x_watson_learning_opt_out=False):
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

        :param bool x_watson_learning_opt_out: Set this parameter to `True`
               to prevent IBM from accessing your data for general service
               improvements. By default, all IBM Watson services log requests
               and their results. Logging is done only to improve the services
               for future users. The logged data is not shared or made public.
               If you are concerned with protecting the privacy of users
               personal information or otherwise do not want your requests to
               be logged, you can opt out of logging.
        """

        WatsonDeveloperCloudService.__init__(
            self,
            vcap_services_name='tone_analyzer',
            url=url,
            username=username,
            password=password,
            use_vcap_services=True,
            api_key=None,
            x_watson_learning_opt_out=x_watson_learning_opt_out)
        self.version = version

    #########################
    # tone
    #########################

    def tone(self,
             tone_input,
             content_type='application/json',
             tones=None,
             sentences=None):
        """
        Analyze general purpose tone.

        Uses the general purpose endpoint to analyze the tone of your input content. The service can analyze the input for several tones: emotion, language, and social. It derives various characteristics for each tone that it analyzes. The method always analyzes the tone of the full document; by default, it also analyzes the tone of each individual sentence of the input. You can submit a maximum of 128 KB of content in JSON, plain text, or HTML format.   Per the JSON specification, the default character encoding for JSON content is effectively always UTF-8; per the HTTP specification, the default encoding for plain text and HTML is ISO-8859-1 (effectively, the ASCII character set). When specifying a content type of plain text or HTML, include the `charset` parameter to indicate the character encoding of the input text; for example: `Content-Type: text/plain;charset=utf-8`. For `text/html`, the service removes HTML tags and analyzes only the textual content.   Use the `POST` request method to analyze larger amounts of content in any of the available formats. Use the `GET` request method to analyze smaller quantities of plain text content.

        :param ToneInput tone_input: JSON, plain text, or HTML input that contains the content to be analyzed. For JSON input, provide an object of type `ToneInput`. Submit a maximum of 128 KB of content. Sentences with fewer than three words cannot be analyzed.
        :param str content_type: The type of the input: application/json, text/plain, or text/html. A character encoding can be specified by including a `charset` parameter. For example, 'text/plain;charset=utf-8'.
        :param list[str] tones: A comma-separated list of tones for which the service is to return its analysis of the input; the indicated tones apply both to the full document and to individual sentences of the document. You can specify one or more of the following values: `emotion`, `language`, and `social`. Omit the parameter to request results for all three tones.
        :param bool sentences: Indicates whether the service is to return an analysis of each individual sentence in addition to its analysis of the full document. If `true` (the default), the service returns results for each sentence. The service returns results only for the first 100 sentences of the input.
        :return: A `ToneAnalysis` object
        :rtype: watson_developer_cloud.tone_analyzer_v3.ToneAnalysis
        """
        headers = {'content-type': content_type}
        params = {
            'version': self.version,
            'tones': ",".join(tones) if isinstance(tones, list) else tones,
            'sentences': sentences
        }
        if content_type == 'application/json' and isinstance(tone_input, dict):
            data = json.dumps(tone_input)
        else:
            data = tone_input
        response = self.request(
            method='POST',
            url='/v3/tone',
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return ToneAnalysis._from_dict(response)

    def tone_chat(self, utterances):
        """
        Analyze customer engagement tone.

        Uses the customer engagement endpoint to analyze the tone of customer service and customer support conversations. For each utterance of a conversation, the method reports the most prevalent subset of the following seven tones: sad, frustrated, satisfied, excited, polite, impolite, and sympathetic. You can submit a maximum of 128 KB of JSON input. Per the JSON specification, the default character encoding for JSON content is effectively always UTF-8.

        :param list[Utterance] utterances: An array of `Utterance` objects that provides the input content that the service is to analyze.
        :return: A `UtteranceAnalyses` object
        :rtype: watson_developer_cloud.tone_analyzer_v3.UtteranceAnalyses
        """
        utterances = [
            x._to_dict() if hasattr(x, "_to_dict") else x for x in utterances
        ]
        params = {'version': self.version}
        data = {'utterances': utterances}
        response = self.request(
            method='POST',
            url='/v3/tone_chat',
            params=params,
            json=data,
            accept_json=True)
        return UtteranceAnalyses._from_dict(response)


##############################################################################
# Models
##############################################################################


class DocumentAnalysis(object):
    """
    DocumentAnalysis.

    :attr list[ToneCategory] tone_categories: An array of `ToneCategory` objects that provides the results of the tone analysis for the full document of the input content. The service returns results only for the tones specified with the `tones` parameter of the request.
    """

    def __init__(self, tone_categories):
        """
        Initialize a DocumentAnalysis object.

        :param list[ToneCategory] tone_categories: An array of `ToneCategory` objects that provides the results of the tone analysis for the full document of the input content. The service returns results only for the tones specified with the `tones` parameter of the request.
        """
        self.tone_categories = tone_categories

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentAnalysis object from a json dictionary."""
        args = {}
        if 'tone_categories' in _dict:
            args['tone_categories'] = [
                ToneCategory._from_dict(x) for x in _dict['tone_categories']
            ]
        else:
            raise ValueError(
                'Required property \'tone_categories\' not present in DocumentAnalysis dict'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'tone_categories') and self.tone_categories is not None:
            _dict['tone_categories'] = [
                x._to_dict() for x in self.tone_categories
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this DocumentAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)


class SentenceAnalysis(object):
    """
    SentenceAnalysis.

    :attr int sentence_id: The unique identifier of a sentence of the input content. The first sentence has ID 0, and the ID of each subsequent sentence is incremented by one.
    :attr str text: The text of the input sentence.
    :attr int input_from: The offset of the first character of the sentence in the overall input content.
    :attr int input_to: The offset of the last character of the sentence in the overall input content.
    :attr list[ToneCategory] tone_categories: An array of `ToneCategory` objects that provides the results for the tone analysis of the sentence. The service returns results only for the tones specified with the `tones` parameter of the request.
    """

    def __init__(self, sentence_id, text, input_from, input_to,
                 tone_categories):
        """
        Initialize a SentenceAnalysis object.

        :param int sentence_id: The unique identifier of a sentence of the input content. The first sentence has ID 0, and the ID of each subsequent sentence is incremented by one.
        :param str text: The text of the input sentence.
        :param int input_from: The offset of the first character of the sentence in the overall input content.
        :param int input_to: The offset of the last character of the sentence in the overall input content.
        :param list[ToneCategory] tone_categories: An array of `ToneCategory` objects that provides the results for the tone analysis of the sentence. The service returns results only for the tones specified with the `tones` parameter of the request.
        """
        self.sentence_id = sentence_id
        self.text = text
        self.input_from = input_from
        self.input_to = input_to
        self.tone_categories = tone_categories

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentenceAnalysis object from a json dictionary."""
        args = {}
        if 'sentence_id' in _dict:
            args['sentence_id'] = _dict['sentence_id']
        else:
            raise ValueError(
                'Required property \'sentence_id\' not present in SentenceAnalysis dict'
            )
        if 'text' in _dict:
            args['text'] = _dict['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in SentenceAnalysis dict'
            )
        if 'input_from' in _dict:
            args['input_from'] = _dict['input_from']
        else:
            raise ValueError(
                'Required property \'input_from\' not present in SentenceAnalysis dict'
            )
        if 'input_to' in _dict:
            args['input_to'] = _dict['input_to']
        else:
            raise ValueError(
                'Required property \'input_to\' not present in SentenceAnalysis dict'
            )
        if 'tone_categories' in _dict:
            args['tone_categories'] = [
                ToneCategory._from_dict(x) for x in _dict['tone_categories']
            ]
        else:
            raise ValueError(
                'Required property \'tone_categories\' not present in SentenceAnalysis dict'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sentence_id') and self.sentence_id is not None:
            _dict['sentence_id'] = self.sentence_id
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'input_from') and self.input_from is not None:
            _dict['input_from'] = self.input_from
        if hasattr(self, 'input_to') and self.input_to is not None:
            _dict['input_to'] = self.input_to
        if hasattr(self,
                   'tone_categories') and self.tone_categories is not None:
            _dict['tone_categories'] = [
                x._to_dict() for x in self.tone_categories
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this SentenceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)


class ToneAnalysis(object):
    """
    ToneAnalysis.

    :attr DocumentAnalysis document_tone: An object of type `DocumentAnalysis` that provides the results for the full document of the input content.
    :attr list[SentenceAnalysis] sentences_tone: (optional) An array of `SentenceAnalysis` objects that provides the results for the individual sentences of the input content. The service returns results only for the first 100 sentences of the input. The field is omitted if the `sentences` parameter of the request is set to `false`.
    """

    def __init__(self, document_tone, sentences_tone=None):
        """
        Initialize a ToneAnalysis object.

        :param DocumentAnalysis document_tone: An object of type `DocumentAnalysis` that provides the results for the full document of the input content.
        :param list[SentenceAnalysis] sentences_tone: (optional) An array of `SentenceAnalysis` objects that provides the results for the individual sentences of the input content. The service returns results only for the first 100 sentences of the input. The field is omitted if the `sentences` parameter of the request is set to `false`.
        """
        self.document_tone = document_tone
        self.sentences_tone = sentences_tone

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneAnalysis object from a json dictionary."""
        args = {}
        if 'document_tone' in _dict:
            args['document_tone'] = DocumentAnalysis._from_dict(
                _dict['document_tone'])
        else:
            raise ValueError(
                'Required property \'document_tone\' not present in ToneAnalysis dict'
            )
        if 'sentences_tone' in _dict:
            args['sentences_tone'] = [
                SentenceAnalysis._from_dict(x) for x in _dict['sentences_tone']
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


class ToneCategory(object):
    """
    ToneCategory.

    :attr list[ToneScore] tones: An array of `ToneScore` objects that provides the results for the tones of the category.
    :attr str category_id: The unique, non-localized identifier of the category for the results. The service can return results for the following category IDs: `emotion_tone`, `language_tone`, and `social_tone`.
    :attr str category_name: The user-visible, localized name of the category.
    """

    def __init__(self, tones, category_id, category_name):
        """
        Initialize a ToneCategory object.

        :param list[ToneScore] tones: An array of `ToneScore` objects that provides the results for the tones of the category.
        :param str category_id: The unique, non-localized identifier of the category for the results. The service can return results for the following category IDs: `emotion_tone`, `language_tone`, and `social_tone`.
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
            args['tones'] = [ToneScore._from_dict(x) for x in _dict['tones']]
        else:
            raise ValueError(
                'Required property \'tones\' not present in ToneCategory dict')
        if 'category_id' in _dict:
            args['category_id'] = _dict['category_id']
        else:
            raise ValueError(
                'Required property \'category_id\' not present in ToneCategory dict'
            )
        if 'category_name' in _dict:
            args['category_name'] = _dict['category_name']
        else:
            raise ValueError(
                'Required property \'category_name\' not present in ToneCategory dict'
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


class ToneChatInput(object):
    """
    ToneChatInput.

    :attr list[Utterance] utterances: An array of `Utterance` objects that provides the input content that the service is to analyze.
    """

    def __init__(self, utterances):
        """
        Initialize a ToneChatInput object.

        :param list[Utterance] utterances: An array of `Utterance` objects that provides the input content that the service is to analyze.
        """
        self.utterances = utterances

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneChatInput object from a json dictionary."""
        args = {}
        if 'utterances' in _dict:
            args['utterances'] = [
                Utterance._from_dict(x) for x in _dict['utterances']
            ]
        else:
            raise ValueError(
                'Required property \'utterances\' not present in ToneChatInput dict'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'utterances') and self.utterances is not None:
            _dict['utterances'] = [x._to_dict() for x in self.utterances]
        return _dict

    def __str__(self):
        """Return a `str` version of this ToneChatInput object."""
        return json.dumps(self._to_dict(), indent=2)


class ToneChatScore(object):
    """
    ToneChatScore.

    :attr float score: The score for the tone in the range of 0.5 to 1. A score greater than 0.75 indicates a high likelihood that the tone is perceived in the utterance.
    :attr str tone_id: The unique, non-localized identifier of the tone for the results. The service can return results for the following tone IDs: `sad`, `frustrated`, `satisfied`, `excited`, `polite`, `impolite`, and `sympathetic`. The service returns results only for tones whose scores meet a minimum threshold of 0.5.
    :attr str tone_name: The user-visible, localized name of the tone.
    """

    def __init__(self, score, tone_id, tone_name):
        """
        Initialize a ToneChatScore object.

        :param float score: The score for the tone in the range of 0.5 to 1. A score greater than 0.75 indicates a high likelihood that the tone is perceived in the utterance.
        :param str tone_id: The unique, non-localized identifier of the tone for the results. The service can return results for the following tone IDs: `sad`, `frustrated`, `satisfied`, `excited`, `polite`, `impolite`, and `sympathetic`. The service returns results only for tones whose scores meet a minimum threshold of 0.5.
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
            args['score'] = _dict['score']
        else:
            raise ValueError(
                'Required property \'score\' not present in ToneChatScore dict'
            )
        if 'tone_id' in _dict:
            args['tone_id'] = _dict['tone_id']
        else:
            raise ValueError(
                'Required property \'tone_id\' not present in ToneChatScore dict'
            )
        if 'tone_name' in _dict:
            args['tone_name'] = _dict['tone_name']
        else:
            raise ValueError(
                'Required property \'tone_name\' not present in ToneChatScore dict'
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


class ToneInput(object):
    """
    ToneInput.

    :attr str text: The input content that the service is to analyze. Sentences with fewer than three words cannot be analyzed.
    """

    def __init__(self, text):
        """
        Initialize a ToneInput object.

        :param str text: The input content that the service is to analyze. Sentences with fewer than three words cannot be analyzed.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToneInput object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in ToneInput dict')
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


class ToneScore(object):
    """
    ToneScore.

    :attr float score: The score for the tone in the range of 0 to 1. A score less than 0.5 indicates that the tone is unlikely to be perceived in the content; a score greater than 0.75 indicates a high likelihood that the tone is perceived.
    :attr str tone_id: The unique, non-localized identifier of the tone for the results. The service can return results for the following tone IDs of the different categories: * For the `emotion` category: `anger`, `disgust`, `fear`, `joy`, and `sadness` * For the `language` category: `analytical`, `confident`, and `tentative` * For the `social` category: `openness_big5`, `conscientiousness_big5`, `extraversion_big5`, `agreeableness_big5`, and `emotional_range_big5`   The service returns scores for all tones of a category, regardless of their values.
    :attr str tone_name: The user-visible, localized name of the tone.
    """

    def __init__(self, score, tone_id, tone_name):
        """
        Initialize a ToneScore object.

        :param float score: The score for the tone in the range of 0 to 1. A score less than 0.5 indicates that the tone is unlikely to be perceived in the content; a score greater than 0.75 indicates a high likelihood that the tone is perceived.
        :param str tone_id: The unique, non-localized identifier of the tone for the results. The service can return results for the following tone IDs of the different categories: * For the `emotion` category: `anger`, `disgust`, `fear`, `joy`, and `sadness` * For the `language` category: `analytical`, `confident`, and `tentative` * For the `social` category: `openness_big5`, `conscientiousness_big5`, `extraversion_big5`, `agreeableness_big5`, and `emotional_range_big5`   The service returns scores for all tones of a category, regardless of their values.
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
            args['score'] = _dict['score']
        else:
            raise ValueError(
                'Required property \'score\' not present in ToneScore dict')
        if 'tone_id' in _dict:
            args['tone_id'] = _dict['tone_id']
        else:
            raise ValueError(
                'Required property \'tone_id\' not present in ToneScore dict')
        if 'tone_name' in _dict:
            args['tone_name'] = _dict['tone_name']
        else:
            raise ValueError(
                'Required property \'tone_name\' not present in ToneScore dict'
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
        """Return a `str` version of this ToneScore object."""
        return json.dumps(self._to_dict(), indent=2)


class Utterance(object):
    """
    Utterance.

    :attr str text: An utterance contributed by a user in the conversation that is to be analyzed. The utterance can contain multiple sentences.
    :attr str user: (optional) A string that identifies the user who contributed the utterance specified by the `text` parameter.
    """

    def __init__(self, text, user=None):
        """
        Initialize a Utterance object.

        :param str text: An utterance contributed by a user in the conversation that is to be analyzed. The utterance can contain multiple sentences.
        :param str user: (optional) A string that identifies the user who contributed the utterance specified by the `text` parameter.
        """
        self.text = text
        self.user = user

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Utterance object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in Utterance dict')
        if 'user' in _dict:
            args['user'] = _dict['user']
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


class UtteranceAnalyses(object):
    """
    UtteranceAnalyses.

    :attr list[UtteranceAnalysis] utterances_tone: An array of `UtteranceAnalysis` objects that provides the results for each utterance of the input.
    """

    def __init__(self, utterances_tone):
        """
        Initialize a UtteranceAnalyses object.

        :param list[UtteranceAnalysis] utterances_tone: An array of `UtteranceAnalysis` objects that provides the results for each utterance of the input.
        """
        self.utterances_tone = utterances_tone

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UtteranceAnalyses object from a json dictionary."""
        args = {}
        if 'utterances_tone' in _dict:
            args['utterances_tone'] = [
                UtteranceAnalysis._from_dict(x)
                for x in _dict['utterances_tone']
            ]
        else:
            raise ValueError(
                'Required property \'utterances_tone\' not present in UtteranceAnalyses dict'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'utterances_tone') and self.utterances_tone is not None:
            _dict['utterances_tone'] = [
                x._to_dict() for x in self.utterances_tone
            ]
        return _dict

    def __str__(self):
        """Return a `str` version of this UtteranceAnalyses object."""
        return json.dumps(self._to_dict(), indent=2)


class UtteranceAnalysis(object):
    """
    UtteranceAnalysis.

    :attr str utterance_id: The unique identifier of the utterance. The first utterance has ID 0, and the ID of each subsequent utterance is incremented by one.
    :attr str utterance_text: The text of the utterance.
    :attr list[ToneChatScore] tones: An array of `ToneChatScore` objects that provides results for the most prevalent tones of the utterance. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
    """

    def __init__(self, utterance_id, utterance_text, tones):
        """
        Initialize a UtteranceAnalysis object.

        :param str utterance_id: The unique identifier of the utterance. The first utterance has ID 0, and the ID of each subsequent utterance is incremented by one.
        :param str utterance_text: The text of the utterance.
        :param list[ToneChatScore] tones: An array of `ToneChatScore` objects that provides results for the most prevalent tones of the utterance. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
        """
        self.utterance_id = utterance_id
        self.utterance_text = utterance_text
        self.tones = tones

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UtteranceAnalysis object from a json dictionary."""
        args = {}
        if 'utterance_id' in _dict:
            args['utterance_id'] = _dict['utterance_id']
        else:
            raise ValueError(
                'Required property \'utterance_id\' not present in UtteranceAnalysis dict'
            )
        if 'utterance_text' in _dict:
            args['utterance_text'] = _dict['utterance_text']
        else:
            raise ValueError(
                'Required property \'utterance_text\' not present in UtteranceAnalysis dict'
            )
        if 'tones' in _dict:
            args['tones'] = [
                ToneChatScore._from_dict(x) for x in _dict['tones']
            ]
        else:
            raise ValueError(
                'Required property \'tones\' not present in UtteranceAnalysis dict'
            )
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
        return _dict

    def __str__(self):
        """Return a `str` version of this UtteranceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)
