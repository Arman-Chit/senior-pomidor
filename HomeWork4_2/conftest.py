import faker
import pytest
import requests
from faker import Faker

from constant import HEADERS
from constant import base_url
from constant import data


@pytest.fixture(scope="session")
def auth_session():
    session = requests.session()
    auth_response = session.post(f"{base_url}/login/access-token", data=data, headers=HEADERS)
    token = auth_response.json().get("access_token")
    session.headers.update({"authorization": f"Bearer {token}"})
    return session


fake = Faker()


@pytest.fixture()
def item_data():
    return {
        "title": fake.word(),
        "description": fake.text()
    }