# coding: utf-8
from unittest import TestCase
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BearerTokenAuthenticator
from ibm_watson.discovery_v2 import CreateEnrichment, EnrichmentOptions
from os.path import abspath
import os
import ibm_watson
import pytest


@pytest.mark.skipif(os.getenv('DISCOVERY_V2_APIKEY') is None,
                    reason='requires DISCOVERY_V2_APIKEY')
class Discoveryv2(TestCase):
    discovery = None
    project_id = os.getenv('DISCOVERY_V2_PROJECT_ID')  # This project is created for integration testing
    collection_id = None
    collection_name = 'python_test_collection'

    @classmethod
    def setup_class(cls):
        authenticator = IAMAuthenticator(os.getenv('DISCOVERY_V2_APIKEY'))
        cls.discovery = ibm_watson.DiscoveryV2(
            version='2020-08-12',
            authenticator=authenticator
        )
        cls.discovery.set_service_url(os.getenv('DISCOVERY_V2_URL'))
        cls.discovery.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

        collections = cls.discovery.list_collections(
            cls.project_id).get_result()['collections']
        for collection in collections:
            if collection['name'] == cls.collection_name:
                cls.collection_id = collection['collection_id']

        if cls.collection_id is None:
            print("Creating a new temporary collection")
            cls.collection_id = cls.discovery.create_collection(
                cls.project_id,
                cls.collection_name,
                description="Integration test for python sdk").get_result(
                )['collection_id']

    @classmethod
    def teardown_class(cls):
        collections = cls.discovery.list_collections(
            cls.project_id).get_result()['collections']
        for collection in collections:
            if collection['name'] == cls.collection_name:
                print('Deleting the temporary collection')
                cls.discovery.delete_collection(cls.project_id,
                                                cls.collection_id)
                break

    def test_projects(self):
        projs = self.discovery.list_projects().get_result()
        assert projs is not None
        proj = self.discovery.get_project(
            self.project_id).get_result()
        assert proj is not None

    def test_collections(self):
        cols = self.discovery.list_collections(self.project_id).get_result()
        assert cols is not None
        col = self.discovery.get_collection(
            self.project_id,
            self.collection_id
        ).get_result()
        assert col is not None

    def test_enrichments(self):
        enrs = self.discovery.list_enrichments(self.project_id).get_result()
        print(enrs)
        assert enrs is not None

        enrichmentOptions = EnrichmentOptions(
            languages=["en"],
            entity_type="keyword"
        )
        enrichment = CreateEnrichment(
            name="python test enrichment",
            description="test enrichment",
            type="dictionary",
            options=enrichmentOptions
        )
        with open(os.path.join(os.path.dirname(__file__), '../../resources/TestEnrichments.csv'), 'r') as fileinfo:
            enr = self.discovery.create_enrichment(
                project_id=self.project_id,
                enrichment=enrichment._to_dict(),
                file=fileinfo
            ).get_result()
            assert enr is not None
            enrichment_id = enr["enrichment_id"]
            enrichment = self.discovery.get_enrichment(
                self.project_id,
                enrichment_id
            ).get_result()
            assert enrichment is not None
            enr = self.discovery.update_enrichment(
                project_id=self.project_id,
                enrichment_id=enrichment_id,
                name="python test enrichment",
                description="updated description"
            ).get_result()
            assert enr is not None
            self.discovery.delete_enrichment(
                self.project_id,
                enrichment_id
            )

    # can only test in CPD
    @pytest.mark.skip(reason="can only test in CPD")
    def test_analyze(self):
        authenticator = BearerTokenAuthenticator('<bearer_token>')
        discovery_cpd = ibm_watson.DiscoveryV2(
            version='2020-08-12',
            authenticator=authenticator
        )
        discovery_cpd.service_url = "<url>"
        discovery_cpd.set_disable_ssl_verification(True)
        test_file = abspath('resources/problem.json')
        with open(test_file, 'rb') as file:
            result = discovery_cpd.analyze_document(
                project_id="<project_id>",
                collection_id="<collection_id>",
                file=file,
                file_content_type="application/json"
            ).get_result()
            assert result is not None

