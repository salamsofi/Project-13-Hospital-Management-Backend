import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():

    with TestClient(app) as c:
        yield c


@pytest.fixture
def auth_headers(client):
    unique_id = uuid.uuid4().hex

    register_payload = {
        "username": f"user_{unique_id}",
        "email": f"{unique_id}@test.com",
        "password": "password123",
        "role": "admin"
    }

    client.post(
        "/register",
        json=register_payload
    )

    login_payload = {
        "username": register_payload["username"],
        "password": "password123"
    }

    response = client.post(
        "/login",
        json=login_payload
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }