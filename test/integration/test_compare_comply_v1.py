# coding: utf-8
import pytest
import ibm_watson
import os
from os.path import abspath
from unittest import TestCase
from ibm_watson.compare_comply_v1 import TableReturn


@pytest.mark.skipif(os.getenv('COMPARE_COMPLY_APIKEY') is None,
                    reason='requires COMPARE_COMPLY_APIKEY')
class IntegrationTestCompareComplyV1(TestCase):
    compare_comply = None

    @classmethod
    def setup_class(cls):
        cls.compare_comply = ibm_watson.CompareComplyV1('2018-10-15')
        cls.compare_comply.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

    def test_convert_to_html(self):
        contract = abspath('resources/contract_A.pdf')
        with open(contract, 'rb') as file:
            result = self.compare_comply.convert_to_html(file).get_result()
        assert result is not None

    def test_classify_elements(self):
        contract = abspath('resources/contract_A.pdf')
        with open(contract, 'rb') as file:
            result = self.compare_comply.classify_elements(
                file, file_content_type='application/pdf').get_result()
        assert result is not None

    def test_extract_tables(self):
        table = abspath('resources/table_test.png')
        with open(table, 'rb') as file:
            result = self.compare_comply.extract_tables(file).get_result()
            TableReturn._from_dict(result)
        assert result is not None

    def test_compare_documents(self):
        with open(os.path.join(os.path.dirname(__file__), '../../resources/contract_A.pdf'), 'rb') as file1, \
          open(os.path.join(os.path.dirname(__file__), '../../resources/contract_B.pdf'), 'rb') as file2:
            result = self.compare_comply.compare_documents(file1,
                                                           file2).get_result()

        assert result is not None

    @pytest.mark.skip(reason="Temporarily skip")
    def test_feedback(self):
        feedback_data = {
            'feedback_type':
                'element_classification',
            'document': {
                'hash': '',
                'title': 'doc title'
            },
            'model_id':
                'contracts',
            'model_version':
                '11.00',
            'location': {
                'begin': '214',
                'end': '237'
            },
            'text':
                '1. IBM will provide a Senior Managing Consultant / expert resource, for up to 80 hours, to assist Florida Power & Light (FPL) with the creation of an IT infrastructure unit cost model for existing infrastructure.',
            'original_labels': {
                'types': [{
                    'label': {
                        'nature': 'Obligation',
                        'party': 'IBM'
                    },
                    'provenance_ids': [
                        '85f5981a-ba91-44f5-9efa-0bd22e64b7bc',
                        'ce0480a1-5ef1-4c3e-9861-3743b5610795'
                    ]
                }, {
                    'label': {
                        'nature': 'End User',
                        'party': 'Exclusion'
                    },
                    'provenance_ids': [
                        '85f5981a-ba91-44f5-9efa-0bd22e64b7bc',
                        'ce0480a1-5ef1-4c3e-9861-3743b5610795'
                    ]
                }],
                'categories': [{
                    'label': 'Responsibilities',
                    'provenance_ids': []
                }, {
                    'label': 'Amendments',
                    'provenance_ids': []
                }]
            },
            'updated_labels': {
                'types': [{
                    'label': {
                        'nature': 'Obligation',
                        'party': 'IBM'
                    }
                }, {
                    'label': {
                        'nature': 'Disclaimer',
                        'party': 'Buyer'
                    }
                }],
                'categories': [{
                    'label': 'Responsibilities'
                }, {
                    'label': 'Audits'
                }]
            }
        }

        add_feedback = self.compare_comply.add_feedback(
            feedback_data, user_id='wonder woman',
            comment='test commment').get_result()
        assert add_feedback is not None
        assert add_feedback['feedback_id'] is not None
        feedback_id = add_feedback['feedback_id']

        self.compare_comply.set_default_headers(
            {'x-watson-metadata': 'customer_id=sdk-test-customer-id'})
        get_feedback = self.compare_comply.get_feedback(
            feedback_id).get_result()
        assert get_feedback is not None

        list_feedback = self.compare_comply.list_feedback(
            feedback_type='element_classification').get_result()
        assert list_feedback is not None

        delete_feedback = self.compare_comply.delete_feedback(
            feedback_id).get_result()
        assert delete_feedback is not None

    @pytest.mark.skip(reason="Temporarily skip")
    def test_batches(self):
        list_batches = self.compare_comply.list_batches().get_result()
        assert list_batches is not None

        with open(os.path.join(os.path.dirname(__file__), '../../resources/cloud-object-storage-credentials-input.json'), 'rb') as input_credentials_file, \
          open(os.path.join(os.path.dirname(__file__), '../../resources/cloud-object-storage-credentials-output.json'), 'rb') as output_credentials_file:
            create_batch = self.compare_comply.create_batch(
                'html_conversion', input_credentials_file, 'us-south',
                'compare-comply-integration-test-bucket-input',
                output_credentials_file, 'us-south',
                'compare-comply-integration-test-bucket-output').get_result()

        assert create_batch is not None
        assert create_batch['batch_id'] is not None
        batch_id = create_batch['batch_id']

        get_batch = self.compare_comply.get_batch(batch_id)
        assert get_batch is not None

        update_batch = self.compare_comply.update_batch(batch_id, 'rescan')
        assert update_batch is not None
