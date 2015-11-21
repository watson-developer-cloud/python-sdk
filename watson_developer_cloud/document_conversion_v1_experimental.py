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
from .watson_developer_cloud_service import WatsonInvalidArgument
import os
import json


class DocumentConversionV1Experimental(WatsonDeveloperCloudService):
    DEFAULT_URL = 'https://gateway.watsonplatform.net/document-conversion-experimental/api'
    ANSWER_UNITS = 'ANSWER_UNITS'
    NORMALIZED_HTML = 'NORMALIZED_HTML'
    NORMALIZED_TEXT = 'NORMALIZED_TEXT'

    def __init__(self, url=DEFAULT_URL, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'document_conversion', url, **kwargs)

    @staticmethod
    def _media_type_from_filename(filename):
        extension = os.path.splitext(filename.lower())[1].split('.')[-1]
        extension_map = {'doc': 'application/msword',
                         'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                         'htm': 'text/html',
                         'html': 'text/html',
                         'pdf': 'application/pdf',
                         'txt': 'text/plain',
                         'xml': 'text/xml'}
        if extension in extension_map:
            return extension_map[extension]
        return None

    def convert_document(self, document, conversion_target, media_type=None):
        filename = os.path.basename(document.name)
        if not media_type:
            media_type = self._media_type_from_filename(filename)
            if not media_type:
                raise WatsonInvalidArgument('Media type could not be read from filename: ' + filename)
        config = {'conversion_target': conversion_target}
        files = [('file', (filename, document, media_type)),
                 ('config', ('config', json.dumps(config), 'application/json'))]
        return self.request(method='POST', url='/v1/convert_document', files=files, accept_json=True)
