from fastapi import APIRouter, Depends
from app.api.deps import get_user_service
from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=UserRead)
def create_user(user_in: UserCreate, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user_in)
