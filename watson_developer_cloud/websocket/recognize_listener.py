import websocket
import json
import time
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
CLOSE = "close"

class RecognizeListener(object):
    def __init__(self, audio, options, callback, url, headers, http_proxy_host=None, http_proxy_port=None):
        self.audio = audio # TBD: this should be a audio file or microphone
        self.options = options
        self.callback = callback
        self.url = url
        self.headers = headers
        self.http_proxy_host = http_proxy_host
        self.http_proxy_port = http_proxy_port
        self.isListening = False

        self.ws_client = websocket.WebSocketApp(
            self.url,
            header=self.headers,
            on_open=self.on_open,
            on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )

        self.ws_client.run_forever(http_proxy_host=self.http_proxy_host, http_proxy_port=self.http_proxy_port)

    def build_start_message(self, options):
        options[ACTION] = START
        return options

    def build_closing_message(self):
        return json.dumps({ACTION: CLOSE}).encode('utf8')

    def extract_transcripts(self, alternatives):
        transcripts = []
        for alternative in alternatives:
            transcript = {}
            if 'confidence' in alternative:
                transcript['confidence'] = alternative['confidence']
            transcript['transcript'] = alternative['transcript']
            transcripts.append(transcript)
        return transcripts

    def on_open(self, ws):
        """
        Callback executed when a connection is opened to the server.
        Handles streaming of audio to the server.

        :param ws: Websocket client
        """
        self.callback.on_connected()

        # Send initialization message
        init_data = self.build_start_message(self.options)
        self.ws_client.send(json.dumps(init_data).encode('utf8'), websocket.ABNF.OPCODE_TEXT)

        # Stream audio to server
        def run(*args):
            """Background process to stream the data"""
            while True:
                chunk = self.audio.read(ONE_KB)
                if not chunk:
                    break
                self.ws_client.send(chunk, websocket.ABNF.OPCODE_BINARY)
                time.sleep(TEN_MILLISECONDS)

            self.audio.close()
            time.sleep(TEN_MILLISECONDS)
            self.ws_client.send(self.build_closing_message(), websocket.ABNF.OPCODE_TEXT)
            ws.close()

        thread.start_new_thread(run, ())

    def on_data(self, ws, message, message_type, fin):
        """
        Callback executed when message is received from the server.

        :param ws: Websocket client
        :param message: utf-8 string which we get from the server.
        :param message_type: Message type which is either ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY
        :param fin: continue flag. If 0, the data continues.
        """
        json_object = json.loads(message.decode('utf8'))

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
            else:
                # close the connection
                self.ws_client.send(self.build_closing_message(), websocket.ABNF.OPCODE_TEXT)
                self.ws.close()

        # if in streaming
        elif 'results' in json_object or 'speaker_labels' in json_object:
            hypothesis = ''
            if 'results' in json_object:
                hypothesis = json_object['results'][0]['alternatives'][0][
                    'transcript']
                b_final = (json_object['results'][0]['final'] is True)
                transcripts = self.extract_transcripts(
                    json_object['results'][0]['alternatives'])

                if b_final:
                    self.callback.on_transcription(transcripts)

                self.callback.on_hypothesis(hypothesis)
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
