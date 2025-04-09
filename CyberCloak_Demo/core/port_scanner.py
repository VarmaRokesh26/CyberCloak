import socket
import concurrent.futures
import threading
import time

from logs.logger import log_message
from utils.net_utils import get_local_ip

# ✅ Scan a Single Port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                return port
    except:
        return None

# ✅ Scan Multiple Ports Asynchronously
def scan_ports(update_bar=None, ui_console=None):
    def scan_task():
        log_message("SCAN", "Scanning open ports...", ui_console)

        ip = get_local_ip()
        ports_to_scan = range(1, 10000)
        open_ports = []

        start_time = time.time()

        if update_bar:
            update_bar(5)  # Simulate progress bar for 5 seconds

        with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
            results = executor.map(lambda port: scan_port(ip, port), ports_to_scan)

        open_ports = [port for port in results if port is not None]
        end_time = time.time()

        if open_ports:
            log_message("RESULT", f"Open Ports Found: {open_ports}", ui_console)
        else:
            log_message("RESULT", "No open ports found.", ui_console)

        log_message("SCAN", f"Scan completed in {end_time - start_time:.2f} seconds.", ui_console)

    threading.Thread(target=scan_task, daemon=True).start()
