import json
import watson_developer_cloud


question_and_answer = watson_developer_cloud.QuestionAndAnswerV1Beta()

print(json.dumps(question_and_answer.datasets(), indent=2))

print(json.dumps(question_and_answer.ask('Where is the hottest place on earth?', dataset='travel', items=1), indent=2))
