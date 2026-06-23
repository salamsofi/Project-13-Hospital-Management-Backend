from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.prescription_service import PrescriptionService

from app.dependencies.prescription_dependency import (
    get_prescription_service
)

from app.schemas.prescription_schema import (
    PrescriptionCreate,
    PrescriptionUpdate,
    PrescriptionResponse
)

# Router
router = APIRouter(
    prefix="/prescriptions",
    tags=["Prescriptions"]
)

# Create Prescription
@router.post(
    "/",
    response_model= PrescriptionResponse
)
def create_prescription(
    prescription_data: PrescriptionCreate,
    db: Session = Depends(get_db),
    
    prescription_service: PrescriptionService = Depends(
        get_prescription_service
    )
):
    
    return prescription_service.create_prescription(
        db,
        prescription_data
    )

# Get All Prescriptions
@router.get(
    "/",
    response_model= list[PrescriptionResponse]
)
def get_all_prescriptions(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    sort_by: str = "id",
    sort_order: str = "asc",
    db: Session = Depends(get_db),
    prescription_service: PrescriptionService = Depends(
        get_prescription_service
    )
):
    
    return prescription_service.get_all_patients(
        db,
        skip,
        limit,
        search,
        sort_by,
        sort_order
    )

# Get Prescription By ID
@router.get(
    "/{prescription_id}",
    response_model= PrescriptionResponse
)
def get_prescription_by_id(
    prescription_id: int,
    db: Session = Depends(get_db),
    prescription_service: PrescriptionService = Depends(
        get_prescription_service
    )
):
    
    return prescription_service.get_prescription_by_id(
        db,
        prescription_id
    )

# Update Prescription
@router.put(
    "/{prescription_id}",
    response_model= PrescriptionService
)
def update_prescription(
    prescription_id: int,
    prescription_data: PrescriptionUpdate,
    db: Session = Depends(get_db),
    prescription_service: PrescriptionService = Depends(
        get_prescription_service
    )
):

    return prescription_service.update_prescription(
        db,
        prescription_id,
        prescription_data
    )

# Delete Prescription
@router.delete(
    "/{prescription_id}",
    response_model= PrescriptionService
)
def delete_prescription(
    prescription_id: int,
    db: Session = Depends(get_db),
    prescription_service: PrescriptionService = Depends(
        get_prescription_service
    )
):
    
    prescription_service.delete_patient(
        prescription_id,
        db
    )

    return {
        "message": "Prescription deleted successfully"
    }