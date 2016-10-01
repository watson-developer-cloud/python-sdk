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

from .watson_developer_cloud_service import WatsonDeveloperCloudService
from .watson_developer_cloud_service import WatsonException
from .watson_developer_cloud_service import WatsonInvalidArgument
from .alchemy_data_news_v1 import AlchemyDataNewsV1
from .alchemy_language_v1 import AlchemyLanguageV1
from .alchemy_vision_v1 import AlchemyVisionV1
from .authorization_v1 import AuthorizationV1
from .conversation_v1 import ConversationV1
from .document_conversion_v1 import DocumentConversionV1
from .dialog_v1 import DialogV1
from .language_translation_v2 import LanguageTranslationV2
from .language_translator_v2 import LanguageTranslatorV2
from .natural_language_classifier_v1 import NaturalLanguageClassifierV1
from .personality_insights_v2 import PersonalityInsightsV2
from .retrieve_and_rank_v1 import RetrieveAndRankV1
from .speech_to_text_v1 import SpeechToTextV1
from .text_to_speech_v1 import TextToSpeechV1
from .tone_analyzer_v3 import ToneAnalyzerV3
from .tradeoff_analytics_v1 import TradeoffAnalyticsV1
from .visual_recognition_v3 import VisualRecognitionV3
from .version import __version__
