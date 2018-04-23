# Watson Developer Cloud Python SDK

[![Build Status](https://travis-ci.org/watson-developer-cloud/python-sdk.svg?branch=master)](https://travis-ci.org/watson-developer-cloud/python-sdk)
[![Slack](https://wdc-slack-inviter.mybluemix.net/badge.svg)](https://wdc-slack-inviter.mybluemix.net)
[![codecov.io](https://codecov.io/github/watson-developer-cloud/python-sdk/coverage.svg?branch=master)](https://codecov.io/github/watson-developer-cloud/python-sdk?branch=master)
[![Latest Stable Version](https://img.shields.io/pypi/v/watson-developer-cloud.svg)](https://pypi.python.org/pypi/watson-developer-cloud)

Python client library to quickly get started with the various [Watson APIs][wdc] services.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade watson-developer-cloud
```

or

```bash
easy_install --upgrade watson-developer-cloud
```

Note the following:

a) If you run into permission issues try:

```bash
sudo -H pip install --ignore-installed six watson-developer-cloud
```

For more details see [#225](https://github.com/watson-developer-cloud/python-sdk/issues/225)

b) In case you run into problems installing the SDK in DSX, try
```
!pip install --upgrade pip
```
Restarting the kernel

For more details see [#405](https://github.com/watson-developer-cloud/python-sdk/issues/405)

## Examples

The [examples][examples] folder has basic and advanced examples.

## Getting the Service Credentials

Service credentials are required to access the APIs.

If you run your app in IBM Cloud, you don't need to specify the username and password or IAM API key (`apikey`). In that case, the SDK uses the `VCAP_SERVICES` environment variable to load the credentials.
To run locally or outside of IBM Cloud you need the `username` and `password` credentials or IAM API key (`apikey`) for each service. (Service credentials are different from your IBM Cloud account email and password.)

To create an instance of the service:

1. Log in to [IBM Cloud][ibm_cloud].
1. Create an instance of the service:
   1. Click on **Create Resource**.
   1. In the IBM Cloud **Catalog**, select the Watson service you want to use. For example, select the Conversation service.
   1. Type a unique name for the service instance in the **Service name** field. For example, type `my-service-name`. Leave the default values for the other options.
   1. Click **Create**.

To get your service credentials:

Copy your credentials from the **Manage** page. To find the Service details page for an existing service, navigate to your [IBM Cloud][ibm_cloud] dashboard and click the service name.

1. On the **Manage** page, you will see a **Credentials** pane
1. Depending on the service you will see use either:
* 2.a: `username`, `password`, and `url`(optional).
* 2.b: `apikey` which is the value for parameter `iam_api_key` when initializing the constructor.

## Python Version

Tested on Python 2.7, 3.4, 3.5, and 3.6.

## Changes for v1.0
Version 1.0 focuses on the move to programmatically-generated code for many of the services. See the [changelog](https://github.com/watson-developer-cloud/python-sdk/wiki/Changelog) for the details.

## Migration
This version includes many breaking changes as a result of standardizing behavior across the new generated services. Full details on migration from previous versions can be found [here](https://github.com/watson-developer-cloud/python-sdk/wiki/Migration).

## Configuring the http client (Supported from v1.1.0)
To set client configs like timeout use the `with_http_config()` function and pass it a dictionary of configs.

```python
from watson_developer_cloud import AssistantV1

assistant = AssistantV1(
    username='xxx',
    password='yyy',
    version='2017-04-21')

assistant.set_http_config({'timeout': 100})
response = assistant.message(workspace_id=workspace_id, input={
    'text': 'What\'s the weather like?'})
print(json.dumps(response, indent=2))
```

## Sending Request Headers
Custom headers can be passed in any request in the form of a `dict` as:
```python
headers = {
    'Custom-Header': 'custom_value'
}
```
For example, to send a header called `Custom-Header` to a call in Watson Assistant, pass
the headers parameter as:
```python
from watson_developer_cloud import AssistantV1

assistant = AssistantV1(
    username='xxx',
    password='yyy',
    version='2017-04-21')

response = assistant.list_workspaces(headers={'Custom-Header': 'custom_value'})
```

## Parsing HTTP Response Info
If you would like access to some HTTP response information along with the response model, you can set the `set_detailed_response()` to `True`
```python
from watson_developer_cloud import AssistantV1

assistant = AssistantV1(
    username='xxx',
    password='yyy',
    version='2017-04-21')

assistant.set_detailed_response(True)
response = assistant.list_workspaces(headers={'Custom-Header': 'custom_value'})
print(response)
```

This would give an output of `DetailedResponse` having the structure:
```python
{
    'result': <response returned by service>,
    'headers': { <http response headers> }
}
```
You can use the `get_result()` and `get_headers()` to return the result and headers respectively.

## Dependencies

* [requests]
* `python_dateutil` >= 2.5.3
* [responses] for testing
* Following for web sockets support in speech to text
   * `autobahn` >= 0.10.9
   * `Twisted` >= 13.2.0
   * `pyOpenSSL` >= 16.2.0
   * `service-identity` >= 17.0.0

## Contributing

See [CONTRIBUTING.md][CONTRIBUTING].

## License

This library is licensed under the [Apache 2.0 license][license].

[wdc]: http://www.ibm.com/watson/developercloud/
[ibm_cloud]: https://console.bluemix.net
[responses]: https://github.com/getsentry/responses
[requests]: http://docs.python-requests.org/en/latest/
[examples]: https://github.com/watson-developer-cloud/python-sdk/tree/master/examples
[CONTRIBUTING]: https://github.com/watson-developer-cloud/python-sdk/blob/master/CONTRIBUTING.md
[license]: http://www.apache.org/licenses/LICENSE-2.0
