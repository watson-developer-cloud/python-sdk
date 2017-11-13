# coding=utf-8

from __future__ import print_function
import re
import traceback
import pytest
import json as json_import
import os
from os.path import join, dirname
from glob import glob

# tests to exclude
excludes = ['authorization_v1.py', 'alchemy_data_news_v1.py',
            'alchemy_language_v1.py', 'discovery_v1.ipynb', '__init__.py']

# examples path. /examples
examples_path = join(dirname(__file__), '../', 'examples', '*.py')

# environment variables
try:
    from dotenv import load_dotenv  # pylint: disable=C0413
except:
    print ('warning: dotenv module could not be imported')

try:
    dotenv_path = join(dirname(__file__), '../', '.env')
    load_dotenv(dotenv_path)
except:
    print ('warning: no .env file loaded')


@pytest.mark.skipif(os.getenv('VCAP_SERVICES') is None,
                    reason='requires VCAP_SERVICES')
def test_examples():
    vcap_services = json_import.loads(os.getenv('VCAP_SERVICES'))
    examples = glob(examples_path)
    for example in examples:
        name = example.split('/')[-1]

        # exclude some tests cases like authorization
        if name in excludes:
            continue

        # exclude tests if there are no credentials for that service
        service_name = name[:-6] if not name.startswith('visual_recognition')\
            else 'watson_vision_combined'

        if service_name not in vcap_services:
            print('%s does not have credentials in VCAP_SERVICES',
                  service_name)
            continue

        try:
            service_file = open(example).read()
            exec(re.sub(r'# coding[:=]\s*utf-8', '', service_file), globals())
        except Exception as e:
            assert False, 'example in file ' + name + ' failed with error: '\
                          + str(e) + '\n' + traceback.format_exc()
