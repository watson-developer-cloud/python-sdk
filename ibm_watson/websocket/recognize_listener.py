# coding: utf-8

# (C) Copyright IBM Corp. 2018, 2020.
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

import websocket
import json
import time
import ssl
try:
    import thread
except ImportError:
    import _thread as thread

ONE_KB = 1024
TIMEOUT_PREFIX = "No speech detected for"
TEN_MILLISECONDS = 0.01
STATE = "state"
ACTION = "action"
START = "start"
STOP = "stop"


class RecognizeListener(object):

    def __init__(self,
                 audio_source,
                 options,
                 callback,
                 url,
                 headers,
                 http_proxy_host=None,
                 http_proxy_port=None,
                 verify=None):
        self.audio_source = audio_source
        self.options = options
        self.callback = callback
        self.url = url
        self.headers = headers
        self.http_proxy_host = http_proxy_host
        self.http_proxy_port = http_proxy_port
        self.isListening = False
        self.verify = verify

        self.ws_client = websocket.WebSocketApp(
            self.url,
            header=self.headers,
            on_open=self.on_open,
            on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )

        self.ws_client.run_forever(http_proxy_host=self.http_proxy_host,
                                   http_proxy_port=self.http_proxy_port,
                                   sslopt={"cert_reqs": ssl.CERT_NONE}
                                   if self.verify is not None else None)

    @classmethod
    def build_start_message(cls, options):
        options[ACTION] = START
        return options

    @classmethod
    def build_closing_message(cls):
        return json.dumps({ACTION: STOP}).encode('utf8')

    @classmethod
    def extract_transcripts(cls, alternatives):
        transcripts = []
        for alternative in alternatives:
            transcript = {}
            if 'confidence' in alternative:
                transcript['confidence'] = alternative['confidence']
            transcript['transcript'] = alternative['transcript']
            transcripts.append(transcript)
        return transcripts

    def send(self, data, opcode=websocket.ABNF.OPCODE_TEXT):
        """
        Send message to server.

        data: message to send. If you set opcode to OPCODE_TEXT,
              data must be utf-8 string or unicode.
        opcode: operation code of data. default is OPCODE_TEXT.
        """
        self.ws_client.send(data, opcode)

    def send_audio(self, ws):
        """
        Stream audio to server

        :param ws: Websocket client
        """

        def run(*args):
            """Background process to stream the data"""
            if not self.audio_source.is_buffer:
                while True:
                    chunk = self.audio_source.input.read(ONE_KB)
                    if not chunk:
                        break
                    self.ws_client.send(chunk, websocket.ABNF.OPCODE_BINARY)
                    time.sleep(TEN_MILLISECONDS)

                self.audio_source.input.close()
            else:
                while True:
                    try:
                        if not self.audio_source.input.empty():
                            chunk = self.audio_source.input.get()
                            self.ws_client.send(chunk,
                                                websocket.ABNF.OPCODE_BINARY)
                            time.sleep(TEN_MILLISECONDS)
                        if self.audio_source.input.empty():
                            if self.audio_source.is_recording:
                                time.sleep(TEN_MILLISECONDS)
                            else:
                                break
                    except Exception:
                        if self.audio_source.is_recording:
                            time.sleep(TEN_MILLISECONDS)
                        else:
                            break

            time.sleep(TEN_MILLISECONDS)
            self.ws_client.send(self.build_closing_message(),
                                websocket.ABNF.OPCODE_TEXT)

        thread.start_new_thread(run, ())

    def on_open(self, ws):
        """
        Callback executed when a connection is opened to the server.
        Handles streaming of audio to the server.

        :param ws: Websocket client
        """
        self.callback.on_connected()

        # Send initialization message
        init_data = self.build_start_message(self.options)
        self.ws_client.send(
            json.dumps(init_data).encode('utf8'), websocket.ABNF.OPCODE_TEXT)

    def on_data(self, ws, message, message_type, fin):
        """
        Callback executed when message is received from the server.

        :param ws: Websocket client
        :param message: utf-8 string which we get from the server.
        :param message_type: Message type which is either ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY
        :param fin: continue flag. If 0, the data continues.
        """

        try:
            json_object = json.loads(message)
        except Exception:
            self.on_error(ws, 'Unable to parse received message.')

        if 'error' in json_object:
            # Only call on_error() if a real error occurred. The STT service sends
            # {"error" : "No speech detected for 5s"} for valid timeouts, configured by
            # options.inactivity_timeout
            error = json_object['error']
            if error.startswith(TIMEOUT_PREFIX):
                self.callback.on_inactivity_timeout(error)
            else:
                self.on_error(ws, error)

        # if uninitialized, receive the initialization response from the server
        elif 'state' in json_object:
            if not self.isListening:
                self.isListening = True
                self.callback.on_listening()
                self.send_audio(ws)
            else:
                # close the connection
                self.callback.on_close()
                ws.close()

        # if in streaming
        elif 'results' in json_object or 'speaker_labels' in json_object:
            # If results are present, extract the hypothesis and, if finalized, the full
            # set of transcriptions and send them to the appropriate callbacks.
            results = json_object.get('results')
            if results:
                if (self.options.get('interim_results') is True):
                    b_final = (results[0].get('final') is True)
                    alternatives = results[0].get('alternatives')
                    if alternatives:
                        hypothesis = alternatives[0].get('transcript')
                        transcripts = self.extract_transcripts(alternatives)
                        if b_final:
                            self.callback.on_transcription(transcripts)
                        if hypothesis:
                            self.callback.on_hypothesis(hypothesis)
                else:
                    final_transcript = []
                    for result in results:
                        transcript = self.extract_transcripts(
                            result.get('alternatives'))
                        final_transcript.append(transcript)

                    self.callback.on_transcription(final_transcript)

            # Always call the on_data callback if 'results' or 'speaker_labels' are present
            self.callback.on_data(json_object)

    def on_error(self, ws, error):
        """
        Callback executed when an error is received

        :param ws: Websocket client
        :param error: Exception object
        """
        self.callback.on_error(error)

    def on_close(self, ws):
        """
        Callback executed when websocket connection is closed

        :param ws: Websocket client
        """
        self.callback.on_close()
