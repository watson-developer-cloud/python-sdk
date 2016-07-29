import os
import responses
import watson_developer_cloud

CLUSTER_ID = 'sc0747112c_f978_4e1f_b97e_0e3a8101ac5b'
URL_CLUSTERS = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters'
URL_CLUSTER = URL_CLUSTERS + '/' + CLUSTER_ID

RANKER_ID = '3b140ax14-rank-10383'
URL_RANKERS = 'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/rankers'
URL_RANKER = URL_RANKERS + '/' + RANKER_ID

retrieve_and_rank = watson_developer_cloud.RetrieveAndRankV1(username="username",
                                                             password="password")

@responses.activate
def test_list_rankers():

    listrank_response = '{"rankers":[{"ranker_id":"3b140ax14-rank-10383","name":"pythonRank"}]}'

    responses.add(responses.GET, URL_RANKERS,
              match_querystring=True,
              body=listrank_response, status=200,
              content_type='application/json')

    ranker_list = retrieve_and_rank.list_rankers()

    assert ranker_list is not None
    assert len(ranker_list['rankers']) == 1
    assert responses.calls[0].request.url == URL_RANKERS
    assert responses.calls[0].response.text == listrank_response


@responses.activate
def test_ranker_status():

    statusrank_response = '{"ranker_id":"3b140ax14-rank-10383","name":"pythonRank","status":"Available"}'

    responses.add(responses.GET, URL_RANKER,
                  match_querystring=True,
                  body=statusrank_response, status=200,
                  content_type='application/json')

    ranker_status = retrieve_and_rank.get_ranker_status(RANKER_ID)

    assert ranker_status is not None
    assert ranker_status['status'] is not None
    assert responses.calls[0].request.url == URL_RANKER
    assert responses.calls[0].response.text == statusrank_response


@responses.activate
def test_rank():

    rank_url = URL_RANKER + '/rank'
    rank_response =  '{"ranker_id":"3b140ax14-rank-10383",' \
                     '"top_answer":"30965a00-5415-4ef5-8e4a-bb21a7aeab44", "answers":[' \
                     '{"answer_id":"30965a00-5415-4ef5-8e4a-bb21a7aeab44","score":180.0,"confidence":0.2636349925008873},' \
                     '{"answer_id":"30965a00-5415-4ef5-8e4a-bb21a7aeab44","score":178.0,"confidence":0.25972667610243827}]}'

    responses.add(responses.POST, rank_url,
                  match_querystring=True,
                  body=rank_response, status=200,
                  content_type='application/json')

    ranker_answer = None

    with open(os.path.join(os.path.dirname(__file__), '../resources/ranker_answer_data.csv'), 'rb') as answer_data:
        ranker_answer = retrieve_and_rank.rank('3b140ax14-rank-10383', answer_data=answer_data, top_answers=3)

    assert ranker_answer is not None
    assert responses.calls[0].request.url == rank_url
    assert responses.calls[0].response.text == rank_response


@responses.activate
def test_create_ranker():

    createrank_response = '{"ranker_id":"3b140ax14-rank-10383","name":"pythonRank","status":"Training"}'

    responses.add(responses.POST, URL_RANKERS,
                  match_querystring=True,
                  body=createrank_response, status=200,
                  content_type='application/json')

    ranker = None
    with open(os.path.join(os.path.dirname(__file__), '../resources/ranker_training_data.csv'), 'rb') as training_data:
        ranker = retrieve_and_rank.create_ranker(training_data=training_data, name='pythonRank')

    assert ranker is not None
    assert ranker['ranker_id'] == RANKER_ID
    assert ranker['name'] == 'pythonRank'
    assert responses.calls[0].request.url == URL_RANKERS
    assert responses.calls[0].response.text == createrank_response


@responses.activate
def test_delete_ranker():
    removerank_response = '{}'

    responses.add(responses.DELETE, URL_RANKER,
                  match_querystring=True,
                  body=removerank_response, status=200,
                  content_type='application/json')

    retrieve_and_rank.delete_ranker(RANKER_ID)

    assert responses.calls[0].request.url == URL_RANKER
    assert responses.calls[0].response.text == removerank_response

@responses.activate
def test_list_cluster():
    listcluster_response = '{"clusters":[{"solr_cluster_id":"sc0747112c_f978_4e1f_b97e_0e3a8101ac5b","cluster_name":"","cluster_size":"","solr_cluster_status":"READY"}]}'

    responses.add(responses.GET, URL_CLUSTERS,
              match_querystring=True,
              body=listcluster_response, status=200,
              content_type='application/json')

    clusters = retrieve_and_rank.list_solr_clusters()

    assert clusters is not None
    assert responses.calls[0].request.url == URL_CLUSTERS
    assert responses.calls[0].response.text == listcluster_response

@responses.activate
def test_create_cluster():
    createcluster_response = '{"solr_cluster_id":"sc0747112c_f978_4e1f_b97e_0e3a8101ac5b","cluster_name":"","cluster_size":"","solr_cluster_status":"NOT_AVAILABLE"}'

    responses.add(responses.POST, URL_CLUSTERS,
              match_querystring=True,
              body=createcluster_response, status=200,
              content_type='application/json')

    retrieve_and_rank.create_solr_cluster(cluster_name='pythonCluster', cluster_size=None)

    assert responses.calls[0].request.url == URL_CLUSTERS
    assert responses.calls[0].response.text == createcluster_response

@responses.activate
def test_delete_cluster():
    removecluster_response = '{"message":"WRRCSR023: Successfully deleted Solr cluster [sc0747112c_f978_4e1f_b97e_0e3a8101ac5b].","statusCode":200}'

    responses.add(responses.DELETE, URL_CLUSTER,
                  body=removecluster_response, status=200,
                  match_querystring=True,
                  content_type='application/json')

    retrieve_and_rank.delete_solr_cluster(CLUSTER_ID)

    assert responses.calls[0].request.url == URL_CLUSTER
    assert responses.calls[0].response.text == removecluster_response

@responses.activate
def test_cluster_status():
    statuscluster_response = '{"solr_cluster_id":"sc0747112c_f978_4e1f_b97e_0e3a8101ac5b","cluster_name":"","cluster_size":"","solr_cluster_status":"READY"}'

    responses.add(responses.GET, URL_CLUSTER,
                  body=statuscluster_response, status=200,
                  match_querystring=True,
                  content_type='application/json')

    cluster_status = retrieve_and_rank.get_solr_cluster_status(CLUSTER_ID)

    assert cluster_status is not None
    assert responses.calls[0].request.url == URL_CLUSTER
    assert responses.calls[0].response.text == statuscluster_response

@responses.activate
def test_list_config():
    listconfigs_url = URL_CLUSTER + '/config'
    listconfigs_response = '{"solr_configs":[]}'

    responses.add(responses.GET, listconfigs_url,
                  body=listconfigs_response, status=200,
                  match_querystring=True,
                  content_type='application/json')

    config_list = retrieve_and_rank.list_configs(CLUSTER_ID)

    assert config_list is not None
    assert responses.calls[0].request.url == listconfigs_url
    assert responses.calls[0].response.text == listconfigs_response

@responses.activate
def test_create_config():
    createconfig_url = URL_CLUSTER + '/config/exampleconfig'
    createconfig_response = '{"message":"WRRCSR026: Successfully uploaded named config [example-config] for Solr cluster [sc0747112c_f978_4e1f_b97e_0e3a8101ac5b].","statusCode":200}'

    responses.add(responses.POST, createconfig_url,
                  body=createconfig_response, status=200,
                  match_querystring=True,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/solr_config.zip'), 'rb') as config_data:
        config = retrieve_and_rank.create_config(CLUSTER_ID, 'exampleconfig',   config=config_data)

    assert config is not None
    assert responses.calls[00].request.url == createconfig_url
    assert responses.calls[00].response.text == createconfig_response

@responses.activate
def test_delete_config():
    removeconfig_url = URL_CLUSTER + '/config/exampleconfig'
    removeconfig_response = '{"message":"WRRCSR025: Successfully deleted named config [example-config] for Solr cluster [sc0747112c_f978_4e1f_b97e_0e3a8101ac5b]].","statusCode":200}'

    responses.add(responses.DELETE, removeconfig_url,
                  body=removeconfig_response, status=200,
                  match_querystring=True,
                  content_type='application/json')

    response = retrieve_and_rank.delete_config(CLUSTER_ID, 'exampleconfig')

    assert response is not None
    assert responses.calls[0].request.url == removeconfig_url
    assert responses.calls[0].response.text == removeconfig_response

@responses.activate
def test_get_config():
    getconfig_url = URL_CLUSTER + '/config/exampleconfig'
    getconfig_response = '{}'

    responses.add(responses.GET, getconfig_url,
                  match_querystring=True,
                  body=getconfig_response, status=200)

    retrieve_and_rank.get_config(CLUSTER_ID, 'exampleconfig')

    assert responses.calls[0].request.url == getconfig_url
    assert responses.calls[0].response.text == getconfig_response

@responses.activate
def test_list_collections():
    listcollection_url = URL_CLUSTER + '/solr/admin/collections?action=LIST&wt=json'

    listcollection_response = '{"responseHeader":{"status":0,"QTime":0},"collections":["examplecollection"]}'

    responses.add(responses.GET, listcollection_url,
                  match_querystring=True,
                  body=listcollection_response, status=200,
                  content_type='application/json')

    retrieve_and_rank.list_collections(CLUSTER_ID)

    assert responses.calls[0].response.text == listcollection_response

@responses.activate
def test_create_collection():
    createcollection_url = URL_CLUSTER + '/solr/admin/collections?action=CREATE&wt=json&collection.configName=exampleconfig&name=examplecollection'
    createcollection_response = '{}'

    responses.add(responses.POST, createcollection_url,
                  match_querystring=True,
                  body=createcollection_response, status=200,
                  content_type='application/json')

    collection = retrieve_and_rank.create_collection(CLUSTER_ID, 'examplecollection',  'exampleconfig')

    assert collection is not None
    assert responses.calls[0].response.text == createcollection_response

@responses.activate
def test_delete_collection():
    deletecollection_url = URL_CLUSTER + '/solr/admin/collections?action=DELETE&wt=json&name=examplecollection'
    deletecollection_response = '{}'

    responses.add(responses.POST, deletecollection_url,
                  body=deletecollection_response, status=200,
                  match_querystring=True,
                  content_type='application/json')

    retrieve_and_rank.delete_collection(CLUSTER_ID, 'examplecollection', None)

    assert responses.calls[0].response.text == deletecollection_response

@responses.activate
def test_get_solr_client():
    solr_client = retrieve_and_rank.get_pysolr_client(CLUSTER_ID, 'examplecollection')
    assert solr_client is not None
