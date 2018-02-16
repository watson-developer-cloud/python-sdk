# coding=utf-8

import responses
import glob
import logging
import watson_developer_cloud

@responses.activate
def test_error(caplog):

    speech_to_text_ws = watson_developer_cloud.WSSpeechToTextV1(username='YOUR SERVICE USERNAME',
                                                                password='YOUR SERVICE PASSWORD',
                                                                x_watson_learning_opt_out=False)

    caplog.set_level(logging.DEBUG)

    #test autobahn ws reactor connection
    file_path_list = glob.glob('../resources/speech_to_text_ws/*.wav')
    output_dir_path = '../resources/speech_to_text_ws/transcriptions/'



    speech_to_text_ws.recognize(
        content_type='audio/bogus',
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

    # test error message received
    error_message = 'Error message received from Watson: '
    watson_response = 'Unable to transcode from audio/bogus to audio/x-float-array; rate=16000; channels=1'
    assert (error_message in s for s in caplog.text)
    assert (watson_response in s for s in caplog.text)
