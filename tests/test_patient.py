# Test Create Patient
def test_create_patient(client, auth_headers):

    doctor_payload = {
        "name": "Dr. John",
        "specialization": "Cardiology"
    }

    doctor_response = client.post(
        "/doctors/",
        json=doctor_payload,
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    payload = {
        "name": "Salam",
        "age": 23,
        "city": "Mumbai",
        "doctor_id": doctor_id
    }

    response = client.post(
        "/patients/",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Salam"


# Test Get Patients By ID
def test_get_patient_by_id(client, auth_headers):

    doctor_payload = {
        "name": "Dr. John",
        "specialization": "Cardiology"
    }

    doctor_response = client.post(
        "/doctors/",
        json=doctor_payload,
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    patient_payload = {
        "name": "Salam",
        "age": 23,
        "city": "Mumbai",
        "doctor_id": doctor_id
    }

    create_response = client.post(
        "/patients/",
        json=patient_payload,
        headers=auth_headers
    )

    patient_id = create_response.json()["id"]

    response = client.get(
        f"/patients/{patient_id}",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == patient_id
    assert data["name"] == "Salam"



# Test Get All Patients
def test_get_all_patients(client, auth_headers):

    response = client.get(
        "/patients/",
        headers=auth_headers
    )

    assert response.status_code == 200

# Test Update Patient
def test_update_patient(client, auth_headers):

    doctor_payload = {
        "name": "Dr. John",
        "specialization": "Cardiology"
    }

    doctor_response = client.post(
        "/doctors/",
        json=doctor_payload,
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    patient_payload = {
        "name": "Salam",
        "age": 23,
        "city": "Mumbai",
        "doctor_id": doctor_id
    }

    create_response = client.post(
        "/patients/",
        json=patient_payload,
        headers=auth_headers
    )

    patient_id = create_response.json()["id"]

    update_payload = {
        "name": "Salam Updated",
        "age": 24,
        "city": "Delhi",
        "doctor_id": doctor_id
    }

    response = client.put(
        f"/patients/{patient_id}",
        json=update_payload,
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Salam Updated"
    assert data["age"] == 24
    assert data["city"] == "Delhi"

# Test Delete Patient
def test_delete_patient(client, auth_headers):

    doctor_payload = {
        "name": "Dr. John",
        "specialization": "Cardiology"
    }

    doctor_response = client.post(
        "/doctors/",
        json=doctor_payload,
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    patient_payload = {
        "name": "Salam",
        "age": 23,
        "city": "Mumbai",
        "doctor_id": doctor_id
    }

    create_response = client.post(
        "/patients/",
        json=patient_payload,
        headers=auth_headers
    )

    patient_id = create_response.json()["id"]

    response = client.delete(
        f"/patients/{patient_id}",
        headers=auth_headers
    )

    assert response.status_code == 204

    response = client.get(
        f"/patients/{patient_id}",
        headers=auth_headers
    )

    assert response.status_code == 404


# Negative Test
def test_get_non_existing_patient(
    client,
    auth_headers
):

    response = client.get(
        "/patients/99999",
        headers=auth_headers
    )

    assert response.status_code == 404