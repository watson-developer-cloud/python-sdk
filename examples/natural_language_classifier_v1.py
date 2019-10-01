import json
import os

from ibm_watson import NaturalLanguageClassifierV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('your_api_key')
service = NaturalLanguageClassifierV1(authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/natural-language-classifier/api')

classifiers = service.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))

# create a classifier
with open(
        os.path.join(
            os.path.dirname(__file__), '../resources/weather_data_train.csv'),
        'rb') as training_data:
    metadata = json.dumps({'name': 'my-classifier', 'language': 'en'})
    classifier = service.create_classifier(
        training_metadata=metadata, training_data=training_data).get_result()
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
#     service.create_classifier(training_data='', training_metadata='metadata'),
#     indent=2))
