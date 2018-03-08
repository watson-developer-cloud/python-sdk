# coding: utf-8
from __future__ import print_function
from dotenv import load_dotenv, find_dotenv

# load the .env file containing your environment variables for the required
try:
    load_dotenv(find_dotenv())
except:
    print('warning: no .env file loaded')
