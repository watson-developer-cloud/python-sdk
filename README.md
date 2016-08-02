## Watson Developer Cloud Python SDK
[![Build Status](https://travis-ci.org/watson-developer-cloud/python-sdk.svg)](https://travis-ci.org/watson-developer-cloud/python-sdk)
[![codecov.io](https://codecov.io/github/watson-developer-cloud/python-sdk/coverage.svg?branch=master)](https://codecov.io/github/watson-developer-cloud/python-sdk?branch=master)
[![Latest Stable Version](https://img.shields.io/pypi/v/watson-developer-cloud.svg)](https://pypi.python.org/pypi/watson-developer-cloud)
[![Download Times](https://img.shields.io/pypi/dm/watson-developer-cloud.svg)](https://pypi.python.org/pypi/watson-developer-cloud)

Python client library to quickly get started with the various [Watson Developer Cloud][wdc] services.

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
The [examples][examples] folder has basic and advanced examples.

## Getting the Service Credentials
You will need the `username` and `password` credentials for each service. Service credentials are different from your Bluemix account username and password.

To get your service credentials, follow these steps:
 1. Log in to Bluemix at https://bluemix.net.

 1. Create an instance of the service:
     1. In the Bluemix **Catalog**, select the Watson service you want to use. For example, select the Natural Language Classifier service.
     1. Under **Add Service**, type a unique name for the service instance in the Service name field. For example, type `my-service-name`. Leave the default values for the other options.
     1. Click **Use**.

 1. Copy your credentials:
     1. On the left side of the page, click **Service Credentials** to view your service credentials.
     1. Copy `username` and `password` from these service credentials.

## Python Version
Tested 👌 (lightly) on: Python from 2.7 to 3.5-dev (development branch).
Python 2.6 is partially supported but generates InsecurePlatformWarnings (and other warnings), which can be ignored.

## CHANGELOG
See [CHANGELOG][CHANGELOG.md].

## Known Issues
There is a known incompatibility with this module with Python versions 3.x with Korean systems.

## Dependencies
* [requests]
* [responses] for testing

## Contributing
See [CONTRIBUTING.md][CONTRIBUTING].

## License

This library is licensed under the [Apache 2.0 license][license].

[wdc]: http://www.ibm.com/watson/developercloud/
[vcap_environment]: http://www.ibm.com/watson/developercloud/doc/getting_started/gs-variables.shtml
[bluemix]: https://console.ng.bluemix.net
[pytest]: http://pytest.org/latest/
[responses]: https://github.com/getsentry/responses
[requests]: http://docs.python-requests.org/en/latest/
[examples]: https://github.com/watson-developer-cloud/python-sdk/tree/master/examples
[CONTRIBUTING]: https://github.com/watson-developer-cloud/python-sdk/blob/master/CONTRIBUTING.md
[CHANGELOG.md]: https://github.com/watson-developer-cloud/python-sdk/blob/master/CHANGELOG.md

[license]: http://www.apache.org/licenses/LICENSE-2.0
