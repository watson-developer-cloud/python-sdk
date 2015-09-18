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

from setuptools import setup

import watson_developer_cloud

setup(name="watson-developer-cloud",
      version=watson_developer_cloud.__version__,
      description="IBM Watson Developer Cloud",
      license="Apache 2.0",
      install_requires=["requests >= 0.13.2"],
      tests_require=['responses', 'nose2'],
      test_suite='nose2.collector.collector',
      author="Jeffrey Stylos",
      author_email="jsstylos@us.ibm.com",
      url="https://github.com/jsstylos/python-wrapper",
      packages=['watson_developer_cloud'],
      keywords="Watson",
      zip_safe=True)
