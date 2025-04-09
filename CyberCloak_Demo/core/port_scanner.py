import socket
import concurrent.futures
import time
from logs.logger import log_message
from utils.net_utils import get_local_ip
from ui.cybercloak_demo_ui import update_progress_bar

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                return port
    except:
        return None

def scan_ports():
    log_message("SCAN", "Scanning open ports...")

    ip = get_local_ip()
    ports_to_scan = range(1, 10000)

    update_progress_bar(5)

    start_time = time.time()
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        results = executor.map(lambda port: scan_port(ip, port), ports_to_scan)

    open_ports = [port for port in results if port is not None]
    end_time = time.time()

    if open_ports:
        log_message("RESULT", f"Open Ports Found: {open_ports}")
    else:
        log_message("RESULT", "No open ports found.")

    log_message("SCAN", f"Scan completed in {end_time - start_time:.2f} seconds.")
