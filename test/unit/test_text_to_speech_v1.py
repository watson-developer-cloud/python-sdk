# coding=utf-8
import responses
import ibm_watson
import json


@responses.activate
def test_success():
    voices_url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/voices'
    voices_response = {
        "voices": [{
            "url":
            "https://stream.watsonplatform.net/text-to-speech/api/v1/voices/VoiceEnUsLisa",
            "gender":
            "female",
            "name":
            "VoiceEnUsLisa",
            "language":
            "en-US"
        }, {
            "url":
            "https://stream.watsonplatform.net/text-to-speech/api/v1/voices/VoiceEsEsEnrique",
            "gender":
            "male",
            "name":
            "VoiceEsEsEnrique",
            "language":
            "es-ES"
        }, {
            "url":
            "https://stream.watsonplatform.net/text-to-speech/api/v1/voices/VoiceEnUsMichael",
            "gender":
            "male",
            "name":
            "VoiceEnUsMichael",
            "language":
            "en-US"
        }, {
            "url":
            "https://stream.watsonplatform.net/text-to-speech/api/v1/voices/VoiceEnUsAllison",
            "gender":
            "female",
            "name":
            "VoiceEnUsAllison",
            "language":
            "en-US"
        }]
    }
    voice_url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/voices/en-us_AllisonVoice'
    voice_response = {
        "url":
        "https://stream.watsonplatform.net/text-to-speech/api/v1/voices/en-US_AllisonVoice",
        "name":
        "en-US_AllisonVoice",
        "language":
        "en-US",
        "customizable":
        True,
        "gender":
        "female",
        "description":
        "Allison: American English female voice.",
        "supported_features": {
            "custom_pronunciation": True,
            "voice_transformation": True
        }
    }
    synthesize_url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize'
    synthesize_response_body = '<binary response>'

    responses.add(
        responses.GET,
        voices_url,
        body=json.dumps(voices_response),
        status=200,
        content_type='application/json')
    responses.add(
        responses.GET,
        voice_url,
        body=json.dumps(voice_response),
        status=200,
        content_type='application/json')
    responses.add(
        responses.POST,
        synthesize_url,
        body=synthesize_response_body,
        status=200,
        content_type='application/json',
        match_querystring=True)

    text_to_speech = ibm_watson.TextToSpeechV1(
        username="username", password="password")

    text_to_speech.list_voices()
    assert responses.calls[0].request.url == voices_url
    assert responses.calls[0].response.text == json.dumps(voices_response)

    text_to_speech.get_voice('en-us_AllisonVoice')
    assert responses.calls[1].request.url == voice_url
    assert responses.calls[1].response.text == json.dumps(voice_response)

    text_to_speech.synthesize('hello')
    assert responses.calls[2].request.url == synthesize_url
    assert responses.calls[2].response.text == synthesize_response_body

    assert len(responses.calls) == 3


@responses.activate
def test_get_pronunciation():

    responses.add(
        responses.GET,
        'https://stream.watsonplatform.net/text-to-speech/api/v1/pronunciation',
        body='{"pronunciation": "pronunciation info" }',
        status=200,
        content_type='application_json')

    text_to_speech = ibm_watson.TextToSpeechV1(
        username="username", password="password")

    text_to_speech.get_pronunciation(text="this is some text")
    text_to_speech.get_pronunciation(text="yo", voice="VoiceEnUsLisa")
    text_to_speech.get_pronunciation(
        text="yo", voice="VoiceEnUsLisa", format='ipa')

    assert len(responses.calls) == 3


@responses.activate
def test_custom_voice_models():
    responses.add(
        responses.GET,
        'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations',
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.POST,
        'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations',
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.GET,
        'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations/custid',
        body='{"customization": "yep, just one" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.POST,
        'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations/custid',
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.DELETE,
        'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations/custid',
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')

    text_to_speech = ibm_watson.TextToSpeechV1(
        username="username", password="password")
    text_to_speech.list_voice_models()
    text_to_speech.list_voice_models(language="en-US")
    assert len(responses.calls) == 2

    text_to_speech.create_voice_model(name="name", description="description")
    text_to_speech.get_voice_model(customization_id='custid')
    text_to_speech.update_voice_model(
        customization_id="custid", name="name", description="description")
    text_to_speech.delete_voice_model(customization_id="custid")

    assert len(responses.calls) == 6


@responses.activate
def test_custom_words():
    base_url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations'
    responses.add(
        responses.GET,
        "{0}/{1}/words".format(base_url, "custid"),
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.POST,
        "{0}/{1}/words".format(base_url, "custid"),
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.GET,
        "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
        body='{"customization": "yep, just one" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.POST,
        "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.PUT,
        "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')
    responses.add(
        responses.DELETE,
        "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
        body='{"customizations": "yep" }',
        status=200,
        content_type='application_json')

    text_to_speech = ibm_watson.TextToSpeechV1(
        username="username", password="password")

    text_to_speech.list_words(customization_id="custid")
    text_to_speech.add_words(
        customization_id="custid", words=[{"word": "one", "translation": "one"}, {"word": "two", "translation": "two"}])
    text_to_speech.get_word(customization_id="custid", word="word")
    text_to_speech.add_word(
        customization_id='custid', word="word", translation="I'm translated")
    text_to_speech.delete_word(customization_id="custid", word="word")

    assert len(responses.calls) == 5

@responses.activate

def test_delete_user_data():
    url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/user_data'
    responses.add(
        responses.DELETE,
        url,
        body='{"description": "success" }',
        status=204,
        content_type='application_json')

    text_to_speech = ibm_watson.TextToSpeechV1(username="username", password="password")
    response = text_to_speech.delete_user_data('id').get_result()
    assert response is None
    assert len(responses.calls) == 1
