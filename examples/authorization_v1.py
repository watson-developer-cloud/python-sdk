import json
import watson_developer_cloud.AuthorizationV1 as Authorization
import watson_developer_cloud.SpeechToTextV1 as SpeechToText

authorization = Authorization(username='YOUR SERVICE USERNAME',
                              password='YOUR SERVICE PASSWORD')

print(json.dumps(authorization.get_token(url=SpeechToText.default_url), indent=2))
