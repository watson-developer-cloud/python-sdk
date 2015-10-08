# coding=utf-8
import json
import watson_developer_cloud


document_conversion = watson_developer_cloud.DocumentConversionV1Experimental()

# print(json.dumps(document_conversion.get_jobs(), indent=2))

with open('../resources/sample-docx.docx', 'rb') as document:
    print(json.dumps(document_conversion.convert_document(document=document), indent=2))
