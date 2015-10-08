## Watson Developer Cloud Python SDK
[![Software License](https://img.shields.io/badge/license-Apache 2.0-brightgreen.svg)](LICENSE)
[![Build Status](https://travis-ci.org/watson-developer-cloud/python-sdk.svg)](https://travis-ci.org/watson-developer-cloud/python-sdk)
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
The [examples](examples) folder has basic and advanced examples.

## Getting the Service Credentials
You will need the `username` and `password` credentials for each service these are *not* your Bluemix credentials.

To get your service credentials, follow these steps:
 1. Log in to Bluemix at https://bluemix.net.
 1. Create an instance of the service:
    1. In the Bluemix **Catalog**, select the Natural Language Classifier service.
    1. Under **Add Service**, type a unique name for the service instance in the Service name field. For example, type `my-service-name`. Leave the default values for the other options.
    1. Click **Use**.
 1. Copy your credentials:
    1. On the left side of the page, click **Service Credentials** to view your service credentials.
    1. Copy `username` and `password` from these service credentials.

## Python Version
Tested 👌 (lightly) on: Python from 2.6 to 3.5-dev (development branch)

## Dependencies
* [requests]
* [responses] (for testing)

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This library is licensed under the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0).

[wdc]: http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/
[vcap_environment]: http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/getting_started/index.html#EnvVars
[bluemix]: https://console.ng.bluemix.net
[pytest]: http://pytest.org/latest/
[responses]: https://github.com/getsentry/responses
[requests]: http://docs.python-requests.org/en/latest/
