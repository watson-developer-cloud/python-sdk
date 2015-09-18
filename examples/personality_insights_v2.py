import json
import watson_developer_cloud


personality_insights = watson_developer_cloud.PersonalityInsightsV2()

with open('../resources/personality.txt') as personality_text:
    print(json.dumps(personality_insights.profile(text=personality_text.read()), indent=2))

# with open('../resources/personality.txt') as personality_text:
#     personality_insights_json = {"contentItems": [
#         {"id": "245160944223793152", "userid": "bob", "sourceid": "twitter", "created": 1427720427,
#          "updated": 1427720427, "contenttype": "text/plain", "charset": "UTF-8", "language": "en-us",
#          "content": personality_text.read(), "parentid": "", "reply": "false", "forward": "false"}]}
#     print(json.dumps(personality_insights.profile(text=personality_insights_json), indent=2))

# with open('../resources/personality.es.txt') as personality_text:
#     print(json.dumps(personality_insights.profile(text=personality_text.read(), language='es'), indent=2))
