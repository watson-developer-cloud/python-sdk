# coding: utf-8

"""
watson websocket connection for speech-to-text
adapted from: 
https://github.com/watson-developer-cloud/speech-to-text-websockets-python
by @daniel-bolanos 
updated by python 3.5/ Watson SDK class
date: 6/20/17 
by @kstohr

speech recognition using the WebSocket interface to the Watson Speech-to-Text service

"""

import json                        # json
import threading                   # multi threading
import os                          # for listing directories
import queue as Queue              # queue used for thread syncronization
import sys                         # system calls
import base64                      # necessary to encode in base64 according to the RFC2045 standard
import certifi                     # validate secure ssl connection
import requests                    # python HTTP requests library
from os.path import join, dirname  # filepath manipulation
import datetime as dt              # datetime objects
from watson_developer_cloud import SpeechToTextV1 #main stt class

# WebSockets
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory, connectWS
from twisted.python import log
from twisted.internet import ssl, reactor                    
    
class WSSpeechToTextV1(SpeechToTextV1):
    
    class WSInterfaceFactory(WebSocketClientFactory):
        def __init__(self, 
                    queue, 
                    dir_output, 
                    content_type, 
                    model, 
                    options,
                    url=None, 
                     headers=None, 
                     debug=None):

            WebSocketClientFactory.__init__(self, url=url, headers=headers)
            self.queue = queue
            self.dir_output = dir_output
            self.content_type = content_type
            self.model = model
            self.options = options
            self.queueProto = Queue.Queue()
            self.openHandshakeTimeout = 10
            self.closeHandshakeTimeout = 10

            # start the thread that takes care of ending the reactor so
            # the script can finish, the reactor is shutdown and the main loop is exited  
            endingThread = threading.Thread(target=self.endReactor, args=())
            endingThread.daemon = True  
            endingThread.start()

        def prepareUtterance(self):

            try:
                utt = self.queue.get_nowait()
                self.queueProto.put(utt)
                return True
            except Queue.Empty:
                log.msg ("getUtterance: no more utterances to process, queue is empty!")
                return False
            
        # this function gets called if there is a keyboard interrupt (precipitating a connection error) 
        # or a connection error    
        def killReactor(self, wasClean, code, reason): 
            
            #first empty the queue
            while self.queue.empty()== False:
                self.queue.get()
            print ("Stopping the websocket reactor due to an error. Connection code: {0}. Warning: The websocket reactor can be called only once per application. You may need to restart the interpreter before running again.".format(code))
            reactor.callFromThread(reactor.stop)
            return

        def endReactor(self):

            self.queue.join()
            log.msg("About to stop the websocket reactor!")
            reactor.callFromThread(reactor.stop)
            return 

        # this function gets called every time connectWS is called (once
        # per WebSocket connection/session)
        def buildProtocol(self, addr):

            try:
                utt = self.queueProto.get_nowait()
                proto = WSSpeechToTextV1.WSInterfaceProtocol(self, self.queue, self.options,
                                            self.dir_output, self.content_type)
                proto.setUtterance(utt)
                return proto
            except Queue.Empty:
                log.msg("Watson file 'queue' should not be empty, otherwise this function should not have been called")
                print ("Watson file queue should not be empty.")
                return None


    # WebSockets interface to the STT service
    # Note: an object of this class is created for each WebSocket
    # connection, every time we call connectWS
    class WSInterfaceProtocol(WebSocketClientProtocol):

        def __init__(self, factory, queue, options, dir_output, content_type):
            self.factory = factory
            self.queue = queue
            self.options = options
            self.dir_output = dir_output
            self.content_type = content_type
            self.packetRate = 20
            self.listeningMessages = 0
            self.timeFirstInterim = -1
            self.bytesSent = 0
            self.chunkSize = 2000     # in bytes
            super(self.__class__, self).__init__()

            print ("queueSize: " + str(self.queue.qsize()))
            log.msg ("content_type: " +  str(self.content_type) + "\n"              
                     "queueSize: " + str(self.queue.qsize()) +  "\n"               
                     "Transcipts saved to: " + self.dir_output
                  )

        def setUtterance(self, utt):

            self.uttNumber = utt[0]
            self.uttFilename = utt[1]
            split_path = os.path.split(self.uttFilename)[1]
            filename = os.path.splitext(split_path)[0]
            self.fileJson = self.dir_output + "/" + str(filename) + ".json"
            try:
                os.remove(self.fileJson)
            except OSError:
                pass

        # Helper method that sends a chunk of audio if needed (as required
        # what the specified pacing is)
        def maybeSendChunk(self, data):

            def sendChunk(chunk, final=False):
                self.bytesSent += len(chunk)
                self.sendMessage(chunk, isBinary=True)
                if final:
                    self.sendMessage(b'', isBinary=True)

            if (self.bytesSent + self.chunkSize >= len(data)):
                if (len(data) > self.bytesSent):
                    sendChunk(data[self.bytesSent:len(data)], True)
                    return
            sendChunk(data[self.bytesSent:self.bytesSent + self.chunkSize])
            self.factory.reactor.callLater(0.01, self.maybeSendChunk, data=data)
            return

        def onConnect(self, response):
            log.msg ("onConnect, server connected: {0}".format(response.peer))

        def onOpen(self):
            log.msg ("onOpen")
            data = self.options
            log.msg ("sendMessage(init)")
            # send the initialization parameters
            self.sendMessage(json.dumps(data).encode('utf8'))

            # start sending audio right away (it will get buffered in the
            # STT service)
            print ("Sending file: " + str(self.uttNumber) + ": " + str(self.uttFilename))
            log.msg ("Sending file: " + str(self.uttNumber) + ": " + str(self.uttFilename))
            f = open(str(self.uttFilename), 'rb')
            self.bytesSent = 0
            dataFile = f.read()
            self.maybeSendChunk(dataFile)
            log.msg ("File sent: " + str(self.uttNumber) + ": " + str(self.uttFilename))
            log.msg ("onOpen ends.")

        def onMessage(self, payload, isBinary):

            if isBinary:
                print("Binary message received: {0} bytes".format(len(payload)))
            else:
                #print output to log (or stdout, if log to stdout selected.)
                log.msg(u"Text message received: {0}".format(payload.decode('utf8')))

                # if uninitialized, receive the initialization response
                # from the server
                jsonObject = json.loads(payload.decode('utf8'))
                if 'state' in jsonObject:
                    self.listeningMessages += 1
                    if (self.listeningMessages == 2):
                        log.msg ("Closing connection to Watson. Sending code: 1000")
                        # close the connection
                        self.sendClose(1000)

                if 'error' in jsonObject:
                    #all responses are printed to log, also print errors to console
                    print ('Error message received from Watson: {0}'.format(jsonObject['error']))

                # if in streaming
                elif 'results' in jsonObject:
                    jsonObject = json.loads(payload.decode('utf8'))
                    # empty hypothesis
                    if (len(jsonObject['results']) == 0):
                        print ("Warning: Watson returned empty results!")
                    # regular hypothesis
                    else:
                        # dump the message to the output directory
                        jsonObject = json.loads(payload.decode('utf8'))
                        f = open(self.fileJson, "a")
                        f.write(json.dumps(jsonObject, indent=4, sort_keys=True))
                        f.close()
                        print ("Transcipt successfully saved to: " + self.dir_output)

        def onClose(self, wasClean, code, reason):

            log.msg("onClose")

            if not code == 1000:
                log.msg ("WebSocket connection error: {0}".format(reason), "code: ", 
                         code, "clean: ", wasClean, "reason: ", reason)
                #clear the queue, shutdown the reactor
                self.factory.killReactor(wasClean, code, reason)
                return

            else: 
                log.msg ("WebSocket connection closed: {0}".format(reason), "code: ",
                  code, "clean: ", wasClean, "reason: ", reason)
                print ("WebSocket connection closed. Status code: {0}".format(code))

            # create a new WebSocket connection if there are still
            # utterances in the queue that need to be processed
            self.queue.task_done()

            if self.factory.prepareUtterance() == False:
                return

            # SSL client context: default
            if self.factory.isSecure:
                contextFactory = ssl.ClientContextFactory()
            else:
                contextFactory = None

            # start new websocket connection
            connectWS(self.factory, contextFactory)


    def recognize(self, 
                  file_input=[],
                  dir_output = None, 
                  threads = None,
                  log_type = None,
                  content_type=None, #required
                  interim_results=None,
                  model=None,
                  customization_id=None,
                  inactivity_timeout=None,
                  keywords=None,
                  keywords_threshold=None,
                  max_alternatives=None,
                  word_alternatives_threshold=None,
                  word_confidence=None,
                  timestamps=None,
                  profanity_filter=None,
                  smart_formatting=None,
                  speaker_labels=None):
        
        if model is None:
            model = 'en-US_BroadbandModel'
            
        if threads is None: 
            threads = 1
        
        #set default logging to stdout, unless an output directory is specified
        if (log_type is None):
            if dir_output is None: 
                log_type = 'stdout'
            else:
                log_type = 'file'   
                
        #set default output path to directory in which interpreter was started (current working directory)
        if dir_output is None: 
            dir_output = os.getcwd() 
            print ("Saving output to current working directory {0}".format(dir_output))
            dir_output = os.getcwd() 
                                    
        authstring = "{0}:{1}".format(self.username, self.password)
        encoded_auth = base64.b64encode(authstring.encode('utf-8')).decode('utf-8')

        headers = {'Authorization': 'Basic {0}'.format(encoded_auth)}
        
        now = dt.datetime.now()
    
        # create output directory if necessary
        dir_output = os.path.join(dir_output, '')
        if not (os.path.isdir(dir_output)):
            try:
                os.makedirs(dir_output)
            except OSError as e: 
                raise (e)
            
        unfiltered_options = {
            'content_type': content_type,
            'inactivity_timeout': inactivity_timeout,
            'interim_results': interim_results,
            'inactivity_timeout': inactivity_timeout,
            'word_confidence': word_confidence,
            'timestamps': timestamps,
            'max_alternatives': max_alternatives,
            'word_alternatives_threshold': word_alternatives_threshold,
            'profanity_filter': profanity_filter,
            'smart_formatting': smart_formatting,
            'keywords': keywords,
            'keywords_threshold': keywords_threshold,
            'max_alternatives': max_alternatives,
            'speaker_labels': speaker_labels}

        options = dict([(k, unfiltered_options[k])
                        for k
                        in unfiltered_options.keys()
                        if unfiltered_options[k] is not None])
        
        options['action'] = 'start'
        
        
        # logging from Twisted module 
        if log_type == 'file': 
            log.startLogging(open(dir_output + "_" + str(now) + "_" + "transcript.log", 'w'), setStdout=False)   
        elif log_type == 'stdout':
            log.startLogging(sys.stdout)
        else:
            raise ValueError ("Please select a destination for the logging: 'file' or 'stdout'")

        # add audio files to the processing queue
        queue = Queue.Queue()
        fileNumber = 0
        for fileName in file_input:
            log.msg (fileName)
            queue.put((fileNumber, fileName))
            fileNumber += 1

        # create a WS server factory with our protocol
        hostname="stream.watsonplatform.net" #set base connection url
        url = "wss://" + hostname + "/speech-to-text/api/v1/recognize?model=" + model
    
        factory = self.WSInterfaceFactory(queue, dir_output, content_type,
                                     model, options, url, headers, debug=False)
            
        factory.protocol = self.WSInterfaceProtocol

        for i in range(min(int(threads), queue.qsize())):

            factory.prepareUtterance()

            # SSL client context: default
            if factory.isSecure:
                contextFactory = ssl.ClientContextFactory()
            else:
                contextFactory = None
            
            connectWS(factory, contextFactory)

        #reactors can be called only once per application
        reactor.run()