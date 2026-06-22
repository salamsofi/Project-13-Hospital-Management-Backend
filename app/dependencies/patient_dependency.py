from app.repositories.patient_repository import PatientRepository
from app.services.patient_service import PatientService

def get_patient_service() -> PatientService:

    patient_repository = PatientRepository()

    return PatientService(patient_repository)