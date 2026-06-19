from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.doctor import Doctor
    from app.models.appointment import Appointment

class Patient(Base):

    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        nullable=False
    )

    age: Mapped[int] = mapped_column(
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        nullable=False
    )

    doctor_id: Mapped[int] = mapped_column(
        ForeignKey("doctors.id")
    )

    doctor: Mapped["Doctor"] = relationship(
        "Doctor",
        back_populates="patients"
    )

    appointments: Mapped[list["Appointment"]] = relationship(
        "Appointment",
        back_populates="patient"
    )