from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_industry():
    industry_data = {
        "create_user": "admin",
        "name": "Test Industry"
    }

    response = client.post("/industries/", json=industry_data)

    print(response.json())
    assert response.status_code == 200


def test_create_industry_with_missing_field():
    industry_data = {
        "name": "Wrong Industry"
    }

    response = client.post("/industries/", json=industry_data)

    assert response.status_code == 422

    error_details = response.json()
    assert "create_user" in str(error_details)


def test_update_industry():
    industry_data = {
        "update_user": "admin",
        "name": "updated industry",
    }

    response = client.patch("/industries/6/", json=industry_data)

    print(response.json())
    assert response.status_code == 200
