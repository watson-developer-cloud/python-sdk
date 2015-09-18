import json
import watson_developer_cloud


natural_language_classifier = watson_developer_cloud.NaturalLanguageClassifierV1()

print(json.dumps(natural_language_classifier.list(), indent=2))

# with open('../resources/weather_data_train.csv', 'rb') as training_data:
#     print(json.dumps(natural_language_classifier.create(training_data=training_data, name='weather2'), indent=2))

status = natural_language_classifier.status('47C164-nlc-243')
print (json.dumps(status, indent=2))

classes = natural_language_classifier.classify('47C164-nlc-243', 'How hot will it be tomorrow?')
print(json.dumps(classes, indent=2))

# print(json.dumps(natural_language_classifier.remove('950DCB-nlc-641')))

