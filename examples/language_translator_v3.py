# coding=utf-8
from __future__ import print_function
import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-31',
    ### url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/language-translator/api',
    iam_api_key='your_api_key')

## Authenticate with username/password if your service instance doesn't provide an API key
# language_translator = LanguageTranslatorV3(
#     version='2018-05-31',
#     username='your_username',
#     password='your_password')


## Translate
translation = language_translator.translate(
    text='Hello',
    model_id='en-es')
print(json.dumps(translation, indent=2, ensure_ascii=False))

## List identifiable languages
# languages = language_translator.list_identifiable_languages()
# print(json.dumps(languages, indent=2))

## Identify
# language = language_translator.identify(
#     'Language translator translates text from one language to another')
# print(json.dumps(language, indent=2))

## List models
# models = language_translator.list_models(
#     source='en')
# print(json.dumps(models, indent=2))

## Create model
# with open('glossary.tmx', 'rb') as glossary:
#   response = language_translator.create_model(
#     base_model_id = 'en-es',
#     name = 'custom-english-to-spanish',
#     forced_glossary = glossary)
#   print(json.dumps(response, indent=2))

## Delete model
# print(json.dumps(language_translator.delete_model(model_id='9f8d9c6f-2123-462f-9793-f17fdcb77cd6'), indent=2))

## Get model details
# model = language_translator.get_model(model_id='fdadfc3b-0b96-4276-a6e5-f5c4a29711fc')
# print(json.dumps(model, indent=2))
