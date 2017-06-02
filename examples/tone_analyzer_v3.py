import json
import os
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2016-05-19')

print("\ntone_chat() example 1:\n")
utterances = [{'text': 'I am very happy.', 'user': 'glenn'},
              {'text': 'It is a good day.', 'user': 'glenn'}]
print(json.dumps(tone_analyzer.tone_chat(utterances), indent=2))

print("\ntone() example 1:\n")
print(json.dumps(tone_analyzer.tone(text='I am very happy. It is a good day.'),
                 indent=2))

print("\ntone() example 2:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = tone_analyzer.tone(json.load(tone_json)['text'], 'emotion')
print(json.dumps(tone, indent=2))

print("\ntone() example 3:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = tone_analyzer.tone(json.load(tone_json)['text'], 'emotion',
                              True, 'text/plain')
print(json.dumps(tone, indent=2))

print("\ntone() example 4:\n")
with open(join(dirname(__file__),
               '../resources/tone-example.json')) as tone_json:
    tone = tone_analyzer.tone(json.load(tone_json), 'emotion',
                              content_type='application/json', )
print(json.dumps(tone, indent=2))

print("\ntone() example 5:\n")
with open(join(dirname(__file__),
               '../resources/tone-example-html.json')) as tone_json:
    tone = tone_analyzer.tone(json.load(tone_json)['text'], 'emotion',
                              content_type='text/html')
print(json.dumps(tone, indent=2))
