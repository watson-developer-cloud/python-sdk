import os
import responses
import watson_developer_cloud

@responses.activate
def test_success():
    
# Ranker endpoints
    retrieve_and_rank = watson_developer_cloud.RetrieveAndRankV1(username="username",
                                                                 password="password")

    listrank_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/rankers'
    listrank_response = '{"rankers":[{"ranker_id":"3b140ax14-rank-10383","url":"https://gateway.watsonplatform.net/retrieve-and-rank' \
                    '/api/v1/rankers/3b140ax14-rank-10383","name":"pythonRank","created":"2016-07-15T19:11:27.801Z"}]}'
                    
    responses.add(responses.GET, listrank_url,
              body=listrank_response, status=200,
              content_type='application/json')

    retrieve_and_rank.list_rankers()
    
    assert responses.calls[0].request.url == listrank_url
    assert responses.calls[0].response.text == listrank_response

    statusrank_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/rankers/3b140ax14-rank-10383'
    statusrank_response = '{"ranker_id":"3b140ax14-rank-10383","name":"pythonRank","created":"2016-07-15T19:11:27.801Z",' \
                      '"url":"https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/rankers/3b140ax14-rank-10383",' \
                      '"status":"Available","status_description":"The ranker instance is now available and is ready to take ranker requests."}'
 
    responses.add(responses.GET, statusrank_url,
                  body=statusrank_response, status=200,
                  content_type='application/json')
 
    retrieve_and_rank.get_ranker_status('3b140ax14-rank-10383')
    
    assert responses.calls[1].request.url == statusrank_url
    assert responses.calls[1].response.text == statusrank_response
 
    rank_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/rankers/3b140ax14-rank-10383/rank'
    rank_response =  '{"ranker_id":"3b140ax14-rank-10383","url":"https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/rankers/3b140ax14-rank-10383",' \
                     '"top_answer":"30965a00-5415-4ef5-8e4a-bb21a7aeab44", "answers":[' \
                     '{"answer_id":"30965a00-5415-4ef5-8e4a-bb21a7aeab44","score":180.0,"confidence":0.2636349925008873},' \
                     '{"answer_id":"30965a00-5415-4ef5-8e4a-bb21a7aeab44","score":179.0,"confidence":0.262185794730098},' \
                     '{"answer_id":"30965a00-5415-4ef5-8e4a-bb21a7aeab44","score":178.0,"confidence":0.25972667610243827}]}'
 
    responses.add(responses.POST, rank_url,
                  body=rank_response, status=200,
                  content_type='application/json')
 
    with open(os.path.join(os.path.dirname(__file__), '../resources/ranker_answer_data.csv'), 'rb') as answer_data:
        retrieve_and_rank.rank('3b140ax14-rank-10383', answer_data=answer_data, top_answers=3)
 
    assert responses.calls[2].request.url == rank_url
    assert responses.calls[2].response.text == rank_response
 
    createrank_url = listrank_url
    createrank_response = '{"ranker_id":"3b140ax14-rank-10544","name":"pythonRank","created":"2016-07-19T15:19:28.485Z",' \
                      '"url":"https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/rankers/3b140ax14-rank-10544",' \
                      '"status":"Training","status_description":"The ranker instance is in its training phase, not yet ready to accept rank requests"}'

    responses.add(responses.POST, createrank_url,
                  body=createrank_response, status=200,
                  content_type='application/json')
    
    with open(os.path.join(os.path.dirname(__file__), '../resources/ranker_training_data.csv'), 'rb') as training_data:
        retrieve_and_rank.create_ranker(training_data=training_data, name='pythonRank')
  
    assert responses.calls[3].request.url == createrank_url
    assert responses.calls[3].response.text == createrank_response
 
    removerank_url = statusrank_url
    removerank_response = '{}'
 
    responses.add(responses.DELETE, removerank_url,
                  body=removerank_response, status=200,
                  content_type='application/json')
 
    retrieve_and_rank.delete_ranker('3b140ax14-rank-10383')
 
    assert responses.calls[4].request.url == removerank_url
    assert responses.calls[4].response.text == removerank_response
 
    assert len(responses.calls) == 5
    
# Retrieve endpoints
    listcluster_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters'
    listcluster_response = '{"clusters":[{"solr_cluster_id":"sc0747112c_f978_4e1f_b97e_0e3a8101ac5b","cluster_name":"","cluster_size":"","solr_cluster_status":"READY"}]}'
                    
    responses.add(responses.GET, listcluster_url,
              body=listcluster_response, status=200,
              content_type='application/json')

    retrieve_and_rank.list_solr_clusters()
    
    assert responses.calls[5].request.url == listcluster_url
    assert responses.calls[5].response.text == listcluster_response

    createcluster_url = listcluster_url
    createcluster_response = '{"solr_cluster_id":"sc0747112c_f978_4e1f_b97e_0e3a8101ac5b","cluster_name":"","cluster_size":"","solr_cluster_status":"NOT_AVAILABLE"}'
                    
    responses.add(responses.POST, createcluster_url,
              body=createcluster_response, status=200,
              content_type='application/json')

    retrieve_and_rank.create_solr_cluster(cluster_name='pythonCluster', cluster_size=None)
    
    assert responses.calls[6].request.url == createcluster_url
    assert responses.calls[6].response.text == createcluster_response   

    removecluster_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/sc0747112c_f978_4e1f_b97e_0e3a8101ac5b'
    removecluster_response = '{"message":"WRRCSR023: Successfully deleted Solr cluster [sc0747112c_f978_4e1f_b97e_0e3a8101ac5b].","statusCode":200}'
 
    responses.add(responses.DELETE, removecluster_url,
                  body=removecluster_response, status=200,
                  content_type='application/json')
 
    retrieve_and_rank.delete_solr_cluster('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b')
 
    assert responses.calls[7].request.url == removecluster_url
    assert responses.calls[7].response.text == removecluster_response
    
    statuscluster_url = removecluster_url
    statuscluster_response = '{"solr_cluster_id":"scecb989cb_b204_4ebd_bc8d_c2244a499d8c","cluster_name":"","cluster_size":"","solr_cluster_status":"READY"}'
 
    responses.add(responses.GET, statuscluster_url,
                  body=statuscluster_response, status=200,
                  content_type='application/json')
 
    retrieve_and_rank.get_solr_cluster_status('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b')
 
    assert responses.calls[8].request.url == statuscluster_url
    assert responses.calls[8].response.text == statuscluster_response       
    
    listconfigs_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/sc0747112c_f978_4e1f_b97e_0e3a8101ac5b/config'
    listconfigs_response = '{"solr_configs":[]}'
 
    responses.add(responses.GET, listconfigs_url,
                  body=listconfigs_response, status=200,
                  content_type='application/json')
 
    retrieve_and_rank.list_configs('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b')
 
    assert responses.calls[9].request.url == listconfigs_url
    assert responses.calls[9].response.text == listconfigs_response       

    createconfig_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/sc0747112c_f978_4e1f_b97e_0e3a8101ac5b/config/exampleconfig'
    createconfig_response = '{"message":"WRRCSR026: Successfully uploaded named config [example-config] for Solr cluster [sc0747112c_f978_4e1f_b97e_0e3a8101ac5b].","statusCode":200}'
 
    responses.add(responses.POST, createconfig_url,
                  body=createconfig_response, status=200,
                  content_type='application/json')
     
    with open(os.path.join(os.path.dirname(__file__), '../resources/solr_config.zip'), 'rb') as config_data:
        retrieve_and_rank.create_config('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b', 'exampleconfig',   config=config_data)
   
    assert responses.calls[10].request.url == createconfig_url
    assert responses.calls[10].response.text == createconfig_response

    removeconfig_url = createconfig_url
    removeconfig_response = '{"message":"WRRCSR025: Successfully deleted named config [example-config] for Solr cluster [sc0747112c_f978_4e1f_b97e_0e3a8101ac5b]].","statusCode":200}'
                         
    responses.add(responses.DELETE, removeconfig_url,
                  body=removeconfig_response, status=200,
                  content_type='application/json')
 
    retrieve_and_rank.delete_config('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b', 'exampleconfig')
 
    assert responses.calls[11].request.url == removeconfig_url
    assert responses.calls[11].response.text == removeconfig_response

    getconfig_url = createconfig_url
    getconfig_response = '% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current' \
                         '                               Dload  Upload   Total   Spent    Left  Speed' \
                         '100   864    0   864    0     0   1627      0 --:--:-- --:--:-- --:--:--  1627'
                         
    responses.add(responses.GET, getconfig_url,
                  body=getconfig_response, status=200,
                  content_type='application/json')
 
    retrieve_and_rank.get_config('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b', 'exampleconfig')
 
    assert responses.calls[12].request.url == getconfig_url
    assert responses.calls[12].response.text == getconfig_response

    listcollection_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/sc0747112c_f978_4e1f_b97e_0e3a8101ac5b/solr/admin/collections'
    listcollection1_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/sc0747112c_f978_4e1f_b97e_0e3a8101ac5b/solr/admin/collections?wt=json&action=LIST'
    listcollection_response = '{"responseHeader":{"status":0,"QTime":0},"collections":["examplecollection"]}'
                         
    responses.add(responses.GET, listcollection_url,
                  body=listcollection_response, status=200,
                  content_type='application/json')
  
    retrieve_and_rank.list_collections('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b')
 
# the response url changes every time the test is run   
#    assert responses.calls[13].request.url == listcollection1_url
    assert responses.calls[13].response.text == listcollection_response

    createcollection_url = listcollection_url
    createcollection1_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/sc0747112c_f978_4e1f_b97e_0e3a8101ac5b/solr/admin/collections?name=examplecollection&collection.configName=exampleconfig&wt=json&action=CREATE'
    createcollection_response = '{}'
 
    responses.add(responses.POST, createcollection_url,
                  body=createcollection_response, status=200,
                  content_type='application/json')
     
    retrieve_and_rank.create_collection('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b', 'examplecollection',  'exampleconfig')

#    assert responses.calls[14].request.url == createcollection1_url
    assert responses.calls[14].response.text == createcollection_response

    deletecollection_url = listcollection_url
    deletecollection1_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/sc0747112c_f978_4e1f_b97e_0e3a8101ac5b/solr/admin/collections?wt=json&name=examplecollection&action=DELETE'
    deletecollection_response = '{}'
 
    responses.add(responses.POST, deletecollection_url,
                  body=deletecollection_response, status=200,
                  content_type='application/json')
     
    retrieve_and_rank.delete_collection('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b', 'examplecollection',  'exampleconfig')
  
#   assert responses.calls[15].request.url == deletecollection1_url
    assert responses.calls[15].response.text == deletecollection_response
     
    retrieve_and_rank.get_pysolr_client('sc0747112c_f978_4e1f_b97e_0e3a8101ac5b', 'examplecollection')