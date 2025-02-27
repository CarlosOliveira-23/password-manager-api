from fastapi.testclient import TestClient


def test_store_password(client: TestClient):
    token = client.post("/auth/login/", json={"username": "testuser", "password": "testpass"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/api/passwords/", json={"service_name": "GitHub", "password": "mypassword"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["service_name"] == "GitHub"


def test_list_passwords(client: TestClient):
    token = client.post("/auth/login/", json={"username": "testuser", "password": "testpass"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/api/passwords/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
