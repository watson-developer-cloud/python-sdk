import json
from watson_developer_cloud import RelationshipExtractionV1Beta


relationship_extraction = RelationshipExtractionV1Beta(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

print(json.dumps(relationship_extraction.extract("Hello from IBM Watson", return_type='json'), indent=2))
