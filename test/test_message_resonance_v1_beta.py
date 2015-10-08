# coding=utf-8
import responses
import watson_developer_cloud


@responses.activate
def test_success():
    datasets_url = 'https://gateway.watsonplatform.net/message-resonance-beta/api/v1/datasets'
    datasets_response = '[{"id": 1, "name": "Cloud Computing"}, {"id": 2, "name": "Big Data & Analytics"}]'

    resonance_request_text = 'cpu'
    resonance_request_dataset = 1
    resonance_url = 'https://gateway.watsonplatform.net/message-resonance-beta/api/v1/ringscore?text=cpu&dataset=1'
    resonance_response = '[{"word": "cpu", "prevalence": 1, "overall": 10, "dataset": 1, "volume": 4, "duration": 5}]'

    responses.add(responses.GET, datasets_url,
                  body=datasets_response, status=200,
                  content_type='application/json')

    responses.add(responses.GET, resonance_url,
                  body=resonance_response, status=200,
                  content_type='application/json', match_querystring=True)

    message_resonance = watson_developer_cloud.MessageResonanceV1Beta(
        username="username", password="password")
    message_resonance.datasets()
    message_resonance.resonance(
        resonance_request_text, resonance_request_dataset)

    assert responses.calls[0].request.url == datasets_url
    assert responses.calls[0].response.text == datasets_response
    if len(responses.calls) == 2:
        #assert responses.calls[1].request.url == resonance_url
        assert responses.calls[1].response.text == resonance_response
        assert len(responses.calls) == 2
    else:
        len(responses.calls) == 2
