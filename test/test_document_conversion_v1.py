# coding=utf-8
import os
import responses
import watson_developer_cloud


@responses.activate
def test_success():
    convert_url = 'https://gateway.watsonplatform.net/document-conversion/api/v1/convert_document'
    convert_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><html>' \
                         '<head><title>Simple HTML Page</title></head>' \
                         '<body><h1>Chapter 1</h1><p>The content of the first chapter.</p></body></html>'
    document_conversion = watson_developer_cloud.DocumentConversionV1(
        username="username", password="password", version='2015-12-15')

    responses.add(responses.POST, convert_url,
                  body=convert_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/simple.html'), 'r') as document:
        convertConfig = {'conversion_target': watson_developer_cloud.DocumentConversionV1.NORMALIZED_HTML}
        document_conversion.convert_document(document=document, config=convertConfig, media_type='text/html')

    assert responses.calls[0].request.url.startswith(convert_url)
    assert responses.calls[0].response.text == convert_response

    index_url = 'https://gateway.watsonplatform.net/document-conversion/api/v1/index_document'
    index_response = '{"status": "success"}'

    responses.add(responses.POST, index_url,
                  body=index_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/example.html'), 'r') as document:
        indexConfig = {
            'retrieve_and_rank': {
                'dry_run':'false',
                'service_instance_id':'serviceInstanceId',
                'cluster_id':'clusterId',
                'search_collection':'searchCollectionName'
            }
        }
        document_conversion.index_document(config=indexConfig, document=document)

    assert responses.calls[1].request.url.startswith(index_url)
    assert responses.calls[1].response.text == index_response

    assert len(responses.calls) == 2
