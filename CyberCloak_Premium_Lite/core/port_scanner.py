import os
import subprocess
import threading
from utils.logger import log_message
from utils.paths import NMAP_PATH
from utils.ip_manager import get_local_ip, check_nmap


def scan_ports(ui_callback=None):
    """
    Performs a detailed port scan on the local IP using Nmap.
    Optionally accepts a `ui_callback(duration)` to show progress bar.
    """
    def scan_task():
        if not check_nmap():
            return

        ip = get_local_ip()
        log_message("SCAN", f"Starting port scan on {ip}...")
        if ui_callback:
            ui_callback(7)

        try:
            cmd = [NMAP_PATH, "-sS", "-sV", "-p-", ip]  # SYN scan + version detection
            output = subprocess.check_output(cmd, text=True)
            log_message("RESULT", f"Port Scan Results:\n{output}")
        except Exception as e:
            log_message("ERROR", f"Port scan failed: {e}")

    threading.Thread(target=scan_task, daemon=True).start()
