from __future__ import print_function
import json
import os
# from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1

# replace with your own classifier_id
classifier_id = '0a0c06c1-8e31-4655-9067-58fcac5134fc'
if os.getenv("natural_language_classifier_classifier_id") is not None:
    classifier_id = os.getenv("natural_language_classifier_classifier_id")

natural_language_classifier = NaturalLanguageClassifierV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

classifiers = natural_language_classifier.list_classifiers()
print(json.dumps(classifiers, indent=2))

# create a classifier
# with open('../resources/weather_data_train.csv', 'rb') as training_data:
#     print(json.dumps(natural_language_classifier.create(
# training_data=training_data, name='weather'), indent=2))

status = natural_language_classifier.get_classifier(classifier_id)
print(json.dumps(status, indent=2))

if status['status'] == 'Available':
    classes = natural_language_classifier.classify(classifier_id,
                                                   'How hot will it be '
                                                   'tomorrow?')
    print(json.dumps(classes, indent=2))

# delete = natural_language_classifier.remove('2374f9x68-nlc-2697')
# print(json.dumps(delete, indent=2))

# example of raising a ValueError
# print(json.dumps(
#     natural_language_classifier.create(training_data='', name='weather3'),
#     indent=2))
