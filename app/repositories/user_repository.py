from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User

class UserRepository:

    def get_by_username(
        self,
        db: Session,
        username: str
    ) -> User | None:
        
        stmt = (
            select(User)
            .where(User.username == username)
        )

        return db.scalar(stmt)

    def create(
        self,
        db: Session,
        user: User
    ) -> User:

        db.add(user)
        db.commit()
        db.refresh(user)

        return user