from fastapi.testclient import TestClient
from app.main import app
from app.schemas.item import ItemSchema

client = TestClient(app)

def test_create_item_route():
    response = client.post("/api/items/", json={"name": "Laptop", "description": "A powerful laptop", "price": 1000.0, "stock": 10})
    assert response.status_code == 200
    assert response.json() is not None

def test_get_item_route():
    create_response = client.post("/api/items/", json={"name": "Laptop", "description": "A powerful laptop", "price": 1000.0, "stock": 10})
    item_id = create_response.json()
    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Laptop"

def test_update_item_route():
    create_response = client.post("/api/items/", json={"name": "Laptop", "description": "A powerful laptop", "price": 1000.0, "stock": 10})
    item_id = create_response.json()
    update_response = client.put(f"/api/items/{item_id}", json={"name": "Laptop", "description": "An updated powerful laptop", "price": 1500.0, "stock": 5})
    assert update_response.status_code == 200
    assert update_response.json() == 1

def test_delete_item_route():
    create_response = client.post("/api/items/", json={"name": "Laptop", "description": "A powerful laptop", "price": 1000.0, "stock": 10})
    item_id = create_response.json()
    delete_response = client.delete(f"/api/items/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == 1
