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
"""
The AlchemyAPI Language service
(http://www.alchemyapi.com/products/alchemylanguage)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class AlchemyLanguageV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'alchemy_api', url, **kwargs)

    def author(self, html=None, url=None):
        return self._alchemy_html_request('GetAuthor', html=html, url=url)

    def authors(self, html=None, url=None):
        return self._alchemy_html_request('GetAuthors', html=html, url=url)

    def keywords(self, html=None, text=None, url=None, strict_extract_mode=False, sentiment=False,
                 show_source_text=False, max_keywords=50):
        params = {'keywordExtractMode': 'strict' if strict_extract_mode else 'normal',
                  'sentiment': sentiment,
                  'showSourceText': show_source_text,
                  'maxRetrieve': max_keywords}
        return self._alchemy_html_request('GetRankedKeywords', html=html, text=text, url=url, params=params)

    def concepts(self, html=None, text=None, url=None, max_items=8, linked_data=True, show_source_text=False):
        params = {'maxRetrieve': max_items,
                  'linkedData': linked_data,
                  'showSourceText': show_source_text}
        return self._alchemy_html_request('GetRankedConcepts', html=html, text=text, url=url, params=params)

    def entities(self, html=None, text=None, url=None, disambiguate=True, linked_data=True, coreference=True,
                 quotations=False, sentiment=False, show_source_text=False, max_items=50):
        params = {'disambiguate': disambiguate,
                  'linkedData': linked_data,
                  'coreference': coreference,
                  'quotations': quotations,
                  'sentiment': sentiment,
                  'showSourceText': show_source_text,
                  'maxRetrieve': max_items}
        return self._alchemy_html_request('GetRankedNamedEntities', html=html, text=text, url=url, params=params)

    def relations(self, html=None, text=None, url=None, sentiment=False, keywords=False, entities=False,
                  require_entities=False, sentiment_excludes_entities=True, disambiguate=True, linked_data=True,
                  coreference=True, show_source_text=False, max_items=50):
        params = {'sentiment': sentiment,
                  'keywords': keywords,
                  'entities': entities,
                  'requireEntities': require_entities,
                  'sentimentExcludesEntities': sentiment_excludes_entities,
                  'disambiguate': disambiguate,
                  'linkedData': linked_data,
                  'coreference': coreference,
                  'showSourceText': show_source_text,
                  'maxRetrieve': max_items}
        return self._alchemy_html_request('GetRelations', html=html, text=text, url=url, params=params)

    def category(self, html=None, text=None, url=None, show_source_text=False):
        params = {'showSourceText': 1 if show_source_text else 0}
        return self._alchemy_html_request('GetCategory', html=html, text=text, url=url, params=params)

    def sentiment(self, html=None, text=None, url=None):
        return self._alchemy_html_request('GetTextSentiment', html=html, text=text, url=url)

    # Should provide a way to provide multiple targets
    def targeted_sentiment(self, target, html=None, text=None, url=None):
        params = {'target': target}
        return self._alchemy_html_request('GetTargetedSentiment', html=html, text=text, url=url, params=params)
