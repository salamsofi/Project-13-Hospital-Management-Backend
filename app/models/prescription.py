from __future__ import annotations

from typing import TYPE_CHECKING

from app.db.database import Base

from sqlalchemy import ForeignKey, ARRAY, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.appointment import Appointment

class Prescription(Base):
    __tablename__ = "prescriptions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    medicines: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=False
    )

    dosage: Mapped[str] = mapped_column(
        nullable=False
    )

    appointment_id: Mapped[int] = mapped_column(
        ForeignKey("appointments.id")
    )

    appointment: Mapped["Appointment"] = relationship(
        "Appointment",
        back_populates="prescriptions"
    )