import pytest
import allure
from helpers.api_client import ApiClient


@allure.feature("Создание заказа")
@allure.title("Создание заказа без ингредиентов")
def test_create_order_without_ingredients(base_url, registered_user):
    api_client = ApiClient(base_url)
    
    with allure.step("Создать заказ без ингредиентов"):
        response = api_client.create_order([], registered_user["access_token"])
        
    api_client.check_response_status(response, 400)
    api_client.check_response_success(response, False)
    assert response.json().get("message") == "Ingredient ids must be provided"