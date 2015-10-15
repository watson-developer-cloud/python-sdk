# coding=utf-8
import json
from watson_developer_cloud import DocumentConversionV1Experimental as DocumentConversion


document_conversion = DocumentConversion(username='YOUR SERVICE USERNAME',
                                         password='YOUR SERVICE PASSWORD')

# print(json.dumps(document_conversion.get_jobs(), indent=2))

with open('../resources/sample-docx.docx', 'rb') as document:
    print(json.dumps(document_conversion.convert_document(document=document), indent=2))
