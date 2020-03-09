# coding=utf-8

import re
import traceback
import pytest
import json as json_import
import os
from os.path import join, dirname
from glob import glob

# tests to include
includes = [
    'assistant_v1.py', 'natural_language_understanding_v1.py',
    'personality_insights_v3.py', 'tone_analyzer_v3.py'
]

# examples path. /examples
examples_path = join(dirname(__file__), '../../', 'examples', '*.py')


@pytest.mark.skipif(os.getenv('VCAP_SERVICES') is None,
                    reason='requires VCAP_SERVICES')
def test_examples():
    vcap_services = json_import.loads(os.getenv('VCAP_SERVICES'))
    examples = glob(examples_path)
    for example in examples:
        name = example.split('/')[-1]

        if name not in includes:
            continue

        service_name = name[:-6]

        if service_name not in vcap_services:
            print('%s does not have credentials in VCAP_SERVICES', service_name)
            continue

        try:
            service_file = open(example).read()
            exec(re.sub(r'# coding[:=]\s*utf-8', '', service_file), globals())
        except Exception as e:
            assert False, 'example in file ' + name + ' failed with error: '\
                          + str(e) + '\n' + traceback.format_exc()
