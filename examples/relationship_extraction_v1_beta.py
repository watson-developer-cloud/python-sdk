import watson_developer_cloud


relationship_extraction = watson_developer_cloud.RelationshipExtractionV1Beta()

print(relationship_extraction.extract("Hello from IBM Watson"))
