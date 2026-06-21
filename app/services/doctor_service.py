from sqlalchemy.orm import Session

from app.core.logger import logger
from app.exceptions.doctor_exception import DoctorNotFoundException
from app.models.doctor import Doctor
from app.repositories.doctor_repository import DoctorRepository
from app.schemas.doctor_schema import DoctorCreate, DoctorUpdate

class DoctorService:

    def __init__(
        self, 
        doctor_repository: DoctorRepository
    ):
        
        self.doctor_repository = doctor_repository

    
    def create_doctor(
        self,
        db: Session,
        doctor_data: DoctorCreate
    ) -> Doctor:

        logger.info(
            f"Creating doctor {doctor_data.name}"
        )

        return self.doctor_repository.create(
            db, 
            doctor_data
        )
    

    def get_all_doctors(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list[Doctor]:
        
        logger.info(
            f"Fetching all doctors"
        )
        
        return self.doctor_repository.get_all(
            db,
            skip,
            limit,
            search,
            sort_by,
            sort_order
        )


    def get_doctor_by_id(
        self,
        db: Session,
        doctor_id: int
    ) -> Doctor:

        logger.info(
            f"Fetching doctor with id {doctor_id}"
        )

        doctor = self.doctor_repository.get_by_id(
            db,
            doctor_id
        )

        if doctor is None:
            logger.warning(
                f"Doctor with id {doctor_id} not found"
            )

            raise DoctorNotFoundException(
                doctor_id
            )

        return doctor


    def update_doctor(
        self,
        db: Session,
        doctor_id: int,
        doctor_data: DoctorUpdate
    ) -> Doctor:
        
        doctor = self.doctor_repository.get_by_id(
            db,
            doctor_id
        )

        if doctor is None:
            logger.warning(
                f"Doctor with id {doctor_id} not found"
            )

            raise DoctorNotFoundException(
                doctor_id
            )

        logger.info(
            f"Updating doctor with id {doctor_id}"
        )

        return self.doctor_repository.update(
            db,
            doctor,
            doctor_data
        )
    

    def delete_doctor(
        self,
        db: Session,
        doctor_id: int
    ) -> None:
        
        doctor = self.doctor_repository.get_by_id(
            db,
            doctor_id
        )

        if doctor is None:
            logger.warning(
                f"Doctor with id {doctor_id} not found"
            )

            raise DoctorNotFoundException(
                doctor_id
            )
        
        logger.info(
            f"Deleting doctor with id {doctor_id}"
        )

        self.doctor_repository.delete(
            db,
            doctor
        )