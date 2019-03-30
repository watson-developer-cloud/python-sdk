import json
from ibm_watson import AuthorizationV1
from ibm_watson import SpeechToTextV1

authorization = AuthorizationV1(
    username='YOUR SERVICE USERNAME', password='YOUR SERVICE PASSWORD')

print(
    json.dumps(
        authorization.get_token(url=SpeechToTextV1.default_url), indent=2))
