from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.prescription import Prescription

from app.repositories.prescription_repository import (
    PrescriptionRepository
)

from app.exceptions.prescription_exception import (
    PrescriptionNotFoundException
)

from app.schemas.prescription_schema import (
    PrescriptionCreate,
    PrescriptionUpdate
)

class PrescriptionService:

    def __init__(
        self,
        prescription_repository: PrescriptionRepository
    ):
        self.prescription_repository = prescription_repository

    # create_prescription()
    def create_prescription(
        self,
        db: Session,
        prescription_data: PrescriptionCreate
    ) -> Prescription:
        
        logger.info(
            f"Creating prescription for appointment {prescription_data.appointment_id}"
        )
        
        return self.prescription_repository.create(
            db, 
            prescription_data
        )
    
    # get_all_prescriptions()
    def get_all_patients(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list[Prescription]:
        
        logger.info(
            "Fetching all prescriptions"
        )
        
        return self.prescription_repository.get_all(
            db,
            skip,
            limit,
            search,
            sort_by,
            sort_order
        )

    #  get_prescription_by_id()
    def get_prescription_by_id(
        self,
        db: Session,
        prescription_id: int
    ) -> Prescription:
        
        logger.info(
            f"Fetching prescription with id {prescription_id}"
        )

        prescription = self.prescription_repository.get_by_id(
            prescription_id,
            db
        )

        if prescription is None:
            logger.warning(
                f"Prescription with id {prescription_id} not found"
            )
            raise PrescriptionNotFoundException(
                prescription_id
            )
        
        return prescription

    # update_prescription()
    def update_prescription(
        self,
        db: Session,
        prescription_id: int,
        prescription_data: PrescriptionUpdate
    ) -> Prescription:
        
        logger.info(
            f"Updating prescription with id {prescription_id}"
        )

        prescription = self.prescription_repository.get_by_id(
            prescription_id,
            db
        )

        if prescription is None:
            logger.warning(
                f"Prescription with id {prescription_id} not found"
            )
            
            raise PrescriptionNotFoundException(
                prescription_id
            )
        
        return self.prescription_repository.update(
            prescription,
            prescription_data,
            db
        )
    
    # delete_prescription()
    def delete_patient(
        self,
        prescription_id: int,
        db: Session
    ) -> None:
        
        logger.info(
            f"Deleted prescription with id {prescription_id}"
        )

        prescription = self.prescription_repository.get_by_id(
            prescription_id,
            db
        )

        if prescription is None:
            logger.warning(
                f"Prescription with id {prescription_id} not found"
            )
            
            raise PrescriptionNotFoundException(
                prescription_id
            )
        
        self.prescription_repository.delete(
            prescription,
            db
        )

        return {
            "message": "Prescription deleted successfully"
        }