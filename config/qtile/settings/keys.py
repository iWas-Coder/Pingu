# Pingu's Qtile Settings (keys) Config File
# (c) iWas. All rights reserved.
# https://github.com/iWas-Coder/Pingu

from libqtile.config import Key
from libqtile.command import lazy


# === Global variables === #
mod = "mod4"
alt = "mod1"
terminal = "kitty"
browser = "chromium"
app_launch = "rofi -show drun"
app_switch = "rofi -show"
screenshot = "flameshot gui"

# === Keys === #
keys = [
    # App menu (rofi)
    Key([mod], "m", lazy.spawn(app_launch)),
    Key([mod, 'shift'], "m", lazy.spawn(app_switch)),
    
    # Browser (chromium)
    Key([mod], "b", lazy.spawn(browser)),
    
    # Screenshots (flameshot)
    Key([mod, "shift"], "s", lazy.spawn(screenshot)),
    
    # New window (terminal)
    Key([mod], "Return", lazy.spawn(terminal)),
    
    # Moving between windows
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    
    # Moving windows between each other
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    
    # Resize window
    Key([mod, alt], "Right", lazy.layout.shrink()),
    Key([mod, alt], "Left", lazy.layout.grow()),
    
    # Toggle floating window
    Key([mod], "f", lazy.window.toggle_floating()),
    
    # Moving between monitors/screens
    Key([mod], "Tab", lazy.next_screen()),
    
    # Close window
    Key([mod], "w", lazy.window.kill()),
]
