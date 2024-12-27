from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_contract():
    contract_data = {
        "object_cost_kzt": 15000.3,
        "object_cost_usd": 200.1,
        "market_cost_kzt": 14000.3,
        "date": datetime.now().strftime('%Y-%m-%d'),
    }

    response = client.post("/contracts/", json=contract_data)

    print(response.json())
    assert response.status_code == 200
