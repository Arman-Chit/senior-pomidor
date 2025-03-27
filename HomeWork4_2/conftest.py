import pytest
import requests
from constant4 import BASE_URL
from faker import Faker
pytest_plugins = ["fixtures"]
faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()

    # Данные для авторизации в нужном формате
    data = {
        "grant_type": "password",
        "username": "karman1488322@gmail.com",
        "password": "Qwerty12345",
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

    assert response.status_code == 200, f"Ошибка авторизации, статус код {response.status_code}, ответ: {response.text}"

    token = response.json().get("access_token")
    assert token, "Ошибка: токен не найден в ответе"

    # Добавляем заголовки с токеном
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session


@pytest.fixture()
def item_data():
    return {
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
