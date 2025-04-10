import socket
import concurrent.futures
import time

from CyberCloak_Demo.config import settings

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                return port
    except:
        return None

def scan_ports(target_ip, logger, show_progress):
    logger.log("SCAN", "Scanning open ports...")

    open_ports = []
    total_ports = len(settings.COMMON_PORTS)
    
    for idx, port in enumerate(settings.COMMON_PORTS):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass

        # Update progress every few ports
        if idx % 5 == 0:
            percent = int((idx / total_ports) * 100)
            show_progress(percent)

    show_progress(100)
    logger.log("RESULT", f"Open Ports Found: {open_ports}")

