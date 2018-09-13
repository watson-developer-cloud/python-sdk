from __future__ import print_function
import json
import os

# from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1

# # If service instance provides API key authentication
# service = NaturalLanguageClassifierV1(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/natural-language-classifier/api',
#     iam_apikey='your_apikey')

service = NaturalLanguageClassifierV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/natural-language-classifier/api',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

classifiers = service.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))

# create a classifier
with open(
    os.path.join(
        os.path.dirname(__file__), '../resources/weather_data_train.csv'),
    'rb') as training_data:
    metadata = json.dumps({'name': 'my-classifier', 'language': 'en'})
    classifier = service.create_classifier(
        metadata=metadata, training_data=training_data).get_result()
    classifier_id = classifier['classifier_id']
    print(json.dumps(classifier, indent=2))

status = service.get_classifier(classifier_id).get_result()
print(json.dumps(status, indent=2))

if status['status'] == 'Available':
    classes = service.classify(classifier_id, 'How hot will it be '
                               'tomorrow?').get_result()
    print(json.dumps(classes, indent=2))

if status['status'] == 'Available':
    collection = [
        '{"text":"How hot will it be today?"}', '{"text":"Is it hot outside?"}'
    ]
    classes = service.classify_collection(classifier_id,
                                          collection).get_result()
    print(json.dumps(classes, indent=2))

delete = service.delete_classifier(classifier_id).get_result()
print(json.dumps(delete, indent=2))

# example of raising a ValueError
# print(json.dumps(
#     service.create_classifier(training_data='', name='weather3', metadata='metadata'),
#     indent=2))
