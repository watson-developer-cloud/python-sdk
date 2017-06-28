# coding=utf-8
import json
import responses
import glob
import logging
import watson_developer_cloud

@responses.activate
def test_success(caplog):
    # test authentication
    models_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/models'
    models_response = '{"models": [{"url": "https://stream.watsonplatform.net/speech-to-text/api/v1/models/' \
                      'WatsonModel", "rate": 16000, "name": "WatsonModel", "language": "en-US", "description": ' \
                      '"Watson model \'v7w_134k.3\' for Attila 2-5 reco engine."}]}'

    responses.add(responses.GET, models_url,
                  body=models_response, status=200,
                  content_type='application/json')

    speech_to_text_ws = watson_developer_cloud.WSSpeechToTextV1(username='YOUR SERVICE USERNAME',
                                                                password='YOUR SERVICE PASSWORD',
                                                                x_watson_learning_opt_out=False)

    speech_to_text_ws.models()

    assert responses.calls[0].request.url == models_url
    assert responses.calls[0].response.text == models_response

    caplog.set_level(logging.DEBUG)

    #test autobahn ws reactor connection
    file_path_list = glob.glob('../resources/speech_to_text_ws/*.wav')
    output_dir_path = '../resources/speech_to_text_ws/transcriptions/'


    speech_to_text_ws.recognize(
        content_type='audio/wav',
        inactivity_timeout=-1, #set to -1 to ignore silence
        word_alternatives_threshold=.75,
        word_confidence=True,
        timestamps=True,
        max_alternatives=1,
        speaker_labels=True,
        keywords=['closed', 'session'],
        keywords_threshold=.6,
        profanity_filter=False,
        smart_formatting=True,
        threads=4,
        log_type='stdout',
        file_input=file_path_list,
        dir_output=output_dir_path
    )


    # test connection url
    # hostname='stream.watsonplatform.net'
    # model='en-US_BroadbandModel'
    # ws_url="wss://" + hostname + "/speech-to-text/api/v1/recognize?model=" + model
    # mock_url=mock_reactor.return_value.speech_to_text.recognize.get(url)
    # assert mock_url == ws_url

    # test log
    log_event = "Log opened."
    assert (log_event in s for s in caplog.text)

    # test close event
    # ensure full transcription received
    listening_event = "Closing connection to Watson. Sending code: 1000"
    assert (listening_event in s for s in caplog.text)

    # test reactor stopped
    reactor_shutdown = "About to stop the websocket reactor."
    assert (reactor_shutdown in s for s in caplog.text)

    # test loop exited
    exit_loop = "Main loop terminated."
    assert (exit_loop in s for s in caplog.text)

    # test transcript saved
    transcript_event = "Transcript saved to: "
    assert (transcript_event in s for s in caplog.text)

    # test transcript files
    first_path = '../resources/speech_to_text_ws/transcriptions/0001.json'
    last_path = '../resources/speech_to_text_ws/transcriptions/0010.json'


    recognize_files = glob.glob(output_dir_path + '*.json')
    assert len(recognize_files) == len(file_path_list)
    assert recognize_files[0] == first_path
    assert recognize_files[-1] == last_path

    # test transcript
    first_transcript = 'several tornadoes touch down as a line of severe thunderstorms swept through Colorado on Sunday '
    last_transcript = 'causing one minor injury and flipping an empty trailer '

    with open(recognize_files[0]) as file:
        jsonObject = json.load(file, encoding='utf-8')
        recognize_first_transcript = jsonObject['results'][0]['alternatives'][0]['transcript']

    with open(recognize_files[-1]) as file:
        jsonObject = json.load(file, encoding='utf-8')
        recognize_last_transcript = jsonObject['results'][-1]['alternatives'][-1]['transcript']

    assert recognize_first_transcript == first_transcript
    assert recognize_last_transcript == last_transcript
