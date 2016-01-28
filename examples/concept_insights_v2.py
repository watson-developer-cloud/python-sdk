# coding=utf-8
import json
from watson_developer_cloud import ConceptInsightsV2 as ConceptInsights


concept_insights = ConceptInsights(username='YOUR SERVICE USERNAME',
                                   password='YOUR SERVICE PASSWORD')

# accounts = concept_insights.get_accounts_info()
# print(json.dumps(accounts, indent=2))

# graphs = concept_insights.get_graphs()
# print(json.dumps(graphs, indent=2))

# annotations = concept_insights.annotate_text('IBM Watson won the Jeopardy television show hosted by Alex Trebek')
# print(json.dumps(annotations, indent=2))

concept = concept_insights.get_concept('IBM')
print(json.dumps(concept, indent=2))
