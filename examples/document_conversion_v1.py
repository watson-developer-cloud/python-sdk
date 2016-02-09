# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import DocumentConversionV1 as DocumentConversion


document_conversion = DocumentConversion(username='YOUR SERVICE USERNAME',
                                         password='YOUR SERVICE PASSWORD',
                                         version='2016-02-09')

with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
    config = {'conversion_target': DocumentConversion.ANSWER_UNITS}
    print(json.dumps(document_conversion.convert_document(document=document, config=config, media_type='text/html'),
                     indent=2))
