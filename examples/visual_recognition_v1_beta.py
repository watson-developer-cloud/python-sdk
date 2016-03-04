import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV1Beta


visual_recognition = VisualRecognitionV1Beta(username='YOUR SERVICE USERNAME',
                                             password='YOUR SERVICE PASSWORD')

print(json.dumps(visual_recognition.labels(), indent=2))

with open(join(dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.recognize(
        image_file,
        labels_to_check={'label_groups': ['Indoors']}), indent=2))
