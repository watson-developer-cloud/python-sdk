## About
This is the Python client library for IBM's Watson Developer Cloud APIs. This is a preview release -- a future version
will be released at https://github.com/watson-developer-cloud and this version will be deleted. Just as a heads up.

## Questions

If you are having difficulties using the APIs or have a question about the IBM
Watson Services, please ask a question on
[dW Answers](https://developer.ibm.com/answers/questions/ask/?topics=watson)
or [Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-watson).


## Installation
Clone the repository and run `python setup.py install`. In the future the SDK will be available via pip.

<!---
To install, use `pip` or `easy_install`:

```bash
$ pip install --upgrade watson-developer-cloud
```
or
```bash
$ easy_install --upgrade watson-developer-cloud
```
-->

## Python Version
Tested (lightly) on Python 2.7 and Python 3.3.


### Getting the Service Credentials
The credentials for the services are stored in the
[VCAP_SERVICES][vcap_environment] environment variable. To get them, you need
to first create and bind the service to your application.

You can use Bluemix to access your app and view the `VCAP_SERVICES` environment variable there.

Example output:
```System-Provided:
  {
  "VCAP_SERVICES": {
    "visual_recognition": [{
        "credentials": {
          "password": "<password>",
          "url": "<url>",
          "username": "<username>"
        },
      "label": "visual_recognition",
      "name": "visual-recognition-service",
      "plan": "free"
   }]
  }
  }
```

You need to copy `username` and `password`.


## Third Party Libraries and Dependencies
* [requests](http://docs.python-requests.org/en/latest/)


## License

This library is licensed under the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0).