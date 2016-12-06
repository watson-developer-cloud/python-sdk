# coding=utf-8
import os,json
import responses
import watson_developer_cloud

@responses.activate
def test_success():
    models_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/models'
    models_response = '{"models": [{"url": "https://stream.watsonplatform.net/speech-to-text/api/v1/models/' \
                      'WatsonModel", "rate": 16000, "name": "WatsonModel", "language": "en-US", "description": ' \
                      '"Watson model \'v7w_134k.3\' for Attila 2-5 reco engine."}]}'

    responses.add(responses.GET, models_url,
                  body=models_response, status=200,
                  content_type='application/json')

    speech_to_text = watson_developer_cloud.SpeechToTextV1(
        username="username", password="password")
    speech_to_text.models()

    assert responses.calls[0].request.url == models_url
    assert responses.calls[0].response.text == models_response

    recognize_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
    recognize_response = '{"results":[{"alternatives":[{"transcript":"thunderstorms could produce large hail ' \
                         'isolated tornadoes and heavy rain "}],"final":true}],"result_index":0}'

    responses.add(responses.POST, recognize_url,
                  body=recognize_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/speech.wav'), 'rb') as audio_file:
        speech_to_text.recognize(
            audio_file, content_type='audio/l16; rate=44100')

    request_url = responses.calls[1].request.url
    assert request_url == recognize_url + '?continuous=false'
    assert responses.calls[1].response.text == recognize_response

    assert len(responses.calls) == 2

@responses.activate
def test_get_model():
    model_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/models/modelid'
    responses.add(responses.GET, model_url,
                  body='{"bogus_response": "yep"}', status=200,
                  content_type='application/json')
    speech_to_text = watson_developer_cloud.SpeechToTextV1(
        username="username", password="password")
    speech_to_text.get_model(model_id='modelid')
    assert len(responses.calls) == 1

@responses.activate
def test_custom_model():

    posted_data = """{\"name\": \"Example model\",
  \"base_model_name\": \"en-US_BroadbandModel\",
  \"description\": \"Example custom language model\"}"
"https://stream.watsonplatform.net/speech-to-text/api/v1/customizations"""

    customization_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations'
    responses.add(responses.GET, customization_url,
                  body='{"get response": "yep"}', status=200,
                  content_type='application/json')

    responses.add(responses.POST, customization_url,
                  body='{"bogus_response": "yep"}', status=200,
                  content_type='application/json')

    responses.add(responses.GET, "{0}/modelid".format(customization_url),
                  body='{"bogus_response": "yep"}', status=200,
                  content_type='application/json')

    responses.add(responses.DELETE, "{0}/modelid".format(customization_url),
                  body='{"bogus_response": "yep"}', status=200,
                  content_type='application/json')

    speech_to_text = watson_developer_cloud.SpeechToTextV1(
        username="username", password="password")

    speech_to_text.list_custom_models()

    speech_to_text.create_custom_model(name="Example model", base_model="en-US_BroadbandModel",
                                       description="Example custom language model")

    parsed_body = json.loads(responses.calls[1].request.body)
    assert parsed_body['name'] == 'Example model'

    speech_to_text.create_custom_model(name="Example model Two")

    parsed_body = json.loads(responses.calls[2].request.body)
    assert parsed_body['name'] == 'Example model Two'
    assert parsed_body['description'] == ''
    assert parsed_body['base_model_name'] == 'en-US_BroadbandModel'

    speech_to_text.get_custom_model(modelid='modelid')
    speech_to_text.delete_custom_model(modelid='modelid')

    assert len(responses.calls) == 5

