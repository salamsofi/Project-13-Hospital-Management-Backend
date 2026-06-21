from pydantic import BaseModel, ConfigDict
from app.models.user import UserRole

class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: UserRole


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: UserRole

    model_config = ConfigDict(
        from_attributes= True
    )