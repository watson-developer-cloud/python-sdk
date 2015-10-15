import json
from os.path import join, dirname
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier


natural_language_classifier = NaturalLanguageClassifier(username='YOUR SERVICE USERNAME',
                                                        password='YOUR SERVICE PASSWORD')

print(json.dumps(natural_language_classifier.list(), indent=2))

# create a classifier
# with open('../resources/weather_data_train.csv', 'rb') as training_data:
#     print(json.dumps(natural_language_classifier.create(training_data=training_data, name='weather2'), indent=2))

# replace 47C164-nlc-243 with your classifier id
status = natural_language_classifier.status('47C164-nlc-243')
print (json.dumps(status, indent=2))

classes = natural_language_classifier.classify('47C164-nlc-243', 'How hot will it be tomorrow?')
print(json.dumps(classes, indent=2))
