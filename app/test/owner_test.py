from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_owner():
    owner_data = {
        "bin": 987654,
        "name": "Test Owner",
        "abbreviation": "TO",
        "mp_share": 50,
        "create_user": "admin",
    }

    response = client.post("/owners/", json=owner_data)

    print(response.json())
    assert response.status_code == 200


def test_update_owner():
    owner_data = {
        "bin": 123456789,
        "name": "Компания 3",
        "abbreviation": "К3",
        "mp_share": 50,
        "update_user": "admin",
    }

    response = client.patch("/owners/7/", json=owner_data)

    print(response.json())
    assert response.status_code == 200
