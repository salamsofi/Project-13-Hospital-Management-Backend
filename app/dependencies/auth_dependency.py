from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)

from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.auth.jwt_handler import decode_access_token
from app.repositories.user_repository import UserRepository


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    
    payload = decode_access_token(token)

    username = payload.get("sub")

    user_repository = UserRepository()

    user = user_repository.get_by_username(
        db,
        username
    )

    return user

