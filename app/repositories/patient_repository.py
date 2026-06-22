from sqlalchemy import select, asc, desc
from sqlalchemy.orm import Session, joinedload

from app.models.patient import Patient
from app.schemas.patient_schema import (
    PatientCreate, 
    PatientUpdate
)

class PatientRepository:

    def create(
        self,
        db: Session,
        patient_data: PatientCreate
    ) -> Patient:
        
        patient = Patient(
            **patient_data.model_dump()
        )

        db.add(patient)
        db.commit()
        db.refresh(patient)

        return patient


    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc",
    ) -> list[Patient]:
        
        stmt = select(Patient).options(
            joinedload(Patient.doctor)
        )

        # Search by patient name
        if search:
            stmt = stmt.where(
                Patient.name.ilike(
                    f"%{search}%"
                )
            )

        # Sorting
        sort_column = getattr(
            Patient,
            sort_by,
            Patient.id
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
            stmt
            .offset(skip)
            .limit(limit)
        )
        
        return db.scalars(stmt).all()
    

    def get_by_id(
        self,
        db: Session,
        patient_id: int  
    ) -> Patient | None:
        
        stmt = (
            select(Patient)
            .options(
                joinedload(Patient.doctor)
            )
            .where(Patient.id == patient_id)
        )

        return db.scalar(stmt)


    def update(
        self,
        db: Session,
        patient: Patient,
        patient_data: PatientUpdate
    ) -> Patient:
        
        update_data = patient_data.model_dump()

        for key, value in update_data.items():
            setattr(
                patient,
                key,
                value
            )

        return patient
    
    
    def delete(
        self,
        db: Session,
        patient: Patient
    ) -> None:
        
        db.delete(patient)
        db.commit()