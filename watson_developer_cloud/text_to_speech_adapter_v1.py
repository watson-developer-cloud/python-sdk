
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

from watson_developer_cloud.websocket import SynthesizeCallback, SynthesizeListener
import base64
from .text_to_speech_v1 import TextToSpeechV1
from .watson_service import _remove_null_values
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

BEARER = 'Bearer'

class TextToSpeechV1Adapter(TextToSpeechV1):
    def synthesize_using_websocket(self,
                                   text,
                                   synthesize_callback,
                                   accept=None,
                                   voice=None,
                                   timings=None,
                                   customization_id=None,
                                   http_proxy_host=None,
                                   http_proxy_port=None,
                                   **kwargs):
        """
        Synthesizes text to spoken audio using web sockets. It supports the use of
        the SSML <mark> element to identify the location of user-specified markers in the audio.
        It can also return timing information for all strings of the input text.
        Note:The service processes one request per connection.

        :param str text: Provides the text that is to be synthesized. The client can pass plain
        text or text that is annotated with the Speech Synthesis Markup Language (SSML). For more
        information, see [Specifying input text](https://console.bluemix.net/docs/services/text-to-speech/http.html#input).
        SSML input can also include the <mark> element;
        see [Specifying an SSML mark](https://console.bluemix.net/docs/services/text-to-speech/word-timing.html#mark).
        The client can pass a maximum of 5 KB of text with the request.
        :param SynthesizeCallback synthesize_callback: The callback method for the websocket.
        :param str accept: Specifies the requested format (MIME type) of the audio. For more information, see [Specifying
        an audio format](https://console.bluemix.net/docs/services/text-to-speech/http.html#format). In addition to the
        supported specifications, you can use */* to specify the default audio format, audio/ogg;codecs=opus.
        :param str voice: The voice to use for synthesis.
        :param list[str] timings: Specifies that the service is to return word timing information for all strings of the
        input text. The service returns the start and end time of each string of the input. Specify words as the lone element
        of the array to request word timings. Specify an empty array or omit the parameter to receive no word timings. For
        more information, see [Obtaining word timings](https://console.bluemix.net/docs/services/text-to-speech/word-timing.html#timing).
        Not supported for Japanese input text.
        :param str customization_id: Specifies the globally unique identifier (GUID) for a custom voice model that is to be used for the
        synthesis. A custom voice model is guaranteed to work only if it matches the language of the voice that is used for the synthesis.
        If you include a customization ID, you must call the method with the service credentials of the custom model's owner. Omit the
        parameter to use the specified voice with no customization. For more information, see [Understanding customization]
        (https://console.bluemix.net/docs/services/text-to-speech/custom-intro.html#customIntro).
        :param str http_proxy_host: http proxy host name.
        :param str http_proxy_port: http proxy port. If not set, set to 80.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `SpeechRecognitionResults` response.
        :rtype: dict
        """
        if text is None:
            raise ValueError('text must be provided')
        if synthesize_callback is None:
            raise ValueError('synthesize_callback must be provided')
        if not isinstance(synthesize_callback, SynthesizeCallback):
            raise Exception(
                'Callback is not a derived class of SynthesizeCallback')

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
            'voice': voice,
            'customization_id': customization_id,
        }
        params = _remove_null_values(params)
        url += '/v1/synthesize?{0}'.format(urlencode(params))

        options = {
            'text': text,
            'accept': accept,
            'timings': timings
        }
        options = _remove_null_values(options)

        SynthesizeListener(options,
                           synthesize_callback,
                           url,
                           headers,
                           http_proxy_host,
                           http_proxy_port,
                           self.verify)
