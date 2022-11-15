import logging 
from datetime import datetime
import os


LOG_DIR= "Housing-logs"
CURRENT_TIME_STAMP = f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}"
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH, 
filemode="w", 
level=logging.INFO, 
format="[%(asctime)s] %(name)s - %(levelname)s %(message)s", 
datefmt="%Y-%m-%d_%H-%M-%S")