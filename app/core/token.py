from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from app.core.config import settings

def create_access_token(data: dict) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode = {**data, "exp": expire, "type": "access"}
    return jwt.encode(to_encode, settings.JWT_ACCESS_KEY, algorithm=settings.JWT_ALG)

def create_refresh_token(data: dict) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=7)
    to_encode = {**data, "exp": expire, "type": "refresh"}
    return jwt.encode(to_encode, settings.JWT_REFRESH_KEY, algorithm=settings.JWT_ALG)

def verify_token(token: str, refresh: bool = False) -> dict | None:
    try:
        secret = settings.JWT_REFRESH_KEY if refresh else settings.JWT_ACCESS_KEY
        payload = jwt.decode(token, secret, algorithms=[settings.JWT_ALG])
        return payload
    except JWTError:
        return None
