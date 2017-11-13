# Watson Developer Cloud Python SDK

[![Build Status](https://travis-ci.org/watson-developer-cloud/python-sdk.svg)](https://travis-ci.org/watson-developer-cloud/python-sdk)
[![Slack](https://wdc-slack-inviter.mybluemix.net/badge.svg)](https://wdc-slack-inviter.mybluemix.net)
[![codecov.io](https://codecov.io/github/watson-developer-cloud/python-sdk/coverage.svg?branch=master)](https://codecov.io/github/watson-developer-cloud/python-sdk?branch=master)
[![Latest Stable Version](https://img.shields.io/pypi/v/watson-developer-cloud.svg)](https://pypi.python.org/pypi/watson-developer-cloud)

Python client library to quickly get started with the various [Watson Developer Cloud][wdc] services.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade watson-developer-cloud
```

or

```bash
easy_install --upgrade watson-developer-cloud
```

Note: If you run into permission issues try:

```bash
sudo -H pip install --ignore-installed six watson-developer-cloud
```

For more details see [#225](https://github.com/watson-developer-cloud/python-sdk/issues/225)

## Examples

The [examples][examples] folder has basic and advanced examples.

## Getting the Service Credentials

Service credentials are required to access the APIs.

If you run your app in Bluemix, you don't need to specify the username and password. In that case, the SDK uses the `VCAP_SERVICES` environment variable to load the credentials.

To run locally or outside of Bluemix you need the `username` and `password` credentials for each service. (Service credentials are different from your Bluemix account email and password.)

To create an instance of the service:

1. Log in to [Bluemix][bluemix].
1. Create an instance of the service:
   1. In the Bluemix **Catalog**, select the Watson service you want to use. For example, select the Conversation service.
   1. Type a unique name for the service instance in the **Service name** field. For example, type `my-service-name`. Leave the default values for the other options.
   1. Click **Create**.

To get your service credentials:

Copy your credentials from the **Service details** page. To find the the Service details page for an existing service, navigate to your Bluemix dashboard and click the service name.

1. On the **Service Details** page, click **Service Credentials**, and then **View credentials**.
1. Copy `username` and `password`.

## Python Version

Tested on Python 2.7, 3.4, 3.5, and 3.6.

## Changes for v1.0
Version 1.0 focuses on the move to programmatically-generated code for many of the services. See the [changelog](https://github.com/watson-developer-cloud/python-sdk/wiki/Changelog) for the details.

## Migration
This version includes many breaking changes as a result of standardizing behavior across the new generated services. Full details on migration from previous versions can be found [here](https://github.com/watson-developer-cloud/python-sdk/wiki/Migration).

## Known Issues

See [issues](https://github.com/watson-developer-cloud/python-sdk/issues).

## Dependencies

* [requests]
* `pysolr` >=3.3, <4.0
* `argparse` >=1.3.0
* `pyOpenSSL` >=16.2.0
* `python_dateutil` >= 2.5.3
* [responses] for testing

## Contributing

See [CONTRIBUTING.md][CONTRIBUTING].

## License

This library is licensed under the [Apache 2.0 license][license].

[wdc]: http://www.ibm.com/watson/developercloud/
[bluemix]: https://console.bluemix.net
[responses]: https://github.com/getsentry/responses
[requests]: http://docs.python-requests.org/en/latest/
[examples]: https://github.com/watson-developer-cloud/python-sdk/tree/master/examples
[CONTRIBUTING]: https://github.com/watson-developer-cloud/python-sdk/blob/master/CONTRIBUTING.md
[license]: http://www.apache.org/licenses/LICENSE-2.0
