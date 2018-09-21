from __future__ import print_function
import json
from os.path import abspath
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'

# # If service instance provides IAM API key authentication
# service = VisualRecognitionV3(
#     '2018-03-19',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/visual-recognition/api',
#     iam_apikey='iam_apikey')

service = VisualRecognitionV3('2018-03-19',
                              ## url is optional, and defaults to the URL below. Use the correct URL for your region.
                              #  url='https://gateway.watsonplatform.net/visual-recognition/api',
                              api_key='YOUR API KEY')

# with open(abspath('resources/cars.zip'), 'rb') as cars, \
#      open(abspath('resources/trucks.zip'), 'rb') as trucks:
#     classifier = service.create_classifier('Cars vs Trucks',
#                                            cars_positive_examples=cars,
#                                            negative_examples=trucks).get_result()
# print(json.dumps(classifier, indent=2))

car_path = abspath("resources/cars.zip")
try:
    with open(car_path, 'rb') as images_file:
        car_results = service.classify(
            images_file=images_file,
            threshold='0.1',
            classifier_ids=['default']).get_result()
        print(json.dumps(car_results, indent=2))
except WatsonApiException as ex:
    print(ex)

# classifier = service.get_classifier('YOUR CLASSIFIER ID').get_result()
# print(json.dumps(classifier, indent=2))

# with open(abspath('resources/car.jpg'), 'rb') as image_file:
#     classifier = service.update_classifier('CarsvsTrucks_1479118188',
#                                            cars_positive_examples=image_file).get_result()
#     print(json.dumps(classifier, indent=2))

# faces_result = service.detect_faces(url=test_url).get_result()
# print(json.dumps(faces_result, indent=2))

# response = service.delete_classifier(classifier_id='YOUR CLASSIFIER ID').get_result()
# print(json.dumps(response, indent=2))

classifiers = service.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))

face_path = abspath('resources/face.jpg')
with open(face_path, 'rb') as image_file:
    face_result = service.detect_faces(images_file=image_file).get_result()
    print(json.dumps(face_result, indent=2))

#Core ml model example
# model_name = '{0}.mlmodel'.format(classifier_id)
# core_ml_model = service.get_core_ml_model(classifier_id).get_result()
# with open('/tmp/{0}'.format(model_name), 'wb') as fp:
#     fp.write(core_ml_model.content)
