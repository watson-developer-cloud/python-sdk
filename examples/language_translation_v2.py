# coding=utf-8
import json
import watson_developer_cloud.LanguageTranslationV2 as LanguageTranslation


language_translation = LanguageTranslation(username='YOUR SERVICE USERNAME',
                                           password='YOUR SERVICE PASSWORD')

print(json.dumps(language_translation.get_models(), indent=2))

print(json.dumps(language_translation.translate('Hola, cómo estás? €', source='es', target='en'), indent=2,
                 ensure_ascii=False))


print(json.dumps(language_translation.identify('Hello how are you?'), indent=2))
