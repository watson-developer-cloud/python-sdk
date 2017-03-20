# Copyright 2016 IBM All Rights Reserved.
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
The v1 Speech to Text service
(https://www.ibm.com/watson/developercloud/speech-to-text.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService
import json
import base64

from autobahn.twisted.websocket import WebSocketClientFactory,\
    WebSocketClientProtocol, connectWS
from twisted.internet import ssl, reactor


class SpeechToTextWebSocketClientProtocol(WebSocketClientProtocol):
    def setFile(self, filename):
        self.filename = filename
    def setContentType(self, content_type):
        self.contentType = content_type
    def setFactory(self, factory):
        self.factory = factory
    def setCallback(self, callableobj):
        self.messageCallback = callableobj
    def setParams(self, params):
        self.params = params
    def onOpen(self):
        data = self.params
        # send the initialization parameters
        self.sendMessage(json.dumps(data).encode('utf-8'))
        with open(self.filename, 'rb') as audiofile:
            while True:
                buf = audiofile.read(1024)
                if not buf:
                    self.sendMessage(json.dumps({'action': 'stop'}).encode('utf-8'))
                    break
                self.sendMessage(buf, isBinary=True)

    def onMessage(self, payload, is_binary):
        if not is_binary:
            json_payload = json.loads(payload)
            try:
                self.messageCallback(json_payload)
            except AttributeError:
                # if we don't have a message callback, don't worry about it
                pass
            if 'results' in json_payload:
                if len(json_payload['results']) > 0:
                    if 'final' in json_payload['results'][0]:
                        if json_payload['results'][0]['final']:
                            # if we're final, close it up
                            self.sendClose(1000)

    def onClose(self, wasClean, code, reason):
        reactor.stop()

class SpeechToTextWebSocketInterfaceFactory(WebSocketClientFactory):
    def __init__(self, target_file,
                 content_type=None,
                 content_callback=None,
                 params=None,
                 url=None,
                 headers=None):

        WebSocketClientFactory.__init__(self, url=url, headers=headers)
        self.file = target_file
        self.content_type = content_type
        self.content_callback = content_callback
        self.params = params
    def buildProtocol(self, addr):
        proto = SpeechToTextWebSocketClientProtocol()
        proto.setFile(self.file)
        proto.setContentType(self.content_type)
        proto.setCallback(self.content_callback)
        proto.setFactory(self)
        proto.setParams(self.params)
        return proto

class SpeechToTextV1(WatsonDeveloperCloudService):
    default_host = 'stream.watsonplatform.net'
    default_url = 'https://{0}/speech-to-text/api'.format(default_host)

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'speech_to_text', url,
                                             **kwargs)

    def recognize(self, audio, content_type, continuous=False, model=None,
                  customization_id=None,
                  inactivity_timeout=None,
                  keywords=None, keywords_threshold=None,
                  max_alternatives=None,
                  word_alternatives_threshold=None,
                  word_confidence=None, timestamps=None, interim_results=None,
                  profanity_filter=None,
                  smart_formatting=None,
                  speaker_labels=None):
        """
        Returns the recognized text from the audio input
        """
        headers = {'content-type': content_type}
        params = {'continuous': continuous,
                  'inactivity_timeout': inactivity_timeout,
                  'keywords': keywords,
                  'keywords_threshold': keywords_threshold,
                  'max_alternatives': max_alternatives,
                  'model': model,
                  'customization_id': customization_id,
                  'word_alternatives_threshold': word_alternatives_threshold,
                  'word_confidence': word_confidence,
                  'timestamps': timestamps,
                  'interim_results': interim_results,
                  'profanity_filter': profanity_filter,
                  'smart_formatting': smart_formatting,
                  'speaker_labels': speaker_labels}

        return self.request(method='POST', url='/v1/recognize',
                            headers=headers,
                            data=audio, params=params,
                            stream=True, accept_json=True)

    def create_recognize_stream(self, audio, content_type,
                                model=None,
                                content_callback=None,
                                customization_id=None,
                                inactivity_timeout=None,
                                keywords=None, keywords_threshold=None,
                                max_alternatives=None,
                                word_alternatives_threshold=None,
                                word_confidence=None, timestamps=None, interim_results=None,
                                profanity_filter=None,
                                smart_formatting=None,
                                speaker_labels=None):

        url = "wss://{0}/speech-to-text/api/v1/recognize?model={1}".format('stream.watsonplatform.net',
                                                                           model)
        if model is None:
            url = "wss://{0}/speech-to-text/api/v1/recognize?model={1}".format('stream.watsonplatform.net',
                                                                               'en-US_BroadbandModel')

        params = {'continuous': True,
                  'inactivity_timeout': inactivity_timeout,
                  'keywords': keywords,
                  'keywords_threshold': keywords_threshold,
                  'max_alternatives': max_alternatives,
                  'customization_id': customization_id,
                  'word_alternatives_threshold': word_alternatives_threshold,
                  'word_confidence': word_confidence,
                  'timestamps': timestamps,
                  'interim_results': interim_results,
                  'profanity_filter': profanity_filter,
                  'smart_formatting': smart_formatting,
                  'speaker_labels': speaker_labels}
        # filter and remove None's
        params = dict([(k, params[k])
                       for k
                       in params.keys()
                       if params[k] is not None])

        headers = {}
        headers["Authorization"] = "Basic {0}".format(
            base64.b64encode("{0}:{1}".format(self.username,
                                              self.password)
                             .encode('utf-8')).decode('utf-8'))
        factory = SpeechToTextWebSocketInterfaceFactory(audio,
                                                        content_type=content_type,
                                                        content_callback=content_callback,
                                                        url=url,
                                                        params=params,
                                                        headers=headers)
        factory.protocol = SpeechToTextWebSocketClientProtocol

        if factory.isSecure:
            context_factory = ssl.ClientContextFactory()
        else:
            context_factory = None
        connectWS(factory, context_factory)
        reactor.run()

    def models(self):
        """
        Returns the list of available models to use with recognize
        """
        return self.request(method='GET', url='/v1/models', accept_json=True)

    def get_model(self, model_id):
        """
        :param model_id: The identifier of the desired model
        :return: A single instance of a Model object with results for the
        specified model.
        """
        return self.request(method='GET',
                            url='/v1/models/{0}'.format(model_id),
                            accept_json=True)

    def create_custom_model(self, name, description="",
                            base_model="en-US_BroadbandModel"):
        json_body = json.dumps({'name': name, 'description': description,
                                'base_model_name': base_model})
        return self.request(method='POST', url='/v1/customizations',
                            headers={'content-type': 'application/json'},
                            data=json_body, accept_json=True)

    def list_custom_models(self):
        return self.request(method='GET', url='/v1/customizations',
                            accept_json=True)

    def get_custom_model(self, modelid):
        return self.request(method='GET',
                            url='/v1/customizations/{0}'.format(modelid),
                            accept_json=True)

    def delete_custom_model(self, modelid):
        return self.request(method='DELETE',
                            url='/v1/customizations/{0}'.format(modelid),
                            accept_json=True)

    def list_corpora(self, customization_id):
        url = '/v1/customizations/{0}/corpora'
        return self.request(method='GET',
                            url=url.format(customization_id),
                            accept_json=True)

    def add_corpus(self,
                   customization_id,
                   corpus_name,
                   file_data,
                   allow_overwrite=None):

        url = '/v1/customizations/{0}/corpora/{1}'

        if allow_overwrite is None:
            allow_overwrite = False

        headers = {'Content-Type': 'application/octet-stream'}

        return self.request(method='GET',
                            url=url.format(customization_id,
                                           corpus_name),
                            headers=headers,
                            data=file_data,
                            params={'allow_overwrite': allow_overwrite},
                            accept_json=True)

    def get_corpus(self, customization_id, corpus_name):
        url = '/v1/customizations/{0}/corpora/{1}'
        return self.request(method='GET',
                            url=url.format(customization_id,
                                           corpus_name),
                            accept_json=True)

    def delete_corpus(self, customization_id, corpus_name):
        url = '/v1/customizations/{0}/corpora/{1}'
        return self.request(method='DELETE',
                            url=url.format(customization_id,
                                           corpus_name),
                            accept_json=True)

    class CustomWord(object):
        def __init__(self, word=None, sounds_like=None, display_as=None):
            self._word = word
            self._sounds_like = sounds_like
            self._display_as = display_as

        @property
        def word(self):
            return self._word

        @property
        def sounds_like(self):
            return self._sounds_like

        @property
        def display_as(self):
            return self._display_as

        def __dict__(self):
            return {'word': self.word,
                    'sounds_like': self.sounds_like,
                    'display_as': self.display_as}

    def add_custom_words(self, customization_id, custom_words):
        url = '/v1/customizations/{0}/words'
        payload = {'words': [x.__dict__() for x in custom_words]}
        return self.request(method='POST',
                            url=url.format(customization_id),
                            data=json.dumps(payload),
                            headers={'content-type': 'application/json'},
                            accept_json=True)

    def add_custom_word(self, customization_id, custom_word):
        url = '/v1/customizations/{0}/words/{1}'

        custom_word_fragment = {'sounds_like': custom_word.sounds_like,
                                'display_as': custom_word.display_as}
        return self.request(method='POST',
                            url=url.format(customization_id,
                                           custom_word.word),
                            data=json.dumps(custom_word_fragment),
                            headers={'content-type': 'application/json'},
                            accept_json=True)

    def list_custom_words(self, customization_id, word_type=None, sort=None):
        url = '/v1/customizations/{0}/words'
        qs = {}

        if word_type:
            if word_type in ['all', 'user', 'corpora']:
                qs['word_type'] = word_type
            else:
                raise KeyError('word type must be all, user, or corpora')

        if sort:
            if sort in ['alphabetical', 'count']:
                qs['sort'] = sort
            else:
                raise KeyError('sort must be alphabetical or count')

        return self.request(method='GET',
                            url=url.format(customization_id),
                            params=qs,
                            accept_json=True)

    def get_custom_word(self, customization_id, custom_word):
        url = '/v1/customizations/{0}/words/{1}'
        word = None
        if isinstance(custom_word, str):
            word = custom_word
        else:
            word = custom_word.word

        return self.request(method='GET',
                            url=url.format(customization_id, word),
                            accept_json=True)

    def delete_custom_word(self, customization_id, custom_word):
        url = '/v1/customizations/{0}/words/{1}'
        word = None
        if isinstance(custom_word, str):
            word = custom_word
        else:
            word = custom_word.word

        return self.request(method='DELETE',
                            url=url.format(customization_id, word),
                            accept_json=True)
