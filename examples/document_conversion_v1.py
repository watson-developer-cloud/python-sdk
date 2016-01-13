# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import DocumentConversionV1 as DocumentConversion


document_conversion = DocumentConversion(username='YOUR SERVICE USERNAME',
                                         password='YOUR SERVICE PASSWORD')

with open(join(dirname(__file__), '../resources/sample-docx.docx'), 'rb') as document:
    config = {'conversion_target': DocumentConversion.ANSWER_UNITS}
    print(json.dumps(document_conversion.convert_document(document=document, config=config), indent=2))
