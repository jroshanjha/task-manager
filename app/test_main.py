from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "name": "Test User",
        "email": "testuser@example.com"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_single_user():
    # assuming user with ID 1 exists
    response = client.get("/users/1")
    if response.status_code == 200:
        assert response.json()["id"] == 1
    else:
        assert response.status_code == 404

def test_update_user():
    response = client.put("/users/1", json={
        "name": "Updated User",
        "email": "updated@example.com"
    })
    assert response.status_code in [200, 404]

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code in [200, 404]
