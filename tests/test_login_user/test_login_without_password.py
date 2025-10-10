import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Логин пользователя")
@allure.title("Вход без пароля")
def test_login_without_password(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Выполнить вход без пароля"):
        response = api_client.login_user({
            "email": registered_user["email"]
        })
        
    api_client.check_response_status(response, 401)
    api_client.check_response_success(response, False)
    assert response.json().get("message") == "email or password are incorrect"