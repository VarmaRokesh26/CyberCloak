import tkinter as tk
from ui.cybercloak_premium_lite_ui import CyberCloakPremiumLiteUI  # Import the Premium Lite UI
from core.vpn_manager import connect_vpn, disconnect_vpn
from core.port_scanner import scan_ports
from core.vuln_check import scan_vulnerabilities
from utils.ip_manager import get_local_ip, get_public_ip
from utils.logger import Logger

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("CyberCloak Premium Lite")

    # Step 1: Create UI with empty handlers
    ui = CyberCloakPremiumLiteUI(root, handlers={})

    # Step 2: Initialize logger with UI callback
    logger = Logger(log_callback=ui.log)

    # Step 3: Handler functions using logger
    def handle_connect_vpn():
        ui.run_with_progress(lambda: connect_vpn(logger, ui.show_progress, ui.toggle_disconnect))

    def handle_disconnect_vpn():
        disconnect_vpn(logger, ui.toggle_disconnect)

    def handle_scan_ports():
        ui.run_with_progress(lambda: scan_ports(get_local_ip(), logger, ui.show_progress))

    def handle_scan_vulns():
        ui.run_with_progress(lambda: scan_vulnerabilities(logger, ui.show_progress))

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
        "scan_vulns": handle_scan_vulns,
        "refresh_ips": handle_refresh_ips
    })

    # Step 5: Trigger initial IP refresh
    handle_refresh_ips()

    root.mainloop()

if __name__ == "__main__":
    main()
