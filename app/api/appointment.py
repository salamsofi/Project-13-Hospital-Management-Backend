from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.user import User
from app.models.appointment import Appointment

from app.enums.user_role import UserRole

from app.services.appointment_service import AppointmentService
from app.dependencies.role_dependency import require_roles
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
    response_model= AppointmentResponse,
    status_code= status.HTTP_201_CREATED
)
def create_appoinment(
    appointment_data: AppointmentCreate,
    db: Session = Depends(get_db),
    appointment_service: AppointmentService = Depends(
        get_appointment_service
    ),
    current_user: User = Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.RECEPTIONIST
        )
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
    "/{appointment_id}",
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
    ),
    current_user: User = Depends(
        require_roles(
            UserRole.ADMIN,
            UserRole.RECEPTIONIST
        )
    )
):
    
    return appointment_service.update_appointment(
        appointment_id,
        appointment_data,
        db
    )

# Delete Appointment
@router.delete(
    "/{appointment_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    appointment_service: AppointmentService= Depends(
        get_appointment_service
    ),
    current_user: User = Depends(
        require_roles(UserRole.ADMIN)
    )
):
    
    appointment_service.delete_appointment(
        db,
        appointment_id
    )