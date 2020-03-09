# coding: utf-8

# (C) Copyright IBM Corp. 2018, 2019.
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


class SynthesizeCallback(object):

    def __init__(self):
        pass

    def on_connected(self):
        """
        Called when a Websocket connection was made
        """

    def on_error(self, error):
        """
        Called when there is an error in the Websocket connection.
        """

    def on_content_type(self, content_type):
        """
        Called when the service responds with the format of the audio response
        """

    def on_timing_information(self, timing_information):
        """
        Called when the service returns timing information
        """

    def on_audio_stream(self, audio_stream):
        """
        Called when the service sends the synthesized audio as a binary stream of data in the indicated format.
        """

    def on_data(self, data):
        """
        Called when the service returns results. The data is returned unparsed.
        """

    def on_close(self):
        """
        Called when the Websocket connection is closed
        """
