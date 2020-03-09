import json
import os
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import FileWithMetadata, TrainingDataObject, Location, AnalyzeEnums
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    'YOUR APIKEY')
service = VisualRecognitionV4(
    '2018-03-19',
    authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api')

# create a classifier
my_collection = service.create_collection(
    name='',
    description='testing for python'
).get_result()
collection_id = my_collection.get('collection_id')

# add images
with open(os.path.join(os.path.dirname(__file__), '../resources/South_Africa_Luca_Galuzzi_2004.jpeg'), 'rb') as giraffe_info:
    add_images_result = service.add_images(
        collection_id,
        images_file=[FileWithMetadata(giraffe_info)],
    ).get_result()
print(json.dumps(add_images_result, indent=2))
image_id = add_images_result.get('images')[0].get('image_id')

# add image training data
training_data = service.add_image_training_data(
    collection_id,
    image_id,
    objects=[
        TrainingDataObject(object='giraffe training data',
                           location=Location(64, 270, 755, 784))
    ]).get_result()
print(json.dumps(training_data, indent=2))

# update object metadata
updated_object_metadata = service.update_object_metadata(
    collection_id=collection_id,
    object='giraffe training data',
    new_object='updated giraffe training data').get_result()
print(json.dumps(updated_object_metadata, indent=2))

# train collection
train_result = service.train(collection_id).get_result()
print(json.dumps(train_result, indent=2))

# training usage
training_usage = service.get_training_usage()
print(json.dumps(training_usage, indent=2))

# analyze
dog_path = os.path.join(os.path.dirname(__file__), '../resources/dog.jpg')
giraffe_path = os.path.join(os.path.dirname(__file__), '../resources/my-giraffe.jpeg')
with open(dog_path, 'rb') as dog_file, open(giraffe_path, 'rb') as giraffe_files:
    analyze_images = service.analyze(
        collection_ids=[collection_id],
        features=[AnalyzeEnums.Features.OBJECTS.value],
        images_file=[
            FileWithMetadata(dog_file),
            FileWithMetadata(giraffe_files)
        ],
        image_url=['https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/American_Eskimo_Dog.jpg/1280px-American_Eskimo_Dog.jpg']).get_result()
    print(json.dumps(analyze_images, indent=2))

# delete collection
service.delete_collection(collection_id)
