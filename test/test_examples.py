# coding=utf-8

import os

import pytest
from os.path import join, dirname
from glob import glob

# tests to exclude
excludes = ['authorization_v1.py', 'alchemy_data_news_v1.py', 'alchemy_language_v1.py']

# examples path. /examples
examples_path = join(dirname(__file__), '../', 'examples', '*.py')

# environment variables
try:
    from dotenv import load_dotenv
except:
    print('warning: dotenv module could not be imported')

try:
    dotenv_path = join(dirname(__file__), '../', '.env')
    load_dotenv(dotenv_path)
except:
    print('warning: no .env file loaded')


@pytest.mark.skipif(os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
def test_examples():
    examples = glob(examples_path)
    for example in examples:
        name = example.split('/')[-1]
        # exclude some tests cases like authorization
        if name in excludes:
            continue

        try:
            exec(open(example).read(), globals())
        except Exception as e:
            assert False, 'example in file ' + name + ' failed with error: ' + str(e)

