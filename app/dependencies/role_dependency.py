from fastapi import Depends

from app.dependencies.auth_dependency import get_current_user
from app.exceptions.auth_exception import UnauthorizedException
from app.models.user import User
from app.enums.user_role import UserRole


def require_roles(*allowed_roles: UserRole):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):
        
        if current_user.role not in allowed_roles:
            raise UnauthorizedException()
        
        return current_user

    return role_checker
    
    