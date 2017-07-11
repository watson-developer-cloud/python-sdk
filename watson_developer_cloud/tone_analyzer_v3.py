# Copyright 2017 IBM All Rights Reserved.
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
The IBM Watson Tone Analyzer Service uses linguistic analysis to detect
three types of tones from written text: emotions, social tendencies, and
language style. Emotions identified include things like anger, cheerfulness
and sadness. Identified social tendencies include things from the Big Five
personality traits used by some psychologists. These include openness,
conscientiousness, extraversion, agreeableness, and neuroticism. Identified
language styles include things like confident, analytical, and tentative.
Input email and other written media into the Tone Analyzer service, and use
the results to determine if your writing comes across with the tone,
personality traits, and writing style that you want for your intended
audience.
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService

class ToneAnalyzerV3(WatsonDeveloperCloudService):
    """Client for the ToneAnalyzer service."""

    default_url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    latest_version = '2016-05-19'

    def __init__(self, version, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'tone_analyzer', url,
                                             **kwargs)
        self.version = version

    #########################
    # tone
    #########################

    def tone(self, text, tones=None, sentences=None, content_type='text/plain'):
        """
        The general purpose tone API analyzes the "tone" of input text.
        The message is analyzed for several tones (social, emotional, and
        writing), with various characteristics derived for each tone.
        :param text: The input content to analyze.
        :param sentences: If false, sentence-level analysis is omitted; by
        default (or if true), each sentence is analyzed.
        :param tones: A comma-separated list of one or more of the following
        tones for which to analyze the input text, 'social', 'language', and
        'emotion'; the default is all tones.
        :param content_type: The type of the input content: "text/plain"
        (the default), "text/html", or "application/json".
        """

        params = {'version': self.version}
        if tones is not None:
            params['tones'] = tones
        if sentences is not None:
            # Cast boolean to "false" / "true"
            params['sentences'] = str(sentences).lower()
        if content_type == 'text/plain':
            text = {'text': text}
            content_type = 'application/json'
        headers = {'content-type': content_type}

        if content_type == 'application/json':
            return self.request(
                method='POST', headers=headers, url='/v3/tone', params=params,
                json=text, accept_json=True)

        # Use the equivalent of an 'else' rather than checking for explicit
        # 'text/html' so that the call is made and returns a meaningful error
        # for an invalid content type.
        if content_type != 'application/json':
            return self.request(
                method='POST', headers=headers, url='/v3/tone', params=params,
                data=text, accept_json=True)

    #########################
    # tone_chat
    #########################

    def tone_chat(self, utterances):
        """
        Analyze customer engagement tone.

        Use the Tone Analyzer for Customer Engagement Endpoint to monitor
        customer service and customer support conversations.

        :param utterances: The content to be analyzed.
        """
        params = {'version': self.version}
        data = {'utterances': utterances}
        return self.request(
            method='POST',
            url='/v3/tone_chat',
            params=params,
            json=data,
            accept_json=True)
