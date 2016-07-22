# coding=utf-8

import os
import watson_developer_cloud
import pytest
import sys
from os import getcwd
from subprocess import Popen, PIPE
from os.path import join, dirname
from glob import glob

# tests to exclude
excludes = []

itests_path = join(dirname(__file__), '../', 'testintegration', '*.py')

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
def test_integration():
    itests = glob(itests_path)
    for itest in itests:
        head, tail = os.path.split(itest)
        # exclude some tests cases like authorization
        if tail in excludes:
            continue

        try:
            exec(open(itest).read(), globals())
        except Exception as e:
            assert False, 'itest in file ' + tail + ' failed with error: ' + str(e)

