import socket
import subprocess
import os
from utils.paths import NMAP_PATH

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unavailable"

def get_public_ip():
    try:
        return subprocess.getoutput("curl -s https://api64.ipify.org")
    except:
        return "Unavailable"

def check_nmap():
    """Checks if the custom Nmap path exists"""
    return os.path.exists(NMAP_PATH)
