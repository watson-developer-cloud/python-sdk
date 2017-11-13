# coding=utf-8
import os
import json
import pytest
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
    assert request_url == recognize_url
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


def _decode_body(body):
    try:
        return body.decode('utf-8')
    except:
        return body


@responses.activate
def test_custom_model():
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

    parsed_body = json.loads(_decode_body(responses.calls[1].request.body))
    assert parsed_body['name'] == 'Example model'

    speech_to_text.create_custom_model(name="Example model Two")

    parsed_body = json.loads(_decode_body(responses.calls[2].request.body))
    assert parsed_body['name'] == 'Example model Two'
    assert parsed_body['description'] == ''
    assert parsed_body['base_model_name'] == 'en-US_BroadbandModel'

    speech_to_text.get_custom_model(modelid='modelid')
    speech_to_text.delete_custom_model(modelid='modelid')

    assert len(responses.calls) == 5


def test_custom_corpora():

    corpora_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/{0}/corpora'
    get_corpora_url = '{0}/{1}'.format(
        corpora_url.format('customid'), 'corpus')

    with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
        rsps.add(responses.GET, corpora_url.format('customid'),
                 body='{"get response": "yep"}', status=200,
                 content_type='application/json')

        rsps.add(responses.POST, get_corpora_url,
                 body='{"get response": "yep"}',
                 status=200,
                 content_type='application/json')

        rsps.add(responses.GET, get_corpora_url,
                 body='{"get response": "yep"}',
                 status=200,
                 content_type='application/json')

        rsps.add(responses.DELETE, get_corpora_url,
                 body='{"get response": "yep"}',
                 status=200,
                 content_type='application/json')

        speech_to_text = watson_developer_cloud.SpeechToTextV1(
            username="username", password="password")

        speech_to_text.list_corpora(customization_id='customid')

        file_path = '../resources/speech_to_text/corpus-short-1.txt'
        full_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(full_path) as corpus_file:
            speech_to_text.add_corpus(customization_id='customid',
                                      corpus_name="corpus", file_data=corpus_file)

        speech_to_text.get_corpus(customization_id='customid',
                                  corpus_name='corpus')

        speech_to_text.delete_corpus(customization_id='customid',
                                     corpus_name='corpus')


@responses.activate
def test_custom_words():
    words_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/{0}/words'
    word_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/{0}/words/{1}'

    responses.add(responses.POST, word_url.format('custid', 'IEEE'),
                  body='{"get response": "yep"}',
                  status=200,
                  content_type='application/json')

    responses.add(responses.DELETE, word_url.format('custid', 'IEEE'),
                  body='{"get response": "yep"}',
                  status=200,
                  content_type='application/json')

    responses.add(responses.GET, word_url.format('custid', 'IEEE'),
                  body='{"get response": "yep"}',
                  status=200,
                  content_type='application/json')

    responses.add(responses.POST, words_url.format('custid'),
                  body='{"get response": "yep"}',
                  status=200,
                  content_type='application/json')

    responses.add(responses.GET, words_url.format('custid'),
                  body='{"get response": "yep"}',
                  status=200,
                  content_type='application/json')

    speech_to_text = watson_developer_cloud.SpeechToTextV1(
        username="username", password="password")

    custom_word = speech_to_text.CustomWord(word="IEEE",
                                            sounds_like=["i triple e"],
                                            display_as="IEEE")

    speech_to_text.add_custom_word(customization_id='custid',
                                   custom_word=custom_word)

    speech_to_text.delete_custom_word(customization_id='custid',
                                      custom_word=custom_word)

    speech_to_text.delete_custom_word(customization_id='custid',
                                      custom_word='IEEE')

    custom_words = [custom_word, custom_word, custom_word]
    speech_to_text.add_custom_words(customization_id='custid',
                                    custom_words=custom_words)

    speech_to_text.get_custom_word(customization_id='custid',
                                   custom_word="IEEE")

    speech_to_text.get_custom_word(customization_id='custid',
                                   custom_word=custom_word)

    speech_to_text.list_custom_words(customization_id='custid')
    speech_to_text.list_custom_words(
        customization_id='custid', sort='alphabetical')
    with pytest.raises(KeyError) as keyerror:
        speech_to_text.list_custom_words(
            customization_id='custid', sort='badsort')
    assert 'sort must be alphabetical or count' in str(keyerror.value)

    speech_to_text.list_custom_words(
        customization_id='custid', word_type='all')

    with pytest.raises(KeyError) as keyerror:
        speech_to_text.list_custom_words(
            customization_id='custid', word_type='badwordtype')
    assert 'word type must be all, user, or corpora' in str(keyerror.value)

    assert len(responses.calls) == 9
