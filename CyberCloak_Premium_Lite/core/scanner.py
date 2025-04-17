import os
import socket
import subprocess
import threading
import time
from utils.logger import log_message
from ui.progress_bar import update_progress_bar
from utils.network import get_local_ip

NMAP_PATH = r"C:\nmap\nmap.exe"  # Ensure nmap is placed in C:\nmap

def check_nmap():
    if os.path.exists(NMAP_PATH):
        log_message("INFO", f"Nmap found at: {NMAP_PATH}")
        return True
    log_message("ERROR", "Nmap is not installed at C:\\nmap\\nmap.exe.")
    return False

def scan_ports():
    def scan_task():
        if not check_nmap():
            return

        log_message("SCAN", "Starting detailed port scan...")
        ip = get_local_ip()
        update_progress_bar(7)

        try:
            cmd = [NMAP_PATH, "-sS", "-sV", "-p-", ip]  # SYN scan + Service detection
            output = subprocess.check_output(cmd, text=True)
            log_message("RESULT", f"Scan Results:\n{output}")
        except Exception as e:
            log_message("ERROR", f"Scan failed: {e}")

    threading.Thread(target=scan_task, daemon=True).start()

def scan_vulnerabilities():
    def vuln_task():
        if not check_nmap():
            return
        
        log_message("SCAN", "Starting vulnerability check...")
        ip = get_local_ip()
        update_progress_bar(10)

        try:
            cmd = [NMAP_PATH, "-sV", "--script", "vuln", ip]
            output = subprocess.check_output(cmd, text=True)
            log_message("RESULT", f"Vulnerability Scan Results:\n{output}")
        except Exception as e:
            log_message("ERROR", f"Vulnerability scan failed: {e}")

    threading.Thread(target=vuln_task, daemon=True).start()
