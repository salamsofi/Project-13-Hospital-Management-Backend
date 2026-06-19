from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.patient import Patient

from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class Doctor(Base):

    __tablename__ = "doctors"

    id : Mapped[int] = mapped_column(
        primary_key= True,
        index= True
    )

    name: Mapped[str] = mapped_column(nullable= False)

    specialization: Mapped[str] = mapped_column(nullable= False)

    patients:  Mapped[list["Patient"]] = relationship(
        "Patient",
        back_populates="doctor"
    )