import tkinter as tk
import os
import subprocess
import shutil


class ControlButtons:
    def __init__(self, parent, theme):
        self.theme = theme

        self.frame = tk.Frame(parent, bg=self.theme.bg)

        # 3-column layout
        self.columns = [
            tk.Frame(self.frame, bg=self.theme.bg),
            tk.Frame(self.frame, bg=self.theme.bg),
            tk.Frame(self.frame, bg=self.theme.bg)
        ]

        for col in self.columns:
            col.pack(side="left", expand=True, fill="both", padx=10)

        # Build button groups
        self.build_system_tools()
        self.build_windows_settings()
        self.build_power_controls()

    # ---------------------------------------------------------
    # Button Builder
    # ---------------------------------------------------------
    def make_button(self, parent, icon, text, command):
        btn = tk.Button(
            parent,
            text=f"{icon}  {text}",
            font=("Segoe UI Emoji", 13),
            bg=self.theme.button_bg,
            fg=self.theme.text,
            activebackground=self.theme.accent,
            activeforeground="white",
            bd=0,
            relief="flat",
            padx=10,
            pady=10,
            anchor="w",
            command=command
        )
        btn.pack(fill="x", pady=6)
        return btn

    # ---------------------------------------------------------
    # Column 1 — System Tools
    # ---------------------------------------------------------
    def build_system_tools(self):
        col = self.columns[0]

        tk.Label(
            col,
            text="System Tools",
            font=("Segoe UI", 14, "bold"),
            bg=self.theme.bg,
            fg=self.theme.text
        ).pack(anchor="w", pady=(0, 10))

        self.make_button(col, "🖥️", "Task Manager", self.open_task_manager)
        self.make_button(col, "💾", "Storage Settings", self.open_storage)
        self.make_button(col, "📡", "Network Settings", self.open_network)
        self.make_button(col, "🧹", "Clear Temp Files", self.clear_temp_files)

    # ---------------------------------------------------------
    # Column 2 — Windows Settings
    # ---------------------------------------------------------
    def build_windows_settings(self):
        col = self.columns[1]

        tk.Label(
            col,
            text="Windows Settings",
            font=("Segoe UI", 14, "bold"),
            bg=self.theme.bg,
            fg=self.theme.text
        ).pack(anchor="w", pady=(0, 10))

        self.make_button(col, "🔄", "Windows Update", self.open_update)
        self.make_button(col, "💡", "Display Settings", self.open_display)
        self.make_button(col, "🔊", "Sound Settings", self.open_sound)
        self.make_button(col, "📶", "Bluetooth Settings", self.open_bluetooth)

    # ---------------------------------------------------------
    # Column 3 — Power Controls
    # ---------------------------------------------------------
    def build_power_controls(self):
        col = self.columns[2]

        tk.Label(
            col,
            text="Power Controls",
            font=("Segoe UI", 14, "bold"),
            bg=self.theme.bg,
            fg=self.theme.text
        ).pack(anchor="w", pady=(0, 10))

        self.make_button(col, "🔌", "Restart", self.restart_pc)
        self.make_button(col, "📴", "Shutdown", self.shutdown_pc)
        self.make_button(col, "🛠️", "Safe Mode Reboot", self.safe_mode_reboot)
        self.make_button(col, "🔋", "Power Settings", self.open_power_settings)

    # ---------------------------------------------------------
    # Button Actions
    # ---------------------------------------------------------
    def open_task_manager(self):
        os.system("start taskmgr")

    def open_storage(self):
        os.system("start ms-settings:storagesense")

    def open_network(self):
        os.system("start ms-settings:network")

    def open_update(self):
        os.system("start ms-settings:windowsupdate")

    def open_display(self):
        os.system("start ms-settings:display")

    def open_sound(self):
        os.system("start ms-settings:sound")

    def open_bluetooth(self):
        os.system("start ms-settings:bluetooth")

    def open_power_settings(self):
        os.system("start ms-settings:powersleep")

    def restart_pc(self):
        os.system("shutdown /r /t 0")

    def shutdown_pc(self):
        os.system("shutdown /s /t 0")

    def safe_mode_reboot(self):
        os.system("bcdedit /set {current} safeboot minimal")
        os.system("shutdown /r /t 0")

    def clear_temp_files(self):
        temp = os.environ.get("TEMP")
        if temp and os.path.exists(temp):
            shutil.rmtree(temp, ignore_errors=True)
            os.makedirs(temp, exist_ok=True)