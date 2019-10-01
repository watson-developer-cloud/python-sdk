import json
from os.path import abspath
from ibm_watson import VisualRecognitionV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('your_apikey')
test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'

# If service instance provides IAM API key authentication
service = VisualRecognitionV3(
    '2018-03-19',
    authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api')

# with open(abspath('resources/cars.zip'), 'rb') as cars, \
#      open(abspath('resources/trucks.zip'), 'rb') as trucks:
#     classifier = service.create_classifier('Cars vs Trucks',
#                                            positive_examples={'cars': cars},
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
except ApiException as ex:
    print(ex)

# classifier = service.get_classifier('YOUR CLASSIFIER ID').get_result()
# print(json.dumps(classifier, indent=2))

# with open(abspath('resources/car.jpg'), 'rb') as image_file:
#     classifier = service.update_classifier('CarsvsTrucks_1479118188',
#                                            positive_examples={'cars_positive_examples': image_file}).get_result()
#     print(json.dumps(classifier, indent=2))

# response = service.delete_classifier(classifier_id='YOUR CLASSIFIER ID').get_result()
# print(json.dumps(response, indent=2))

classifiers = service.list_classifiers().get_result()
print(json.dumps(classifiers, indent=2))

#Core ml model example
# model_name = '{0}.mlmodel'.format(classifier_id)
# core_ml_model = service.get_core_ml_model(classifier_id).get_result()
# with open('/tmp/{0}'.format(model_name), 'wb') as fp:
#     fp.write(core_ml_model.content)
