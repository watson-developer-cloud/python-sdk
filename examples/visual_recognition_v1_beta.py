import json
import watson_developer_cloud


visual_recognition = watson_developer_cloud.VisualRecognitionV1Beta()

print(json.dumps(visual_recognition.labels(), indent=2))

with open('../resources/test.jpg', 'rb') as image_file:
    print(json.dumps(visual_recognition.recognize(image_file, labels_to_check={'label_groups': ['Indoors']}), indent=2))
