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
        username="username", password="password")

    responses.add(responses.POST, convert_url,
                  body=convert_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/simple.html'), 'r') as document:
        config = {'conversion_target': watson_developer_cloud.DocumentConversionV1.NORMALIZED_HTML}
        document_conversion.convert_document(
            document=document, config=config, media_type='text/html')

    assert responses.calls[
               1].request.url == convert_url
    assert responses.calls[1].response.text == convert_response

    assert len(responses.calls) == 2

    index_url = 'https://gateway.watsonplatform.net/document-conversion/api/v1/index_document'
    index_response = '{"status": "success"}'

    responses.add(responses.POST, index_url,
                  body=index_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/simple.html'), 'r') as document:
        config = {
            'retrieve_and_rank': {
                'dry_run':'false',
                'service_instance_id':'serviceInstanceId',
                'cluster_id':'clusterId',
                'search_collection':'searchCollectionName'
            }
        }
        document_conversion.index_document(
            config=config, document=document)

    assert responses.calls[
               1].request.url == index_url
    assert responses.calls[1].response.text == index_response

    assert len(responses.calls) == 2
