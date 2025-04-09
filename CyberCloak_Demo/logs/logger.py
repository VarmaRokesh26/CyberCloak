import os
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), "logs")
LOG_FILE = os.path.join(LOG_DIR, "activity_log.txt")

class Logger:
    def __init__(self, log_callback=None):
        self.log_callback = log_callback
        os.makedirs(LOG_DIR, exist_ok=True)

    def log(self, category, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"{timestamp} [{category.upper()}] {message}"

        # Write to file
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

        # Send to UI if callback is available
        if self.log_callback:
            self.log_callback(category.upper(), message)
