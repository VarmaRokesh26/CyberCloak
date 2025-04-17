import os
import subprocess
import threading
import time

from utils.paths import CONFIG_DIR, COMMON_PATHS


def check_openvpn(callback_log):
    for path in COMMON_PATHS:
        if os.path.exists(path):
            callback_log("INFO", f"OpenVPN found at: {path}")
            return path
    callback_log("ERROR", "OpenVPN is not installed or not found in expected paths.")
    return None


def get_vpn_configs(callback_log):
    try:
        configs = [f for f in os.listdir(CONFIG_DIR) if f.endswith(".ovpn")]
        if not configs:
            callback_log("ERROR", "No VPN configuration files found in config folder.")
        return configs
    except Exception as e:
        callback_log("ERROR", f"Failed to load VPN configs: {e}")
        return []


def connect_vpn(callback_log, callback_progress, callback_disconnect_toggle):
    def vpn_task():
        openvpn_path = check_openvpn(callback_log)
        if not openvpn_path:
            return

        configs = get_vpn_configs(callback_log)
        if not configs:
            return

        vpn_config = os.path.join(CONFIG_DIR, configs[0])
        callback_log("VPN", f"Connecting to VPN using: {configs[0]}")
        callback_progress(7)

        try:
            subprocess.Popen([openvpn_path, "--config", vpn_config], shell=True)
            callback_log("SUCCESS", "VPN Connected Successfully!")
            callback_disconnect_toggle(True)
        except Exception as e:
            callback_log("ERROR", f"Failed to connect to VPN: {e}")

    threading.Thread(target=vpn_task, daemon=True).start()


def disconnect_vpn(callback_log, callback_progress, callback_disconnect_toggle):
    def disconnect_task():
        callback_log("VPN", "Disconnecting VPN...")
        callback_progress(3)

        try:
            os.system("taskkill /F /IM openvpn.exe")
            time.sleep(2)
            callback_log("VPN", "VPN Disconnected Successfully.")
        except Exception as e:
            callback_log("ERROR", f"Failed to disconnect VPN: {e}")

        callback_disconnect_toggle(False)

    threading.Thread(target=disconnect_task, daemon=True).start()
