from fastapi import Depends

from app.dependencies.auth_dependency import get_current_user
from app.exceptions.auth_exception import UnauthorizedException
from app.models.user import User, UserRole


def require_admin(
    current_user: User = Depends(
        get_current_user
    )
):
    
    if current_user.role != UserRole.ADMIN:
        raise UnauthorizedException

    return current_user