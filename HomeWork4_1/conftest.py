import pytest
import requests


from HomeWork4_1.constant import headers, BASE_URL
from faker import Faker



faker= Faker()
@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(headers)


    response = requests.post(f"{BASE_URL}/auth", headers=headers,json={"username": "admin", "password": "password123"})
    assert response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data():
    return {
            "firstname": faker.first_name(),
            "lastname": faker.last_name(),
            "totalprice": faker.random_int(min=100,max=100000),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "Cigars"
        }


