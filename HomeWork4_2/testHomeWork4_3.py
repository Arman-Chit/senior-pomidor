BASE_URL = "https://api.pomidor-stage.ru/api/v1/users/me"
headers = headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}


def test_pagination():
    """Тест пагинации списка элементов"""
    # Запрос первой страницы
    response1 = requests.get(f"{BASE_URL}/items/?skip=0&limit=10", headers=headers)
    assert response1.status_code == 200, "Ошибка при получении первой страницы"
    data1 = response1.json()
    assert len(data1) == 10, "Ошибка: первая страница не содержит 10 элементов"

    # Запрос второй страницы
    response2 = requests.get(f"{BASE_URL}/items/?skip=10&limit=10", headers=headers)
    assert response2.status_code == 200, "Ошибка при получении второй страницы"
    data2 = response2.json()
    assert len(data2) == 10, "Ошибка: вторая страница не содержит 10 элементов"

    # Проверяем, что страницы разные
    assert data1 != data2, "Ошибка: данные на первой и второй странице одинаковые"

    print("Тест пагинации успешно пройден!")

test_pagination()