## Watson Developer Cloud Python SDK
Python client library to quickly get started with the various [Watson Developer Cloud][wdc] services - A collection of REST APIs and SDKs that use cognitive computing to solve complex problems.

## Questions

If you are having difficulties using the APIs or have a question about the IBM
Watson Services, please ask a question on
[dW Answers](https://developer.ibm.com/answers/questions/ask/?topics=watson)
or [Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-watson).


## Installation

To install, use `pip` or `easy_install`:

```bash
$ pip install --upgrade watson-developer-cloud
```
or
```bash
$ easy_install --upgrade watson-developer-cloud
```

### Getting the Service Credentials
You will need the `username` and `password` credentials for each service these are *not* your Bluemix credentials, and are found in the VCAP_SERVICES variable on Bluemix, and they are different for each service.

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

## Build + Test

To build and test the project you need [nosetests][nosetests].  
```bash
install: "pip install -r requirements.txt"
nodetests
```
## Python Version
Tested (lightly) on: Python 2.6, 2.7, 3.2, 3.3, 3.4, 3.5, 3.5-dev and 3.6-dev (development branch)

## Python Version

## Third Party Libraries and Dependencies
* [requests](http://docs.python-requests.org/en/latest/)
* [responses](https://github.com/getsentry/responses)(for testing)

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This library is licensed under the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0).

[wdc]: http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/
[vcap_environment]: http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/getting_started/index.html#EnvVars
[bluemix]: https://console.ng.bluemix.net
[nosetests]: https://nose.readthedocs.org/en/latest/
