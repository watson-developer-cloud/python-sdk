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


class AudioSource(object):
    """"Audio source for the speech to text recognize using websocket"""

    def __init__(self, input, is_recording=False, is_buffer=False):
        """
        :param bytes/Queue input: The audio to transcribe in the format specified by the
        `Content-Type` header.
        :param bool is_recording: Used to represent if audio recording is in progress
        :param bool is_buffer: `True` if audio is a Queue
        """
        self.input = input
        self.is_recording = is_recording
        self.is_buffer = is_buffer

    def completed_recording(self):
        """
        Sets the `is_recording` to False
        """
        self.is_recording = False
