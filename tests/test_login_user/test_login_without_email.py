import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Логин пользователя")
@allure.title("Вход без email")
def test_login_without_email(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Выполнить вход без email"):
        response = api_client.login_user({
            "password": registered_user["password"]
        })
        
    api_client.check_response_status(response, 401)
    api_client.check_response_success(response, False)
    assert response.json().get("message") == "email or password are incorrect"