# coding: utf-8
import pytest
import ibm_watson
import os
import json
from unittest import TestCase
from ibm_watson.visual_recognition_v4 import AnalyzeEnums, FileWithMetadata, TrainingDataObject, Location


@pytest.mark.skipif(os.getenv('VISUAL_RECOGNITION_APIKEY') is None,
                    reason='requires VISUAL_RECOGNITION_APIKEY')
class IntegrationTestVisualRecognitionV3(TestCase):
    visual_recognition = None

    @classmethod
    def setup_class(cls):
        cls.visual_recognition = ibm_watson.VisualRecognitionV4('2019-02-11')
        cls.visual_recognition.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

    def test_01_colllections(self):
        collection = self.visual_recognition.create_collection(
            name='my_collection', description='just for fun').get_result()
        collection_id = collection.get('collection_id')
        assert collection_id is not None

        my_collection = self.visual_recognition.get_collection(
            collection_id=collection.get('collection_id')).get_result()
        assert my_collection is not None
        assert my_collection.get('name') == 'my_collection'

        updated_collection = self.visual_recognition.update_collection(
            collection_id=collection_id,
            description='new description').get_result()
        assert updated_collection is not None

        collections = self.visual_recognition.list_collections().get_result(
        ).get('collections')
        assert collections is not None

        self.visual_recognition.delete_collection(collection_id=collection_id)

    def test_02_images(self):
        collection = self.visual_recognition.create_collection(
            name='my_collection', description='just for fun').get_result()
        collection_id = collection.get('collection_id')

        add_images = self.visual_recognition.add_images(
            collection_id,
            image_url=[
                "https://upload.wikimedia.org/wikipedia/commons/3/33/KokoniPurebredDogsGreeceGreekCreamWhiteAdult.jpg",
                "https://upload.wikimedia.org/wikipedia/commons/0/07/K%C3%B6nigspudel_Apricot.JPG"
            ],
        ).get_result()
        assert add_images is not None
        image_id = add_images.get('images')[0].get('image_id')

        list_images = self.visual_recognition.list_images(
            collection_id).get_result()
        assert list_images is not None

        image_details = self.visual_recognition.get_image_details(
            collection_id, image_id).get_result()
        assert image_details is not None

        response = self.visual_recognition.get_jpeg_image(
            collection_id, image_id).get_result()
        assert response.content is not None

        self.visual_recognition.delete_image(collection_id, image_id)
        self.visual_recognition.delete_collection(collection_id)

    def test_03_analyze(self):
        dog_path = os.path.join(os.path.dirname(__file__),
                                '../../resources/dog.jpg')
        giraffe_path = os.path.join(os.path.dirname(__file__),
                                    '../../resources/my-giraffe.jpeg')

        with open(dog_path, 'rb') as dog_file, open(giraffe_path,
                                                    'rb') as giraffe_files:
            analyze_images = self.visual_recognition.analyze(
                collection_ids=['a06f7036-0529-49ee-bdf6-82ddec276923'],
                features=[AnalyzeEnums.Features.OBJECTS.value],
                images_file=[
                    FileWithMetadata(dog_file),
                    FileWithMetadata(giraffe_files)
                ],
                image_url=[
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/American_Eskimo_Dog.jpg/1280px-American_Eskimo_Dog.jpg'
                ]).get_result()
            assert analyze_images is not None
        print(json.dumps(analyze_images, indent=2))

    def test_04_objects_and_training(self):
        # create a classifier
        my_collection = self.visual_recognition.create_collection(
            name='my_test_collection',
            description='testing for python').get_result()
        collection_id = my_collection.get('collection_id')
        assert collection_id is not None

        # add images
        with open(
                os.path.join(
                    os.path.dirname(__file__),
                    '../../resources/South_Africa_Luca_Galuzzi_2004.jpeg'),
                'rb') as giraffe_info:
            add_images_result = self.visual_recognition.add_images(
                collection_id,
                images_file=[FileWithMetadata(giraffe_info)],
            ).get_result()
        assert add_images_result is not None
        image_id = add_images_result.get('images')[0].get('image_id')
        assert image_id is not None

        # add image training data
        training_data = self.visual_recognition.add_image_training_data(
            collection_id,
            image_id,
            objects=[
                TrainingDataObject(object='giraffe training data',
                                   location=Location(64, 270, 755, 784))
            ]).get_result()
        assert training_data is not None

        # list objects metadata
        object_metadata_list = self.visual_recognition.list_object_metadata(
            collection_id=collection_id).get_result()
        assert object_metadata_list is not None

        # update object metadata
        object_metadata = object_metadata_list.get('objects')[0]
        updated_object_metadata = self.visual_recognition.update_object_metadata(
            collection_id=collection_id,
            object=object_metadata.get('object'),
            new_object='updated giraffe training data').get_result()
        assert updated_object_metadata is not None

        # get object metadata
        object_metadata = self.visual_recognition.get_object_metadata(
            collection_id=collection_id,
            object='updated giraffe training data',
        ).get_result()
        assert object_metadata is not None
        assert object_metadata.get('object') == 'updated giraffe training data'

        # train collection
        train_result = self.visual_recognition.train(collection_id).get_result()
        assert train_result is not None
        assert train_result.get('training_status') is not None

        # training usage
        training_usage = self.visual_recognition.get_training_usage(
            start_time='2019-11-01', end_time='2019-11-27').get_result()
        assert training_usage is not None

        # delete object
        self.visual_recognition.delete_object(
            collection_id, object='updated giraffe training data')

        # delete collection
        self.visual_recognition.delete_collection(collection_id)
