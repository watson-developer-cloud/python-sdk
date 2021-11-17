# coding: utf-8
import unittest
import ibm_watson
from os.path import join, dirname
import pytest
import os


@pytest.mark.skipif(os.getenv('LANGUAGE_TRANSLATOR_APIKEY') is None,
                    reason='requires LANGUAGE_TRANSLATOR_APIKEY')
class TestIntegrationLanguageTranslatorV3(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.language_translator = ibm_watson.LanguageTranslatorV3('2018-05-01')
        cls.language_translator.set_default_headers({'X-Watson-Test': '1'})

    def test_translate(self):
        translation = self.language_translator.translate(
            text='Hello', model_id='en-es').get_result()
        assert translation is not None
        translation = self.language_translator.translate(
            text='Hello, how are you?', target='es').get_result()
        assert translation is not None

    def test_list_languages(self):
        languages = self.language_translator.list_languages()
        assert languages is not None

    def test_document_translation(self):
        with open(join(dirname(__file__), '../../resources/hello_world.txt'),
                  'r') as fileinfo:
            translation = self.language_translator.translate_document(
                file=fileinfo, file_content_type='text/plain',
                model_id='en-es').get_result()
        document_id = translation.get('document_id')
        assert document_id is not None

        document_status = self.language_translator.get_document_status(
            document_id).get_result()
        assert document_status is not None

        if document_status.get('status') == 'available':
            response = self.language_translator.get_translated_document(
                document_id, 'text/plain').get_result()
            assert response.content is not None

        list_documents = self.language_translator.list_documents().get_result()
        assert list_documents is not None

        delete_document = self.language_translator.delete_document(
            document_id).get_result()
        assert delete_document is None
