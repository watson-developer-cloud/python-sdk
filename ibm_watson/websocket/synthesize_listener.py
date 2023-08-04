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
import ssl
import time
try:
    import thread
except ImportError:
    import _thread as thread

TEN_MILLISECONDS = 0.01


class SynthesizeListener(object):

    def __init__(self,
                 options,
                 callback,
                 url,
                 headers,
                 http_proxy_host=None,
                 http_proxy_port=None,
                 verify=None):
        self.options = options
        self.callback = callback
        self.url = url
        self.headers = headers
        self.http_proxy_host = http_proxy_host
        self.http_proxy_port = http_proxy_port
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
                                   suppress_origin=True,
                                   sslopt={'cert_reqs': ssl.CERT_NONE}
                                   if self.verify is not None else None)

    def send_text(self):
        """
        Sends the text message
        Note: The service handles one request per connection
        """

        def run(*args):
            """Background process to send the text"""
            self.ws_client.send(json.dumps(self.options).encode('utf8'))

            time.sleep(TEN_MILLISECONDS)

        thread.start_new_thread(run, ())

    def on_open(self, ws):
        """
        Callback executed when a connection is opened to the server.
        Handles sending text to server

        :param ws: Websocket client
        """
        self.callback.on_connected()
        self.send_text()

    def on_data(self, ws, message, message_type, fin):
        """
        Callback executed when message is received from the server.

        :param ws: Websocket client
        :param message: utf-8 string which we get from the server.
        :param message_type: Message type which is either ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY
        :param fin: continue flag. If 0, the data continues.
        """
        try:
            if message_type == websocket.ABNF.OPCODE_TEXT:
                json_object = json.loads(message)
                if 'binary_streams' in json_object:
                    self.callback.on_content_type(
                        json_object['binary_streams'][0]['content_type'])
                elif 'error' in json_object:
                    self.on_error(ws, json_object.get('error'))
                    return
                else:
                    self.callback.on_timing_information(json_object)
        except Exception:
            self.on_error(ws, 'Unable to parse received message.')

        if message_type == websocket.ABNF.OPCODE_BINARY:
            self.callback.on_audio_stream(message)

        self.callback.on_data(message)

    def on_error(self, ws, error):
        """
        Callback executed when an error is received

        :param ws: Websocket client
        :param error: Exception object
        """
        self.callback.on_error(error)

    def on_close(self, ws, *args, **kwargs):
        """
        Callback executed when websocket connection is closed

        :param ws: Websocket client
        """
        self.callback.on_close()
