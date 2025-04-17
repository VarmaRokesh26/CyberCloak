import time
from config import settings
import tkinter as tk

# This will be set by UI module on app startup
log_console = None

def set_console_reference(console_widget: tk.Text):
    global log_console
    log_console = console_widget

def log_message(category: str, message: str):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} [{category}] {message}\n"

    # Log to file
    with open(settings.LOG_FILE, "a") as log:
        log.write(log_entry)

    # Log to UI console if available
    if log_console:
        log_console.config(state="normal")
        log_console.insert("end", log_entry)
        log_console.see("end")
        log_console.config(state="disabled")
