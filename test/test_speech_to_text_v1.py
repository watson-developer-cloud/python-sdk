# coding=utf-8
import os
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

    assert responses.calls[
        1].request.url == recognize_url + '?continuous=False'
    assert responses.calls[1].response.text == recognize_response

    assert len(responses.calls) == 2
