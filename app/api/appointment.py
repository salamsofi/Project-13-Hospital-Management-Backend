from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.appointment import Appointment

from app.services.appointment_service import AppointmentService
from app.dependencies.appointment_dependency import get_appointment_service

from app.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse
)

router = APIRouter(
    prefix= "/appointments",
    tags= ["Appointment"]
)

# Create Appointment
@router.post(
    "/",
    response_model= AppointmentResponse
)
def create_appoinment(
    appointment_data: AppointmentCreate,
    db: Session = Depends(get_db),
    appointment_service: AppointmentService = Depends(
        get_appointment_service
    )
):

    return appointment_service.create_appointment(
        appointment_data,
        db
    )

# Get All Appointments
@router.get(
    "/",
    response_model= list[AppointmentResponse]
)
def get_all_appointment(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    sort_by: str = "id",
    sort_order: str = "asc",
    
    db: Session = Depends(get_db),
    
    appointment_service: AppointmentService = Depends(
        get_appointment_service
    )
):
    
    return appointment_service.get_all_appointment(
        db,
        skip,
        limit,
        search,
        sort_by,
        sort_order
    )

# Get Appointment By ID
@router.get(
    "/{apppointment_id}",
    response_model= AppointmentResponse
)
def get_appointment_by_id(
    appointment_id: int,
    
    db: Session = Depends(get_db),
    appointment_service: AppointmentService = Depends(
        get_appointment_service
    )
):
    
    return appointment_service.get_appointment_by_id(
        appointment_id,
        db
    )

# Update Appointment
@router.put(
    "/{appointment_id}",
    response_model= AppointmentResponse
)
def update_appointment(
    appointment_id: int,
    appointment_data: AppointmentUpdate,
    db: Session = Depends(get_db),
    appointment_service: AppointmentService = Depends(
        get_appointment_service
    )
):
    
    return appointment_service.update_appointment(
        appointment_id,
        appointment_data,
        db
    )

# Delete Appointment
@router.delete(
    "/{appointment_id}"
)
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    appointment_service: AppointmentService= Depends(
        get_appointment_service
    )
):
    
    appointment_service.delete_appointment(
        db,
        appointment_id
    )

    return {
        "message": "Appointment deleted successfully"
    }