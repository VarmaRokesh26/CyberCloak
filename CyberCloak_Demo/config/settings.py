import os

APP_DIR = r"C:\Users\ROKESH's-PC\OurVPN"
CONFIG_DIR = os.path.join(APP_DIR, "config")
LOG_DIR = os.path.join(APP_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "vpn_log.txt")

COMMON_OPENVPN_PATHS = [
    r"C:\Program Files\OpenVPN\bin\openvpn.exe",
    r"C:\Program Files (x86)\OpenVPN\bin\openvpn.exe"
]

COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 135, 139,
    143, 443, 445, 993, 995, 1723, 3306,
    3389, 5900, 8080
]