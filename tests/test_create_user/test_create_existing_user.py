import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Создание пользователя")
@allure.title("Создание пользователя, который уже зарегистрирован")
def test_create_existing_user(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Попытаться создать пользователя с уже существующими данными"):
        response = api_client.create_user({
            "email": registered_user["email"],
            "password": registered_user["password"],
            "name": registered_user["name"]
        })
        
    api_client.check_response_status(response, 403)
    api_client.check_response_success(response, False)
    
    with allure.step("Проверить сообщение об ошибке"):
        assert response.json().get("message") == "User already exists"