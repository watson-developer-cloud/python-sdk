import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV2Beta


visual_recognition = VisualRecognitionV2Beta(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2015-12-02')

# with open(join(dirname(__file__), '../resources/cars.zip'), 'rb') as cars, \
#         open(join(dirname(__file__), '../resources/trucks.zip'), 'rb') as trucks:
#     print(json.dumps(visual_recognition.create_classifier('Cars vs Trucks', positive_examples=cars,
#                                                           negative_examples=trucks), indent=2))

# with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as image_file:
#     print(json.dumps(visual_recognition.classify(image_file), indent=2))

# print(json.dumps(visual_recognition.get_classifier(classifier_id='Tiger'), indent=2))

# The service currently has a bug where even successful deletions return a 404
# print(json.dumps(visual_recognition.delete_classifier(classifier_id='YOUR CLASSIFIER ID'), indent=2))

print(json.dumps(visual_recognition.list_classifiers(), indent=2))

with open(join(dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(image_file, classifier_ids=['Tiger', 'Cat']), indent=2))
