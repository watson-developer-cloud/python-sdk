import responses
from watson_developer_cloud import iam_token_manager
import time

@responses.activate
def test_request_token():
    iam_url = "https://iam.bluemix.net/identity/token"
    response = """{
        "access_token": "oAeisG8yqPY7sFR_x66Z15",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": 1524167011,
        "refresh_token": "jy4gl91BQ"
    }"""
    responses.add(responses.POST, url=iam_url, body=response, status=200)

    token_manager = iam_token_manager.IAMTokenManager("iam_api_key", "iam_access_token", iam_url)
    token_manager._request_token()

    assert responses.calls[0].request.url == iam_url
    assert responses.calls[0].response.text == response
    assert len(responses.calls) == 1

@responses.activate
def test_refresh_token():
    iam_url = "https://iam.bluemix.net/identity/token"
    response = """{
        "access_token": "oAeisG8yqPY7sFR_x66Z15",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": 1524167011,
        "refresh_token": "jy4gl91BQ"
    }"""
    responses.add(responses.POST, url=iam_url, body=response, status=200)

    token_manager = iam_token_manager.IAMTokenManager("iam_api_key", "iam_access_token", iam_url)
    token_manager._refresh_token()

    assert responses.calls[0].request.url == iam_url
    assert responses.calls[0].response.text == response
    assert len(responses.calls) == 1

@responses.activate
def test_is_token_expired():
    token_manager = iam_token_manager.IAMTokenManager("iam_api_key", "iam_access_token", "iam_url")
    token_manager.token_info = {
        "access_token": "oAeisG8yqPY7sFR_x66Z15",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": int(time.time()) + 6000,
        "refresh_token": "jy4gl91BQ"
    }
    assert token_manager._is_token_expired() is False
    token_manager.token_info['expiration'] = int(time.time()) - 3600
    assert token_manager._is_token_expired()

@responses.activate
def test_is_refresh_token_expired():
    token_manager = iam_token_manager.IAMTokenManager("iam_api_key", "iam_access_token", "iam_url")
    token_manager.token_info = {
        "access_token": "oAeisG8yqPY7sFR_x66Z15",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": int(time.time()),
        "refresh_token": "jy4gl91BQ"
    }
    assert token_manager._is_refresh_token_expired() is False
    token_manager.token_info['expiration'] = int(time.time()) - (8 * 24 * 3600)
    assert token_manager._is_token_expired()

@responses.activate
def test_get_token():
    iam_url = "https://iam.bluemix.net/identity/token"
    token_manager = iam_token_manager.IAMTokenManager("iam_api_key", iam_url=iam_url)
    token_manager.user_access_token = 'user_access_token'

    # Case 1:
    token = token_manager.get_token()
    assert token == token_manager.user_access_token

    # Case 2:
    token_manager.user_access_token = ''
    response = """{
        "access_token": "hellohello",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": 1524167011,
        "refresh_token": "jy4gl91BQ"
    }"""
    responses.add(responses.POST, url=iam_url, body=response, status=200)
    token = token_manager.get_token()
    assert token == "hellohello"

    # Case 3:
    token_manager.token_info['expiration'] = int(time.time()) - (20 * 24 * 3600)
    token = token_manager.get_token()
    assert "grant_type=urn" in responses.calls[1].request.body
    token_manager.token_info['expiration'] = int(time.time()) - 4000
    token = token_manager.get_token()
    assert "grant_type=refresh_token" in responses.calls[2].request.body

    # Case 4
    token_manager.token_info = {
        "access_token": "dummy",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": int(time.time()) + 3600,
        "refresh_token": "jy4gl91BQ"
    }
    token = token_manager.get_token()
    assert token == 'dummy'
