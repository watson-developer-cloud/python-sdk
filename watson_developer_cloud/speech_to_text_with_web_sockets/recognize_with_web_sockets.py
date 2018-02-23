
import base64 # necessary to encode in base64 according to the RFC2045 standard
import sys
import os
from os.path import join, dirname, isfile, basename, isdir, splitext
from zope.interface import implementer
import json
# WebSockets
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory, connectWS
from twisted.python import log
from twisted.internet import ssl, reactor, interfaces

class SpeechToTextWithWebSockets:
    def __init__(self,
                username=None,
                password=None,
                audio_path=None,
                content_type='audio/l16; rate=44100',
                model='en-US_BroadbandModel',
                customization_id=None,
                acoustic_customization_id=None,
                customization_weight=None,
                version=None,
                x_watson_learning_opt_out=None,
                log_type='stdout',
                inactivity_timeout=600,
                keywords=None,
                keywords_threshold=None,
                max_alternatives=None,
                word_alternatives_threshold=None,
                word_confidence=True,
                timestamps=True,
                profanity_filter=None,
                smart_formatting=None,
                speaker_labels=None):
        self.listeners = []
        if audio_path is None:
              raise ValueError('audio path must be provided')
        if not isfile(audio_path):
            raise TypeError('audio path: {0} file does not exist'.format(audio_path))
        self.audio_path = audio_path
        self.content_type = content_type
        self.username = username
        self.password = password
        unfiltered_options = {
                        'content_type': content_type,
                        'customization_id': customization_id,
                        'acoustic_customization_id': acoustic_customization_id,
                        'customization_weight': customization_weight,
                        'version': version,
                        'x_watson_learning_opt_out': x_watson_learning_opt_out,
                        'inactivity_timeout': inactivity_timeout,
                        'keywords': keywords,
                        'keywords_threshold': keywords_threshold,
                        'max_alternatives': max_alternatives,
                        'word_alternatives_threshold': word_alternatives_threshold,
                        'word_confidence': word_confidence,
                        'timestamps': timestamps,
                        'profanity_filter': profanity_filter,
                        'smart_formatting': smart_formatting,
                        'speaker_labels': speaker_labels
                    }
        self.options = dict([(k, unfiltered_options[k])
                for k
                in unfiltered_options.keys()
                if unfiltered_options[k] is not None])

    def setListeners(self, listeners):
        self.listeners = listeners

    def getListeners(self):
        return self.listeners

    def start(self):
        # logging
        # log.startLogging(sys.stdout)

        authstring = "{0}:{1}".format(self.username, self.password)
        encoded_auth = base64.b64encode(authstring.encode('utf-8')).decode('utf-8')
        headers = {'Authorization': 'Basic {0}'.format(encoded_auth)}
        model = 'en-US_BroadbandModel'
        wsURI = 'wss://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model={0}'.format(model)

        summary = {
            'hypothesis': '',
            'status': {
                'code': '',
                'reason': '',
                'error': '',
                'successful': False
                }
            }

        factory = self.WSInterfaceFactory(self.audio_path,
                                          self.content_type,
                                          summary,
                                          self.options,
                                          wsURI,
                                          headers)
        factory.setListeners(self.listeners)
        factory.protocol = self.WSInterfaceProtocol

        if factory.isSecure:
            contextFactory = ssl.ClientContextFactory()
        else:
            contextFactory = None
        connectWS(factory, contextFactory)

        reactor.run()


    @implementer(interfaces.IPushProducer)
    class AudioProducer:
        def __init__(self, proto, factory):
            self.factory = factory
            self.proto = proto
            self.started = False
            self.paused = False
            self.bytes_sent = 0
            self.chunk_size = 2000     # in bytes

        # helper method that sends a chunk of audio if needed (as required what the specified pacing is)
        def maybeSendChunk(self, data):
            def sendChunk(chunk, final=False):
                self.bytes_sent += len(chunk)
                self.proto.sendMessage(chunk, isBinary=True)
                if final:
                    self.proto.sendMessage(b'', isBinary=True)

            if (self.bytes_sent + self.chunk_size >= len(data)):
                if (len(data) > self.bytes_sent):
                    sendChunk(data[self.bytes_sent:len(data)], True)
                    return

            sendChunk(data[self.bytes_sent:self.bytes_sent + self.chunk_size])
            self.factory.reactor.callLater(0.01, self.maybeSendChunk, data=data)
            return

        def pauseProducing(self):
            self.paused = True

        def resumeProducing(self, data):
            self.paused = False

            if not self.started:
                self.proto.sendMessage(json.dumps(data).encode('utf8'))
                self.started = True

            elif not self.paused:
                self.maybeSendChunk(data)

        def stopProducing(self):
            self.proto.sendClose(1000)

    class WSInterfaceProtocol(WebSocketClientProtocol):
        def __init__(self, factory, audio_path, content_type, summary, options):
            self.listeners = []
            self.factory = factory
            self.audio_path = audio_path
            self.content_type = content_type
            self.summary = summary
            self.init_data = options
            self.listening_messages = 0
            super(self.__class__, self).__init__()

        def setListeners(self, listeners):
            self.listeners = listeners

        def getListeners(self):
            return self.listeners

        def onConnect(self, response):
            log.msg("onConnect, server connected: {}".format(response.peer))

        def onOpen(self):
            log.msg("onOpen, Websocket connection open")

            producer = SpeechToTextWithWebSockets.AudioProducer(self, self.factory)
            self.registerProducer(producer, True)

            # send the initialization parameters
            self.init_data['action'] = 'start'
            self.init_data['interim_results'] = True
            producer.resumeProducing(self.init_data)

            # start sending audio right away (it will get buffered in the STT service)
            f = open(self.audio_path, 'rb')
            producer.resumeProducing(f.read())
            log.msg("onOpen ends")

        def onMessage(self, payload, isBinary):
            # if uninitialized, receive the initialization response from the server
            json_object = json.loads(payload.decode('utf8'))
            if 'state' in json_object:
                self.listening_messages += 1
                if self.listening_messages == 2:
                    # close the connection
                    self.sendMessage(json.dumps({'action': 'close'}).encode('utf8'))
                    self.sendClose(1000)

            if 'error' in json_object:
                self.summary['status']['error'] = json_object['error']
                log.msg('Error : {}'.format(json_object['error']))

            # if in streaming
            elif 'results' in json_object:
                json_object = json.loads(payload.decode('utf8'))
                hypothesis = ""
                # empty hypothesis
                if len(json_object['results']) == 0:
                    print("empty hypothesis!")
                # regular hypothesis
                else:
                    hypothesis = json_object['results'][0]['alternatives'][0]['transcript']
                    b_final = (json_object['results'][0]['final'] == True)
                    transcripts = self.extractTranscripts(json_object['results'][0]['alternatives'])

                    if b_final:
                        self.notifyListeners(payload.decode('utf8'), transcripts)
                        self.summary['hypothesis'] += hypothesis
                    else:
                        self.notifyListeners(payload.decode('utf8'), None, transcripts)

        def extractTranscripts(self, alternatives):
            transcripts = []
            for alternative in alternatives:
                transcript = {}
                if 'confidence' in alternative:
                    transcript['confidence'] = alternative['confidence']
                transcript['transcript'] = alternative['transcript']
                transcripts.append(transcript)
            return transcripts

        def notifyListeners(self, payload, hypothesis=None, interimHypothesis=None):
            for listener in self.listeners:
                listener.listen_payload(payload)
                if hypothesis is not None:
                    listener.listen_hypothesis(hypothesis)
                if interimHypothesis is not None:
                    listener.listen_interim_hypothesis(interimHypothesis)

        def onClose(self, wasClean, code, reason):
            print("onClose, WebSocket connection closed: {0}".format(reason), "code: ", code, "clean: ", wasClean, "reason: ", reason)
            self.summary['status']['code'] = code
            self.summary['status']['reason'] = reason
            if code == 1000:
                self.summary['status']['successful'] = True
            else:
                self.summary['status']['successful'] = False

            self.factory.endReactor()


    class WSInterfaceFactory(WebSocketClientFactory):
        def __init__(self,
                     audio_path,
                     content_type,
                     summary,
                     options,
                     url=None,
                     headers=None):
            WebSocketClientFactory.__init__(self, url=url, headers=headers)
            self.listeners = []
            self.audio_path = audio_path
            self.content_type = content_type
            self.summary = summary
            self.options = options

            self.openHandshakeTimeout = 6
            self.closeHandshakeTimeout = 6

        def setListeners(self, listeners):
            self.listeners = listeners

        def getListeners(self):
            return self.listeners

        def endReactor(self):
            reactor.stop()

        # this function gets called every time connectWS is called (once per WebSocket connection/session)
        def buildProtocol(self, addr):
            proto = SpeechToTextWithWebSockets.WSInterfaceProtocol(self,
                                                       self.audio_path,
                                                       self.content_type,
                                                       self.summary,
                                                       self.options)
            proto.setListeners(self.listeners)
            return proto

class Recognize:
    def __init__(self,
            username=None,
            password=None,
            audio_path=None):
        self.listeners = []
        self.audio_path = audio_path
        self.watsonClient = SpeechToTextWithWebSockets(username, password, audio_path)

    def addListener(self, listener):
        self.listeners.append(listener)

    def setListeners(self, listeners):
        if listeners is not list:
            listeners = [listeners]
        for listener in listeners:
            self.addListener(listener)

    def getListeners(self):
        return self.listeners

    def run(self):
        self.watsonClient.setListeners(self.listeners)
        self.watsonClient.start()