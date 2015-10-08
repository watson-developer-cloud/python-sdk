import json
import watson_developer_cloud


visual_insights = watson_developer_cloud.VisualInsightsV1Experimental()

print(json.dumps(visual_insights.classifiers(), indent=2))

with open('../resources/images.zip', 'rb') as images_file:
    print(json.dumps(visual_insights.summary(images_file), indent=2))

