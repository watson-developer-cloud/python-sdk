import responses
import watson_developer_cloud
import json
import os

from unittest import TestCase

base_url = "https://gateway-a.watsonplatform.net/visual-recognition/api/"


class TestVisualRecognitionV3(TestCase):
    @responses.activate
    def test_get_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers/bogusnumber')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        vr_service.get_classifier(classifier_id='bogusnumber')

        assert len(responses.calls) == 1

    @responses.activate
    def test_delete_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers/bogusnumber')

        responses.add(responses.DELETE,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        vr_service.delete_classifier(classifier_id='bogusnumber')

        assert len(responses.calls) == 1

    @responses.activate
    def test_list_classifiers(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        vr_service.list_classifiers()

        assert len(responses.calls) == 1

    @responses.activate
    def test_create_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.create_classifier(name="bogus name")
        assert len(responses.calls) == 1

    @responses.activate
    def test_update_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers/bogusid')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.update_classifier(classifier_id="bogusid", name="bogus name")
        assert len(responses.calls) == 1

    @responses.activate
    def test_classify(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classify')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        thrown = False
        try:
            vr_service.classify()
        except AssertionError as ae:
            assert str(ae) == 'You must specify either a file or a url'
            thrown = True
        assert thrown

        vr_service.classify(images_url="http://google.com")

        vr_service.classify(images_url="http://google.com", classifier_ids=['one', 'two', 'three'])
        vr_service.classify(images_url="http://google.com", owners=['one', 'two', 'three'])

        with open(os.path.join(os.path.dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
            vr_service.classify(images_file=image_file)
        assert len(responses.calls) == 4

    @responses.activate
    def test_detect_faces(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/detect_faces')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        thrown = False
        try:
            vr_service.detect_faces()
        except AssertionError as ae:
            assert str(ae) == 'You must specify either a file or a url'
            thrown = True
        assert thrown

        vr_service.detect_faces(images_url="http://google.com")
        with open(os.path.join(os.path.dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
            vr_service.detect_faces(images_file=image_file)
        assert len(responses.calls) == 2

    @responses.activate
    def test_recognize_text(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/recognize_text')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        thrown = False
        try:
            vr_service.recognize_text()
        except AssertionError as ae:
            assert str(ae) == 'You must specify either a file or a url'
            thrown = True
        assert thrown

        vr_service.recognize_text(images_url="http://google.com")

        with open(os.path.join(os.path.dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
            vr_service.recognize_text(images_file=image_file)

        assert len(responses.calls) == 2

    @responses.activate
    def test_create_collection(self):

        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.create_collection(name="bogus name")
        assert len(responses.calls) == 1

    @responses.activate
    def test_get_collection(self):

        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.get_collection(collection_id="bogusid")
        assert len(responses.calls) == 1

    @responses.activate
    def test_list_collections(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.list_collections()
        assert len(responses.calls) == 1

    @responses.activate
    def test_delete_collection(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid')

        responses.add(responses.DELETE,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.delete_collection(collection_id='bogusid')
        assert len(responses.calls) == 1

    @responses.activate
    def test_add_image(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/images')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        with open(os.path.join(os.path.dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
            vr_service.add_image(collection_id='bogusid', image_file=image_file)
        assert len(responses.calls) == 1

    @responses.activate
    def test_list_images(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/images')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.list_images(collection_id='bogusid')
        assert len(responses.calls) == 1

    @responses.activate
    def test_get_image(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/images/imageid')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.get_image(collection_id='bogusid', image_id="imageid")
        assert len(responses.calls) == 1

    @responses.activate
    def test_delete_image(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/images/imageid')

        responses.add(responses.DELETE,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.delete_image(collection_id='bogusid', image_id="imageid")
        assert len(responses.calls) == 1

    @responses.activate
    def test_set_image_metadata(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/images/imageid/metadata')

        responses.add(responses.PUT,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.set_image_metadata(collection_id="bogusid", image_id="imageid", metadata={'one': 10})
        assert len(responses.calls) == 1

    @responses.activate
    def test_get_image_metadata(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/images/imageid/metadata')

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.get_image_metadata(collection_id="bogusid", image_id="imageid")
        assert len(responses.calls) == 1

    @responses.activate
    def test_delete_image_metadata(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/images/imageid/metadata')

        responses.add(responses.DELETE,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        vr_service.delete_image_metadata(collection_id="bogusid", image_id="imageid")
        assert len(responses.calls) == 1

    @responses.activate
    def test_find_similar(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/collections/bogusid/find_similar')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')

        with open(os.path.join(os.path.dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
            vr_service.find_similar(collection_id='bogusid', image_file=image_file)
        assert len(responses.calls) == 1
