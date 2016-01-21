import json
from watson_developer_cloud import RetrieveAndRankV1 as RetrieveAndRank


retrieve_and_rank = RetrieveAndRank(username='YOUR SERVICE USERNAME',
                                    password='YOUR SERVICE PASSWORD')

rankers = retrieve_and_rank.list_rankers()
print(json.dumps(rankers, indent=2))

# create a ranker
# with open('../resources/ranker_training_data.csv', 'rb') as training_data:
#     print(json.dumps(retrieve_and_rank.create_ranker(training_data=training_data, name='Ranker Test'), indent=2))

# replace YOUR RANKER ID
status = retrieve_and_rank.get_ranker_status('42AF7Ex10-rank-47')
print(json.dumps(status, indent=2))

# delete_results = retrieve_and_rank.delete_ranker('YOUR RANKER ID')
# print(json.dumps(delete_results))

# replace '42AF7Ex10-rank-47' with your ranker_id
with open('../resources/ranker_answer_data.csv', 'rb') as answer_data:
    ranker_results = retrieve_and_rank.rank('42AF7Ex10-rank-47', answer_data)
    print(json.dumps(ranker_results, indent=2))
