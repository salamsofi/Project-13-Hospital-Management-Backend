from pydantic import BaseModel, ConfigDict

class DoctorCreate(BaseModel):

    name: str
    specialization: str


class DoctorResponse(BaseModel):

    id: int
    name: str
    specialization: str

    model_config = ConfigDict(
        from_attributes=True
    )


class DoctorUpdate(BaseModel):

    name: str
    specialization: str

    model_config = ConfigDict(
        from_attributes=True
    )

class DoctorSummary(BaseModel):

    id: int
    name: str
    specialization: str

    model_config = ConfigDict(
        from_attributes=True
    )