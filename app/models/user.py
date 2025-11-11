from datetime import datetime 
from sqlalchemy import Uuid, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Text
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[Uuid] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(Text)
    email: Mapped[str] = mapped_column(Text)
    password: Mapped[str] = mapped_column(Text)
    refresh_token: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())
