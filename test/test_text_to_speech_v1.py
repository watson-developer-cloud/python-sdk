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
