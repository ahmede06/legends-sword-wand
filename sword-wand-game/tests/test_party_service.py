import requests

BASE_URL = "http://localhost:5001"

def test_create_hero():

    hero = {
        "name": "Arin",
        "class": "Warrior"
    }

    r = requests.post(f"{BASE_URL}/hero/create", json=hero)

    assert r.status_code == 200
    data = r.json()

    assert data["name"] == "Arin"
    assert data["class"] == "Warrior"
    assert data["level"] == 1


def test_level_up():

    r = requests.post(f"{BASE_URL}/hero/levelup", json={"hero_id":1})

    assert r.status_code == 200
    data = r.json()

    assert data["level"] > 1


def test_add_to_party():

    r = requests.post(
        f"{BASE_URL}/party/add",
        json={"party_id":1,"hero_id":1}
    )

    assert r.status_code == 200