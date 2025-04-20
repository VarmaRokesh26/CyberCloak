import os
import tkinter as tk
import threading
from tkinter import scrolledtext, ttk

class CyberCloakPremiumLiteUI:
    def __init__(self, root, handlers):
        self.root = root
        self.handlers = handlers
        self.local_ip = tk.StringVar(value="Fetching...")
        self.public_ip = tk.StringVar(value="Fetching...")

        self._setup_window()
        self._build_ip_display()
        self._build_progress_bar()
        self._build_log_console()

        if "refresh_ips" in self.handlers:
            self.handlers["refresh_ips"]()

    def _setup_window(self):
        self.root.title("Cyber Cloak Premium Lite")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "..", "assets", "cc_icon.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

    def _build_ip_display(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Local IP:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(frame, width=25, textvariable=self.local_ip, state="readonly").grid(row=0, column=1)
        tk.Button(frame, text="Refresh", command=lambda: self.handlers["refresh_ips"]()).grid(row=0, column=2, padx=5)

        tk.Label(frame, text="Public IP:", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(frame, width=25, textvariable=self.public_ip, state="readonly").grid(row=1, column=1)

    def _build_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Scan Ports", width=15, command=self.handlers.get("scan_ports")).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Vuln Check", width=15, command=self.handlers.get("scan_vulns")).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Connect VPN", width=15, command=self.handlers.get("connect_vpn")).grid(row=1, column=0, padx=5)

        self.disconnect_button = tk.Button(frame, text="Disconnect VPN", width=15, state="disabled", command=self.handlers.get("disconnect_vpn"))
        self.disconnect_button.grid(row=1, column=1, padx=5)

    def _build_progress_bar(self):
        style = ttk.Style(self.root)
        style.theme_use('default')
        style.configure("blue.Horizontal.TProgressbar", troughcolor="#e0e0e0", background="#2196F3", thickness=10)

        self.progress = ttk.Progressbar(
            self.root,
            style="blue.Horizontal.TProgressbar",
            orient="horizontal",
            mode="determinate",
            length=500
        )
        self.progress.pack(pady=10)
        self.progress.pack_forget()

    def _build_log_console(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=20, fill="both", expand=True)

        self.log_console = tk.Text(frame, height=10, wrap="none", font=("Courier", 9), bg="black", fg="white")

        x_scroll = tk.Scrollbar(frame, orient="horizontal", command=self.log_console.xview)
        y_scroll = tk.Scrollbar(frame, orient="vertical", command=self.log_console.yview)

        self.log_console.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        self.log_console.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.log_console.config(state="disabled")

    def show_progress(self, duration_sec):
        self.progress.pack()
        self.progress["value"] = 0
        steps = 50
        interval = duration_sec / steps

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
        entry = f"{timestamp} [{category}] {message}\n"

        self.log_console.config(state="normal")
        self.log_console.insert("end", entry)
        self.log_console.see("end")
        self.log_console.config(state="disabled")

    def set_ip_info(self, local_ip, public_ip):
        self.local_ip.set(local_ip)
        self.public_ip.set(public_ip)

    def set_disconnect_button_state(self, enabled):
        self.disconnect_button.config(state="normal" if enabled else "disabled")

    def set_handlers(self, handlers):
        self.handlers = handlers
        self._build_buttons()

    def run_with_progress(self, task_func, *args, **kwargs):
        def thread_wrapper():
            try:
                self.show_progress(7)
                task_func(*args, **kwargs)
            finally:
                self.show_progress(0)

        threading.Thread(target=thread_wrapper, daemon=True).start()
