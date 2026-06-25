from pydantic import BaseModel, ConfigDict
from app.schemas.appointment_schema import AppointmentSummary

class PrescriptionCreate(BaseModel):
    medicines: list[str]
    dosage: str
    appointment_id: int


class PrescriptionUpdate(BaseModel):
    medicines: list[str]
    dosage: str


class PrescriptionResponse(BaseModel):
    id: int
    medicines: list[str]
    dosage: str
    # appointment_id: int
    appointment : AppointmentSummary
    
    model_config = ConfigDict(
        from_attributes=True
    )