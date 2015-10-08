import responses
import watson_developer_cloud


@responses.activate
def test_success():
    create_url = 'https://gateway.watsonplatform.net/concept-expansion-beta/api/v1/upload'
    create_response = '{"jobid": "2014"}'

    responses.add(responses.POST, create_url, body=create_response,
                  status=200, content_type='application/json')

    status_url = 'https://gateway.watsonplatform.net/concept-expansion-beta/api/v1/status?jobid=2014'
    status_response = '{"state": "D"}'

    responses.add(responses.GET, status_url, body=status_response, status=200, content_type='application/json',
                  match_querystring=True)

    results_url = 'https://gateway.watsonplatform.net/concept-expansion-beta/api/v1/result'
    results_response = '{"return_seeds": [{"prevalence": 1, "result": "*"}, {"prevalence": 2, "result": "+"}]}'

    responses.add(responses.PUT, results_url, body=results_response,
                  status=200, content_type='application/json')

    concept_expansion = watson_developer_cloud.ConceptExpansionV1Beta(
        username="username", password="password")
    job_id = concept_expansion.create_job(dataset='mtsamples', seeds=['motrin', 'tylenol', 'aspirin'],
                                          label='medications')

    concept_expansion.get_status(job_id)
    concept_expansion.get_results(job_id)

    assert len(responses.calls) == 3
    assert responses.calls[0].request.url == create_url
    assert responses.calls[0].response.text == create_response
    assert responses.calls[1].request.url == status_url
    assert responses.calls[1].response.text == status_response
    assert responses.calls[2].request.url == results_url
    assert responses.calls[2].response.text == results_response

test_success()
