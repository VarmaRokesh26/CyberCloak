import tkinter as tk
import threading
from ui.cybercloak_demo_ui import CyberCloakDemoUI
from core.vpn_connector import connect_vpn, disconnect_vpn
from core.port_scanner import scan_ports
from utils.net_utils import get_local_ip, get_public_ip
from config.logger import Logger

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("CyberCloak Demo")

    # Step 1: Create UI with empty handlers
    ui = CyberCloakDemoUI(root, handlers={})

    # Step 2: Initialize logger with UI callback
    logger = Logger(log_callback=ui.log)

    # Step 3: Handler functions using logger
    def handle_connect_vpn():
        def scan_task():
            connect_vpn(logger, ui.show_progress, ui.disconnect_button)  # Pass actual button
        threading.Thread(target=scan_task, daemon=True).start()

    def handle_disconnect_vpn():
        disconnect_vpn(logger, ui.disconnect_button)  # Pass actual button

    def handle_scan_ports():
        def scan_task():
            scan_ports(get_local_ip(), logger, ui.show_progress)
        threading.Thread(target=scan_task, daemon=True).start()

    def handle_refresh_ips():
        local_ip = get_local_ip()
        public_ip = get_public_ip()
        ui.set_ip_info(local_ip, public_ip)
        logger.log("INFO", "IPs refreshed.")

    # Step 4: Assign handlers to UI
    ui.set_handlers({
        "connect_vpn": handle_connect_vpn,
        "disconnect_vpn": handle_disconnect_vpn,
        "scan_ports": handle_scan_ports,
        "refresh_ips": handle_refresh_ips
    })

    # Step 5: Trigger initial IP refresh
    handle_refresh_ips()

    root.mainloop()

if __name__ == "__main__":
    main()
