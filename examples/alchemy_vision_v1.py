import json
from watson_developer_cloud import AlchemyVisionV1 as AlchemyVision

alchemy_vision = AlchemyVision(api_key='YOUR API KEY')


# with open(join(dirname(__file__), '../resources/face.jpg'), 'rb') as image_file:
#     print(json.dumps(alchemy_vision.recognize_faces(image_file, knowledge_graph=True), indent=2))

print(json.dumps(alchemy_vision.get_image_keywords(
   image_url='https://upload.wikimedia.org/wikipedia/commons/9/9d/Barack_Obama.jpg'), indent=2))
