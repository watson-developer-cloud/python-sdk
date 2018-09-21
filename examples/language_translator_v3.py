# coding=utf-8
from __future__ import print_function
import json
from watson_developer_cloud import LanguageTranslatorV3

# language_translator = LanguageTranslatorV3(
#     version='2018-05-01.',
#     ### url is optional, and defaults to the URL below. Use the correct URL for your region.
#     # url='https://gateway.watsonplatform.net/language-translator/api',
#     iam_apikey='your_apikey')

# Authenticate with username/password if your service instance doesn't provide an API key
language_translator = LanguageTranslatorV3(
    version='2018-05-01.',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

## Translate
translation = language_translator.translate(
    text='Hello', model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

# List identifiable languages
# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))

# # Identify
# language = language_translator.identify(
#     'Language translator translates text from one language to another').get_result()
# print(json.dumps(language, indent=2))

# # List models
# models = language_translator.list_models(
#     source='en').get_result()
# print(json.dumps(models, indent=2))

# # Create model
# with open('glossary.tmx', 'rb') as glossary:
#     response = language_translator.create_model(
#         base_model_id='en-es',
#         name='custom-english-to-spanish',
#         forced_glossary=glossary).get_result()
#     print(json.dumps(response, indent=2))

# # Delete model
# response = language_translator.delete_model(model_id='<YOUR MODEL ID>').get_result()
# print(json.dumps(response, indent=2))

# # Get model details
# model = language_translator.get_model(model_id='<YOUR MODEL ID>').get_result()
# print(json.dumps(model, indent=2))
