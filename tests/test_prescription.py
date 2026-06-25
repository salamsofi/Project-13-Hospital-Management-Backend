from datetime import datetime


# Test Create Prescription
def test_create_prescription(client, auth_headers):

    # Create Doctor
    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
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
        headers=auth_headers
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
        headers=auth_headers
    )

    appointment_id = appointment_response.json()["id"]

    # Create Prescription
    response = client.post(
        "/prescriptions/",
        json={
            "medicines": ["Paracetamol", "Vitamin C"],
            "dosage": "Twice a day",
            "appointment_id": appointment_id
        },
        headers=auth_headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["dosage"] == "Twice a day"


# Get Prescription By ID
def test_get_prescription_by_id(client, auth_headers):

    # Create Doctor
    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
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
        headers=auth_headers
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
        headers=auth_headers
    )

    appointment_id = appointment_response.json()["id"]

    # Create Prescription
    create_response = client.post(
        "/prescriptions/",
        json={
            "medicines": ["Paracetamol"],
            "dosage": "Twice a day",
            "appointment_id": appointment_id
        },
        headers=auth_headers
    )

    prescription_id = create_response.json()["id"]

    response = client.get(
        f"/prescriptions/{prescription_id}",
        headers=auth_headers
    )

    assert response.status_code == 200

    assert response.json()["id"] == prescription_id


# Get All Prescriptions
def test_get_all_prescriptions(client, auth_headers):

    response = client.get(
        "/prescriptions/",
        headers=auth_headers
    )

    assert response.status_code == 200


# Test Update Prescription
def test_update_prescription(client, auth_headers):

    # Create Doctor
    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
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
        headers=auth_headers
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
        headers=auth_headers
    )

    appointment_id = appointment_response.json()["id"]

    # Create Prescription
    create_response = client.post(
        "/prescriptions/",
        json={
            "medicines": ["Paracetamol"],
            "dosage": "Twice a day",
            "appointment_id": appointment_id
        },
        headers=auth_headers
    )

    prescription_id = create_response.json()["id"]

    # Update Prescription
    response = client.put(
        f"/prescriptions/{prescription_id}",
        json={
            "medicines": ["Crocin"],
            "dosage": "Three times a day"
        },
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["medicines"] == ["Crocin"]
    assert data["dosage"] == "Three times a day"


# Test Delete Prescription
def test_delete_prescription(client, auth_headers):

    # Create Doctor
    doctor_response = client.post(
        "/doctors/",
        json={
            "name": "Dr. John",
            "specialization": "Cardiology"
        },
        headers=auth_headers
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
        headers=auth_headers
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
        headers=auth_headers
    )

    appointment_id = appointment_response.json()["id"]

    # Create Prescription
    create_response = client.post(
        "/prescriptions/",
        json={
            "medicines": ["Paracetamol"],
            "dosage": "Twice a day",
            "appointment_id": appointment_id
        },
        headers=auth_headers
    )

    prescription_id = create_response.json()["id"]

    # Delete Prescription
    response = client.delete(
        f"/prescriptions/{prescription_id}",
        headers=auth_headers
    )

    assert response.status_code == 204

    response = client.get(
        f"/prescriptions/{prescription_id}",
        headers=auth_headers
    )

    assert response.status_code == 404


# Negative Test
def test_get_non_existing_prescription(
    client,
    auth_headers
):

    response = client.get(
        "/prescriptions/99999",
        headers=auth_headers
    )

    assert response.status_code == 404