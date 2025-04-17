import os
import subprocess
import threading
import time

from utils.logger import log_message
from ui.progress_bar import update_progress_bar

# Update this to your OpenVPN install locations
COMMON_PATHS = [
    r"C:\Program Files\OpenVPN\bin\openvpn.exe",
    r"C:\Program Files (x86)\OpenVPN\bin\openvpn.exe"
]

CONFIG_DIR = r"C:\Users\ROKESH's-PC\OurVPN\config"

def check_openvpn():
    for path in COMMON_PATHS:
        if os.path.exists(path):
            log_message("INFO", f"OpenVPN found at: {path}")
            return path
    log_message("ERROR", "OpenVPN is not installed or not in PATH.")
    return None

def get_vpn_configs():
    configs = [f for f in os.listdir(CONFIG_DIR) if f.endswith(".ovpn")]
    if not configs:
        log_message("ERROR", "No VPN configuration files found in config folder.")
    return configs

def connect_vpn(btn_disconnect):
    def vpn_task():
        openvpn_path = check_openvpn()
        if not openvpn_path:
            return

        configs = get_vpn_configs()
        if not configs:
            return

        vpn_config = os.path.join(CONFIG_DIR, configs[0])
        log_message("VPN", f"Trying VPN: {configs[0]}...")

        update_progress_bar(7)

        try:
            subprocess.Popen([openvpn_path, "--config", vpn_config], shell=True)
            log_message("SUCCESS", "VPN Connected Successfully!")
            btn_disconnect.config(state="normal")
        except Exception as e:
            log_message("ERROR", f"Failed to connect VPN: {e}")

    threading.Thread(target=vpn_task, daemon=True).start()

def disconnect_vpn(btn_disconnect):
    def vpn_disconnect_task():
        log_message("VPN", "Disconnecting VPN...")
        update_progress_bar(3)

        try:
            os.system("taskkill /F /IM openvpn.exe")
            time.sleep(2)
            log_message("VPN", "VPN Disconnected Successfully.")
        except Exception as e:
            log_message("ERROR", f"Failed to disconnect VPN: {e}")

    btn_disconnect.config(state="disabled")
    threading.Thread(target=vpn_disconnect_task, daemon=True).start()
