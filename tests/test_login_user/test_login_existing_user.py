import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Логин пользователя")
@allure.title("Вход под существующим пользователем")
def test_login_existing_user(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Выполнить вход с корректными данными"):
        response = api_client.login_user({
            "email": registered_user["email"],
            "password": registered_user["password"]
        })
        
    api_client.check_response_status(response, 200)
    api_client.check_response_success(response, True)
    
    with allure.step("Проверить данные в ответе"):
        json_data = response.json()
        assert "accessToken" in json_data
        assert "refreshToken" in json_data
        assert "user" in json_data
        assert json_data["user"]["email"] == registered_user["email"]
        assert json_data["user"]["name"] == registered_user["name"]