# coding=utf-8
import json
import watson_developer_cloud


concept_insights = watson_developer_cloud.ConceptInsightsV2()

print(json.dumps(concept_insights.get_accounts_info(), indent=2))
