import os
import glob
import json

from watson_developer_cloud import WSSpeechToTextV1

speech_to_text_ws = watson_developer_cloud.WSSpeechToTextV1(username='YOUR SERVICE USERNAME',
                                                            password='YOUR SERVICE PASSWORD',
                                                            x_watson_learning_opt_out=False)

print(json.dumps(speech_to_text.models(), indent=2))

print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

file_path_list = glob.glob('../resources/speech_to_text_ws/*.wav')
output_dir_path = '../resources/speech_to_text_ws/transcriptions/'

speech_to_text.recognize(
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
    log_type='file',
    file_input=file_path_list,
    dir_output=output_dir_path
)
