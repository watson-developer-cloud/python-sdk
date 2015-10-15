import json
from watson_developer_cloud import ToneAnalyzerV2Experimental as ToneAnalyzer


tone_analyzer = ToneAnalyzer(username='YOUR SERVICE USERNAME',
                             password='YOUR SERVICE PASSWORD')


print(json.dumps(tone_analyzer.scorecards(), indent=2))

print(json.dumps(tone_analyzer.synonyms(word='happy'), indent=2))

print(json.dumps(tone_analyzer.tone(text='Hello how are you?'), indent=2))
