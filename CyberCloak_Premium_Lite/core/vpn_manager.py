import subprocess
import threading
from utils.paths import COMMON_PATHS
from utils.logger import Logger

def connect_vpn(logger: Logger, show_progress, disconnect_button):

    def update_progress(steps):
        show_progress(steps)

    def run_vpn_connection():
        vpn_exe_path = None
        for path in COMMON_PATHS:
            if subprocess.call(["where", "openvpn"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
                vpn_exe_path = path
                break

        if vpn_exe_path is None:
            logger.log("ERROR", "No OpenVPN executable found.")
            update_progress(0)
            return

        command = [vpn_exe_path, "--config", "config/vpn_config.ovpn"] 

        try:
            logger.log("INFO", "Starting VPN connection...")
            update_progress(1)

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            for line in process.stdout:
                logger.log("INFO", line.strip()) 

            process.wait() 
            update_progress(100)

            logger.log("INFO", "VPN connected successfully.")
            disconnect_button.config(state="normal") 

        except Exception as e:
            logger.log("ERROR", f"Error during VPN connection: {str(e)}")
            update_progress(0)
            disconnect_button.config(state="disabled")

    threading.Thread(target=run_vpn_connection, daemon=True).start()


def disconnect_vpn(logger: Logger, disconnect_button):
    """Disconnect VPN using OpenVPN and reset button state"""
    try:
        logger.log("INFO", "Disconnecting VPN...")
        command = ["openvpn", "--config", "config/vpn_config.ovpn", "--disconnect"]

        subprocess.call(command)

        logger.log("INFO", "VPN disconnected successfully.")
        disconnect_button.config(state="disabled") 

    except Exception as e:
        logger.log("ERROR", f"Error during VPN disconnection: {str(e)}")
