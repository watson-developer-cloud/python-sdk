from __future__ import print_function
import json
import os
from watson_developer_cloud import TradeoffAnalyticsV1

tradeoff_analytics = TradeoffAnalyticsV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

with open(os.path.join(os.path.dirname(__file__),
                       '../resources/problem.json')) as problem_json:
    dilemma = tradeoff_analytics.dilemmas(json.load(problem_json),
                                          generate_visualization=True,
                                          find_preferable_options=True)

print(json.dumps(dilemma, indent=2))
