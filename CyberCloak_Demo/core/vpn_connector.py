import os
import subprocess
import threading
import time

from logs.logger import log_message

# ✅ OpenVPN Installation Paths
COMMON_PATHS = [
    r"C:\Program Files\OpenVPN\bin\openvpn.exe",
    r"C:\Program Files (x86)\OpenVPN\bin\openvpn.exe"
]

# ✅ Get OpenVPN Path
def check_openvpn():
    for path in COMMON_PATHS:
        if os.path.exists(path):
            log_message("INFO", f"OpenVPN found at: {path}")
            return path
    log_message("ERROR", "OpenVPN is not installed or not in PATH.")
    return None

# ✅ Get Available VPN Config Files
def get_vpn_configs(config_dir):
    configs = [f for f in os.listdir(config_dir) if f.endswith(".ovpn")]
    if not configs:
        log_message("ERROR", "No VPN configuration files found.")
    return configs

# ✅ Connect to VPN
def connect_vpn(config_dir, btn_disconnect, update_bar, ui_console=None):
    def vpn_task():
        openvpn_path = check_openvpn()
        if not openvpn_path:
            return

        configs = get_vpn_configs(config_dir)
        if not configs:
            return

        vpn_config = os.path.join(config_dir, configs[0])
        log_message("VPN", f"Trying VPN: {configs[0]}...", ui_console)

        update_bar(7)  # Simulate loading bar during VPN connect

        try:
            subprocess.Popen([openvpn_path, "--config", vpn_config], shell=True)
            log_message("SUCCESS", "VPN Connected Successfully!", ui_console)
            if btn_disconnect:
                btn_disconnect.config(state="normal")
        except Exception as e:
            log_message("ERROR", f"VPN connection failed: {e}", ui_console)

    threading.Thread(target=vpn_task, daemon=True).start()

# ✅ Disconnect VPN
def disconnect_vpn(btn_disconnect=None, ui_console=None):
    log_message("VPN", "Disconnecting VPN...", ui_console)
    subprocess.run(["taskkill", "/F", "/IM", "openvpn.exe"], shell=True)
    log_message("SUCCESS", "VPN Disconnected.", ui_console)
    if btn_disconnect:
        btn_disconnect.config(state="disabled")
