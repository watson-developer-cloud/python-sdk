# coding: utf-8
import responses
import ibm_watson
import json
import os
import time
import jwt

from unittest import TestCase

base_url = "https://gateway.watsonplatform.net/compare-comply/api"
feedback = {
    "comment": "test commment",
    "user_id": "wonder woman",
    "feedback_id": "lala",
    "feedback_data": {
        "model_id": "contracts",
        "original_labels": {
            "categories": [
                {
                    "modification": "unchanged",
                    "provenance_ids": [],
                    "label": "Responsibilities"
                },
                {
                    "modification": "removed",
                    "provenance_ids": [],
                    "label": "Amendments"
                }
            ],
            "types": [
                {
                    "modification": "unchanged",
                    "provenance_ids": [
                        "111",
                        "2222"
                    ],
                    "label": {
                        "party": "IBM",
                        "nature": "Obligation"
                    }
                },
                {
                    "modification": "removed",
                    "provenance_ids": [
                        "111",
                        "2222"
                    ],
                    "label": {
                        "party": "Exclusion",
                        "nature": "End User"
                    }
                }
            ]
        },
        "text": "1. IBM will provide a Senior Managing Consultant / expert resource, for up to 80 hours, to assist Florida Power & Light (FPL) with the creation of an IT infrastructure unit cost model for existing infrastructure.",
        "feedback_type": "element_classification",
        "updated_labels": {
            "categories": [
                {
                    "modification": "unchanged",
                    "label": "Responsibilities"
                },
                {
                    "modification": "added",
                    "label": "Audits"
                }
            ],
            "types": [
                {
                    "modification": "unchanged",
                    "label": {
                        "party": "IBM",
                        "nature": "Obligation"
                    }
                },
                {
                    "modification": "added",
                    "label": {
                        "party": "Buyer",
                        "nature": "Disclaimer"
                    }
                }
            ]
        },
        "model_version": "11.00",
        "location": {
            "begin": "214",
            "end": "237"
        },
        "document": {
            "hash": "",
            "title": "doc title"
        }
        },
    "created": "2018-11-16T22:57:14+0000"
}


batch = {
    "function": "html_conversion",
    "status": "completed",
    "updated": "2018-11-12T21:02:43.867+0000",
    "document_counts": {
        "successful": 4,
        "failed": 0,
        "total": 4,
        "pending": 0
    },
    "created": "2018-11-12T21:02:38.907+0000",
    "input_bucket_location": "us-south",
    "input_bucket_name": "compare-comply-integration-test-bucket-input",
    "batch_id": "xxx",
    "output_bucket_name": "compare-comply-integration-test-bucket-output",
    "model": "contracts",
    "output_bucket_location": "us-south"
}

def get_access_token():
    access_token_layout = {
        "username": "dummy",
        "role": "Admin",
        "permissions": [
            "administrator",
            "manage_catalog"
        ],
        "sub": "admin",
        "iss": "sss",
        "aud": "sss",
        "uid": "sss",
        "iat": 3600,
        "exp": int(time.time())
    }

    access_token = jwt.encode(access_token_layout, 'secret', algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})
    return access_token.decode('utf-8')

class TestCompareComplyV1(TestCase):

    @classmethod
    def setUp(cls):
        iam_url = "https://iam.cloud.ibm.com/identity/token"
        iam_token_response = {
            "access_token": get_access_token(),
            "token_type": "Bearer",
            "expires_in": 3600,
            "expiration": 1524167011,
            "refresh_token": "jy4gl91BQ"
        }
        responses.add(
            responses.POST, url=iam_url, body=json.dumps(iam_token_response), status=200)

    @responses.activate
    def test_convert_to_html(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/html_conversion')

        response = {
            "hash": "0d9589556c16fca21c64ce9c8b10d065",
            "html": "<html><html>",
            "num_pages": "4",
            "publication_date": "2018-11-10",
            "title": "Microsoft Word - contract_A.doc"
        }

        responses.add(
            responses.POST,
            url,
            body=json.dumps(response),
            status=200,
            content_type='application/json')

        with open(
            os.path.join(os.path.dirname(__file__),
                         '../../resources/contract_A.pdf'), 'rb') as file:
            service.convert_to_html(
                file,
                model_id="contracts",
                file_content_type="application/octet-stream")

        assert len(responses.calls) == 2

    @responses.activate
    def test_classify_elements(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/element_classification')

        response = [{
            "text":
            "__November 9, 2018______________ date",
            "categories": [],
            "location": {
                "begin": 19373,
                "end": 19410
            },
            "types": [],
            "attributes": [{
                "text": "November 9, 2018",
                "type": "DateTime",
                "location": {
                    "begin": 19375,
                    "end": 19391
                }
            }]
        }]

        responses.add(
            responses.POST,
            url,
            body=json.dumps(response),
            status=200,
            content_type='application/json')

        with open(os.path.join(os.path.dirname(__file__),
                               '../../resources/contract_A.pdf'), 'rb') as file:
            service.classify_elements(
                file,
                model_id="contracts",
                file_content_type="application/octet-stream")

        assert len(responses.calls) == 2

    @responses.activate
    def test_extract_tables(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/tables')

        response = {
            "model_version":
            "0.2.8-SNAPSHOT",
            "model_id":
            "tables",
            "document": {
                "hash": "0906a4721a59ffeaf2ec12997aa4f7f7",
                "title": "Design and build accessible PDF tables, sample tables"
            },
            "tables": [{
                "section_title": {
                    "text": "Sample tables ",
                    "location": {
                        "begin": 2099,
                        "end": 2113
                    }
                },
                "text":
                "Column header (TH) Column header (TH) Column header (TH) Row header (TH) Data cell (TD) Data cell (TD) Row header(TH) Data cell (TD) Data cell (TD) ",
                "table_headers": [],
                "row_headers": [],
                "location": {
                    "begin": 2832,
                    "end": 4801
                },
                "body_cells": [],
            }]
        }

        responses.add(
            responses.POST,
            url,
            body=json.dumps(response),
            status=200,
            content_type='application/json')

        with open(os.path.join(os.path.dirname(__file__),
                               '../../resources/sample-tables.pdf'), 'rb') as file:
            service.extract_tables(file)

        assert len(responses.calls) == 2

    @responses.activate
    def test_compare_documents(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/comparison')

        response = {
            "aligned_elements": [
                {
                    "element_pair": [{
                        "text":
                        "WITNESSETH: that the Owner and Contractor undertake and agree as follows:",
                        "types": [],
                        "document_label":
                        "file_1",
                        "attributes": [],
                        "categories": [],
                        "location": {
                            "begin": 3845,
                            "end": 4085
                        }
                    }, {
                        "text":
                        "WITNESSETH: that the Owner and Contractor undertake and agree as follows:",
                        "types": [],
                        "document_label":
                        "file_2",
                        "attributes": [],
                        "categories": [],
                        "location": {
                            "begin": 3846,
                            "end": 4086
                        }
                    }],
                    "provenance_ids":
                    ["1mSG/96z1wY4De35LAExJzhCo2t0DfvbYnTl+vbavjY="],
                },
            ],
            "model_id":
            "contracts",
            "model_version":
            "1.0.0"
        }

        responses.add(
            responses.POST,
            url,
            body=json.dumps(response),
            status=200,
            content_type='application/json')

        with open(os.path.join(os.path.dirname(__file__),
                               '../../resources/contract_A.pdf'), 'rb') as file1:
            with open(os.path.join(os.path.dirname(__file__),
                                   '../../resources/contract_B.pdf'), 'rb') as file2:
                service.compare_documents(file1, file2)

        assert len(responses.calls) == 2

    @responses.activate
    def test_add_feedback(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/feedback')

        feedback_data = {
            "feedback_type": "element_classification",
            "document": {
                "hash": "",
                "title": "doc title"
            },
            "model_id": "contracts",
            "model_version": "11.00",
            "location": {
                "begin": "214",
                "end": "237"
            },
            "text": "1. IBM will provide a Senior Managing Consultant / expert resource, for up to 80 hours, to assist Florida Power & Light (FPL) with the creation of an IT infrastructure unit cost model for existing infrastructure.",
            "original_labels": {
                "types": [
                    {
                        "label": {
                            "nature": "Obligation",
                            "party": "IBM"
                        },
                        "provenance_ids": [
                            "85f5981a-ba91-44f5-9efa-0bd22e64b7bc",
                            "ce0480a1-5ef1-4c3e-9861-3743b5610795"
                        ]
                    },
                    {
                        "label": {
                            "nature": "End User",
                            "party": "Exclusion"
                        },
                        "provenance_ids": [
                            "85f5981a-ba91-44f5-9efa-0bd22e64b7bc",
                            "ce0480a1-5ef1-4c3e-9861-3743b5610795"
                        ]
                    }
                ],
                "categories": [
                    {
                        "label": "Responsibilities",
                        "provenance_ids": []
                    },
                    {
                        "label": "Amendments",
                        "provenance_ids": []
                    }
                ]
            },
            "updated_labels": {
                "types": [
                    {
                        "label": {
                            "nature": "Obligation",
                            "party": "IBM"
                        }
                    },
                    {
                        "label": {
                            "nature": "Disclaimer",
                            "party": "Buyer"
                        }
                    }
                ],
                "categories": [
                    {
                        "label": "Responsibilities"
                    },
                    {
                        "label": "Audits"
                    }
                ]
            }
        }

        responses.add(
            responses.POST,
            url,
            body=json.dumps(feedback),
            status=200,
            content_type='application/json')

        result = service.add_feedback(
            feedback_data,
            "wonder woman",
            "test commment").get_result()
        assert result["feedback_id"] == "lala"

        assert len(responses.calls) == 2

    @responses.activate
    def test_get_feedback(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/feedback/xxx')

        responses.add(
            responses.GET,
            url,
            body=json.dumps(feedback),
            status=200,
            content_type='application/json')

        result = service.get_feedback("xxx").get_result()
        assert result["feedback_id"] == "lala"

        assert len(responses.calls) == 2

    @responses.activate
    def test_list_feedback(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/feedback')

        responses.add(
            responses.GET,
            url,
            body=json.dumps({"feedback":[feedback]}),
            status=200,
            content_type='application/json')

        result = service.list_feedback().get_result()
        assert result["feedback"][0]["feedback_id"] == "lala"

        assert len(responses.calls) == 2

    @responses.activate
    def test_delete_feedback(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/feedback/xxx')

        response = {
            "status": 200,
            "message": "Successfully deleted the feedback with id  - 90ae2cb9-e6c5-43eb-a70f-199959f76019"
        }

        responses.add(
            responses.DELETE,
            url,
            body=json.dumps(response),
            status=200,
            content_type='application/json')

        result = service.delete_feedback("xxx").get_result()
        assert result["status"] == 200

        assert len(responses.calls) == 2

    @responses.activate
    def test_create_batch(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/batches')

        responses.add(
            responses.POST,
            url,
            body=json.dumps(batch),
            status=200,
            content_type='application/json')

        with open(os.path.join(os.path.dirname(__file__),
                               '../../resources/dummy-storage-credentials.json'), 'rb') as input_credentials_file:
            with open(os.path.join(os.path.dirname(__file__),
                                   '../../resources/dummy-storage-credentials.json'), 'rb') as output_credentials_file:
                result = service.create_batch(
                    "html_conversion",
                    input_credentials_file,
                    "us-south",
                    "compare-comply-integration-test-bucket-input",
                    output_credentials_file,
                    "us-south",
                    "compare-comply-integration-test-bucket-output").get_result()

        assert result["batch_id"] == "xxx"
        assert len(responses.calls) == 2

    @responses.activate
    def test_get_batch(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/batches/xxx')

        responses.add(
            responses.GET,
            url,
            body=json.dumps(batch),
            status=200,
            content_type='application/json')

        result = service.get_batch("xxx").get_result()
        assert result["batch_id"] == "xxx"

        assert len(responses.calls) == 2

    @responses.activate
    def test_list_batches(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/batches')

        responses.add(
            responses.GET,
            url,
            body=json.dumps({"batches": [batch]}),
            status=200,
            content_type='application/json')

        result = service.list_batches().get_result()
        assert result["batches"][0]["batch_id"] == "xxx"

        assert len(responses.calls) == 2

    @responses.activate
    def test_update_batch(self):
        service = ibm_watson.CompareComplyV1(
            '2016-10-20', iam_apikey='bogusapikey')

        url = "{0}{1}".format(base_url, '/v1/batches/xxx')

        responses.add(
            responses.PUT,
            url,
            body=json.dumps(batch),
            status=200,
            content_type='application/json')

        result = service.update_batch("xxx", "rescan").get_result()
        assert result["batch_id"] == "xxx"
        assert len(responses.calls) == 2
