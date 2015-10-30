import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyVisionV1 as AlchemyVision

alchemy_vision = AlchemyVision(api_key='YOUR API KEY')


# Face recognition
with open(join(dirname(__file__), '../resources/face.jpg'), 'rb') as image_file:
    print(json.dumps(alchemy_vision.recognize_faces(image_file, knowledge_graph=True), indent=2))

faceUrl = 'https://upload.wikimedia.org/wikipedia/commons/0/00/Scarlett_Johansson_-_Captain_America_2_press_conference_%28retouched%29_2.jpg'
print(json.dumps(alchemy_vision.recognize_faces(image_url=faceUrl, knowledge_graph=True), indent=2))

# Image tagging
with open(join(dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
    print(json.dumps(alchemy_vision.get_image_keywords(image_file, knowledge_graph=True), indent=2))

print(json.dumps(alchemy_vision.get_image_keywords(
    image_url='https://upload.wikimedia.org/wikipedia/commons/8/81/Morris-Chair-Ironwood.jpg'), indent=2))

# Image link extraction
print(json.dumps(alchemy_vision.get_image_links(url='http://www.ibm.com/smarterplanet/us/en/ibmwatson/'), indent=2))

with open(join(dirname(__file__), '../resources/example.html'), 'r') as webpage:
    print(json.dumps(alchemy_vision.get_image_links(html=webpage.read()), indent=2))
