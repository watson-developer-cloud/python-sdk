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
          .content)

# Example with JSON
with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
    config['conversion_target'] = DocumentConversionV1.ANSWER_UNITS
    print(json.dumps(document_conversion.convert_document(document=document, config=config), indent=2))

# Examples of index_document API
print("########## Example of a dry run of index_document with only a document ##########")
with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
    config = {
        'retrieve_and_rank': {
            'dry_run': 'true'
        }
    }
    print(json.dumps(document_conversion.index_document(config=config, document=document), indent=2))

print("########## Example of a dry run of index_document with only metadata ##########")
config = {
    'retrieve_and_rank': {
        'dry_run': 'true'
    }
}
metadata = {
    'metadata': [
        {'name': 'id', 'value': '12345'}
    ]
}
print(json.dumps(document_conversion.index_document(config=config, metadata=metadata), indent=2))

print("########## Example of a dry run of index_document with document and metadata ##########")
with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
    config = {
        'retrieve_and_rank': {
            'dry_run': 'true'
        }
    }
    metadata = {
        'metadata': [
            {'name': 'id', 'value': '12345'}
        ]
    }
    print(json.dumps(document_conversion.index_document(config=config, document=document, metadata=metadata), indent=2))

print("########## Example of a dry run of index_document with document, metadata, and additional config for conversion ##########")
with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
    config = {
        'convert_document': {
            'normalized_html': {
                'exclude_content': {"xpaths": ["//body/div"]}
            }
        },
        'retrieve_and_rank': {
            'dry_run': 'true'
        }
    }
    metadata = {
        'metadata': [
            {'name': 'id', 'value': '12345'}
        ]
    }
    print(json.dumps(document_conversion.index_document(config=config, document=document, metadata=metadata), indent=2))

# print("########## Example of index_document with document, metadata (A service instance id, SOLR cluster id, and "
#       "a SOLR collection name must be provided from the Retrieve and Rank service in order to index) ##########")
# with open(join(dirname(__file__), '../resources/example.html'), 'r') as document:
#     config = {
#         'retrieve_and_rank': {
#             'dry_run': 'false',
#             'service_instance_id': 'YOUR RETRIEVE AND RANK SERVICE INSTANCE ID',
#             'cluster_id': 'YOUR RETRIEVE AND RANK SERVICE SOLR CLUSTER ID',
#             'search_collection': 'YOUR RETRIEVE AND RANK SERVICE SOLR SEARCH COLLECTION NAME'
#         }
#     }
#     metadata = {
#         'metadata': [
#             {'name': 'id', 'value': '12345'}
#         ]
#     }
#     print(json.dumps(document_conversion.index_document(config=config, document=document, metadata=metadata), indent=2))
