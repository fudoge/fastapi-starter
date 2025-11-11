import json
import logging
from logging import Formatter

class JsonFormatter(Formatter):
    def format(self, record):
        json_record = {
            "level": record.levelname,
            "message": record.getMessage(),
            "time": self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        }

        return json.dumps(json_record, ensure_ascii=False)

logger = logging.getLogger("app")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.handlers = [handler]
logger.setLevel(logging.INFO)
logging.getLogger("uvicorn.access").disabled = True
