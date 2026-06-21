from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.dependencies.user_dependency import get_user_service

from app.schemas.user_schema import (
    UserLogin, 
    TokenResponse, 
    UserCreate,
    UserResponse
)

from app.services.user_service import UserService

# Router
router = APIRouter(
    tags=["Authentication"]
)

# Login Endpoint
@router.post(
    "/login",
    response_model= TokenResponse
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service)
):
    token = user_service.authenticate_user(
        db, 
        user_data
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post(
    "/register",
    response_model= UserResponse
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service)
):
    
    return user_service.create_user(
        db,
        user_data
    )