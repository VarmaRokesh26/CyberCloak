import socket
import subprocess

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