import tkinter as tk
from ui.cybercloak_demo_ui import CyberCloakDemoUI
from core import vpn_connector, port_scanner
from utils import net_utils
from logs import logger

def main():
    root = tk.Tk()

    # 🧠 Define handlers with UI callbacks
    def connect_vpn():
        ui.show_progress(7)
        vpn_connector.connect_vpn(
            log_callback=ui.log,
            enable_disconnect_btn=lambda: ui.set_disconnect_button_state(True)
        )

    def disconnect_vpn():
        vpn_connector.disconnect_vpn(
            log_callback=ui.log,
            disable_disconnect_btn=lambda: ui.set_disconnect_button_state(False)
        )

    def scan_ports():
        ui.show_progress(5)
        port_scanner.scan_ports(
            log_callback=ui.log
        )

    def refresh_ips(local_ip_var, public_ip_var):
        local_ip = net_utils.get_local_ip()
        public_ip = net_utils.get_public_ip()

        local_ip_var.set(local_ip)
        public_ip_var.set(public_ip)
        logger.log("INFO", "IPs refreshed.")
        ui.log("INFO", "IPs refreshed.")

    # 👇 Create UI instance with all handlers
    ui = CyberCloakDemoUI(root, handlers={
        "connect_vpn": connect_vpn,
        "disconnect_vpn": disconnect_vpn,
        "scan_ports": scan_ports,
        "refresh_ips": refresh_ips
    })

    root.mainloop()

if __name__ == "__main__":
    main()
