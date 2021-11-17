# coding: utf-8
from unittest import TestCase
import os
import ibm_watson
import pytest
import json
import time
from os.path import join

@pytest.mark.skipif(os.getenv('PERSONALITY_INSIGHTS_APIKEY') is None,
                    reason='requires PERSONALITY_INSIGHTS_APIKEY')
class TestPersonalityInsightsV3(TestCase):

    def setUp(self):
        self.personality_insights = ibm_watson.PersonalityInsightsV3(version='2017-10-13')
        self.personality_insights.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

    def test_profile1(self):
        with open(join(os.getcwd(), 'resources/personality-v3.json')) as \
        profile_json:
            profile = self.personality_insights.profile(
                profile_json.read(),
                'application/json',
                raw_scores=True,
                consumption_preferences=True).get_result()
        assert profile is not None
