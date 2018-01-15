# Copyright 2016 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
 * Thresholds for identifying meaningful tones returned by the Watson Tone
 Analyzer.  Current values are
 * based on the recommendations made by the Watson Tone Analyzer at
 * https://console.bluemix.net/docs/services/tone-analyzer/using-tone.html
 * These thresholds can be adjusted to client/domain requirements.
"""

PRIMARY_EMOTION_SCORE_THRESHOLD = 0.5
WRITING_HIGH_SCORE_THRESHOLD = 0.75
WRITING_NO_SCORE_THRESHOLD = 0.0
SOCIAL_HIGH_SCORE_THRESHOLD = 0.75
SOCIAL_LOW_SCORE_THRESHOLD = 0.25

# Labels for the tone categories returned by the Watson Tone Analyzer
EMOTION_TONE_LABEL = 'emotion_tone'
WRITING_TONE_LABEL = 'writing_tone'
SOCIAL_TONE_LABEL = 'social_tone'


def updateUserTone(conversationPayload, toneAnalyzerPayload, maintainHistory):
    """
    updateUserTone processes the Tone Analyzer payload to pull out the emotion,
    writing and social tones, and identify the meaningful tones (i.e.,
    those tones that meet the specified thresholds).
    The conversationPayload json object is updated to include these tones.
    @param conversationPayload json object returned by the Watson Conversation
    Service
    @param toneAnalyzerPayload json object returned by the Watson Tone Analyzer
    Service
    @returns conversationPayload where the user object has been updated with tone
    information from the toneAnalyzerPayload
    """
    emotionTone = None
    writingTone = None
    socialTone = None

    # if there is no context in a
    if 'context' not in conversationPayload:
        conversationPayload['context'] = {}

    if 'user' not in conversationPayload['context']:
        conversationPayload['context'] = initUser()

    # For convenience sake, define a variable for the user object
    user = conversationPayload['context']['user']

    # Extract the tones - emotion, writing and social
    if toneAnalyzerPayload and toneAnalyzerPayload['document_tone']:
        for toneCategory in toneAnalyzerPayload['document_tone'][
                'tone_categories']:
            if toneCategory['category_id'] == EMOTION_TONE_LABEL:
                emotionTone = toneCategory
            if toneCategory['category_id'] == WRITING_TONE_LABEL:
                writingTone = toneCategory
            if toneCategory['category_id'] == SOCIAL_TONE_LABEL:
                socialTone = toneCategory

        updateEmotionTone(user, emotionTone, maintainHistory)
        updateWritingTone(user, writingTone, maintainHistory)
        updateSocialTone(user, socialTone, maintainHistory)

    conversationPayload['context']['user'] = user

    return conversationPayload


def initUser():
    """
    initUser initializes a user object containing tone data (from the
    Watson Tone Analyzer)
    @returns user json object with the emotion, writing and social tones.  The
    current tone identifies the tone for a specific conversation turn, and the
    history provides the conversation for all tones up to the current tone for a
    conversation instance with a user.
    """
    return {
        'user': {
            'tone': {
                'emotion': {
                    'current': None
                },
                'writing': {
                    'current': None
                },
                'social': {
                    'current': None
                }
            }
        }
    }




def updateEmotionTone(user, emotionTone, maintainHistory):
    """
    updateEmotionTone updates the user emotion tone with the primary emotion -
    the emotion tone that has a score greater than or equal to the
    EMOTION_SCORE_THRESHOLD; otherwise primary emotion will be 'neutral'
    @param user a json object representing user information (tone) to be used in
    conversing with the Conversation Service
    @param emotionTone a json object containing the emotion tones in the payload
    returned by the Tone Analyzer
    """
    maxScore = 0.0
    primaryEmotion = None
    primaryEmotionScore = None

    for tone in emotionTone['tones']:
        if tone['score'] > maxScore:
            maxScore = tone['score']
            primaryEmotion = tone['tone_name'].lower()
            primaryEmotionScore = tone['score']

    if maxScore <= PRIMARY_EMOTION_SCORE_THRESHOLD:
        primaryEmotion = 'neutral'
        primaryEmotionScore = None

    # update user emotion tone
    user['tone']['emotion']['current'] = primaryEmotion

    if maintainHistory:
        if 'history' not in user['tone']['emotion']:
            user['tone']['emotion']['history'] = []
            user['tone']['emotion']['history'].append({
                'tone_name': primaryEmotion,
                'score': primaryEmotionScore
            })


def updateWritingTone(user, writingTone, maintainHistory):
    """
    updateWritingTone updates the user with the writing tones interpreted based
    on the specified thresholds
    @param: user a json object representing user information (tone) to be used
    in conversing with the Conversation Service
    @param: writingTone a json object containing the writing tones in the
    payload returned by the Tone Analyzer
    """
    currentWriting = []
    currentWritingObject = []

    # Process each writing tone and determine if it is high or low
    for tone in writingTone['tones']:
        if tone['score'] >= WRITING_HIGH_SCORE_THRESHOLD:
            currentWriting.append(tone['tone_name'].lower() + '_high')
            currentWritingObject.append({
                'tone_name': tone['tone_name'].lower(),
                'score': tone['score'],
                'interpretation': 'likely high'
            })
        elif tone['score'] <= WRITING_NO_SCORE_THRESHOLD:
            currentWritingObject.append({
                'tone_name': tone['tone_name'].lower(),
                'score': tone['score'],
                'interpretation': 'no evidence'
            })
        else:
            currentWritingObject.append({
                'tone_name': tone['tone_name'].lower(),
                'score': tone['score'],
                'interpretation': 'likely medium'
            })

    # update user writing tone
    user['tone']['writing']['current'] = currentWriting
    if maintainHistory:
        if 'history' not in user['tone']['writing']:
            user['tone']['writing']['history'] = []
    user['tone']['writing']['history'].append(currentWritingObject)


def updateSocialTone(user, socialTone, maintainHistory):
    """
    updateSocialTone updates the user with the social tones interpreted based on
    the specified thresholds
    @param user a json object representing user information (tone) to be used in
    conversing with the Conversation Service
    @param socialTone a json object containing the social tones in the payload
    returned by the Tone Analyzer
    """
    currentSocial = []
    currentSocialObject = []

    # Process each social tone and determine if it is high or low
    for tone in socialTone['tones']:
        if tone['score'] >= SOCIAL_HIGH_SCORE_THRESHOLD:
            currentSocial.append(tone['tone_name'].lower() + '_high')
            currentSocialObject.append({
                'tone_name': tone['tone_name'].lower(),
                'score': tone['score'],
                'interpretation': 'likely high'
            })
        elif tone['score'] <= SOCIAL_LOW_SCORE_THRESHOLD:
            currentSocial.append(tone['tone_name'].lower() + '_low')
            currentSocialObject.append({
                'tone_name': tone['tone_name'].lower(),
                'score': tone['score'],
                'interpretation': 'likely low'
            })
        else:
            currentSocialObject.append({
                'tone_name': tone['tone_name'].lower(),
                'score': tone['score'],
                'interpretation': 'likely medium'
            })

    # update user social tone
    user['tone']['social']['current'] = currentSocial
    if maintainHistory:
        if not user['tone']['social']['current']:
            user['tone']['social']['current'] = []
        user['tone']['social']['current'].append(currentSocialObject)
