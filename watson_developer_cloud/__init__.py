# coding: utf-8
# Copyright 2016 IBM All Rights Reserved.
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

from .watson_service import WatsonService
from .watson_service import WatsonException
from .watson_service import WatsonApiException
from .watson_service import WatsonInvalidArgument
from .authorization_v1 import AuthorizationV1
from .iam_token_manager import IAMTokenManager
from .conversation_v1 import ConversationV1
from .assistant_v1 import AssistantV1
from .assistant_v2 import AssistantV2
from .language_translator_v3 import LanguageTranslatorV3
from .natural_language_classifier_v1 import NaturalLanguageClassifierV1
from .natural_language_understanding_v1 import NaturalLanguageUnderstandingV1
from .personality_insights_v3 import PersonalityInsightsV3
from .text_to_speech_v1 import TextToSpeechV1
from .tone_analyzer_v3 import ToneAnalyzerV3
from .discovery_v1 import DiscoveryV1
from .version import __version__
from .speech_to_text_v1_adapter import SpeechToTextV1Adapter as SpeechToTextV1
from .visual_recognition_v3_adapter import VisualRecognitionV3Adapter as VisualRecognitionV3
