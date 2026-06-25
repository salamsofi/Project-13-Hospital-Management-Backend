def test_get_all_doctors(client, auth_headers):

    response = client.get(
        "/doctors/",
        headers= auth_headers
    )

    assert response.status_code == 200

# Test Create Doctor
def test_create_doctor(client, auth_headers):

    payload = {
        "name": "John Doe",
        "specialization": "Cardiology"
    }

    response = client.post(
        "/doctors/",
        json= payload,
        headers= auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "John Doe"
    assert data["specialization"] == "Cardiology"

# Test Get Doctor by Id
def test_get_doctor_by_id(client, auth_headers):

    payload = {
        "name": "Alice",
        "specialization": "Neurology"
    }

    create_response = client.post(
        "/doctors/",
        json=payload,
        headers= auth_headers
    )

    doctor_id = create_response.json()["id"]

    response = client.get(
        f"/doctors/{doctor_id}",
        headers= auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == doctor_id


# Test Update Doctor
def test_update_doctor(client, auth_headers):

    payload = {
        "name": "Rahul",
        "specialization": "ENT"
    }

    create_response = client.post(
        "/doctors/",
        json=payload,
        headers= auth_headers
    )

    doctor_id = create_response.json()["id"]

    update_payload = {
        "name": "Rahul Updated",
        "specialization": "Dermatology"
    }

    response = client.put(
        f"/doctors/{doctor_id}",
        json=update_payload,
        headers= auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Rahul Updated"


# Test Delete Doctor
def test_delete_doctor(client, auth_headers):

    payload = {
        "name": "Delete Me",
        "specialization": "Cardiology"
    }

    create_response = client.post(
        "/doctors/",
        json=payload,
        headers= auth_headers
    )

    doctor_id = create_response.json()["id"]

    response = client.delete(
        f"/doctors/{doctor_id}",
        headers= auth_headers
    )

    assert response.status_code == 204


# Negative Test
def test_get_non_existing_doctor(client, auth_headers):

    response = client.get(
        "/doctors/99999",
        headers= auth_headers
    )

    assert response.status_code == 404