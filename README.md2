## Watson Developer Cloud Python SDK
[![Software License](https://img.shields.io/badge/license-Apache 2.0-brightgreen.svg)](LICENSE)
[![Build Status](https://travis-ci.org/qiniu/python-sdk.svg)](https://travis-ci.org/watson-developer-cloud/python-sdk)
[![Latest Stable Version](https://img.shields.io/pypi/v/watson-developer-cloud.svg)](https://pypi.python.org/pypi/watson-developer-cloud)
[![Download Times](https://img.shields.io/pypi/dm/watson-developer-cloud.svg)](https://pypi.python.org/pypi/watson-developer-cloud)

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

## Examples
The [examples](examples) folder has basic and advanced examples.

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
Tested (lightly) on: Python from 2.6 to 3.6-dev (development branch)

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
