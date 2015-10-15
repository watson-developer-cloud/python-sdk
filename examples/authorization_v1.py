import json
from watson_developer_cloud import AuthorizationV1 as Authorization
from watson_developer_cloud import SpeechToTextV1 as SpeechToText

authorization = Authorization(username='YOUR SERVICE USERNAME',
                              password='YOUR SERVICE PASSWORD')

print(json.dumps(authorization.get_token(url=SpeechToText.default_url), indent=2))
