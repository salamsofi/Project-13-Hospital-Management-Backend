from __future__ import annotations

from typing import TYPE_CHECKING

from datetime import datetime
from sqlalchemy import DateTime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.patient import Patient
    from app.models.prescription import Prescription

class Appointment(Base):

    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    appointment_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        nullable= False
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id")
    )

    patient: Mapped["Patient"] = relationship(
        "Patient",
        back_populates= "appointments"
    )

    prescriptions: Mapped[list["Prescription"]] = relationship(
        "Prescription",
        back_populates="appointment"
    )