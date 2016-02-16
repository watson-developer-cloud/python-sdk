import json
from watson_developer_cloud import ToneAnalyzerV3Beta as ToneAnalyzer


tone_analyzer = ToneAnalyzer(username='YOUR SERVICE USERNAME',
                             password='YOUR SERVICE PASSWORD',
                             version='2016-02-11')

print(json.dumps(tone_analyzer.tone(text='I am very happy'), indent=2))
