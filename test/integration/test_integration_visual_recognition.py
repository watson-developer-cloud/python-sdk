import pytest
import watson_developer_cloud
import os
from os.path import join, dirname
from unittest import TestCase

pytestmark = pytest.mark.skip('Run These Manually, they are destructive')

class IntegrationTestVisualRecognitionV3(TestCase):

    def setUp(self):
        self.visual_recognition = watson_developer_cloud.VisualRecognitionV3('2016-05-20', api_key=os.environ.get(
            'VISUAL_RECOGNITION_API_KEY'))
        self.collections = self.visual_recognition.list_collections()

        collection_json = self.visual_recognition.create_collection(name="test_integration_collection")
        self.collection_id = collection_json['collection_id']

    def tearDown(self):
        results = self.visual_recognition.delete_collection(collection_id=self.collection_id)
        assert not results

    def test_list_collections(self):
        results = self.visual_recognition.list_collections()
        assert len(results['collections']) - len(self.collections['collections']) == 1

    def test_add_image_check_metadata_delete_image(self):
        with open(join(dirname(__file__), '../resources/face.jpg'), 'rb') as image_file:
            self.visual_recognition.add_image(collection_id=self.collection_id, image_file=image_file, metadata={'name': 'face'})

        images = self.visual_recognition.list_images(self.collection_id)
        assert len(images['images']) == 1

        image_id = images['images'][0]['image_id']
        meta = self.visual_recognition.get_image_metadata(collection_id=self.collection_id, image_id=image_id)
        assert not meta

        assert meta['name'] == 'face'
        assert 'neverland' not in meta

        self.visual_recognition.set_image_metadata(collection_id=self.collection_id, image_id=image_id, metadata={'location': 'neverland'})
        meta = self.visual_recognition.get_image_metadata(collection_id=self.collection_id, image_id=image_id)
        assert not meta
        assert 'name' not in meta
        assert meta['location'] == 'neverland'

        self.visual_recognition.delete_image(collection_id=self.collection_id, image_id=image_id)

        images = self.visual_recognition.list_images(self.collection_id)
        assert images['images']

    def test_find_similar(self):
        with open(join(dirname(__file__), '../resources/face.jpg'), 'rb') as image_file:
            results = self.visual_recognition.find_similar(collection_id=self.collection_id, image_file=image_file)
            assert results['images_processed'] == 1
