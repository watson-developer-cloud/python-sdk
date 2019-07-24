# coding: utf-8
from __future__ import print_function
import json
import os
from ibm_watson import CompareComplyV1

# If service instance provides API key authentication
compare_comply = CompareComplyV1(
    version='2018-03-23',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/compare-comply/api',
    iam_apikey='YOUR APIKEY')

# compare_comply = CompareComplyV1(
#     version='2018-03-23',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     # url='https://gateway.watsonplatform.net/compare-comply/api',
#     username='YOUR SERVICE USERNAME',
#     password='YOUR SERVICE PASSWORD')

print('Convert to HTML')
contract = os.path.abspath('resources/contract_A.pdf')
with open(contract, 'rb') as file:
    result = compare_comply.convert_to_html(file).get_result()
    print(json.dumps(result, indent=2))

print('Classify elements')
contract = os.path.abspath('resources/contract_A.pdf')
with open(contract, 'rb') as file:
    result = compare_comply.classify_elements(file, 'application/pdf').get_result()
    print(json.dumps(result, indent=2))

print('Extract tables')
table = os.path.abspath('resources/contract_A.pdf')
with open(table, 'rb') as file:
    result = compare_comply.extract_tables(file).get_result()
    print(json.dumps(result, indent=2))
