import os

APP_DIR = r"C:\Users\ROKESH's-PC\OurVPN"
CONFIG_DIR = os.path.join(APP_DIR, "config")
LOG_DIR = os.path.join(APP_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "vpn_log.txt")

COMMON_OPENVPN_PATHS = [
    r"C:\Program Files\OpenVPN\bin\openvpn.exe",
    r"C:\Program Files (x86)\OpenVPN\bin\openvpn.exe"
]
