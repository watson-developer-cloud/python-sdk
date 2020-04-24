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
The IBM Watson&trade; Personality Insights service enables applications to derive insights
from social media, enterprise data, or other digital communications. The service uses
linguistic analytics to infer individuals' intrinsic personality characteristics,
including Big Five, Needs, and Values, from digital communications such as email, text
messages, tweets, and forum posts.
The service can automatically infer, from potentially noisy social media, portraits of
individuals that reflect their personality characteristics. The service can infer
consumption preferences based on the results of its analysis and, for JSON content that is
timestamped, can report temporal behavior.
* For information about the meaning of the models that the service uses to describe
personality characteristics, see [Personality
models](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-models#models).
* For information about the meaning of the consumption preferences, see [Consumption
preferences](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-preferences#preferences).
**Note:** Request logging is disabled for the Personality Insights service. Regardless of
whether you set the `X-Watson-Learning-Opt-Out` request header, the service does not log
or retain data from requests and responses.
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


class PersonalityInsightsV3(BaseService):
    """The Personality Insights V3 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/personality-insights/api'
    DEFAULT_SERVICE_NAME = 'personality_insights'

    def __init__(
            self,
            version: str,
            authenticator: Authenticator = None,
            service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Personality Insights service.

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

    def profile(self,
                content: object,
                accept: str,
                *,
                content_type: str = None,
                content_language: str = None,
                accept_language: str = None,
                raw_scores: bool = None,
                csv_headers: bool = None,
                consumption_preferences: bool = None,
                **kwargs) -> 'DetailedResponse':
        """
        Get profile.

        Generates a personality profile for the author of the input text. The service
        accepts a maximum of 20 MB of input content, but it requires much less text to
        produce an accurate profile. The service can analyze text in Arabic, English,
        Japanese, Korean, or Spanish. It can return its results in a variety of languages.
        **See also:**
        * [Requesting a
        profile](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-input#input)
        * [Providing sufficient
        input](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-input#sufficient)
        ### Content types
         You can provide input content as plain text (`text/plain`), HTML (`text/html`),
        or JSON (`application/json`) by specifying the **Content-Type** parameter. The
        default is `text/plain`.
        * Per the JSON specification, the default character encoding for JSON content is
        effectively always UTF-8.
        * Per the HTTP specification, the default encoding for plain text and HTML is
        ISO-8859-1 (effectively, the ASCII character set).
        When specifying a content type of plain text or HTML, include the `charset`
        parameter to indicate the character encoding of the input text; for example,
        `Content-Type: text/plain;charset=utf-8`.
        **See also:** [Specifying request and response
        formats](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-input#formats)
        ### Accept types
         You must request a response as JSON (`application/json`) or comma-separated
        values (`text/csv`) by specifying the **Accept** parameter. CSV output includes a
        fixed number of columns. Set the **csv_headers** parameter to `true` to request
        optional column headers for CSV output.
        **See also:**
        * [Understanding a JSON
        profile](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-output#output)
        * [Understanding a CSV
        profile](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-outputCSV#outputCSV).

        :param Content content: A maximum of 20 MB of content to analyze, though
               the service requires much less text; for more information, see [Providing
               sufficient
               input](https://cloud.ibm.com/docs/personality-insights?topic=personality-insights-input#sufficient).
               For JSON input, provide an object of type `Content`.
        :param str accept: The type of the response. For more information, see
               **Accept types** in the method description.
        :param str content_type: (optional) The type of the input. For more
               information, see **Content types** in the method description.
        :param str content_language: (optional) The language of the input text for
               the request: Arabic, English, Japanese, Korean, or Spanish. Regional
               variants are treated as their parent language; for example, `en-US` is
               interpreted as `en`.
               The effect of the **Content-Language** parameter depends on the
               **Content-Type** parameter. When **Content-Type** is `text/plain` or
               `text/html`, **Content-Language** is the only way to specify the language.
               When **Content-Type** is `application/json`, **Content-Language** overrides
               a language specified with the `language` parameter of a `ContentItem`
               object, and content items that specify a different language are ignored;
               omit this parameter to base the language on the specification of the
               content items. You can specify any combination of languages for
               **Content-Language** and **Accept-Language**.
        :param str accept_language: (optional) The desired language of the
               response. For two-character arguments, regional variants are treated as
               their parent language; for example, `en-US` is interpreted as `en`. You can
               specify any combination of languages for the input and response content.
        :param bool raw_scores: (optional) Indicates whether a raw score in
               addition to a normalized percentile is returned for each characteristic;
               raw scores are not compared with a sample population. By default, only
               normalized percentiles are returned.
        :param bool csv_headers: (optional) Indicates whether column labels are
               returned with a CSV response. By default, no column labels are returned.
               Applies only when the response type is CSV (`text/csv`).
        :param bool consumption_preferences: (optional) Indicates whether
               consumption preferences are returned with the results. By default, no
               consumption preferences are returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if content is None:
            raise ValueError('content must be provided')
        if accept is None:
            raise ValueError('accept must be provided')
        if isinstance(content, Content):
            content = self._convert_model(content)

        headers = {
            'Accept': accept,
            'Content-Type': content_type,
            'Content-Language': content_language,
            'Accept-Language': accept_language
        }
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='profile')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'raw_scores': raw_scores,
            'csv_headers': csv_headers,
            'consumption_preferences': consumption_preferences
        }

        if content_type == 'application/json' and isinstance(content, dict):
            data = json.dumps(content)
        else:
            data = content

        url = '/v3/profile'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response


class ProfileEnums(object):

    class Accept(Enum):
        """
        The type of the response. For more information, see **Accept types** in the method
        description.
        """
        APPLICATION_JSON = 'application/json'
        TEXT_CSV = 'text/csv'

    class ContentType(Enum):
        """
        The type of the input. For more information, see **Content types** in the method
        description.
        """
        APPLICATION_JSON = 'application/json'
        TEXT_HTML = 'text/html'
        TEXT_PLAIN = 'text/plain'

    class ContentLanguage(Enum):
        """
        The language of the input text for the request: Arabic, English, Japanese, Korean,
        or Spanish. Regional variants are treated as their parent language; for example,
        `en-US` is interpreted as `en`.
        The effect of the **Content-Language** parameter depends on the **Content-Type**
        parameter. When **Content-Type** is `text/plain` or `text/html`,
        **Content-Language** is the only way to specify the language. When
        **Content-Type** is `application/json`, **Content-Language** overrides a language
        specified with the `language` parameter of a `ContentItem` object, and content
        items that specify a different language are ignored; omit this parameter to base
        the language on the specification of the content items. You can specify any
        combination of languages for **Content-Language** and **Accept-Language**.
        """
        AR = 'ar'
        EN = 'en'
        ES = 'es'
        JA = 'ja'
        KO = 'ko'

    class AcceptLanguage(Enum):
        """
        The desired language of the response. For two-character arguments, regional
        variants are treated as their parent language; for example, `en-US` is interpreted
        as `en`. You can specify any combination of languages for the input and response
        content.
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


class Behavior():
    """
    The temporal behavior for the input content.

    :attr str trait_id: The unique, non-localized identifier of the characteristic
          to which the results pertain. IDs have the form `behavior_{value}`.
    :attr str name: The user-visible, localized name of the characteristic.
    :attr str category: The category of the characteristic: `behavior` for temporal
          data.
    :attr float percentage: For JSON content that is timestamped, the percentage of
          timestamped input data that occurred during that day of the week or hour of the
          day. The range is 0 to 1.
    """

    def __init__(self, trait_id: str, name: str, category: str,
                 percentage: float) -> None:
        """
        Initialize a Behavior object.

        :param str trait_id: The unique, non-localized identifier of the
               characteristic to which the results pertain. IDs have the form
               `behavior_{value}`.
        :param str name: The user-visible, localized name of the characteristic.
        :param str category: The category of the characteristic: `behavior` for
               temporal data.
        :param float percentage: For JSON content that is timestamped, the
               percentage of timestamped input data that occurred during that day of the
               week or hour of the day. The range is 0 to 1.
        """
        self.trait_id = trait_id
        self.name = name
        self.category = category
        self.percentage = percentage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Behavior':
        """Initialize a Behavior object from a json dictionary."""
        args = {}
        valid_keys = ['trait_id', 'name', 'category', 'percentage']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Behavior: '
                + ', '.join(bad_keys))
        if 'trait_id' in _dict:
            args['trait_id'] = _dict.get('trait_id')
        else:
            raise ValueError(
                'Required property \'trait_id\' not present in Behavior JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Behavior JSON')
        if 'category' in _dict:
            args['category'] = _dict.get('category')
        else:
            raise ValueError(
                'Required property \'category\' not present in Behavior JSON')
        if 'percentage' in _dict:
            args['percentage'] = _dict.get('percentage')
        else:
            raise ValueError(
                'Required property \'percentage\' not present in Behavior JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Behavior object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'trait_id') and self.trait_id is not None:
            _dict['trait_id'] = self.trait_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'category') and self.category is not None:
            _dict['category'] = self.category
        if hasattr(self, 'percentage') and self.percentage is not None:
            _dict['percentage'] = self.percentage
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Behavior object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Behavior') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Behavior') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConsumptionPreferences():
    """
    A consumption preference that the service inferred from the input content.

    :attr str consumption_preference_id: The unique, non-localized identifier of the
          consumption preference to which the results pertain. IDs have the form
          `consumption_preferences_{preference}`.
    :attr str name: The user-visible, localized name of the consumption preference.
    :attr float score: The score for the consumption preference:
          * `0.0`: Unlikely
          * `0.5`: Neutral
          * `1.0`: Likely
          The scores for some preferences are binary and do not allow a neutral value. The
          score is an indication of preference based on the results inferred from the
          input text, not a normalized percentile.
    """

    def __init__(self, consumption_preference_id: str, name: str,
                 score: float) -> None:
        """
        Initialize a ConsumptionPreferences object.

        :param str consumption_preference_id: The unique, non-localized identifier
               of the consumption preference to which the results pertain. IDs have the
               form `consumption_preferences_{preference}`.
        :param str name: The user-visible, localized name of the consumption
               preference.
        :param float score: The score for the consumption preference:
               * `0.0`: Unlikely
               * `0.5`: Neutral
               * `1.0`: Likely
               The scores for some preferences are binary and do not allow a neutral
               value. The score is an indication of preference based on the results
               inferred from the input text, not a normalized percentile.
        """
        self.consumption_preference_id = consumption_preference_id
        self.name = name
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConsumptionPreferences':
        """Initialize a ConsumptionPreferences object from a json dictionary."""
        args = {}
        valid_keys = ['consumption_preference_id', 'name', 'score']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ConsumptionPreferences: '
                + ', '.join(bad_keys))
        if 'consumption_preference_id' in _dict:
            args['consumption_preference_id'] = _dict.get(
                'consumption_preference_id')
        else:
            raise ValueError(
                'Required property \'consumption_preference_id\' not present in ConsumptionPreferences JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in ConsumptionPreferences JSON'
            )
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        else:
            raise ValueError(
                'Required property \'score\' not present in ConsumptionPreferences JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConsumptionPreferences object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'consumption_preference_id'
                  ) and self.consumption_preference_id is not None:
            _dict['consumption_preference_id'] = self.consumption_preference_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConsumptionPreferences object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ConsumptionPreferences') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConsumptionPreferences') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConsumptionPreferencesCategory():
    """
    The consumption preferences that the service inferred from the input content.

    :attr str consumption_preference_category_id: The unique, non-localized
          identifier of the consumption preferences category to which the results pertain.
          IDs have the form `consumption_preferences_{category}`.
    :attr str name: The user-visible name of the consumption preferences category.
    :attr List[ConsumptionPreferences] consumption_preferences: Detailed results
          inferred from the input text for the individual preferences of the category.
    """

    def __init__(
            self, consumption_preference_category_id: str, name: str,
            consumption_preferences: List['ConsumptionPreferences']) -> None:
        """
        Initialize a ConsumptionPreferencesCategory object.

        :param str consumption_preference_category_id: The unique, non-localized
               identifier of the consumption preferences category to which the results
               pertain. IDs have the form `consumption_preferences_{category}`.
        :param str name: The user-visible name of the consumption preferences
               category.
        :param List[ConsumptionPreferences] consumption_preferences: Detailed
               results inferred from the input text for the individual preferences of the
               category.
        """
        self.consumption_preference_category_id = consumption_preference_category_id
        self.name = name
        self.consumption_preferences = consumption_preferences

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConsumptionPreferencesCategory':
        """Initialize a ConsumptionPreferencesCategory object from a json dictionary."""
        args = {}
        valid_keys = [
            'consumption_preference_category_id', 'name',
            'consumption_preferences'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ConsumptionPreferencesCategory: '
                + ', '.join(bad_keys))
        if 'consumption_preference_category_id' in _dict:
            args['consumption_preference_category_id'] = _dict.get(
                'consumption_preference_category_id')
        else:
            raise ValueError(
                'Required property \'consumption_preference_category_id\' not present in ConsumptionPreferencesCategory JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in ConsumptionPreferencesCategory JSON'
            )
        if 'consumption_preferences' in _dict:
            args['consumption_preferences'] = [
                ConsumptionPreferences._from_dict(x)
                for x in (_dict.get('consumption_preferences'))
            ]
        else:
            raise ValueError(
                'Required property \'consumption_preferences\' not present in ConsumptionPreferencesCategory JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConsumptionPreferencesCategory object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'consumption_preference_category_id'
                  ) and self.consumption_preference_category_id is not None:
            _dict[
                'consumption_preference_category_id'] = self.consumption_preference_category_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'consumption_preferences'
                  ) and self.consumption_preferences is not None:
            _dict['consumption_preferences'] = [
                x._to_dict() for x in self.consumption_preferences
            ]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConsumptionPreferencesCategory object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ConsumptionPreferencesCategory') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConsumptionPreferencesCategory') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Content():
    """
    The full input content that the service is to analyze.

    :attr List[ContentItem] content_items: An array of `ContentItem` objects that
          provides the text that is to be analyzed.
    """

    def __init__(self, content_items: List['ContentItem']) -> None:
        """
        Initialize a Content object.

        :param List[ContentItem] content_items: An array of `ContentItem` objects
               that provides the text that is to be analyzed.
        """
        self.content_items = content_items

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Content':
        """Initialize a Content object from a json dictionary."""
        args = {}
        valid_keys = ['content_items', 'contentItems']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Content: ' +
                ', '.join(bad_keys))
        if 'contentItems' in _dict:
            args['content_items'] = [
                ContentItem._from_dict(x) for x in (_dict.get('contentItems'))
            ]
        else:
            raise ValueError(
                'Required property \'contentItems\' not present in Content JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Content object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content_items') and self.content_items is not None:
            _dict['contentItems'] = [x._to_dict() for x in self.content_items]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Content object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Content') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Content') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ContentItem():
    """
    An input content item that the service is to analyze.

    :attr str content: The content that is to be analyzed. The service supports up
          to 20 MB of content for all `ContentItem` objects combined.
    :attr str id: (optional) A unique identifier for this content item.
    :attr int created: (optional) A timestamp that identifies when this content was
          created. Specify a value in milliseconds since the UNIX Epoch (January 1, 1970,
          at 0:00 UTC). Required only for results that include temporal behavior data.
    :attr int updated: (optional) A timestamp that identifies when this content was
          last updated. Specify a value in milliseconds since the UNIX Epoch (January 1,
          1970, at 0:00 UTC). Required only for results that include temporal behavior
          data.
    :attr str contenttype: (optional) The MIME type of the content. The default is
          plain text. The tags are stripped from HTML content before it is analyzed; plain
          text is processed as submitted.
    :attr str language: (optional) The language identifier (two-letter ISO 639-1
          identifier) for the language of the content item. The default is `en` (English).
          Regional variants are treated as their parent language; for example, `en-US` is
          interpreted as `en`. A language specified with the **Content-Type** parameter
          overrides the value of this parameter; any content items that specify a
          different language are ignored. Omit the **Content-Type** parameter to base the
          language on the most prevalent specification among the content items; again,
          content items that specify a different language are ignored. You can specify any
          combination of languages for the input and response content.
    :attr str parentid: (optional) The unique ID of the parent content item for this
          item. Used to identify hierarchical relationships between posts/replies,
          messages/replies, and so on.
    :attr bool reply: (optional) Indicates whether this content item is a reply to
          another content item.
    :attr bool forward: (optional) Indicates whether this content item is a
          forwarded/copied version of another content item.
    """

    def __init__(self,
                 content: str,
                 *,
                 id: str = None,
                 created: int = None,
                 updated: int = None,
                 contenttype: str = None,
                 language: str = None,
                 parentid: str = None,
                 reply: bool = None,
                 forward: bool = None) -> None:
        """
        Initialize a ContentItem object.

        :param str content: The content that is to be analyzed. The service
               supports up to 20 MB of content for all `ContentItem` objects combined.
        :param str id: (optional) A unique identifier for this content item.
        :param int created: (optional) A timestamp that identifies when this
               content was created. Specify a value in milliseconds since the UNIX Epoch
               (January 1, 1970, at 0:00 UTC). Required only for results that include
               temporal behavior data.
        :param int updated: (optional) A timestamp that identifies when this
               content was last updated. Specify a value in milliseconds since the UNIX
               Epoch (January 1, 1970, at 0:00 UTC). Required only for results that
               include temporal behavior data.
        :param str contenttype: (optional) The MIME type of the content. The
               default is plain text. The tags are stripped from HTML content before it is
               analyzed; plain text is processed as submitted.
        :param str language: (optional) The language identifier (two-letter ISO
               639-1 identifier) for the language of the content item. The default is `en`
               (English). Regional variants are treated as their parent language; for
               example, `en-US` is interpreted as `en`. A language specified with the
               **Content-Type** parameter overrides the value of this parameter; any
               content items that specify a different language are ignored. Omit the
               **Content-Type** parameter to base the language on the most prevalent
               specification among the content items; again, content items that specify a
               different language are ignored. You can specify any combination of
               languages for the input and response content.
        :param str parentid: (optional) The unique ID of the parent content item
               for this item. Used to identify hierarchical relationships between
               posts/replies, messages/replies, and so on.
        :param bool reply: (optional) Indicates whether this content item is a
               reply to another content item.
        :param bool forward: (optional) Indicates whether this content item is a
               forwarded/copied version of another content item.
        """
        self.content = content
        self.id = id
        self.created = created
        self.updated = updated
        self.contenttype = contenttype
        self.language = language
        self.parentid = parentid
        self.reply = reply
        self.forward = forward

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ContentItem':
        """Initialize a ContentItem object from a json dictionary."""
        args = {}
        valid_keys = [
            'content', 'id', 'created', 'updated', 'contenttype', 'language',
            'parentid', 'reply', 'forward'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ContentItem: '
                + ', '.join(bad_keys))
        if 'content' in _dict:
            args['content'] = _dict.get('content')
        else:
            raise ValueError(
                'Required property \'content\' not present in ContentItem JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created' in _dict:
            args['created'] = _dict.get('created')
        if 'updated' in _dict:
            args['updated'] = _dict.get('updated')
        if 'contenttype' in _dict:
            args['contenttype'] = _dict.get('contenttype')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'parentid' in _dict:
            args['parentid'] = _dict.get('parentid')
        if 'reply' in _dict:
            args['reply'] = _dict.get('reply')
        if 'forward' in _dict:
            args['forward'] = _dict.get('forward')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ContentItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = self.created
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = self.updated
        if hasattr(self, 'contenttype') and self.contenttype is not None:
            _dict['contenttype'] = self.contenttype
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'parentid') and self.parentid is not None:
            _dict['parentid'] = self.parentid
        if hasattr(self, 'reply') and self.reply is not None:
            _dict['reply'] = self.reply
        if hasattr(self, 'forward') and self.forward is not None:
            _dict['forward'] = self.forward
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ContentItem object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ContentItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ContentItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ContenttypeEnum(Enum):
        """
        The MIME type of the content. The default is plain text. The tags are stripped
        from HTML content before it is analyzed; plain text is processed as submitted.
        """
        TEXT_PLAIN = "text/plain"
        TEXT_HTML = "text/html"

    class LanguageEnum(Enum):
        """
        The language identifier (two-letter ISO 639-1 identifier) for the language of the
        content item. The default is `en` (English). Regional variants are treated as
        their parent language; for example, `en-US` is interpreted as `en`. A language
        specified with the **Content-Type** parameter overrides the value of this
        parameter; any content items that specify a different language are ignored. Omit
        the **Content-Type** parameter to base the language on the most prevalent
        specification among the content items; again, content items that specify a
        different language are ignored. You can specify any combination of languages for
        the input and response content.
        """
        AR = "ar"
        EN = "en"
        ES = "es"
        JA = "ja"
        KO = "ko"


class Profile():
    """
    The personality profile that the service generated for the input content.

    :attr str processed_language: The language model that was used to process the
          input.
    :attr int word_count: The number of words from the input that were used to
          produce the profile.
    :attr str word_count_message: (optional) When guidance is appropriate, a string
          that provides a message that indicates the number of words found and where that
          value falls in the range of required or suggested number of words.
    :attr List[Trait] personality: A recursive array of `Trait` objects that
          provides detailed results for the Big Five personality characteristics
          (dimensions and facets) inferred from the input text.
    :attr List[Trait] needs: Detailed results for the Needs characteristics inferred
          from the input text.
    :attr List[Trait] values: Detailed results for the Values characteristics
          inferred from the input text.
    :attr List[Behavior] behavior: (optional) For JSON content that is timestamped,
          detailed results about the social behavior disclosed by the input in terms of
          temporal characteristics. The results include information about the distribution
          of the content over the days of the week and the hours of the day.
    :attr List[ConsumptionPreferencesCategory] consumption_preferences: (optional)
          If the **consumption_preferences** parameter is `true`, detailed results for
          each category of consumption preferences. Each element of the array provides
          information inferred from the input text for the individual preferences of that
          category.
    :attr List[Warning] warnings: An array of warning messages that are associated
          with the input text for the request. The array is empty if the input generated
          no warnings.
    """

    def __init__(
        self,
        processed_language: str,
        word_count: int,
        personality: List['Trait'],
        needs: List['Trait'],
        values: List['Trait'],
        warnings: List['Warning'],
        *,
        word_count_message: str = None,
        behavior: List['Behavior'] = None,
        consumption_preferences: List['ConsumptionPreferencesCategory'] = None
    ) -> None:
        """
        Initialize a Profile object.

        :param str processed_language: The language model that was used to process
               the input.
        :param int word_count: The number of words from the input that were used to
               produce the profile.
        :param List[Trait] personality: A recursive array of `Trait` objects that
               provides detailed results for the Big Five personality characteristics
               (dimensions and facets) inferred from the input text.
        :param List[Trait] needs: Detailed results for the Needs characteristics
               inferred from the input text.
        :param List[Trait] values: Detailed results for the Values characteristics
               inferred from the input text.
        :param List[Warning] warnings: An array of warning messages that are
               associated with the input text for the request. The array is empty if the
               input generated no warnings.
        :param str word_count_message: (optional) When guidance is appropriate, a
               string that provides a message that indicates the number of words found and
               where that value falls in the range of required or suggested number of
               words.
        :param List[Behavior] behavior: (optional) For JSON content that is
               timestamped, detailed results about the social behavior disclosed by the
               input in terms of temporal characteristics. The results include information
               about the distribution of the content over the days of the week and the
               hours of the day.
        :param List[ConsumptionPreferencesCategory] consumption_preferences:
               (optional) If the **consumption_preferences** parameter is `true`, detailed
               results for each category of consumption preferences. Each element of the
               array provides information inferred from the input text for the individual
               preferences of that category.
        """
        self.processed_language = processed_language
        self.word_count = word_count
        self.word_count_message = word_count_message
        self.personality = personality
        self.needs = needs
        self.values = values
        self.behavior = behavior
        self.consumption_preferences = consumption_preferences
        self.warnings = warnings

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Profile':
        """Initialize a Profile object from a json dictionary."""
        args = {}
        valid_keys = [
            'processed_language', 'word_count', 'word_count_message',
            'personality', 'needs', 'values', 'behavior',
            'consumption_preferences', 'warnings'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Profile: ' +
                ', '.join(bad_keys))
        if 'processed_language' in _dict:
            args['processed_language'] = _dict.get('processed_language')
        else:
            raise ValueError(
                'Required property \'processed_language\' not present in Profile JSON'
            )
        if 'word_count' in _dict:
            args['word_count'] = _dict.get('word_count')
        else:
            raise ValueError(
                'Required property \'word_count\' not present in Profile JSON')
        if 'word_count_message' in _dict:
            args['word_count_message'] = _dict.get('word_count_message')
        if 'personality' in _dict:
            args['personality'] = [
                Trait._from_dict(x) for x in (_dict.get('personality'))
            ]
        else:
            raise ValueError(
                'Required property \'personality\' not present in Profile JSON')
        if 'needs' in _dict:
            args['needs'] = [Trait._from_dict(x) for x in (_dict.get('needs'))]
        else:
            raise ValueError(
                'Required property \'needs\' not present in Profile JSON')
        if 'values' in _dict:
            args['values'] = [
                Trait._from_dict(x) for x in (_dict.get('values'))
            ]
        else:
            raise ValueError(
                'Required property \'values\' not present in Profile JSON')
        if 'behavior' in _dict:
            args['behavior'] = [
                Behavior._from_dict(x) for x in (_dict.get('behavior'))
            ]
        if 'consumption_preferences' in _dict:
            args['consumption_preferences'] = [
                ConsumptionPreferencesCategory._from_dict(x)
                for x in (_dict.get('consumption_preferences'))
            ]
        if 'warnings' in _dict:
            args['warnings'] = [
                Warning._from_dict(x) for x in (_dict.get('warnings'))
            ]
        else:
            raise ValueError(
                'Required property \'warnings\' not present in Profile JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Profile object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(
                self,
                'processed_language') and self.processed_language is not None:
            _dict['processed_language'] = self.processed_language
        if hasattr(self, 'word_count') and self.word_count is not None:
            _dict['word_count'] = self.word_count
        if hasattr(
                self,
                'word_count_message') and self.word_count_message is not None:
            _dict['word_count_message'] = self.word_count_message
        if hasattr(self, 'personality') and self.personality is not None:
            _dict['personality'] = [x._to_dict() for x in self.personality]
        if hasattr(self, 'needs') and self.needs is not None:
            _dict['needs'] = [x._to_dict() for x in self.needs]
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [x._to_dict() for x in self.values]
        if hasattr(self, 'behavior') and self.behavior is not None:
            _dict['behavior'] = [x._to_dict() for x in self.behavior]
        if hasattr(self, 'consumption_preferences'
                  ) and self.consumption_preferences is not None:
            _dict['consumption_preferences'] = [
                x._to_dict() for x in self.consumption_preferences
            ]
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = [x._to_dict() for x in self.warnings]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Profile object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Profile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Profile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProcessedLanguageEnum(Enum):
        """
        The language model that was used to process the input.
        """
        AR = "ar"
        EN = "en"
        ES = "es"
        JA = "ja"
        KO = "ko"


class Trait():
    """
    The characteristics that the service inferred from the input content.

    :attr str trait_id: The unique, non-localized identifier of the characteristic
          to which the results pertain. IDs have the form
          * `big5_{characteristic}` for Big Five personality dimensions
          * `facet_{characteristic}` for Big Five personality facets
          * `need_{characteristic}` for Needs
           *`value_{characteristic}` for Values.
    :attr str name: The user-visible, localized name of the characteristic.
    :attr str category: The category of the characteristic: `personality` for Big
          Five personality characteristics, `needs` for Needs, and `values` for Values.
    :attr float percentile: The normalized percentile score for the characteristic.
          The range is 0 to 1. For example, if the percentage for Openness is 0.60, the
          author scored in the 60th percentile; the author is more open than 59 percent of
          the population and less open than 39 percent of the population.
    :attr float raw_score: (optional) The raw score for the characteristic. The
          range is 0 to 1. A higher score generally indicates a greater likelihood that
          the author has that characteristic, but raw scores must be considered in
          aggregate: The range of values in practice might be much smaller than 0 to 1, so
          an individual score must be considered in the context of the overall scores and
          their range.
          The raw score is computed based on the input and the service model; it is not
          normalized or compared with a sample population. The raw score enables
          comparison of the results against a different sampling population and with a
          custom normalization approach.
    :attr bool significant: (optional) **`2017-10-13`**: Indicates whether the
          characteristic is meaningful for the input language. The field is always `true`
          for all characteristics of English, Spanish, and Japanese input. The field is
          `false` for the subset of characteristics of Arabic and Korean input for which
          the service's models are unable to generate meaningful results.
          **`2016-10-19`**: Not returned.
    :attr List[Trait] children: (optional) For `personality` (Big Five) dimensions,
          more detailed results for the facets of each dimension as inferred from the
          input text.
    """

    def __init__(self,
                 trait_id: str,
                 name: str,
                 category: str,
                 percentile: float,
                 *,
                 raw_score: float = None,
                 significant: bool = None,
                 children: List['Trait'] = None) -> None:
        """
        Initialize a Trait object.

        :param str trait_id: The unique, non-localized identifier of the
               characteristic to which the results pertain. IDs have the form
               * `big5_{characteristic}` for Big Five personality dimensions
               * `facet_{characteristic}` for Big Five personality facets
               * `need_{characteristic}` for Needs
                *`value_{characteristic}` for Values.
        :param str name: The user-visible, localized name of the characteristic.
        :param str category: The category of the characteristic: `personality` for
               Big Five personality characteristics, `needs` for Needs, and `values` for
               Values.
        :param float percentile: The normalized percentile score for the
               characteristic. The range is 0 to 1. For example, if the percentage for
               Openness is 0.60, the author scored in the 60th percentile; the author is
               more open than 59 percent of the population and less open than 39 percent
               of the population.
        :param float raw_score: (optional) The raw score for the characteristic.
               The range is 0 to 1. A higher score generally indicates a greater
               likelihood that the author has that characteristic, but raw scores must be
               considered in aggregate: The range of values in practice might be much
               smaller than 0 to 1, so an individual score must be considered in the
               context of the overall scores and their range.
               The raw score is computed based on the input and the service model; it is
               not normalized or compared with a sample population. The raw score enables
               comparison of the results against a different sampling population and with
               a custom normalization approach.
        :param bool significant: (optional) **`2017-10-13`**: Indicates whether the
               characteristic is meaningful for the input language. The field is always
               `true` for all characteristics of English, Spanish, and Japanese input. The
               field is `false` for the subset of characteristics of Arabic and Korean
               input for which the service's models are unable to generate meaningful
               results. **`2016-10-19`**: Not returned.
        :param List[Trait] children: (optional) For `personality` (Big Five)
               dimensions, more detailed results for the facets of each dimension as
               inferred from the input text.
        """
        self.trait_id = trait_id
        self.name = name
        self.category = category
        self.percentile = percentile
        self.raw_score = raw_score
        self.significant = significant
        self.children = children

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Trait':
        """Initialize a Trait object from a json dictionary."""
        args = {}
        valid_keys = [
            'trait_id', 'name', 'category', 'percentile', 'raw_score',
            'significant', 'children'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Trait: ' +
                ', '.join(bad_keys))
        if 'trait_id' in _dict:
            args['trait_id'] = _dict.get('trait_id')
        else:
            raise ValueError(
                'Required property \'trait_id\' not present in Trait JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Trait JSON')
        if 'category' in _dict:
            args['category'] = _dict.get('category')
        else:
            raise ValueError(
                'Required property \'category\' not present in Trait JSON')
        if 'percentile' in _dict:
            args['percentile'] = _dict.get('percentile')
        else:
            raise ValueError(
                'Required property \'percentile\' not present in Trait JSON')
        if 'raw_score' in _dict:
            args['raw_score'] = _dict.get('raw_score')
        if 'significant' in _dict:
            args['significant'] = _dict.get('significant')
        if 'children' in _dict:
            args['children'] = [
                Trait._from_dict(x) for x in (_dict.get('children'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Trait object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'trait_id') and self.trait_id is not None:
            _dict['trait_id'] = self.trait_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'category') and self.category is not None:
            _dict['category'] = self.category
        if hasattr(self, 'percentile') and self.percentile is not None:
            _dict['percentile'] = self.percentile
        if hasattr(self, 'raw_score') and self.raw_score is not None:
            _dict['raw_score'] = self.raw_score
        if hasattr(self, 'significant') and self.significant is not None:
            _dict['significant'] = self.significant
        if hasattr(self, 'children') and self.children is not None:
            _dict['children'] = [x._to_dict() for x in self.children]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Trait object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Trait') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Trait') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CategoryEnum(Enum):
        """
        The category of the characteristic: `personality` for Big Five personality
        characteristics, `needs` for Needs, and `values` for Values.
        """
        PERSONALITY = "personality"
        NEEDS = "needs"
        VALUES = "values"


class Warning():
    """
    A warning message that is associated with the input content.

    :attr str warning_id: The identifier of the warning message.
    :attr str message: The message associated with the `warning_id`:
          * `WORD_COUNT_MESSAGE`: "There were {number} words in the input. We need a
          minimum of 600, preferably 1,200 or more, to compute statistically significant
          estimates."
          * `JSON_AS_TEXT`: "Request input was processed as text/plain as indicated,
          however detected a JSON input. Did you mean application/json?"
          * `CONTENT_TRUNCATED`: "For maximum accuracy while also optimizing processing
          time, only the first 250KB of input text (excluding markup) was analyzed.
          Accuracy levels off at approximately 3,000 words so this did not affect the
          accuracy of the profile."
          * `PARTIAL_TEXT_USED`, "The text provided to compute the profile was trimmed for
          performance reasons. This action does not affect the accuracy of the output, as
          not all of the input text was required." Applies only when Arabic input text
          exceeds a threshold at which additional words do not contribute to the accuracy
          of the profile.
    """

    def __init__(self, warning_id: str, message: str) -> None:
        """
        Initialize a Warning object.

        :param str warning_id: The identifier of the warning message.
        :param str message: The message associated with the `warning_id`:
               * `WORD_COUNT_MESSAGE`: "There were {number} words in the input. We need a
               minimum of 600, preferably 1,200 or more, to compute statistically
               significant estimates."
               * `JSON_AS_TEXT`: "Request input was processed as text/plain as indicated,
               however detected a JSON input. Did you mean application/json?"
               * `CONTENT_TRUNCATED`: "For maximum accuracy while also optimizing
               processing time, only the first 250KB of input text (excluding markup) was
               analyzed. Accuracy levels off at approximately 3,000 words so this did not
               affect the accuracy of the profile."
               * `PARTIAL_TEXT_USED`, "The text provided to compute the profile was
               trimmed for performance reasons. This action does not affect the accuracy
               of the output, as not all of the input text was required." Applies only
               when Arabic input text exceeds a threshold at which additional words do not
               contribute to the accuracy of the profile.
        """
        self.warning_id = warning_id
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Warning':
        """Initialize a Warning object from a json dictionary."""
        args = {}
        valid_keys = ['warning_id', 'message']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Warning: ' +
                ', '.join(bad_keys))
        if 'warning_id' in _dict:
            args['warning_id'] = _dict.get('warning_id')
        else:
            raise ValueError(
                'Required property \'warning_id\' not present in Warning JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError(
                'Required property \'message\' not present in Warning JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Warning object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'warning_id') and self.warning_id is not None:
            _dict['warning_id'] = self.warning_id
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Warning object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Warning') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Warning') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class WarningIdEnum(Enum):
        """
        The identifier of the warning message.
        """
        WORD_COUNT_MESSAGE = "WORD_COUNT_MESSAGE"
        JSON_AS_TEXT = "JSON_AS_TEXT"
        CONTENT_TRUNCATED = "CONTENT_TRUNCATED"
        PARTIAL_TEXT_USED = "PARTIAL_TEXT_USED"
