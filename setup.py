#!/usr/bin/env python
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

setup(name='watson-developer-cloud',
      version=watson_developer_cloud.__version__,
      description='Client library to the IBM Watson Services',
      license='Apache 2.0',
      install_requires=['requests'],
      tests_require=['responses', 'pytest'],
      author='Jeffrey Stylos',
      author_email='jsstylos@us.ibm.com',
      long_description=open('README.md').read(),
      url='https://github.com/watson-developer-cloud/python-sdk',
      packages=['watson_developer_cloud'],
      keywords='alchemy datanews, language, vision, question and answer' +
      ' tone_analyzer, natural language classifier, retrieve and rank,' +
      ' tradeoff analytics, concept insights, text to speech,' +
      ' language translation, language identification,' +
      ' concept expansion, machine translation, personality insights,' +
      ' message resonance, watson developer cloud, wdc, watson, ibm,' +
      ' dialog, user modeling, alchemyapi, alchemy, tone analyzer,' +
      'speech to text, visual recognition, relationship extraction',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 2.8',
          'Programming Language :: Python :: 2.9',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      zip_safe=True
      )
