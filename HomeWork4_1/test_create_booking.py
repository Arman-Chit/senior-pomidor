from constant import BASE_URL

def test_create_booking(auth_session, booking_data):
    """Тест создания бронирования (POST /booking)"""
    response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200, "Ошибка: бронирование не создано"
    assert "bookingid" in response.json(), "Ошибка: отсутствует идентификатор бронирования"


def test_get_booking(auth_session, booking_data):
    """Тест получения конкретного бронирования (GET /booking/{booking_id})"""
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    booking_id = create_response.json().get("bookingid")

    response = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 200, "Ошибка: не удалось получить бронирование"
    assert response.json()["firstname"] == booking_data["firstname"], "Ошибка: данные бронирования не совпадают"


def test_update_booking(auth_session, booking_data):
    """Тест обновления бронирования (PUT /booking/{booking_id})"""
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    booking_id = create_response.json().get("bookingid")

    updated_data = booking_data.copy()
    updated_data["firstname"] = "UpdatedName"
    update_response = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=updated_data)
    assert update_response.status_code == 200, "Ошибка: бронирование не обновлено"


def test_partial_update_booking(auth_session, booking_data):
    """Тест частичного обновления бронирования (PATCH /booking/{booking_id})"""
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    booking_id = create_response.json().get("bookingid")

    patch_data = {"lastname": "PatchedLastName"}
    patch_response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_data)
    assert patch_response.status_code == 200, "Ошибка: частичное обновление не выполнено"
    print(patch_data)

def test_delete_booking(auth_session, booking_data):
    """Тест удаления бронирования (DELETE /booking/{booking_id})"""
    create_response = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
    booking_id = create_response.json().get("bookingid")

    delete_response = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
    assert delete_response.status_code == 201, "Ошибка: бронирование не удалено"


def test_get_all_bookings(auth_session):
    """Тест получения списка всех бронирований (GET /booking)"""
    response = auth_session.get(f"{BASE_URL}/booking")
    assert response.status_code == 200, "Ошибка: не удалось получить список бронирований"
    assert isinstance(response.json(), list), "Ошибка: список бронирований отсутствует"


def test_update_nonexistent_booking(auth_session):
    """Тест обновления несуществующего бронирования (PUT /booking/{booking_id})"""
    nonexistent_id = 9999999999
    updated_data = {"firstname": "Test"}
    response = auth_session.put(f"{BASE_URL}/booking/{nonexistent_id}", json=updated_data)
    assert response.status_code == 400, "Ошибка: сервер не вернул 400 при обновлении несуществующего бронирования"
