from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

def test_create_user():
    # Use a unique email to avoid conflicts
    unique_email = f"testuser_{uuid.uuid4().hex[:8]}@example.com"
    response = client.post(
        "/users/",
        json={"name": "Test User", "email": unique_email}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == unique_email
    assert "id" in data
    assert "created_at" in data

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
