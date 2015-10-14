# coding=utf-8
import json
import watson_developer_cloud.ConceptInsightsV2 as ConceptInsights


concept_insights = ConceptInsights(username='YOUR SERVICE USERNAME',
                                   password='YOUR SERVICE PASSWORD')

print(json.dumps(concept_insights.get_accounts_info(), indent=2))
