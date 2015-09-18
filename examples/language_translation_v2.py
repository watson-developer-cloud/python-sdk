# coding=utf-8
import json
import watson_developer_cloud


language_translation = watson_developer_cloud.LanguageTranslationV2()

print(json.dumps(language_translation.get_models(), indent=2))

print(watson_developer_cloud.LanguageTranslationV2.default_url)

print(json.dumps(language_translation.translate('Hola, cómo estás? €', source='es', target='en'), indent=2,
                 ensure_ascii=False))


print(json.dumps(language_translation.identify('Hello how are you?'), indent=2))
