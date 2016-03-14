# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import DocumentConversionV1


document_conversion = DocumentConversionV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2016-02-09')

# Example of retrieving html or plain text
with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
    config = {'conversion_target': DocumentConversionV1.NORMALIZED_HTML}
    print(document_conversion.convert_document(document=document, config=config, media_type='text/html')
          .content.decode('utf-8'))

# Example with JSON
with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
    config['conversion_target'] = DocumentConversionV1.ANSWER_UNITS
    print(json.dumps(document_conversion.convert_document(document=document, config=config), indent=2))
