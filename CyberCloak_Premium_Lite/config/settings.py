import os

# ===== Base App Folder =====
APP_DIR = r"C:\Users\ROKESH's-PC\OurVPN"

# ===== Sub-directories =====
CONFIG_DIR = os.path.join(APP_DIR, "config")
LOG_DIR = os.path.join(APP_DIR, "logs")

# ===== Files =====
LOG_FILE = os.path.join(LOG_DIR, "vpn_log.txt")

# ===== Tools =====
NMAP_PATH = r"C:\nmap\nmap.exe"  # Make sure nmap.exe exists here
OPENVPN_PATHS = [
    r"C:\Program Files\OpenVPN\bin\openvpn.exe",
    r"C:\Program Files (x86)\OpenVPN\bin\openvpn.exe"
]
