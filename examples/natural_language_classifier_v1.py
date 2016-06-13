import json
# from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1


natural_language_classifier = NaturalLanguageClassifierV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

classifiers = natural_language_classifier.list()
print(json.dumps(classifiers, indent=2))

# create a classifier
# with open('../resources/weather_data_train.csv', 'rb') as training_data:
#     print(json.dumps(natural_language_classifier.create(training_data=training_data, name='weather'), indent=2))

# replace 2374f9x68-nlc-2697 with your classifier id
status = natural_language_classifier.status('2374f9x68-nlc-2697')
print(json.dumps(status, indent=2))

if status['status'] == 'Available':
    classes = natural_language_classifier.classify('2374f9x68-nlc-2697', 'How hot will it be tomorrow?')
    print(json.dumps(classes, indent=2))

# delete = natural_language_classifier.remove('2374f9x68-nlc-2697')
# print(json.dumps(delete, indent=2))

# example of raising a WatsonException
# print(json.dumps(natural_language_classifier.create(training_data='', name='weather3'), indent=2))
