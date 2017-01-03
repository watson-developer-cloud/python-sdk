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
The AlchemyData News service
(https://www.ibm.com/watson/developercloud/alchemy-data-news.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class AlchemyDataNewsV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'alchemy_api', url,
                                             **kwargs)

    def get_news_documents(self, start, end, max_results=10, query_fields=None,
                           return_fields=None, time_slice=None,
                           next_page=None, dedup=None, dedup_threshold=None,
                           rank=None):
        """
        :param start: The time (in UTC seconds) of the beginning date and time
        of the query. Valid values are UTC times and relative times:
        now (current time), now-{time value}, s (seconds), m (minutes),
        h (hours), d (days), M (months), and y (years)

        :param end: The time (in UTC seconds) of the end date and time of the
        query. Valid values are UTC times and relative times:
        now (current time), now-{time value}, s (seconds), m (minutes),
        h (hours), d (days), M (months), and y (years)

        :param max_results: The maximum number of results that are returned
        from your query. If None, all matching results are returned

        :param query_fields: There are nearly 400 variations of entity,
        taxonomy, sentiment analysis, concepts, and keywords. The full list
        of parameters is available in the Developer Cloud API documentation.
        Common fields include q.enriched.url.enrichedTitle.relations.relation,
        q.enriched.url.enrichedTitle.entities.entity,
        q.enriched.url.enrichedTitle.taxonomy.taxonomy,
        q.enriched.url.enrichedTitle.docSentiment.type,
        q.enriched.url.concepts.concept.text,
        q.enriched.url.enrichedTitle.keywords.keyword.text

        :param return fields: A comma-separated list of document fields to
        return for each matching document. Any available document fields can
        be retrieved. To return multiple fields, use a comma separated list.
        Common fields to return are enriched.url.url (URL), enriched.url.title
        (title), enriched.url.text(full article text), and enriched.url.author
        (author name). If you do not specify fields to be returned or a
        timeSlice, the AlchemyData News API only returns the total number of
        matching results within the start and end date range

        :param time_slice: The interval to divide the returned data. The
        default is that the query engine returns the total count over the time
        duration specified with start and end. If you specify a value, it
        returns a time series representing the count (max 1000) in each slice
        of time: now (current time), s (seconds), m (minutes), h (hours),
        d (days), M (months), and y (years)

        :param next_page: If a query is too broad or spans a long time period,
        the number of results can be very large and more results may be
        available than those which were returned. If there are more matching
        results available, a next parameter is returned in the response. To
        get the next page of results, execute the query again and append the
        next parameter to your query

        :param dedup: Many news articles are published by a single source,
        such as Associated Press, and then syndicated widely across the web.
        dedup removes duplicate results based on a comparison of their cleaned
        titles: False (Default) turns off dudup, True turns on dedup

        :param dedup_threshold: Defines how strictly the algorithm defines a
        duplicate. Valid values are between 0 and 1. The default value is 0.4.
        A value of 0.0 allows only titles that exactly match those of other
        articles to be tagged as duplicate. 0.4 allows articles that are very
        similar but not necessarily identical to be tagged as duplicates. A
        value of 1.0 allows articles to be aggressively labeled as duplicates,
        sometimes even when the titles are very dissimilar

        :param rank: The News API monitors and ranks 60,000 top-level domains,
        each with a varying range of page views. rank allows you to specify to
        only return articles from well-known, high-traffic publishers. If the
        rank parameter is not specified, articles of all ranks are returned:
        high, medium, low, or unknown

        :return: result elements depend on the parameters that you passed to
        the query. If return fields are requested, the result element contains
        a docs element that contains the matching documents, a next element
        that contains an identifier for the next matching result in the
        AlchemyData News data set, and a status element that provides status
        information about retrieving the requested number of results. If no
        return fields are requested in your query, the result element contains
        a count of matching news items and the status of querying the
        AlchemyData News data set.
        """

        if isinstance(return_fields, list):
            return_fields = ','.join(return_fields)
        params = {'start': start,
                  'end': end,
                  'maxResults': max_results,
                  'return': return_fields,
                  'timeSlice': time_slice,
                  'next': next_page,
                  'dedup': dedup,
                  'dedupThreshold': dedup_threshold,
                  'rank': rank}
        if isinstance(query_fields, dict):
            for key in query_fields:
                params[key if key.startswith('q.') else 'q.' + key] = \
                    query_fields[key]
        return self._alchemy_html_request(method_url='/data/GetNews',
                                          method='GET', params=params)
