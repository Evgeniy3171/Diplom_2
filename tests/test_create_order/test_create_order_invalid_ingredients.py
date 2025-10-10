import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Создание заказа")
@allure.title("Создание заказа с неверным хешем ингредиентов")
def test_create_order_invalid_ingredients(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Создать заказ с невалидными ингредиентами"):
        response = api_client.create_order(
            ["invalid_hash_1", "invalid_hash_2"], 
            registered_user["access_token"]
        )
        
    api_client.check_response_status(response, 500)