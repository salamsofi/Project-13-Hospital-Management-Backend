import uuid
from datetime import datetime
import pytest

# 1. Fixtures
def register_and_login(client, role):

    username = f"user_{uuid.uuid4().hex[:8]}"
    email = f"{username}@test.com"

    register_payload = {
        "username": username,
        "email": email,
        "password": "password123",
        "role": role
    }

    client.post(
        "/register",
        json=register_payload
    )

    login_payload = {
        "username": username,
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


@pytest.fixture
def admin_headers(client):
    return register_and_login(client, "admin")


@pytest.fixture
def doctor_headers(client):
    return register_and_login(client, "doctor")


@pytest.fixture
def receptionist_headers(client):
    return register_and_login(client, "receptionist")

# 2: Receptionist cannot create doctor
def test_receptionist_cannot_create_doctor(
    client,
    receptionist_headers
):

    response = client.post(
        "/doctors/",
        json={
            "name": "Dr Test",
            "specialization": "Cardiology"
        },
        headers=receptionist_headers
    )

    assert response.status_code == 403

# 3 Doctor cannot create doctor
def test_doctor_cannot_create_doctor(
    client,
    doctor_headers
):

    response = client.post(
        "/doctors/",
        json={
            "name": "Dr Test",
            "specialization": "Cardiology"
        },
        headers=doctor_headers
    )

    assert response.status_code == 403


# 4. Admin can create doctor
def test_admin_can_create_doctor(
    client,
    admin_headers
):

    response = client.post(
        "/doctors/",
        json={
            "name": "Dr Admin",
            "specialization": "Cardiology"
        },
        headers=admin_headers
    )

    assert response.status_code == 201


# 5. Receptionist can create patient
def test_receptionist_can_create_patient(
    client,
    admin_headers,
    receptionist_headers
):

    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Doctor",
            "specialization": "ENT"
        },
        headers=admin_headers
    )

    doctor_id = doctor_response.json()["id"]

    response = client.post(
        "/patients/",
        json={
            "name": "Salam",
            "age": 23,
            "city": "Mumbai",
            "doctor_id": doctor_id
        },
        headers=receptionist_headers
    )

    assert response.status_code == 201


# 6. Receptionist cannot create prescription
def test_receptionist_cannot_create_prescription(
    client,
    admin_headers,
    receptionist_headers
):

    # Create Doctor
    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr Admin",
            "specialization": "Cardiology"
        },
        headers=admin_headers
    )

    doctor_id = doctor_response.json()["id"]

    # Create Patient
    patient_response = client.post(
        "/patients/",
        json={
            "name": "Salam",
            "age": 23,
            "city": "Mumbai",
            "doctor_id": doctor_id
        },
        headers=admin_headers
    )

    patient_id = patient_response.json()["id"]

    # Create Appointment
    appointment_response = client.post(
        "/appointments/",
        json={
            "appointment_date": datetime.now().isoformat(),
            "reason": "Fever",
            "patient_id": patient_id
        },
        headers=admin_headers
    )

    appointment_id = appointment_response.json()["id"]

    # Receptionist tries to create Prescription
    response = client.post(
        "/prescriptions/",
        json={
            "medicines": ["Paracetamol"],
            "dosage": "Twice a day",
            "appointment_id": appointment_id
        },
        headers=receptionist_headers
    )

    assert response.status_code == 403


# 7. Doctor can create prescription
def test_doctor_can_create_prescription(
    client,
    admin_headers,
    doctor_headers
):

    # Create Doctor
    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr Admin",
            "specialization": "Cardiology"
        },
        headers=admin_headers
    )

    doctor_id = doctor_response.json()["id"]

    # Create Patient
    patient_response = client.post(
        "/patients/",
        json={
            "name": "Salam",
            "age": 23,
            "city": "Mumbai",
            "doctor_id": doctor_id
        },
        headers=admin_headers
    )

    patient_id = patient_response.json()["id"]

    # Create Appointment
    appointment_response = client.post(
        "/appointments/",
        json={
            "appointment_date": datetime.now().isoformat(),
            "reason": "Fever",
            "patient_id": patient_id
        },
        headers=admin_headers
    )

    appointment_id = appointment_response.json()["id"]

    # Doctor creates Prescription
    response = client.post(
        "/prescriptions/",
        json={
            "medicines": ["Paracetamol"],
            "dosage": "Twice a day",
            "appointment_id": appointment_id
        },
        headers=doctor_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["dosage"] == "Twice a day"