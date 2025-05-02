from datetime import datetime
from utils.paths import LOG_FILE
import os

class Logger:
    def __init__(self, log_callback=None):
        self.log_callback = log_callback
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    def log(self, category, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"{timestamp} [{category.upper()}] {message}"

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

        if self.log_callback:
            self.log_callback(category.upper(), message)
