import json
import os
from os.path import join, dirname
from watson_developer_cloud import TradeoffAnalyticsV1 as TradeoffAnalytics


tradeoff_analytics = TradeoffAnalytics(username='YOUR SERVICE USERNAME',
                                       password='YOUR SERVICE PASSWORD')

with open(join(dirname(__file__), '../resources/problem.json')) as data_file:
    problem_data = json.load(data_file)
print(json.dumps(tradeoff_analytics.dilemmas(problem_data), indent=2))
