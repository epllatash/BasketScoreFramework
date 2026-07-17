from loguru import logger

from src.core.config.settings import LOGS_DIR

logger.remove()

logger.add(
    LOGS_DIR / "basket_score.log",
    rotation="5 MB",
    retention=10,
    level="INFO",
    enqueue=True,
)

logger.add(
    lambda msg: print(msg, end=""),
    level="DEBUG",
)

app_logger = logger
