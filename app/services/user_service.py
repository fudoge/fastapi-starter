from app.schemas.user_schema import UserCreate
from app.utils.bcrypt import hash_password

class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_user(self, data: UserCreate):
        data.password = hash_password(data.password)
        return self.user_repo.create(data)
