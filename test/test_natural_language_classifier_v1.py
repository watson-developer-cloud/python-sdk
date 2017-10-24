import os
import responses
import watson_developer_cloud


@responses.activate
def test_success():
    natural_language_classifier = watson_developer_cloud.NaturalLanguageClassifierV1(username="username",
                                                                                     password="password")

    list_url = 'https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers'
    list_response = '{"classifiers": [{"url": "https://gateway.watsonplatform.net/natural-language-classifier-' \
                    'experimental/api/v1/classifiers/497EF2-nlc-00", "classifier_id": "497EF2-nlc-00"}]}'
    responses.add(responses.GET, list_url,
                  body=list_response, status=200,
                  content_type='application/json')

    natural_language_classifier.list()

    assert responses.calls[0].request.url == list_url
    assert responses.calls[0].response.text == list_response

    status_url = ('https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/'
                  '497EF2-nlc-00')
    status_response = '{"url": "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/' \
                      'classifiers/497EF2-nlc-00", "status": "Available", "status_description": "The classifier ' \
                      'instance is now available and is ready to take classifier requests.", "classifier_id": ' \
                      '"497EF2-nlc-00"}'

    responses.add(responses.GET, status_url,
                  body=status_response, status=200,
                  content_type='application/json')

    natural_language_classifier.status('497EF2-nlc-00')

    assert responses.calls[1].request.url == status_url
    assert responses.calls[1].response.text == status_response

    classify_url = 'https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/' \
                   '497EF2-nlc-00/classify'
    classify_response = '{"url": "https://gateway.watsonplatform.net/natural-language-classifier/api/' \
                        'v1", "text": "test", "classes": [{"class_name": "conditions", "confidence": ' \
                        '0.6575315710901418}, {"class_name": "temperature", "confidence": 0.3424684289098582}], ' \
                        '"classifier_id": "497EF2-nlc-00", "top_class": "conditions"}'

    responses.add(responses.POST, classify_url,
                  body=classify_response, status=200,
                  content_type='application/json')

    natural_language_classifier.classify('497EF2-nlc-00', 'test')

    assert responses.calls[2].request.url == classify_url
    assert responses.calls[2].response.text == classify_response

    create_url = 'https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers'
    create_response = '{"url": "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/' \
                      'classifiers/497EF2-nlc-00", "status": "Available", "status_description": "The classifier ' \
                      'instance is now available and is ready to take classifier requests.", "classifier_id": ' \
                      '"497EF2-nlc-00"}'

    responses.add(responses.POST, create_url,
                  body=create_response, status=200,
                  content_type='application/json')
    with open(os.path.join(os.path.dirname(__file__), '../resources/weather_data_train.csv'), 'rb') as training_data:
        natural_language_classifier.create(
            training_data=training_data, language='en')

    assert responses.calls[3].request.url == create_url
    assert responses.calls[3].response.text == create_response

    remove_url = status_url
    remove_response = '{}'

    responses.add(responses.DELETE, remove_url,
                  body=remove_response, status=200,
                  content_type='application/json')

    natural_language_classifier.remove('497EF2-nlc-00')

    assert responses.calls[4].request.url == remove_url
    assert responses.calls[4].response.text == remove_response

    assert len(responses.calls) == 5
