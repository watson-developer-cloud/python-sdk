import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV2Beta as VisualRecognition


visual_recognition = VisualRecognition(version='2015-12-02', username='YOUR SERVICE USERNAME',
                                       password='YOUR SERVICE PASSWORD')

# print(json.dumps(visual_recognition.list_classifiers(), indent=2))

with open(join(dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(image_file, classifier_ids=['Tiger', 'Cat']), indent=2))
