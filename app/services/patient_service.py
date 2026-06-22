from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.patient import Patient

from app.exceptions.patient_exception import PatientNotFoundException
from app.repositories.patient_repository import PatientRepository

from app.schemas.patient_schema import (
    PatientCreate,
    PatientUpdate
)


class PatientService:

    def __init__(
        self,
        patient_repository: PatientRepository
    ):
        self.patient_repository = patient_repository

    def create_patient(
        self,
        db: Session,
        patient_data: PatientCreate
    ) -> Patient:
        
        logger.info(
            f"Creating patient {patient_data.name}"
        )

        return self.patient_repository.create(
            db,
            patient_data
        )

    def get_all_patients(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list[Patient]:
        
        logger.info(
            f"Fetching all patients"
        )

        return self.patient_repository.get_all(
            db,
            skip,
            limit,
            search,
            sort_by,
            sort_order
        )
    
    def get_patient_by_id(
        self,
        db: Session,
        patient_id: int
    ) -> Patient:
        
        logger.info(
            f"Fetching patient with id {patient_id}"
        )

        patient = self.patient_repository.get_by_id(
            db, 
            patient_id
        )

        if patient is None:
            
            logger.warning(
                f"Patient with id {patient_id} not found"
            )

            raise PatientNotFoundException(
                patient_id
            )
        
        return patient

    def update_patient(
        self,
        db: Session,
        patient_id: int,
        patient_data: PatientUpdate
    ) -> Patient:
        
        logger.info(
            f"Updating patient with id {patient_id}"
        )

        patient = self.patient_repository.get_by_id(
            db,
            patient_id
        )

        if patient is None:
            logger.warning(
                f"Patient with id {patient_id} not found"
            )

            raise PatientNotFoundException(
                patient_id
            )
        
        return self.patient_repository.update(
            db,
            patient,
            patient_data
        )
    
    def delete_patient(
        self,
        db: Session,
        patient_id: int
    ) -> None:
        
        logger.info(
            f"Deleting patient with id: {patient_id}"
        )

        patient = self.patient_repository.get_by_id(
            db,
            patient_id
        )

        if patient is None:
            logger.warning(
                f"Patient with id {patient_id} not found"
            )

            raise PatientNotFoundException(
                patient_id
            )

        self.patient_repository.delete(
            db,
            patient
        )        