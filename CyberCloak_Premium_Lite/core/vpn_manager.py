import subprocess
import threading
import os
from utils.logger import Logger
from utils.paths import CONFIG_DIR, COMMON_PATHS


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

            for line in process.stdout:
                cleaned_line = line.strip()

                if len(cleaned_line) > 20 and cleaned_line[4] == '-' and cleaned_line[7] == '-' and cleaned_line[13] == ' ':
                    parts = cleaned_line.split(' ')
                    if len(parts) > 2:
                        cleaned_line = ' '.join(parts[2:])

                if cleaned_line:
                    logger.log("VPN", cleaned_line)

            process.wait()
            update_progress(100)
            logger.log("SUCCESS", "VPN Connected Successfully!")

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