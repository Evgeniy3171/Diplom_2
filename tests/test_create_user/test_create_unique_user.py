import pytest
import allure
from helpers.api_client import ApiClient


@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
@allure.story("Успешное создание пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_unique_user(base_url, generate_user_data):
    api_client = ApiClient(base_url)
    
    with allure.step("Подготовить данные нового пользователя"):
        user_data = generate_user_data()
        allure.attach(str(user_data), name="User Data", attachment_type=allure.attachment_type.JSON)
    
    with allure.step("Отправить запрос на создание пользователя"):
        response = api_client.create_user(user_data)
        allure.attach(f"Status Code: {response.status_code}\nResponse: {response.text}", 
                     name="API Response", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Проверить статус ответа"):
        api_client.check_response_status(response, 200)
    
    with allure.step("Проверить успешность операции"):
        api_client.check_response_success(response, True)
    
    with allure.step("Проверить данные в ответе"):
        json_data = response.json()
        assert "user" in json_data
        assert json_data["user"]["email"] == user_data["email"]
        assert json_data["user"]["name"] == user_data["name"]
        assert "accessToken" in json_data
        assert "refreshToken" in json_data
        
        allure.attach(str(json_data), name="Response JSON", attachment_type=allure.attachment_type.JSON)