# coding=utf-8
import json
from watson_developer_cloud import ConceptInsightsV2


concept_insights = ConceptInsightsV2(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

accounts = concept_insights.get_accounts_info()
print(json.dumps(accounts, indent=2))

graphs = concept_insights.get_graphs()
print(json.dumps(graphs, indent=2))

annotations = concept_insights.annotate_text('IBM Watson won the Jeopardy television show hosted by Alex Trebek')
print(json.dumps(annotations, indent=2))

concept = concept_insights.get_concept('IBM')
print(json.dumps(concept, indent=2))

concepts = concept_insights.search_concept_by_label('cognitive', concept_fields={'link': 1, 'type': 1})
print(json.dumps(concepts, indent=2))

concepts = concept_insights.get_related_concepts(['IBM_Watson', 'Business'])
print(json.dumps(concepts, indent=2))

relation_scores = concept_insights.get_relation_scores('IBM', ['Mainframe_computer', 'Web_services',
                                                               'Java_programming_language'])
print(json.dumps(relation_scores, indent=2))

corpora = concept_insights.list_corpora()
print (json.dumps(corpora, indent=2))

corpora = concept_insights.list_corpora(account='public')
print (json.dumps(corpora, indent=2))


corpus = concept_insights.get_corpus('ibmresearcher', account='public')
print(json.dumps(corpus, indent=2))

# creation_response = concept_insights.create_corpus('test_corpus', ttl_hours=25)
# print(creation_response)

corpus_state = concept_insights.get_corpus_processing_state('ibmresearcher', account='public')
print(json.dumps(corpus_state, indent=2))

corpus_stats = concept_insights.get_corpus_stats('ibmresearcher', account='public')
print(json.dumps(corpus_stats, indent=2))

corpus = concept_insights.get_corpus('ibmresearcher', account='public')
print(json.dumps(corpus, indent=2))

# update_response = concept_insights.update_corpus_metadata('test_corpus', users=corpus['users'],  ttl_hours=26)
# print(update_response)

# delete_response = concept_insights.delete_corpus('test_corpus')
# print(delete_response)

document_labels = concept_insights.search_corpus_by_label('TEDTalks', account='public', query='John', prefix=True)
print(json.dumps(document_labels, indent=2))

related_concepts = concept_insights.get_corpus_related_concepts('ibmresearcher', account='public', limit=3)
print(json.dumps(related_concepts, indent=2))

# Showing abbreviated and full concept referencing
relation_scores = concept_insights.get_corpus_relation_scores('ibmresearcher', account='public', concepts=[
    'Artificial_intelligence', '/graphs/wikipedia/en-20120601/concepts/Botany'
])
print(json.dumps(relation_scores, indent=2))

related_documents = concept_insights.get_corpus_related_documents('ibmresearcher', account='public', limit=1, ids=[
    '/corpora/public/TEDTalks/documents/2',
    '/graphs/wikipedia/en-20120601/concepts/Artificial_intelligence'
])
print(json.dumps(related_documents, indent=2))

documents = concept_insights.list_documents('ibmresearcher', account='public')
print(json.dumps(documents, indent=2))

document = concept_insights.get_document('TEDTalks', document='2', account='public')
print(json.dumps(document, indent=2))

document_annotations = concept_insights.get_document_annotations('TEDTalks', document='2', account='public')
print(json.dumps(document_annotations, indent=2))

document_processing_state = concept_insights.get_document_processing_state('TEDTalks', document='2', account='public')
print(json.dumps(document_processing_state, indent=2))

document_related_concepts = concept_insights.get_document_related_concepts('TEDTalks', document='2', account='public')
print(json.dumps(document_related_concepts, indent=2))

document_relation_scores = concept_insights.get_document_relation_scores(
    'ibmresearcher', document='us-etm', concepts=['Artificial_intelligence',
                                                  '/graphs/wikipedia/en-20120601/concepts/Botany'], account='public')
print(json.dumps(document_relation_scores, indent=2))

# test_document = {
#     'label': 'Test document with custom fields',
#     'user_fields': {
#       'latitude': 41.1329599,
#       'longitude': -73.7492039
#     },
#     'parts': [
#       {
#         'name': 'test-partOne',
#         'content-type': 'text/plain',
#         'data': 'Text data'
#       }
#     ]
#   }

# creation_response = concept_insights.create_document('test_corpus', 'test_document', test_document)
# print(creation_response)

# update_response = concept_insights.update_document('test_corpus', 'test_document', test_document)
# print(update_response)

# delete_response = concept_insights.delete_document('test_corpus', 'test_document')
# print(delete_response)
