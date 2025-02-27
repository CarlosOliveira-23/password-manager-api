from fastapi.testclient import TestClient


def test_register_user(client: TestClient):
    response = client.post("/auth/register/", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"


def test_login_user(client: TestClient):
    response = client.post("/auth/login/", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()
