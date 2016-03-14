import json
from watson_developer_cloud import AuthorizationV1
from watson_developer_cloud import SpeechToTextV1

authorization = AuthorizationV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

print(json.dumps(authorization.get_token(url=SpeechToTextV1.default_url), indent=2))
