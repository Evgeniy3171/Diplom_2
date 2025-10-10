import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Создание пользователя")
@allure.title("Создание пользователя без заполнения обязательного поля password")
def test_create_user_without_password(base_url, generate_user_data):
    api_client = ApiClient(base_url)
    user_data = generate_user_data()
    user_data.pop("password")
    
    with allure.step("Создать пользователя без пароля"):
        response = api_client.create_user(user_data)
        
    api_client.check_response_status(response, 403)
    api_client.check_response_success(response, False)
    assert response.json().get("message") == "Email, password and name are required fields"