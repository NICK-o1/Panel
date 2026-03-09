import tkinter as tk
import psutil
import platform
import socket
import uuid
import requests
import subprocess
import winreg


class SystemInfoPanel:
    def __init__(self, parent, theme):
        self.theme = theme

        self.frame = tk.Frame(
            parent,
            bg=self.theme.bg,
            width=300
        )

        title = tk.Label(
            self.frame,
            text="🖥️ System Information",
            font=("Segoe UI Emoji", 16, "bold"),
            bg=self.theme.bg,
            fg=self.theme.text
        )
        title.pack(anchor="w", pady=(0, 10))

        self.info_box = tk.Frame(self.frame, bg=self.theme.bg)
        self.info_box.pack(anchor="w")

        # Store labels for hover reveal
        self.hidden_labels = {}

        self.populate_info()

    # ---------------------------------------------------------
    # Collect System Info
    # ---------------------------------------------------------
    def populate_info(self):
        local_ip = self.get_local_ip()
        public_ip = self.get_public_ip()
        mac_addr = self.get_mac_address()

        info = {
            "CPU": self.get_cpu_name(),
            "Cores": psutil.cpu_count(logical=False),
            "Threads": psutil.cpu_count(logical=True),
            "GPU": self.get_gpu_name(),
            "RAM": f"{round(psutil.virtual_memory().total / (1024**3), 1)} GB",

            # Hidden fields
            "Local IP": local_ip,
            "Public IP": public_ip,
            "MAC Address": mac_addr,

            "Wi-Fi Signal": self.get_wifi_signal(),
        }

        # Normal info rows
        for key, value in info.items():
            if key in ["Local IP", "Public IP", "MAC Address"]:
                self.add_hidden_row(key, value)
            else:
                self.add_info_row(key, value)

        # Add storage section
        self.add_storage_section()

    # ---------------------------------------------------------
    # Normal Info Row
    # ---------------------------------------------------------
    def add_info_row(self, label, value):
        row = tk.Frame(self.info_box, bg=self.theme.bg)
        row.pack(anchor="w", pady=2)

        tk.Label(
            row,
            text=f"{label}: ",
            font=("Segoe UI", 11, "bold"),
            bg=self.theme.bg,
            fg=self.theme.text
        ).pack(side="left")

        tk.Label(
            row,
            text=value,
            font=("Segoe UI", 11),
            bg=self.theme.bg,
            fg=self.theme.text
        ).pack(side="left")

    # ---------------------------------------------------------
    # Hidden Row (Hover to Reveal)
    # ---------------------------------------------------------
    def add_hidden_row(self, label, real_value):
        row = tk.Frame(self.info_box, bg=self.theme.bg)
        row.pack(anchor="w", pady=2)

        tk.Label(
            row,
            text=f"{label}: ",
            font=("Segoe UI", 11, "bold"),
            bg=self.theme.bg,
            fg=self.theme.text
        ).pack(side="left")

        value_label = tk.Label(
            row,
            text="Hidden",
            font=("Segoe UI", 11),
            bg=self.theme.bg,
            fg=self.theme.text
        )
        value_label.pack(side="left")

        # Store real value for hover
        self.hidden_labels[value_label] = real_value

        # Bind hover events
        value_label.bind("<Enter>", self.reveal_value)
        value_label.bind("<Leave>", self.hide_value)

    def reveal_value(self, event):
        label = event.widget
        label.config(text=self.hidden_labels[label])

    def hide_value(self, event):
        label = event.widget
        label.config(text="Hidden")

    # ---------------------------------------------------------
    # Storage Section
    # ---------------------------------------------------------
    def add_storage_section(self):
        section_title = tk.Label(
            self.info_box,
            text="💾 Storage Devices",
            font=("Segoe UI Emoji", 14, "bold"),
            bg=self.theme.bg,
            fg=self.theme.text
        )
        section_title.pack(anchor="w", pady=(10, 5))

        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                total = round(usage.total / (1024**3), 1)
                used = round(usage.used / (1024**3), 1)
                free = round(usage.free / (1024**3), 1)

                row = tk.Frame(self.info_box, bg=self.theme.bg)
                row.pack(anchor="w", pady=2)

                tk.Label(
                    row,
                    text=f"{part.device} ",
                    font=("Segoe UI", 11, "bold"),
                    bg=self.theme.bg,
                    fg=self.theme.text
                ).pack(side="left")

                tk.Label(
                    row,
                    text=f"{used} / {total} GB (Free: {free} GB)",
                    font=("Segoe UI", 11),
                    bg=self.theme.bg,
                    fg=self.theme.text
                ).pack(side="left")

            except PermissionError:
                continue

    # ---------------------------------------------------------
    # System Info Functions
    # ---------------------------------------------------------
    def get_cpu_name(self):
        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
            )
            cpu_name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
            return cpu_name.strip()
        except:
            return "Unknown CPU"

    def get_gpu_name(self):
        try:
            output = subprocess.check_output(
                "wmic path win32_VideoController get name",
                shell=True
            ).decode().split("\n")[1].strip()
            return output if output else "Unknown"
        except:
            return "Unknown"

    def get_local_ip(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except:
            return "Unknown"

    def get_public_ip(self):
        try:
            return requests.get("https://api.ipify.org").text
        except:
            return "Unknown"

    def get_mac_address(self):
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "Unknown"

    def get_wifi_signal(self):
        try:
            output = subprocess.check_output(
                "netsh wlan show interfaces",
                shell=True
            ).decode()

            for line in output.split("\n"):
                if "Signal" in line:
                    return line.split(":")[1].strip()
            return "N/A"
        except:
            return "N/A"