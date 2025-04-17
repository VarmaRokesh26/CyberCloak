import subprocess
import threading

from utils.logger import log_message
from utils.network import get_local_ip
from ui.progress_bar import update_progress_bar
from settings import NMAP_PATH
from core.nmap_checker import check_nmap  # We'll assume this lives separately

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
