# coding=utf-8
import json
import time
from watson_developer_cloud import ConceptExpansionV1Beta


concept_expansion = ConceptExpansionV1Beta(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

job_id = concept_expansion.create_job(
    dataset='mtsamples', seeds=['motrin', 'tylenol', 'aspirin'], label='medications')
print(json.dumps(job_id, indent=2))

time.sleep(5)  # sleep for 5 seconds
job_status = concept_expansion.get_status(job_id)

while job_status['status'] == 'in progress' or job_status['status'] == 'awaiting work':
    time.sleep(5)  # sleep for 5 seconds
    job_status = concept_expansion.get_status(job_id)
    print(json.dumps(job_status, indent=2))

if job_status['status'] == 'done':
    results = concept_expansion.get_results(job_id)
    print(json.dumps(results, indent=2))
