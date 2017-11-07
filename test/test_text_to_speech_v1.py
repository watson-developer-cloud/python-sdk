# coding=utf-8
import responses
import watson_developer_cloud


@responses.activate
def test_success():
    voices_url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/voices'
    voices_response = '{"voices": [{"url": "https://stream.watsonplatform.net/text-to-speech/api/v1/voices/' \
                      'VoiceEnUsLisa", "gender": "female", "name": "VoiceEnUsLisa", "language": "en-US"}, {"url": ' \
                      '"https://stream.watsonplatform.net/text-to-speech/api/v1/voices/VoiceEsEsEnrique", ' \
                      '"gender": "male", "name": "VoiceEsEsEnrique", "language": "es-ES"}, {"url": ' \
                      '"https://stream.watsonplatform.net/text-to-speech/api/v1/voices/VoiceEnUsMichael", ' \
                      '"gender": "male", "name": "VoiceEnUsMichael", "language": "en-US"}, {"url": ' \
                      '"https://stream.watsonplatform.net/text-to-speech/api/v1/voices/VoiceEnUsAllison", ' \
                      '"gender": "female", "name": "VoiceEnUsAllison", "language": "en-US"}]}'

    responses.add(responses.GET, voices_url, body=voices_response,
                  status=200, content_type='application/json')

    text_to_speech = watson_developer_cloud.TextToSpeechV1(
        username="username", password="password")
    text_to_speech.voices()

    assert responses.calls[0].request.url == voices_url
    assert responses.calls[0].response.text == voices_response

    synthesize_text = 'hello'
    synthesize_url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize'
    synthesize_response_body = '<binary response>'

    responses.add(responses.POST, synthesize_url,
                  body=synthesize_response_body, status=200,
                  content_type='application/json', match_querystring=True)
    text_to_speech.synthesize(synthesize_text)

    assert responses.calls[1].request.url == synthesize_url
    assert responses.calls[1].response.text == synthesize_response_body

    assert len(responses.calls) == 2


@responses.activate
def test_pronounciation():

    responses.add(responses.GET, 'https://stream.watsonplatform.net/text-to-speech/api/v1/pronunciation',
                  body='{"pronunciation": "pronunciation info" }',
                  status=200, content_type='application_json')

    text_to_speech = watson_developer_cloud.TextToSpeechV1(
        username="username", password="password")
    text_to_speech.pronunciation(text="this is some text")
    text_to_speech.pronunciation(text="yo", voice="VoiceEnUsLisa")
    text_to_speech.pronunciation(
        text="yo", voice="VoiceEnUsLisa", pronunciation_format='ipa')

    assert len(responses.calls) == 3


@responses.activate
def test_customizations():
    responses.add(responses.GET, 'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations',
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')
    responses.add(responses.POST, 'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations',
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')
    responses.add(responses.GET, 'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations/custid',
                  body='{"customization": "yep, just one" }',
                  status=200, content_type='application_json')
    responses.add(responses.POST, 'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations/custid',
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')
    responses.add(responses.DELETE, 'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations/custid',
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')

    text_to_speech = watson_developer_cloud.TextToSpeechV1(
        username="username", password="password")
    text_to_speech.customizations()
    text_to_speech.customizations(language="en-US")
    assert len(responses.calls) == 2

    text_to_speech.create_customization(name="name", description="description")
    text_to_speech.get_customization(customization_id='custid')
    text_to_speech.update_customization(
        customization_id="custid", name="name", description="description")
    text_to_speech.delete_customization(customization_id="custid")

    assert len(responses.calls) == 6


@responses.activate
def test_customization_words():
    base_url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/customizations'
    responses.add(responses.GET, "{0}/{1}/words".format(base_url, "custid"),
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')
    responses.add(responses.POST, "{0}/{1}/words".format(base_url, "custid"),
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')
    responses.add(responses.GET, "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
                  body='{"customization": "yep, just one" }',
                  status=200, content_type='application_json')
    responses.add(responses.POST, "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')
    responses.add(responses.PUT, "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')
    responses.add(responses.DELETE, "{0}/{1}/words/{2}".format(base_url, "custid", "word"),
                  body='{"customizations": "yep" }',
                  status=200, content_type='application_json')

    text_to_speech = watson_developer_cloud.TextToSpeechV1(
        username="username", password="password")
    text_to_speech.get_customization_words(customization_id="custid")
    text_to_speech.add_customization_words(
        customization_id="custid", words=["one", "two", "three"])
    text_to_speech.get_customization_word(
        customization_id="custid", word="word")
    text_to_speech.set_customization_word(
        customization_id='custid', word="word", translation="I'm translated")
    text_to_speech.delete_customization_word(
        customization_id="custid", word="word")
    assert len(responses.calls) == 5
