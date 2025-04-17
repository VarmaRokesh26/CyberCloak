import os
import subprocess
import threading
from utils.logger import Logger
from utils.paths import NMAP_PATH
from utils.ip_manager import get_local_ip, check_nmap


def scan_vulnerabilities(ui_callback=None):
    """
    Performs a vulnerability scan using Nmap scripts on the local IP.
    Optionally accepts a `ui_callback(duration)` to show progress bar.
    """
    def vuln_task():
        if not check_nmap():
            return

        ip = get_local_ip()
        Logger.log("SCAN", f"Starting vulnerability scan on {ip}...")
        if ui_callback:
            ui_callback(10)

        try:
            cmd = [NMAP_PATH, "-sV", "--script", "vuln", ip]
            output = subprocess.check_output(cmd, text=True)
            Logger.log("RESULT", f"Vulnerability Scan Results:\n{output}")
        except Exception as e:
            Logger.log("ERROR", f"Vulnerability scan failed: {e}")

    threading.Thread(target=vuln_task, daemon=True).start()
