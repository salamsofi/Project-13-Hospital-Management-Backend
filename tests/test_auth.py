import uuid

# Test Register
def test_register_user(client):

    payload = {
        "username": "testuser1",
        "email": "test1@test.com",
        "password": "password123",
        "role": "admin"
    }

    response = client.post(
        "/register",
        json=payload
    )

    print("\n")
    print("response.json()")
    print("\n")

    # assert response.status_code == 201

    # data = response.json()

    # assert data["username"] == payload["username"]
    # assert data["email"] == payload["email"]
    # assert data["role"] == payload["role"]


# Test Login
def test_login_user(client):

    register_payload = {
        "username": f"user_{uuid.uuid4().hex}",
        "email": f"{uuid.uuid4().hex}@test.com",
        "password": "password123",
        "role": "admin"
    }

    register_response = client.post(
        "/register",
        json=register_payload
    )

    assert register_response.status_code == 201

    login_payload = {
        "username": "testuser2",
        "password": "password123"
    }

    response = client.post(
        "/login",
        json=login_payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


# Test Invalid Password
def test_invalid_login(client):

    login_payload = {
        "username": "randomuser",
        "password": "wrongpassword"
    }

    response = client.post(
        "/login",
        json=login_payload
    )

    assert response.status_code == 401


# Test Duplicate Username
def test_duplicate_username(client):

    payload = {
        "username": "duplicateuser",
        "email": "duplicate@test.com",
        "password": "password123",
        "role": "admin"
    }

    client.post(
        "/register",
        json=payload
    )

    response = client.post(
        "/register",
        json=payload
    )

    assert response.status_code == 409