import requests

BASE_URL = "http://localhost:5000"

def test_register_user():
    data = {
        "username": "player1",
        "password": "password123"
    }

    r = requests.post(f"{BASE_URL}/register", json=data)

    assert r.status_code == 200
    assert r.json()["status"] == "success"


def test_login_user():
    data = {
        "username": "player1",
        "password": "password123"
    }

    r = requests.post(f"{BASE_URL}/login", json=data)

    assert r.status_code == 200
    assert "token" in r.json()


def test_login_invalid_user():
    data = {
        "username": "wronguser",
        "password": "wrongpass"
    }

    r = requests.post(f"{BASE_URL}/login", json=data)

    assert r.status_code == 401