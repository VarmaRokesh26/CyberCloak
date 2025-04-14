import socket
import concurrent.futures
import time

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                return port
    except:
        return None

def scan_ports(ip, logger, update_progress_callback):
    logger.log("SCAN", "Scanning open ports...")
    ports_to_scan = range(1, 10000)

    open_ports = []
    start_time = time.time()

    update_progress_callback(1000)

    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        results = executor.map(lambda port: scan_port(ip, port), ports_to_scan)

    open_ports = [port for port in results if port is not None]
    end_time = time.time()

    if open_ports:
        logger.log("RESULT", f"Open Ports Found: {open_ports}")
    else:
        logger.log("RESULT", "No open ports found.")

    logger.log("SCAN", f"Scan completed in {end_time - start_time:.2f} seconds.")
