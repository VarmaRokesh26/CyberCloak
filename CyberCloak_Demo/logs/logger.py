import time
from config import settings

class Logger:
    def __init__(self, log_console_widget=None):
        self.log_console = log_console_widget

    def log(self, category, message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} [{category}] {message}\n"

        with open(settings.LOG_FILE, "a") as log_file:
            log_file.write(log_entry)

        if self.log_console:
            self.log_console.config(state="normal")
            self.log_console.insert("end", log_entry)
            self.log_console.see("end")
            self.log_console.config(state="disabled")