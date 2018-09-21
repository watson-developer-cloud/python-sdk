from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput

# If service instance provides API key authentication
# service = ToneAnalyzerV3(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/tone-analyzer/api',
#     version='2017-09-21',
#     iam_apikey='your_apikey')

service = ToneAnalyzerV3(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/tone-analyzer/api',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2017-09-21')

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
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = service.tone(json.load(tone_json)['text'], "text/plain").get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 3:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = service.tone(
        tone_input=json.load(tone_json)['text'],
        content_type='text/plain',
        sentences=True).get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 4:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = service.tone(
        tone_input=json.load(tone_json),
        content_type='application/json').get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 5:\n")
with open(join(dirname(__file__),
               '../resources/tone-example-html.json')) as tone_html:
    tone = service.tone(
        json.load(tone_html)['text'], content_type='text/html').get_result()
print(json.dumps(tone, indent=2))

print("\ntone() example 6 with GDPR support:\n")
service.set_detailed_response(True)
with open(join(dirname(__file__),
               '../resources/tone-example-html.json')) as tone_html:
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
service.set_detailed_response(False)

print("\ntone() example 7:\n")
tone_input = ToneInput('I am very happy. It is a good day.')
tone = service.tone(tone_input=tone_input, content_type="application/json")
print(json.dumps(tone, indent=2))
