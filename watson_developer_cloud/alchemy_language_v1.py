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
"""
The AlchemyAPI Language service
(https://www.ibm.com/watson/developercloud/alchemy-language.html)
"""

from .watson_service import WatsonService


class AlchemyLanguageV1(WatsonService):
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonService.__init__(self, 'alchemy_api', url, **kwargs)

    def author(self, html=None, url=None, language=None):
        params = {'language': language}
        return self._alchemy_html_request('GetAuthor', html=html, url=url,
                                          params=params)

    def authors(self, html=None, url=None, language=None):
        params = {'language': language}
        return self._alchemy_html_request('GetAuthors', html=html, url=url,
                                          params=params)

    def keywords(self, html=None, text=None, url=None,
                 strict_extract_mode=False, sentiment=False, emotion=False,
                 show_source_text=False, max_items=None, language=None,
                 max_keywords=50):
        """
        :param html: HTML input
        :param text: Text input
        :param url: URL input
        :param max_items: The number of results to return (default 50)
        :param max_keywords: deprecated, use max_items instead
        :return: A JSON object with extracted keywords from the source document
        """
        if not max_items:
            max_items = max_keywords
        params = {
            'keywordExtractMode':
                'strict' if strict_extract_mode else 'normal',
            'sentiment': sentiment,
            'emotion': emotion,
            'showSourceText': show_source_text,
            'maxRetrieve': max_items,
            'language': language}
        return self._alchemy_html_request('GetRankedKeywords', html=html,
                                          text=text, url=url, params=params)

    def concepts(self, html=None, text=None, url=None, max_items=8,
                 linked_data=True, show_source_text=False,
                 language=None, knowledge_graph=False):
        params = {'maxRetrieve': max_items,
                  'linkedData': linked_data,
                  'showSourceText': show_source_text,
                  'language': language,
                  'knowledgeGreaph': knowledge_graph}
        return self._alchemy_html_request('GetRankedConcepts', html=html,
                                          text=text, url=url, params=params)

    def dates(self, html=None, text=None, url=None, anchor_date=None,
              show_source_text=False, language=None):
        params = {'anchorDate': anchor_date,
                  'showSourceText': show_source_text,
                  'language': language}
        return self._alchemy_html_request('ExtractDates', html=html, text=text,
                                          url=url, params=params)

    def entities(self, html=None, text=None, url=None, disambiguate=True,
                 linked_data=True, coreference=True,
                 quotations=False, sentiment=False, emotion=False,
                 show_source_text=False, max_items=50, language=None,
                 model=None):
        params = {'disambiguate': disambiguate,
                  'linkedData': linked_data,
                  'coreference': coreference,
                  'quotations': quotations,
                  'sentiment': sentiment,
                  'emotion': emotion,
                  'showSourceText': show_source_text,
                  'maxRetrieve': max_items,
                  'language': language,
                  'model': model}
        return self._alchemy_html_request('GetRankedNamedEntities', html=html,
                                          text=text, url=url, params=params)

    def emotion(self, html=None, text=None, url=None, show_source_text=False,
                source_text_type=None,
                constraint_query=None, xpath_query=None, language=None):
        params = {'showSourceText': show_source_text,
                  'sourceText': source_text_type,
                  'cquery': constraint_query,
                  'xpath': xpath_query,
                  'language': language}
        return self._alchemy_html_request('GetEmotion', html=html, text=text,
                                          url=url, params=params)

    def targeted_emotion(self, targets, html=None, text=None, url=None,
                         language=None, constraint_query=None,
                         xpath_query=None, show_source_text=False,
                         source_text_type=None):
        if isinstance(targets, list):
            targets = '|'.join(targets)

        params = {'targets': targets,
                  'language': language,
                  'cquery': constraint_query,
                  'xpath': xpath_query,
                  'showSourceText': show_source_text,
                  'sourceText': source_text_type}
        return self._alchemy_html_request('GetTargetedEmotion', html=html,
                                          text=text, url=url, params=params)

    def typed_relations(self, html=None, text=None, url=None, model=None,
                        show_source_text=False):
        params = {'model': model,
                  'showSourceText': show_source_text}
        return self._alchemy_html_request('GetTypedRelations', html=html,
                                          text=text, url=url, params=params)

    def relations(self, html=None, text=None, url=None, sentiment=False,
                  keywords=False, entities=False,
                  require_entities=False, sentiment_excludes_entities=True,
                  disambiguate=True, linked_data=True,
                  coreference=True, show_source_text=False, max_items=50,
                  language=None):
        params = {'sentiment': sentiment,
                  'keywords': keywords,
                  'entities': entities,
                  'requireEntities': require_entities,
                  'sentimentExcludesEntities': sentiment_excludes_entities,
                  'disambiguate': disambiguate,
                  'linkedData': linked_data,
                  'coreference': coreference,
                  'showSourceText': show_source_text,
                  'maxRetrieve': max_items,
                  'language': language}
        return self._alchemy_html_request('GetRelations', html=html, text=text,
                                          url=url, params=params)

    def language(self, html=None, text=None, url=None):
        return self._alchemy_html_request('GetLanguage', html=html, text=text,
                                          url=url)

    def text(self, html=None, url=None, use_metadata=True,
             extract_links=False):
        params = {'useMetadata': use_metadata,
                  'extractLinks': extract_links}
        return self._alchemy_html_request('GetText', html=html, url=url,
                                          params=params)

    def raw_text(self, html=None, url=None):
        return self._alchemy_html_request('GetRawText', html=html, url=url)

    def category(self, html=None, text=None, url=None, show_source_text=False,
                 language=None):
        params = {'showSourceText': show_source_text, 'language': language}
        return self._alchemy_html_request('GetCategory', html=html, text=text,
                                          url=url, params=params)

    def title(self, html=None, url=None, use_metadata=True, language=None):
        params = {'useMetadata': use_metadata, 'language': language}
        return self._alchemy_html_request('GetTitle', html=html, url=url,
                                          params=params)

    def feeds(self, html=None, url=None):
        return self._alchemy_html_request('GetFeedLinks', html=html, url=url)

    def microformats(self, html=None, url=None):
        return self._alchemy_html_request('GetMicroformatData', html=html,
                                          url=url)

    def publication_date(self, html=None, url=None):
        return self._alchemy_html_request('GetPubDate', html=html, url=url)

    def taxonomy(self, html=None, text=None, url=None, show_source_text=False,
                 source_text_type=None,
                 constraint_query=None, xpath_query=None, base_url=None,
                 language=None):
        """
        source_text_type ->
            where to obtain the text that will be processed by this API call.
            AlchemyAPI supports multiple modes of text extraction:
                web page cleaning (removes ads, navigation links, etc.),
                raw text extraction
                (processes all web page text, including ads / nav links),
                visual constraint queries, and XPath queries.
            Possible values:
                cleaned_or_raw  : cleaning enabled, fallback to raw when
                cleaning produces no text (default)
                cleaned         : operate on 'cleaned' web page text (web
                page cleaning enabled)
                raw             : operate on raw web page text (web page
                cleaning disabled)
                cquery          : operate on the results of a visual
                constraints query
                                  Note: The 'constraint_query'  argument must
                                  also be set to a valid visual constraints
                                  query.
                xpath           : operate on the results of an XPath query
                                  Note: The 'xpath' http argument must also
                                  be set to a valid XPath query.
        constraint_query ->
            a visual constraints query to apply to the web page.
        xpath ->
            an XPath query to apply to the web page.
        base_url ->
            rel-tag output base http url (must be uri-argument encoded)
        """
        params = {'showSourceText': show_source_text,
                  'sourceText': source_text_type,
                  'cquery': constraint_query,
                  'xpath': xpath_query,
                  'baseUrl': base_url,
                  'language': language}
        return self._alchemy_html_request('GetRankedTaxonomy', html=html,
                                          text=text, url=url, params=params)

    # Some of these options don't appear in the API documentation but are
    # supported by the previous AlchemyAPI SDK
    def combined(self, html=None, text=None, url=None, extract=None,
                 disambiguate=True, linked_data=True,
                 coreference=True, quotations=False, sentiment=False,
                 show_source_text=False, max_items=50,
                 base_url=None, language=None):
        """
        Combined call for page-image, entity, keyword, title, author,
        taxonomy, concept, doc-emotion.
        INPUT:
        extract ->
            List or comma separated string
            Possible values: page-image, entity, keyword, title, author,
            taxonomy,  concept
            default        : entity, keyword, taxonomy,  concept
        disambiguate ->
            disambiguate detected entities
            Possible values:
                True : enabled (default)
                False : disabled
        linked_data ->
            include Linked Data content links with disambiguated entities
            Possible values :
                True : enabled (default)
                False : disabled
        coreference ->
            resolve he/she/etc coreferences into detected entities
            Possible values:
                True : enabled (default)
                False : disabled
        quotations ->
            enable quotations extraction
            Possible values:
                True : enabled
                False : disabled (default)
        sentiment ->
            enable entity-level sentiment analysis
            Possible values:
                True : enabled
                False : disabled (default)
        show_source_text ->
            include the original 'source text' the entities were extracted
            from within the API response
            Possible values:
                True : enabled
                False : disabled (default)
        max_items ->
            maximum number of named entities to extract
            default : 50
        base_url ->
            rel-tag output base http url
        OUTPUT:
        The response, already converted from JSON to a Python object.
        """
        if isinstance(extract, list):
            extract = ','.join(extract)

        params = {'extract': extract,
                  'disambiguate': disambiguate,
                  'linkedData': linked_data,
                  'coreference': coreference,
                  'quotations': quotations,
                  'sentiment': sentiment,
                  'showSourceText': show_source_text,
                  'maxRetrieve': max_items,
                  'baseUrl': base_url,
                  'language': language}
        return self._alchemy_html_request('GetCombinedData', html=html,
                                          text=text, url=url, params=params)

    def sentiment(self, html=None, text=None, url=None, language=None):
        params = {'language': language}
        return self._alchemy_html_request('GetTextSentiment', html=html,
                                          text=text, url=url, params=params)

    def targeted_sentiment(self, targets, html=None, text=None, url=None,
                           language=None, constraint_query=None,
                           xpath_query=None, show_source_text=False,
                           source_text_type=None):
        if isinstance(targets, list):
            targets = '|'.join(targets)

        params = {'targets': targets,
                  'language': language,
                  'cquery': constraint_query,
                  'xpath': xpath_query,
                  'showSourceText': show_source_text,
                  'sourceText': source_text_type}
        return self._alchemy_html_request('GetTargetedSentiment', html=html,
                                          text=text, url=url, params=params)
