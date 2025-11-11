from warnings import warn
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = Field(default="FastAPI")
    DB_URL: str = Field(default="postgresql+psyconpg2://user:pass@host:5432/db")
    JWT_ACCESS_KEY: str = Field(default="jwtaccesskey")
    JWT_REFRESH_KEY: str = Field(default="jwtrefreshkey")
    JWT_ALG: str = "HS256"

settings = Settings()
