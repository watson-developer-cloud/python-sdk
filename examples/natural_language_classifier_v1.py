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
#     print(json.dumps(natural_language_classifier.create(training_data=training_data, name='weather2'), indent=2))

# replace 47C164-nlc-243 with your classifier id
status = natural_language_classifier.status('c7e487x21-nlc-1063')
print (json.dumps(status, indent=2))

classes = natural_language_classifier.classify('c7e487x21-nlc-1063', 'How hot will it be tomorrow?')
print(json.dumps(classes, indent=2))

# example of raising a WatsonException
# print(json.dumps(natural_language_classifier.create(training_data='', name='weather3'), indent=2))
