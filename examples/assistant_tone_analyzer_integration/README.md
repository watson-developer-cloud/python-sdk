# Assistant and Tone Analyzer Integration Example

This example provides sample code for integrating [Tone Analyzer][tone_analyzer] and [Assistant][assistant] in Python 2.6+.  All calls are made synchronously. For sample Python 3.5 asynchronous code, please see [https://github.com/aprilwebster/python-sdk][aprilwebster_python_sdk_github].

  * [tone_detection.py][tone_assistant_integration_example_tone_detection] - sample code to initialize a user object in the assistant payload's context (initUser), to call Tone Analyzer to retrieve tone for a user's input (invokeToneAsync), and to update tone in the user object in the assistant payload's context (updateUserTone).

  * [tone_assistant_integration.v1.py][tone_assistant_integration_example] - sample code to use tone_detection.py to get and add tone to the payload and send a request to the Assistant Service's message endpoint both in a synchronous and asynchronous manner.


Requirements to run the sample code

  * [Tone Analyzer Service credentials][ibm_cloud_tone_analyzer_service]
  * [Assistant Service credentials][ibm_cloud_assistant_service]
  * [Assistant Workspace ID][assistant_simple_workspace]

Credentials & the Workspace ID can be set in environment properties, a .env file, or directly in the code.

Dependencies provided in
`init.py`

Command to run the sample code

`python tone_assistant_integration.v1.py`

[assistant]: https://cloud.ibm.com/apidocs/assistant
[tone_analyzer]: https://cloud.ibm.com/apidocs/tone-analyzer
[ibm_cloud_assistant_service]: https://cloud.ibm.com/catalog/services/watson-assistant
[ibm_cloud_tone_analyzer_service]: https://cloud.ibm.com/catalog/services/tone-analyzer
[assistant_simple_workspace]: https://github.com/watson-developer-cloud/conversation-simple#workspace
[tone_assistant_integration_example]: https://github.com/watson-developer-cloud/python-sdk/tree/master/examples/assistant_tone_analyzer_integration/tone_assistant_integration.v1.py
[tone_assistant_integration_example_tone_detection]: https://github.com/watson-developer-cloud/python-sdk/tree/master/examples/assistant_tone_analyzer_integration/tone_detection.py
[aprilwebster_python_sdk_github]: https://github.com/aprilwebster/python-sdk