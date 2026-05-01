from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
huh
a
def test_normal_discount():

    response = client.get("/calculate/discount?price=1000&discount_percentage=20")
    assert response.status_code == 200
    assert response.json() == {"final_price": 800.00}

def test_invalid_discount():

    response = client.get("/calculate/discount?price=1000&discount_percentage=-10")
    assert response.status_code == 400
