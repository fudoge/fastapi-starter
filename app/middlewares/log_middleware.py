from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from app.core.logger import logger

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            logger.info(
                "Incoming request",
                extra = {
                    "req": {"method": request.method, "url": str(request.url)},
                    "res": {"status_code": response.status_code,},
                },
            )
            return response
        except Exception as e:
            logger.exception(
                "Unhandled Exception",
                extra = {
                    "req": {"method": request.method, "url": str(request.url)},
                    "req": {"status_code": 500, "error": str(e)},
                },
            )
            raise e
