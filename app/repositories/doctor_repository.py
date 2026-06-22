from sqlalchemy.orm import Session
from sqlalchemy import select, asc, desc

from app.models.doctor import Doctor
from app.schemas.doctor_schema import DoctorCreate, DoctorUpdate

class DoctorRepository:

    def create(
        self,
        db: Session,
        doctor_data: DoctorCreate
    ) -> Doctor:
        
        doctor = Doctor(
            name = doctor_data.name,
            specialization = doctor_data.specialization
        )

        db.add(doctor)
        db.commit()
        db.refresh(doctor)

        return doctor


    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list[Doctor]:
        
        stmt = select(Doctor)

        # Search by doctor name
        if search:
            stmt = stmt.where(
                Doctor.name.ilike(f"%{search}%")
            )

        # Sorting
        sort_column = getattr(
            Doctor,
            sort_by,
            Doctor.id
        )

        if sort_order == "desc":
            stmt = stmt.order_by(
                desc(sort_column)
            )
        else:
            stmt.order_by(
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
        doctor_id: int
    ) -> Doctor | None:
        
        stmt = (
            select(Doctor)
            .where(Doctor.id == doctor_id)
        )

        return db.scalar(stmt)


    def update(
            self,
            db: Session,
            doctor: Doctor,
            doctor_data: DoctorUpdate
    ) -> Doctor:
        
        doctor.name = doctor_data.name
        doctor.specialization = doctor_data.specialization

        db.commit()
        db.refresh(doctor)

        return doctor
        
        
    def delete(
        self,
        db: Session,
        doctor: Doctor
    ) -> None:
        
        db.delete(doctor)
        db.commit()