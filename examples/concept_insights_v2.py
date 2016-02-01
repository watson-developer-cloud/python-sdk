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

# concept = concept_insights.get_concept('IBM')
# print(json.dumps(concept, indent=2))

# concepts = concept_insights.search_concept_by_label('cognitive', concept_fields={'link': 1, 'type': 1})
# print(json.dumps(concepts, indent=2))

# concepts = concept_insights.get_related_concepts(['IBM_Watson', 'Business'])
# print(json.dumps(concepts, indent=2))

# relation_scores = concept_insights.get_relation_scores('IBM', ['Mainframe_computer', 'Web_services',
#                                                                'Java_programming_language'])
# print(json.dumps(relation_scores, indent=2))

# corpora = concept_insights.list_corpora()
# print (json.dumps(corpora, indent=2))

# corpus = concept_insights.get_corpus('ibmresearcher', account='public')
# print(json.dumps(corpus, indent=2))

corpus = concept_insights.create_corpus('test_corpus', ttl_hours=25)
print(corpus)

delete_results = concept_insights.delete_corpus('test_corpus')
print(delete_results)
