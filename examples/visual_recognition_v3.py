import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

test_url = 'http://ia.media-imdb.com/images/M/MV5BMTMxMDIzMDEzNF5BMl5BanBnXkFtZTcwODcxMjE2Mg@@._V1_UY317_CR2,0,214,317_AL_.jpg'

visual_recognition = VisualRecognitionV3('2016-05-20',api_key=environ['API_KEY'])

#with open(join(dirname(__file__), '../resources/cars.zip'), 'rb') as cars, \
#        open(join(dirname(__file__), '../resources/trucks.zip'), 'rb') as trucks:
#    print(json.dumps(visual_recognition.create_classifier('Cars vs Trucks', cars_positive_examples=cars,
#                                                          negative_examples=trucks), indent=2))

with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as image_file:
    print(json.dumps(visual_recognition.classify(images_file=image_file),indent=2))

#print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))

#The service currently has a bug where even successful deletions return a 404
#print(json.dumps(visual_recognition.delete_classifier(classifier_id='YOUR CLASSIFIER ID'), indent=2))

#print(json.dumps(visual_recognition.list_classifiers(), indent=2))

# with open(join(dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
#     print(json.dumps(visual_recognition.classify(image_file, classifier_ids=['Tiger', 'Cat']), indent=2))
