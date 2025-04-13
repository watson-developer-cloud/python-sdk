import os
import requests
from watson_developer_cloud import DiscoveryV2

# Disable SSL verification globally for requests made by Watson SDK
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Set your Watson Discovery credentials
api_key = "YOUR_API_KEY"
service_url = "YOUR_SERVICE_URL"
version = "2021-08-01"  # Specify the correct API version

# Instantiate the Discovery V2 client
discovery = DiscoveryV2(
    version=version,
    iam_apikey=api_key,
    url=service_url,
    disable_ssl_verification=True  # Disable SSL verification here
)

# Example: Get the list of collections (as a test endpoint)
try:
    response = discovery.list_collections(
        environment_id="YOUR_ENVIRONMENT_ID"
    ).get_result()
    print("Collections retrieved successfully:")
    print(response)
except Exception as e:
    print(f"Error: {str(e)}")

