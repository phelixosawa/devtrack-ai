import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "devtrack.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("devtrack")