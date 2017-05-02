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

    def tone(self, text, tones=None, sentences=None):
        """
        The tone API is the main API call: it analyzes the "tone" of a piece
        of text. The message is analyzed from
        several tones (social tone, emotional tone, writing tone), and for
        each of them various traits are derived
        (such as conscientiousness, agreeableness, openness).
        :param text: Text to analyze
        :param sentences: If "false", sentence-level analysis is omitted
        :param tones: Can be one or more of 'social', 'language', 'emotion';
        comma-separated.
        """
        params = {'version': self.version}
        if tones is not None:
            params['tones'] = tones
        if sentences is not None:
            params['sentences'] = str(
                sentences).lower()  # Cast boolean to "false" / "true"
        data = {'text': text}
        return self.request(method='POST', url='/v3/tone', params=params,
                            json=data, accept_json=True)

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
