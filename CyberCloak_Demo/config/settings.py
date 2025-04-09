import os

# 📌 Base Application Directory
APP_DIR = os.path.expandvars(r"C:\Users\ROKESH's-PC\OurVPN")

# 📌 Folder Paths
CONFIG_DIR = os.path.join(APP_DIR, "config")
LOG_DIR = os.path.join(APP_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "vpn_log.txt")

# 📌 Common OpenVPN installation paths
COMMON_PATHS = [
    r"C:\Program Files\OpenVPN\bin\openvpn.exe",
    r"C:\Program Files (x86)\OpenVPN\bin\openvpn.exe"
]

# 📌 Port Range for Scanner
PORT_SCAN_RANGE = range(1, 10000)

# 🧠 Ensure all folders exist when settings is imported
os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
