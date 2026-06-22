from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.schemas.patient_schema import PatientSummary

class AppointmentCreate(BaseModel):
    appointment_date: datetime
    reason: str
    patient_id: int


class AppointmentUpdate(BaseModel):
    appointment_date: datetime
    reason: str

class AppointmentResponse(BaseModel):
    id: int
    appointment_date: datetime
    reason: str
    patient: PatientSummary

    model_config = ConfigDict(
        from_attributes=True
    )