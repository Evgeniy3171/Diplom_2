import requests
import json


def check_api_availability():
    """Проверка доступности API endpoints"""
    base_url = "https://stellarburgers.education-services.ru/api"
    
    endpoints = {
        "GET /ingredients": f"{base_url}/ingredients",
        "POST /auth/register": f"{base_url}/auth/register",
        "POST /auth/login": f"{base_url}/auth/login", 
        "POST /orders": f"{base_url}/orders",
    }
    
    test_user = {
        "email": "test@example.com",
        "password": "password123",
        "name": "Test User"
    }
    
    print("🔍 Проверка доступности API Stellar Burgers...")
    print("=" * 60)
    
    for endpoint_name, url in endpoints.items():
        print(f"\n📡 Тестируем {endpoint_name}...")
        print(f"   URL: {url}")
        
        try:
            if endpoint_name == "GET /ingredients":
                response = requests.get(url, timeout=10)
            elif endpoint_name == "POST /auth/register":
                response = requests.post(url, json=test_user, timeout=10)
            elif endpoint_name == "POST /auth/login":
                response = requests.post(url, json=test_user, timeout=10)
            elif endpoint_name == "POST /orders":
                response = requests.post(url, json={"ingredients": []}, timeout=10)
            
            print(f"   ✅ Статус: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"   📊 Success: {data.get('success', 'N/A')}")
                    if endpoint_name == "GET /ingredients" and "data" in data:
                        print(f"   🍔 Ингредиентов: {len(data['data'])}")
                except json.JSONDecodeError:
                    print(f"   ❌ Ответ не в JSON формате: {response.text[:100]}...")
            else:
                print(f"   📝 Ответ: {response.text[:200]}...")
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Ошибка соединения")
        except requests.exceptions.Timeout:
            print(f"   ⏰ Таймаут запроса")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")


if __name__ == "__main__":
    check_api_availability()