import json
import watson_developer_cloud


tone_analyzer = watson_developer_cloud.ToneAnalyzerV1Experimental()


print(json.dumps(tone_analyzer.scorecards(), indent=2))

print(json.dumps(tone_analyzer.synonym(words=['happy']), indent=2))

print(json.dumps(tone_analyzer.tone(text='Hello how are you?'), indent=2))
