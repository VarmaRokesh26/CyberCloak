import socket
import subprocess

# ✅ Get Local IP Address
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "Unavailable"

# ✅ Get Public IP Address using ipify
def get_public_ip():
    try:
        return subprocess.getoutput("curl -s https://api64.ipify.org")
    except Exception:
        return "Unavailable"
