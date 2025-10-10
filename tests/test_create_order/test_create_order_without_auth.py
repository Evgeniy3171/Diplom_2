import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Создание заказа")
@allure.title("Создание заказа без авторизации")
def test_create_order_without_auth(base_url, get_ingredients):
    api_client = ApiClient(base_url)
    
    with allure.step("Получить валидные ингредиенты"):
        ingredients = [ingredient["_id"] for ingredient in get_ingredients[:2]]
        
    with allure.step("Создать заказ без авторизации"):
        response = api_client.create_order(ingredients)
        
    api_client.check_response_status(response, 200)
    api_client.check_response_success(response, True)