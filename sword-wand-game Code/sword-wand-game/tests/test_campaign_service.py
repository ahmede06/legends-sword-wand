import requests

BASE_URL = "http://localhost:5003"

def test_generate_room():

    r = requests.get(f"{BASE_URL}/campaign/room")

    assert r.status_code == 200

    room = r.json()

    assert room["type"] in ["battle","inn"]


def test_campaign_progress():

    r = requests.post(
        f"{BASE_URL}/campaign/progress",
        json={"player_id":1}
    )

    assert r.status_code == 200


def test_campaign_end():

    r = requests.post(
        f"{BASE_URL}/campaign/end",
        json={"player_id":1}
    )

    assert r.status_code == 200

    result = r.json()

    assert "score" in result