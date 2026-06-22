from sqlalchemy import select, asc, desc
from sqlalchemy.orm import Session, joinedload

from app.models.patient import Patient
from app.models.appointment import Appointment

from app.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate
)

class AppointmentRepository:
    def create(
        self,
        appointment_data: AppointmentCreate,
        db: Session
    ) -> Appointment:
        
        new_appointment = Appointment(
            **appointment_data.model_dump()
        )

        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)

        return new_appointment
    

    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list[Appointment]:

        stmt = (
            select(Appointment)
            .options(
                joinedload(
                    Appointment.patient
                ).joinedload(
                    Patient.doctor
                )
            )
        )

        # Search by reason
        if search:
            stmt = stmt.where(
                Appointment.reason.ilike(
                    f"%{search}%"
                )
            )

        # Sorting
        sort_column = getattr(
            Appointment,
            sort_by,
            Appointment.id
        )

        if sort_order == "desc":
            stmt = stmt.order_by(
                desc(sort_column)
            )
        else:
            stmt = stmt.order_by(
                asc(sort_column)
            )

        # Pagination
        stmt = (
            stmt.offset(skip).limit(limit)
        )

        return db.scalars(Appointment).all()
    

    def get_by_id(
        self,
        db: Session,
        appointment_id: int
    ) -> Appointment | None:
        
        stmt = (
            select(Appointment)
            .options(
                joinedload(
                    Appointment.patient
                ).joinedload(
                    Patient.doctor
                )
            )
            .where(Appointment.id == appointment_id)
        )

        return db.scalar(stmt)


    def update(
        self,
        appointment: Appointment,
        appointment_data: AppointmentUpdate,
        db: Session
    ) -> Appointment:
        
        update_data = Appointment(
            appointment_data.model_dump()
        )

        for key, value in update_data.items():
            setattr(
                appointment,
                key,
                value
            )

        db.commit(appointment)
        db.refresh(appointment)

        return appointment


    def delete(
        self,
        appointment: Appointment,
        db: Session
    ) -> None:
        
        db.delete(appointment)
        db.commit()

        