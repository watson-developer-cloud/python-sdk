import json
import mimetypes
import os
from os.path import join, dirname
import responses
import tempfile
import watson_developer_cloud

@responses.activate
def test_success():
    if os.environ.get('API_KEY') is None:
        # skip the tests if we don't have an api key
        return

    classify_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify'
    image_file = open(join(dirname(__file__), '../resources/car.jpg'), 'rb')
    response = requests.post(
        url=classify_url,
        params = {
            "version": '2016-05-20',
            "api_key": os.environ.get('API_KEY')
        },
        files = { "images_file" : (image_file.name, image_file, mimetypes.guess_type(image_file.name)[0])}
    )

    visual_recognition = watson_developer_cloud.VisualRecognitionV3('2016-05-20',api_key=os.environ.get('API_KEY'))
    classification_results = visual_recognition.classify(images_file=image_file)

    assert json.dumps(response) == json.dumps(classification_results)


    response = requests.post(
        url=classify_url,
        params = {
            'version': '2016-05-20',
            'api_key': os.environ.get('API_KEY'),
            'url' : 'http://www.stackoverflow.com'
        })

    classification_results = visual_recognition.classify(images_url='http://www.stackoverflow.com')

    assert json.dumps(response) == json.dumps(classification_results)


    assert visual_recognition.guess_mime_type(image_file)[0] == 'image/jpeg'

    try:
        failing_temp = tempfile.NamedTemporaryFile()
        visual_recognition.guess_mime_type(failing_temp.file)
    except AssertionError as ae:
        assert str(ae) == 'You must specify a jpeg, png, or gif image'

    try:
        failing_temp = tempfile.NamedTemporaryFile(suffix='.pdf')
        visual_recognition.guess_mime_type(failing_temp.file)
    except AssertionError as ae:
        assert str(ae) == 'You must specify a jpeg, png, or gif image'


        if os.environ.get('API_KEY') is None:
            # skip the tests if we don't have an api key
            return

    faces_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/detect_faces'
    image_file = open(join(dirname(__file__), '../resources/car.jpg'), 'rb')
    response = requests.post(
        url=faces_url,
        params = {
            "version": '2016-05-20',
            "api_key": os.environ.get('API_KEY')
        },
        files = { "images_file" : (image_file.name, image_file, mimetypes.guess_type(image_file.name)[0])}
    )

    face_results = visual_recognition.detect_faces(images_file=image_file)

    assert json.dumps(response) == json.dumps(face_results)

    text_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/recognize_text'
    image_file = open(join(dirname(__file__), '../resources/car.jpg'), 'rb')
    response = requests.post(
        url=faces_url,
        params = {
            "version": '2016-05-20',
            "api_key": os.environ.get('API_KEY')
        },
        files = { "images_file" : (image_file.name, image_file, mimetypes.guess_type(image_file.name)[0])}
    )

    text_results = visual_recognition.recognize_text(images_file=image_file)

    assert json.dumps(response) == json.dumps(text_results)

    list_classifiers_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers'
    response = requests.get(
        url=list_classifiers_url,
        params = {
            "version": '2016-05-20',
            "api_key": os.environ.get('API_KEY')
        }
    )

    list_results = visual_recognition.list_classifiers()
    assert json.dumps(response) == json.dumps(list_results)
