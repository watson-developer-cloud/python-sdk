import json
from os.path import join, dirname
from watson_developer_cloud import VisualInsightsV1Experimental


visual_insights = VisualInsightsV1Experimental(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

print(json.dumps(visual_insights.classifiers(), indent=2))

with open(join(dirname(__file__), '../resources/images.zip'), 'rb') as images_file:
    print(json.dumps(visual_insights.summary(images_file), indent=2))
