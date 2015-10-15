# coding=utf-8
import json
from watson_developer_cloud import ConceptInsightsV2 as ConceptInsights


concept_insights = ConceptInsights(username='YOUR SERVICE USERNAME',
                                   password='YOUR SERVICE PASSWORD')

print(json.dumps(concept_insights.get_accounts_info(), indent=2))
