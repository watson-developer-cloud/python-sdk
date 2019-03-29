# coding=utf-8
import os
import json
import responses
import ibm_watson
from ibm_watson.speech_to_text_v1 import CustomWord


@responses.activate
def test_success():
    models_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/models'
    models_response = '{"models": [{"url": "https://stream.watsonplatform.net/speech-to-text/api/v1/models/' \
                      'WatsonModel", "rate": 16000, "name": "WatsonModel", "language": "en-US", "description": ' \
                      '"Watson model \'v7w_134k.3\' for Attila 2-5 reco engine."}]}'

    responses.add(
        responses.GET,
        models_url,
        body=models_response,
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")
    speech_to_text.list_models()

    assert responses.calls[0].request.url == models_url
    assert responses.calls[0].response.text == models_response

    recognize_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
    recognize_response = '{"results":[{"alternatives":[{"transcript":"thunderstorms could produce large hail ' \
                         'isolated tornadoes and heavy rain "}],"final":true}],"result_index":0}'

    responses.add(
        responses.POST,
        recognize_url,
        body=recognize_response,
        status=200,
        content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../../resources/speech.wav'), 'rb') as audio_file:
        speech_to_text.recognize(
            audio=audio_file, content_type='audio/l16; rate=44100')

    request_url = responses.calls[1].request.url
    assert request_url == recognize_url
    assert responses.calls[1].response.text == recognize_response

    with open(os.path.join(os.path.dirname(__file__), '../../resources/speech.wav'), 'rb') as audio_file:
        speech_to_text.recognize(
            audio=audio_file, customization_id='x', content_type='audio/l16; rate=44100')
    expected_url = "{0}?customization_id=x".format(recognize_url)
    assert expected_url == responses.calls[2].request.url
    assert len(responses.calls) == 3


@responses.activate
def test_get_model():
    model_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/models/modelid'
    responses.add(
        responses.GET,
        model_url,
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')
    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")
    speech_to_text.get_model(model_id='modelid')
    assert len(responses.calls) == 1


def _decode_body(body):
    try:
        return body.decode('utf-8')
    except:
        return body


@responses.activate
def test_recognitions():
    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognitions'
    get_response = '{"recognitions": [{"created": "2018-02-01T17:43:15.432Z","id": "6193190c-0777-11e8-9b4b-43ad845196dd","updated": "2018-02-01T17:43:17.998Z","status": "failed"}]}'
    responses.add(
        responses.GET,
        url,
        body=get_response,
        status=200,
        content_type='application/json')

    responses.add(
        responses.POST,
        url,
        body='{"status": "waiting"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.DELETE,
        "{0}/jobid".format(url),
        body='{"description": "deleted successfully"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        "{0}/jobid".format(url),
        body='{"status": "waiting"}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")

    speech_to_text.check_jobs()
    assert responses.calls[0].response.json()['recognitions'][0][
        'id'] == '6193190c-0777-11e8-9b4b-43ad845196dd'

    speech_to_text.check_job('jobid')
    assert responses.calls[1].response.json() == {'status': 'waiting'}

    with open(os.path.join(os.path.dirname(__file__), '../../resources/speech.wav'), 'rb') as audio_file:
        speech_to_text.create_job(audio=audio_file, content_type='audio/basic')
    assert responses.calls[2].response.json() == {'status': 'waiting'}

    speech_to_text.delete_job('jobid')
    assert responses.calls[3].response.json() == {
        "description": "deleted successfully"
    }

    assert len(responses.calls) == 4


@responses.activate
def test_callbacks():
    base_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1'
    responses.add(
        responses.POST,
        "{0}/register_callback".format(base_url),
        body='{"status": "created", "url": "monitorcalls.com"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.POST,
        "{0}/unregister_callback".format(base_url),
        body='{"response": "The callback URL was successfully unregistered"}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")
    speech_to_text.register_callback("monitorcalls.com")
    assert responses.calls[0].response.json() == {
        "status": "created",
        "url": "monitorcalls.com"
    }

    speech_to_text.unregister_callback("monitorcalls.com")
    assert responses.calls[1].response.json() == {
        "response": "The callback URL was successfully unregistered"
    }

    assert len(responses.calls) == 2


@responses.activate
def test_custom_model():
    customization_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations'
    train_url = "{0}/{1}/train".format(customization_url, 'customid')

    responses.add(
        responses.GET,
        customization_url,
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.POST,
        customization_url,
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        "{0}/modelid".format(customization_url),
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.DELETE,
        "{0}/modelid".format(customization_url),
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.POST,
        train_url,
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")

    speech_to_text.list_language_models()

    speech_to_text.create_language_model(
        name="Example model",
        base_model_name="en-US_BroadbandModel")

    parsed_body = json.loads(_decode_body(responses.calls[1].request.body))
    assert parsed_body['name'] == 'Example model'

    speech_to_text.create_language_model(
        name="Example model Two",
        base_model_name="en-US_BroadbandModel")

    parsed_body = json.loads(_decode_body(responses.calls[2].request.body))
    assert parsed_body['name'] == 'Example model Two'
    assert parsed_body['base_model_name'] == 'en-US_BroadbandModel'

    speech_to_text.train_language_model('customid')
    speech_to_text.get_language_model(customization_id='modelid')
    speech_to_text.delete_language_model(customization_id='modelid')

    assert len(responses.calls) == 6


@responses.activate
def test_acoustic_model():
    acoustic_customization_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/acoustic_customizations'
    train_url = "{0}/{1}/train".format(acoustic_customization_url, 'customid')

    responses.add(
        responses.GET,
        acoustic_customization_url,
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.POST,
        acoustic_customization_url,
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        "{0}/modelid".format(acoustic_customization_url),
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.DELETE,
        "{0}/modelid".format(acoustic_customization_url),
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.POST,
        train_url,
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")

    speech_to_text.list_acoustic_models()

    speech_to_text.create_acoustic_model(
        name="Example model",
        base_model_name="en-US_BroadbandModel",
        description="Example custom language model")

    parsed_body = json.loads(_decode_body(responses.calls[1].request.body))
    assert parsed_body['name'] == 'Example model'

    speech_to_text.create_acoustic_model(
        name="Example model Two",
        base_model_name="en-US_BroadbandModel")

    parsed_body = json.loads(_decode_body(responses.calls[2].request.body))
    assert parsed_body['name'] == 'Example model Two'
    assert parsed_body['base_model_name'] == 'en-US_BroadbandModel'

    speech_to_text.train_acoustic_model('customid')
    speech_to_text.get_acoustic_model(customization_id='modelid')
    speech_to_text.delete_acoustic_model(customization_id='modelid')

    assert len(responses.calls) == 6

@responses.activate
def test_upgrade_acoustic_model():
    acoustic_customization_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/acoustic_customizations'
    upgrade_url = "{0}/{1}/upgrade_model".format(acoustic_customization_url, 'customid')

    responses.add(
        responses.POST,
        upgrade_url,
        body='{"bogus_response": "yep"}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")

    speech_to_text.upgrade_acoustic_model(
        'customid',
        'model_x',
        force=True)
    assert responses.calls[0].response.json() == {"bogus_response": "yep"}

    assert len(responses.calls) == 1


def test_custom_corpora():

    corpora_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/{0}/corpora'
    get_corpora_url = '{0}/{1}'.format(
        corpora_url.format('customid'), 'corpus')

    with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
        rsps.add(
            responses.GET,
            corpora_url.format('customid'),
            body='{"get response": "yep"}',
            status=200,
            content_type='application/json')

        rsps.add(
            responses.POST,
            get_corpora_url,
            body='{"get response": "yep"}',
            status=200,
            content_type='application/json')

        rsps.add(
            responses.GET,
            get_corpora_url,
            body='{"get response": "yep"}',
            status=200,
            content_type='application/json')

        rsps.add(
            responses.DELETE,
            get_corpora_url,
            body='{"get response": "yep"}',
            status=200,
            content_type='application/json')

        speech_to_text = ibm_watson.SpeechToTextV1(
            username="username", password="password")

        speech_to_text.list_corpora(customization_id='customid')

        file_path = '../../resources/speech_to_text/corpus-short-1.txt'
        full_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(full_path) as corpus_file:
            speech_to_text.add_corpus(
                customization_id='customid',
                corpus_name="corpus",
                corpus_file=corpus_file)

        speech_to_text.get_corpus(
            customization_id='customid', corpus_name='corpus')

        speech_to_text.delete_corpus(
            customization_id='customid', corpus_name='corpus')


@responses.activate
def test_custom_words():
    words_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/{0}/words'
    word_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/{0}/words/{1}'

    responses.add(
        responses.PUT,
        word_url.format('custid', 'IEEE'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.PUT,
        word_url.format('custid', 'wordname'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.DELETE,
        word_url.format('custid', 'IEEE'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.DELETE,
        word_url.format('custid', 'wordname'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        word_url.format('custid', 'IEEE'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        word_url.format('custid', 'wordname'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.POST,
        words_url.format('custid'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        words_url.format('custid'),
        body='{"get response": "yep"}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")

    custom_word = CustomWord(
        word="IEEE", sounds_like=["i triple e"], display_as="IEEE")

    speech_to_text.add_word(
        customization_id='custid',
        word_name="IEEE",
        sounds_like=["i triple e"],
        display_as="IEEE")

    speech_to_text.delete_word(customization_id='custid', word_name="wordname")

    speech_to_text.delete_word(customization_id='custid', word_name='IEEE')

    custom_words = [custom_word, custom_word, custom_word]
    speech_to_text.add_words(
        customization_id='custid',
        words=custom_words)

    speech_to_text.get_word(customization_id='custid', word_name="IEEE")

    speech_to_text.get_word(customization_id='custid', word_name='wordname')

    speech_to_text.list_words(customization_id='custid')
    speech_to_text.list_words(customization_id='custid', sort='alphabetical')

    speech_to_text.list_words(customization_id='custid', word_type='all')

    assert len(responses.calls) == 9


@responses.activate
def test_custom_audio_resources():
    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/acoustic_customizations/{0}/audio/{1}'

    responses.add(
        responses.POST,
        url.format('custid', 'hiee'),
        body='{"post response": "done"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.DELETE,
        url.format('custid', 'hiee'),
        body='{"delete response": "done"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        url.format('custid', 'hiee'),
        body='{"get response": "done"}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        'https://stream.watsonplatform.net/speech-to-text/api/v1/acoustic_customizations/custid/audio',
        body='{"get response all": "done"}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../../resources/speech.wav'), 'rb') as audio_file:
        speech_to_text.add_audio(
            customization_id='custid',
            audio_name="hiee",
            audio_resource=audio_file,
            content_type="application/json")
    assert responses.calls[0].response.json() == {"post response": "done"}

    speech_to_text.delete_audio('custid', 'hiee')
    assert responses.calls[1].response.json() == {"delete response": "done"}

    speech_to_text.get_audio('custid', 'hiee')
    assert responses.calls[2].response.json() == {"get response": "done"}

    speech_to_text.list_audio('custid')
    assert responses.calls[3].response.json() == {"get response all": "done"}

@responses.activate
def test_delete_user_data():
    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/user_data'
    responses.add(
        responses.DELETE,
        url,
        body='{"description": "success" }',
        status=204,
        content_type='application_json')

    speech_to_text = ibm_watson.SpeechToTextV1(username="username", password="password")
    response = speech_to_text.delete_user_data('id').get_result()
    assert response is None
    assert len(responses.calls) == 1

@responses.activate
def test_custom_grammars():
    url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/{0}/grammars/{1}'

    responses.add(
        responses.POST,
        url.format('customization_id', 'grammar_name'),
        body='{}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.DELETE,
        url.format('customization_id', 'grammar_name'),
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        url.format('customization_id', 'grammar_name'),
        body='{"status": "analyzed", "name": "test-add-grammar-python", "out_of_vocabulary_words": 0}',
        status=200,
        content_type='application/json')

    responses.add(
        responses.GET,
        url='https://stream.watsonplatform.net/speech-to-text/api/v1/customizations/customization_id/grammars',
        body='{"grammars":[{"status": "analyzed", "name": "test-add-grammar-python", "out_of_vocabulary_words": 0}]}',
        status=200,
        content_type='application/json')

    speech_to_text = ibm_watson.SpeechToTextV1(
        username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../../resources/confirm-grammar.xml'), 'rb') as grammar_file:
        speech_to_text.add_grammar(
            "customization_id",
            grammar_name='grammar_name',
            grammar_file=grammar_file,
            content_type='application/srgs+xml',
            allow_overwrite=True)
    assert responses.calls[0].response.json() == {}

    speech_to_text.delete_grammar('customization_id', 'grammar_name')
    assert responses.calls[1].response.status_code == 200

    speech_to_text.get_grammar('customization_id', 'grammar_name')
    assert responses.calls[2].response.json() == {"status": "analyzed", "name": "test-add-grammar-python", "out_of_vocabulary_words": 0}

    speech_to_text.list_grammars('customization_id')
    assert responses.calls[3].response.json() == {"grammars":[{"status": "analyzed", "name": "test-add-grammar-python", "out_of_vocabulary_words": 0}]}
