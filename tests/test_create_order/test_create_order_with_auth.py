import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Создание заказа")
@allure.title("Создание заказа с авторизацией")
def test_create_order_with_auth(base_url, registered_user, get_ingredients):
    api_client = ApiClient(base_url)
    
    with allure.step("Получить валидные ингредиенты"):
        ingredients = [ingredient["_id"] for ingredient in get_ingredients[:2]]
        
    with allure.step("Создать заказ с авторизацией"):
        response = api_client.create_order(ingredients, registered_user["access_token"])
        
    api_client.check_response_status(response, 200)
    api_client.check_response_success(response, True)
    
    with allure.step("Проверить данные заказа"):
        json_data = response.json()
        assert "order" in json_data
        assert "number" in json_data["order"]
        assert "name" in json_data