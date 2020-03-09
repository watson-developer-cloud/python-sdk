# coding: utf-8

# (C) Copyright IBM Corp. 2019, 2020.
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

from ibm_watson import get_sdk_headers
import unittest


class TestCommon(unittest.TestCase):

    def test_get_sdk_headers(self):
        headers = get_sdk_headers('my_service', 'v1', 'my_operation')
        self.assertIsNotNone(headers)
        self.assertIsNotNone(headers.get('X-IBMCloud-SDK-Analytics'))
        self.assertIsNotNone(headers.get('User-Agent'))
        self.assertIn('watson-apis-python-sdk', headers.get('User-Agent'))
        self.assertEqual(
            headers.get('X-IBMCloud-SDK-Analytics'),
            'service_name=my_service;service_version=v1;operation_id=my_operation'
        )
