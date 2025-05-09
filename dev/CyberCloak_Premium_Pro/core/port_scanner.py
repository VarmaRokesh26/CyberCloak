import subprocess
import threading
from utils.paths import NMAP_PATH
from utils.logger import Logger

def scan_ports(local_ip, logger: Logger, show_progress):

    def update_progress(steps):
        show_progress(steps)

    def run_scan():
        command = [NMAP_PATH, "-p", "1-65535", local_ip] 

        try:
            logger.log("INFO", f"Scanning ports on {local_ip} using Nmap...")
            update_progress(1)

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            for line in process.stdout:
                logger.log("INFO", line.strip())

            process.wait() 
            logger.log("INFO", "Port scan completed.")

            update_progress(100)

        except Exception as e:
            logger.log("ERROR", f"Error during Nmap port scan: {str(e)}")
            update_progress(0)

    threading.Thread(target=run_scan, daemon=True).start()
