import tkinter as tk


class Sidebar:
    def __init__(self, root, theme, width=260, animation_speed=12):
        self.root = root
        self.theme = theme
        self.width = width
        self.animation_speed = animation_speed

        self.is_open = True
        self.current_width = width

        # Sidebar frame
        self.frame = tk.Frame(
            self.root,
            bg=self.theme.sidebar_bg,
            width=self.width,
            height=self.root.winfo_height()
        )
        self.frame.place(x=0, y=50)

        # Build sidebar content
        self.build_sidebar()

    # ---------------------------------------------------------
    # Sidebar UI
    # ---------------------------------------------------------
    def build_sidebar(self):
        # Title
        title = tk.Label(
            self.frame,
            text="☰  Dashboard",
            font=("Segoe UI Emoji", 16, "bold"),
            bg=self.theme.sidebar_bg,
            fg=self.theme.text
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))

        self.add_divider()

        # Sections
        self.add_section("🖥  System Information")
        self.add_section("💾  Storage Devices")
        self.add_section("📡  Network Status")
        self.add_section("🔊  Sound Settings")

        self.add_divider()

        self.add_section("🔌  Power Controls")
        self.add_section("🧹  Cleanup Tools")

    def add_section(self, text):
        label = tk.Label(
            self.frame,
            text=text,
            font=("Segoe UI Emoji", 13),
            bg=self.theme.sidebar_bg,
            fg=self.theme.text
        )
        label.pack(anchor="w", padx=25, pady=6)

    def add_divider(self):
        divider = tk.Frame(
            self.frame,
            bg=self.theme.button_bg,
            height=2
        )
        divider.pack(fill="x", padx=15, pady=10)

    # ---------------------------------------------------------
    # Sidebar Animation
    # ---------------------------------------------------------
    def toggle(self):
        if self.is_open:
            self.slide_close()
        else:
            self.slide_open()

    def slide_close(self):
        if self.current_width > 0:
            self.current_width -= self.animation_speed
            if self.current_width < 0:
                self.current_width = 0

            self.frame.config(width=self.current_width)
            self.frame.place(x=0, y=50)

            self.root.after(10, self.slide_close)
        else:
            self.is_open = False

    def slide_open(self):
        if self.current_width < self.width:
            self.current_width += self.animation_speed
            if self.current_width > self.width:
                self.current_width = self.width

            self.frame.config(width=self.current_width)
            self.frame.place(x=0, y=50)

            self.root.after(10, self.slide_open)
        else:
            self.is_open = True