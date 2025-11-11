from app.models.user import User
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_in: UserCreate) -> User:
        user = User(username=user_in.username, email=user_in.email, password=user_in.password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
