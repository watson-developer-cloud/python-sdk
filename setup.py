#!/usr/bin/env python
# (C) Copyright IBM Corp. 2015, 2020.
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
from os import path

__version__ = '5.2.3'

# read contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as file:
    readme_file = file.read()

setup(name='ibm-watson',
      version=__version__,
      description='Client library to use the IBM Watson Services',
      packages=['ibm_watson'],
      install_requires=['requests>=2.0, <3.0', 'python_dateutil>=2.5.3', 'websocket-client==1.1.0', 'ibm_cloud_sdk_core>=3.3.6, == 3.*'],
      tests_require=['responses', 'pytest', 'python_dotenv', 'pytest-rerunfailures'],
      license='Apache 2.0',
      author='IBM Watson',
      author_email='watdevex@us.ibm.com',
      long_description=readme_file,
      long_description_content_type='text/markdown',
      url='https://github.com/watson-developer-cloud/python-sdk',
      include_package_data=True,
      keywords='language, vision, question and answer' +
      ' tone_analyzer, natural language classifier,' +
      ' text to speech, language translation, ' +
      'language identification, concept expansion, machine translation, ' +
      'personality insights, message resonance, watson developer cloud, ' +
      ' wdc, watson, ibm, dialog, user modeling,' +
      'tone analyzer, speech to text, visual recognition',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Libraries :: Application '
          'Frameworks',
      ],
      zip_safe=True
     )
