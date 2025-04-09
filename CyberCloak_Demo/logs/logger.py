import time
from config.settings import LOG_FILE

# 🔁 UI log console reference (will be injected)
log_console = None

def attach_log_console(console_widget):
    """Link the UI's log console (scrolledtext) to enable UI log updates."""
    global log_console
    log_console = console_widget

def log_message(category, message):
    """Log with timestamp and category to both file and (if available) UI."""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} [{category}] {message}\n"

    # ✅ Write to log file
    with open(LOG_FILE, "a") as log:
        log.write(log_entry)

    # ✅ Update log console (if UI linked it)
    if log_console:
        log_console.config(state="normal")
        log_console.insert("end", log_entry)
        log_console.see("end")
        log_console.config(state="disabled")
