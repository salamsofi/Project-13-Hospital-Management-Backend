from datetime import date


# Test Create Appointment
def test_create_appointment(client, auth_headers):

    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    patient_response = client.post(
        "/patients/",
        json={
            "name": "Salam",
            "age": 23,
            "city": "Mumbai",
            "doctor_id": doctor_id
        },
        headers=auth_headers
    )

    patient_id = patient_response.json()["id"]

    payload = {
        "appointment_date": str(date.today()),
        "reason": "Fever",
        "patient_id": patient_id
    }

    response = client.post(
        "/appointments/",
        json=payload,
        headers=auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["reason"] == "Fever"


# Test Get Appointment By Id
def test_get_appointment_by_id(client, auth_headers):

    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    patient_response = client.post(
        "/patients/",
        json={
            "name": "Salam",
            "age": 23,
            "city": "Mumbai",
            "doctor_id": doctor_id
        },
        headers=auth_headers
    )

    patient_id = patient_response.json()["id"]

    create_response = client.post(
        "/appointments/",
        json={
            "appointment_date": str(date.today()),
            "reason": "Fever",
            "patient_id": patient_id
        },
        headers=auth_headers
    )

    appointment_id = create_response.json()["id"]

    response = client.get(
        f"/appointments/{appointment_id}",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == appointment_id


# Test Get All Appointments
def test_get_all_appointments(client, auth_headers):

    response = client.get(
        "/appointments/",
        headers=auth_headers
    )

    assert response.status_code == 200


# Test Update Appointment
def test_update_appointment(client, auth_headers):

    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    patient_response = client.post(
        "/patients/",
        json={
            "name": "Salam",
            "age": 23,
            "city": "Mumbai",
            "doctor_id": doctor_id
        },
        headers=auth_headers
    )

    patient_id = patient_response.json()["id"]

    create_response = client.post(
        "/appointments/",
        json={
            "appointment_date": str(date.today()),
            "reason": "Fever",
            "patient_id": patient_id
        },
        headers=auth_headers
    )

    appointment_id = create_response.json()["id"]

    update_payload = {
        "appointment_date": str(date.today()),
        "reason": "Headache",
        "patient_id": patient_id
    }

    response = client.put(
        f"/appointments/{appointment_id}",
        json=update_payload,
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["reason"] == "Headache"


# Test Delete Appointment
def test_delete_appointment(client, auth_headers):

    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
    )

    doctor_id = doctor_response.json()["id"]

    patient_response = client.post(
        "/patients/",
        json={
            "name": "Salam",
            "age": 23,
            "city": "Mumbai",
            "doctor_id": doctor_id
        },
        headers=auth_headers
    )

    patient_id = patient_response.json()["id"]

    create_response = client.post(
        "/appointments/",
        json={
            "appointment_date": str(date.today()),
            "reason": "Fever",
            "patient_id": patient_id
        },
        headers=auth_headers
    )

    appointment_id = create_response.json()["id"]

    response = client.delete(
        f"/appointments/{appointment_id}",
        headers=auth_headers
    )

    assert response.status_code == 204

    response = client.get(
        f"/appointments/{appointment_id}",
        headers=auth_headers
    )

    assert response.status_code == 404


# Negative Test
def test_get_non_existing_appointment(client, auth_headers):

    response = client.get(
        "/appointments/99999",
        headers=auth_headers
    )

    assert response.status_code == 404