import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Логин пользователя")
@allure.title("Вход с неверным email")
def test_login_with_wrong_email(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Выполнить вход с неверным email"):
        response = api_client.login_user({
            "email": "wrong_email@example.com",
            "password": registered_user["password"]
        })
        
    api_client.check_response_status(response, 401)
    api_client.check_response_success(response, False)
    assert response.json().get("message") == "email or password are incorrect"