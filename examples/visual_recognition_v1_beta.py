import json
from watson_developer_cloud import VisualRecognitionV1Beta as VisualRecognition


visual_recognition = VisualRecognition(username='YOUR SERVICE USERNAME',
                                       password='YOUR SERVICE PASSWORD')

print(json.dumps(visual_recognition.labels(), indent=2))

with open('../resources/test.jpg', 'rb') as image_file:
    print(json.dumps(visual_recognition.recognize(image_file,
                                                  labels_to_check={'label_groups': ['Indoors']}), indent=2))
