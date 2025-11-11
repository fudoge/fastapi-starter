from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from app.core.logger import logger
from app.core.config import settings
from app.api.v1 import user_router
from app.db.session import get_engine
from app.middlewares.log_middleware import LogMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # starting phase
    logger.info("Service Starting...")
    engine = get_engine()
    session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

    app.state.engine = engine
    app.state.session_factory = session_factory

    yield

    # graceful shutdown
    logger.info("Service shutting down..")
    try:
        engine.dispose()
    except Exception:
        logger.exception("engine dispose failed")


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.add_middleware(LogMiddleware)

app.include_router(user_router.router, prefix="/api/v1", tags=["users"])

