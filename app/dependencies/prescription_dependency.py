from app.repositories.prescription_repository import (
    PrescriptionRepository
)

from app.services.prescription_service import PrescriptionService

def get_prescription_service() -> PrescriptionService:

    prescription_repository = PrescriptionRepository()

    return PrescriptionService(prescription_repository)