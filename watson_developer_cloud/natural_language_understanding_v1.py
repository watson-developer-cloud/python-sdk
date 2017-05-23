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

from watson_developer_cloud.watson_developer_cloud_service import \
    WatsonDeveloperCloudService


class NaturalLanguageUnderstandingV1(WatsonDeveloperCloudService):
    """
    All methods taking features use the feature classes
    from watson_developer_cloud/natural_language_understanding/features/v1

    """
    base_url = 'https://gateway.watsonplatform.net'
    default_url = '{0}/natural-language-understanding/api'.format(base_url)
    latest_version = '2017-02-27'

    def __init__(self,
                 version,
                 url=default_url,
                 username=None,
                 password=None,
                 use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'natural-language-understanding', url,
            username, password, use_vcap_services)
        self.version = version

    def analyze(self, features, text=None, url=None, html=None,
                clean=True, xpath=None, fallback_to_raw=True,
                return_analyzed_text=False, language=None):
        """
        This is the method to call and analyze text with the supplied features
        :param features: The list of features
        :param text: Text to analyze (pick one of text, url, or html)
        :param url: url to analyze (pick one of text, url, or html)
        :param html: html to analyze (pick one of text, url, or html)
        :param clean: should the service clean the text?
        :param xpath: xpath to use for html or url
        :param fallback_to_raw:
        :param return_analyzed_text: should the analyzed
               text be returned (defaults to false)
        :param language: what language to use
        :return: dict of analyzed text
        """
        body = {
            'clean': clean,
            'fallback_to_raw': fallback_to_raw,
            'return_analyzed_text': return_analyzed_text,
            'xpath': xpath,
            'language': language,
            'text': text,
            'url': url,
            'html': html
        }

        feature_dict = {}
        for feature in features:
            feature_dict[feature.name()] = feature.toDict()
        body['features'] = feature_dict

        if text is None and html is None and url is None:
            msg = "html, text, or url must have content"
            raise ValueError(msg)

        if len(features) < 1:
            raise ValueError("Must supply at least one feature")

        return self.request(method='POST', url='/v1/analyze',
                            params={"version": self.version},
                            headers={'content-type': 'application/json'},
                            json=body,
                            accept_json=True)

    def list_models(self):
        """
        Lists the custom models available for your service instance
        :return: dict of available custom models
        """
        return self.request(method='GET', url='/v1/models',
                            params={"version": self.version},
                            accept_json=True)

    def delete_model(self, model_id):
        """
        Deletes a custom model
        :param model_id: The ID of the model to delete
        :return: dict with status of model deletion
        """

        return self.request(method='DELETE',
                            url='/v1/models/{0}'.format(model_id),
                            params={"version": self.version},
                            accept_json=True)
