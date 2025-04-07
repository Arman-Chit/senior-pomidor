base_url = "https://api.pomidor-stage.ru/api/v1"
HEADERS = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}

data = {
    "grant_type": "password",
    "username": "karman1488322@gmail.com",
    "password": "Qwerty12345",
    "scope":"",
    "client_id": "",
    "client_secret": ""
}

put_update_data = {
  "title": "updated_title",
  "description": "updated_description"
}

