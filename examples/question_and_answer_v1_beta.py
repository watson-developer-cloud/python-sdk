import json
from watson_developer_cloud import QuestionAndAnswerV1Beta as QuestionAndAnswer


question_and_answer = QuestionAndAnswer(username='YOUR SERVICE USERNAME',
                                        password='YOUR SERVICE PASSWORD')

print(json.dumps(question_and_answer.datasets(), indent=2))

print(json.dumps(question_and_answer.ask(
    'Where is the hottest place on earth?', dataset='travel', items=1), indent=2))
