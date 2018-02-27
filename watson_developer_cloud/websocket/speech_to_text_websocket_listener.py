import sys
import os
import json

# WebSockets
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory, connectWS
from twisted.python import log
from twisted.internet import ssl, reactor


class RecognizeListener:
    def __init__(self, audio, options, recognize_callback, url, headers):
        self.audio = audio
        self.options = options
        self.callback = recognize_callback
        self.url = url
        self.headers = headers

        factory = self.WSInterfaceFactory(self.audio, self.options,
                                          self.callback, self.url, self.headers)
        factory.protocol = self.WSInterfaceProtocol

        if factory.isSecure:
            contextFactory = ssl.ClientContextFactory()
        else:
            contextFactory = None
        connectWS(factory, contextFactory)

        reactor.run()

    class WSInterfaceProtocol(WebSocketClientProtocol):
        def __init__(self, factory, audio, options, callback):
            self.factory = factory
            self.audio = audio
            self.options = options
            self.callback = callback
            self.listening_messages = 0
            self.bytes_sent = 0
            self.ONE_KB = 1000  # in bytes
            self.TIMEOUT_PREFIX = "No speech detected for"
            super(self.__class__, self).__init__()

        def build_start_message(self, options):
            options['action'] = 'start'
            return options

        def build_close_message(self):
            return json.dumps({'action': 'close'})

        # helper method that sends a chunk of audio if needed (as required what the specified pacing is)
        def send_audio(self, data):
            def send_chunk(chunk, final=False):
                self.bytes_sent += len(chunk)
                self.sendMessage(chunk, isBinary=True)
                if final:
                    self.sendMessage(b'', isBinary=True)

            if (self.bytes_sent + self.ONE_KB >= len(data)):
                if (len(data) > self.bytes_sent):
                    send_chunk(data[self.bytes_sent:len(data)], True)
                    return

            send_chunk(data[self.bytes_sent:self.bytes_sent + self.ONE_KB])
            self.factory.reactor.callLater(0.01, self.send_audio, data=data)
            return

        def extract_transcripts(self, alternatives):
            transcripts = []
            for alternative in alternatives:
                transcript = {}
                if 'confidence' in alternative:
                    transcript['confidence'] = alternative['confidence']
                transcript['transcript'] = alternative['transcript']
                transcripts.append(transcript)
            return transcripts

        def onConnect(self, response):
            log.msg("onConnect, server connected: {}".format(response.peer))
            self.callback.on_connected()

        def onOpen(self):
            log.msg("onOpen, Websocket connection open")
            # send the initialization parameters
            init_data = self.build_start_message(self.options)
            self.sendMessage(json.dumps(init_data).encode('utf8'))

            # start sending audio right away (it will get buffered in the STT service)
            self.send_audio(self.audio.read())
            log.msg("onOpen ends")

        def onMessage(self, payload, isBinary):
            json_object = json.loads(payload.decode('utf8'))

            if 'error' in json_object:
                log.msg('Error : {}'.format(json_object['error']))
                # Only call on_error() if a real error occurred. The STT service sends
                # // {"error" : "No speech detected for 5s"} for valid timeouts, configured by
                # options.inactivity_timeout
                error = json_object['error']
                if error.startswith(self.TIMEOUT_PREFIX):
                    self.callback.on_inactivity_timeout()
                else:
                    self.callback.on_error()

            # if uninitialized, receive the initialization response from the server
            elif 'state' in json_object:
                self.listening_messages += 1
                if self.listening_messages == 1:
                    self.callback.on_listening()

                elif self.listening_messages == 2:
                    # close the connection
                    self.sendMessage(self.build_close_message())
                    self.callback.on_transcription_complete()
                    self.sendClose(1000)

            # if in streaming
            elif 'results' in json_object or 'speaker_labels' in json_object:
                hypothesis = ""
                # empty hypothesis
                if len(json_object['results']) == 0:
                    print("empty hypothesis!")
                # regular hypothesis
                else:
                    hypothesis = json_object['results'][0]['alternatives'][0][
                        'transcript']
                    b_final = (json_object['results'][0]['final'] == True)
                    transcripts = self.extract_transcripts(
                        json_object['results'][0]['alternatives'])

                    if b_final:
                        self.callback.on_hypothesis(hypothesis)
                    else:
                        self.callback.on_transcription(transcripts)

        def onClose(self, wasClean, code, reason):
            log.msg("onClose, WebSocket connection closed: {0}".format(reason),
                    "code: ", code, "clean: ", wasClean, "reason: ", reason)
            self.factory.endReactor()

    class WSInterfaceFactory(WebSocketClientFactory):
        def __init__(self, audio, options, callback, url=None, headers=None):
            WebSocketClientFactory.__init__(self, url=url, headers=headers)
            self.audio = audio
            self.options = options
            self.callback = callback

            self.openHandshakeTimeout = 6
            self.closeHandshakeTimeout = 6

        def endReactor(self):
            reactor.stop()

        # this function gets called every time connectWS is called (once per WebSocket connection/session)
        def buildProtocol(self, addr):
            proto = RecognizeListener.WSInterfaceProtocol(
                self, self.audio, self.options, self.callback)
            return proto
