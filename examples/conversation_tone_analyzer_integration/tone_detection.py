import json

"""
 * Copyright 2015 IBM Corp. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

"""
 * Thresholds for identifying meaningful tones returned by the Watson Tone Analyzer.  Current values are
 * based on the recommendations made by the Watson Tone Analyzer at
 * https://www.ibm.com/watson/developercloud/doc/tone-analyzer/understanding-tone.shtml
 * These thresholds can be adjusted to client/domain requirements.
"""
PRIMARY_EMOTION_SCORE_THRESHOLD = 0.5
LANGUAGE_HIGH_SCORE_THRESHOLD = 0.75
LANGUAGE_NO_SCORE_THRESHOLD = 0.0
SOCIAL_HIGH_SCORE_THRESHOLD = 0.75
SOCIAL_LOW_SCORE_THRESHOLD = 0.25

# Labels for the tone categories returned by the Watson Tone Analyzer
EMOTION_TONE_LABEL = 'emotion_tone'
LANGUAGE_TONE_LABEL = 'language_tone'
SOCIAL_TONE_LABEL = 'social_tone'

'''
 * updateUserTone processes the Tone Analyzer payload to pull out the emotion, language and social
 * tones, and identify the meaningful tones (i.e., those tones that meet the specified thresholds).
 * The conversationPayload json object is updated to include these tones.
 * @param conversationPayload json object returned by the Watson Conversation Service
 * @param toneAnalyzerPayload json object returned by the Watson Tone Analyzer Service
 * @returns conversationPayload where the user object has been updated with tone information from the toneAnalyzerPayload
 '''
def updateUserTone (conversationPayload, toneAnalyzerPayload, maintainHistory):

  emotionTone = None
  languageTone = None
  socialTone = None

  # if there is no context in a
  if conversationPayload.context == None:
    conversationPayload.context = {};

  if conversationPayload.context.user == None:
     conversationPayload.context = initUser()

  # For convenience sake, define a variable for the user object
  user = conversationPayload['context']['user'];

  # Extract the tones - emotion, language and social
  if toneAnalyzerPayload and toneAnalyzerPayload['document_tone']:
    for toneCategory in toneAnalyzerPayload['document_tone']['tone_categories']:
      if toneCategory['category_id'] == EMOTION_TONE_LABEL:
        emotionTone = toneCategory
      if toneCategory['category_id'] == LANGUAGE_TONE_LABEL:
        languageTone = toneCategory
      if toneCategory['category_id'] == SOCIAL_TONE_LABEL:
        socialTone = toneCategory

    updateEmotionTone(user, emotionTone, maintainHistory)
    updateLanguageTone(user, languageTone, maintainHistory)
    updateSocialTone(user, socialTone, maintainHistory)

  conversationPayload['context']['user'] = user

  return conversationPayload;

'''
 initToneContext initializes a user object containing tone data (from the Watson Tone Analyzer)
 @returns user json object with the emotion, language and social tones.  The current
 tone identifies the tone for a specific conversation turn, and the history provides the conversation for
 all tones up to the current tone for a conversation instance with a user.
 '''
def initUser():
  return {
    'user': {
      'tone': {
        'emotion': {
          'current': null
        },
        'language': {
          'current': null
        },
        'social': {
          'current': null
        }
      }
    }
  }

'''
 updateEmotionTone updates the user emotion tone with the primary emotion - the emotion tone that has
 a score greater than or equal to the EMOTION_SCORE_THRESHOLD; otherwise primary emotion will be 'neutral'
 @param user a json object representing user information (tone) to be used in conversing with the Conversation Service
 @param emotionTone a json object containing the emotion tones in the payload returned by the Tone Analyzer
 '''
def updateEmotionTone(user, emotionTone, maintainHistory):

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
  user['tone']['emotion']['current'] = primaryEmotion;

  if maintainHistory:
    if not user['tone']['emotion']['history']:
        user['tone']['emotion']['history'] = []
        user['tone']['emotion']['history'].append({
            'tone_name': primaryEmotion,
            'score': primaryEmotionScore
    })

'''
 updateLanguageTone updates the user with the language tones interpreted based on the specified thresholds
 @param: user a json object representing user information (tone) to be used in conversing with the Conversation Service
 @param: languageTone a json object containing the language tones in the payload returned by the Tone Analyzer
'''
def updateLanguageTone (user, languageTone, maintainHistory):

  currentLanguage = [];
  currentLanguageObject = [];

  # Process each language tone and determine if it is high or low
  for tone in languageTone['tones']:
    if tone['score'] >= LANGUAGE_HIGH_SCORE_THRESHOLD:
      currentLanguage.append(tone['tone_name'].lower() + '_high')
      currentLanguageObject.append({
        'tone_name': tone['tone_name'].lower(),
        'score': tone['score'],
        'interpretation': 'likely high'
      })
    elif tone['score'] <= LANGUAGE_NO_SCORE_THRESHOLD:
      currentLanguageObject.append({
        'tone_name': tone['tone_name'].lower(),
        'score': tone['score'],
        'interpretation': 'no evidence'
      })
    else:
      currentLanguageObject.append({
        'tone_name': tone['tone_name'].lower(),
        'score': tone['score'],
        'interpretation': 'likely medium'
      })

  # update user language tone
  user['tone']['language']['current'] = currentLanguage
  if maintainHistory:
    if not user['tone']['language']['history']:
     user['tone']['language']['history'] = []
  user['tone']['language']['history'].append(currentLanguageObject)  #TODO - is this the correct location??? AW

'''
 updateSocialTone updates the user with the social tones interpreted based on the specified thresholds
 @param user a json object representing user information (tone) to be used in conversing with the Conversation Service
 @param socialTone a json object containing the social tones in the payload returned by the Tone Analyzer
 '''
def updateSocialTone (user, socialTone, maintainHistory):

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
      currentSocial.append(tone['tone_name'].lower() + '_low');
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
     user['tone']['social']['current'] = [];
    user['tone']['social']['current'].append(currentSocialObject);

