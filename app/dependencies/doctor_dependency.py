from fastapi import Depends

from app.repositories.doctor_repository import DoctorRepository
from app.services.doctor_service import DoctorService


def get_doctor_repository() -> DoctorRepository:
    return DoctorRepository()


def get_doctor_service(
    doctor_repository: DoctorRepository = Depends(
        get_doctor_repository
    )
) -> DoctorService:

    return DoctorService(
        doctor_repository
    )