# coding: utf-8
from unittest import TestCase
import os
import ibm_watson
import pytest
import json
import time
from os.path import join
from ibm_watson.tone_analyzer_v3 import ToneInput

@pytest.mark.skipif(os.getenv('TONE_ANALYZER_APIKEY') is None,
                    reason='requires PTONE_ANALYZER_APIKEY')
class TestToneAnalyzerV3(TestCase):

    def setUp(self):
        self.tone_analyzer = ibm_watson.ToneAnalyzerV3(version='2017-09-21')
        self.tone_analyzer.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

    def test_tone_chat(self):
        utterances = [{
            'text': 'I am very happy.',
            'user': 'glenn'
        }, {
            'text': 'It is a good day.',
            'user': 'glenn'
        }]
        tone_chat = self.tone_analyzer.tone_chat(utterances).get_result()
        assert tone_chat is not None

    def test_tone1(self):
        tone = self.tone_analyzer.tone(tone_input='I am very happy. It is a good day.', content_type="text/plain").get_result()
        assert tone is not None

    def test_tone2(self):
        with open(join(os.getcwd(), 'resources/tone-example.json')) as tone_json:
            tone = self.tone_analyzer.tone(json.load(tone_json)['text'], content_type="text/plain").get_result()
        assert tone is not None

    def test_tone3(self):
        with open(join(os.getcwd(), 'resources/tone-example.json')) as tone_json:
            tone = self.tone_analyzer.tone(tone_input=json.load(tone_json)['text'], content_type='text/plain', sentences=True).get_result()
        assert tone is not None

    def test_tone4(self):
        with open(join(os.getcwd(), 'resources/tone-example.json')) as tone_json:
            tone = self.tone_analyzer.tone(tone_input=json.load(tone_json), content_type='application/json').get_result()
        assert tone is not None

    def test_tone5(self):
        with open(join(os.getcwd(), 'resources/tone-example-html.json')) as tone_html:
            tone = self.tone_analyzer.tone(json.load(tone_html)['text'],content_type='text/html').get_result()
        assert tone is not None

    def test_tone6(self):
        tone_input = ToneInput('I am very happy. It is a good day.')
        tone = self.tone_analyzer.tone(tone_input=tone_input, content_type="application/json").get_result()
        assert tone is not None