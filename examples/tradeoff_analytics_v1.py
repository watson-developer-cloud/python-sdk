import json
import os
import watson_developer_cloud


tradeoff_analytics = watson_developer_cloud.TradeoffAnalyticsV1()

with open(os.path.join(os.path.dirname(__file__), '../resources/problem.json')) as data_file:
    problem_data = json.load(data_file)
print(json.dumps(tradeoff_analytics.dilemmas(problem_data), indent=2))
