import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyVisionV1

alchemy_vision = AlchemyVisionV1(api_key='YOUR API KEY')


# Face recognition
with open(join(dirname(__file__), '../resources/face.jpg'), 'rb') as image_file:
    print(json.dumps(alchemy_vision.recognize_faces(image_file, knowledge_graph=True), indent=2))

face_url = 'https://upload.wikimedia.org/wikipedia/commons/9/9d/Barack_Obama.jpg'
print(json.dumps(alchemy_vision.recognize_faces(image_url=face_url, knowledge_graph=True), indent=2))

# Image tagging
with open(join(dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
    print(json.dumps(alchemy_vision.get_image_keywords(image_file, knowledge_graph=True,
                                                       force_show_all=True), indent=2))
# Text recognition
with open(join(dirname(__file__), '../resources/text.png'), 'rb') as image_file:
    print(json.dumps(alchemy_vision.get_image_scene_text(image_file), indent=2))

print(json.dumps(alchemy_vision.get_image_keywords(
    image_url='https://upload.wikimedia.org/wikipedia/commons/8/81/Morris-Chair-Ironwood.jpg'), indent=2))

# Image link extraction
print(json.dumps(alchemy_vision.get_image_links(url='http://www.zillow.com/'), indent=2))

with open(join(dirname(__file__), '../resources/example.html'), 'r') as webpage:
    print(json.dumps(alchemy_vision.get_image_links(html=webpage.read()), indent=2))
