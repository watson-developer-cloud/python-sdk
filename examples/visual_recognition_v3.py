from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'

# If service instance provides IAM API key authentication
visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_apikey='iam_apikey')

# visual_recognition = VisualRecognitionV3('2016-05-20',
#                                          ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#                                          #  url='https://gateway.watsonplatform.net/visual-recognition/api',
#                                          api_key='YOUR API KEY')

# with open(join(dirname(__file__), '../resources/cars.zip'), 'rb') as cars, \
#        open(join(dirname(__file__), '../resources/trucks.zip'), 'rb') as
# trucks:
#     print(json.dumps(visual_recognition.create_classifier('Cars vs Trucks',
#  cars_positive_examples=cars,

# negative_examples=trucks).get_result(), indent=2))

car_path = join(dirname(__file__), '../resources/cars.zip')
try:
    with open(car_path, 'rb') as images_file:
        car_results = visual_recognition.classify(
            images_file=images_file,
            threshold='0.1',
            classifier_ids=['default']).get_result()
        print(json.dumps(car_results, indent=2))
except WatsonApiException as ex:
    print(ex.httpResponse.json())

# print(json.dumps(visual_recognition.get_classifier('YOUR CLASSIFIER ID').get_result(),
# indent=2))

# with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as
# image_file:
#     print(json.dumps(visual_recognition.update_classifier(
# 'CarsvsTrucks_1479118188',
#
# cars_positive_examples=image_file).get_result(), indent=2))

faces_result = visual_recognition.detect_faces(url=test_url).get_result()
print(json.dumps(faces_result, indent=2))

# print(json.dumps(visual_recognition.delete_classifier(classifier_id='YOUR
# CLASSIFIER ID').get_result(), indent=2))

print(json.dumps(visual_recognition.list_classifiers().get_result(), indent=2))

face_path = join(dirname(__file__), '../resources/face.jpg')
with open(face_path, 'rb') as image_file:
    face_result = visual_recognition.detect_faces(images_file=image_file).get_result()
    print(json.dumps(face_result, indent=2))

#Core ml model example
# model_name = '{0}.mlmodel'.format(classifier_id)
# core_ml_model = visual_recognition.get_core_ml_model(classifier_id).get_result()
# with open('/tmp/{0}'.format(model_name), 'wb') as fp:
#     fp.write(core_ml_model.content)
