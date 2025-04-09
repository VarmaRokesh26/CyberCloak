import time
import os
from config.settings import LOG_FILE_PATH

# Ensure log folder exists
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

def log_message(category, message, ui_console=None):
    """
    Logs a message to file and optionally updates a UI console.
    """
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} [{category}] {message}\n"

    # Write to log file
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(log_entry)

    # Update log console in UI (optional, passed from UI)
    if ui_console:
        ui_console.config(state="normal")
        ui_console.insert("end", log_entry)
        ui_console.see("end")
        ui_console.config(state="disabled")
