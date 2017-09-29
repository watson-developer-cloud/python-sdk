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
### Service Overview The IBM Watson Tone Analyzer service uses linguistic analysis to detect emotional and language tones in written text. The service can analyze tone at both the document and sentence levels. You can use the service to understand how your written communications are perceived and then to improve the tone of your communications. Businesses can use the service to learn the tone of their customers' communications and to respond to each customer appropriately, or to understand and improve their customer conversations. ### API Usage The following information provides details about using the service to analyze tone: * **The tone method:** The service offers `GET` and `POST /v3/tone` methods that use the general purpose endpoint to analyze the tone of input content. The methods accept content in JSON, plain text, or HTML format. * **The tone_chat method:** The service offers a `POST /v3/tone_chat` method that uses the customer engagement endpoint to analyze the tone of customer service and customer support conversations. The method accepts content in JSON format. * **Authentication:** You authenticate to the service by using your service credentials. You can use your credentials to authenticate via a proxy server that resides in Bluemix, or you can use your credentials to obtain a token and contact the service directly. See [Service credentials for Watson services](https://console.bluemix.net/docs/services/watson/getting-started-credentials.html) and [Tokens for authentication](https://console.bluemix.net/docs/services/watson/getting-started-tokens.html). * **Request Logging:** By default, all Watson services log requests and their results. Data is collected only to improve the Watson services. If you do not want to share your data, set the header parameter `X-Watson-Learning-Opt-Out` to `true` for each request. Data is collected for any request that omits this header. See [Controlling request logging for Watson services](https://console.bluemix.net/docs/services/watson/getting-started-logging.html).   For more information about the service, see [About Tone Analyzer](https://console.bluemix.net/docs/services/tone-analyzer/index.html).
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
             sentences=None,
             content_language=None,
             accept_language=None):
        """
        Analyze general purpose tone.

        Uses the general purpose endpoint to analyze the tone of your input content. The service analyzes the content for emotional and language tones. The method always analyzes the tone of the full document; by default, it also analyzes the tone of each individual sentence of the content.   You can submit no more than 128 KB of total input content and no more than 1000 individual sentences in JSON, plain text, or HTML format. The service analyzes the first 1000 sentences for document-level analysis and only the first 100 sentences for sentence-level analysis.   Use the `POST` request method to analyze larger amounts of content in any of the available formats. Use the `GET` request method to analyze smaller quantities of plain text content.   Per the JSON specification, the default character encoding for JSON content is effectively always UTF-8; per the HTTP specification, the default encoding for plain text and HTML is ISO-8859-1 (effectively, the ASCII character set). When specifying a content type of plain text or HTML, include the `charset` parameter to indicate the character encoding of the input text; for example: `Content-Type: text/plain;charset=utf-8`. For `text/html`, the service removes HTML tags and analyzes only the textual content.   **Note:** The `tones` query parameter is no longer supported. The service continues to accept the parameter for backward-compatibility, but the parameter no longer affects the response.

        :param ToneInput tone_input: JSON, plain text, or HTML input that contains the content to be analyzed. For JSON input, provide an object of type `ToneInput`.
        :param str content_type: The type of the input: application/json, text/plain, or text/html. A character encoding can be specified by including a `charset` parameter. For example, 'text/plain;charset=utf-8'.
        :param bool sentences: Indicates whether the service is to return an analysis of each individual sentence in addition to its analysis of the full document. If `true` (the default), the service returns results for each sentence.
        :param str content_language: The language of the input text for the request: English or French. Regional variants are treated as their parent language; for example, `en-US` is interpreted as `en`. The input content must match the specified language. Do not submit content that contains both languages. You can specify any combination of languages for `content_language` and `Accept-Language`.
        :param str accept_language: The desired language of the response. For two-character arguments, regional variants are treated as their parent language; for example, `en-US` is interpreted as `en`. You can specify any combination of languages for `Content-Language` and `accept_language`.
        :return: A `ToneAnalysis` object
        :rtype: watson_developer_cloud.tone_analyzer_v3.ToneAnalysis
        """
        headers = {
            'content-type': content_type,
            'Content-Language': content_language,
            'Accept-Language': accept_language
        }
        params = {'version': self.version, 'sentences': sentences}
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

    def tone_chat(self, utterances, accept_language=None):
        """
        Analyze customer engagement tone.

        Use the customer engagement endpoint to analyze the tone of customer service and customer support conversations. For each utterance of a conversation, the method reports the most prevalent subset of the following seven tones: sad, frustrated, satisfied, excited, polite, impolite, and sympathetic.   If you submit more than 50 utterances, the service returns a warning for the overall content and analyzes only the first 50 utterances. If you submit a single utterance that contains more than 500 characters, the service returns an error for that utterance and does not analyze the utterance. The request fails if all utterances have more than 500 characters.   Per the JSON specification, the default character encoding for JSON content is effectively always UTF-8.

        :param list[Utterance] utterances: An array of `Utterance` objects that provides the input content that the service is to analyze.
        :param str accept_language: The desired language of the response. For two-character arguments, regional variants are treated as their parent language; for example, `en-US` is interpreted as `en`.
        :return: A `UtteranceAnalyses` object
        :rtype: watson_developer_cloud.tone_analyzer_v3.UtteranceAnalyses
        """
        utterances = list(
            map(lambda x: x._to_dict() if hasattr(x, "_to_dict") else x,
                utterances))
        headers = {'Accept-Language': accept_language}
        params = {'version': self.version}
        data = {'utterances': utterances}
        response = self.request(
            method='POST',
            url='/v3/tone_chat',
            headers=headers,
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

    :attr list[ToneScore] tones: An array of `ToneScore` objects that provides the results of the analysis for each qualifying tone of the document. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
    :attr str warning: (optional) A warning message if the overall content exceeds 128 KB or contains more than 1000 sentences. The service analyzes only the first 1000 sentences for document-level analysis and the first 100 sentences for sentence-level analysis.
    """

    def __init__(self, tones, warning=None):
        """
        Initialize a DocumentAnalysis object.

        :param list[ToneScore] tones: An array of `ToneScore` objects that provides the results of the analysis for each qualifying tone of the document. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
        :param str warning: (optional) A warning message if the overall content exceeds 128 KB or contains more than 1000 sentences. The service analyzes only the first 1000 sentences for document-level analysis and the first 100 sentences for sentence-level analysis.
        """
        self.tones = tones
        self.warning = warning

    @classmethod
    def _from_dict(cls, json):
        """Initialize a DocumentAnalysis object from a json dictionary."""
        args = {}
        if 'tones' in json:
            args['tones'] = list(
                map(lambda x: ToneScore._from_dict(x), json['tones']))
        if 'warning' in json:
            args['warning'] = json['warning']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'tones') and self.tones is not None:
            json['tones'] = list(map(lambda x: x._to_dict(), self.tones))
        if hasattr(self, 'warning') and self.warning is not None:
            json['warning'] = self.warning
        return json

    def __str__(self):
        """Return a `str` version of this DocumentAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)


class SentenceAnalysis(object):
    """
    SentenceAnalysis.

    :attr int sentence_id: The unique identifier of a sentence of the input content. The first sentence has ID 0, and the ID of each subsequent sentence is incremented by one.
    :attr str text: The text of the input sentence.
    :attr list[ToneScore] tones: An array of `ToneScore` objects that provides the results of the analysis for each qualifying tone of the sentence. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
    """

    def __init__(self, sentence_id, text, tones):
        """
        Initialize a SentenceAnalysis object.

        :param int sentence_id: The unique identifier of a sentence of the input content. The first sentence has ID 0, and the ID of each subsequent sentence is incremented by one.
        :param str text: The text of the input sentence.
        :param list[ToneScore] tones: An array of `ToneScore` objects that provides the results of the analysis for each qualifying tone of the sentence. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
        """
        self.sentence_id = sentence_id
        self.text = text
        self.tones = tones

    @classmethod
    def _from_dict(cls, json):
        """Initialize a SentenceAnalysis object from a json dictionary."""
        args = {}
        if 'sentence_id' in json:
            args['sentence_id'] = json['sentence_id']
        if 'text' in json:
            args['text'] = json['text']
        if 'tones' in json:
            args['tones'] = list(
                map(lambda x: ToneScore._from_dict(x), json['tones']))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'sentence_id') and self.sentence_id is not None:
            json['sentence_id'] = self.sentence_id
        if hasattr(self, 'text') and self.text is not None:
            json['text'] = self.text
        if hasattr(self, 'tones') and self.tones is not None:
            json['tones'] = list(map(lambda x: x._to_dict(), self.tones))
        return json

    def __str__(self):
        """Return a `str` version of this SentenceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)


class ToneAnalysis(object):
    """
    ToneAnalysis.

    :attr DocumentAnalysis document_tone: An object of type `DocumentAnalysis` that provides the results of the analysis for the full input document.
    :attr list[SentenceAnalysis] sentences_tone: (optional) An array of `SentenceAnalysis` objects that provides the results of the analysis for the individual sentences of the input content. The service returns results only for the first 100 sentences of the input. The field is omitted if the sentences parameter of the request is set to `false`.
    """

    def __init__(self, document_tone, sentences_tone=None):
        """
        Initialize a ToneAnalysis object.

        :param DocumentAnalysis document_tone: An object of type `DocumentAnalysis` that provides the results of the analysis for the full input document.
        :param list[SentenceAnalysis] sentences_tone: (optional) An array of `SentenceAnalysis` objects that provides the results of the analysis for the individual sentences of the input content. The service returns results only for the first 100 sentences of the input. The field is omitted if the sentences parameter of the request is set to `false`.
        """
        self.document_tone = document_tone
        self.sentences_tone = sentences_tone

    @classmethod
    def _from_dict(cls, json):
        """Initialize a ToneAnalysis object from a json dictionary."""
        args = {}
        if 'document_tone' in json:
            args['document_tone'] = DocumentAnalysis._from_dict(
                json['document_tone'])
        if 'sentences_tone' in json:
            args['sentences_tone'] = list(
                map(lambda x: SentenceAnalysis._from_dict(x), json[
                    'sentences_tone']))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'document_tone') and self.document_tone is not None:
            json['document_tone'] = self.document_tone._to_dict()
        if hasattr(self, 'sentences_tone') and self.sentences_tone is not None:
            json['sentences_tone'] = list(
                map(lambda x: x._to_dict(), self.sentences_tone))
        return json

    def __str__(self):
        """Return a `str` version of this ToneAnalysis object."""
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
    def _from_dict(cls, json):
        """Initialize a ToneChatInput object from a json dictionary."""
        args = {}
        if 'utterances' in json:
            args['utterances'] = list(
                map(lambda x: Utterance._from_dict(x), json['utterances']))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'utterances') and self.utterances is not None:
            json['utterances'] = list(
                map(lambda x: x._to_dict(), self.utterances))
        return json

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
    def _from_dict(cls, json):
        """Initialize a ToneChatScore object from a json dictionary."""
        args = {}
        if 'score' in json:
            args['score'] = json['score']
        if 'tone_id' in json:
            args['tone_id'] = json['tone_id']
        if 'tone_name' in json:
            args['tone_name'] = json['tone_name']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'score') and self.score is not None:
            json['score'] = self.score
        if hasattr(self, 'tone_id') and self.tone_id is not None:
            json['tone_id'] = self.tone_id
        if hasattr(self, 'tone_name') and self.tone_name is not None:
            json['tone_name'] = self.tone_name
        return json

    def __str__(self):
        """Return a `str` version of this ToneChatScore object."""
        return json.dumps(self._to_dict(), indent=2)


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
    def _from_dict(cls, json):
        """Initialize a ToneInput object from a json dictionary."""
        args = {}
        if 'text' in json:
            args['text'] = json['text']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'text') and self.text is not None:
            json['text'] = self.text
        return json

    def __str__(self):
        """Return a `str` version of this ToneInput object."""
        return json.dumps(self._to_dict(), indent=2)


class ToneScore(object):
    """
    ToneScore.

    :attr float score: The score for the tone in the range of 0.5 to 1. A score greater than 0.75 indicates a high likelihood that the tone is perceived in the content.
    :attr str tone_id: The unique, non-localized identifier of the tone. The service can return results for the following tone IDs: `anger`, `fear`, `joy`, and `sadness` (emotional tones); `analytical`, `confident`, and `tentative` (language tones). The service returns results only for tones whose scores meet a minimum threshold of 0.5.
    :attr str tone_name: The user-visible, localized name of the tone.
    """

    def __init__(self, score, tone_id, tone_name):
        """
        Initialize a ToneScore object.

        :param float score: The score for the tone in the range of 0.5 to 1. A score greater than 0.75 indicates a high likelihood that the tone is perceived in the content.
        :param str tone_id: The unique, non-localized identifier of the tone. The service can return results for the following tone IDs: `anger`, `fear`, `joy`, and `sadness` (emotional tones); `analytical`, `confident`, and `tentative` (language tones). The service returns results only for tones whose scores meet a minimum threshold of 0.5.
        :param str tone_name: The user-visible, localized name of the tone.
        """
        self.score = score
        self.tone_id = tone_id
        self.tone_name = tone_name

    @classmethod
    def _from_dict(cls, json):
        """Initialize a ToneScore object from a json dictionary."""
        args = {}
        if 'score' in json:
            args['score'] = json['score']
        if 'tone_id' in json:
            args['tone_id'] = json['tone_id']
        if 'tone_name' in json:
            args['tone_name'] = json['tone_name']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'score') and self.score is not None:
            json['score'] = self.score
        if hasattr(self, 'tone_id') and self.tone_id is not None:
            json['tone_id'] = self.tone_id
        if hasattr(self, 'tone_name') and self.tone_name is not None:
            json['tone_name'] = self.tone_name
        return json

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
    def _from_dict(cls, json):
        """Initialize a Utterance object from a json dictionary."""
        args = {}
        if 'text' in json:
            args['text'] = json['text']
        if 'user' in json:
            args['user'] = json['user']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'text') and self.text is not None:
            json['text'] = self.text
        if hasattr(self, 'user') and self.user is not None:
            json['user'] = self.user
        return json

    def __str__(self):
        """Return a `str` version of this Utterance object."""
        return json.dumps(self._to_dict(), indent=2)


class UtteranceAnalyses(object):
    """
    UtteranceAnalyses.

    :attr list[UtteranceAnalysis] utterances_tone: An array of `UtteranceAnalysis` objects that provides the results for each utterance of the input.
    :attr str warning: (optional) A warning message if the content contains more than 50 utterances. The service analyzes only the first 50 utterances.
    """

    def __init__(self, utterances_tone, warning=None):
        """
        Initialize a UtteranceAnalyses object.

        :param list[UtteranceAnalysis] utterances_tone: An array of `UtteranceAnalysis` objects that provides the results for each utterance of the input.
        :param str warning: (optional) A warning message if the content contains more than 50 utterances. The service analyzes only the first 50 utterances.
        """
        self.utterances_tone = utterances_tone
        self.warning = warning

    @classmethod
    def _from_dict(cls, json):
        """Initialize a UtteranceAnalyses object from a json dictionary."""
        args = {}
        if 'utterances_tone' in json:
            args['utterances_tone'] = list(
                map(lambda x: UtteranceAnalysis._from_dict(x), json[
                    'utterances_tone']))
        if 'warning' in json:
            args['warning'] = json['warning']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self,
                   'utterances_tone') and self.utterances_tone is not None:
            json['utterances_tone'] = list(
                map(lambda x: x._to_dict(), self.utterances_tone))
        if hasattr(self, 'warning') and self.warning is not None:
            json['warning'] = self.warning
        return json

    def __str__(self):
        """Return a `str` version of this UtteranceAnalyses object."""
        return json.dumps(self._to_dict(), indent=2)


class UtteranceAnalysis(object):
    """
    UtteranceAnalysis.

    :attr str utterance_id: The unique identifier of the utterance. The first utterance has ID 0, and the ID of each subsequent utterance is incremented by one.
    :attr str utterance_text: The text of the utterance.
    :attr list[ToneChatScore] tones: An array of `ToneChatScore` objects that provides results for the most prevalent tones of the utterance. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
    :attr str error: (optional) An error message if the utterance contains more than 500 characters. The service does not analyze the utterance.
    """

    def __init__(self, utterance_id, utterance_text, tones, error=None):
        """
        Initialize a UtteranceAnalysis object.

        :param str utterance_id: The unique identifier of the utterance. The first utterance has ID 0, and the ID of each subsequent utterance is incremented by one.
        :param str utterance_text: The text of the utterance.
        :param list[ToneChatScore] tones: An array of `ToneChatScore` objects that provides results for the most prevalent tones of the utterance. The array includes results for any tone whose score is at least 0.5. The array is empty if no tone has a score that meets this threshold.
        :param str error: (optional) An error message if the utterance contains more than 500 characters. The service does not analyze the utterance.
        """
        self.utterance_id = utterance_id
        self.utterance_text = utterance_text
        self.tones = tones
        self.error = error

    @classmethod
    def _from_dict(cls, json):
        """Initialize a UtteranceAnalysis object from a json dictionary."""
        args = {}
        if 'utterance_id' in json:
            args['utterance_id'] = json['utterance_id']
        if 'utterance_text' in json:
            args['utterance_text'] = json['utterance_text']
        if 'tones' in json:
            args['tones'] = list(
                map(lambda x: ToneChatScore._from_dict(x), json['tones']))
        if 'error' in json:
            args['error'] = json['error']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        json = {}
        if hasattr(self, 'utterance_id') and self.utterance_id is not None:
            json['utterance_id'] = self.utterance_id
        if hasattr(self, 'utterance_text') and self.utterance_text is not None:
            json['utterance_text'] = self.utterance_text
        if hasattr(self, 'tones') and self.tones is not None:
            json['tones'] = list(map(lambda x: x._to_dict(), self.tones))
        if hasattr(self, 'error') and self.error is not None:
            json['error'] = self.error
        return json

    def __str__(self):
        """Return a `str` version of this UtteranceAnalysis object."""
        return json.dumps(self._to_dict(), indent=2)
