import os
from datetime import datetime

# Get the directory where the EXE or script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")  # Points to logs/ alongside exe
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
