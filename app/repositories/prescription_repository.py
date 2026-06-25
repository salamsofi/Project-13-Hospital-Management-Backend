from sqlalchemy import select, asc, desc
from sqlalchemy.orm import Session, joinedload

from app.models.prescription import Prescription
from app.models.appointment import Appointment
from app.models.patient import Patient

from app.schemas.prescription_schema import (
    PrescriptionCreate,
    PrescriptionUpdate
)


class PrescriptionRepository:

    # create()
    def create(
        self,
        db: Session,
        prescription_data: PrescriptionCreate
    ) -> Prescription:
        
        new_prescription = Prescription(
            **prescription_data.model_dump()
        )

        db.add(new_prescription)
        db.commit()
        db.refresh(new_prescription)

        return new_prescription
    
    # get_all()
    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list[Prescription]:
        
        stmt = (
            select(Prescription)
            .options(
                joinedload(
                    Prescription.appointment
                ).joinedload(
                    Appointment.patient
                ).joinedload(
                    Patient.doctor
                )
            )
        )

        # Search by medicines
        if search:
            stmt = stmt.where(
                Prescription.dosageI.ilike(
                    f"%{search}%"
                )
            )

        # Sorting
        sort_column = getattr(
            Prescription,
            sort_by,
            Prescription.id
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
        stmt = stmt.offset(skip).limit(limit)

        return db.scalars(stmt).all()
    
    # get_by_id()
    def get_by_id(
        self,
        prescription_id: int,
        db: Session
    ) -> Prescription | None:
        
        stmt = (
            select(Prescription)
            .options(
                joinedload(
                    Prescription.appointment
                ).joinedload(
                    Appointment.patient
                ).joinedload(
                    Patient.doctor
                )
            )
            .where(
            Prescription.id == prescription_id
            )
        )

        return db.scalar(stmt)

    # update()
    def update(
        self,
        prescription: Prescription,
        prescription_data: PrescriptionUpdate,
        db: Session
    ) -> Prescription:
        
        update_data = prescription_data.model_dump()

        print(update_data)
        print(type(update_data["medicines"]))

        for key, value in update_data.items():
            setattr(
                prescription,
                key,
                value
            )

        db.commit()
        db.refresh(prescription)

        print("AFTER REFRESH")
        print(prescription.medicines)
        print(type(prescription.medicines))

        return prescription
    
    def delete(
        self,
        prescription: Prescription,
        db: Session
    ) -> None:
        
        db.delete(prescription)
        db.commit()

