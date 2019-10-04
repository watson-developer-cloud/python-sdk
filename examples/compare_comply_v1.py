# coding: utf-8
import json
import os
from ibm_watson import CompareComplyV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('your apikey')
compare_comply = CompareComplyV1(
    version='2018-03-23',
    authenticator=authenticator)
compare_comply.set_service_url('https://gateway.watsonplatform.net/compare-comply/api')

print('Convert to HTML')
contract = os.path.abspath('resources/contract_A.pdf')
with open(contract, 'rb') as file:
    result = compare_comply.convert_to_html(file).get_result()
    print(json.dumps(result, indent=2))

print('Classify elements')
contract = os.path.abspath('resources/contract_A.pdf')
with open(contract, 'rb') as file:
    result = compare_comply.classify_elements(file, file_content_type='application/pdf').get_result()
    print(json.dumps(result, indent=2))

print('Extract tables')
table = os.path.abspath('resources/contract_A.pdf')
with open(table, 'rb') as file:
    result = compare_comply.extract_tables(file).get_result()
    print(json.dumps(result, indent=2))
