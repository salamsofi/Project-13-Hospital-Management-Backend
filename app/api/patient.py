from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services.patient_service import PatientService

from app.dependencies.patient_dependency import get_patient_service

from app.schemas.patient_schema import (
    PatientCreate, 
    PatientUpdate, 
    PatientResponse
)

router = APIRouter(
    prefix="/patients",
    tags=["Patient"]
)

# CREATE PATIENT
@router.post(
    "/",
    response_model= PatientResponse    
)
def create_patient(
    patient_data: PatientCreate,
    db: Session = Depends(get_db),
    patient_service: PatientService = Depends(get_patient_service)
):
    
    return patient_service.create_patient(
        db,
        patient_data
    )

# GET ALL PATIENTS
@router.get(
    "/",
    response_model= list[PatientResponse]
)
def get_all_patients(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    sort_by: str = "id",
    sort_order: str = "asc",
    db: Session = Depends(get_db),
    patient_service: PatientService = Depends(get_patient_service)
):
    
    return patient_service.get_all_patients(
        db,
        skip,
        limit,
        search,
        sort_by,
        sort_order
    )

# GET PATIENT BY ID
@router.get(
    "/{patient_id}",
    response_model= PatientResponse
)
def get_patient_by_id(
    patient_id: int,
    db: Session = Depends(get_db),
    patient_service: PatientService = Depends(get_patient_service)
):

    return patient_service.get_patient_by_id(
        db,
        patient_id
    )

# UPDATE
@router.put(
    "/{patient_id}",
    response_model= PatientResponse
)
def update_patient(
    patient_id: int,
    patient_data: PatientUpdate,
    db: Session = Depends(get_db),
    patient_service: PatientService = Depends(get_patient_service) 
):
    
    return patient_service.update_patient(
        db,
        patient_id,
        patient_data
    )


# DELETE 
@router.delete(
    "/{patient_id}"
)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    patient_service: PatientService = Depends(get_patient_service)
):

    patient_service.delete_patient(
        db,
        patient_id
    )

    return {
        "message": "Patient deleted successfully"
    }