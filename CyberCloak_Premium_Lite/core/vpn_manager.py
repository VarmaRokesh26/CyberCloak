import subprocess
import threading
import os
from utils.logger import Logger
from utils.paths import CONFIG_DIR, COMMON_PATHS
import re


def get_vpn_config_file():
    config_files = [f for f in os.listdir(CONFIG_DIR) if f.endswith(".ovpn")]
    if not config_files:
        return None

    config_files.sort()
    return os.path.join(CONFIG_DIR, config_files[0])


def connect_vpn(logger: Logger, show_progress, disconnect_button):
    def update_progress(steps):
        show_progress(steps)

    def run_vpn_connection():
        vpn_config_file = get_vpn_config_file()

        if vpn_config_file is None:
            logger.log("ERROR", "No OpenVPN config file found.")
            update_progress(0)
            return

        openvpn_executable = None
        for path in COMMON_PATHS:
            if os.path.exists(path):
                openvpn_executable = path
                break

        if openvpn_executable is None:
            logger.log("ERROR", "OpenVPN executable not found in specified paths.")
            update_progress(0)
            return

        command = [openvpn_executable, "--config", vpn_config_file]

        try:
            logger.log("INFO", f"Starting VPN connection with {vpn_config_file}...")
            update_progress(1)

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            disconnect_button.config(state="normal")
            connected_flag = False

            for line in process.stdout:
                cleaned_line = line.strip()

                display_line = re.sub(r'^\S+\s+\S+\s+', '', cleaned_line)
                if display_line:
                    logger.log("VPN", display_line)

                if "Protocol options: protocol-flags cc-exit tls-ekm dyn-tls-crypt" in display_line:
                    logger.log("SUCCESS", "VPN Connected Successfully!")
                    update_progress(100)
                    connected_flag = True

            process.wait()

            if not connected_flag:
                logger.log("ERROR", "VPN process ended without a successful connection.")
                update_progress(0)
                disconnect_button.config(state="disabled")

        except Exception as e:
            logger.log("ERROR", f"Error during VPN connection: {str(e)}")
            update_progress(0)
            disconnect_button.config(state="disabled")

    threading.Thread(target=run_vpn_connection, daemon=True).start()



def disconnect_vpn(logger: Logger, disconnect_button):
    try:
        logger.log("VPN", "Disconnecting VPN...")

        process = subprocess.Popen(
            ["taskkill", "/F", "/IM", "openvpn.exe"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            text=True
        )

        for line in process.stdout:
            if line.strip():
                logger.log("VPN", line.strip())

        process.wait()

        logger.log("SUCCESS", "VPN Disconnected.")
        disconnect_button.config(state="disabled")

    except Exception as e:
        logger.log("ERROR", f"Error during VPN disconnection: {str(e)}")