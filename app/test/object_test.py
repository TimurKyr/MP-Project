from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_object():
    object_data = {
        "create_user": "admin",
        "name": "New Test Object",
        "owner": {
            "bin": 123456789,
            "name": "first company",
            "abbreviation": "FC",
            "mp_share": 60,
        },
        "industry_id": 1,
        "address_id": 1,
        "year_construction": 2000,
        "year_purchase": 2010,
        "document": {
            "type_id": 1,
            "number": "30",
            "date": "2024-10-06"
        },
        "contract": {
            "object_cost_kzt": 150000000,
            "object_cost_usd": 300000,
            "market_cost_kzt": 130000000,
            "date": "2024-11-05"
        },
        "class_name": "A",
        "floors_below": 3,
        "floors_above": 15,
        "area_total": 15000.0,
        "area_rentable": 12000.0,
        "parking_closed": 300,
        "parking_open": 150,
        "plot_owned": 10000.0,
        "plot_rent": 20000.0,
        "status_id": 1,
    }

    response = client.post("/objects/", json=object_data)

    print(response.json())
    assert response.status_code == 200


def test_create_object_with_missing_field():
    object_data = {
        "industry_id": 1,
        "address_id": 1,
        "class_name": "New Building",
        "status_id": 1
    }

    response = client.post("/objects/", json=object_data)

    assert response.status_code == 422

    error_details = response.json()
    assert "owner_id" in str(error_details)


def test_update_object():
    object_data = {
        "update_user": "new_admin",
        "name": "Updated Name",
        "owner_bin": 11111,
        "industry_id": 1,
        "address_id": 1,
        "year_construction": 2000,
        "year_purchase": 2010,
        "document": {
            "type_id": 1,
            "number": "40",
            "date": "2024-10-06"
        },
        "contract": {
            "object_cost_kzt": 50000,
            "object_cost_usd": 2000,
            "market_cost_kzt": 40000,
            "date": "2024-11-05"
        },
        "class_name": "A",
        "floors_below": 3,
        "floors_above": 15,
        "status_id": 1,
    }

    response = client.patch("/objects/10/", json=object_data)

    print(response.json())
    assert response.status_code == 200
