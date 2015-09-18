# Copyright 2015 IBM All Rights Reserved.
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

from .watson_developer_cloud_service import WatsonDeveloperCloudService
from .watson_developer_cloud_service import WatsonException
from .watson_developer_cloud_service import WatsonInvalidArgument
from .authorization_v1 import AuthorizationV1
from .concept_expansion_v1_beta import ConceptExpansionV1Beta
from .concept_insights_v2 import ConceptInsightsV2
from .dialog_v1_beta import DialogV1Experimental
from .language_translation_v2 import LanguageTranslationV2
from .message_resonance_v1_beta import MessageResonanceV1Beta
from .natural_language_classifier_v1 import NaturalLanguageClassifierV1
from .personality_insights_v2 import PersonalityInsightsV2
from .question_and_answer_v1_beta import QuestionAndAnswerV1Beta
from .relationship_extraction_v1_beta import RelationshipExtractionV1Beta
from .speech_to_text_v1 import SpeechToTextV1
from .text_to_speech_v1 import TextToSpeechV1
from .tone_analyzer_v1_experimental import ToneAnalyzerV1Experimental
from .tone_analyzer_v2_experimental import ToneAnalyzerV2Experimental
from .tradeoff_analytics_v1 import TradeoffAnalyticsV1
from .visual_recognition_v1_beta import VisualRecognitionV1Beta


__version__ = '0.1.0'
