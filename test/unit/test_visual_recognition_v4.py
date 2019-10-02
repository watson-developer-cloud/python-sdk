# (C) Copyright IBM Corp. 2019.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import ibm_watson
import responses
import json
import os
import jwt
import time
import pytest
from unittest import TestCase
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.visual_recognition_v4 import AnalyzeEnums, FileWithMetadata

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/visual-recognition/api'
base_url = '{0}{1}'.format(platform_url, service_path)


def get_access_token():
    access_token_layout = {
        "username": "dummy",
        "role": "Admin",
        "permissions": ["administrator", "manage_catalog"],
        "sub": "admin",
        "iss": "sss",
        "aud": "sss",
        "uid": "sss",
        "iat": 3600,
        "exp": int(time.time())
    }

    access_token = jwt.encode(
        access_token_layout,
        'secret',
        algorithm='HS256',
        headers={'kid': '230498151c214b788dd97f22b85410a5'})
    return access_token.decode('utf-8')


class TestVisualRecognitionV4(TestCase):

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
        responses.add(responses.POST,
                      url=iam_url,
                      body=json.dumps(iam_token_response),
                      status=200)

    #########################
    # analysis
    #########################

    @responses.activate
    def test_analyze(self):
        endpoint = '/v4/analyze'
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "images": [{
                "objects": {
                    "collections": [{
                        "collection_id":
                            "collection_id",
                        "objects": [{
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }, {
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }]
                    }, {
                        "collection_id":
                            "collection_id",
                        "objects": [{
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }, {
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }]
                    }]
                },
                "source": {
                    "archive_filename": "archive_filename",
                    "filename": "filename",
                    "type": "file",
                    "resolved_url": "resolved_url",
                    "source_url": "source_url"
                },
                "errors": {
                    "code":
                        "invalid_field",
                    "message":
                        "The date provided for `version` is not valid. Specify dates in `YYYY-MM-DD` format.",
                    "more_info":
                        "https://cloud.ibm.com/apidocs/visual-recognition-v4#versioning",
                    "target": {
                        "type": "parameter",
                        "name": "version"
                    }
                },
                "dimensions": {
                    "width": 6,
                    "height": 0
                }
            }, {
                "objects": {
                    "collections": [{
                        "collection_id":
                            "collection_id",
                        "objects": [{
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }, {
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }]
                    }, {
                        "collection_id":
                            "collection_id",
                        "objects": [{
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }, {
                            "score": 7.0614014,
                            "location": {
                                "top": 1,
                                "left": 5,
                                "width": 5,
                                "height": 2
                            },
                            "object": "object"
                        }]
                    }]
                },
                "source": {
                    "archive_filename": "archive_filename",
                    "filename": "filename",
                    "type": "file",
                    "resolved_url": "resolved_url",
                    "source_url": "source_url"
                },
                "errors": {
                    "code":
                        "invalid_field",
                    "message":
                        "The date provided for `version` is not valid. Specify dates in `YYYY-MM-DD` format.",
                    "more_info":
                        "https://cloud.ibm.com/apidocs/visual-recognition-v4#versioning",
                    "target": {
                        "type": "parameter",
                        "name": "version"
                    }
                },
                "dimensions": {
                    "width": 6,
                    "height": 0
                }
            }],
            "trace":
                "trace",
            "warnings": [{
                "code": "invalid_field",
                "more_info": "more_info",
                "message": "message"
            }, {
                "code": "invalid_field",
                "more_info": "more_info",
                "message": "message"
            }]
        }
        responses.add(responses.POST,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        with open(
                os.path.join(os.path.dirname(__file__),
                             '../../resources/cars.zip'), 'rb') as cars:
            detailed_response = service.analyze(
                collection_ids=['collection_id1, collection_id2'],
                features=[AnalyzeEnums.Features.OBJECTS.value],
                images_file=[FileWithMetadata(cars)],
                image_url=[
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/American_Eskimo_Dog.jpg/1280px-American_Eskimo_Dog.jpg'
                ],
                threshold='0.2')
        result = detailed_response.get_result()
        assert result is not None
        assert len(responses.calls) == 2

    #########################
    # collections
    #########################

    @responses.activate
    def test_create_collection(self):
        endpoint = '/v4/collections'
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "collection_id": "collection_id",
            "training_status": {
                "objects": {
                    "in_progress": "true",
                    "data_changed": "true",
                    "ready": "true",
                    "latest_failed": "true",
                    "description": "description"
                }
            },
            "created": "2000-01-23T04:56:07.000+00:00",
            "name": "name",
            "description": "description",
            "image_count": 0,
            "updated": "2000-01-23T04:56:07.000+00:00"
        }
        responses.add(responses.POST,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')
        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)
        detailed_response = service.create_collection(name='name',
                                                      description='description')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

    @responses.activate
    def test_list_collections(self):
        endpoint = '/v4/collections'
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "collections": [{
                "collection_id": "collection_id",
                "training_status": {
                    "objects": {
                        "in_progress": "true",
                        "data_changed": "true",
                        "ready": "true",
                        "latest_failed": "true",
                        "description": "description"
                    }
                },
                "created": "2000-01-23T04:56:07.000+00:00",
                "name": "name",
                "description": "description",
                "image_count": 0,
                "updated": "2000-01-23T04:56:07.000+00:00"
            }, {
                "collection_id": "collection_id",
                "training_status": {
                    "objects": {
                        "in_progress": "true",
                        "data_changed": "true",
                        "ready": "true",
                        "latest_failed": "true",
                        "description": "description"
                    }
                },
                "created": "2000-01-23T04:56:07.000+00:00",
                "name": "name",
                "description": "description",
                "image_count": 0,
                "updated": "2000-01-23T04:56:07.000+00:00"
            }]
        }
        responses.add(responses.GET,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.list_collections()
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

    @responses.activate
    def test_get_collection(self):
        endpoint = '/v4/collections/{0}'.format('collection_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "collection_id": "collection_id",
            "training_status": {
                "objects": {
                    "in_progress": "true",
                    "data_changed": "true",
                    "ready": "true",
                    "latest_failed": "true",
                    "description": "description"
                }
            },
            "created": "2000-01-23T04:56:07.000+00:00",
            "name": "name",
            "description": "description",
            "image_count": 0,
            "updated": "2000-01-23T04:56:07.000+00:00"
        }
        responses.add(responses.GET,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.get_collection(
            collection_id='collection_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

    @responses.activate
    def test_update_collection(self):
        endpoint = '/v4/collections/{0}'.format('collection_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "collection_id": "collection_id",
            "training_status": {
                "objects": {
                    "in_progress": "true",
                    "data_changed": "true",
                    "ready": "true",
                    "latest_failed": "true",
                    "description": "description"
                }
            },
            "created": "2000-01-23T04:56:07.000+00:00",
            "name": "name",
            "description": "description",
            "image_count": 0,
            "updated": "2000-01-23T04:56:07.000+00:00"
        }
        responses.add(responses.POST,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.update_collection(
            collection_id='collection_id',
            name='name',
            description='description')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

    @responses.activate
    def test_delete_collection(self):
        endpoint = '/v4/collections/{0}'.format('collection_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {}
        responses.add(responses.DELETE,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.delete_collection(
            collection_id='collection_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.delete_collection()

    # #########################
    # # images
    # #########################

    @responses.activate
    def test_add_images(self):
        endpoint = '/v4/collections/{0}/images'.format('collection_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "images": [{
                "training_data": {
                    "objects": [{
                        "location": {
                            "top": 1,
                            "left": 5,
                            "width": 5,
                            "height": 2
                        },
                        "object": "object"
                    }, {
                        "location": {
                            "top": 1,
                            "left": 5,
                            "width": 5,
                            "height": 2
                        },
                        "object": "object"
                    }]
                },
                "created": "2000-01-23T04:56:07.000+00:00",
                "source": {
                    "archive_filename": "archive_filename",
                    "filename": "filename",
                    "type": "file",
                    "resolved_url": "resolved_url",
                    "source_url": "source_url"
                },
                "image_id": "image_id",
                "updated": "2000-01-23T04:56:07.000+00:00",
                "errors": {
                    "code":
                        "invalid_field",
                    "message":
                        "The date provided for `version` is not valid. Specify dates in `YYYY-MM-DD` format.",
                    "more_info":
                        "https://cloud.ibm.com/apidocs/visual-recognition-v4#versioning",
                    "target": {
                        "type": "parameter",
                        "name": "version"
                    }
                },
                "dimensions": {
                    "width": 6,
                    "height": 0
                }
            }, {
                "training_data": {
                    "objects": [{
                        "location": {
                            "top": 1,
                            "left": 5,
                            "width": 5,
                            "height": 2
                        },
                        "object": "object"
                    }, {
                        "location": {
                            "top": 1,
                            "left": 5,
                            "width": 5,
                            "height": 2
                        },
                        "object": "object"
                    }]
                },
                "created": "2000-01-23T04:56:07.000+00:00",
                "source": {
                    "archive_filename": "archive_filename",
                    "filename": "filename",
                    "type": "file",
                    "resolved_url": "resolved_url",
                    "source_url": "source_url"
                },
                "image_id": "image_id",
                "updated": "2000-01-23T04:56:07.000+00:00",
                "errors": {
                    "code":
                        "invalid_field",
                    "message":
                        "The date provided for `version` is not valid. Specify dates in `YYYY-MM-DD` format.",
                    "more_info":
                        "https://cloud.ibm.com/apidocs/visual-recognition-v4#versioning",
                    "target": {
                        "type": "parameter",
                        "name": "version"
                    }
                },
                "dimensions": {
                    "width": 6,
                    "height": 0
                }
            }],
            "trace":
                "trace",
            "warnings": [{
                "code": "invalid_field",
                "more_info": "more_info",
                "message": "message"
            }, {
                "code": "invalid_field",
                "more_info": "more_info",
                "message": "message"
            }]
        }
        responses.add(responses.POST,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.add_images(collection_id='collection_id',
                                               image_url='image_url',
                                               training_data='training_data')

        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.add_images()

    @responses.activate
    def test_list_images(self):
        endpoint = '/v4/collections/{0}/images'.format('collection_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "images": [{
                "image_id": "image_id",
                "updated": "2000-01-23T04:56:07.000+00:00"
            }, {
                "image_id": "image_id",
                "updated": "2000-01-23T04:56:07.000+00:00"
            }]
        }
        responses.add(responses.GET,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.list_images(collection_id='collection_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.list_images()

    @responses.activate
    def test_get_image_details(self):
        endpoint = '/v4/collections/{0}/images/{1}'.format(
            'collection_id', 'image_id').format('image_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "training_data": {
                "objects": [{
                    "location": {
                        "top": 1,
                        "left": 5,
                        "width": 5,
                        "height": 2
                    },
                    "object": "object"
                }, {
                    "location": {
                        "top": 1,
                        "left": 5,
                        "width": 5,
                        "height": 2
                    },
                    "object": "object"
                }]
            },
            "created": "2000-01-23T04:56:07.000+00:00",
            "source": {
                "archive_filename": "archive_filename",
                "filename": "filename",
                "type": "file",
                "resolved_url": "resolved_url",
                "source_url": "source_url"
            },
            "image_id": "image_id",
            "updated": "2000-01-23T04:56:07.000+00:00",
            "errors": {
                "code":
                    "invalid_field",
                "message":
                    "The date provided for `version` is not valid. Specify dates in `YYYY-MM-DD` format.",
                "more_info":
                    "https://cloud.ibm.com/apidocs/visual-recognition-v4#versioning",
                "target": {
                    "type": "parameter",
                    "name": "version"
                }
            },
            "dimensions": {
                "width": 6,
                "height": 0
            }
        }
        responses.add(responses.GET,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.get_image_details(
            collection_id='collection_id', image_id='image_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.get_image_details()

    @responses.activate
    def test_delete_image(self):
        endpoint = '/v4/collections/{0}/images/{1}'.format(
            'collection_id', 'image_id').format('image_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {}
        responses.add(responses.DELETE,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.delete_image(collection_id='collection_id',
                                                 image_id='image_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.delete_image()

    @responses.activate
    def test_get_jpeg_image(self):
        endpoint = '/v4/collections/{0}/images/{1}/jpeg'.format(
            'collection_id', 'image_id').format('image_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {}
        responses.add(responses.GET,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.get_jpeg_image(
            collection_id='collection_id', image_id='image_id', size='size')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.get_jpeg_image()

    #########################
    # training
    #########################

    @responses.activate
    def test_train(self):
        endpoint = '/v4/collections/{0}/train'.format('collection_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "collection_id": "collection_id",
            "training_status": {
                "objects": {
                    "in_progress": "true",
                    "data_changed": "true",
                    "ready": "true",
                    "latest_failed": "true",
                    "description": "description"
                }
            },
            "created": "2000-01-23T04:56:07.000+00:00",
            "name": "name",
            "description": "description",
            "image_count": 0,
            "updated": "2000-01-23T04:56:07.000+00:00"
        }
        responses.add(responses.POST,
                      url,
                      body=json.dumps(response),
                      status=202,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.train(collection_id='collection_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.train()

    @responses.activate
    def test_add_image_training_data(self):
        endpoint = '/v4/collections/{0}/images/{1}/training_data'.format(
            'collection_id', 'image_id')
        url = '{0}{1}'.format(base_url, endpoint)
        response = {
            "objects": [{
                "location": {
                    "top": 1,
                    "left": 5,
                    "width": 5,
                    "height": 2
                },
                "object": "object"
            }, {
                "location": {
                    "top": 1,
                    "left": 5,
                    "width": 5,
                    "height": 2
                },
                "object": "object"
            }]
        }
        responses.add(responses.POST,
                      url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.add_image_training_data(
            collection_id='collection_id', image_id='image_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.add_image_training_data()

    #########################
    # userData
    #########################

    @responses.activate
    def test_delete_user_data(self):
        endpoint = '/v4/user_data'
        url = '{0}{1}'.format(base_url, endpoint)
        response = {}
        responses.add(responses.DELETE,
                      url,
                      body=json.dumps(response),
                      status=202,
                      content_type='')

        authenticator = IAMAuthenticator('bogusapikey')
        service = ibm_watson.VisualRecognitionV4('YYYY-MM-DD',
                                                 authenticator=authenticator)
        service.set_service_url(base_url)

        detailed_response = service.delete_user_data(customer_id='customer_id')
        result = detailed_response.get_result()
        assert len(responses.calls) == 2

        with pytest.raises(TypeError):
            service.delete_user_data()
