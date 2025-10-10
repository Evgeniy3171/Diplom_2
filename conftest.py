import pytest
import requests
import random
import string


@pytest.fixture
def base_url():
    return "https://stellarburgers.education-services.ru/api"


@pytest.fixture
def generate_user_data():
    """Генерация случайных данных пользователя"""
    def _generate():
        email = f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@example.com"
        password = "password123"
        name = f"TestUser{random.randint(100, 999)}"
        return {"email": email, "password": password, "name": name}
    return _generate


@pytest.fixture
def registered_user(base_url, generate_user_data):
    """Фикстура для зарегистрированного пользователя"""
    try:
        user_data = generate_user_data()
        response = requests.post(f"{base_url}/auth/register", json=user_data, timeout=10)
        
        if response.status_code != 200:
            pytest.fail(f"Failed to register user. Status: {response.status_code}, Response: {response.text}")
            
        response_data = response.json()
        user_data["access_token"] = response_data.get("accessToken")
        return user_data
    except requests.exceptions.RequestException as e:
        pytest.skip(f"Cannot register user: {e}")


@pytest.fixture
def get_ingredients(base_url):
    """Получение списка ингредиентов"""
    try:
        response = requests.get(f"{base_url}/ingredients", timeout=10)
        
        if response.status_code != 200:
            pytest.fail(f"Failed to get ingredients. Status: {response.status_code}, Response: {response.text}")
            
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        pytest.skip(f"Cannot get ingredients: {e}")