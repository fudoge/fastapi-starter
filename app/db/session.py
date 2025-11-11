from fastapi import Request
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker
from app.core.config import settings

def get_engine() -> Engine:
    engine = create_engine(
        settings.DB_URL,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        pool_recycle=1800,
        echo=False
    )
    return engine


def get_db(request: Request):
    SessionLocal: sessionmaker = request.app.state.sesstion_factory
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
