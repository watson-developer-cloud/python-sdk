# coding: utf-8
# (C) Copyright IBM Corp. 2016, 2019.
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

from ibm_cloud_sdk_core import IAMTokenManager, DetailedResponse, BaseService, ApiException

from .assistant_v1 import AssistantV1
from .assistant_v2 import AssistantV2
from .language_translator_v3 import LanguageTranslatorV3
from .natural_language_classifier_v1 import NaturalLanguageClassifierV1
from .natural_language_understanding_v1 import NaturalLanguageUnderstandingV1
from .personality_insights_v3 import PersonalityInsightsV3
from .text_to_speech_v1 import TextToSpeechV1
from .tone_analyzer_v3 import ToneAnalyzerV3
from .discovery_v1 import DiscoveryV1
from .discovery_v2 import DiscoveryV2
from .compare_comply_v1 import CompareComplyV1
from .visual_recognition_v3 import VisualRecognitionV3
from .version import __version__
from .common import get_sdk_headers
from .speech_to_text_v1_adapter import SpeechToTextV1Adapter as SpeechToTextV1
from .text_to_speech_adapter_v1 import TextToSpeechV1Adapter as TextToSpeechV1
from .visual_recognition_v4 import VisualRecognitionV4
