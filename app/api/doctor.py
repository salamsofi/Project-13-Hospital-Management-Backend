from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.enums.user_role import UserRole

from app.models.doctor import Doctor
from app.models.user import User

from app.services.doctor_service import DoctorService
from app.repositories.doctor_repository import DoctorRepository
from app.schemas.doctor_schema import DoctorCreate, DoctorResponse

from app.dependencies.role_dependency import require_roles
from app.dependencies.doctor_dependency import get_doctor_service
from app.dependencies.auth_dependency import get_current_user

# Step 2: Create Router
router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post(
    "/",
    response_model= DoctorResponse,
    status_code= status.HTTP_201_CREATED    
)
def create_doctor(
    doctor_data: DoctorCreate,
    db: Session = Depends(get_db),
    doctor_service: DoctorService = Depends(get_doctor_service),
    current_user: User = Depends(
        require_roles(UserRole.ADMIN)
    )
):
    
    return doctor_service.create_doctor(
        db,
        doctor_data
    )


# GET ALL
@router.get(
    "/",
    response_model= list[DoctorResponse]
)
def get_all_doctors(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    sort_by: str = "id",
    sort_order: str = "asc",
    db: Session = Depends(get_db),
    doctor_service: DoctorService = Depends(
        get_doctor_service
    )
):
    
    return doctor_service.get_all_doctors(
        db,
        skip,
        limit,
        search,
        sort_by,
        sort_order
    )


# GETE BY ID
@router.get("/{doctor_id}", response_model= DoctorResponse)
def get_doctor_by_id(
    doctor_id: int,
    db: Session = Depends(get_db),

    doctor_service: DoctorService = Depends(
        get_doctor_service
    )
):

    return doctor_service.get_doctor_by_id(
        db,
        doctor_id
    )

# UPDATE 
@router.put("/{doctor_id}", response_model= DoctorResponse)
def update(
    doctor_id: int,
    doctor_data: DoctorCreate,
    db: Session = Depends(get_db),
    doctor_service: DoctorService = Depends(
        get_doctor_service
    ),
    current_user: User = Depends(
        require_roles(UserRole.ADMIN)
    )
):

    return doctor_service.update_doctor(
            db,
            doctor_id,
            doctor_data
        )


# DELETE
@router.delete(
    "/{doctor_id}",
    status_code= status.HTTP_204_NO_CONTENT
)
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    
    doctor_service: DoctorService = Depends(
        get_doctor_service
    ),
    ccurrent_user: User = Depends(
        require_roles(UserRole.ADMIN)
    )
):
    
    doctor_service.delete_doctor(
        db,
        doctor_id
    )