import tkinter as tk
from tkinter import scrolledtext, ttk

class CyberCloakPremiumLiteUI:
    def __init__(self, root, handlers):
        self.root = root
        self.handlers = handlers
        self.local_ip = tk.StringVar(value="Fetching...")
        self.public_ip = tk.StringVar(value="Fetching...")

        self._setup_window()
        self._build_ip_display()
        self._build_buttons()
        self._build_progress_bar()
        self._build_log_console()

        if self.handlers.get("refresh_ips"):
            self.handlers["refresh_ips"]()

    def _setup_window(self):
        self.root.title("Cyber Cloak Premium Lite")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

    def _build_ip_display(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Local IP:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(frame, width=25, textvariable=self.local_ip, state="readonly").grid(row=0, column=1)
        tk.Button(frame, text="Refresh", command=self.handlers["refresh_ips"]).grid(row=0, column=2, padx=5)

        tk.Label(frame, text="Public IP:", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(frame, width=25, textvariable=self.public_ip, state="readonly").grid(row=1, column=1)

    def _build_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Scan Ports", width=15, command=self.handlers["scan_ports"]).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Vuln Check", width=15, command=self.handlers["scan_vulns"]).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Connect VPN", width=15, command=self.handlers["connect_vpn"]).grid(row=1, column=0, padx=5)

        self.disconnect_btn = tk.Button(frame, text="Disconnect VPN", width=15, command=self.handlers["disconnect_vpn"])
        self.disconnect_btn.grid(row=1, column=1, padx=5)
        self.disconnect_btn.config(state="disabled")

    def _build_progress_bar(self):
        self.progress = ttk.Progressbar(self.root, mode="determinate", length=500)
        self.progress.pack(pady=10)
        self.progress.pack_forget()

    def _build_log_console(self):
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.log_console = scrolledtext.ScrolledText(frame, height=10, wrap="word", font=("Courier", 9))
        self.log_console.pack(fill="both", expand=True)
        self.log_console.config(state="disabled")

    def set_ip_info(self, local, public):
        self.local_ip.set(local)
        self.public_ip.set(public)

    def toggle_disconnect(self, enable):
        self.disconnect_btn.config(state="normal" if enable else "disabled")

    def show_progress(self, duration):
        self.progress.pack()
        self.progress["value"] = 0
        steps = 100
        interval = duration / steps

        def step(i=0):
            if i <= steps:
                self.progress["value"] = i
                self.root.after(int(interval * 1000), step, i + 1)
            else:
                self.progress.pack_forget()

        step()

    def log(self, category, message):
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"{timestamp} [{category.upper()}] {message}\n"

        self.log_console.config(state="normal")
        self.log_console.insert("end", entry)
        self.log_console.see("end")
        self.log_console.config(state="disabled")
