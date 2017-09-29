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

import json
import responses
import watson_developer_cloud

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/tone-analyzer/api'
base_url = '{0}{1}'.format(platform_url, service_path)

#########################
# tone
#########################


@responses.activate
def test_tone():
    endpoint = '/v3/tone'
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "sentences_tone": [{
            "sentence_id": 6,
            "tones": [""],
            "text": "aeiou"
        }],
        "document_tone": {
            "tones": [{
                "score": 0.8008281904610115,
                "tone_name": "aeiou",
                "tone_id": "aeiou"
            }],
            "warning":
            "aeiou"
        }
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ToneAnalyzerV3(
        username='username', password='password', version='')
    TODO = conversation.tone(
        tone_input=TODO,
        sentences=TODO,)
    # TODO: Asserts


@responses.activate
def test_tone_chat():
    endpoint = '/v3/tone_chat'
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "utterances_tone": [{
            "utterance_text":
            "aeiou",
            "tones": [{
                "score": 0.8008281904610115,
                "tone_name": "aeiou",
                "tone_id": "aeiou"
            }],
            "utterance_id":
            "aeiou",
            "error":
            "aeiou"
        }],
        "warning":
        "aeiou"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ToneAnalyzerV3(
        username='username', password='password', version='')
    TODO = conversation.tone_chat(utterances=TODO)
    # TODO: Asserts
