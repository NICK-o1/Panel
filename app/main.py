import tkinter as tk
from tkinter import ttk
import json
import os

from sidebar import Sidebar
from system_info import SystemInfoPanel
from buttons import ControlButtons
from theme import ThemeManager


class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Dashboard")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e1e1e")

        # Load theme
        self.theme = ThemeManager("config.json")
        self.theme.apply_root_theme(self.root)

        # Sidebar
        self.sidebar = Sidebar(
            root=self.root,
            theme=self.theme,
            width=self.theme.sidebar_width,
            animation_speed=12,
        )

        # Top bar with sidebar toggle
        self.top_bar = tk.Frame(
            self.root,
            bg=self.theme.bg,
            height=50
        )
        self.top_bar.pack(fill="x", side="top")

        self.menu_button = tk.Button(
            self.top_bar,
            text="☰",
            font=("Segoe UI Emoji", 18),
            bg=self.theme.button_bg,
            fg=self.theme.text,
            bd=0,
            activebackground=self.theme.accent,
            command=self.sidebar.toggle
        )
        self.menu_button.pack(side="left", padx=10, pady=5)

        # Main content frame
        self.content_frame = tk.Frame(self.root, bg=self.theme.bg)
        self.content_frame.pack(fill="both", expand=True)

        # System info panel (left side)
        self.system_info_panel = SystemInfoPanel(
            parent=self.content_frame,
            theme=self.theme
        )
        self.system_info_panel.frame.pack(
            side="left",
            fill="y",
            padx=20,
            pady=20
        )

        # Control buttons (right side)
        self.buttons_panel = ControlButtons(
            parent=self.content_frame,
            theme=self.theme
        )
        self.buttons_panel.frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()