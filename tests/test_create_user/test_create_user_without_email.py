import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Создание пользователя")
@allure.title("Создание пользователя без заполнения обязательного поля email")
def test_create_user_without_email(base_url, generate_user_data):
    api_client = ApiClient(base_url)
    user_data = generate_user_data()
    user_data.pop("email")
    
    with allure.step("Создать пользователя без email"):
        response = api_client.create_user(user_data)
        
    api_client.check_response_status(response, 403)
    api_client.check_response_success(response, False)
    assert response.json().get("message") == "Email, password and name are required fields"