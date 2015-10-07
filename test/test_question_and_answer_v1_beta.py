# coding=utf-8
import responses
import watson_developer_cloud


@responses.activate
def test_success():
    datasets_url = 'https://gateway.watsonplatform.net/question-and-answer-beta/api/v1/services'
    datasets_response = '[{"description": "Watson for the Travel Domain", "id": "travel", "name": ' \
                        '"Travel Content Lab"}, {"description": "Watson for the Healthcare Domain", "id": ' \
                        '"healthcare", "name": "Healthcare Content Lab"}]'

    responses.add(responses.GET, datasets_url,
                  body=datasets_response, status=200,
                  content_type='application/json')

    question_and_answer = watson_developer_cloud.QuestionAndAnswerV1Beta(
        username="username", password="password")
    question_and_answer.datasets()

    assert responses.calls[0].request.url == datasets_url
    assert responses.calls[0].response.text == datasets_response

    question_request_text = 'what is hiv'
    question_request_dataset = 'healthcare'
    question_url = 'https://gateway.watsonplatform.net/question-and-answer-beta/api/v1/question/healthcare'
    question_response = '[{"question": {"category": "", "status": "Complete", "passthru": "", "formattedAnswer":' \
                        ' false, "evidencelist": []}}]'

    responses.add(responses.POST, question_url,
                  body=question_response, status=200,
                  content_type='application/json')

    question_and_answer.ask(
        question_request_text, dataset=question_request_dataset, items=1)

    assert responses.calls[1].request.url == question_url
    assert responses.calls[1].response.text == question_response

    assert len(responses.calls) == 2
