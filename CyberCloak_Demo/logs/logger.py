import os
import time

LOG_FILE = os.path.join(os.path.dirname(__file__), "vpn_log.txt")

# ✅ Centralized Logger Function
def log_message(category, message, ui_console=None):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} [{category}] {message}\n"

    # Write to log file
    with open(LOG_FILE, "a") as log:
        log.write(log_entry)

    # Optional: Update UI Console if provided
    if ui_console:
        ui_console.config(state="normal")
        ui_console.insert("end", log_entry)
        ui_console.see("end")
        ui_console.config(state="disabled")