import logging
import os

LOG_DIR = "Logs"
os.makedirs(LOG_DIR, exist_ok= True)

logging.basicConfig(
    filename= os.path.join(LOG_DIR, "pipeline.log"),
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger():
    return logging.getLogger("phishing_classifier")


