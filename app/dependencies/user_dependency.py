from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

def get_user_service():

    user_repository = UserRepository()

    return UserService(
        user_repository
    )