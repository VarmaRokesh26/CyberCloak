import os
import subprocess
import threading
from config import settings

def check_openvpn(logger):
    for path in settings.COMMON_OPENVPN_PATHS:
        if os.path.exists(path):
            logger.log("INFO", f"OpenVPN found at: {path}")
            return path
    logger.log("ERROR", "OpenVPN is not installed or not in PATH.")
    return None

def get_vpn_configs(logger):
    configs = [f for f in os.listdir(settings.CONFIG_DIR) if f.endswith(".ovpn")]
    if not configs:
        logger.log("ERROR", "No VPN configuration files found in config folder.")
    return configs

def connect_vpn(logger, update_progress_callback, btn_disconnect):
    def vpn_task():
        openvpn_path = check_openvpn(logger)
        if not openvpn_path:
            return

        configs = get_vpn_configs(logger)
        if not configs:
            return

        vpn_config = os.path.join(settings.CONFIG_DIR, configs[0])
        logger.log("VPN", f"Trying VPN: {configs[0]}...")

        update_progress_callback(7)

        try:
            subprocess.Popen([openvpn_path, "--config", vpn_config], shell=True)
            logger.log("SUCCESS", "VPN Connected Successfully!")
            btn_disconnect.config(state="normal")
        except Exception as e:
            logger.log("ERROR", f"Failed to connect VPN: {e}")

    threading.Thread(target=vpn_task, daemon=True).start()

def disconnect_vpn(logger, btn_disconnect):
    logger.log("VPN", "Disconnecting VPN...")
    subprocess.run(["taskkill", "/F", "/IM", "openvpn.exe"], shell=True)
    logger.log("SUCCESS", "VPN Disconnected.")
    btn_disconnect.config(state="disabled")
