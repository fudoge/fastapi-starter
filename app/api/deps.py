from fastapi import Depends

from app.db.session import get_db
from app.repository.user_repository import UserRepository
from app.services.user_service import UserService

def get_user_repository(db=Depends(get_db)):
    return UserRepository(db)

def get_user_service(user_repo: UserRepository = Depends(get_user_repository)):
    return UserService(user_repo)
