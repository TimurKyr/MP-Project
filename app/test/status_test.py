from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_status():
    status_data = {
        "name": "В Эксплуатации",
        "create_user": "admin",
    }

    response = client.post("/statuses/", json=status_data)

    print(response.json())
    assert response.status_code == 200


def test_update_status():
    status_data = {
        "update_user": "admin",
        "name": "В Ремонте",
    }

    response = client.patch("/statuses/12/", json=status_data)

    print(response.json())
    assert response.status_code == 200
