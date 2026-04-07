import requests

BASE_URL = "http://localhost:5002"

def test_attack():

    data = {
        "attacker_attack": 10,
        "defender_defense": 4
    }

    r = requests.post(f"{BASE_URL}/battle/attack", json=data)

    assert r.status_code == 200

    result = r.json()

    assert result["damage"] == 6


def test_defend():

    r = requests.post(f"{BASE_URL}/battle/defend", json={"hero_id":1})

    assert r.status_code == 200


def test_turn_order():

    r = requests.post(
        f"{BASE_URL}/battle/turn-order",
        json={
            "units":[
                {"name":"hero","attack":8},
                {"name":"enemy","attack":5}
            ]
        }
    )

    assert r.status_code == 200
    order = r.json()

    assert order[0]["attack"] >= order[1]["attack"]