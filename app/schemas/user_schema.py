from datetime import datetime
from pydantic import BaseModel, EmailStr
from sqlalchemy import Uuid

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: Uuid
    username: str
    email: EmailStr
    refresh_token: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
