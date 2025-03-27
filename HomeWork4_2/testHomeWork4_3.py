import requests
import pytest
from constant4 import BASE_URL
from faker import Faker

faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    """Фикстура для аутентификации и установки сессии с токеном"""
    session = requests.Session()

    # Данные для авторизации
    data = {
        "grant_type": "password",
        "username": "admin",
        "password": "password123",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    # Запрос токена
    response = session.post(f"{BASE_URL}/login/access-token", data=data, headers=headers)

    assert response.status_code == 200, f"Ошибка авторизации: {response.status_code}, ответ: {response.text}"

    token = response.json().get("access_token")
    assert token, "Ошибка: токен не найден в ответе"

    # Добавляем заголовки с токеном
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    })

    return session


@pytest.fixture(scope="function")
def create_test_items(auth_session):
    """Создает тестовые элементы перед тестом"""
    session = auth_session

    for _ in range(10):
        data = {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100, max=100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "Cigars"
        }
        response = session.post(f"{BASE_URL}/items/", json=data)
        assert response.status_code == 201, f"Ошибка при создании тестового элемента: {response.text}"

    return session


@pytest.mark.usefixtures("auth_session", "create_test_items")
def test_pagination(auth_session):
    """Тест пагинации списка элементов"""

    session = auth_session

    # Запрос первой страницы
    response1 = session.get(f"{BASE_URL}/items/?skip=0&limit=10")
    assert response1.status_code == 200, f"Ошибка при получении первой страницы: {response1.text}"
    data1 = response1.json().get("data", [])  # Берем только список элементов
    assert len(data1) == 10, f"Ошибка: первая страница содержит {len(data1)} элементов, а не 10"

    # Запрос второй страницы
    response2 = session.get(f"{BASE_URL}/items/?skip=10&limit=10")
    assert response2.status_code == 200, f"Ошибка при получении второй страницы: {response2.text}"
    data2 = response2.json().get("data", [])  # Берем только список элементов
    assert len(data2) == 10, f"Ошибка: вторая страница содержит {len(data2)} элементов, а не 10"

    # Проверяем, что страницы разные
    assert data1 != data2, "Ошибка: данные на первой и второй странице одинаковые"

    print("Тест пагинации успешно пройден!")
