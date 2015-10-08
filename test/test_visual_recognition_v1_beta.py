import os
import responses
import watson_developer_cloud


@responses.activate
def test_success():
    labels_url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v1/tag/labels'
    labels_response_body = '{"labels": ["Non_Scene", "Scene"], "label_groups": ["Activities (facet)", "Activity"]}'

    responses.add(responses.GET, labels_url,
                  body=labels_response_body, status=200,
                  content_type='application/json')

    visual_recognition = watson_developer_cloud.VisualRecognitionV1Beta(
        username="username", password="password")
    visual_recognition.labels()

    assert responses.calls[0].request.url == labels_url
    assert responses.calls[0].response.text == labels_response_body

    recognize_url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v1/tag/recognize'
    recognize_response = '{"images":[{"image_id":"0","labels":[{"label_name":"Indoors","label_score":"0.692818"},' \
                         '{"label_name":"Room","label_score":"0.547413"}],"image_name":"test.jpg"}]}'

    responses.add(responses.POST, recognize_url,
                  body=recognize_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/test.jpg'), 'rb') as image_file:
        visual_recognition.recognize(
            image_file, labels_to_check={'label_groups': ['Indoors']})

    assert responses.calls[1].request.url == recognize_url
    assert responses.calls[1].response.text == recognize_response

    assert len(responses.calls) == 2
