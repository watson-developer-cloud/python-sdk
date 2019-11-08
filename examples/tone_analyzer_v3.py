import json
import os
from os.path import join
from ibm_watson import ToneAnalyzerV3
from ibm_watson.tone_analyzer_v3 import ToneInput
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authentication via IAM
# authenticator = IAMAuthenticator('your_api_key')
# service = ToneAnalyzerV3(
#     version='2017-09-21',
#     authenticator=authenticator)
# service.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')

# Authentication via external config like VCAP_SERVICES
service = ToneAnalyzerV3(version='2017-09-21')
service.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')

print("\ntone_chat() example 1:\n")
utterances = [{
    'text': 'I am very happy.',
    'user': 'glenn'
}, {
    'text': 'It is a good day.',
    'user': 'glenn'
}]
tone_chat = service.tone_chat(utterances).get_result()
print(json.dumps(tone_chat, indent=2))

print("\ntone() example 1:\n")
print(
    json.dumps(
        service.tone(
            tone_input='I am very happy. It is a good day.',
            content_type="text/plain").get_result(),
        indent=2))

print("\ntone() example 2:\n")
with open(join(os.getcwd(),
               'resources/tone-example.json')) as tone_json:
    tone = service.tone(json.load(tone_json)['text'], content_type="text/plain").get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 3:\n")
with open(join(os.getcwd(),
               'resources/tone-example.json')) as tone_json:
    tone = service.tone(
        tone_input=json.load(tone_json)['text'],
        content_type='text/plain',
        sentences=True).get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 4:\n")
with open(join(os.getcwd(),
               'resources/tone-example.json')) as tone_json:
    tone = service.tone(
        tone_input=json.load(tone_json),
        content_type='application/json').get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 5:\n")
with open(join(os.getcwd(),
               'resources/tone-example-html.json')) as tone_html:
    tone = service.tone(
        json.load(tone_html)['text'],
        content_type='text/html').get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 6 with GDPR support:\n")
with open(join(os.getcwd(),
               'resources/tone-example-html.json')) as tone_html:
    tone = service.tone(
        json.load(tone_html)['text'],
        content_type='text/html',
        headers={
            'Custom-Header': 'custom_value'
        })

print(tone)
print(tone.get_headers())
print(tone.get_result())
print(tone.get_status_code())

print("\ntone() example 7:\n")
tone_input = ToneInput('I am very happy. It is a good day.')
tone = service.tone(tone_input=tone_input, content_type="application/json").get_result()
print(json.dumps(tone, indent=2))
