from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_document():
    document_data = {
        "type_id": 1,
        "number": "1937475a",
        "date": datetime.now().strftime('%Y-%m-%d'),
    }

    response = client.post("/documents/", json=document_data)

    print(response.json())
    assert response.status_code == 200


def test_create_document_type():
    document_type_data = {
        "name": "My New Document Type"
    }

    response = client.post("/documents/types/", json=document_type_data)

    print(response.json())
    assert response.status_code == 200


def test_update_document_type():
    document_type_data = {
        "name": "updated document type",
    }

    response = client.patch("/documents/types/8/", json=document_type_data)

    print(response.json())
    assert response.status_code == 200
