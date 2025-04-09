import socket
import concurrent.futures
import time
from logs.logger import log_message
from config.settings import SCAN_PORT_START, SCAN_PORT_END, SCAN_TIMEOUT, MAX_THREADS
from utils.net_utils import get_local_ip
from ui.loading_bar import show_loading_bar
import threading

def scan_port(ip, port):
    """Attempts to connect to a single port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(SCAN_TIMEOUT)
            if sock.connect_ex((ip, port)) == 0:
                return port
    except:
        return None

def scan_ports_ui_callback(callback_ui=None):
    """Runs port scan and logs results; accepts UI callback to show result."""
    
    def scan_task():
        log_message("SCAN", "Scanning open ports...")

        ip = get_local_ip()
        ports_to_scan = range(SCAN_PORT_START, SCAN_PORT_END + 1)
        open_ports = []

        start_time = time.time()

        # Show loading bar from UI module (optional)
        show_loading_bar(5)

        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            results = executor.map(lambda port: scan_port(ip, port), ports_to_scan)

        open_ports = [port for port in results if port is not None]
        end_time = time.time()

        if open_ports:
            log_message("RESULT", f"Open Ports Found: {open_ports}")
        else:
            log_message("RESULT", "No open ports found.")

        log_message("SCAN", f"Scan completed in {end_time - start_time:.2f} seconds.")

        if callback_ui:
            callback_ui(open_ports)  # Optional callback to update UI

    threading.Thread(target=scan_task, daemon=True).start()
