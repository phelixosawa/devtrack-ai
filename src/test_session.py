from src.session_logger import SessionLogger
import time

logger = SessionLogger()

logger.start_session(
    project_name="devtrack-ai",
    description="Testing session logging system",
    tags=["test"]
)

time.sleep(5)

logger.end_session()