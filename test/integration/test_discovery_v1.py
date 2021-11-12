# coding: utf-8
from unittest import TestCase
import os
import ibm_watson
import random
import pytest


@pytest.mark.skipif(os.getenv('DISCOVERY_APIKEY') is None,
                    reason='requires DISCOVERY_APIKEY')
class Discoveryv1(TestCase):
    discovery = None
    environment_id = os.getenv('DISCOVERY_ENVIRONMENT_ID')  # This environment is created for integration testing
    collection_id = None
    collection_name = 'FOR-PYTHON-DELETE-ME'

    @classmethod
    def setup_class(cls):
        cls.discovery = ibm_watson.DiscoveryV1(version='2018-08-01')
        cls.discovery.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

        collections = cls.discovery.list_collections(
            cls.environment_id).get_result()['collections']
        for collection in collections:
            if collection['name'] == cls.collection_name:
                cls.collection_id = collection['collection_id']

        if cls.collection_id is None:
            print("Creating a new temporary collection")
            cls.collection_id = cls.discovery.create_collection(
                cls.environment_id,
                cls.collection_name,
                description="Integration test for python sdk").get_result(
                )['collection_id']

    @classmethod
    def teardown_class(cls):
        collections = cls.discovery.list_collections(
            cls.environment_id).get_result()['collections']
        for collection in collections:
            if collection['name'] == cls.collection_name:
                print('Deleting the temporary collection')
                cls.discovery.delete_collection(cls.environment_id,
                                                cls.collection_id)
                break

    def test_environments(self):
        envs = self.discovery.list_environments().get_result()
        assert envs is not None
        env = self.discovery.get_environment(
            envs['environments'][0]['environment_id']).get_result()
        assert env is not None
        fields = self.discovery.list_fields(self.environment_id,
                                            self.collection_id).get_result()
        assert fields is not None

    def test_configurations(self):
        configs = self.discovery.list_configurations(
            self.environment_id).get_result()
        assert configs is not None

        name = 'test' + random.choice('ABCDEFGHIJKLMNOPQ')
        new_configuration_id = self.discovery.create_configuration(
            self.environment_id,
            name,
            description='creating new config for python sdk').get_result(
            )['configuration_id']
        assert new_configuration_id is not None
        self.discovery.get_configuration(self.environment_id,
                                         new_configuration_id).get_result()

        updated_config = self.discovery.update_configuration(
            self.environment_id, new_configuration_id, 'lala').get_result()
        assert updated_config['name'] == 'lala'

        deleted_config = self.discovery.delete_configuration(
            self.environment_id, new_configuration_id).get_result()
        assert deleted_config['status'] == 'deleted'

    def test_collections_and_expansions(self):
        self.discovery.get_collection(self.environment_id, self.collection_id)
        updated_collection = self.discovery.update_collection(
            self.environment_id,
            self.collection_id,
            self.collection_name,
            description='Updating description').get_result()
        assert updated_collection['description'] == 'Updating description'

        self.discovery.create_expansions(self.environment_id,
                                         self.collection_id, [{
                                             'input_terms': ['a'],
                                             'expanded_terms': ['aa']
                                         }]).get_result()
        expansions = self.discovery.list_expansions(
            self.environment_id, self.collection_id).get_result()
        assert expansions['expansions']
        self.discovery.delete_expansions(self.environment_id,
                                         self.collection_id)

    def test_documents(self):
        with open(
                os.path.join(os.path.dirname(__file__),
                             '../../resources/simple.html'), 'r') as fileinfo:
            add_doc = self.discovery.add_document(
                environment_id=self.environment_id,
                collection_id=self.collection_id,
                file=fileinfo).get_result()
        assert add_doc['document_id'] is not None

        doc_status = self.discovery.get_document_status(
            self.environment_id, self.collection_id,
            add_doc['document_id']).get_result()
        assert doc_status is not None

        with open(
                os.path.join(os.path.dirname(__file__),
                             '../../resources/simple.html'), 'r') as fileinfo:
            update_doc = self.discovery.update_document(
                self.environment_id,
                self.collection_id,
                add_doc['document_id'],
                file=fileinfo,
                filename='newname.html').get_result()
        assert update_doc is not None
        delete_doc = self.discovery.delete_document(
            self.environment_id, self.collection_id,
            add_doc['document_id']).get_result()
        assert delete_doc['status'] == 'deleted'

    def test_queries(self):
        query_results = self.discovery.query(
            self.environment_id,
            self.collection_id,
            filter='extracted_metadata.sha1::9181d244*').get_result()
        assert query_results is not None

    @pytest.mark.skip(
        reason="Temporary skipping because update_credentials fails")
    def test_credentials(self):
        credential_details = {
            'credential_type': 'username_password',
            'url': 'https://login.salesforce.com',
            'username': 'user@email.com',
            'password': 'xxx'
        }
        credentials = self.discovery.create_credentials(
            self.environment_id,
            source_type='salesforce',
            credential_details=credential_details).get_result()
        assert credentials['credential_id'] is not None
        credential_id = credentials['credential_id']

        get_credentials = self.discovery.get_credentials(
            self.environment_id, credential_id).get_result()
        assert get_credentials['credential_id'] == credential_id

        list_credentials = self.discovery.list_credentials(
            self.environment_id).get_result()
        assert list_credentials is not None

        new_credential_details = {
            'credential_type': 'username_password',
            'url': 'https://logo.salesforce.com',
            'username': 'user@email.com',
            'password': 'xxx'
        }
        updated_credentials = self.discovery.update_credentials(
            self.environment_id,
            credential_id,
            source_type='salesforce',
            credential_details=new_credential_details).get_result()
        assert updated_credentials is not None

        get_credentials = self.discovery.get_credentials(
            self.environment_id, credentials['credential_id']).get_result()
        assert get_credentials['credential_details'][
            'url'] == new_credential_details['url']

        delete_credentials = self.discovery.delete_credentials(
            self.environment_id, credential_id).get_result()
        assert delete_credentials['credential_id'] is not None

    def test_create_event(self):
        # create test document
        with open(
                os.path.join(os.path.dirname(__file__),
                             '../../resources/simple.html'), 'r') as fileinfo:
            add_doc = self.discovery.add_document(
                environment_id=self.environment_id,
                collection_id=self.collection_id,
                file=fileinfo).get_result()
        assert add_doc['document_id'] is not None
        document_id = add_doc['document_id']

        # make query to get session token
        query = self.discovery.query(
            self.environment_id,
            self.collection_id,
            natural_language_query='The content of the first chapter'
        ).get_result()
        assert query['session_token'] is not None

        # create_event
        event_data = {
            "environment_id": self.environment_id,
            "session_token": query['session_token'],
            "collection_id": self.collection_id,
            "document_id": document_id,
        }
        create_event_response = self.discovery.create_event(
            'click', event_data).get_result()
        assert create_event_response['type'] == 'click'

        #delete the documment
        self.discovery.delete_document(self.environment_id, self.collection_id,
                                       document_id).get_result()

    @pytest.mark.skip(reason="Temporary disable")
    def test_tokenization_dictionary(self):
        result = self.discovery.get_tokenization_dictionary_status(
            self.environment_id, self.collection_id).get_result()
        assert result['status'] is not None

    def test_feedback(self):
        response = self.discovery.get_metrics_event_rate(
            start_time='2018-08-13T14:39:59.309Z',
            end_time='2018-08-14T14:39:59.309Z',
            result_type='document').get_result()
        assert response['aggregations'] is not None

        response = self.discovery.get_metrics_query(
            start_time='2018-08-13T14:39:59.309Z',
            end_time='2018-08-14T14:39:59.309Z',
            result_type='document').get_result()
        assert response['aggregations'] is not None

        response = self.discovery.get_metrics_query_event(
            start_time='2018-08-13T14:39:59.309Z',
            end_time='2018-08-14T14:39:59.309Z',
            result_type='document').get_result()
        assert response['aggregations'] is not None

        response = self.discovery.get_metrics_query_no_results(
            start_time='2018-07-13T14:39:59.309Z',
            end_time='2018-08-14T14:39:59.309Z',
            result_type='document').get_result()
        assert response['aggregations'] is not None

        response = self.discovery.get_metrics_query_token_event(
            count=10).get_result()
        assert response['aggregations'] is not None

        response = self.discovery.query_log(count=2).get_result()
        assert response is not None

    @pytest.mark.skip(reason="Skip temporarily.")
    def test_stopword_operations(self):
        with open(
                os.path.join(os.path.dirname(__file__),
                             '../../resources/stopwords.txt'),
                'r') as stopwords_file:
            create_stopword_list_result = self.discovery.create_stopword_list(
                self.environment_id, self.collection_id,
                stopwords_file).get_result()
        assert create_stopword_list_result is not None

        delete_stopword_list_result = self.discovery.delete_stopword_list(
            self.environment_id, self.collection_id).get_result()
        assert delete_stopword_list_result is None

    def test_gateway_configuration(self):
        create_gateway_result = self.discovery.create_gateway(
            self.environment_id,
            name='test-gateway-configuration-python').get_result()
        assert create_gateway_result['gateway_id'] is not None

        get_gateway_result = self.discovery.get_gateway(
            self.environment_id,
            create_gateway_result['gateway_id']).get_result()
        assert get_gateway_result is not None

        list_gateways_result = self.discovery.list_gateways(
            self.environment_id).get_result()
        assert list_gateways_result is not None

        delete_gateways_result = self.discovery.delete_gateway(
            self.environment_id,
            create_gateway_result['gateway_id']).get_result()
        assert delete_gateways_result is not None
