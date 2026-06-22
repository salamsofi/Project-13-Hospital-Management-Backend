from sqlalchemy.orm import Session

from app.core.logger import logger
from app.models.appointment import Appointment

from app.exceptions.appointment_exception import AppointmentNotFoundException
from app.repositories.appointment_repository import AppointmentRepository

from app.schemas.appointment_schema import (
    AppointmentCreate, 
    AppointmentUpdate
)


class AppointmentService:

    def __init__(
        self,
        appointment_repository: AppointmentRepository
    ):
        self.appointment_repository = appointment_repository


    def create_appointment(
        self,
        appointment_data: AppointmentCreate,
        db: Session
    ) -> Appointment:
        
        logger.info(
            f"Creating appointment for patient {appointment_data.patient_id}"
        )

        return self.appointment_repository.create(
            appointment_data,
            db
        )
    
    def get_all_appointment(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list[Appointment]:
        
        logger.info(
            f"Fetching all appointments"
        )
        
        return self.appointment_repository.get_all(
            db,
            skip,
            limit,
            search,
            sort_by,
            sort_order
        )
    
    def get_appointment_by_id(
        self,
        appointment_id: int,
        db: Session
    ):
        logger.info(
            f"Fetching appointment with id {appointment_id} "
        )
        
        appointment = self.appointment_repository.get_by_id(
            db,
            appointment_id
        )

        if appointment is None:
            logger.warning(
                f"Appointment with id {appointment_id} not found"
            )
            
            raise AppointmentNotFoundException(
                appointment_id
            )
        
        return appointment
    
    def update_appointment(
        self,
        appointment_id: int,
        appointment_data: AppointmentUpdate,
        db: Session
    ) -> Appointment:
        
        logger.info(
            f"Updating appointment {appointment_id}"
        )

        appointment = self.appointment_repository.get_by_id(
            db,
            appointment_id
        )

        if appointment is None:
            logger.warning(
                f"Appointment with id {appointment_id} not found"
            )

            raise AppointmentNotFoundException(
                appointment_id
            )
        
        return self.appointment_repository.update(
            appointment,
            appointment_data,
            db
        )
    
    def delete_appointment(
        self,
        db: Session,
        appointment_id: int
    ) -> None:
        
        logger.info(
            f"Deleted appointment {appointment_id}"
        )

        appointment = self.appointment_repository.get_by_id(
            db,
            appointment_id
        )

        if appointment is None:
            logger.warning(
                f"Appointment with id {appointment_id} not found"
            )

            raise AppointmentNotFoundException(
                appointment_id
            )
        
        self.appointment_repository.delete(
            appointment,
            db
        )