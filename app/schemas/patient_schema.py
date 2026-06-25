from pydantic import BaseModel, ConfigDict
from app.schemas.doctor_schema import DoctorSummary

class PatientCreate(BaseModel):
    name: str
    age: int
    city: str
    doctor_id: int
    

class PatientUpdate(BaseModel):
    name: str
    age: int
    city: str


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    city: str
    doctor: DoctorSummary
    
    model_config = ConfigDict(
        from_attributes= True
    )


class PatientSummary(BaseModel):
    id: int
    name: str
    age: int
    city: str

    doctor: DoctorSummary

    model_config = ConfigDict(
        from_attributes= True
    )