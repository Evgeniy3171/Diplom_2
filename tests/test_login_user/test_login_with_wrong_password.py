import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Логин пользователя")
@allure.title("Вход с неверным паролем")
def test_login_with_wrong_password(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Выполнить вход с неверным паролем"):
        response = api_client.login_user({
            "email": registered_user["email"],
            "password": "wrong_password"
        })
        
    api_client.check_response_status(response, 401)
    api_client.check_response_success(response, False)
    assert response.json().get("message") == "email or password are incorrect"