# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import DocumentConversionV1Experimental


document_conversion = DocumentConversionV1Experimental(username='YOUR SERVICE USERNAME',
                                                       password='YOUR SERVICE PASSWORD')

# print(json.dumps(document_conversion.get_jobs(), indent=2))

with open(join(dirname(__file__), '../resources/sample-docx.docx'), 'rb') as document:
    print(json.dumps(document_conversion.convert_document(
        document=document,
        conversion_target=DocumentConversionV1Experimental.ANSWER_UNITS), indent=2))
