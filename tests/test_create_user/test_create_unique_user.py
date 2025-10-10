import pytest
import requests
from helpers.api_client import ApiClient


def test_create_unique_user(base_url, generate_user_data):
    api_client = ApiClient(base_url)
    
    user_data = generate_user_data()
    response = api_client.create_user(user_data)
        
    api_client.check_response_status(response, 200)
    api_client.check_response_success(response, True)
    
    json_data = response.json()
    assert "user" in json_data
    assert json_data["user"]["email"] == user_data["email"]
    assert json_data["user"]["name"] == user_data["name"]
    assert "accessToken" in json_data
    assert "refreshToken" in json_data