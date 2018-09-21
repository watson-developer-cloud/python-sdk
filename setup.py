#!/usr/bin/env python
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

from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import os
import sys

__version__ = '2.1.0'

if sys.argv[-1] == 'publish':
    # test server
    os.system('python setup.py register -r pypitest')
    os.system('python setup.py sdist upload -r pypitest')

    # production server
    os.system('python setup.py register -r pypi')
    os.system('python setup.py sdist upload -r pypi')
    sys.exit()

# Convert README.md to README.rst for pypi
try:
    from pypandoc import convert_file

    def read_md(f):
        return convert_file(f, 'rst')

    # read_md = lambda f: convert(f, 'rst')
except:
    print('warning: pypandoc module not found, '
          'could not convert Markdown to RST')

    def read_md(f):
        return open(f, 'rb').read().decode(encoding='utf-8')
    # read_md = lambda f: open(f, 'rb').read().decode(encoding='utf-8')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'test']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(name='watson-developer-cloud',
      version=__version__,
      description='Client library to use the IBM Watson Services',
      license='Apache 2.0',
      install_requires=['requests>=2.0, <3.0', 'python_dateutil>=2.5.3', 'websocket-client==0.47.0'],
      tests_require=['responses', 'pytest', 'python_dotenv', 'pytest-rerunfailures', 'tox'],
      cmdclass={'test': PyTest},
      author='Jeffrey Stylos',
      author_email='jsstylos@us.ibm.com',
      long_description=read_md('README.md'),
      url='https://github.com/watson-developer-cloud/python-sdk',
      packages=['watson_developer_cloud'],
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
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Libraries :: Application '
          'Frameworks',
      ],
      zip_safe=True
     )
