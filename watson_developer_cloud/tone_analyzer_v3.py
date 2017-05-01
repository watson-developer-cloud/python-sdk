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
The IBM Watson™ Tone Analyzer Service uses linguistic analysis to detect three types of tones from written text: emotions, social tendencies, and language style. Emotions identified include things like anger, cheerfulness and sadness. Identified social tendencies include things from the Big Five personality traits used by some psychologists. These include openness, conscientiousness, extraversion, agreeableness, and neuroticism. Identified language styles include things like confident, analytical, and tentative. Input email and other written media into the Tone Analyzer service, and use the results to determine if your writing comes across with the tone, personality traits, and writing style that you want for your intended audience.
"""

import json
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

    def tone(self,
             text,
             content_type='application/json',
             tones=None,
             sentences=None):
        """
        Analyze general tone.

        Analyze the tone of a piece of text. The message is analyzed for several tones - social, emotional, and language. For each tone, various traits are derived. For example, conscientiousness, agreeableness, and openness.

        :param text: The content to be analyzed. The Tone Analyzer service supports up to 128 KB of text, or about 1000 sentences. Sentences with less than three words cannot be analyzed.
        :param content_type: The type of the input: application/json, text/plain, or application/json.
        :param tones: Filter the results by a specific tone. Valid values are `emotion`, `language`, and `social`.
        :param sentences: Filter your response to remove the sentence level analysis. Valid values are `true` and `false`. This parameter defaults to `true` when it's not set, which means that a sentence level analysis is automatically provided. Change `sentences` to `false` to filter out the sentence level analysis.
        """
        headers = {'content-type': content_type}
        params = {
            'version': self.version,
            'tones': tones,
            'sentences': str(sentences).lower()
        }
        if content_type == 'application/json' and isinstance(text, dict):
            data = json.dumps(text)
        else:
            data = text
        return self.request(
            method='POST',
            url='/v3/tone',
            headers=headers,
            params=params,
            data=data,
            accept_json=True)

    def tone_chat(self, utterances):
        """
        Analyze customer engagement tone.

        Use the Tone Analyzer for Customer Engagement Endpoint to monitor customer service and customer support conversations.

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
