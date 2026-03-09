import json


class ThemeManager:
    def __init__(self, config_path):
        self.config_path = config_path

        # Load theme from config.json
        self.load_theme()

    # ---------------------------------------------------------
    # Load theme settings
    # ---------------------------------------------------------
    def load_theme(self):
        try:
            with open(self.config_path, "r") as f:
                cfg = json.load(f)
        except:
            cfg = {}

        # Colors
        self.bg = cfg.get("background", "#1e1e1e")
        self.text = cfg.get("text", "#ffffff")
        self.button_bg = cfg.get("button_bg", "#2d2d2d")
        self.accent = cfg.get("accent", "#3a86ff")
        self.sidebar_bg = cfg.get("sidebar_bg", "#252525")

        # Sizes
        self.sidebar_width = cfg.get("sidebar_width", 260)
        self.button_height = cfg.get("button_height", 48)
        self.icon_size = cfg.get("icon_size", 22)
        self.font_size = cfg.get("font_size", 13)

    # ---------------------------------------------------------
    # Apply theme to root window
    # ---------------------------------------------------------
    def apply_root_theme(self, root):
        root.configure(bg=self.bg)