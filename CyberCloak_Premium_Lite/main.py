import tkinter as tk
from ui.cybercloak_premium_lite_ui import CyberCloakPremiumLiteUI
from core.vpn_manager import connect_vpn, disconnect_vpn
from core.port_scanner import scan_ports
from core.vuln_check import run_vulnerability_check
from utils.logger import Logger
from utils.ip_manager import get_local_ip, get_public_ip

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("CyberCloak Premium Lite")

    # Step 1: Initialize UI with empty handlers
    ui = CyberCloakPremiumLiteUI(root, handlers={})

    # Step 2: Setup Logger with UI log output
    logger = Logger(log_callback=ui.log)

    # Step 3: Define handler functions
    def handle_connect_vpn():
        ui.run_with_progress(lambda: connect_vpn(logger, ui.show_progress, ui.disconnect_btn))

    def handle_disconnect_vpn():
        disconnect_vpn(logger, ui.disconnect_btn)

    def handle_scan_ports():
        ip = get_local_ip()
        ui.run_with_progress(lambda: scan_ports(ip, logger, ui.show_progress))

    def handle_scan_vulns():
        ip = get_local_ip()
        ui.run_with_progress(lambda: run_vulnerability_check(ip, logger, ui.show_progress))

    def handle_refresh_ips():
        local_ip = get_local_ip()
        public_ip = get_public_ip()
        ui.set_ip_info(local_ip, public_ip)
        logger.log("INFO", "IP addresses refreshed.")

    # Step 4: Bind handlers to UI
    ui.set_handlers({
        "connect_vpn": handle_connect_vpn,
        "disconnect_vpn": handle_disconnect_vpn,
        "scan_ports": handle_scan_ports,
        "scan_vulns": handle_scan_vulns,
        "refresh_ips": handle_refresh_ips,
    })

    # Step 5: Initial IP fetch
    handle_refresh_ips()

    # Run the UI loop
    root.mainloop()

if __name__ == "__main__":
    main()
