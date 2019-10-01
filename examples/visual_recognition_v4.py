import json
import os
from ibm_watson import VisualRecognitionV4
from ibm_watson.visual_recognition_v4 import FileWithMetadata, BaseObject, Location
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('<your api key>')
service = VisualRecognitionV4(
    '2018-03-19',
    authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api')

# create a classifier
my_collection = service.create_collection(
    name='',
    description='tetsing for python'
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
        BaseObject(object='giraffe training data', location=Location(64, 270, 755, 784))
    ]).get_result()

# train collection
train_result = service.train(collection_id).get_result()

# delete collection
service.delete_collection(collection_id)
