from sqlalchemy.orm import Session

from app.auth.password import verify_password, hash_password
from app.auth.jwt_handler import create_access_token

from app.core.logger import logger

from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin

from app.exceptions.auth_exception import (
    InvalidCredentialsException, 
    UserAlreadyExistsException
)

class UserService:

    def __init__(
        self,
        user_repository: UserRepository
    ):
        
        self.user_repository = user_repository

    
    def authenticate_user(
        self,
        db: Session,
        user_data: UserLogin
    ) -> str:
        
        logger.info(
            f"Authenticating user {user_data.username}"
        )

        user = self.user_repository.get_by_username(
            db,
            user_data.username
        )

        if (
            user is None
            or 
            not verify_password(
                user_data.password, 
                user.hashed_password
            )
        ):
            logger.warning(
               f"Invalid login attempt for {user_data.username}"
            )

            raise InvalidCredentialsException()
        
        access_token = create_access_token(
            {
                "sub": user.username
            }
        )

        logger.info(
            f"User {user_data.username} logged in successfully"
        )

        return access_token
    
    def create_user(
        self,
        db: Session,
        user_data: UserCreate
    ) -> User:

        logger.info(
            f"Creating user {user_data.username}"
        )
        
        existing_user = (
            self.user_repository.get_by_username(
                db,
                user_data.username
            )
        )

        if existing_user:
            logger.warning(
                f"User {user_data.username} already exists"
            )

            raise UserAlreadyExistsException()

        hashed_password = hash_password(user_data.password)

        user = User(
            username = user_data.username,
            email = user_data.email,
            hashed_password = hashed_password,
            role= user_data.role
        )

        return self.user_repository.create(
            db, user
        )
    
    