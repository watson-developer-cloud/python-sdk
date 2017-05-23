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

from __future__ import print_function
from .watson_developer_cloud_service import WatsonDeveloperCloudService
import json
from collections import deque, Counter, namedtuple
import base64

from autobahn.twisted.websocket import WebSocketClientFactory,\
    WebSocketClientProtocol, connectWS
from twisted.internet import ssl, reactor, task, interfaces
from zope.interface import implementer

Filedata = namedtuple('FileData', ['file_name',
                                   'file_metadata',
                                   'initial_data'])


@implementer(interfaces.IPushProducer)
class AudioFileProducer(object):
    def __init__(self, proto):
        self.proto = proto
        self.started = False
        self.paused = False
        self.filedata = proto.filedatasource.pop()
        self.fileobj = open(self.filedata.file_name, 'rb')
        self.proto.metadata = self.filedata.file_metadata

    def pauseProducing(self):
        self.paused = True

    def resumeProducing(self):
        self.paused = False
        if not self.started:
            as_json = json.dumps(self.filedata.initial_data).encode('utf-8')
            self.proto.sendMessage(as_json, False)
            self.started = True

        while not self.paused:
            buf = self.fileobj.read(1024)
            if not buf:
                as_json = json.dumps({"action": "stop"}).encode('utf-8')
                self.proto.sendMessage(as_json, False)
                break
            self.proto.sendMessage(buf, True)

    def stopProducing(self):
        self.fileobj.close()


class StreamingSpeechToTextProtocol(WebSocketClientProtocol):
    filedatasource = deque()
    params = {}
    factory = None
    ssl_context_factory = None
    connects = 0

    @classmethod
    def buildFactory(cls, url, headers, params):
        # only build the factory once
        if cls.factory is None:
            cls.factory = WebSocketClientFactory(url, headers=headers)
            cls.factory.protocol = cls
            cls.ssl_context_factory = ssl.ClientContextFactory()
            cls.params = params

    @classmethod
    def start(cls):
        reactor.run()

    @classmethod
    def stop(cls):
        reactor.stop()

    @classmethod
    def addContentType(cls, content_type):
        newparams = cls.params.copy()
        newparams['content-type'] = content_type
        return newparams

    @classmethod
    def addAudioFile(cls, filename, content_type, metadata=None):
        data = cls.addContentType(content_type)
        fdat = Filedata(filename, metadata, data)
        cls.filedatasource.append(fdat)
        connectWS(cls.factory, cls.ssl_context_factory)
        cls.connects += 1

    @classmethod
    def done(cls):
        if cls.connects == 0:
            reactor.stop()

    @classmethod
    def runUntilDone(cls):
        looper = task.LoopingCall(cls.done)
        looper.start(5)
        cls.start()

    def __init__(self):
        super(StreamingSpeechToTextProtocol, self).__init__()
        self.counter = Counter()

    def addState(self, state):
        update = {}
        update[state] = 1
        self.counter.update(update)

    def countState(self, state):
        return self.counter[state]

    def onError(self, error):
        print(error)

    def onOpen(self):
        producer = AudioFileProducer(self)
        self.registerProducer(producer, True)
        producer.resumeProducing()

    def onMessage(self, payload, isBinary):
        pass

    def onConnect(self, request):
        pass

    def onClose(self, wasClean, code, reason):
        self.__class__.connects -= 1


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

    def create_recognize_stream(self,
                                model=None,
                                protocol_class=None,
                                customization_id=None,
                                inactivity_timeout=None,
                                keywords=None, keywords_threshold=None,
                                max_alternatives=None,
                                word_alternatives_threshold=None,
                                word_confidence=None,
                                interim_results=None,
                                timestamps=None,
                                profanity_filter=None,
                                smart_formatting=None,
                                speaker_labels=None):

        url = "wss://{0}{2}?model={1}".format(
            'stream.watsonplatform.net',
            model,
            "/speech-to-text/api/v1/recognize")

        if model is None:
            url = "wss://{0}{2}?model={1}".format(
                'stream.watsonplatform.net',
                'en-US_BroadbandModel',
                "/speech-to-text/api/v1/recognize")

        params = {'action': 'start',
                  'continuous': True,
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

        protocol_class.buildFactory(url, headers, params)
        return params

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

        return self.request(method='POST',
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
