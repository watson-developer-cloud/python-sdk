import json
import watson_developer_cloud

authorization = watson_developer_cloud.AuthorizationV1(username='YOUR SERVICE USERNAME',
                                                       password='YOUR SERVICE PASSWORD')

print(json.dumps(authorization.get_token(url=watson_developer_cloud.SpeechToTextV1.default_url), indent=2))
